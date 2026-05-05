# P5 China — Manuscript v1.8 (Blinded) + Replication Pipeline

Replication of *The Export Intensity–Performance Relationship in Chinese Private Firms: A Threshold-Stability Perspective* (P5, manuscript v1.8) using WBES China 2012 and 2024 microdata.

The repository contains everything needed to (a) rebuild the blinded manuscript `apjm/manuscript_v1_8_blinded.docx`, (b) reproduce all empirical results behind the manuscript's tables and figures, and (c) prepare the APJM submission package.

## Headline empirical findings (verified)

| | 2012 | 2024 | Pooled |
|---|---|---|---|
| Sample size (sample_base) | 2,610 | 1,934 | 4,544 |
| Turning point of inverted-U | **49.37 %** | **47.19 %** | **48.78 %** |
| 95 % delta-method CI | [43.17, 55.57] | [34.46, 59.92] | [42.65, 54.91] |
| Lind–Mehlum U-test p | < .001 | .037 | < .001 |

**Cross-wave threshold stability (Paternoster z-test on M2):**

| Coefficient | b (2012) | b (2024) | z | p |
|---|---|---|---|---|
| FSTS | +2.065 | +1.498 | +0.821 | **0.412** (NOT rejected) |
| FSTS² | −2.092 | −1.587 | −0.605 | **0.545** (NOT rejected) |

**Pooled three-way moderation (joint F-tests):**

| Hypothesis | Test | F | p | Verdict |
|---|---|---|---|---|
| H2 cross-wave shift | F1: (FSTS×wave_2024, FSTS²×wave_2024) = 0 | 2.24 | .107 | NOT rejected |
| H4 capability curvature moderation | F2: (FSTS×Tech, FSTS²×Tech) = 0 | 3.26 | .039 | marginal |
| Capability-conditioned dynamic moderation | F3: 3-way = 0 | 0.27 | .760 | NOT rejected |

Three null moderation channels (H2, H3, H4 curvature) converge on the substantive interpretation that the Chinese internationalization–performance trade-off is **durably structural** rather than wave-specific or capability-conditioned.

## Repository layout

```
p5-china/
├── README.md                                this file
├── do/                                      Stata 4-step data builders
│   ├── 01_build_2012.do
│   ├── 02_build_2024.do
│   ├── 03_build_pooled.do
│   └── 04_run_models.do
├── python/                                  Python verification + replication
│   ├── audit_v1_6_claims.py                 audits empirical claims in v1.7+
│   ├── build_and_run.py                     builds 'all' / 'mfg' analytic frames
│   ├── full_models.py                       runs M0–M8 on 'all' frame
│   └── three_way_moderation.py              three-way moderation spec (Table 3)
├── audit/                                   sample-size audit tables
│   ├── audit_N_checklist.csv
│   ├── audit_N_all.csv
│   └── audit_N_mfg.csv
├── results/                                 verified empirical outputs
│   ├── M2_table.csv                         Table 2 (main threshold model)
│   ├── results_coefs.csv                    M0–M8 coefficients × 3 samples
│   ├── three_way_moderation.csv             Table 3 (three-way moderation)
│   ├── moderator_test_summary.csv           moderator interaction tests
│   ├── moderator_test_VERDICT.md            level-shifter vs moderator analysis
│   └── summary.md                           empirical summary
└── apjm/
    ├── manuscript_v1_8_blinded_part{1..6}_*.md   blinded manuscript source (6 parts)
    ├── build_docx.sh                              one-shot docx builder
    ├── figures/                                   figure source files
    │   ├── figure1_conceptual_model_v1_4.dot      Graphviz source (Figure 1)
    │   ├── figure1_conceptual_model_v1_4.mmd      Mermaid source (Figure 1, alt)
    │   ├── render_figures.py                      matplotlib script (Figures 2–4)
    │   ├── README.md                              figures documentation
    │   └── RENDER_FIGURES_README.md               render script usage
    ├── CITATION_AUDIT.md                          reference verification audit
    ├── VERIFICATION_RESULTS.md                    Tier-C reference verification
    ├── CLAIMS_AUDIT.md                            empirical claims audit
    ├── SUBMISSION_TARGETS.md                      14 alternative target journals
    └── submission/                                APJM submission package
        ├── 00_SUBMISSION_CHECKLIST.md
        ├── 01_title_page.md                       (fill author info)
        ├── 02_cover_letter.md
        ├── 03_declarations.md
        ├── 04_blinding_check.md
        └── 05_suggested_reviewers.md
```

