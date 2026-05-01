#!/usr/bin/env python3
"""
make_figure_2_results.py
========================
Figure 2 — main empirical results for the v4.4 manuscript.

Renders four panels (2009, 2015, 2023, pooled) of the predicted lnLP
across direct-export intensity (FSTS), holding controls at within-wave
means. Each panel shades the 95% CI for the predicted mean and marks
the turning-point point estimate with a vertical dashed line. The
Lind-Mehlum p-value is annotated in each panel.

Inputs (read-only):
  ../output/p4_python_baseline.csv    (cleaned analytic dataset)
  ../tables/table_lind_mehlum.csv     (TP estimates + LM p)

Outputs:
  ../figures/figure_2_main_results.pdf
  ../figures/figure_2_main_results.png
"""

from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def fit_model(df: pd.DataFrame, with_wave_fe: bool = False):
    """Refit baseline OLS-HC1 on the supplied subset."""
    rhs = ["fsts_c", "fsts_c2", "tci_z", "dai_z",
           "lnemp", "firmage", "foreign_owned"]
    X = df[rhs].astype(float).copy()
    sec = pd.get_dummies(df["sector_broad"].astype(str),
                         prefix="sec", drop_first=True).astype(float)
    X = pd.concat([X, sec], axis=1)
    if with_wave_fe and df["wave"].nunique() > 1:
        wfe = pd.get_dummies(df["wave"].astype(str),
                             prefix="wave", drop_first=True).astype(float)
        X = pd.concat([X, wfe], axis=1)
    X = sm.add_constant(X)
    y = df["lnLP"].astype(float)
    return sm.OLS(y, X).fit(cov_type="HC1"), X.columns.tolist()


def predict_along_fsts(model, cols, df: pd.DataFrame, n_grid: int = 60):
    """Predict lnLP along the FSTS support, controls at within-sample means.
    Returns (fsts_grid_pct, pred, ci_lo, ci_hi)."""
    fsts_min = float(df["fsts"].min())
    fsts_max = float(df["fsts"].max())
    fsts_mean = float(df["fsts"].mean())
    grid_fsts = np.linspace(fsts_min, fsts_max, n_grid)
    grid_fsts_c = grid_fsts - fsts_mean
    grid_fsts_c2 = grid_fsts_c ** 2

    Xnew = pd.DataFrame(0.0, index=range(n_grid), columns=cols)
    Xnew["const"] = 1.0
    Xnew["fsts_c"] = grid_fsts_c
    Xnew["fsts_c2"] = grid_fsts_c2
    # Set z-stds at zero (within-wave mean), controls at sample means
    for c in ("tci_z", "dai_z"):
        Xnew[c] = 0.0
    for c in ("lnemp", "firmage", "foreign_owned"):
        Xnew[c] = float(df[c].mean())
    # Sector + wave dummies: hold at proportional shares (so prediction
    # represents the wave-average firm composition)
    for c in cols:
        if c.startswith(("sec_", "wave_")):
            base = c.split("_", 1)[1]
            if c.startswith("sec_"):
                share = float((df["sector_broad"].astype(str) == base).mean())
            else:
                share = float((df["wave"].astype(str) == base).mean())
            Xnew[c] = share

    Xnew_v = Xnew[cols].astype(float).values
    pred = Xnew_v @ model.params.values
    cov = np.asarray(model.cov_params())
    var_pred = np.einsum("ij,jk,ik->i", Xnew_v, cov, Xnew_v)
    se_pred = np.sqrt(np.maximum(var_pred, 0.0))
    return grid_fsts * 100, pred, pred - 1.96 * se_pred, pred + 1.96 * se_pred


def main():
    pool = pd.read_csv(ROOT / "output" / "p4_python_baseline.csv")
    pool["wave"] = pool["wave"].astype(str)
    lm = pd.read_csv(ROOT / "tables" / "table_lind_mehlum.csv")

    fig, axes = plt.subplots(2, 2, figsize=(10.5, 7.4), dpi=150,
                             sharey=True)
    panels = [("2009", axes[0, 0]),
              ("2015", axes[0, 1]),
              ("2023", axes[1, 0]),
              ("pooled", axes[1, 1])]

    fig.suptitle(
        "Figure 2. Predicted lnLP across direct-export intensity, "
        "by Vietnam WBES wave",
        fontsize=12, fontweight="bold", y=0.995)

    for wave, ax in panels:
        sub = pool if wave == "pooled" else pool[pool["wave"] == wave]
        model, cols = fit_model(sub, with_wave_fe=(wave == "pooled"))
        x_pct, mu, lo, hi = predict_along_fsts(model, cols, sub)
        ax.fill_between(x_pct, lo, hi, color="#9EBCD9", alpha=0.30,
                        label="95% CI (predicted mean)")
        ax.plot(x_pct, mu, color="#1F4E79", linewidth=2.0,
                label="Predicted lnLP")

        # Turning point + LM p
        row = lm[lm["wave"] == wave].iloc[0]
        tp = float(row["tp_raw_pct"])
        ci_lo = float(row["tp_ci_lo"]) + float(row["mean_fsts_pct"])
        ci_hi = float(row["tp_ci_hi"]) + float(row["mean_fsts_pct"])
        lm_p = float(row["lm_p"])

        if tp >= x_pct.min() and tp <= x_pct.max():
            ax.axvline(tp, color="#A0522D", linestyle="--", linewidth=1.2,
                       label=f"Turning point ≈ {tp:.0f}%")
            ax.axvspan(max(ci_lo, x_pct.min()), min(ci_hi, x_pct.max()),
                       color="#A0522D", alpha=0.06)

        ax.set_title(
            f"Wave {wave}  (N = {int(model.nobs)})   LM p = {lm_p:.3f}",
            fontsize=10, fontweight="bold")
        ax.set_xlabel("Direct-export intensity FSTS (%)", fontsize=9)
        ax.set_ylabel("Predicted lnLP", fontsize=9)
        ax.tick_params(labelsize=8)
        ax.grid(alpha=0.3)
        ax.legend(loc="lower center", fontsize=7, framealpha=0.9)

    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    fig.text(0.5, 0.005,
             "Notes. OLS-HC1 fitted curve with controls (lnEmp, FirmAge, "
             "ForeignOwned), sector FE, and (pooled panel) wave FE held at "
             "within-sample means; shaded band is the 95% CI for the "
             "predicted mean. Turning point: −β(FSTS_c)/(2 β(FSTS_c²)); "
             "LM p is the Lind & Mehlum (2010) U-test p-value.",
             ha="center", va="bottom", fontsize=7, color="#444444")

    fig.savefig(OUT / "figure_2_main_results.pdf",
                bbox_inches="tight", pad_inches=0.05)
    fig.savefig(OUT / "figure_2_main_results.png",
                bbox_inches="tight", pad_inches=0.05, dpi=200)
    print(f"[ok] Figure 2 -> {OUT/'figure_2_main_results.pdf'}")


if __name__ == "__main__":
    main()
