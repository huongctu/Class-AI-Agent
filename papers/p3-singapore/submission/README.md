# P3 Submission Package — Management International Review

This folder contains the complete submission package for:

> **Technological Capability, Digital Adoption, and the Internationalization–Performance Relationship: A Firm-Level Study of Singapore**

| # | File | Format | Purpose |
|---|---|---|---|
| 01 | `manuscript_R3_FIGFIXED.docx` | Word | Blinded manuscript with embedded Figures 1–3 and Tables 1–4 (R3 + 12 patches) |
| 02 | `Title_Page.docx` | Word | Author info, ORCID, declarations, data availability |
| 03 | `Cover_Letter.docx` | Word | Cover letter to the editor |
| — | `../figures/` | PNG | Standalone copies of Figures 1, 2, 3 (300 dpi) |

---

## Authors

- **Do Thuy Huong** (lead author) — College of Economics, Can Tho University, Vietnam
  ORCID: 0000-0002-7711-2487 · huongp1323001@gstudent.ctu.vn
- **Phan Anh Tu** (corresponding author) — School of Economics, Can Tho University, Vietnam
  ORCID: 0000-0003-0667-3137 · patu@ctu.edu.vn

---

## What's inside the manuscript

- **Abstract** — 215 words (within MIR 150–250 limit).
- **7 sections** — Introduction · Theory & Hypotheses · Methods · Results · Discussion · Conclusion · Limitations.
- **4 tables** — Descriptive statistics · Hierarchical OLS (M0–M8) · Marginal effects of DAI · Robustness checks (six specifications).
- **3 figures** — Conceptual model · DAI marginal effect (support-aware) · Predicted I–P curve (with bootstrap CI).
- **36 references** — APA-style reference list, MIR-style in-text citations (no comma between author and year).
- **Data Availability Statement** — references the public WBES Singapore 2023 dataset.
- **8,140 words** total (28 PDF pages with figures and references).

The manuscript is **double-blinded**: no author identifiers anywhere in the body, references, or acknowledgments.

---

## Empirical anchors

All numerical content traces to a single canonical M8 specification reproduced from raw `.dta`:

| Quantity | Value | Source |
|---|---:|---|
| Sample size (M0/M2/M5) | N = 623 | full sample |
| Sample size (M6/M7/M4/M8) | N = 617 | DAI sample (drops 6 firms missing both k33+k38) |
| TCI direct effect (M8) | β = +0.153 (p < .001) | Table 2 |
| FSTS² × DAI moderation (M8) | β = +3.119 (p = .006) | Table 2 / Table 3 |
| Adjusted R² (M8) | 0.196 | Table 2 |
| FSTS turning point (M2) | 82.4% | text + Figure 3 |
| Bootstrap 95% CI for turning point | [52.8%, 252.9%] | Section 7 + Figure 3 |
| Inverted-U shape recovery (5,000 reps) | 96.3% | Section 7 + Figure 3 |
| Intensive-margin joint F (DAI moderation) | F = 6.32, p = .003 | Section 4.5 |
| LOO % runs significant (FSTS² × DAI) | 100% | Section 4.5 |

---

## How to upload to the MIR Editorial Manager portal

**Portal URL:** https://www.editorialmanager.com/mir/

1. Sign in with the corresponding author's account.
2. Click *Submit New Manuscript* → choose article type (Original Research).
3. Upload files in this order:
   - `manuscript_R3_FIGFIXED.docx` → as **Manuscript (anonymised)**
   - `Title_Page.docx` → as **Title Page**
   - `Cover_Letter.docx` → as **Cover Letter**
   - `../figures/figure1_conceptual_model.png` (regenerated, 300 dpi)
   - `../figures/figure2_dai_marginal.png` (300 dpi)
   - `../figures/figure3_predicted_curve.png` (300 dpi)
4. Confirm metadata (authors, ORCID, keywords).
5. Submit.

> Springer/MIR usually accepts both PDF and Word. The `.docx` is the editable source.

---

## R3 revision summary (one paragraph)

This is a Round 3 resubmission. Round 2 reviewer flagged five framing/identification concerns and two factual errors. The R3 revision (a) recasts the framing from a "digital-frontier boundary condition" to an extreme-case, within-context study of Singapore; (b) rebuilds the empirical architecture around an extensive–intensive split, with the exporter-only intensive analysis as the primary inferential test and the full-sample polynomial as a descriptive baseline; (c) corrects all six rows of Table 3 (which had transcription errors against the canonical M8 specification); (d) rewrites H2 and H3 to align with what the models can establish; and (e) re-grounds the Section 7 caveat in thin upper-tail support and small-subsample precision rather than in cross-sample adjusted R². See `../audit/R3_Master_Revision_Memo.md` for the internal summary.

---

## Reproducibility

All numerical content can be regenerated end-to-end from the raw WBES `.dta` file. See [`../replication/README.md`](../replication/README.md) for step-by-step.

Quick reproduce:
```bash
pip install python-docx matplotlib pillow
python3 ../replication/fix_r3_post_revision.py    # 11 text patches
python3 ../figures/source/regenerate_fig1.py       # Figure 1 regen
```

---

## Submission package — checklist before uploading

- [x] Title is identical across manuscript, title page, cover letter.
- [x] No "Digital-Frontier Economy" wording anywhere.
- [x] Manuscript is blinded (no author identifiers, affiliations, ORCIDs).
- [x] Hypotheses (H1, H2, H3) consecutive — no gap (was H1, H3, H4 in R3 reference; renumbered).
- [x] Table 3 matches canonical re-estimation (all six rows).
- [x] Abstract = 215 words (within 150–250).
- [x] In-text citations follow MIR style: `(Author Year)`, no comma.
- [x] Reference list intact, 36 references, hanging-indent style.
- [x] Avenyo (2021) DOI verified `s41287-021-00364-6` — title "Evidence from African firms".
- [x] Data Availability Statement present.
- [x] Three figures embedded with support-aware presentation (rug plots, decile counts, bootstrap CI bands, thin-tail shading).
- [x] Cover Letter contains the two mandatory Springer sentences ("not published elsewhere", "all authors approved").
- [x] Title Page contains corresponding-author info, ORCID, postal address, full Declarations block.
- [x] Authors' Contributions follow CRediT format.
