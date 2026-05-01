#!/usr/bin/env python3
"""
make_figure_1_conceptual.py
===========================
Figure 1 — conceptual model for the v4.4 manuscript.

Renders a path diagram with the four hypothesis arrows:
  H1 — FSTS + FSTS² -> lnLP (inverted-U curvature) and TCI -> lnLP (level)
  H2 — FSTS × TCI, FSTS² × TCI -> lnLP (curvature shift)
  H3 — DAI -> lnLP
  H4 — FSTS × DAI, FSTS² × DAI -> lnLP (curvature shift; sign empirical)

The diagram also shows the controls block (lnEmp, FirmAge, ForeignOwned,
sector FE, wave FE) feeding lnLP. Output: PDF + PNG into ../figures/.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch

OUT = Path(__file__).resolve().parent.parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def draw_box(ax, xy, w, h, text, fc="#FFFFFF", ec="#222222", fontsize=9, bold=False):
    rect = patches.FancyBboxPatch(
        xy, w, h, boxstyle="round,pad=0.02,rounding_size=0.03",
        linewidth=1.4, edgecolor=ec, facecolor=fc,
    )
    ax.add_patch(rect)
    weight = "bold" if bold else "normal"
    ax.text(xy[0] + w / 2, xy[1] + h / 2, text,
            ha="center", va="center", fontsize=fontsize,
            fontweight=weight, color="#111111")


def arrow(ax, src_xy, dst_xy, label="", style="-|>", color="#444444",
          rad=0.0, ls="-", lw=1.2, label_offset=(0, 0.04), fs=8):
    a = FancyArrowPatch(src_xy, dst_xy,
                        arrowstyle=style, mutation_scale=12,
                        connectionstyle=f"arc3,rad={rad}",
                        color=color, linewidth=lw, linestyle=ls)
    ax.add_patch(a)
    if label:
        mx = (src_xy[0] + dst_xy[0]) / 2 + label_offset[0]
        my = (src_xy[1] + dst_xy[1]) / 2 + label_offset[1]
        ax.text(mx, my, label, ha="center", va="center",
                fontsize=fs, color=color,
                bbox=dict(boxstyle="round,pad=0.1",
                          fc="#FFFFFF", ec="none", alpha=0.9))


def main():
    fig, ax = plt.subplots(figsize=(10.5, 6.2), dpi=150)
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 6.2)
    ax.set_axis_off()

    # Title
    ax.text(5.25, 5.95,
            "Figure 1. Conceptual model — TCI, DAI, and the I–P relationship",
            ha="center", va="center", fontsize=12, fontweight="bold")

    # ---- LEFT: predictors ----
    # Internationalisation block
    draw_box(ax, (0.3, 4.3), 2.0, 0.55,
             "FSTS\n(direct-export intensity)", fc="#E8F1FB", bold=True)
    draw_box(ax, (0.3, 3.55), 2.0, 0.55,
             "FSTS²\n(curvature, H1)", fc="#E8F1FB")

    # TCI block
    draw_box(ax, (0.3, 2.5), 2.0, 0.55,
             "TCI\n(b8, e6 — Lall capability)", fc="#FFF1E0", bold=True)

    # DAI block
    draw_box(ax, (0.3, 1.45), 2.0, 0.55,
             "DAI\n(c22b — Bharadwaj/Verhoef)", fc="#E5F4E5", bold=True)

    # Interactions block
    draw_box(ax, (3.4, 4.05), 2.6, 0.7,
             "FSTS × TCI,  FSTS² × TCI\n(H2 — curvature shift)", fc="#FFF1E0")
    draw_box(ax, (3.4, 1.4), 2.6, 0.7,
             "FSTS × DAI,  FSTS² × DAI\n(H4 — curvature shift; sign empirical)",
             fc="#E5F4E5")

    # Controls block
    draw_box(ax, (0.3, 0.2), 5.7, 0.7,
             "Controls: lnEmp, FirmAge, ForeignOwned  |  Sector FE  |  Wave FE",
             fc="#F4F4F4")

    # Outcome
    draw_box(ax, (7.6, 2.85), 2.5, 1.0,
             "lnLP\n(log labour productivity)\n= ln(d2 / l1)",
             fc="#FDE9E9", bold=True, fontsize=10)

    # ---- arrows ----
    # H1 curvature: FSTS + FSTS² -> lnLP
    arrow(ax, (2.3, 4.55), (7.6, 3.5), label="H1 (curvature)",
          color="#1F4E79", rad=-0.1, label_offset=(0.0, 0.18))
    arrow(ax, (2.3, 3.85), (7.6, 3.30), color="#1F4E79", rad=-0.05)

    # H1 TCI direct
    arrow(ax, (2.3, 2.78), (7.6, 3.30), label="H1 (TCI direct)",
          color="#A0522D", label_offset=(0.0, 0.14))

    # H2 moderation
    arrow(ax, (3.4, 4.40), (2.3, 4.55), color="#A0522D", rad=0.2,
          ls="--", lw=1.0)
    arrow(ax, (3.4, 4.40), (2.3, 2.78), color="#A0522D", rad=-0.2,
          ls="--", lw=1.0)
    arrow(ax, (6.0, 4.40), (7.6, 3.55), label="H2 (moderation)",
          color="#A0522D", rad=0.05, label_offset=(0.0, 0.12))

    # H3 DAI direct
    arrow(ax, (2.3, 1.73), (7.6, 3.10), label="H3 (DAI direct)",
          color="#2E7D32", rad=0.15, label_offset=(-0.4, 0.18))

    # H4 moderation
    arrow(ax, (3.4, 1.75), (2.3, 4.55), color="#2E7D32", rad=-0.2,
          ls="--", lw=1.0)
    arrow(ax, (3.4, 1.75), (2.3, 1.73), color="#2E7D32", rad=0.2,
          ls="--", lw=1.0)
    arrow(ax, (6.0, 1.75), (7.6, 3.10), label="H4 (moderation)",
          color="#2E7D32", rad=-0.05, label_offset=(0.0, -0.18))

    # Controls -> lnLP
    arrow(ax, (5.3, 0.55), (7.6, 2.95), color="#666666", rad=-0.08,
          label="controls", fs=7, label_offset=(0.5, 0.05))

    # Legend
    ax.text(0.3, 5.55,
            "Notes. Solid arrows: direct effects. Dashed arrows: terms entering "
            "interaction products.\nWithin-wave z-standardisation applied to TCI and DAI; "
            "FSTS centred within wave.\nAll specifications estimated by OLS-HC1; "
            "see §3 for verification protocol.",
            ha="left", va="top", fontsize=8, color="#444444")

    fig.savefig(OUT / "figure_1_conceptual_model.pdf",
                bbox_inches="tight", pad_inches=0.05)
    fig.savefig(OUT / "figure_1_conceptual_model.png",
                bbox_inches="tight", pad_inches=0.05, dpi=200)
    print(f"[ok] Figure 1 -> {OUT/'figure_1_conceptual_model.pdf'}")


if __name__ == "__main__":
    main()
