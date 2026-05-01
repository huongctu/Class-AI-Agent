#!/usr/bin/env python3
"""
make_figure_1_conceptual.py
===========================
Figure 1 — conceptual model for P5 manuscript_p5_v1 (Option C+).

Renders a path diagram with the four hypothesis blocks:
  H1 — FSTS + FSTS² → lnLP (inverted-U curvature; threshold)
  H2 — cross-wave stability of the H1 turning point (2012 ↔ 2024)
  H3 — Working-capital × FSTS² → lnLP (post-threshold conditioning;
       sign theory-permissive negative under stress framing)
  H4a — TCI → lnLP (level-shift; technological capability)
  H4b — DAI → lnLP (level-shift; digital adoption)

P5 architectural rule (Option C+):
  Threshold-stability is the central contribution; WC and digital are
  secondary. H3 is reported as exploratory (β = NULL in pipeline) and
  drawn with a dashed border to signal interpretive status.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch

OUT = Path(__file__).resolve().parent.parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def draw_box(ax, xy, w, h, text, fc="#FFFFFF", ec="#222222",
             fontsize=9, bold=False, ls="-", lw=1.4):
    rect = patches.FancyBboxPatch(
        xy, w, h, boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=lw, edgecolor=ec, facecolor=fc, linestyle=ls,
    )
    ax.add_patch(rect)
    weight = "bold" if bold else "normal"
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text,
            ha="center", va="center", fontsize=fontsize,
            fontweight=weight, color="#111111")


def arrow(ax, src, dst, label="", color="#444444", rad=0.0,
          ls="-", lw=1.2, label_offset=(0, 0.05), fs=8,
          style="-|>"):
    a = FancyArrowPatch(src, dst,
                        arrowstyle=style, mutation_scale=12,
                        connectionstyle=f"arc3,rad={rad}",
                        color=color, linewidth=lw, linestyle=ls)
    ax.add_patch(a)
    if label:
        mx = (src[0] + dst[0]) / 2 + label_offset[0]
        my = (src[1] + dst[1]) / 2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=fs, color=color,
                bbox=dict(boxstyle="round,pad=0.15",
                          fc="#FFFFFF", ec="none", alpha=0.92))


def main():
    fig, ax = plt.subplots(figsize=(11.0, 7.0), dpi=150)
    ax.set_xlim(0, 11.0)
    ax.set_ylim(0, 7.0)
    ax.set_axis_off()

    # Title
    ax.text(5.5, 6.75,
            "Figure 1. Conceptual model — Threshold stability and bounded "
            "internationalisation–performance",
            ha="center", va="center", fontsize=11, fontweight="bold")
    ax.text(5.5, 6.40,
            "Chinese manufacturing SMEs (WBES 2012 + 2024)",
            ha="center", va="center", fontsize=10, fontweight="normal", color="#444")

    # Architectural note (top-left)
    ax.text(0.30, 5.95,
            "P5 architecture (Option C+): threshold stability is the central contribution;\n"
            "working-capital conditioning (H3) and digital adoption (H4b) are secondary explanatory layers.",
            ha="left", va="top", fontsize=8, color="#1F4E79", fontweight="bold")

    # ---- LEFT column: predictors ----
    draw_box(ax, (0.3, 4.55), 2.2, 0.55,
             "Export intensity (FSTS)\nshare of foreign sales", fc="#E8F1FB", bold=True, fontsize=8)
    draw_box(ax, (0.3, 3.80), 2.2, 0.55,
             "FSTS² (curvature)\ninverted-U downturn", fc="#E8F1FB", fontsize=8)
    draw_box(ax, (0.3, 2.85), 2.2, 0.55,
             "TCI — technological capability\n(Lall 1992; Cohen-Levinthal 1990)",
             fc="#FFF1E0", bold=True, fontsize=8)
    draw_box(ax, (0.3, 2.05), 2.2, 0.55,
             "DAI — digital adoption (thin)\n(Bharadwaj 2013; Verhoef 2021)",
             fc="#E5F4E5", bold=True, fontsize=8)

    # ---- MIDDLE column: H3 working-capital conditioning (secondary, dashed border) ----
    draw_box(ax, (3.50, 3.95), 2.8, 1.05,
             "Working-capital condition (H3)\n"
             "Liquidity access: k7, k8/k82\n"
             "Financing structure: k3a, k3bc, k3f\n"
             "Access-to-finance obstacle: k30",
             fc="#F8F0F4", ls="--", lw=1.5, fontsize=7.5)

    # Controls block (lower middle)
    draw_box(ax, (3.50, 0.55), 2.8, 0.65,
             "Controls\nlnEmp · firm age · foreign-ownership dummy\n(pooled: + wave FE)",
             fc="#F4F4F4", fontsize=8)

    # ---- RIGHT: Outcome + H2 stability annotation ----
    draw_box(ax, (8.0, 3.20), 2.6, 1.0,
             "lnLP\nlog labour productivity\n= ln(d2 / l1)",
             fc="#FDE9E9", bold=True, fontsize=10)
    draw_box(ax, (8.0, 4.95), 2.6, 0.70,
             "H2 — Threshold stability\nacross 2012 and 2024\n(Paternoster z-test ns)",
             fc="#E0EBF6", ls=":", lw=1.4, fontsize=8)

    # ---- Arrows ----
    # H1 — FSTS + FSTS² → lnLP (curvature)
    arrow(ax, (2.5, 4.82), (8.0, 4.00),
          label="H1 (inverted-U curvature)",
          color="#1F4E79", rad=-0.10, label_offset=(0.0, 0.20))
    arrow(ax, (2.5, 4.07), (8.0, 3.55),
          color="#1F4E79", rad=-0.04, lw=1.0)

    # H2 — link from outcome up to stability box (visual indicator)
    arrow(ax, (9.30, 4.20), (9.30, 4.95),
          color="#1F4E79", lw=1.2, ls=":", style="<->")

    # H3 — WC × FSTS² → curvature shift (post-threshold conditioning)
    arrow(ax, (6.30, 4.45), (8.0, 3.95),
          label="H3 (post-threshold\nconditioning; sign empirical)",
          color="#A0522D", rad=0.05, ls="--", lw=1.2,
          label_offset=(0.05, 0.20), fs=7.5)

    # H4a TCI → lnLP level shift
    arrow(ax, (2.5, 3.13), (8.0, 3.55),
          label="H4a (TCI level shift)",
          color="#A0522D", rad=0.05, label_offset=(0.0, 0.18))

    # H4b DAI → lnLP level shift
    arrow(ax, (2.5, 2.32), (8.0, 3.30),
          label="H4b (DAI level shift)",
          color="#2E7D32", rad=0.10, label_offset=(0.0, -0.22))

    # Controls → lnLP
    arrow(ax, (5.7, 0.95), (8.0, 3.10),
          color="#666666", rad=-0.06, lw=1.0)
    ax.text(7.0, 1.85, "controls", fontsize=7.5, color="#666666",
            rotation=55, va="center")

    # Notes (bottom)
    ax.text(0.30, 0.30,
            "Notes. Solid arrows: directional hypotheses (H1 / H4a / H4b). "
            "Dashed arrow: H3 reported as exploratory in §4.5 — direct working-capital conditioning of the\n"
            "post-threshold downturn classified as NULL; interpretation retained as theoretically grounded "
            "mechanism. Dotted double-headed arrow links the H1\n"
            "curvature finding to the H2 cross-wave stability test. All specifications estimated by "
            "OLS-HC1; see §3 for variable construction and verification protocol.",
            ha="left", va="bottom", fontsize=7.3, color="#444444")

    fig.savefig(OUT / "figure_1_conceptual_model.pdf",
                bbox_inches="tight", pad_inches=0.05)
    fig.savefig(OUT / "figure_1_conceptual_model.png",
                bbox_inches="tight", pad_inches=0.05, dpi=200)
    print(f"[ok] Figure 1 → {OUT/'figure_1_conceptual_model.pdf'}")


if __name__ == "__main__":
    main()
