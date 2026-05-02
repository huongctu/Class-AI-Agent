# P4 — Submission checklist (IJoEM)

Last refresh: 2026-05-02 (manuscript v5.3).
Target journal: International Journal of Emerging Markets (Emerald).
Corresponding author: Phan Anh Tu (patu@ctu.edu.vn).

## Deliverable files

| # | File | Purpose | Upload role on Editorial Manager |
|---|------|---------|-----------------------------------|
| 1 | `manuscript_v4_5.docx` | Full version with title page, authors, ORCID, back matter | Title page (or "manuscript with author info" if journal asks for one combined file) |
| 2 | `manuscript_blinded.docx` | Anonymous review copy: title, abstract, keywords, body, figures, tables, references; no author names, no ORCID, no Author contributions section | Main document (blinded) |
| 3 | `cover_letter_ijoem.docx` | Editor cover letter | Cover letter |
| 4 | `p4_vietnam/output/figures/figure_1_conceptual_model.{pdf,png}` | Figure 1 source files | Figure 1 |
| 5 | `p4_vietnam/output/figures/figure_2_main_results.{pdf,png}` | Figure 2 source files | Figure 2 |
| 6 | `p4_vietnam/output/tables/*.csv` | Replication outputs | Supplementary file (optional) |
| 7 | `p4_vietnam/` directory | Stata + Python replication package | Supplementary materials (zip if needed) |

## Pre-submission checks

- [x] Title page has both authors with full ORCID and verified e-mail
- [x] Phan Anh Tu flagged as corresponding author
- [x] Abstract is structured (Purpose / Design / Findings / Originality)
- [x] Keywords (six terms) and JEL codes (five codes) present
- [x] In-text citations follow Emerald Harvard (`Author and Author, Year`)
- [x] References list in Emerald Harvard (`(YYYY), "Title", Journal, Vol. X No. Y, pp. Z–Z.`)
- [x] Every reference is cited at least once in the body
- [x] Every in-text citation has a matching reference entry
- [x] No "submission to Journal of World Business" wording remains
- [x] No "this submission" wording (replaced with "this manuscript")
- [x] No JWB editorial-team / reviewer thanks in Acknowledgements
- [x] Sample sizes (989 / 956 / 1,013 / 2,958) consistent across abstract, §3, tables, figures
- [x] Turning points (46.2 / 39.3 / 41.6 / 39.7 %) consistent across §4 prose and figures
- [x] DAI primary spec is c22b only; no e6 sharing with TCI
- [x] Data Availability Statement spells out the WBES Data Access Protocol
- [x] Conflict of interest declared (none)
- [x] Funding declared (none specific)
- [x] Use-of-AI disclosure included

## Pre-upload Word checks

Open `manuscript_blinded.docx` and confirm:

- No author surname appears anywhere
- No e-mail address appears anywhere
- No ORCID ID appears anywhere
- "Author contributions" heading is removed
- Acknowledgements section retains only the World Bank attribution and the no-funding sentence
- Figures render as PNG embedded inline (Figure 1 and Figure 2)
- Table 1 (descriptives) and Table 2 (main empirical pattern) render as Word tables

Open `manuscript_v4_5.docx` (the title-page version) and confirm:

- Title, both author lines, both affiliations and the corresponding-author tag are present
- The 6 Heading-1 back-matter sections appear in this order: Author contributions, Conflict of interest, Funding, Data availability statement, Use of generative AI in the writing process, Acknowledgements

## Submission note (for "Comments to the editor")

> This manuscript is original, has not been published previously, and is not under consideration elsewhere. All authors have approved the submitted version and agree to its submission. The study uses World Bank Enterprise Surveys data under the applicable data-access protocol; accordingly, the raw .dta files are not redistributed, although replication materials and computational documentation can be shared to the extent permitted by the data-access terms.

## Reproducibility

Anyone can rebuild the entire submission from the repository root:

```bash
# 1. Re-estimate everything on the three Vietnam WBES waves
python3 scripts/p4_vietnam_analysis.py

# 2. Render Figure 1 (B&W conceptual model) and Figure 2 (predicted I–P curves)
PYTHONPATH=scripts python3 scripts/p4_render_figures.py

# 3. Build the full manuscript (with title page + back matter)
python3 scripts/build_p4_v4_5.py

# 4. Build the blinded manuscript (no author identity)
BLINDED=1 python3 scripts/build_p4_v4_5.py

# 5. Build the cover letter
python3 scripts/build_cover_letter.py
```

Outputs:

- `manuscript_v4_5.docx` (full)
- `manuscript_blinded.docx` (review copy)
- `cover_letter_ijoem.docx`
- `p4_vietnam/output/tables/*.csv` (Table 1, Table 2, Table 3 robustness, Table LM, Heckman, Paternoster)
- `p4_vietnam/output/figures/figure_{1,2}_*.{pdf,png}`
