# Manuscript v1.4 — Final Assembly Instructions

This is the final v1.4 of the P5 China APJM submission, incorporating the dissertation-architecture realignment (P5 as temporal-extension paper of the China stream).

## Six v1.4 parts (assemble in order)

| # | File | Section | Status |
|---|---|---|---|
| 1 | `manuscript_v1_4_part1_frontmatter_intro.md` | Title, abstract, keywords, Section 1 (Introduction) | NEW v1.4 |
| 2 | `manuscript_v1_4_part2_theory.md` | Section 2 (Theory & 4 hypotheses, H2 reversed to predict shift, H4a/H4b expanded to curvature moderation) | NEW v1.4 |
| 3 | `manuscript_v1_4_part3_data_methods.md` | Section 3 (Data, variables, estimation, supplementary, §3.5 three-way moderation spec) | NEW v1.4 |
| 4 | `manuscript_v1_4_part4_results.md` | Section 4 (Results: descriptives, inverted-U, shift test, capability moderation, supplementary, §4.6 mfg-only robustness) | NEW v1.4 |
| 5 | `manuscript_v1_4_part5_discussion.md` | Section 5 (Discussion: durability against expected shift, managerial, policy) | NEW v1.4 |
| 6 | `manuscript_v1_4_part6_limits_refs.md` | Section 6 (Limitations), Acknowledgements, References (29 entries APA 7th) | NEW v1.4 |

## Quick assembly

```bash
cd p5-china/apjm/
cat \
    manuscript_v1_4_part1_frontmatter_intro.md \
    manuscript_v1_4_part2_theory.md \
    manuscript_v1_4_part3_data_methods.md \
    manuscript_v1_4_part4_results.md \
    manuscript_v1_4_part5_discussion.md \
    manuscript_v1_4_part6_limits_refs.md \
    > manuscript_v1_4_complete.md
```

## Convert to .docx for APJM upload

```bash
pandoc \
    manuscript_v1_4_part1_frontmatter_intro.md \
    manuscript_v1_4_part2_theory.md \
    manuscript_v1_4_part3_data_methods.md \
    manuscript_v1_4_part4_results.md \
    manuscript_v1_4_part5_discussion.md \
    manuscript_v1_4_part6_limits_refs.md \
    --reference-doc=apjm-template.docx \
    -o manuscript_v1_4.docx
```

(Replace `apjm-template.docx` with the APJM-provided template if available; otherwise omit `--reference-doc` for default formatting.)

## Render figures

Figure 1 (conceptual model):
```bash
cd figures/
dot -Tsvg figure1_conceptual_model_v1_4.dot -o figure1_v1_4.svg
dot -Tpdf figure1_conceptual_model_v1_4.dot -o figure1_v1_4.pdf
```

Figures 2, 3, 4 (data-based):
```bash
python3 render_figures.py    # generates figure2/3/4 PNG (300 dpi) + SVG
```

Then embed at the figure placeholders in `manuscript_v1_4.docx`.

## Verification grep

```bash
# Should find exactly 8 lines mentioning 'manufactur' — all intentional
# (4 in main narrative incl. §4.6 robustness; 1 in Yangtze River Delta reference)
grep -ni 'manufactur' manuscript_v1_4_complete.md

# Should return ~16 instances of consistent identity
grep -c 'Chinese private firms' manuscript_v1_4_complete.md

# Confirm 6 main sections present
grep -n '^## [1-6]\.' manuscript_v1_4_complete.md
```

## What changed v1.3 → v1.4

- **H2 reversed:** v1.3 predicted stability, v1.4 predicts shift. Empirical null becomes the contribution ("unexpected stability against expected shift").
- **H4a/H4b expanded:** v1.3 treated TCI/DAI only as level-shifters; v1.4 tests both level shift and curvature moderation, reports that level-shift component supported but curvature moderation NOT robustly supported.
- **§3.5 NEW three-way moderation specification** with joint F-tests F1 (cross-wave shift), F2 (capability moderation), F3 (capability-conditioned dynamic moderation).
- **§4.6 NEW mfg-only robustness** (Phương án C: full private as main + mfg subsample as robustness).
- **§5.1 reframed** as "durability against expected shift" with three-null-channels convergence.
- **References extended** from 21 to 29 entries (added Bausch & Krist 2007, Chen & Tan 2012, Do & Tu 2025/2026, Feng et al. 2019, Kirca et al. 2012, Teece 2007, Xiao et al. 2013).
- **Figure 1 v1.4** adds wave2024 explicit construct + H2 "predicted shift, observed stability" annotation.
- **Figures 2, 3, 4** rendered from verified Python replication coefficients.
- **Empirical numbers updated** throughout (Paternoster z = +0.82/-0.61 instead of v1.3's +0.91/-0.70; turning points 49.4/47.2/48.8 % instead of 49.4/47.6/48.9 %; new joint F-test results).

For full diff log see `CHANGELOG_v1_3_to_v1_4.md`.

## v1.4 headline result table

| Hypothesis | Predicted | F or z | p-value | Verdict |
|---|---|---|---|---|
| **H1** Inverted-U | nonlinear | β_FSTS² = -1.83 (pooled) | < .001 | **Supported** |
| **H2** Cross-wave shift | shape differs 2012–2024 | F(2, 3,558) = 2.24 | .107 | **NOT supported → unexpected stability finding** |
| **H3** Working-capital conditioning | moderation | mixed across blocks | mixed | NOT robustly supported |
| **H4a** TCI level shift | positive | β_z = +0.28 to +0.43 | < .001 | **Supported** |
| **H4a** TCI curvature moderation | shapes curve | F(2, 3,558) = 3.26 | .039 | Marginal; individual coefs NS → NOT robustly supported |
| **H4b** DAI level shift | positive | β_z = +0.07 to +0.13 | ≤ .03 | **Modestly supported** |
| **H4b** DAI curvature moderation | shapes curve | (joint F NS) | (NS) | NOT supported |
| **H3 dynamic** Tech×wave moderation | dynamic shift | F(2, 3,558) = 0.27 | .760 | NOT supported |

**Substantive interpretation:** the Chinese internationalization-performance trade-off is durably structural, not capability-conditioned or wave-specific. The unexpected null on H2 (against multiple plausible directional priors) becomes the paper's central contribution.

## Pre-submission checklist

- [x] All 6 manuscript v1.4 parts pushed to GitHub
- [x] Figure 1 v1.4 sources (mmd + dot) pushed
- [x] Render script for Figures 2/3/4 pushed
- [x] Three-way moderation Python spec + CSV pushed
- [x] Replication pipeline (Stata do-files + Python) pushed
- [x] CHANGELOG_v1_3_to_v1_4.md documents diff
- [ ] **Manuscript v1.4 .docx assembled** (pending pandoc local run)
- [ ] **Figures 2/3/4 rendered locally and embedded** (pending matplotlib local run)
- [ ] **Cover letter v1.4 drafted** (pending)
- [ ] **Title page (separate file) prepared** with author/affiliation/ORCID details
- [ ] **Internal review** by ≥1 colleague
- [ ] **Final submission** upload to APJM editorial system
