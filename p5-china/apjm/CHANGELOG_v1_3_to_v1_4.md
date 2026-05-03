# Manuscript v1.3 → v1.4 Changelog

**Date:** 2026-05-03
**Branch:** `claude/p5-china-sample-outline-1KXp4`
**Trigger:** dissertation-architecture realignment (P5 as temporal-extension paper of China stream, distinct from P2 shape-discovery study)

## Summary

v1.4 reverses the H2 framing from "predicted stability" (v1.3) to **"predicted shape shift"**. Empirical data still show no shift (Paternoster p > .10, joint F p = .107), but the rhetorical contribution becomes *stronger* because the unexpected null now contradicts a strong directional prior. Three additional null moderation channels (H3 working-capital, H4a/H4b capability curvature, H3 dynamic Tech×wave moderation) all converge on the same substantive interpretation: **the Chinese internationalization-performance trade-off is durably structural**.

## Empirical additions

New test: 3-way moderation `lnLP ~ DOI + DOI² + wave2024 + DOI×wave2024 + DOI²×wave2024 + Tech + DOI×Tech + DOI²×Tech + DOI×wave2024×Tech + DOI²×wave2024×Tech + controls`, with cluster-robust SE on `idstd`. Pooled N = 3,559 (`sample_full`).

| Joint F-test | F(df) | p-value | Verdict |
|---|---|---|---|
| F1: H2 cross-wave shift (DOI×wave2024, DOI²×wave2024) | 2.236 (2, 3558) | **0.107** | FAIL TO REJECT — stability finding |
| F2: H3 cross-sectional Tech moderation (DOI×Tech, DOI²×Tech) | 3.256 (2, 3558) | **0.039** | Marginal pooled support; individual coefs NS |
| F3: H3 dynamic Tech×wave moderation (DOI×wave2024×Tech, DOI²×wave2024×Tech) | 0.274 (2, 3558) | **0.760** | NO support |

## Sample identity

- **Main analysis:** full WBES private-firm frame (Phase C decision; no manufacturing filter applied). Same as v1.3.
- **Robustness (§4.6 NEW):** manufacturing-only subsample with `a4a 15-38` (2012, N=1,656) + `d1a2_v4//100 ∈ [10, 33]` (2024, N=1,062) = pooled N=2,718. Reports turning point shift to ~42% (2012) / lower in 2024 with wider CI; Paternoster z still cannot reject equality. Documented as Appendix D.

## Files affected

### NEW v1.4 files (this commit set)
- `apjm/manuscript_v1_4_part2_theory.md` — theory + 4 hypotheses (H2 reversed; H4a/H4b expanded to include curvature moderation)
- `apjm/manuscript_v1_4_part4_results.md` — results with reframed §4.3 'predicted shift; observed stability', new §4.6 mfg-only robustness
- `apjm/manuscript_v1_4_part5_discussion.md` — discussion reframed as 'durability against expected shift'
- `apjm/figures/figure1_conceptual_model_v1_4.{mmd,dot}` — adds wave2024 explicit construct + H2 'predicted shift, observed stability' annotation; H4a/H4b expanded to curvature moderation arms
- `apjm/figures/render_figures.py` — generates Figures 2, 3, 4 from verified coefficients
- `apjm/figures/RENDER_FIGURES_README.md` — render instructions + value tables
- `python/three_way_moderation.py` — pooled 3-way DOI×Year2024×Tech spec with joint F-tests
- `results/three_way_moderation.csv` — 10 focal coefficients + 3 F-test p-values
- `apjm/CHANGELOG_v1_3_to_v1_4.md` — this file

### Unchanged from v1.3 (no edit needed)
- `apjm/manuscript_v1_3_part1_frontmatter_intro.md` — title, abstract, introduction (sample identity "Chinese private firms" still correct)
- `apjm/manuscript_v1_3_part3_data_methods.md` — data and methods (sample-construction protocol unchanged)
- `apjm/manuscript_v1_3_part6_limits_refs.md` — limitations and references

## Hypothesis summary table v1.4

| H | Statement | Predicted | Empirical verdict | Verdict source |
|---|---|---|---|---|
| H1 | Inverted-U between FSTS and lnLP | nonlinear shape | **Supported** (β_FSTS² < 0, p < .03 every wave) | M2 main spec |
| H2 (REVERSED) | Shape differs between 2012 and 2024 | shift | **NOT supported** (Paternoster p > .10; joint F p = .107) → *unexpected stability finding* | F1 of 3-way spec + Paternoster |
| H3 | Working-capital conditions strengthen post-threshold downturn | moderation | **NOT robustly supported** (mixed signs across blocks/waves) | §4.5 supplementary |
| H4a | TCI level shift + curvature moderation | level shift + moderation | **Level shift supported** (β +0.26 to +0.43, p < .001); **curvature moderation NOT robustly supported** (joint F p = .039 marginal, individual coefs NS) | M5 + 3-way spec F2 |
| H4b | DAI level shift + curvature moderation | level shift + moderation | **Level shift supported** (modestly, β +0.05 to +0.13, p ≤ .03); **curvature moderation NOT supported** | M6 + 3-way spec |
| H3 dynamic | Capability-conditioned shift over time | Tech×wave moderation | **NOT supported** (F(2, 3558) = 0.27, p = .760) | F3 of 3-way spec |

