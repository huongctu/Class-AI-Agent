# P5 China — APJM v1.8

> Status: **v1.8 + Avenyo DOI fix → ready APJM submission**
> Last update: 2026-05-06
> Source branch (archive): [`claude/p5-china-sample-outline-1KXp4`](https://github.com/huongctu/Class-AI-Agent/tree/claude/p5-china-sample-outline-1KXp4)

## Manuscript info

| Item | Value |
|---|---|
| **Title** | The Export Intensity–Performance Relationship in Chinese Private Firms: A Threshold-Stability Perspective |
| **Target journal** | **Asia Pacific Journal of Management** (APJM), Springer |
| **Tier** | ABS 3, SSCI Q2 |
| **Authors** | Đỗ Thùy Hương, Phan Anh Tú |
| **Data** | WBES China 2012 + 2024 (2 waves) + 217 panel firms common to both |
| **Sample** | ~2,400 (2012); ~2,400 (2024); 217 panel firms |
| **Method** | OLS HC1 with HC1/HC3 robust SEs; threshold-stability test; capability moderation; three-way moderation; manufacturing-only robustness |
| **Word count** | 13,146 words main text |
| **References** | 39 APA 7th with DOIs (verified Tier A: 22, Tier B: 8, Tier C: 10, Tier D: 2 — closed audit 42/42) |

## File map

```
p5-china/
├── README.md                                     # this file
├── manuscript/
│   ├── manuscript_v1_8_blinded.docx              # compiled output (768 KB) (USE THIS)
│   ├── parts/                                    # 6 markdown source parts
│   │   ├── manuscript_v1_8_blinded_part1_frontmatter_intro.md
│   │   ├── manuscript_v1_8_blinded_part2_theory.md
│   │   ├── manuscript_v1_8_blinded_part3_data_methods.md
│   │   ├── manuscript_v1_8_blinded_part4_results.md
│   │   ├── manuscript_v1_8_blinded_part5_discussion.md
│   │   └── manuscript_v1_8_blinded_part6_limits_refs.md
│   └── build_docx.sh                             # one-shot pandoc build
├── submission/
│   ├── 00_SUBMISSION_CHECKLIST.md
│   ├── 01_title_page.md
│   ├── 02_cover_letter.md
│   ├── 03_declarations.md
│   ├── 04_blinding_check.md
│   └── 05_suggested_reviewers.md
├── figures/
│   ├── figure1_conceptual_model.png              # Graphviz output (regenerated)
│   ├── figure2_threshold_forest.png              # matplotlib
│   ├── figure3_predicted_curves.png              # matplotlib
│   ├── figure4_level_shift_bars.png              # matplotlib
│   └── source/
│       ├── figure1_conceptual_model_v1_4.dot     # Graphviz source
│       ├── figure1_conceptual_model_v1_4.mmd     # Mermaid alternative
│       ├── render_figures.py                     # matplotlib for figs 2-4
│       ├── README.md
│       └── RENDER_FIGURES_README.md
├── tables/
│   └── README.md                                 # tables embedded inline; export procedure documented
├── replication/
│   ├── README.md
│   └── data_source.md                            # WBES China mapping
└── audit/
    ├── CITATION_AUDIT.md                         # 42/42 verified (closed)
    ├── CLAIMS_AUDIT.md
    ├── VERIFICATION_RESULTS.md                   # per-reference verification table
    └── SUBMISSION_TARGETS.md                     # APJM + alternatives
```

## Hypothesis structure

- **H1** (inverted-U): FSTS has inverted U-shaped relationship with firm performance among Chinese private firms
- **H2** (temporal shift): Shape of the inverted U differs between 2012 and 2024 waves, reflecting changes in operating environment
- **H3** (working-capital moderation): Adverse working-capital conditions strengthen the negative post-threshold segment
- **H4a** (TCI moderation): Higher technological capability moderates the curvature of the inverted U-shaped I–P relationship
- **H4b** (DAI moderation): Higher digital adoption moderates the curvature of the inverted U-shaped I–P relationship

## Key findings — Threshold-Stability claim

The central empirical contribution: **the location and shape of the inverted-U threshold remains structurally similar across two repeated cross-sectional samples (2012 and 2024) despite the intervening decade of substantial economic change in China**.

- 2012 wave M2: positive linear FSTS, negative quadratic FSTS² → inverted-U confirmed
- 2024 wave M2: similar curvature pattern with comparable turning point
- Cross-wave coefficient differences: not statistically significant (Paternoster z-tests)
- TCI moderation: positive direct effect; curvature moderation marginal
- DAI moderation: weaker than TCI; only Tier-1 (website) operationalised
- Three-way DOI × wave × Tech interaction: joint F = 0.27, p = .760 (no significant dynamic moderation)

This is interpreted as **cross-sectional structural similarity** rather than within-firm temporal stability (panel needed for the latter).

## Construct measurement (TCI vs DAI orthogonality)

P5 makes a deliberate choice to keep TCI and DAI **operationally orthogonal**:

- **TCI_full**: 4 binary indicators — foreign-licensed technology (e6), quality certification (b8), product innovation (h1), R&D activity (h8)
- **DAI_core**: 1 binary indicator — own-website presence (c22b)

No shared items. Cross-construct correlation is low. This is more conservative than P3 (Singapore) which uses a broader DAI; P5's narrow DAI_core is a deliberate trade-off for cross-wave comparability (since 2012 schema lacks B-READY 2023 e-payment items).

## Avenyo (2021) DOI fix (only patch since v1.8 build)

- **Old (v1.8)**: `10.1057/s41287-020-00269-w` ❌
- **Verified correct (v1.8.1)**: `10.1057/s41287-021-00364-6` ✓ (Crossref + Springer)
- **Title**: "Microeconomic evidence from sub-Saharan Africa" → "Evidence from African firms"

See [`audit/CITATION_AUDIT.md`](audit/CITATION_AUDIT.md) for full audit details.

## Replication

See [`replication/README.md`](replication/README.md) for step-by-step.

Quick reproduce:
```bash
# Prerequisites
brew install pandoc graphviz   # or apt install
pip install matplotlib numpy python-docx

# Build manuscript
cd manuscript
bash build_docx.sh             # one-shot: figures + 6 parts → manuscript_v1_8_blinded.docx
```

Data prerequisites: WBES China 2012 + 2024 raw — see [`replication/data_source.md`](replication/data_source.md).

## Audit reports (4 files)

| File | Purpose |
|---|---|
| [`audit/CITATION_AUDIT.md`](audit/CITATION_AUDIT.md) | All 42 references verified across Tier A/B/C/D — **closed** |
| [`audit/CLAIMS_AUDIT.md`](audit/CLAIMS_AUDIT.md) | All empirical claims verified against data |
| [`audit/VERIFICATION_RESULTS.md`](audit/VERIFICATION_RESULTS.md) | Per-reference verification table with sources |
| [`audit/SUBMISSION_TARGETS.md`](audit/SUBMISSION_TARGETS.md) | APJM + alternative journal analysis (MIR, JWB, JIM, IBR) |

## Cross-link với thesis

P5 evidence được cite trong:

- [`../../thesis/04_references_apa7.md`](../../thesis/04_references_apa7.md) Section M
- [`../../thesis/05_p5_china_design_vi.md`](../../thesis/05_p5_china_design_vi.md) full design + integration
- [`../../thesis/01_chapter_outline_vi.md`](../../thesis/01_chapter_outline_vi.md) Ch.4.5 temporal heterogeneity
- [`../../thesis/16_cd1_part3_cases_conclusion_vi.md`](../../thesis/16_cd1_part3_cases_conclusion_vi.md) §5.4 China tiểu cảnh