## How to build the blinded manuscript

```bash
cd p5-china/apjm
bash build_docx.sh
# → manuscript_v1_8_blinded.docx (~770 KB) with 4 figures embedded
```

Prerequisites: pandoc, graphviz, Python 3 with matplotlib + numpy.

## How to run the empirical pipeline

### Stata (4-step pipeline)

```bash
cd p5-china/do
stata -b do 01_build_2012.do
stata -b do 02_build_2024.do
stata -b do 03_build_pooled.do
stata -b do 04_run_models.do
```

Update paths to local raw `.dta` files at the top of `01_build_2012.do` and `02_build_2024.do`.

### Python (verification)

```bash
pip install pyreadstat pandas numpy statsmodels scipy matplotlib
python3 p5-china/python/build_and_run.py            # build analytic frames
python3 p5-china/python/full_models.py              # M0–M8 on full-private frame
python3 p5-china/python/three_way_moderation.py     # Table 3 specification
python3 p5-china/python/audit_v1_6_claims.py        # audit specific claims
```

Both Python and Stata pipelines reproduce the manuscript's headline numbers.

## Data

WBES microdata are publicly available from https://www.enterprisesurveys.org/en/data subject to registration with the World Bank Enterprise Analysis Unit and acceptance of the WBES Data Access Protocol. The protocol prohibits redistribution; we therefore reference the public download endpoint rather than redistributing the source `.dta` files.

- China 2012 — full release, 2,700 private firms (analytic sample 2,619 after listwise deletion).
- China 2024 — 2,189 firms including 217 panel observations re-interviewed from 2012 (analytic sample 1,940).

## Key methodological decisions

| Fork | Choice | Rationale |
|---|---|---|
| Sample frame | Full WBES private firms | Matches sample sizes 2,619 / 1,940 / 4,559 |
| 2024 industry filter (if mfg robust) | `d1a2_v4` 10–33 | WBES recommended realized-industry code |
| 2012 manufacturing scope (if mfg robust) | `a4a` 15–38 incl. Other Mfg | Cross-wave consistent |
| Pooled SE | `vce(cluster idstd)` | Address 217 panel-firm dependence |
| TCI nonmissing rule | ≥ 3 of 4 items | Convention from prior China replications |
| DAI proxy | c22b own-website (Tier 1 digital) | Cross-wave comparable; e6 reserved for TCI |
| Within-wave standardization | Yes, before pooling | Preserves cross-wave coefficient comparability |
| Robust SE | HC1 (single wave); cluster on `idstd` (pooled) | Standard for survey microdata |

## Audits (closed)

- `apjm/CITATION_AUDIT.md` — reference verification (39 refs, 4 tiers).
- `apjm/VERIFICATION_RESULTS.md` — Tier-C verification: 10 of 11 verified correct; 1 patched (Demir & Javorcik 2018: vol 117/pp 11–22 → vol 111/pp 177–189).
- `apjm/CLAIMS_AUDIT.md` — empirical claims audited against `python/audit_v1_6_claims.py` outputs.

## Submission package (APJM)

See `apjm/submission/00_SUBMISSION_CHECKLIST.md` for the master checklist mapping APJM portal slots to local files. Author placeholders in `01_title_page.md` and `02_cover_letter.md` must be filled before submission.

## Citation / data attribution

World Bank Enterprise Survey, China 2012 and China 2024. World Bank Group. https://www.enterprisesurveys.org/
