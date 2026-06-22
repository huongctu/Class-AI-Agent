# P4 Vietnam — replication blueprint

End-to-end Stata pipeline that rebuilds the three Vietnam WBES waves (2009, 2015, 2023), runs the M0–M8 model sequence per wave and pooled, and emits every table / figure the manuscript references.

## Layout

```
p4_vietnam/
├── do/                     # 10-step pipeline + master + helper library
│   ├── 00_master.do
│   ├── _lib_build.do
│   ├── 01_build_2009.do
│   ├── 02_build_2015.do
│   ├── 03_build_2023.do
│   ├── 04_append_pooled.do
│   ├── 05_main_models.do
│   ├── 06_lind_mehlum.do
│   ├── 07_selection_checks.do
│   ├── 08_crosswave_tests.do
│   ├── 09_robustness.do
│   └── 10_export_tables_figures.do
├── raw/                    # drop the WBES releases here (see below)
├── work/                   # intermediate per-wave + pooled clean files
└── output/
    ├── tables/             # CSV outputs consumed by the manuscript
    ├── figures/            # PDF + PNG figures
    └── logs/               # Stata logs
```

## Required raw inputs

Place the three WBES releases into `raw/` with these exact filenames:

| Filename             | Source release                                  |
|----------------------|-------------------------------------------------|
| `vietnam_2009.dta`   | World Bank Enterprise Survey — Vietnam 2009     |
| `vietnam_2015.dta`   | World Bank Enterprise Survey — Vietnam 2015     |
| `vietnam_2023.dta`   | World Bank Enterprise Survey — Vietnam 2023     |

Variable presence has been pre-verified against the uploaded `.dta` files:

- 2009 ships `d2 l1 d3c b8 e6 c22b b2b b5 a2 a4a a4b` (no `h1 h8 k33 k38`).
- 2015 ships the 2009 set plus `h1 h8` (still no `k33 k38`).
- 2023 ships everything except `a4b`; sector FE falls back to `a4a`.

So `TCI_full` is constructed only for 2015 and 2023, and `DAI_rich` (continuous and binary) only for 2023, in line with the manuscript.

## Running the pipeline

```stata
cd p4_vietnam
do do/00_master.do
```

`00_master.do` derives every other path from its working directory, installs the user-written commands it depends on (`estout`, `utest`, `parmest`, `ftools`, `reghdfe`) on a fresh machine, and runs the full sequence into `output/logs/00_master.log`.

## What each step writes

| Step | Output                                                     | Used by manuscript section |
|------|-----------------------------------------------------------|----------------------------|
| 01–03| `work/vnm{2009,2015,2023}_clean.dta`                       | §3.1 sample sizes          |
| 04   | `work/vnm_pooled_clean.dta`                                | §3.1 pooled spec           |
| 05   | `tables/coefs_main_models.csv`, `tables/joint_tests_main_models.csv` | §4.2–4.5         |
| 06   | `tables/table_lind_mehlum.csv` (also copied to `table_LM.csv`) | §4.2 (H1)               |
| 07   | `tables/selection_checks.csv`                              | §4.6 (Heckman / CF)        |
| 08   | `tables/table_paternoster.csv`                             | §4.6 (cross-wave z-test)   |
| 09   | `tables/robustness_TCI_full.csv`, `robustness_DAI_rich.csv`, `robustness_sector2digit.csv`, `robustness_microfirm.csv`, `robustness_commonN_2023.csv` | §4.6 panels |
| 10   | `tables/table_1_descriptives.csv`, `table_2_baseline.csv`, `table_3_robustness.csv`, `table_LM.csv`, `figure_2_predictions.csv`, `figs/figure_2_main_results.{pdf,png}` | Tables 1–3, Figure 2 |

## Spec invariants (do not change without manuscript update)

- OLS with `vce(robust)` (HC1) throughout.
- `FSTSc` is **wave-mean-centred** before squaring; in `04_append_pooled.do` the centring is recomputed within wave on the pooled file.
- `TCI_z` and `DAI_z` are **z-standardised within wave** (so the pooled coefficients are interpretable as one-SD effects net of wave).
- WBES `-9` codes are converted to missing **before** any composite is built; listwise deletion runs on `lnLP lnEmp FirmAge ForeignOwned FSTS TCI_thin DAI_thin sector1`.
- Wave fixed effects appear only in pooled specifications (`$pooled_controls`).
- Sector FE uses the first digit of `a4b` where available, falling back to `a4a` for 2023.

## Reconciliation rule

If a coefficient or p-value reported in the manuscript drifts from what the rerun produces, **the manuscript text is what changes** — never the do-file output. The four canonical tables (`table_1_descriptives`, `table_2_baseline`, `table_3_robustness`, `table_LM`) are the source of truth.
