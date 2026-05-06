# Figures 2, 3, 4 — P5 China rendered from verified replication

This directory contains the rendering script for Figures 2, 3, and 4. The script encodes verified replication coefficients (from `results/M2_table.csv`, `results/results_coefs.csv`, and `results/three_way_moderation.csv`) and generates publication-quality PNG + SVG outputs.

## Quick render

```bash
pip install matplotlib numpy
python3 render_figures.py
```

Outputs (300 dpi PNG + vector SVG):
- `figure2_threshold_forest.{png,svg}` — forest plot, M2 turning points 2012/2024/pooled with 95 % CI + safe-zone shading + Paternoster annotation
- `figure3_predicted_curves.{png,svg}` — predicted ln(LP) curves overlay 2012 vs 2024 with shaded confidence bands and safe operating zone
- `figure4_level_shift_bars.{png,svg}` — TCI / DAI direct level-shift bars with 95 % CI by wave

## What each figure shows

### Figure 2 — turning-point forest plot

| Wave | Turning point | 95 % CI | N |
|---|---|---|---|
| 2012 | **49.4 %** | [43.2 %, 55.6 %] | 2,610 |
| 2024 | **47.2 %** | [34.5 %, 59.9 %] | 1,934 |
| Pooled | **48.8 %** | [42.7 %, 54.9 %] | 4,544 |

Annotation box reports Paternoster z-tests (FSTS p = .412, FSTS² p = .545) + joint F-test (F(2, 3558) = 2.24, p = .107) showing **equality NOT rejected → unexpected stability finding (predicted shift not detected)**.

### Figure 3 — predicted curves overlay

Two near-parallel inverted-U curves (2012 blue, 2024 red), both peaking inside the 30-60 % safe zone. 2024 is level-shifted upward by ~0.24 log points (productivity growth) but with **identical curvature** — visualizes the structural durability finding.

### Figure 4 — TCI / DAI level-shift bars

| Construct | 2012 β (SE) | 2024 β (SE) | Pooled β (SE) |
|---|---|---|---|
| TCI (tech capability) | +0.276 (0.043) | +0.426 (0.047) | +0.361 (0.032) |
| DAI (digital adoption) | +0.077 (0.027) | +0.188 (0.044) | +0.115 (0.024) |

Annotation: Paternoster cross-wave on TCI (z = −2.55, p = .011) showing strengthening 2012 → 2024.

## How to embed in manuscript .docx

1. Render: `python3 render_figures.py`
2. Open Word/Overleaf at the Figure 2/3/4 placeholders
3. Insert SVG (preferred for vector scaling) or 300-dpi PNG
4. Verify font legibility (≥ 10 pt body, ≥ 8.5 pt annotations)
5. Cross-reference with `manuscript_v1_4_part4_results.md` Figure captions

## Source for plotted values

All coefficients hard-coded in `render_figures.py` are pulled from:
- `results/M2_table.csv` — wide-format M2 main threshold table
- `results/results_coefs.csv` — long-format M0–M8 coefficients (51 rows)
- `results/three_way_moderation.csv` — joint F-tests for shift / moderation / dynamic moderation

If you re-run `python/full_models.py` and `python/three_way_moderation.py` against fresh data and get materially different numbers, update the hard-coded dicts in `render_figures.py` (`m2`, `turning`, `paternoster`, `levels`) to match.
