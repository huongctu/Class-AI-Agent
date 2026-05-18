# P3 — Singapore Manuscript

**Title:** Technological Capability, Digital Adoption, and the Internationalization–Performance Relationship: A Firm-Level Study of Singapore.

**Status:** Round 3 ready for submission to *Management International Review*.
**Branch:** `claude/p3-r3-revision` · GitHub PR #6.

---

## Where the submission package lives

➡️ **`submission/`** — the complete, ready-to-upload package.

| File | Purpose |
|---|---|
| [`submission/01_Manuscript.pdf`](submission/01_Manuscript.pdf) | Blinded manuscript with embedded Figures 1–3 and Tables 1–4 (28 pages) |
| [`submission/02_Title_Page.pdf`](submission/02_Title_Page.pdf) | Author info, ORCID, declarations |
| [`submission/03_Cover_Letter.pdf`](submission/03_Cover_Letter.pdf) | Cover letter to the editor |
| [`submission/04_Master_Revision_Memo.md`](submission/04_Master_Revision_Memo.md) | One-page internal R3 summary |
| [`submission/figures/`](submission/figures) | Standalone Figure 1, 2, 3 PNGs (300 dpi) |
| [`submission/README.md`](submission/README.md) | Portal-upload instructions and checklist |

Editable Word sources (`.docx`) are kept alongside each PDF in case the portal requests them.

---

## Other files in this folder

| File | Purpose |
|---|---|
| `Manuscript_Blinded_MIR_2_original.docx` | Round-2 blinded manuscript (pre-R3, kept for diff/recovery) |
| `Manuscript_Blinded_MIR_2_revised.docx` | The current working manuscript (same content as `submission/01_Manuscript.docx`) |
| `Manuscript_Blinded_MIR_2_revised.before-figs.docx` | Pre-figure-replacement backup |
| `Cover_Letter.docx` | Working cover letter (same as `submission/03_Cover_Letter.docx`) |
| `Title_Page.docx` | Working title page (same as `submission/02_Title_Page.docx`) |
| `R3_Master_Revision_Memo.md` | One-page R3 strategy summary for co-author |
| `P3_Revision_Package.md` | Original revision package (R2 → R3 transition wording) |

---

## Authors

- **Do Thuy Huong** (lead author) · ORCID 0000-0002-7711-2487 · College of Economics, Can Tho University.
- **Phan Anh Tu** (corresponding author) · ORCID 0000-0003-0667-3137 · School of Economics, Can Tho University.

---

## R3 revision in one sentence

R3 reframes the manuscript from a "digital-frontier boundary condition" claim to an **extreme-case, within-context study of Singapore**, rebuilds the empirical architecture around an **extensive–intensive split** with the exporter-only intensive analysis as the primary inferential test, corrects a transcription error that affected all six rows of Table 3, and rewrites H2 / H3 / Section 7 to align with what the data can support — while embedding three new support-aware figures (rug plots, decile counts, bootstrap CI for the turning point) so readers can see exactly where the evidence is dense and where it relies on sparse upper-tail data.

---

## Reproduce all numbers + figures

From the repository root:

```bash
# Single source of truth
python3 tools/r3/00_canonical_m8.py            # Reproduces Table 2 M8 exactly

# Robustness pipeline
python3 tools/r3/02_audit_table3.py            # Re-estimates all 6 Table 3 rows
python3 tools/r3/10_extensive_margin.py        # Stage 1 logit
python3 tools/r3/11_intensive_margin.py        # Stage 2 OLS on N=84 exporters
python3 tools/r3/20_influence_diag.py          # Cook's D, DFBETA
python3 tools/r3/21_loo_re_estimation.py       # Leave-one-out
python3 tools/r3/22_trimmed_tail.py            # Trimmed-tail re-estimation
python3 tools/r3/23_bootstrap_tp.py            # Bootstrap CI for turning point
python3 tools/r3/30_indicator_sensitivity.py   # Drop-one-item, item-swap

# Figures + manuscript embedding
python3 tools/r3/70_make_figures_for_manuscript.py
python3 tools/r3/71_embed_figures_into_manuscript.py

# Final consistency audit
python3 tools/r3/50_final_consistency_audit.py    # 51/51 pass, 0 issues
```

Outputs go to `outputs/r3/audit/`, `outputs/r3/tables/`, `outputs/r3/figures/`.
The audit memo is at `outputs/r3/audit/D1_root_cause.md`.
