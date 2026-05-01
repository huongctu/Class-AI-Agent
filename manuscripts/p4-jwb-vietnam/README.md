# P4 — Vietnam I–P Analysis (JWB v4.4)

Replication package for the manuscript *"Digital Adoption, Technological Capability, and the Internationalisation–Performance Relationship in Vietnam: Evidence from a Transitional Digital Economy"* — submission to the *Journal of World Business*.

This package contains the analytic code, a dataset of cleaned analysis variables, regenerated regression tables, two figures, and a set of human-readable run logs. The pipeline was implemented and verified in **Python**; a **Stata** do-file mirroring the same specification is included for third-party verification but has not been run by the authors.

---

## 1. Layout

```
manuscripts/p4-jwb-vietnam/
├── README.md                               # this file
├── manuscript_v4_4.md                      # source-of-truth manuscript (Markdown)
├── manuscript_v4_4.docx                    # pandoc export for journal submission
├── highlights_v4_4.md                      # 5 bullets, 3 updated against v4.3
├── cover_letter_v4_4.md                    # cover letter (Option H2 wording)
├── changelog_v4_3_to_v4_4.md               # section-by-section diff log
├── code/
│   ├── inspect_wbes_vn.py                  # WBES variable inspection
│   ├── p4_python_check.py                  # main pipeline (baseline + robustness)
│   ├── p4_h4_and_extras.py                 # H2 + H4 moderation + LM CI extras
│   ├── p4_triple_source.py                 # statsmodels + linearmodels + manual HC1
│   ├── make_figure_1_conceptual.py         # Figure 1 generator
│   ├── make_figure_2_results.py            # Figure 2 generator
│   ├── P4_Vietnam_FullAnalysis.do          # Stata mirror (NOT executed by authors)
│   └── requirements.txt                    # pinned Python deps
├── figures/
│   ├── figure_1_conceptual_model.{pdf,png}
│   └── figure_2_main_results.{pdf,png}
├── tables/
│   ├── table_2_baseline.csv                # per-wave + pooled main coefficients
│   ├── table_3_robustness.csv              # H2 / H4 moderation + joint F
│   └── table_lind_mehlum.csv               # turning points + delta-method 95% CI + LM p
└── output/
    ├── wbes_vn_inspection.md               # variable availability by wave
    ├── pipeline_run.log                    # stdout of p4_python_check.py
    ├── triple_source_verification.log      # numerical agreement evidence
    ├── h4_extras.md                        # H2/H4/LM extras human summary
    ├── p4_python_check.md                  # pipeline-generated report
    ├── p4_python_baseline.csv              # cleaned analytic dataset
    └── p4_python_results.csv               # coefficient table from pipeline (if emitted)
```

---

## 2. Data

The analysis uses three waves of the World Bank Enterprise Surveys (WBES) for Vietnam:

| Wave | File expected at runtime          | Raw N | Analytic N |
|------|-----------------------------------|-------|------------|
| 2009 | `Vietnam2009fulldata.dta`         | 1,053 | 734        |
| 2015 | `Vietnam2015fulldata.dta`         | 996   | 614        |
| 2023 | `VietNam2023fulldata.dta`         | 1,028 | 974        |

The WBES public release is freely downloadable from <https://www.enterprisesurveys.org/en/data> after acceptance of the **WBES Data Access Protocol**. The protocol explicitly prohibits redistribution of the `.dta` files to third parties (including journals), and accordingly **this repository does not redistribute the WBES microdata**. Researchers wishing to reproduce the results must download the three Vietnam waves themselves from the WBES portal under the same Data Access Protocol. The 2015 release is encoded in latin‑1; the pipeline transparently falls back to latin‑1 / cp1252 when a UTF‑8 decode fails.

When citing the data, use the format the World Bank Enterprise Analysis Unit specifies on <https://www.enterprisesurveys.org/en/citing-the-data>:

> Source: World Bank Enterprise Surveys, www.enterprisesurveys.org.

Authors are encouraged to detail the version of the dataset by highlighting its name and date of publication in the citation or in graphs/tables. Per the WB Acknowledgement convention, papers using the data should also include the line: *"We thank the Enterprise Analysis Unit of the Development Economics Global Indicators Group of the World Bank for the data."* The Acknowledgements paragraph in the manuscript adopts this wording verbatim, together with the standard data‑user disclaimer ("the original collector of the data, the authorised distributor of the data, and the relevant funding agency bear no responsibility for use of the data...").

---

## 3. Reproducing the results

### 3.1 Python (verified pipeline)

