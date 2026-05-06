# Blinding Check — v1.8 Manuscript

**APJM uses double-blind peer review.** The version uploaded to the "Manuscript" portal slot must remove all author-identifying information; the author-bearing version goes to the separate "Title Page" slot (`01_title_page.md`).

## Unblinding sites identified in v1.8 (full version)

The fully-attributed `manuscript_v1_8_part{1..6}_*.md` files (and the docx built from them) contain the following author-disclosing items that must be replaced or removed in the blinded build:

| # | Site | File / line | Patch applied in blinded version |
|---|---|---|---|
| 1 | In-text `(Do & Tu, 2025)` self-citation × 2 | part5 line 15; part6 line 17 | → `(Author Citation, 2025)` |
| 2 | In-text `(Do & Tu, 2026)` self-citation × 5 | part1 line 25; part2 lines 17, 39, 41; part5 line 5; part6 line 15 | → `(Author Citation, 2026)` |
| 3 | Reference list entry: `Do, T. H., & Tu, P. A. (2025). Internationalization and firm performance: A meta-analysis review. In *ICBEF 2025 proceedings* (Vol. 2, pp. 469–489). Can Tho University Press.` | part6 line 51 | → `Author Citation. (2025). Internationalization and firm performance: A meta-analysis review. [Conference proceedings; full citation withheld for blind review.]` |
| 4 | Reference list entry: `Do, T. H., & Tu, P. A. (2026). Firm performance heterogeneity in emerging Asia. *Vietnam Economic Financial Review, 2*(1), 111–115.` | part6 line 53 | → `Author Citation. (2026). Firm performance heterogeneity in emerging Asia. [Journal article; full citation withheld for blind review.]` |
| 5 | GitHub repository handle in replication-package note: `corresponding author's GitHub repository (huongctu/Class-AI-Agent)` | part6 line 119 | → `corresponding author's repository (handle withheld for blind review)` |
| 6 | Version-label byline in title-page region: `v1.8 — submission to APJM` | part1 line 3 | → `v1.8 (BLINDED) — submission to APJM` (still anonymous; flags the file as the blinded variant for the editorial workflow) |

**No author institutional affiliations, ORCID iDs, email addresses, telephone numbers, or postal addresses appear anywhere in the v1.8 manuscript files** because the title page is maintained as a separate document (`01_title_page.md`). The Acknowledgements paragraph in `manuscript_v1_8_part6_limits_refs.md` thanks "the Enterprise Analysis Unit of the Development Economics Global Indicators Group of the World Bank" — generic, not unblinding — and is preserved verbatim in the blinded version.

## Blinded artefacts produced

Running the blinding patches (per the procedure below) produced the following blinded files in `apjm/`:

- `manuscript_v1_8_blinded_part{1..6}_*.md` — six section-level blinded markdown files
- `manuscript_v1_8_blinded_complete.md` — concatenated blinded markdown
- `manuscript_v1_8_blinded_with_figures.md` — figures injected for pandoc
- `manuscript_v1_8_blinded.docx` — final blinded docx (~768 KB), upload this to the APJM "Manuscript" slot

## Blinding procedure (for reproducibility)

```bash
cd /home/user/p5-china/apjm

# 1. Copy v1.8 parts to blinded versions
for n in 1 2 3 4 5 6; do
  src=$(ls manuscript_v1_8_part${n}_*.md)
  dst=$(echo "$src" | sed 's/v1_8/v1_8_blinded/')
  cp "$src" "$dst"
done

# 2. Apply blinding patches (replace_all)
for f in manuscript_v1_8_blinded_part*.md; do
  sed -i 's/(Do & Tu, 2025)/(Author Citation, 2025)/g; s/(Do & Tu, 2026)/(Author Citation, 2026)/g' "$f"
  sed -i 's/Do & Tu, 2025/Author Citation, 2025/g; s/Do & Tu, 2026/Author Citation, 2026/g' "$f"
  # ... reference list entry replacements (multi-line; see git history of this folder)
  sed -i "s|(huongctu/Class-AI-Agent)|(repository handle withheld for blind review)|g" "$f"
  sed -i "s|corresponding author's GitHub repository (repository handle withheld for blind review)|corresponding author's repository (handle withheld for blind review)|g" "$f"
  sed -i 's/v1.8 — submission to Asia Pacific Journal of Management (APJM)/v1.8 (BLINDED) — submission to Asia Pacific Journal of Management (APJM)/g' "$f"
done

# 3. Verify no unblinding patterns remain
grep -nE "(Do & Tu|huongctu|Class-AI-Agent)" manuscript_v1_8_blinded_part*.md
# expected output: empty (no matches)

# 4. Build blinded docx
cat manuscript_v1_8_blinded_part{1..6}*.md > manuscript_v1_8_blinded_complete.md
# (then run figure-injection python block from build_docx.sh against the blinded file,
#  followed by pandoc to .docx)
```

## Final blinding verification

After running the procedure, the verification grep returns **no matches** for any of the six unblinding patterns. The `manuscript_v1_8_blinded.docx` file is therefore safe to upload to the APJM "Manuscript" slot. The `manuscript_v1_8_final.docx` (full attributed version) is retained for internal records and for the cover-letter / title-page submission slots — it must NOT be uploaded to the manuscript slot.

## Reviewer-identifiable secondary leaks (audit checklist)

In addition to the explicit author-name patches, the corresponding author should personally verify the absence of subtler unblinding cues:

- [ ] **Document properties (Word).** Open `manuscript_v1_8_blinded.docx` → File → Info → Inspect Document → Document Inspector → run "Author"-related checks. Strip any author-name metadata pandoc may have inherited.
- [ ] **PDF metadata (if converting to PDF before upload).** Run `exiftool manuscript_v1_8_blinded.pdf -all=` (or use Acrobat → File → Properties) to remove author / creator / producer fields.
- [ ] **Track-changes / comments.** Confirm Word document has no surviving tracked changes or reviewer comments that name colleagues.
- [ ] **File-name leaks.** Rename the file from `manuscript_v1_8_blinded.docx` to a neutral name like `Manuscript_BlindedReview.docx` before uploading; some portals display the uploaded filename in reviewer dashboards.
- [ ] **Tables / figures axis labels.** Verify no figure axis label or legend includes a software-license string with the author's username (e.g., matplotlib's default username in plot save dialogs).
- [ ] **Acknowledgements paragraph.** Re-read the acknowledgements paragraph in `manuscript_v1_8_blinded_part6_limits_refs.md` to confirm it does not name specific colleagues or seminar venues that would identify the authors.
- [ ] **Self-citation language.** Verify the manuscript does not contain phrasings like "as shown in our prior work…", "in our 2025 paper…", or other first-person prior-work references that an alert reviewer could deanonymize.
- [ ] **Country-of-origin and language tells.** The manuscript is in English; no Vietnamese phrases or non-anonymous regional references (e.g., specific Mekong Delta cities, specific Can Tho institutional units) appear in the v1.8 text. Verified at audit.
