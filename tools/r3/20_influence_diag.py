"""
R3 Phase 2 — Influence diagnostics for canonical M8.

Reviewer #4: only 3% of firms have FSTS > 50%; significance in Table 4
(DAI marginal effects) appears only at FSTS=70 and FSTS=100 — the
thinnest portion of empirical support. Demand: Cook's distance, DFBETA,
and high-leverage observations identification.

This script computes:
  - Cook's distance for every observation
  - DFBETA for the three coefficients reviewer flagged:
      fsts_c2, fsts_c_DAI, fsts_c2_DAI
  - Hat values (leverage)
  - Top-20 most influential observations sorted by Cook's D

Outputs:
  outputs/r3/audit/influence_top20.csv
  outputs/r3/audit/influence_summary.json
  outputs/r3/figures/CooksD.png
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import OLSInfluence
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parents[2]
DTA = REPO / "data" / "raw" / "Singapore2023fulldata.dta"
AUDIT_DIR = REPO / "outputs" / "r3" / "audit"
FIG_DIR = REPO / "outputs" / "r3" / "figures"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)


def load_frame():
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
    return df


def fit_m8(df):
    core = ["ln_lp", "fsts_c", "fsts_c2", "TCI", "DAI",
            "fsts_c_DAI", "fsts_c2_DAI",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    mask = df[core].notna().all(axis=1)
    formula = (
        "ln_lp ~ fsts_c + fsts_c2 + TCI + DAI"
        " + fsts_c_DAI + fsts_c2_DAI"
        " + ln_empl + firm_age + foreign + C(broad_sector)"
    )
    # Use non-robust SE here because OLSInfluence uses classical residuals.
    model = smf.ols(formula, data=df[mask]).fit()
    return model, mask


def main():
    print("=" * 72)
    print("R3 Phase 2 — Influence diagnostics for canonical M8")
    print("=" * 72)

    df = load_frame()
    model, mask = fit_m8(df)
    n = int(mask.sum())
    k = len(model.params)
    print(f"\nM8 fit: N = {n}, k = {k}")
    print(f"Cook's D thresholds: 4/n = {4/n:.4f}, 4/(n-k) = {4/(n-k):.4f}")
    print(f"Hat-value cutoff (2k/n): {2*k/n:.4f}")

    inf = OLSInfluence(model)
    cooks_d = inf.cooks_distance[0]
    hat = inf.hat_matrix_diag
    dfb = inf.dfbetas  # ndarray (n, k)

    # Map column index to term name
    term_idx = {t: i for i, t in enumerate(model.params.index)}
    flagged_terms = ["fsts_c2", "fsts_c_DAI", "fsts_c2_DAI"]

    df_sub = df[mask].reset_index(drop=False).rename(columns={"index": "row_idx"})
    df_sub["cooks_d"] = cooks_d
    df_sub["hat"] = hat
    for term in flagged_terms:
        if term in term_idx:
            df_sub[f"dfb_{term}"] = dfb[:, term_idx[term]]

    # Top-20 by Cook's D
    top20 = df_sub.nlargest(20, "cooks_d")[
        ["row_idx", "fsts", "ln_lp", "TCI", "DAI",
         "ln_empl", "firm_age", "foreign", "cooks_d", "hat"]
        + [f"dfb_{t}" for t in flagged_terms if f"dfb_{t}" in df_sub.columns]
    ]
    out_csv = AUDIT_DIR / "influence_top20.csv"
    top20.to_csv(out_csv, index=False)
    print(f"\nTop-20 most influential observations:")
    cols = ["row_idx", "fsts", "ln_lp", "TCI", "DAI", "cooks_d", "hat"]
    print(top20[cols].to_string(index=False))

    # Summary stats
    n_above_4n = int((cooks_d > 4 / n).sum())
    n_above_4nk = int((cooks_d > 4 / (n - k)).sum())
    n_high_hat = int((hat > 2 * k / n).sum())
    n_fsts_gt_50 = int(((df_sub["fsts"] > 0.5)).sum())
    n_fsts_gt_70 = int(((df_sub["fsts"] > 0.7)).sum())
    fsts_top_cooksD = top20["fsts"].mean()
    summary = {
        "n": n,
        "k_params": k,
        "n_obs_cooksD_gt_4_over_n": n_above_4n,
        "n_obs_cooksD_gt_4_over_n_minus_k": n_above_4nk,
        "n_obs_high_leverage_hat_gt_2k_over_n": n_high_hat,
        "n_firms_FSTS_gt_50pct": n_fsts_gt_50,
        "n_firms_FSTS_gt_70pct": n_fsts_gt_70,
        "mean_FSTS_in_top20_cooksD": float(fsts_top_cooksD),
        "max_cooksD": float(cooks_d.max()),
        "median_cooksD": float(np.median(cooks_d)),
    }
    summary_path = AUDIT_DIR / "influence_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2))
    print(f"\nWrote: {summary_path}")
    print(json.dumps(summary, indent=2))

    # Plot Cook's D
    fig, ax = plt.subplots(figsize=(9, 5))
    fsts_pct = df_sub["fsts"].values * 100
    ax.scatter(fsts_pct, cooks_d, alpha=0.45, s=18, color="steelblue",
               label=f"All obs (N={n})")
    threshold = 4 / n
    ax.axhline(threshold, color="C3", lw=1, ls="--",
               label=f"4/n = {threshold:.4f}")
    ax.axvspan(70, 100, color="lightgray", alpha=0.4,
               label="Thin support (FSTS > 70%)")
    # Highlight top-20 with bigger markers
    top_pct = top20["fsts"].values * 100
    top_cd = top20["cooks_d"].values
    ax.scatter(top_pct, top_cd, s=80, facecolor="none",
               edgecolor="C3", lw=1.5, label="Top-20 Cook's D")
    ax.set_xlabel("FSTS (%)")
    ax.set_ylabel("Cook's distance")
    ax.set_title("Influence diagnostics: Cook's D by FSTS (canonical M8)")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    out_fig = FIG_DIR / "CooksD.png"
    fig.savefig(out_fig, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote: {out_fig}")

    # Print interpretation
    print("\n" + "=" * 72)
    print("Interpretation:")
    print("=" * 72)
    pct_top20_in_thin = ((top20["fsts"] > 0.7).sum()) / 20 * 100
    print(f"  • {n_above_4n}/{n} observations exceed Cook's D = 4/n = "
          f"{threshold:.4f}.")
    print(f"  • {n_high_hat}/{n} observations have leverage hat > 2k/n.")
    print(f"  • Firms with FSTS > 70%: {n_fsts_gt_70}/{n} "
          f"({n_fsts_gt_70/n*100:.1f}%).")
    print(f"  • Among Top-20 high-Cook's-D firms: "
          f"{int((top20['fsts'] > 0.7).sum())} have FSTS > 70% "
          f"({pct_top20_in_thin:.0f}%).")
    if pct_top20_in_thin > 30:
        print("  → High-leverage observations are concentrated in the thin")
        print("    upper tail. Combined with Phase 2's LOO and trimmed-tail")
        print("    re-estimation, this strengthens the case for narrative")
        print("    caution about the upper-tail moderation pattern.")


if __name__ == "__main__":
    main()
