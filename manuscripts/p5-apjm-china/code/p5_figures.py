#!/usr/bin/env python3
"""
p5_figures.py
=============
Phase C — generate the 3 figures called for in Option C+ writing pack:
  Fig 1: TP-stability plot (TP + 95% CI in 2012, 2024, pooled + Paternoster annotation)
  Fig 2: predicted lnLP curves overlay 2012 vs 2024 + threshold lines
  Fig 3: level-shift TCI / DAI by wave (bar plot with Paternoster z annotations)

Skips Figure 4 (WC marginal effect plot) because β classified NULL.

Also writes:
  tables/p5_threshold_table.csv  (TP, CI, LM p per sample)
  tables/p5_paternoster_table.csv (cross-wave z-tests)
  tables/p5_baseline_coefs.csv   (M0p TCI/DAI/controls coefficients)
"""

from __future__ import annotations
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats

# Re-use the build_wave / read_dta_with_fallback from the β pipeline
sys.path.insert(0, str(Path(__file__).parent))
from p5_beta_pipeline import (
    PATHS, read_dta_with_fallback, build_wave,
)

ROOT = Path(__file__).resolve().parent.parent
TABLES = ROOT / "tables"
FIGURES = ROOT / "figures"
TABLES.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)


def fit_threshold_core(df: pd.DataFrame, with_wave_fe: bool = False):
    rhs = ["FSTS", "FSTS_sq", "lnemp", "firm_age", "foreign_dummy"]
    if with_wave_fe and "wave_2024" in df.columns:
        rhs += ["wave_2024"]
    sub = df.dropna(subset=["lnLP"] + rhs).copy()
    X = sm.add_constant(sub[rhs].astype(float))
    return sm.OLS(sub["lnLP"].astype(float), X).fit(cov_type="HC1"), sub


def fit_TCI_DAI(df: pd.DataFrame, suffix: str, with_wave_fe: bool = False):
    """Return M0p model with TCI/DAI z + controls. suffix '_z' (within-wave) or '_zp' (pooled)."""
    sub = df.copy()
    # Build z columns if absent
    for v in ["TCI_full", "DAI_thin"]:
        col = f"{v}{suffix}"
        if col not in sub.columns:
            sub[col] = (sub[v] - sub[v].mean()) / sub[v].std(ddof=1)
    rhs = ["FSTS", "FSTS_sq", f"TCI_full{suffix}", f"DAI_thin{suffix}",
           "lnemp", "firm_age", "foreign_dummy"]
    if with_wave_fe and "wave_2024" in sub.columns:
        rhs += ["wave_2024"]
    sub2 = sub.dropna(subset=["lnLP"] + rhs).copy()
    X = sm.add_constant(sub2[rhs].astype(float))
    m = sm.OLS(sub2["lnLP"].astype(float), X).fit(cov_type="HC1")
    return m, sub2


def lind_mehlum_with_ci(model, x_lo: float = 0.0, x_hi: float = 1.0):
    b1 = model.params.get("FSTS", np.nan)
    b2 = model.params.get("FSTS_sq", np.nan)
    se1 = model.bse.get("FSTS", np.nan)
    se2 = model.bse.get("FSTS_sq", np.nan)
    cov12 = model.cov_params().loc["FSTS", "FSTS_sq"]
    # Slopes at endpoints
    slope_lo = b1 + 2 * b2 * x_lo
    slope_hi = b1 + 2 * b2 * x_hi
    var_lo = se1 ** 2 + (2 * x_lo) ** 2 * se2 ** 2 + 2 * (2 * x_lo) * cov12
    var_hi = se1 ** 2 + (2 * x_hi) ** 2 * se2 ** 2 + 2 * (2 * x_hi) * cov12
    t_lo = slope_lo / max(np.sqrt(var_lo), 1e-12)
    t_hi = slope_hi / max(np.sqrt(var_hi), 1e-12)
    p_lo = 1 - stats.norm.cdf(t_lo)
    p_hi = stats.norm.cdf(t_hi)
    p_lm = max(p_lo, p_hi)
    # TP + delta-method CI
    tp = -b1 / (2 * b2) if b2 != 0 else np.nan
    if not np.isnan(tp):
        # Var(tp) = (1/(2b2))^2 Var(b1) + (b1/(2 b2^2))^2 Var(b2) + 2 (-1/(2b2))(b1/(2b2^2)) Cov(b1,b2)
        g1 = -1.0 / (2 * b2)
        g2 = b1 / (2 * b2 ** 2)
        var_tp = g1 ** 2 * se1 ** 2 + g2 ** 2 * se2 ** 2 + 2 * g1 * g2 * cov12
        se_tp = float(np.sqrt(max(var_tp, 0.0)))
    else:
        se_tp = np.nan
    return {"b1": b1, "b2": b2, "se1": se1, "se2": se2, "cov12": cov12,
            "tp_pct": tp * 100, "se_tp_pct": se_tp * 100,
            "tp_ci_lo": (tp - 1.96 * se_tp) * 100,
            "tp_ci_hi": (tp + 1.96 * se_tp) * 100,
            "lm_p": p_lm}


