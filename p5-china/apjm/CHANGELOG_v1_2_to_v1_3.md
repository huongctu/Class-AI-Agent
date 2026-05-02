# Manuscript v1.2 → v1.3 Changelog

**Date:** 2026-05-02
**Branch:** `claude/p5-china-sample-outline-1KXp4`
**Output file:** `apjm/manuscript_v1_3.md`
**Patch source:** `apjm/patch_list_v1_2_to_v1_3.md`

## Summary

Applied 27 sentence-level edits + 2 paragraph insertions to rename sample identity from **"Chinese manufacturing SMEs"** → **"Chinese private firms"**. Rationale: replication established that manuscript v1.2's analytic sample (N = 2,619 / 1,940 / 4,559) corresponds to the full WBES private-firm frame, not a manufacturing-only subsample.

## Sample identity rename

Verified post-edit:
- **0** instances of "Chinese manufacturing SMEs" remain
- **19** instances of "Chinese private firms" added
- **8** instances of "private‑firm" (compound, e.g., "private‑firm exporter cohort")
- **2** intentional retentions of `manufactur` (literature/frame register only):
  - §3.1 data clarification: "...rather than a manufacturing‑only subsample" (transparency note)
  - §6 Limitations Fourth: "...the manufacturing‑services balance" (sample-frame drift literature)

## Edits applied (27)

| Block | ID | Location | Type |
|---|---|---|---|
| A. Title / Frontmatter | A1 | Title line | Sample-identity rename |
| | A2 | Abstract sentence 1 | Sample-identity rename |
| | A3 | Abstract last sentence | Sample-identity rename |
| | A4 | Keywords line | Sample-identity rename |
| B. Introduction | B1 | ¶2 motivation | Soften (manufacturing SMEs → private firms) |
| | B2 | ¶3 study positioning | Sample-identity rename |
| | B3 | ¶5 first contribution | Sample-identity rename |
| C. Theory & H | C1 | §2.1 ¶1 nonlinearity | Soften (smaller private firms in EE) |
| | C2 | §2.1 ¶2 costs | Soften (smaller private firms) |
| | C3 | H1 | Sample-identity rename |
| | C4 | §2.2 ¶2 stability rationale | Sample-identity rename |
| | C5 | §2.3 ¶1 mechanism | "Manufacturing exporters" → "Exporting firms" |
| | C6 | H3 | Sample-identity rename |
| | C7 | H4a | Sample-identity rename |
| | C8 | H4b | Sample-identity rename |
| D. Figure captions | D1 | Figure 1 | Sample-identity rename |
| | D2 | Figure 2 | Sample-identity rename |
| | D3 | Figure 3 | Sample-identity rename |
| | D4 | Figure 4 | Sample-identity rename |
| E. Data | E2 | §4.1 descriptives | "manufacturing exporter cohort" → "private‑firm exporter cohort" |
| F. Results | F1 | §4.3 cross-wave conclusion | Sample-identity rename |
| | F2 | §4.4 capability interp | Sample-identity rename |
| G. Discussion | G1 | §5.1 ¶1 threshold contribution | Sample-identity rename |
| | G2 | §5.1 ¶4 capability discussion | Sample-identity rename |
| | G3 | §5.2 ¶1 managerial opening | Sample-identity rename |
| | G4 | §5.3 ¶1 long-run interpretation | Sample-identity rename |
| H. Limitations | H2 | §6 Fifth limitation | Sample-identity rename (CRITICAL for reviewers) |

## Paragraph insertions (2)

### E1 — Section 3.1 data clarification (after first descriptive paragraph)

> The analytic sample is drawn from the broader private‑firm WBES frame for China rather than a manufacturing‑only subsample; firms in services, retail, IT, and construction are included alongside manufacturing because the manuscript's identification strategy depends on the full WBES private‑firm frame in which the threshold result is estimated. We control for sectoral composition through ISIC stratum dummies (`a4a`).

### I — Section 3.1 replication note (added after E1)

> Replication note. The analytic samples reported throughout this paper (2012, N = 2,619; 2024, N = 1,940; pooled, N = 4,559) are constructed from the full WBES private‑firm frame for each wave, with World Bank nonresponse codes (−9 and −7 in 2012; −9, −8, and −7 in 2024) recoded as missing on focal variables and listwise deletion applied across `lnLP`, `FSTS`, `FSTS²`, `lnEmp`, firm age, and the foreign‑ownership indicator. Composite indices `TCI_full` and `DAI_core` are within‑wave z‑standardised before pooling. We have verified the analytic sample sizes, turning‑point estimates (49.4 % in 2012, 47.6 % in 2024, 48.9 % pooled), and Paternoster cross‑wave equality results in an independent Python replication of the Stata pipeline.

## Side updates (not in patch list)

- **§3.1 ¶1** updated to mention 2024's separate `-8` refusal code: "non‑response codes -9 and -7 as missing (and the additional 2024 refusal code -8)".
- **§3.2 transparency note** updated to reflect 2024's separated refusal code: "the 2024 release additionally separates -8 for refusal from -9 for don't know".
- **§5.3 ¶1** small adjustment: "Chinese SME-oriented industrial policy" → "Chinese private‑firm-oriented industrial policy" (consistency with new identity).
- **§5.2 managerial implications** — changed "SME managers" to "Managers" in two sentences for register consistency with new "private firms" identity.
- **Replication footer** updated to point at this repository's `p5-china/` directory rather than the original `manuscripts/p5-apjm-china/` reference.
- **Date** moved from 2026-04-30 (v1.2) to 2026-05-02 (v1.3).

## Files changed

- **NEW:** `p5-china/apjm/manuscript_v1_3.md` (full edited manuscript, ~53 KB, 269 lines)
- **NEW:** `p5-china/apjm/CHANGELOG_v1_2_to_v1_3.md` (this file)

## Verification check

```bash
# Verify only intentional 'manufactur' mentions remain:
grep -ni 'manufactur' apjm/manuscript_v1_3.md
# Expected: exactly 2 matches
#   1. §3.1 data clarification ("manufacturing‑only subsample")
#   2. §6 limitation 4 ("manufacturing‑services balance")

# Count rename hits:
grep -c 'Chinese private firms' apjm/manuscript_v1_3.md     # = 19
grep -c 'private‑firm' apjm/manuscript_v1_3.md              # = 8
```

## Next steps for author

1. Open `manuscript_v1_3.md` and confirm wording reads well in context.
2. Decide on Word/Overleaf workflow:
   - Option A: paste markdown into Word, restore formatting (headings, italics, references hanging indent).
   - Option B: convert via pandoc: `pandoc apjm/manuscript_v1_3.md -o manuscript_v1_3.docx`.
3. Re-attach figures (Figure 1 conceptual model, Figure 2 turning-point forest plot, Figure 3 predicted curves overlay, Figure 4 level-shift bars) — these are not embedded in the markdown.
4. Apply final author/affiliation page (kept separate from blinded manuscript per APJM rules).
5. Cross-check references against current APJM style requirements.
6. Optional: add full-table CSV outputs from `results/results_coefs.csv` as supplementary materials.
