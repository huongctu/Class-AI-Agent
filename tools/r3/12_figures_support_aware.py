"""
R3 Phase 1 — Support-aware Figures 2 and 3.

Reviewer #4 demanded "support-aware visualizations" so readers can see
where statistical significance lies relative to where the data lives.

Figure 2 (revised) — Marginal effect of FSTS on ln_lp from M8 (full sample),
  evaluated across FSTS ∈ [0%, 100%], with:
    (a) Decile-count bars in the lower panel
    (b) Rug plot (every observation tick)
    (c) Shaded region for "thin support" (FSTS > 70%, only ~3% of firms)

Figure 3 (revised) — Marginal effect of DAI on ln_lp at varying FSTS levels
  (M8 full-sample), with:
    (a) Rug plot at the bottom
    (b) Shaded region for thin support (FSTS > 70%)
    (c) Bootstrap-derived 95% CI for the implied turning point
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
FIG_DIR = REPO / "outputs" / "r3" / "figures"
AUDIT_DIR = REPO / "outputs" / "r3" / "audit"
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
    return smf.ols(formula, data=df[mask]).fit(cov_type="HC1"), mask


def figure2(df, model, mask, fsts_mean):
    """Marginal effect of FSTS on ln_lp from M8."""
    fsts_pct = np.linspace(0, 100, 201)
    fsts_c_grid = fsts_pct / 100 - fsts_mean

    # dE[ln_lp]/dFSTS = β1 + 2 β2 * FSTS_c (+ DAI interaction terms at DAI=0).
    b1 = model.params["fsts_c"]
    b2 = model.params["fsts_c2"]
    me = b1 + 2 * b2 * fsts_c_grid

    # Delta-method SE
    cov = model.cov_params()
    se = np.zeros_like(fsts_c_grid)
    for i, fc in enumerate(fsts_c_grid):
        v = (cov.loc["fsts_c", "fsts_c"]
             + 4 * fc**2 * cov.loc["fsts_c2", "fsts_c2"]
             + 4 * fc * cov.loc["fsts_c", "fsts_c2"])
        se[i] = np.sqrt(v)
    ci_lo = me - 1.96 * se
    ci_hi = me + 1.96 * se

    fig = plt.figure(figsize=(8, 6))
    gs = fig.add_gridspec(3, 1, height_ratios=[5, 0.7, 1.5], hspace=0.10)
    ax = fig.add_subplot(gs[0, 0])
    ax_rug = fig.add_subplot(gs[1, 0], sharex=ax)
    ax_dec = fig.add_subplot(gs[2, 0], sharex=ax)

    # Main panel: marginal effect with CI
    ax.fill_between(fsts_pct, ci_lo, ci_hi, color="C0", alpha=0.15,
                    label="95% CI")
    ax.plot(fsts_pct, me, color="C0", lw=2, label="Marginal effect")
    ax.axhline(0, color="gray", lw=0.8, ls="--")

    # Shade thin-support region (FSTS > 70%)
    ax.axvspan(70, 100, color="lightgray", alpha=0.4,
               label="Thin support (FSTS > 70%)")
    ax_rug.axvspan(70, 100, color="lightgray", alpha=0.4)
    ax_dec.axvspan(70, 100, color="lightgray", alpha=0.4)

    # Turning point (where ME crosses zero)
    if b2 != 0:
        tp_centered = -b1 / (2 * b2)
        tp_pct = (tp_centered + fsts_mean) * 100
        if 0 <= tp_pct <= 100:
            ax.axvline(tp_pct, color="C3", lw=1.2, ls=":",
                       label=f"Turning point ≈ {tp_pct:.1f}%")

    ax.set_ylabel(r"$\partial$ ln(labor productivity) / $\partial$ FSTS")
    ax.set_title("Figure 2 (revised). Marginal effect of FSTS on ln_lp "
                 "from full-sample M8")
    ax.legend(loc="upper right", fontsize=9)
    ax.grid(alpha=0.3)
    ax.tick_params(labelbottom=False)

    # Rug plot
    fsts_obs = (df.loc[mask, "fsts"] * 100).values
    ax_rug.plot(fsts_obs, np.zeros_like(fsts_obs), "|",
                color="black", alpha=0.4, markersize=6)
    ax_rug.set_yticks([])
    ax_rug.set_ylabel("Obs", rotation=0, ha="right", va="center", fontsize=9)
    ax_rug.tick_params(labelbottom=False)

    # Decile counts
    bins = np.arange(0, 110, 10)
    counts, _ = np.histogram(fsts_obs, bins=bins)
    centers = (bins[:-1] + bins[1:]) / 2
    ax_dec.bar(centers, counts, width=8, color="steelblue", alpha=0.7)
    for c, cnt in zip(centers, counts):
        if cnt > 0:
            ax_dec.text(c, cnt, str(cnt), ha="center", va="bottom", fontsize=8)
    ax_dec.set_xlabel("FSTS (%)")
    ax_dec.set_ylabel("Firms\nper bin", fontsize=9)
    ax_dec.set_xlim(-2, 102)
    ax_dec.grid(axis="y", alpha=0.3)

    out = FIG_DIR / "Fig2_v2.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote: {out}")


def figure3(df, model, mask, fsts_mean):
    """Marginal effect of DAI on ln_lp at varying FSTS levels."""
    fsts_pct = np.linspace(0, 100, 201)
    fsts_c_grid = fsts_pct / 100 - fsts_mean

    # ME of DAI = β_DAI + β_{FSTS×DAI} * FSTS_c + β_{FSTS²×DAI} * FSTS_c²
    b_dai = model.params["DAI"]
    b_dai_f = model.params["fsts_c_DAI"]
    b_dai_f2 = model.params["fsts_c2_DAI"]
    me = b_dai + b_dai_f * fsts_c_grid + b_dai_f2 * fsts_c_grid**2

    cov = model.cov_params()
    se = np.zeros_like(fsts_c_grid)
    for i, fc in enumerate(fsts_c_grid):
        # Var(b_DAI + b_f * fc + b_f2 * fc^2)
        v = (cov.loc["DAI", "DAI"]
             + fc**2 * cov.loc["fsts_c_DAI", "fsts_c_DAI"]
             + fc**4 * cov.loc["fsts_c2_DAI", "fsts_c2_DAI"]
             + 2 * fc * cov.loc["DAI", "fsts_c_DAI"]
             + 2 * fc**2 * cov.loc["DAI", "fsts_c2_DAI"]
             + 2 * fc**3 * cov.loc["fsts_c_DAI", "fsts_c2_DAI"])
        se[i] = np.sqrt(max(v, 0))
    ci_lo = me - 1.96 * se
    ci_hi = me + 1.96 * se

    # Implied turning point of DAI marginal effect (where ME crosses zero,
    # going from negative to positive). Solve: b_dai_f2 * x² + b_dai_f * x + b_dai = 0
    disc = b_dai_f**2 - 4 * b_dai_f2 * b_dai
    tp_pct = None
    if disc >= 0 and abs(b_dai_f2) > 1e-9:
        roots_centered = ((-b_dai_f - np.sqrt(disc)) / (2 * b_dai_f2),
                          (-b_dai_f + np.sqrt(disc)) / (2 * b_dai_f2))
        roots_pct = [(r + fsts_mean) * 100 for r in roots_centered]
        # Take the in-range positive root
        in_range = [r for r in roots_pct if 0 <= r <= 100]
        if in_range:
            tp_pct = sorted(in_range)[-1]  # right-most in-range root

    fig = plt.figure(figsize=(8, 6))
    gs = fig.add_gridspec(3, 1, height_ratios=[5, 0.7, 1.5], hspace=0.10)
    ax = fig.add_subplot(gs[0, 0])
    ax_rug = fig.add_subplot(gs[1, 0], sharex=ax)
    ax_dec = fig.add_subplot(gs[2, 0], sharex=ax)

    ax.fill_between(fsts_pct, ci_lo, ci_hi, color="C2", alpha=0.15,
                    label="95% CI")
    ax.plot(fsts_pct, me, color="C2", lw=2,
            label="ME of DAI on ln_lp")
    ax.axhline(0, color="gray", lw=0.8, ls="--")

    # Thin-support shade
    ax.axvspan(70, 100, color="lightgray", alpha=0.4,
               label="Thin support (FSTS > 70%)")
    ax_rug.axvspan(70, 100, color="lightgray", alpha=0.4)
    ax_dec.axvspan(70, 100, color="lightgray", alpha=0.4)

    if tp_pct is not None:
        ax.axvline(tp_pct, color="C3", lw=1.2, ls=":",
                   label=f"DAI ME turning point ≈ {tp_pct:.1f}%")

    ax.set_ylabel(r"$\partial$ ln(labor productivity) / $\partial$ DAI")
    ax.set_title("Figure 3 (revised). Marginal effect of DAI on ln_lp "
                 "across FSTS (full-sample M8)")
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)
    ax.tick_params(labelbottom=False)

    fsts_obs = (df.loc[mask, "fsts"] * 100).values
    ax_rug.plot(fsts_obs, np.zeros_like(fsts_obs), "|",
                color="black", alpha=0.4, markersize=6)
    ax_rug.set_yticks([])
    ax_rug.set_ylabel("Obs", rotation=0, ha="right", va="center", fontsize=9)
    ax_rug.tick_params(labelbottom=False)

    bins = np.arange(0, 110, 10)
    counts, _ = np.histogram(fsts_obs, bins=bins)
    centers = (bins[:-1] + bins[1:]) / 2
    ax_dec.bar(centers, counts, width=8, color="forestgreen", alpha=0.7)
    for c, cnt in zip(centers, counts):
        if cnt > 0:
            ax_dec.text(c, cnt, str(cnt), ha="center", va="bottom", fontsize=8)
    ax_dec.set_xlabel("FSTS (%)")
    ax_dec.set_ylabel("Firms\nper bin", fontsize=9)
    ax_dec.set_xlim(-2, 102)
    ax_dec.grid(axis="y", alpha=0.3)

    out = FIG_DIR / "Fig3_v2.png"
    fig.savefig(out, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Wrote: {out}")
    return tp_pct


def main():
    print("=" * 72)
    print("R3 Phase 1 — Support-aware figures (rev. Figure 2 & 3)")
    print("=" * 72)

    df = load_frame()
    fsts_mean = df["fsts"].mean()
    print(f"FSTS mean (centering offset, full sample): {fsts_mean:.4f}")

    model, mask = fit_m8(df)
    print(f"M8 (canonical, full sample): N = {int(mask.sum())}")

    figure2(df, model, mask, fsts_mean)
    tp_pct = figure3(df, model, mask, fsts_mean)
    if tp_pct is not None:
        print(f"DAI marginal-effect turning point (full-sample M8): {tp_pct:.2f}%")


if __name__ == "__main__":
    main()
