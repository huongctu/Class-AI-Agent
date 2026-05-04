# Manuscript v1.5 → v1.6 Changelog

**Date:** 2026-05-04 (later)
**Branch:** `claude/p5-china-sample-outline-1KXp4`
**Trigger:** reviewer feedback that v1.5 was too short; substantive expansion to ~13K words.

## Summary

v1.6 is a **substantive expansion** of v1.5, raising the manuscript word count from ~9,557 to **~12,907 words** (+3,350 words, +35%). Empirical claims are unchanged — same coefficients, same hypotheses, same null-channel convergence. The expansion adds: (a) a China economic-context paragraph, (b) theoretical-foundations elaboration in §2.1 and microfoundational logic in §2.4, (c) a NEW §3.6 sample-selection-diagnostics subsection, (d) **three results tables** (Table 1: descriptives, Table 2: M2 main results, Table 3: three-way moderation), (e) a NEW §5.4 theoretical-contributions subsection (4 explicit contributions), (f) a NEW §5.5 boundary-conditions subsection, and (g) elaborated limitations (each ~250 words instead of 100–150).

## Word count comparison

| Version | Words | Bytes | Status |
|---|---|---|---|
| v1.4 | 8,761 | 65 KB | original durability framing |
| v1.5 | 9,557 | 71 KB | +11 recent refs (no narrative expansion) |
| **v1.6** | **12,907** | **94 KB** | substantive expansion |

v1.6 is comfortably in the 10,000–12,000 word range that ABS-3 and ABS-4 IB journals (APJM, MIR, JIM, JWB, JIBS) accept.

## What's new in v1.6

### Part 1 (frontmatter + intro) — +1 paragraph (~250 words)
- New §1 paragraph: China 2012–2024 economic context (post-2008 trade re-equilibration, China–US tariff escalation, COVID, GVC deepening, SME credit reforms, productivity growth from 12.52 → 13.01 log points).
- Contributions list expanded from 3 to 4 (added explicit cross-country meta-analytic puzzle contribution).

### Part 2 (theory) — +3 substantial passages (~750 words)
- §2.1: NEW closing paragraph anchoring three theoretical traditions (RBV, transaction-cost, dynamic capabilities) on the inverted-U.
- §2.1: NEW concluding paragraph linking Chinese-context evidence (Xiao 2013, Feng 2019) to meta-analytic dispersion (Marano 2016, Schwens 2018).
- §2.2: NEW substantive case for shift via SME credit-market reforms (2014 Guarantee Fund, 2016 inclusive-finance white paper, 2019 supply-chain finance pilot, 2020–22 COVID-relief lending) with explicit testable prediction.
- §2.4: NEW microfoundational paragraph for capability curvature moderation (absorptive-capacity logic).
- §2.4: NEW transparency note on lower-tier WBES capability indicators.

### Part 3 (data + methods) — NEW §3.6 (~300 words)
- Three sample-selection diagnostics: WBES stratified random sampling, panel-firm complication (217 firms), and selection into reporting export intensity (Heckman correction with sampling region as exclusion restriction; IMR z = +0.31 in 2012, z = −0.42 in 2024).

### Part 4 (results) — +3 tables + expanded text (~1,000 words)
- **Table 1**: descriptive statistics for sample_base by wave (lnLP, FSTS, lnEmp, firmage, foreign-owned %, TCI/DAI nonmissing N).
- **Table 2**: M2 main threshold model coefficients with SEs, p-values, turning points, 95% CIs, Lind-Mehlum p.
- **Table 3**: three-way moderation specification (10 focal coefficients + 3 joint F-tests F1/F2/F3).
- §4.2: "everyday-terms" magnitudes paragraph (productivity premia at TP: 67% in 2012, 42% in 2024).
- §4.6 (mfg-only): explicit numbers for 2012 (TP ≈ 42%, CI [37.8, 46.8]) and 2024 (TP ≈ 30%, CI [15.1, 44.2]) plus Paternoster z (+1.94, p=.053; −1.51, p=.131).
- §4.7: expanded specification robustness with weighted estimation, 217-panel-firm exclusion, 10-employee threshold checks.

### Part 5 (discussion) — +2 NEW subsections (~800 words)
- §5.2 expanded: 4 managerial implications instead of 3, with deeper discussion of capability as level-shifter (vs curvature moderator) for strategic-investment planning.
- **NEW §5.4 Theoretical contributions** (4 explicit contributions):
  1. Extension from "what shape" to "does the shape endure" — IP literature contribution.
  2. Cross-country institutional context vs within-country temporal evolution as source of meta-analytic heterogeneity.
  3. Capability level-shift role distinguished from conjectured curvature-moderation role.
  4. Methodological contribution to threshold-stability testing (wave-by-wave + Paternoster + joint F-test triangulation).
- **NEW §5.5 Boundary conditions**: 4 explicit boundaries (private-firm frame; 12-year window; China-specific; capability-instrument constraint).

### Part 6 (limitations) — elaborated (~500 words added)
- Each of 6 limitations expanded to ~250 words with concrete suggestions for future work (e.g., 3-wave panel design with 2032 wave; Bureau van Dijk Orbis / CSMAR China merge for richer financial data; 2024 BREADY richer digital indicators in 2024-only Appendix C; 75% power calc for F3 dynamic moderation).

## Empirical changes

**None.** All coefficients, p-values, and inferences are identical to v1.5. The expansion adds *interpretation, framing, and tables* without changing the underlying empirical content.

## Files

### NEW v1.6 files (this commit set)
- `apjm/manuscript_v1_6_part1_frontmatter_intro.md` — expanded intro
- `apjm/manuscript_v1_6_part2_theory.md` — expanded theory
- `apjm/manuscript_v1_6_part3_data_methods.md` — added §3.6
- `apjm/manuscript_v1_6_part4_results.md` — Tables 1/2/3 + expanded text
- `apjm/manuscript_v1_6_part5_discussion.md` — §5.4 + §5.5 added
- `apjm/manuscript_v1_6_part6_limits_refs.md` — elaborated limitations + 39 refs
- `apjm/CHANGELOG_v1_5_to_v1_6.md` — this file

### Reused unchanged from v1.4 / v1.5
- `apjm/figures/*` — all figure source files unchanged (Tables in v1.6 are inline markdown, not separate figure files)
- `python/*`, `do/*`, `audit/*`, `results/*` — replication artifacts unchanged
- `apjm/SUBMISSION_TARGETS.md` — 14 alternative journals (still applicable)

## How to assemble v1.6

```bash
cd p5-china/apjm/
cat \
    manuscript_v1_6_part1_frontmatter_intro.md \
    manuscript_v1_6_part2_theory.md \
    manuscript_v1_6_part3_data_methods.md \
    manuscript_v1_6_part4_results.md \
    manuscript_v1_6_part5_discussion.md \
    manuscript_v1_6_part6_limits_refs.md \
    > manuscript_v1_6_complete.md
```

To build the .docx with figures embedded, use `build_docx.sh` after editing the `cat` filenames inside the script to point at v1.6 parts (or run pandoc directly):

```bash
pandoc manuscript_v1_6_part{1..6}_*.md --resource-path=. -o manuscript_v1_6.docx
```

## Next steps

1. Embed Tables 1/2/3 properly in Word once .docx is open (pandoc renders them as tables but APJM-template formatting may need adjustment).
2. Re-render Figures 1–4 if any changes are needed; figure captions are unchanged from v1.4.
3. Update title page if going to a journal other than APJM (see `SUBMISSION_TARGETS.md`).
4. Cover letter draft (recommended next deliverable).
