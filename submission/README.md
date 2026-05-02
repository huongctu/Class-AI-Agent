# P4 Vietnam — IJoEM submission package

This folder contains everything needed to submit the manuscript to the
**International Journal of Emerging Markets** (Emerald Publishing). All files
are reproducible from the scripts in the parent repository.

- **Target journal:** International Journal of Emerging Markets
- **Manuscript title:** *Revisiting the Internationalisation–Performance
  Relationship in an Emerging Market: The Roles of Technological Capability
  and Digital Adoption*
- **Corresponding author:** Phan Anh Tu (patu@ctu.edu.vn)
- **Co-author:** Do Thuy Huong (huongp1323001@gstudent.ctu.edu.vn)
- **Last refresh:** 2026-05-02 (v5.7 — reviewer-driven revision)

## What to upload to Editorial Manager

| File in this folder | Upload role on the manuscript-submission system |
|---|---|
| `manuscript_full_with_authors.docx` | *Title page* (or "Manuscript with author info") |
| `manuscript_blinded.docx` | *Main document* (anonymous review copy) |
| `cover_letter_ijoem.docx` | *Cover letter* |
| `response_letter_to_reviewer.docx` | *Response to reviewer* (point-by-point) |
| `figures/figure_1_conceptual_model.{pdf,png}` | *Figure 1* |
| `figures/figure_2a.{pdf,png}` … `figure_2d.{pdf,png}` | *Figures 2a–2d* |
| `figures/figure_3_moderator_marginals.{pdf,png}` | *Figure 3* (predicted curves at low/high DAI/TCI) |
| `tables/*.csv` | *Supplementary materials* (optional) |
| `SUBMISSION_CHECKLIST.md` | Internal checklist (do not upload) |

## File map

```
submission/
├── README.md                              ← this file
├── manuscript_full_with_authors.docx      ← title-page version (with authors)
├── manuscript_blinded.docx                ← anonymous review copy
├── cover_letter_ijoem.docx                ← editor cover letter
├── response_letter_to_reviewer.docx       ← point-by-point reviewer response
├── SUBMISSION_CHECKLIST.md                ← pre-upload checklist
├── figures/
│   ├── figure_1_conceptual_model.{pdf,png}
│   ├── figure_2a.{pdf,png}   ← 2009
│   ├── figure_2b.{pdf,png}   ← 2015
│   ├── figure_2c.{pdf,png}   ← 2023
│   ├── figure_2d.{pdf,png}   ← pooled
│   ├── figure_2_main_results.{pdf,png}   ← legacy combined
│   └── figure_3_moderator_marginals.{pdf,png}   ← v5.7 moderator marginals
└── tables/
    ├── table_1_descriptives.csv
    ├── coefs_main_models.csv
    ├── joint_tests_main_models.csv
    ├── table_lind_mehlum.csv
    ├── table_3_robustness.csv
    ├── table_density_around_tp.csv         ← v5.7 density around TP
    ├── selection_checks.csv
    └── table_paternoster.csv
```

## Quick sanity check

Before submitting, open `manuscript_blinded.docx` and confirm there is
**no** author name, e-mail, ORCID or "Author contributions" heading anywhere
in the document. The blinded file should contain only: title, abstract
(structured), keywords, JEL codes, body (Sections 1–7), Conflict of
interest, Funding, Data availability statement, AI-use disclosure,
Acknowledgements (World Bank attribution only), Figures, Tables and
References. The full version (`manuscript_full_with_authors.docx`) should
have everything plus the author block on the title page and an *Author
contributions* section.

## Reproducibility

Every file in this folder can be regenerated from the repository root:

```bash
# 1. Re-estimate everything on the three Vietnam WBES waves
python3 scripts/p4_vietnam_analysis.py

# 2. Render Figure 1 (B&W conceptual model) and Figure 2
PYTHONPATH=scripts python3 scripts/p4_render_figures.py

# 3. Build the full manuscript (title-page version)
python3 scripts/build_p4_v4_5.py

# 4. Build the blinded manuscript
BLINDED=1 python3 scripts/build_p4_v4_5.py

# 5. Build the cover letter
python3 scripts/build_cover_letter.py

# 6. Refresh this submission folder
mkdir -p submission/figures submission/tables
cp manuscript_v4_5.docx submission/manuscript_full_with_authors.docx
cp manuscript_blinded.docx cover_letter_ijoem.docx submission/
cp SUBMISSION_CHECKLIST.md submission/
cp p4_vietnam/output/figures/figure_*.{pdf,png} submission/figures/
cp p4_vietnam/output/tables/*.csv submission/tables/
```

## Headline numbers

- Sample sizes: 2009 N = 989, 2015 N = 956, 2023 N = 1,013, pooled N = 2,958
- Lind–Mehlum p-values: 2009 .006, 2015 .009, 2023 .013, pooled < .001
- Turning points (raw FSTS): 46.2 % / 39.3 % / 41.6 % / 39.7 %
- TCI_z direct (M7): 0.215 *** / 0.128 * / 0.123 ** / 0.179 ***
- DAI_z direct (M7): 0.175 *** / −0.044 n.s. / 0.095 * / 0.078 **
- 2023 FSTS_c × DAI_z (M8): −0.912 (p = .043)
- Paternoster: DAI 2009 vs 2015 z = 3.353 (p < .001); DAI 2015 vs 2023 z = −2.051 (p = .040)
