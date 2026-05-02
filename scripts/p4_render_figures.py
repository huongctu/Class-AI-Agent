"""Render Figure 1 (conceptual model) and Figure 2 (predicted I–P curves by wave).

Figure 2 is rebuilt from the real M2 inverted-U specification per wave + pooled,
holding controls at within-wave means and computing the 95% delta-method CI band
on the predicted mean.

Run from repo root:
    python3 scripts/p4_render_figures.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import statsmodels.api as sm

from p4_vietnam_analysis import build_pooled, build_wave  # type: ignore

ROOT = Path("/home/user/Class-AI-Agent/p4_vietnam")
OUT_FIGS = ROOT / "output" / "figures"
OUT_FIGS.mkdir(parents=True, exist_ok=True)


def fit_inverted_u(df, with_wave_fe: bool):
    """Fit lnLP ~ FSTSc + FSTSc² + lnEmp + FirmAge + ForeignOwned + sector + (wave?)."""
    parts = [np.ones((len(df), 1)),
             df["FSTSc"].to_numpy().reshape(-1, 1),
             df["FSTSc2"].to_numpy().reshape(-1, 1),
             df["lnEmp"].to_numpy().reshape(-1, 1),
             df["FirmAge"].to_numpy().reshape(-1, 1),
             df["ForeignOwned"].to_numpy().reshape(-1, 1)]
    names = ["const", "FSTSc", "FSTSc2", "lnEmp", "FirmAge", "ForeignOwned"]
    import pandas as pd
    sec = pd.get_dummies(df["sector1"].astype(int), prefix="sector1", drop_first=True, dtype=float)
    parts.append(sec.to_numpy())
    names.extend(sec.columns.tolist())
    if with_wave_fe:
        wf = pd.get_dummies(df["wave"].astype(int), prefix="wave", drop_first=True, dtype=float)
        parts.append(wf.to_numpy())
        names.extend(wf.columns.tolist())
    X = np.hstack(parts)
    fit = sm.OLS(df["lnLP"].to_numpy(), X).fit(cov_type="HC1")
    return fit, names


def predict_curve(fit, names, df, fsts_grid):
    """Predict lnLP across raw FSTS grid, holding controls at within-wave means."""
    fmean = df["FSTS"].mean()
    fsts_c = fsts_grid - fmean
    fsts_c2 = fsts_c ** 2

    means = {
        "lnEmp": df["lnEmp"].mean(),
        "FirmAge": df["FirmAge"].mean(),
        "ForeignOwned": df["ForeignOwned"].mean(),
    }
    sector_mode = int(df["sector1"].mode().iloc[0])
    wave_mode = int(df["wave"].mode().iloc[0]) if "wave" in df.columns else None

    preds = []
    ses = []
    cov = fit.cov_params()
    b = fit.params
    for f_c, f_c2 in zip(fsts_c, fsts_c2):
        x = np.zeros(len(names))
        x[names.index("const")] = 1.0
        x[names.index("FSTSc")] = f_c
        x[names.index("FSTSc2")] = f_c2
        x[names.index("lnEmp")] = means["lnEmp"]
        x[names.index("FirmAge")] = means["FirmAge"]
        x[names.index("ForeignOwned")] = means["ForeignOwned"]
        for n in names:
            if n.startswith("sector1_"):
                if int(n.split("_")[1]) == sector_mode:
                    x[names.index(n)] = 1.0
            if n.startswith("wave_") and wave_mode is not None:
                if int(n.split("_")[1]) == wave_mode:
                    x[names.index(n)] = 1.0
        yhat = float(x @ b)
        var = float(x @ cov @ x.T)
        preds.append(yhat)
        ses.append(np.sqrt(max(var, 0.0)))
    return np.array(preds), np.array(ses)


def render_figure_2(waves, pooled):
    fig, axes = plt.subplots(2, 2, figsize=(11, 8.5), sharey=True)
    panels = [(2009, axes[0, 0]), (2015, axes[0, 1]), (2023, axes[1, 0])]

    for year, ax in panels:
        df = waves[year]
        fit, names = fit_inverted_u(df, with_wave_fe=False)
        f_max = min(1.0, df["FSTS"].max())
        grid = np.linspace(0, f_max, 100)
        yhat, se = predict_curve(fit, names, df, grid)

        ax.plot(grid * 100, yhat, color="#1f77b4", linewidth=2.0, label="Predicted lnLP")
        ax.fill_between(grid * 100, yhat - 1.96 * se, yhat + 1.96 * se,
                        color="#1f77b4", alpha=0.18, label="95% CI")

        b1 = fit.params[names.index("FSTSc")]
        b2 = fit.params[names.index("FSTSc2")]
        if b2 < 0:
            tp_c = -b1 / (2 * b2)
            tp_raw = tp_c + df["FSTS"].mean()
            if 0 <= tp_raw <= f_max:
                ax.axvline(tp_raw * 100, color="#d62728", linestyle="--", linewidth=1.2,
                           label=f"Turning point ≈ {tp_raw*100:.1f}%")

        ax.set_title(f"VNM {year}  (N = {len(df):,})", fontsize=11)
        ax.set_xlabel("Direct-export intensity, FSTS (%)")
        ax.set_ylabel("Predicted ln(labour productivity)")
        ax.grid(True, alpha=0.25, linestyle=":")
        ax.legend(fontsize=8, loc="best", frameon=False)

    # Pooled panel ----------------------------------------------------------
    ax = axes[1, 1]
    fit, names = fit_inverted_u(pooled, with_wave_fe=True)
    f_max = min(1.0, pooled["FSTS"].max())
    grid = np.linspace(0, f_max, 100)
    yhat, se = predict_curve(fit, names, pooled, grid)

    ax.plot(grid * 100, yhat, color="#2ca02c", linewidth=2.0, label="Predicted lnLP")
    ax.fill_between(grid * 100, yhat - 1.96 * se, yhat + 1.96 * se,
                    color="#2ca02c", alpha=0.18, label="95% CI")

    b1 = fit.params[names.index("FSTSc")]
    b2 = fit.params[names.index("FSTSc2")]
    tp_c = -b1 / (2 * b2)
    tp_raw = tp_c + pooled["FSTS"].mean()
    ax.axvline(tp_raw * 100, color="#d62728", linestyle="--", linewidth=1.2,
               label=f"Turning point ≈ {tp_raw*100:.1f}%")

    ax.set_title(f"Pooled VNM 2009/2015/2023  (N = {len(pooled):,})", fontsize=11)
    ax.set_xlabel("Direct-export intensity, FSTS (%)")
    ax.set_ylabel("Predicted ln(labour productivity)")
    ax.grid(True, alpha=0.25, linestyle=":")
    ax.legend(fontsize=8, loc="best", frameon=False)

    fig.suptitle(
        "Figure 2. Predicted ln(labour productivity) across direct-export intensity\n"
        "by Vietnam WBES wave and pooled sample (M2 inverted-U specification, HC1 robust)",
        fontsize=12, fontweight="bold",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_FIGS / "figure_2_main_results.pdf")
    fig.savefig(OUT_FIGS / "figure_2_main_results.png", dpi=300)
    plt.close(fig)


def render_figure_1():
    """Conceptual model: black-and-white box diagram for IJoEM-style print.

    Independent variable (Internationalisation, FSTS) on the left, dependent
    variable (Firm performance, lnLP) on the right, both with thick borders.
    Moderators (TCI, DAI) sit above and below the IV-DV spine with thinner
    borders. Controls run across the top in a thin dashed box. All shapes are
    monochrome (black borders, white fill) for greyscale-safe print.
    """
    fig, ax = plt.subplots(figsize=(11.0, 6.6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis("off")

    iv_x, iv_y, iv_w, iv_h = 0.5, 3.4, 3.6, 1.6
    dv_x, dv_y, dv_w, dv_h = 9.9, 3.4, 3.6, 1.6
    ax.add_patch(mpatches.FancyBboxPatch(
        (iv_x, iv_y), iv_w, iv_h, boxstyle="square,pad=0.05",
        linewidth=2.6, edgecolor="black", facecolor="white"))
    ax.text(iv_x + iv_w / 2, iv_y + iv_h / 2 + 0.18,
            "Internationalisation",
            ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(iv_x + iv_w / 2, iv_y + iv_h / 2 - 0.32,
            "(FSTS_c, FSTS_c²)\nIndependent variable",
            ha="center", va="center", fontsize=9, style="italic")

    ax.add_patch(mpatches.FancyBboxPatch(
        (dv_x, dv_y), dv_w, dv_h, boxstyle="square,pad=0.05",
        linewidth=2.6, edgecolor="black", facecolor="white"))
    ax.text(dv_x + dv_w / 2, dv_y + dv_h / 2 + 0.18,
            "Firm performance",
            ha="center", va="center", fontsize=12, fontweight="bold")
    ax.text(dv_x + dv_w / 2, dv_y + dv_h / 2 - 0.32,
            "(ln LP)\nDependent variable",
            ha="center", va="center", fontsize=9, style="italic")

    ax.annotate("", xy=(dv_x, dv_y + dv_h / 2),
                xytext=(iv_x + iv_w, iv_y + iv_h / 2),
                arrowprops=dict(arrowstyle="-|>", lw=2.4, color="black",
                                mutation_scale=20, shrinkA=4, shrinkB=4))
    ax.text((iv_x + iv_w + dv_x) / 2, iv_y + iv_h / 2 + 0.32,
            "H1 (nonlinear, inverted-U)",
            ha="center", va="center", fontsize=10, fontweight="bold",
            bbox=dict(boxstyle="square,pad=0.20", facecolor="white",
                      edgecolor="white"))

    tci_x, tci_y, tci_w, tci_h = 5.6, 6.0, 2.8, 1.0
    dai_x, dai_y, dai_w, dai_h = 5.6, 0.9, 2.8, 1.0
    moderators = [
        (tci_x, tci_y, tci_w, tci_h, "Technological Capability",
         "(TCI_z) — moderator (H2)"),
        (dai_x, dai_y, dai_w, dai_h, "Digital Adoption",
         "(DAI_z) — moderator (H3, H4)"),
    ]
    for (x, y, w, h, label, sublabel) in moderators:
        ax.add_patch(mpatches.FancyBboxPatch(
            (x, y), w, h, boxstyle="square,pad=0.04",
            linewidth=1.2, edgecolor="black", facecolor="white"))
        ax.text(x + w / 2, y + h / 2 + 0.16, label,
                ha="center", va="center", fontsize=10, fontweight="bold")
        ax.text(x + w / 2, y + h / 2 - 0.22, sublabel,
                ha="center", va="center", fontsize=8, style="italic")

    ax.annotate("", xy=((iv_x + iv_w + dv_x) / 2, iv_y + iv_h - 0.15),
                xytext=(tci_x + tci_w / 2, tci_y),
                arrowprops=dict(arrowstyle="->", lw=1.0, color="black",
                                mutation_scale=14))
    ax.annotate("", xy=((iv_x + iv_w + dv_x) / 2, iv_y + 0.15),
                xytext=(dai_x + dai_w / 2, dai_y + dai_h),
                arrowprops=dict(arrowstyle="->", lw=1.0, color="black",
                                mutation_scale=14))

    ax.text(tci_x + tci_w / 2, tci_y - 0.40,
            "moderates curvature", ha="center", va="center",
            fontsize=8, style="italic")
    ax.text(dai_x + dai_w / 2, dai_y + dai_h + 0.40,
            "moderates curvature", ha="center", va="center",
            fontsize=8, style="italic")

    ctrl_x, ctrl_y, ctrl_w, ctrl_h = 0.5, 7.1, 13.0, 0.6
    ax.add_patch(mpatches.FancyBboxPatch(
        (ctrl_x, ctrl_y), ctrl_w, ctrl_h, boxstyle="square,pad=0.04",
        linewidth=0.9, edgecolor="black", facecolor="white",
        linestyle="dashed"))
    ax.text(ctrl_x + ctrl_w / 2, ctrl_y + ctrl_h / 2,
            "Control variables: firm size (lnEmp), firm age (FirmAge), "
            "foreign ownership (ForeignOwned), sector FE; pooled adds wave FE",
            ha="center", va="center", fontsize=9, style="italic")

    ax.text(7.0, 0.10,
            "All paths estimated as OLS HC1 robust associations on three Vietnam "
            "WBES waves\n(2009 N = 989, 2015 N = 956, 2023 N = 1,013, pooled "
            "N = 2,958).",
            ha="center", va="center", fontsize=8, style="italic")

    fig.suptitle("Figure 1. Conceptual model: technological capability and digital "
                 "adoption as moderators\nof the internationalisation–firm "
                 "performance relationship",
                 fontsize=11.5, fontweight="bold", y=0.97)
    fig.tight_layout(rect=(0, 0.02, 1, 0.93))
    fig.savefig(OUT_FIGS / "figure_1_conceptual_model.pdf")
    fig.savefig(OUT_FIGS / "figure_1_conceptual_model.png", dpi=300)
    plt.close(fig)


def main():
    waves = {y: build_wave(y) for y in (2009, 2015, 2023)}
    pooled = build_pooled(waves)
    render_figure_1()
    render_figure_2(waves, pooled)
    print(f"Figures written to {OUT_FIGS}")


if __name__ == "__main__":
    main()