```bash
# from manuscripts/p4-jwb-vietnam/
pip install -r code/requirements.txt

# 1) Inspect raw .dta variable availability (sanity check, optional)
python code/inspect_wbes_vn.py \
    --files /path/to/Vietnam2009fulldata.dta \
            /path/to/Vietnam2015fulldata.dta \
            /path/to/VietNam2023fulldata.dta \
    --out output/wbes_vn_inspection.md

# 2) Run the main pipeline (baseline OLS, Heckman, control function, robustness)
python code/p4_python_check.py \
    --files /path/to/Vietnam2009fulldata.dta \
            /path/to/Vietnam2015fulldata.dta \
            /path/to/VietNam2023fulldata.dta \
    --outdir output/

# 3) H2 + H4 moderation, Lind–Mehlum CI extras, regenerate tables/*.csv
python code/p4_h4_and_extras.py

# 4) Triple-source numerical verification (must PASS at 1e-9 threshold)
python code/p4_triple_source.py \
    --baseline-csv output/p4_python_baseline.csv \
    --log          output/triple_source_verification.log

# 5) Render figures
python code/make_figure_1_conceptual.py
python code/make_figure_2_results.py
```

Total runtime on a modern laptop: under three minutes.

### 3.2 Stata (independent verification — unrun by authors)

```stata
* from manuscripts/p4-jwb-vietnam/
do code/P4_Vietnam_FullAnalysis.do
```

The do-file expects the three Vietnam `.dta` files in a sibling `wbes_dta/` directory. Adjust the `local datadir` line at the top of the do-file as needed. The `utest` user-contributed package is required for the Lind & Mehlum (2010) U-test; install with `ssc install utest, replace`.

---

## 4. Numerical-verification protocol

The baseline pooled outcome equation (n = 2,322; k = 16) is estimated by three independent estimators on the same X / y design matrix:

| Implementation                | Library         | Cov option                          |
|-------------------------------|-----------------|-------------------------------------|
| `statsmodels.OLS`             | statsmodels     | `cov_type='HC1'`                    |
| `linearmodels.iv.IV2SLS`      | linearmodels    | `cov_type='robust', debiased=True`  |
| Pure NumPy closed-form        | numpy           | manual HC1 (n / (n − k) correction) |

Pairwise pass thresholds (max absolute difference):

| Pair                          | Coefficient | Standard error |
|-------------------------------|-------------|----------------|
| statsmodels vs linearmodels   | 3.77 × 10⁻¹³ | 1.54 × 10⁻¹⁴   |
| statsmodels vs numpy          | 4.06 × 10⁻¹³ | 1.80 × 10⁻¹⁴   |
| linearmodels vs numpy         | 1.22 × 10⁻¹³ | 7.44 × 10⁻¹⁵   |

PASS at `1 × 10⁻⁹`; full log in `output/triple_source_verification.log`.

---

## 5. Mapping manuscript claims to artefacts

| Manuscript element                    | Code path                               | Output artefact                       |
|---------------------------------------|-----------------------------------------|---------------------------------------|
| §3.4 verification fingerprint         | `code/p4_triple_source.py`              | `output/triple_source_verification.log` |
| §4.1 descriptive Ns                   | `code/p4_python_check.py::apply_listwise` | `output/pipeline_run.log`             |
| §4.2 inverted-U + LM p + TPs          | `code/p4_h4_and_extras.py::lind_mehlum_with_ci` | `tables/table_lind_mehlum.csv`        |
| §4.3 TCI direct + H2 moderation       | `code/p4_h4_and_extras.py`              | `tables/table_2_baseline.csv` + `tables/table_3_robustness.csv` |
| §4.4 DAI direct                       | same                                    | `tables/table_2_baseline.csv` (rows DAI_z) |
| §4.5 H4 moderation (incl. 2023 sig.)  | `code/p4_h4_and_extras.py`              | `tables/table_3_robustness.csv` (rows FSTS×DAI, FSTS²×DAI, H4_joint_F) |
| §4.6 DAI_rich attenuation             | `code/p4_python_check.py::robustness_dai_rich` | `output/p4_python_check.md` (Block 7) |
| Figure 1                              | `code/make_figure_1_conceptual.py`      | `figures/figure_1_conceptual_model.{pdf,png}` |
| Figure 2                              | `code/make_figure_2_results.py`         | `figures/figure_2_main_results.{pdf,png}`     |

Every numerical claim in the manuscript text traces to one row in `tables/` or one block in `output/`.

---

## 6. License and citation

Code: MIT License. Data: re-use under WBES Terms of Use; do not redistribute the `.dta` files. If you use this replication package, please cite the manuscript as:

> [Authors] (2026). Digital adoption, technological capability, and the internationalisation–performance relationship in Vietnam: Evidence from a transitional digital economy. *Journal of World Business*, *forthcoming*.

---

## 7. Contact

Open an issue on the host repository for replication questions.