def paternoster(b_a, se_a, b_b, se_b):
    if any(np.isnan(x) for x in (b_a, se_a, b_b, se_b)):
        return np.nan, np.nan
    z = (b_a - b_b) / np.sqrt(se_a ** 2 + se_b ** 2)
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p


def predict_along_fsts(model, sub, sample_label, n_grid=80):
    fsts_grid = np.linspace(0.0, 1.0, n_grid)
    fsts_grid_sq = fsts_grid ** 2
    # Hold controls at within-sample means
    means = {c: sub[c].mean() for c in ["lnemp", "firm_age", "foreign_dummy"]}

    # Build X_pred
    cols_in_model = list(model.params.index)
    X = pd.DataFrame(0.0, index=range(n_grid), columns=cols_in_model)
    X["const"] = 1.0
    X["FSTS"] = fsts_grid
    X["FSTS_sq"] = fsts_grid_sq
    for c, val in means.items():
        if c in X.columns:
            X[c] = val
    if "wave_2024" in X.columns:
        X["wave_2024"] = 1 if "2024" in sample_label else 0

    pred = X @ model.params
    cov = model.cov_params()
    var_pred = np.einsum("ij,jk,ik->i", X.values, cov.values, X.values)
    se_pred = np.sqrt(np.maximum(var_pred, 0))
    return fsts_grid, pred.values, pred.values - 1.96 * se_pred, pred.values + 1.96 * se_pred


