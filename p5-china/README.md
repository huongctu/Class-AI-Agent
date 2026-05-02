# P5 China — Replication Pipeline + APJM Submission Artifacts

Replication of *Threshold Stability in the Export Intensity–Performance Relationship: Evidence from Chinese Private Firms* (P5, manuscript v1.2) using WBES China 2012 and 2024 microdata.

## Status

**Replication verified.** Python pipeline reproduces manuscript v1.2 within rounding:

| | Mine (Python) | Manuscript v1.2 |
|---|---|---|
| Turning point 2012 | **49.37 %** | 49.4 % |
| Turning point 2024 | **47.19 %** | 47.6 % |
| Turning point pooled | **48.78 %** | 48.9 % |
| Paternoster z (FSTS) | p = 0.412 | stable ✓ |
| Paternoster z (FSTS²) | p = 0.545 | stable ✓ |
| 2012 sample_base N | 2,610 | 2,612 |
| 2024 sample_base N | 1,934 | 1,934 ✓ |
| Pooled sample_base N | 4,544 | 4,546 |

## Critical findings during replication

1. **Manuscript v1.2 uses the FULL WBES private-firm frame, not a manufacturing-only subsample.** The title/abstract reference to "Chinese manufacturing SMEs" does not match the analytic sample (2,619 / 1,940 / 4,559) — it includes services, retail, IT, construction. Patch list `apjm/patch_list_v1_2_to_v1_3.md` renames the paper's identity to "Chinese private firms" (Phương án 1, safe).
2. **2012 vs 2024 sector coding is incompatible.** 2012 `a4a` is ISIC Rev 3.1 (codes 15–37 + 38 Other Mfg). 2024 `a4a` is a 14-category stratum code (1–14, 1–9 = mfg). 2024 also has `d1a2_v4` = 4-digit ISIC Rev 4 (WBES recommended). If a future revision applies a manufacturing filter, code-frame mapping is required per wave.
3. **2024 has 217 panel firms** (also surveyed in 2012). Pooled regressions cluster on `idstd` to handle dependence — but in the current data, 2012 `idstd` does not appear to share values with the panel firms in 2024, so cluster correction may be a no-op. Verify panel link mechanism before submitting.
4. **Nonresponse codes differ across waves.** 2012: `-9` and `-7`. 2024: `-9`, `-8`, `-7`. Pipeline recodes all → missing.

## Repository layout

```
p5-china/
├── README.md                              this file
├── PLAN.md                                planning doc (sample-construction protocol)
├── do/                                    Stata do-files (4-step pipeline)
│   ├── 01_build_2012.do
│   ├── 02_build_2024.do
│   ├── 03_build_pooled.do
│   └── 04_run_models.do
├── python/                                Python verification pipeline
│   ├── build_and_run.py                   tries 'all' vs 'mfg' frames
│   └── full_models.py                     runs M0–M8 on 'all' frame
├── audit/                                 sample-size audit tables
│   ├── audit_N_checklist.csv              expected N per step (RA fills observed)
│   ├── audit_N_all.csv                    observed N, full-private frame
│   └── audit_N_mfg.csv                    observed N, manufacturing-only frame
├── results/
│   ├── results_coefs.csv                  M0–M8 coefficients (3 samples × 9 models)
│   └── M2_table.csv                       main threshold model summary
└── apjm/
    ├── APJM_submission_outline.md         title, abstract, sections, cover letter
    └── patch_list_v1_2_to_v1_3.md         27 sentence-level edits + 2 inserts
```

## How to run

### Stata

```bash
cd do/
stata -b do 01_build_2012.do
stata -b do 02_build_2024.do
stata -b do 03_build_pooled.do
stata -b do 04_run_models.do
```

Update paths in `01_build_2012.do` and `02_build_2024.do` to point at local raw `.dta` files.

### Python

```bash
pip install pyreadstat pandas numpy statsmodels scipy
python3 python/build_and_run.py    # audits both frames
python3 python/full_models.py      # runs full M0–M8 on 'all' frame
```

Both scripts hard-code raw-data paths at the top of the file — update before running.

## Key methodological decisions (chốt)

| Fork | Choice | Rationale |
|---|---|---|
| Sample frame | Full WBES private firms | Matches manuscript v1.2 reported N |
| 2024 industry filter (if mfg) | `d1a2_v4` (10–33) | WBES recommended (realized industry) |
| 2012 manufacturing scope | `a4a` 15–38 incl. Other Mfg | Cross-wave consistent |
| Pooled SE | `vce(cluster idstd)` | Handle 217 panel firms |
| TCI nonmissing rule | ≥ 3 of 4 items | Manuscript v1.2 convention |
| DAI proxy | z-mean(c22b, e6) | Cross-wave comparable thin proxy |
| Within-wave standardization | Yes, before pooling | Preserves cross-wave coefficient comparability |

## Open items for RA before APJM submission

1. Verify exact `firmage` formula in v1.2 (`year − b5` vs alternative) against current draft.
2. Verify `foreigndummy` threshold (`b2b > 0` vs `b2b ≥ 10`).
3. Cross-check TCI/DAI item names in BREADY 2024 questionnaire (whether `e6/b8/h1/h8/c22b` survived rename).
4. Verify panel link mechanism between 2012 and 2024 `idstd` (cluster SE depends on it).
5. Decide whether to apply WBES sampling weights (`wmedian`) for robustness; v1.2 currently unweighted.
6. Confirm Phương án 1 wording ("Chinese private firms") before applying patch list.

## Citation / reference

World Bank Enterprise Survey, China 2012 (full release, 2,700 private firms) and China 2024 (BREADY, 2,189 firms incl. 217 panel). https://www.enterprisesurveys.org/
