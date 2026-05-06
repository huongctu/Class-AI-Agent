# APJM Submission Package — P5 Manuscript v1.8

**Manuscript:** *The Export Intensity–Performance Relationship in Chinese Private Firms: A Threshold-Stability Perspective*
**Target journal:** *Asia Pacific Journal of Management* (APJM) — primary; see `SUBMISSION_TARGETS.md` for alternatives
**Manuscript version:** v1.8 (2026-05-04, Tier-C reference verification revision; closes CITATION_AUDIT.md and CLAIMS_AUDIT.md)
**Package owner:** corresponding author (see `01_title_page.md`)

---

## What goes into the APJM submission portal

APJM uses Editorial Manager. The portal asks you to upload these items separately. Each row maps a portal slot → file in this folder → status.

| # | Portal slot | File | Status | Notes |
|---|---|---|---|---|
| 1 | **Cover Letter** | `02_cover_letter.md` | Draft ready (fill `[corresponding author info]` placeholders) | Convert to PDF or paste into portal text box |
| 2 | **Title Page (with author info)** | `01_title_page.md` | Template — fill author names, affiliations, ORCID, corresponding author contact | Separate from blinded manuscript |
| 3 | **Blinded Manuscript** | `manuscript_v1_8_blinded.docx` (built from blinded markdown parts via the procedure in `04_blinding_check.md`) | Built and verified (no `Do & Tu` / `huongctu` matches) | 768 KB; upload to "Manuscript" slot |
| 4 | **Tables/Figures** | Embedded inline in blinded manuscript (APJM accepts both inline and separate; we use inline) | Ready (3 tables, 4 figures already embedded in v1.8 docx) |  |
| 5 | **Highlights** | N/A | APJM does not require highlights | — |
| 6 | **Declarations** (COI, funding, ethics, data, AI use) | `03_declarations.md` | Draft ready | Some journals embed in cover letter; APJM accepts as separate document |
| 7 | **Suggested Reviewers** | `05_suggested_reviewers.md` | 6 reviewer names with affiliations + rationale | Portal asks for 4–6 |
| 8 | **Title page checklist (institutional)** | (varies by author institution) | TBD | E.g., Can Tho University internal authorship form, if required |

---

## Pre-submission checklist (do these in order)

### A. Author-info-dependent (cannot finalise without author input)

- [ ] **Fill `01_title_page.md`** — author names, affiliations, ORCID iDs, corresponding author email/phone/postal. Provide in author order matching v1.8 self-citations (Do, T. H., & Tu, P. A.).
- [ ] **Confirm corresponding author** — the person who will receive editorial correspondence and respond to reviewer comments.
- [ ] **Confirm authorship contributions** (CRediT taxonomy; APJM increasingly asks for per-author roles such as Conceptualization, Methodology, Data curation, Formal analysis, Writing — original draft, Writing — review & editing, Supervision). See `03_declarations.md` §3.
- [ ] **ORCID iDs** for all authors. Required by APJM for the corresponding author; recommended for co-authors.
- [ ] **Funding statement** — confirm "received no specific grant" still holds, or provide grant ID + agency.
- [ ] **Ethics statement** — confirm WBES public-data exemption applies (no human subjects approval required because data are de-identified microdata distributed under WBES protocol).

### B. Manuscript-level finalisation

- [x] All Tier-A / Tier-B / Tier-C references verified (see `apjm/VERIFICATION_RESULTS.md`).
- [x] All empirical claims audited (see `apjm/CLAIMS_AUDIT.md`).
- [x] Word count target met: 13,146 words (within APJM 10–15K convention range).
- [x] APA 7th referencing throughout (39 references with DOIs).
- [x] 3 tables, 4 figures embedded in v1.8 docx.
- [x] Manuscript v1.8 final docx built (`manuscript_v1_8_final.docx`, 768 KB).
- [x] **Blinded version built** — `manuscript_v1_8_blinded.docx` produced and verified empty against unblinding regex.
- [ ] **Cover letter signed by corresponding author** (electronic signature acceptable for APJM).
- [ ] **Plagiarism / similarity check** — run iThenticate or Turnitin before upload (APJM editor desk-rejects manuscripts with similarity > 25 %). The replication-pipeline section, table cells, and reference list typically generate ~10–15 % similarity; if your run is higher, audit Methods §3.x for over-reliance on prior phrasings.
- [ ] **Self-citation audit** — confirm Do & Tu 2025 and Do & Tu 2026 are correctly cited and accessible (proceedings link / journal link should resolve).

### C. Submission portal mechanics

- [ ] Create / sign in to APJM Editorial Manager (or whatever portal APJM is currently using; verify on the journal homepage at the time of submission).
- [ ] Select the correct article type (likely "Original Research" or "Empirical Article").
- [ ] Upload files in the order above.
- [ ] Enter keywords matching abstract: `internationalization–performance; export intensity; threshold stability; technological capability; digital adoption; Chinese private firms; World Bank Enterprise Survey`
- [ ] Submit and confirm receipt.

### D. Post-submission

- [ ] Save the submission ID returned by the portal in `apjm/submission/SUBMISSION_LOG.md` (create after first submit).
- [ ] Archive a frozen copy of `manuscript_v1_8_final.docx`, the blinded version, the cover letter, and the title page in a private cloud folder (Google Drive / OneDrive) with a date stamp.
- [ ] If APJM does not respond within ~12 weeks, follow up with editorial office.

---

## Files in this folder

| File | Purpose | Read order |
|---|---|---|
| `00_SUBMISSION_CHECKLIST.md` | This file — start here | 1 |
| `01_title_page.md` | Title page with author info (template) | 2 |
| `02_cover_letter.md` | Cover letter to APJM editor | 3 |
| `03_declarations.md` | COI, funding, data, ethics, AI-use declarations | 4 |
| `04_blinding_check.md` | Procedure + unblinding sites identified in v1.8 | 5 |
| `05_suggested_reviewers.md` | 6 suggested reviewers with rationale | 6 |

## Files in parent `apjm/` (referenced from this package)

- `manuscript_v1_8_final.docx` — primary manuscript (with author-disclosing self-citations)
- `manuscript_v1_8_blinded.docx` — blinded version for review (upload this to APJM "Manuscript" slot)
- `manuscript_v1_8_part{1..6}_*.md` — manuscript source parts (full/attributed)
- `manuscript_v1_8_blinded_part{1..6}_*.md` — manuscript source parts (blinded)
- `build_docx.sh` — one-shot builder
- `figures/figure{1..4}_*.png` — embedded figures
- `CITATION_AUDIT.md` — reference verification audit (closed)
- `VERIFICATION_RESULTS.md` — Tier-C verification per-reference results
- `CLAIMS_AUDIT.md` — empirical claims audit
- `SUBMISSION_TARGETS.md` — 14 alternative target journals if APJM declines

---

## If APJM declines or desk-rejects

The same submission package can be redirected to alternative targets listed in `SUBMISSION_TARGETS.md`. For each alternative:

1. **Re-target cover letter** (`02_cover_letter.md` has APJM-specific framing; the next-target version should re-emphasise the contribution most relevant to that journal's scope).
2. **Re-blind / un-blind** depending on target's review policy (single-blind, double-blind, transparent).
3. **Re-format** to target style guide (APJM uses APA; some alternatives use Chicago, Harvard, or numbered).
4. **Suggested reviewers** — partially overlap with this list; add 1–2 reviewers more central to the alternative target's editorial board.
