"""
R3 Phase 2 — Leave-one-out re-estimation of canonical M8.

For each of N=617 observations, drop it and re-fit M8. Track the
distribution of the three reviewer-flagged coefficients:
  fsts_c2 (linear/quadratic of FSTS)
  fsts_c_DAI (linear DAI moderation)
  fsts_c2_DAI (quadratic DAI moderation — the key DAI-moderation term)

Reports the LOO range, IQR, % runs significant, and identifies the
single most influential observation for each coefficient.

Outputs:
  outputs/r3/audit/loo_summary.json
  outputs/r3/figures/LOO_distribution.png
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.formula.api as smf
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parents[2]
DTA = REPO / "data" / "raw" / "Singapore2023fulldata.dta"
AUDIT_DIR = REPO / "outputs" / "r3" / "audit"
FIG_DIR = REPO / "outputs" / "r3" / "figures"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)


def load_clean():
    df, _ = pyreadstat.read_dta(str(DTA))
    for col in ["b2b", "d2", "l1", "b5", "d3c", "a4a", "a4b_v4"]:
        df[col] = df[col].where(df[col] >= 0, np.nan)
    for col in ["b8", "e6", "h1", "h8"]:
        df[col + "_yn"] = (df[col] == 1).astype(int)
    df["c22b_yn"] = (df["c22b"] == 1).astype(int)
    df["dai_drop"] = (df["k33"] < 0) & (df["k38"] < 0)
    k33_med = df.loc[df["k33"] >= 0, "k33"].median()
    k38_med = df.loc[df["k38"] >= 0, "k38"].median()
    df["k33_imp"] = df["k33"].where(df["k33"] >= 0, k33_med)
    df["k38_imp"] = df["k38"].where(df["k38"] >= 0, k38_med)
    df.loc[df["dai_drop"], ["k33_imp", "k38_imp"]] = np.nan
    df["lp"] = df["d2"] / df["l1"]
    df["ln_lp"] = np.log(df["lp"])
    lo, hi = df["ln_lp"].quantile([0.01, 0.99])
    df["ln_lp"] = df["ln_lp"].clip(lo, hi)
    df["fsts"] = df["d3c"] / 100.0
    df["fsts_c"] = df["fsts"] - df["fsts"].mean()
    df["fsts_c2"] = df["fsts_c"] ** 2
    df["ln_empl"] = np.log(df["l1"])
    df["firm_age"] = 2023 - df["b5"]
    df["foreign"] = (df["b2b"].fillna(0) >= 10).astype(int)

    def bucket(nace):
        if pd.isna(nace):
            return np.nan
        n = int(nace)
        if 10 <= n <= 33:
            return "manufacturing"
        if 41 <= n <= 43:
            return "construction"
        return "retail_services"

    df["broad_sector"] = df["a4b_v4"].apply(bucket)

    def composite(parts, name):
        zs = []
        for c in parts:
            mu, sd = df[c].mean(), df[c].std()
            zcol = c + "_z_" + name
            df[zcol] = (df[c] - mu) / sd
            zs.append(zcol)
        raw = df[zs].sum(axis=1, skipna=False) / len(parts)
        df[name] = (raw - raw.mean()) / raw.std()

    composite(["b8_yn", "e6_yn", "h1_yn", "h8_yn"], "TCI")
    composite(["c22b_yn", "k33_imp", "k38_imp"], "DAI")
    df["fsts_c_DAI"] = df["fsts_c"] * df["DAI"]
    df["fsts_c2_DAI"] = df["fsts_c2"] * df["DAI"]
    core = ["ln_lp", "fsts_c", "fsts_c2", "TCI", "DAI",
            "fsts_c_DAI", "fsts_c2_DAI",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    return df[df[core].notna().all(axis=1)].copy()


FORMULA = (
    "ln_lp ~ fsts_c + fsts_c2 + TCI + DAI"
    " + fsts_c_DAI + fsts_c2_DAI"
    " + ln_empl + firm_age + foreign + C(broad_sector)"
)
TERMS = ["fsts_c2", "fsts_c_DAI", "fsts_c2_DAI"]


def fit_one(df):
    return smf.ols(FORMULA, data=df).fit(cov_type="HC1")


def main():
    print("=" * 72)
    print("R3 Phase 2 — Leave-one-out re-estimation")
    print("=" * 72)

    df = load_clean().reset_index(drop=False).rename(columns={"index": "row_id"})
    n = len(df)
    print(f"\nClean sample: N = {n}")
    print(f"LOO loops: {n} fits")

    full = fit_one(df)
    full_vals = {t: float(full.params[t]) for t in TERMS}
    full_p = {t: float(full.pvalues[t]) for t in TERMS}
    print(f"\nFull-sample reference:")
    for t in TERMS:
        print(f"  {t:<14} = {full_vals[t]:+.4f} (p={full_p[t]:.4f})")

    rows = []
    for i in range(n):
        sub = df.drop(df.index[i])
        m = fit_one(sub)
        row = {"i_drop": int(df["row_id"].iloc[i]),
               "fsts_dropped": float(df["fsts"].iloc[i])}
        for t in TERMS:
            row[t] = float(m.params[t])
            row[f"{t}_p"] = float(m.pvalues[t])
        rows.append(row)
        if (i + 1) % 100 == 0:
            print(f"  done {i+1}/{n}")

    loo = pd.DataFrame(rows)

    summary = {"full_sample": {**full_vals, **{f"{t}_p": full_p[t] for t in TERMS}}}
    print("\n" + "=" * 72)
    print(f"{'Term':<14}{'Full':>10}{'LOO mean':>11}{'LOO min':>11}"
          f"{'LOO max':>11}{'%sig@.05':>10}")
    print("-" * 72)
    for t in TERMS:
        col = loo[t]
        col_p = loo[f"{t}_p"]
        sig_pct = (col_p < 0.05).mean() * 100
        summary[t] = {
            "full": full_vals[t],
            "loo_mean": float(col.mean()),
            "loo_median": float(col.median()),
            "loo_min": float(col.min()),
            "loo_max": float(col.max()),
            "loo_iqr_lo": float(col.quantile(0.25)),
            "loo_iqr_hi": float(col.quantile(0.75)),
            "pct_sig_05": float(sig_pct),
            "most_influential_drop_idx": int(loo.iloc[col.sub(full_vals[t]).abs().idxmax()]["i_drop"]),
            "max_abs_change": float(col.sub(full_vals[t]).abs().max()),
        }
        print(f"{t:<14}{full_vals[t]:>+10.4f}{col.mean():>+11.4f}"
              f"{col.min():>+11.4f}{col.max():>+11.4f}"
              f"{sig_pct:>9.1f}%")

    out_json = AUDIT_DIR / "loo_summary.json"
    out_json.write_text(json.dumps(summary, indent=2))
    print(f"\nWrote: {out_json}")

    # Plot LOO histograms
    fig, axes = plt.subplots(1, 3, figsize=(13, 4))
    for ax, t in zip(axes, TERMS):
        col = loo[t]
        ax.hist(col, bins=40, color="steelblue", alpha=0.75, edgecolor="white")
        ax.axvline(full_vals[t], color="C3", lw=2,
                   label=f"Full = {full_vals[t]:+.3f}")
        ax.axvline(col.mean(), color="C2", lw=1.5, ls="--",
                   label=f"LOO mean = {col.mean():+.3f}")
        ax.set_title(f"LOO distribution of β({t})")
        ax.set_xlabel("Coefficient")
        ax.set_ylabel("Count of LOO fits")
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)
    fig.tight_layout()
    out_fig = FIG_DIR / "LOO_distribution.png"
    fig.savefig(out_fig, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote: {out_fig}")


if __name__ == "__main__":
    main()
