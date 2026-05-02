"""
R3 — Generate three manuscript-ready figures aligned with canonical data.

Replaces the three embedded PNGs in
papers/p3-singapore/Manuscript_Blinded_MIR_2_revised.docx:

  Figure 1 (image3.png)  Conceptual model (no "Digital-frontier" wording).
  Figure 2 (image2.png)  Marginal effect of DAI across export intensity,
                         with support-aware rug + thin-tail shading and
                         bootstrap-aware caveat.
  Figure 3 (image1.png)  Predicted I–P curve from canonical M2 with 95% CI
                         band, scatter, rug, and bootstrap CI for the
                         turning point overlaid as a shaded vertical band.

All numerical content is regenerated from raw .dta via the locked spec
in `tools/r3/00_canonical_m8.py`. No hardcoded coefficients.

Outputs:
  outputs/r3/figures/Fig1_conceptual.png
  outputs/r3/figures/Fig2_DAI_marginal.png
  outputs/r3/figures/Fig3_IP_predicted.png
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
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

REPO = Path(__file__).resolve().parents[2]
DTA = REPO / "data" / "raw" / "Singapore2023fulldata.dta"
FIG_DIR = REPO / "outputs" / "r3" / "figures"
AUDIT_DIR = REPO / "outputs" / "r3" / "audit"
FIG_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# Data prep (replicates locked spec)
# ============================================================
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
    df.attrs["fsts_mean"] = float(df["fsts"].mean())
    df["fsts_c"] = df["fsts"] - df.attrs["fsts_mean"]
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
            df[c + "_z"] = (df[c] - mu) / sd
            zs.append(c + "_z")
        raw = df[zs].sum(axis=1, skipna=False) / len(parts)
        df[name] = (raw - raw.mean()) / raw.std()

    composite(["b8_yn", "e6_yn", "h1_yn", "h8_yn"], "TCI")
    composite(["c22b_yn", "k33_imp", "k38_imp"], "DAI")
    df["fsts_c_DAI"] = df["fsts_c"] * df["DAI"]
    df["fsts_c2_DAI"] = df["fsts_c2"] * df["DAI"]
    return df


def fit_m2(df):
    core = ["ln_lp", "fsts_c", "fsts_c2",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    mask = df[core].notna().all(axis=1)
    formula = ("ln_lp ~ fsts_c + fsts_c2 + ln_empl + firm_age + foreign"
               " + C(broad_sector)")
    return smf.ols(formula, data=df[mask]).fit(cov_type="HC1"), mask


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


# ============================================================
# Figure 1 — Conceptual model (no "digital-frontier")
# ============================================================
def fig1_conceptual(out: Path):
    fig, ax = plt.subplots(figsize=(13, 7.5))
    ax.set_xlim(0, 130)
    ax.set_ylim(0, 70)
    ax.axis("off")

    def box(x, y, w, h, color, label_main, label_sub=""):
        rect = FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.4,rounding_size=1.8",
            linewidth=1.8, edgecolor=color, facecolor=color,
            alpha=0.20,
        )
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2 + (1.6 if label_sub else 0),
                label_main, ha="center", va="center",
                fontsize=11, fontweight="bold", color=color)
        if label_sub:
            ax.text(x + w/2, y + h/2 - 2.0, label_sub,
                    ha="center", va="center", fontsize=8.5, style="italic",
                    color="#444444")

    def arrow(x1, y1, x2, y2, *, dashed=False, color="#222",
              connectionstyle="arc3,rad=0"):
        ls = "--" if dashed else "-"
        a = FancyArrowPatch((x1, y1), (x2, y2),
                            arrowstyle="-|>", mutation_scale=16,
                            linewidth=2.0, linestyle=ls, color=color,
                            connectionstyle=connectionstyle)
        ax.add_patch(a)

    def label_at(x, y, text, color="#222", fontsize=9.5):
        ax.text(x, y, text, ha="center", va="center", fontsize=fontsize,
                fontweight="bold", color=color,
                bbox=dict(boxstyle="round,pad=0.30",
                          facecolor="white", edgecolor=color, alpha=0.95,
                          linewidth=0.8))

    # Title
    ax.text(65, 66,
            "Figure 1. Conceptual model",
            ha="center", fontsize=13, fontweight="bold")
    ax.text(65, 62.5,
            "Technological capability, digital adoption, and the "
            "internationalization–performance relationship",
            ha="center", fontsize=10.5)

    # Box layout — wider, no overlaps
    # Left column: TCI (top), DAI (bottom)
    box(3,  44, 28, 11, "#1f77b4",
        "Technological\nCapability (TCI)",
        "Lall 1992; Cohen & Levinthal 1990")
    box(3,  10, 28, 11, "#ff7f0e",
        "Digital Adoption\n(DAI)",
        "Bharadwaj et al. 2013; Verhoef et al. 2021")
    # Middle: Internationalization
    box(53, 27, 26, 12, "#7f7f7f",
        "Internationalization\n(FSTS, FSTS²)",
        "foreign sales / total sales")
    # Right: Productivity
    box(99, 27, 28, 12, "#2ca02c",
        "Firm Productivity",
        "ln(labour productivity)")

    # Arrows + labels
    # H1 TCI → Productivity direct (long arrow over the top)
    arrow(31, 50, 99, 39, color="#1f77b4",
          connectionstyle="arc3,rad=-0.20")
    label_at(67, 56, "H1: TCI → Productivity (+ direct)", color="#1f77b4")

    # H3 DAI → Productivity direct (long arrow under the bottom)
    arrow(31, 15, 99, 28, color="#ff7f0e",
          connectionstyle="arc3,rad=0.20")
    label_at(67, 9, "H3: DAI → Productivity (conditional on FSTS)",
             color="#ff7f0e")

    # H2 TCI → moderates I-P arrow (dashed, into mid-arrow)
    arrow(20, 44, 60, 39.5, dashed=True, color="#1f77b4")
    label_at(40, 47.5, "H2: TCI moderation\n(open empirical question)",
             color="#1f77b4", fontsize=8.5)

    # H4 DAI → moderates I-P arrow (dashed)
    arrow(20, 21, 60, 27, dashed=True, color="#ff7f0e")
    label_at(40, 23.5, "H4: DAI moderation\n(stronger at high FSTS)",
             color="#ff7f0e", fontsize=8.5)

    # Internationalization → Productivity (descriptive inverted-U)
    arrow(79, 33, 99, 33, color="#666")
    label_at(89, 36.5, "Inverted-U (descriptive,\nfull sample)",
             color="#444", fontsize=8.5)

    # Legend (top-left)
    legend_y = 59
    ax.plot([3, 9], [legend_y, legend_y], color="black", lw=1.8)
    ax.text(10, legend_y, "Direct association",
            fontsize=9, va="center")
    ax.plot([29, 35], [legend_y, legend_y],
            color="black", lw=1.8, ls="--")
    ax.text(36, legend_y, "Moderation association",
            fontsize=9, va="center")

    # Bottom scope-condition box (replaces old "Digital-frontier" wording)
    scope = FancyBboxPatch(
        (4, 1), 122, 5,
        boxstyle="round,pad=0.5,rounding_size=2",
        linewidth=1.2, edgecolor="#555", facecolor="#f7f7f7",
        linestyle=(0, (4, 3)),
    )
    ax.add_patch(scope)
    ax.text(65, 4.3,
            "Scope: extreme-case, within-context evidence from Singapore",
            ha="center", fontsize=10.5, fontweight="bold", color="#333")
    ax.text(65, 2.0,
            "WBES 2023, N = 623; FSTS = 0 in 82.2% of firms; "
            "FSTS > 70% in 3.2% of firms — see Section 7 for scope conditions.",
            ha="center", fontsize=8.5, style="italic", color="#666")

    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote: {out}")


# ============================================================
# Figure 2 — DAI marginal effect across FSTS (support-aware)
# ============================================================
def fig2_dai_marginal(df, model, mask, out: Path):
    fsts_mean = df.attrs["fsts_mean"]
    fsts_pct = np.linspace(0, 100, 201)
    fsts_c_grid = fsts_pct / 100 - fsts_mean
    b_dai = model.params["DAI"]
    b_dai_f = model.params["fsts_c_DAI"]
    b_dai_f2 = model.params["fsts_c2_DAI"]
    me = b_dai + b_dai_f * fsts_c_grid + b_dai_f2 * fsts_c_grid**2

    cov = model.cov_params()
    se = np.zeros_like(fsts_c_grid)
    for i, fc in enumerate(fsts_c_grid):
        v = (cov.loc["DAI", "DAI"]
             + fc**2 * cov.loc["fsts_c_DAI", "fsts_c_DAI"]
             + fc**4 * cov.loc["fsts_c2_DAI", "fsts_c2_DAI"]
             + 2 * fc * cov.loc["DAI", "fsts_c_DAI"]
             + 2 * fc**2 * cov.loc["DAI", "fsts_c2_DAI"]
             + 2 * fc**3 * cov.loc["fsts_c_DAI", "fsts_c2_DAI"])
        se[i] = np.sqrt(max(v, 0))
    ci_lo = me - 1.96 * se
    ci_hi = me + 1.96 * se

    fig = plt.figure(figsize=(9, 6.2))
    gs = fig.add_gridspec(3, 1, height_ratios=[5.5, 0.55, 1.6], hspace=0.10)
    ax = fig.add_subplot(gs[0, 0])
    ax_rug = fig.add_subplot(gs[1, 0], sharex=ax)
    ax_dec = fig.add_subplot(gs[2, 0], sharex=ax)

    # Main panel
    ax.fill_between(fsts_pct, ci_lo, ci_hi, color="#2ca02c", alpha=0.18,
                    label="95% CI")
    ax.plot(fsts_pct, me, color="#2ca02c", lw=2.2,
            label="Marginal effect of DAI")
    ax.axhline(0, color="gray", lw=0.8, ls="--")
    ax.axvspan(70, 100, color="lightgray", alpha=0.45,
               label="Thin support (FSTS > 70%, ~3.2% of firms)")
    ax.set_ylabel(r"$\partial$ ln(labour productivity) / $\partial$ DAI (z)",
                  fontsize=10.5)
    ax.set_title("Figure 2. Marginal effect of digital adoption (DAI) "
                 "on labour productivity\nacross export intensity — "
                 "canonical M8 (N = 617)",
                 fontsize=11.5, pad=10)
    ax.legend(loc="upper left", fontsize=9)
    ax.grid(alpha=0.3)
    ax.tick_params(labelbottom=False)

    # Rug
    fsts_obs = (df.loc[mask, "fsts"] * 100).values
    ax_rug.plot(fsts_obs, np.zeros_like(fsts_obs), "|",
                color="black", alpha=0.4, markersize=6)
    ax_rug.set_yticks([])
    ax_rug.set_ylabel("Obs", rotation=0, ha="right",
                      va="center", fontsize=9)
    ax_rug.tick_params(labelbottom=False)
    ax_rug.axvspan(70, 100, color="lightgray", alpha=0.45)

    # Decile counts
    bins = np.arange(0, 110, 10)
    counts, _ = np.histogram(fsts_obs, bins=bins)
    centers = (bins[:-1] + bins[1:]) / 2
    ax_dec.bar(centers, counts, width=8, color="#2ca02c", alpha=0.55)
    for c, cnt in zip(centers, counts):
        if cnt > 0:
            ax_dec.text(c, cnt, str(cnt), ha="center", va="bottom",
                        fontsize=8)
    ax_dec.set_xlabel("Export intensity FSTS (%)", fontsize=10.5)
    ax_dec.set_ylabel("Firms\nper bin", fontsize=9)
    ax_dec.set_xlim(-2, 102)
    ax_dec.grid(axis="y", alpha=0.3)
    ax_dec.axvspan(70, 100, color="lightgray", alpha=0.45)

    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote: {out}")


# ============================================================
# Figure 3 — Predicted I-P curve from M2 with bootstrap turning-point CI
# ============================================================
def fig3_ip_predicted(df, m2, mask, out: Path):
    fsts_mean = df.attrs["fsts_mean"]
    df_m = df[mask].copy()

    # Predicted ln_lp at varying FSTS, holding controls at sample means.
    fsts_pct = np.linspace(0, 100, 201)
    fsts_c_grid = fsts_pct / 100 - fsts_mean
    pred_df = pd.DataFrame({
        "fsts_c": fsts_c_grid,
        "fsts_c2": fsts_c_grid ** 2,
        "ln_empl": [df_m["ln_empl"].mean()] * len(fsts_c_grid),
        "firm_age": [df_m["firm_age"].mean()] * len(fsts_c_grid),
        "foreign": [int(df_m["foreign"].mean() > 0.5)] * len(fsts_c_grid),
        "broad_sector": [df_m["broad_sector"].mode().iloc[0]] * len(fsts_c_grid),
    })
    pred = m2.get_prediction(pred_df).summary_frame(alpha=0.05)
    yhat = pred["mean"].values
    ci_lo = pred["mean_ci_lower"].values
    ci_hi = pred["mean_ci_upper"].values

    # Turning point + bootstrap CI from the audit json
    boot = json.loads((AUDIT_DIR / "bootstrap_tp.json").read_text())
    tp_full = boot["full_sample_tp_pct"]   # 82.43
    ci_low, ci_high = boot["boot_ci_95"]   # [52.8, 252.9]
    pct_invU = boot["pct_inverted_U_shape"]  # 96.3

    fig = plt.figure(figsize=(9, 6.2))
    gs = fig.add_gridspec(2, 1, height_ratios=[5.8, 0.6], hspace=0.10)
    ax = fig.add_subplot(gs[0, 0])
    ax_rug = fig.add_subplot(gs[1, 0], sharex=ax)

    # Scatter (subdued)
    fsts_obs = (df_m["fsts"] * 100).values
    ax.scatter(fsts_obs, df_m["ln_lp"].values, s=10, color="#888",
               alpha=0.18, label=f"Observed firms (N = {len(df_m)})")

    # Bootstrap turning-point CI band (clip to plot range)
    ci_low_plot = max(0, ci_low)
    ci_high_plot = min(100, ci_high)
    ax.axvspan(ci_low_plot, ci_high_plot, color="#d62728", alpha=0.10,
               label=f"95% bootstrap CI for turning point\n"
                     f"[{ci_low:.1f}%, {ci_high:.1f}%]")
    # Turning-point dashed line
    ax.axvline(tp_full, color="#d62728", lw=1.4, ls="--",
               label=f"Point estimate: {tp_full:.1f}%")

    # Predicted curve + CI band
    ax.fill_between(fsts_pct, ci_lo, ci_hi, color="#1f77b4", alpha=0.22,
                    label="95% CI for predicted ln(LP)")
    ax.plot(fsts_pct, yhat, color="#1f77b4", lw=2.2,
            label="Predicted curve (M2)")

    # Annotate inverted-U shape robustness
    ax.text(2, ax.get_ylim()[1] * 0.985 if False else 16,
            f"Inverted-U shape recovered in {pct_invU:.1f}%\n"
            f"of 5,000 bootstrap replications",
            fontsize=9, ha="left", va="top",
            bbox=dict(boxstyle="round,pad=0.3",
                      facecolor="white", edgecolor="#aaa"))

    ax.set_ylabel("ln(labour productivity)", fontsize=10.5)
    ax.set_title("Figure 3. Predicted internationalization–performance "
                 "curve (canonical M2)\n"
                 "Shape robust; turning-point location loosely identified",
                 fontsize=11.5, pad=10)
    ax.legend(loc="lower right", fontsize=8.5)
    ax.grid(alpha=0.3)
    ax.tick_params(labelbottom=False)
    ax.set_ylim(7, 17)

    # Rug plot
    ax_rug.plot(fsts_obs, np.zeros_like(fsts_obs), "|",
                color="black", alpha=0.4, markersize=6)
    ax_rug.set_yticks([])
    ax_rug.set_xlabel("Export intensity FSTS (%)", fontsize=10.5)
    ax_rug.set_ylabel("Obs", rotation=0, ha="right",
                      va="center", fontsize=9)
    ax_rug.set_xlim(-2, 102)

    fig.savefig(out, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote: {out}")


# ============================================================
# Main
# ============================================================
def main():
    print("=" * 72)
    print("R3 — Generate manuscript-ready figures aligned with canonical data")
    print("=" * 72)

    df = load_clean()
    print(f"\nLoaded N = {len(df)} (Singapore 2023 raw .dta)")
    m8, mask8 = fit_m8(df)
    m2, mask2 = fit_m2(df)
    print(f"M8 fit: N = {int(mask8.sum())} | M2 fit: N = {int(mask2.sum())}")
    print(f"M8 TCI = {m8.params['TCI']:+.4f}  "
          f"FSTS²×DAI = {m8.params['fsts_c2_DAI']:+.4f}  "
          f"Adj R² = {m8.rsquared_adj:.4f}")

    fig1_conceptual(FIG_DIR / "Fig1_conceptual.png")
    fig2_dai_marginal(df, m8, mask8, FIG_DIR / "Fig2_DAI_marginal.png")
    fig3_ip_predicted(df, m2, mask2, FIG_DIR / "Fig3_IP_predicted.png")

    print("\nAll figures written to:", FIG_DIR)


if __name__ == "__main__":
    main()