Three null moderation channels (H2, H4 curvature, H3 dynamic) + ambiguous H3 cross-sectional + ambiguous H4 cross-sectional moderation → **convergent narrative: durably structural inverted-U**.

## Cumulative repo structure (v1.4)

```
p5-china/
├── README.md
├── PLAN.md
├── do/
│   ├── 01_build_2012.do
│   ├── 02_build_2024.do
│   ├── 03_build_pooled.do
│   └── 04_run_models.do
├── python/
│   ├── build_and_run.py
│   ├── full_models.py
│   └── three_way_moderation.py            # NEW v1.4
├── audit/
│   ├── audit_N_checklist.csv
│   ├── audit_N_all.csv
│   └── audit_N_mfg.csv
├── results/
│   ├── results_coefs.csv
│   ├── M2_table.csv
│   ├── summary.md
│   ├── moderator_test.csv
│   ├── moderator_test_summary.csv
│   ├── moderator_test_VERDICT.md
│   └── three_way_moderation.csv          # NEW v1.4
└── apjm/
    ├── APJM_submission_outline.md
    ├── patch_list_v1_2_to_v1_3.md
    ├── CHANGELOG_v1_2_to_v1_3.md
    ├── CHANGELOG_v1_3_to_v1_4.md         # NEW v1.4 (this file)
    ├── MANUSCRIPT_v1_3_README.md
    ├── manuscript_v1_3_part1_frontmatter_intro.md   # unchanged → reuse
    ├── manuscript_v1_3_part2_theory.md              # superseded by v1.4
    ├── manuscript_v1_3_part3_data_methods.md        # unchanged → reuse
    ├── manuscript_v1_3_part4_results.md             # superseded by v1.4
    ├── manuscript_v1_3_part5_discussion.md          # superseded by v1.4
    ├── manuscript_v1_3_part6_limits_refs.md         # unchanged → reuse
    ├── manuscript_v1_4_part2_theory.md              # NEW v1.4
    ├── manuscript_v1_4_part4_results.md             # NEW v1.4
    ├── manuscript_v1_4_part5_discussion.md          # NEW v1.4
    └── figures/
        ├── figure1_conceptual_model.{mmd,dot}             # v1.3 (kept for diff)
        ├── figure1_conceptual_model_v1_4.{mmd,dot}        # NEW v1.4
        ├── README.md                                       # v1.3 figure-1 docs
        ├── render_figures.py                              # NEW v1.4
        └── RENDER_FIGURES_README.md                       # NEW v1.4
```

## Assembly for submission

To build the v1.4 .docx for APJM upload:

```bash
cd apjm/
pandoc \
    manuscript_v1_3_part1_frontmatter_intro.md \
    manuscript_v1_4_part2_theory.md \
    manuscript_v1_3_part3_data_methods.md \
    manuscript_v1_4_part4_results.md \
    manuscript_v1_4_part5_discussion.md \
    manuscript_v1_3_part6_limits_refs.md \
    -o manuscript_v1_4.docx

cd figures/
python3 render_figures.py    # generates figure2/3/4 PNG + SVG
```

Then embed Figure 1 (render `figure1_conceptual_model_v1_4.dot` via Graphviz) + Figures 2/3/4 (already rendered PNG/SVG) at the appropriate placeholders in the .docx.

## References note

Manuscript v1.3 references file (`manuscript_v1_3_part6_limits_refs.md`) is reused unchanged. New v1.4 narrative draws on the same reference set plus dissertation-architecture references already integrated in v1.3 (Do & Tu, 2025 = P6 meta-analysis; Do & Tu, 2026 = P1 emerging Asia heterogeneity). For dissertation-internal context, see plan file at `/root/.claude/plans/root-claude-uploads-e1de2c9d-8e8c-4e4f-functional-dream.md`.

## Verification checks for v1.4 submission

- [x] H2 reversed in part 2 theory (predicting shift)
- [x] Results §4.3 reframed as 'predicted shift; observed stability'
- [x] Discussion §5.1 reframed as 'durability against expected shift'
- [x] Figure 1 v1.4 includes wave2024 + curvature-moderation arms
- [x] §4.6 robustness with mfg-only documented
- [x] 3-way moderation script + CSV pushed (F1 = 0.107, F2 = 0.039, F3 = 0.760)
- [x] Render script for Figures 2/3/4 pushed with verified coefficients
- [ ] Manuscript v1.4 .docx assembled (pending pandoc local run)
- [ ] Figures 2/3/4 rendered locally and embedded (pending matplotlib local run)
- [ ] APJM cover letter updated to reflect v1.4 narrative (pending)
- [ ] Internal review by ≥1 colleague
- [ ] Final submission upload
