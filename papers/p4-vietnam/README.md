# P4 Vietnam — IJoEM v5.9

> Status: **v5.9 (was v5.8 round 2) + 27 reviewer-driven edits → ready round 3 submission**
> Last update: 2026-05-06
> Source branch (archive): [`claude/update-p4-draft-W6UKL`](https://github.com/huongctu/Class-AI-Agent/tree/claude/update-p4-draft-W6UKL)

## Manuscript info

| Item | Value |
|---|---|
| **Title** | Revisiting the Internationalisation–Performance Relationship in an Emerging Market: The Roles of Technological Capability and Digital Adoption — Three-Wave Evidence from Vietnam |
| **Target journal** | **International Journal of Emerging Markets** (IJoEM), Emerald |
| **Tier** | ABS 2, SSCI Q2 |
| **Authors** | Phan Anh Tú (corresponding), Đỗ Thùy Hương |
| **Data** | WBES Vietnam 2009 + 2015 + 2023 (3 waves) |
| **Sample** | N = 989 (2009), 956 (2015), 1,013 (2023); pooled = 2,958 |
| **Method** | OLS HC1; wave-specific + pooled; PSM (Panel J); IV/2SLS (Panel K); Oster bounds; Heckman (Panel E); Paternoster cross-wave z-tests; 11 robustness panels A–K |
| **Word count** | ~6,800 words main text |

## File map

```
p4-vietnam/
├── README.md                                     # this file
├── manuscript/
│   ├── manuscript_v5_9_blinded.docx              # FINAL: v5.8 + 7 + 20 edits (USE THIS)
│   ├── manuscript_v5_9_full_with_authors.docx    # title-page version
│   ├── manuscript_v5_8_blinded.docx              # legacy reference (before v5.9)
│   └── manuscript_v5_8_full_with_authors.docx    # legacy reference
├── submission/
│   ├── README.md                                 # IJoEM upload mapping
│   ├── SUBMISSION_CHECKLIST.md
│   ├── cover_letter_ijoem.docx
│   ├── response_letter_to_reviewer.docx          # round 1
│   └── response_letter_round2.docx               # round 2
├── figures/
│   ├── figure_1_conceptual_model.png + .pdf
│   ├── figure_2a.png + .pdf                      # 2009 wave
│   ├── figure_2b.png + .pdf                      # 2015 wave
│   ├── figure_2c.png + .pdf                      # 2023 wave
│   ├── figure_2d.png + .pdf                      # pooled
│   ├── figure_2_main_results.png + .pdf          # legacy combined
│   ├── figure_3_moderator_marginals.png + .pdf
│   └── source/                                   # XLSX with data + chart + image sheets
│       ├── figure_1_conceptual_model.xlsx
│       ├── figure_2a.xlsx                        # 2009
│       ├── figure_2b.xlsx                        # 2015
│       ├── figure_2c.xlsx                        # 2023
│       ├── figure_2d.xlsx                        # pooled
│       └── figure_3_moderator_marginals.xlsx
├── tables/                                       # 10 CSV files
│   ├── table_1_descriptives.csv
│   ├── coefs_main_models.csv                     # M0–M8 long-format
│   ├── joint_tests_main_models.csv
│   ├── table_lind_mehlum.csv                     # Table 4 source (turning points)
│   ├── table_3_robustness.csv                    # 6 panels A–D + G
│   ├── table_density_around_tp.csv               # density around TP
│   ├── table_oster_bounds.csv                    # Oster delta-stability
│   ├── table_paternoster.csv                     # cross-wave z-tests
│   ├── table_psm_balance.csv                     # PSM balance diagnostics
│   └── selection_checks.csv                      # Heckman / control function
├── replication/
│   ├── README.md
│   ├── apply_v59_edits.py                        # 20 reviewer-driven edits
│   ├── fix_p4_v58.py                             # 7 prior fixes (legacy)
│   └── data_source.md                            # WBES Vietnam mapping
└── audit/
    └── v5_9_changelog.md                         # 27 total edits across v5.8 → v5.9
```

## Hypothesis structure (v5.9)

- **H1** (dual-margin): I–P relationship is non-monotonic in full sample, best understood through participation-and-intensity structure. **H1a** (participation): non-exporter → exporter is positively associated with productivity. **H1b** (intensity): within exporters, additional FSTS yields weaker, diminishing, or non-significant marginal returns.
- **H2** (TCI direct): Foreign-technology / standards capability is positively associated with firm performance — **supported** in all 3 waves (β = 0.215 / 0.128 / 0.123) and pooled (β = 0.179, p < .001)
- **H3** (DAI direct, on average): DAI is positively associated with productivity — **supported on average** (pooled β = 0.078, p = .004), null in 2015
- **H4** (exploratory wave-specific moderation): DAI moderation is wave-specific, expected strongest in 2023 — **limited exploratory support** (FSTS_c × DAI_z = −0.912, p = .043 in 2023; M8 joint p = .062 marginal)

## Key findings

1. **Robustly nonlinear I–P** in full sample with turning points clustered 39–46% FSTS
2. **TCI is identification-robust** under PSM and 2SLS; β attenuates but stays large under IV
3. **DAI is wave-sensitive**: strong 2009, null 2015, recovery 2023 — Paternoster z-tests confirm cross-wave shifts are statistically distinguishable
4. **2015 dip**: interpreted as wave-specific compression of foundational digital adoption channel under transitional infrastructure conditions (institutionally plausible, not formally identified)
5. **Full-sample inverted-U weakens substantially** in exporter-only models — combined participation+intensity structure rather than within-exporter curvature

## 27 patches applied (v5.8 → v5.9)

### Phase 1: 7 metadata + structural fixes
See [`replication/fix_p4_v58.py`](replication/fix_p4_v58.py).

1. Header metadata Tables: 2 → 4, Figures: 2 → 3
2. §4.4 "Table 1" duplicate label → "Table 2"
3. §4.5 "Table LM" → "Table 4"
4. Supplementary CSV ref "Table LM source" → "Table 4 source"
5. §2.1 added (Cuervo-Cazurra, 2012) cite
6. §2.4 added (Helfat & Peteraf, 2003) cite
7. Title append "— Three-Wave Evidence from Vietnam"

### Phase 2: 20 reviewer-driven clean-copy edits
See [`replication/apply_v59_edits.py`](replication/apply_v59_edits.py).

- **Abstract** (4 blocks): tighter framing; drop technical overload; add dual-margin reading
- **§2.1 H1**: rewritten with participation-and-intensity framing
- **§2.4 H4**: tightened to wave-specific exploratory framing
- **§4.3 hypothesis tests**: H1 "qualified support" (not "strongly supported"); H4 "limited exploratory support"
- **§5.1**: "foundational digital adoption" replaces "digital capability" for DAI_z referent (2 paragraphs)
- **§5.2**: PSM/2SLS evidence sharpens TCI vs DAI distinction (3 paragraphs)
- **§5.3**: 2015 dip reframed as institutional plausibility, not formally identified explanation (3 paragraphs)
- **§6 Limitations**: limit2 Tier-1 proxy framing; limit4 grammar fix + cross-wave evenness reframing
- **§7 Conclusion**: dual-margin + TCI robust / DAI wave-sensitive (2 paragraphs)

## Replication

See [`replication/README.md`](replication/README.md) for step-by-step.

Quick reproduce:
```bash
pip install python-docx
python3 replication/fix_p4_v58.py        # apply 7 prior fixes (creates _FIXED.docx)
python3 replication/apply_v59_edits.py   # apply 20 reviewer edits (creates _v5_9.docx)
```

Data prerequisites: WBES Vietnam 2009 + 2015 + 2023 raw — see [`replication/data_source.md`](replication/data_source.md).

## Cross-link với thesis

P4 evidence được cite trong:

- [`../../thesis/04_references_apa7.md`](../../thesis/04_references_apa7.md) Section M
- [`../../thesis/01_chapter_outline_vi.md`](../../thesis/01_chapter_outline_vi.md) Ch.4.2 (transitional economy benchmark)
- [`../../thesis/16_cd1_part3_cases_conclusion_vi.md`](../../thesis/16_cd1_part3_cases_conclusion_vi.md) §5.3 Việt Nam tiểu cảnh
- [`../../manuscripts/p3_vietnam_en_clean.md`](../../manuscripts/p3_vietnam_en_clean.md) markdown summary internal