def main():
    print("Phase C — building figures from β baseline")

    # Build waves
    waves = {}
    for year, p in PATHS.items():
        raw = read_dta_with_fallback(p)
        waves[year] = build_wave(year, raw)
    pool = pd.concat(waves.values(), ignore_index=False, sort=False)
    pool["wave_2024"] = (pool["wave"] == 2024).astype(int)
    # Pooled z columns for TCI / DAI
    for v in ["TCI_full", "DAI_thin"]:
        pool[f"{v}_zp"] = (pool[v] - pool[v].mean()) / pool[v].std(ddof=1)

    # ============================================
    # Threshold core stats
    # ============================================
    threshold_rows = []
    models_by_sample = {}
    subs_by_sample = {}
    for label, df, with_wave_fe in [
        ("CHN_2012", waves[2012], False),
        ("CHN_2024", waves[2024], False),
        ("CHN_pooled", pool, True),
    ]:
        m, s = fit_threshold_core(df, with_wave_fe=with_wave_fe)
        models_by_sample[label] = m
        subs_by_sample[label] = s
        lm = lind_mehlum_with_ci(m)
        threshold_rows.append({
            "sample": label,
            "n": int(m.nobs),
            "b_FSTS": m.params["FSTS"], "se_FSTS": m.bse["FSTS"],
            "b_FSTS_sq": m.params["FSTS_sq"], "se_FSTS_sq": m.bse["FSTS_sq"],
            "tp_pct": lm["tp_pct"], "se_tp_pct": lm["se_tp_pct"],
            "tp_ci_lo": lm["tp_ci_lo"], "tp_ci_hi": lm["tp_ci_hi"],
            "lm_p": lm["lm_p"],
        })
    df_thr = pd.DataFrame(threshold_rows)
    df_thr.to_csv(TABLES / "p5_threshold_table.csv", index=False)
    print(df_thr.to_string(index=False))

    # ============================================
    # TCI / DAI direct effect models for level-shift figure
    # ============================================
    coef_rows = []
    tci_dai_models = {}
    for label, df, suffix, with_wave_fe in [
        ("CHN_2012", waves[2012], "_z", False),
        ("CHN_2024", waves[2024], "_z", False),
        ("CHN_pooled", pool, "_zp", True),
    ]:
        m, s = fit_TCI_DAI(df, suffix, with_wave_fe=with_wave_fe)
        tci_dai_models[label] = (m, s, suffix)
        for v in [f"TCI_full{suffix}", f"DAI_thin{suffix}"]:
            if v in m.params.index:
                coef_rows.append({"sample": label, "var": v.replace(suffix, ""),
                                  "beta": m.params[v], "se": m.bse[v],
                                  "p": m.pvalues[v], "n": int(m.nobs)})
    df_coef = pd.DataFrame(coef_rows)
    df_coef.to_csv(TABLES / "p5_baseline_coefs.csv", index=False)
    print("\nTCI / DAI direct effects:")
    print(df_coef.to_string(index=False))

    # ============================================
    # Paternoster z-tests across waves
    # ============================================
    pat_rows = []
    # FSTS / FSTS² from M0 threshold core
    for var in ["FSTS", "FSTS_sq"]:
        m12, m24 = models_by_sample["CHN_2012"], models_by_sample["CHN_2024"]
        z, p = paternoster(m12.params[var], m12.bse[var],
                            m24.params[var], m24.bse[var])
        pat_rows.append({"variable": var, "wave_pair": "2012 vs 2024",
                          "b12": m12.params[var], "b24": m24.params[var],
                          "z": z, "p": p})
    # TCI / DAI from M0p
    m12 = tci_dai_models["CHN_2012"][0]
    m24 = tci_dai_models["CHN_2024"][0]
    for var_short in ["TCI_full", "DAI_thin"]:
        v12 = f"{var_short}_z"  # within-wave z
        v24 = f"{var_short}_z"
        if v12 in m12.params.index and v24 in m24.params.index:
            z, p = paternoster(m12.params[v12], m12.bse[v12],
                                m24.params[v24], m24.bse[v24])
            pat_rows.append({"variable": var_short, "wave_pair": "2012 vs 2024",
                              "b12": m12.params[v12], "b24": m24.params[v24],
                              "z": z, "p": p})
    df_pat = pd.DataFrame(pat_rows)
    df_pat.to_csv(TABLES / "p5_paternoster_table.csv", index=False)
    print("\nPaternoster z-tests:")
    print(df_pat.to_string(index=False))

    # ============================================
    # Figure 1 — TP stability with 95% CI + Paternoster annotation
    # ============================================
    fig, ax = plt.subplots(figsize=(7.5, 4.6), dpi=150)
    samples = ["CHN_2012", "CHN_2024", "CHN_pooled"]
    labels = ["China 2012", "China 2024", "Pooled"]
    xs = [0, 1, 2]
    tps = [df_thr.loc[df_thr["sample"] == s, "tp_pct"].iloc[0] for s in samples]
    los = [df_thr.loc[df_thr["sample"] == s, "tp_ci_lo"].iloc[0] for s in samples]
    his = [df_thr.loc[df_thr["sample"] == s, "tp_ci_hi"].iloc[0] for s in samples]
    ns = [int(df_thr.loc[df_thr["sample"] == s, "n"].iloc[0]) for s in samples]
    pvals = [df_thr.loc[df_thr["sample"] == s, "lm_p"].iloc[0] for s in samples]

    yerrs = [[tp - lo for tp, lo in zip(tps, los)],
             [hi - tp for tp, hi in zip(tps, his)]]
    ax.errorbar(xs, tps, yerr=yerrs, fmt='o', capsize=8, capthick=2.0,
                lw=2.2, mfc="#1F4E79", mec="#1F4E79", color="#1F4E79",
                markersize=10, label="TP estimate ± 95% CI (delta-method)")
    # Annotate
    for x, tp, lo, hi, n, p in zip(xs, tps, los, his, ns, pvals):
        ax.text(x, hi + 3, f"TP={tp:.1f}%\nLM p={p:.3f}\nN={n}",
                ha="center", va="bottom", fontsize=8, color="#444444")

    # Paternoster annotation between 2012 and 2024
    z_FSTS = df_pat.loc[df_pat["variable"] == "FSTS", "z"].iloc[0]
    p_FSTS = df_pat.loc[df_pat["variable"] == "FSTS", "p"].iloc[0]
    z_FSTS_sq = df_pat.loc[df_pat["variable"] == "FSTS_sq", "z"].iloc[0]
    p_FSTS_sq = df_pat.loc[df_pat["variable"] == "FSTS_sq", "p"].iloc[0]
    ax.text(0.5, 18,
            f"Paternoster z (2012 vs 2024):\nFSTS  z={z_FSTS:+.2f} (p={p_FSTS:.3f})\nFSTS²  z={z_FSTS_sq:+.2f} (p={p_FSTS_sq:.3f})",
            ha="center", va="bottom", fontsize=8, color="#A0522D",
            bbox=dict(boxstyle="round,pad=0.4", fc="#FFF1E0", ec="#A0522D"))

    ax.set_xticks(xs)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Optimal export-intensity threshold (%)", fontsize=10)
    ax.set_ylim(0, 90)
    ax.set_title("Figure 1. Stable export-intensity threshold across waves\nChinese manufacturing SMEs, WBES 2012 + 2024",
                 fontsize=11, fontweight="bold")
    ax.grid(alpha=0.3, axis="y")
    ax.legend(loc="upper right", fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "figure_1_threshold_stability.pdf", bbox_inches="tight")
    fig.savefig(FIGURES / "figure_1_threshold_stability.png", bbox_inches="tight", dpi=200)
    plt.close(fig)
    print("[ok] Figure 1")

    # ============================================
    # Figure 2 — Predicted lnLP curves overlay 2012 vs 2024 + threshold lines
    # ============================================
    fig, ax = plt.subplots(figsize=(8.5, 5.0), dpi=150)
    for sample, color, ls, label in [
        ("CHN_2012", "#1F4E79", "-", "China 2012"),
        ("CHN_2024", "#A0522D", "--", "China 2024"),
    ]:
        m = models_by_sample[sample]
        s = subs_by_sample[sample]
        x_grid, mu, lo, hi = predict_along_fsts(m, s, sample)
        ax.plot(x_grid * 100, mu, color=color, lw=2.5, linestyle=ls, label=f"{label} (N={int(m.nobs)})")
        ax.fill_between(x_grid * 100, lo, hi, color=color, alpha=0.15)
        # Mark threshold
        tp = df_thr.loc[df_thr["sample"] == sample, "tp_pct"].iloc[0]
        ax.axvline(tp, color=color, lw=1.0, alpha=0.7, ls=":")

    # Safe operating zone shading
    ax.axvspan(30, 60, color="#9EBCD9", alpha=0.10,
               label="Safe operating zone 30–60%")

    ax.set_xlabel("Export intensity FSTS (%)", fontsize=10)
    ax.set_ylabel("Predicted ln(labour productivity)", fontsize=10)
    ax.set_xlim(0, 100)
    ax.set_xticks(np.arange(0, 101, 10))
    ax.set_title("Figure 2. Predicted internationalisation–performance curves\nChina 2012 vs 2024, threshold-stability overlay",
                 fontsize=11, fontweight="bold")
    ax.grid(alpha=0.3)
    ax.legend(loc="lower center", fontsize=9)
    fig.tight_layout()
    fig.savefig(FIGURES / "figure_2_ip_curves_overlay.pdf", bbox_inches="tight")
    fig.savefig(FIGURES / "figure_2_ip_curves_overlay.png", bbox_inches="tight", dpi=200)
    plt.close(fig)
    print("[ok] Figure 2")

    # ============================================
    # Figure 3 — Level-shift TCI / DAI by wave with Paternoster z
    # ============================================
    fig, ax = plt.subplots(figsize=(7.5, 4.6), dpi=150)
    waves_lbl = ["China 2012", "China 2024", "Pooled"]
    xs = np.arange(len(waves_lbl))
    width = 0.36

    tci_betas = [df_coef.loc[(df_coef["sample"] == s) & (df_coef["var"] == "TCI_full"), "beta"].iloc[0]
                 for s in ["CHN_2012", "CHN_2024", "CHN_pooled"]]
    tci_ses = [df_coef.loc[(df_coef["sample"] == s) & (df_coef["var"] == "TCI_full"), "se"].iloc[0]
               for s in ["CHN_2012", "CHN_2024", "CHN_pooled"]]
    dai_betas = [df_coef.loc[(df_coef["sample"] == s) & (df_coef["var"] == "DAI_thin"), "beta"].iloc[0]
                 for s in ["CHN_2012", "CHN_2024", "CHN_pooled"]]
    dai_ses = [df_coef.loc[(df_coef["sample"] == s) & (df_coef["var"] == "DAI_thin"), "se"].iloc[0]
               for s in ["CHN_2012", "CHN_2024", "CHN_pooled"]]

    bars1 = ax.bar(xs - width / 2, tci_betas, width,
                   yerr=[1.96 * s for s in tci_ses], capsize=4,
                   color="#1F4E79", label="TCI_full β_z (technological capability)")
    bars2 = ax.bar(xs + width / 2, dai_betas, width,
                   yerr=[1.96 * s for s in dai_ses], capsize=4,
                   color="#2E7D32", label="DAI_thin β_z (digital adoption)")

    for b, val in zip(bars1, tci_betas):
        ax.text(b.get_x() + b.get_width() / 2, val + (0.01 if val > 0 else -0.03),
                f"{val:+.3f}", ha="center",
                fontsize=8, color="#1F4E79")
    for b, val in zip(bars2, dai_betas):
        ax.text(b.get_x() + b.get_width() / 2, val + (0.01 if val > 0 else -0.03),
                f"{val:+.3f}", ha="center",
                fontsize=8, color="#2E7D32")

    ax.axhline(0, color="black", lw=0.7)
    ax.set_xticks(xs)
    ax.set_xticklabels(waves_lbl)
    ax.set_ylabel("β_z (within-wave z-standardised; pooled wave-FE adjusted)", fontsize=9)
    ax.set_title("Figure 3. Direct level-shift effects of TCI and DAI by wave\nChinese manufacturing SMEs, WBES 2012 + 2024",
                 fontsize=11, fontweight="bold")

    z_TCI = df_pat.loc[df_pat["variable"] == "TCI_full", "z"].iloc[0]
    p_TCI = df_pat.loc[df_pat["variable"] == "TCI_full", "p"].iloc[0]
    z_DAI = df_pat.loc[df_pat["variable"] == "DAI_thin", "z"].iloc[0]
    p_DAI = df_pat.loc[df_pat["variable"] == "DAI_thin", "p"].iloc[0]
    ax.text(0.02, 0.97,
            f"Paternoster z (2012 vs 2024):\nTCI z={z_TCI:+.2f} (p={p_TCI:.3f})\nDAI z={z_DAI:+.2f} (p={p_DAI:.3f})",
            ha="left", va="top", transform=ax.transAxes, fontsize=8, color="#444444",
            bbox=dict(boxstyle="round,pad=0.4", fc="#F4F4F4", ec="#888"))

    ax.legend(loc="upper right", fontsize=8)
    ax.grid(alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(FIGURES / "figure_3_level_shifts.pdf", bbox_inches="tight")
    fig.savefig(FIGURES / "figure_3_level_shifts.png", bbox_inches="tight", dpi=200)
    plt.close(fig)
    print("[ok] Figure 3")

    print(f"\n[done] Figures and tables in {FIGURES} and {TABLES}")


if __name__ == "__main__":
    main()
