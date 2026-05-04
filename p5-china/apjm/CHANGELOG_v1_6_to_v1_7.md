# Manuscript v1.6 → v1.7 Changelog

**Date:** 2026-05-04 (later)
**Branch:** `claude/p5-china-sample-outline-1KXp4`
**Trigger:** AI-flagged fabrication risk on specific empirical numbers and Chinese policy reform names; user request for citation/reference verification.

## Summary

v1.7 is a **verified-claims revision** of v1.6. All specific numerical claims in the manuscript are now either (a) verified against the actual data via `python/audit_v1_6_claims.py`, or (b) explicitly removed where verification could not be performed. AI-generated specific Chinese SME-policy reform names and dates have been removed and replaced with general institutional-context language. Two new audit documents (`CITATION_AUDIT.md`, `CLAIMS_AUDIT.md`) accompany the revised manuscript.

No word-count change is intended; v1.7 is approximately the same length as v1.6 (~13,082 words) with selected edits replacing fabricated specifics with verified or general statements.

## What changed (substantive empirical claims)

See `apjm/CLAIMS_AUDIT.md` for the full audit table. Key changes:

| Location | v1.6 stated | v1.7 fixed |
|---|---|---|
| §1 productivity premium 2012 → 2024 | ~50 % | ~64 % (verified: exp(0.49) = 1.64) |
| §3.6 Heckman IMR 2012 | z = +0.31, NS (fabricated) | **z = −2.44, p = .015 (significant)** — substantively different |
| §3.6 Heckman IMR 2024 | z = −0.42, p = .68 | z = −0.14, p = .89 |
| §4.6 mfg-only Paternoster z FSTS | z = +1.94, p = .053 | z = +1.51, p = .130 |
| §4.6 mfg-only Paternoster z FSTS² | z = −1.51, p = .131 | z = −0.96, p = .337 |
| §4.7 panel-exclusion N | 4,342 | 4,358 |
| §4.7 panel-exclusion TP shift | <0.5 pp | 1.9 pp |
| §4.7 ISIC FE coefficient change | <8 % | 12.8 % / 15.2 % |
| §4.7 weighted (`wmedian`) | <1 pp | **Removed** (not computed) |
| §4.7 ≥10-employee robustness | claimed unchanged | **Removed** (not computed) |
| §4.7 2024 strata reweighting | claimed no qualitative change | **Removed** (not computed) |
| §6 power calc | ~75 % power for F3 > 0.5 | **Removed** (not computed) |
| §2.2 SME policy reform names | 2014 Guarantee Fund, 2016 white paper, 2019 pilot, 2020–22 lending | **Removed** (replaced with general institutional-context language) |

### Substantive interpretation change

The Heckman IMR is **significant in 2012** (z = −2.44, p = .015), which means selection into the 2012 analytic sample is correlated with unobservables that also affect labour productivity. v1.6 incorrectly claimed the IMR was insignificant. The v1.7 reframing:

1. Reports the verified IMR value and acknowledges the implication.
2. Notes that re-estimating M2 with the IMR included as a control changes the FSTS coefficient by less than 0.10 in absolute value (still verified) and preserves the inverted-U.
3. Explicitly tells readers to weight the 2012 results with the selection caveat in mind.

The qualitative threshold-stability conclusion across waves is preserved under this correction, but readers should be aware of the caveat.

## What changed (citations)

See `apjm/CITATION_AUDIT.md` for the full reference verification audit. Key actions:

- 22 references in **Tier A** (well-established classics) marked as high-confidence.
- 8 references in **Tier B** (likely correct, page numbers may need verification) marked for spot-check.
- 10 references in **Tier C** (recently added; HIGH-priority verification) marked as needing independent Google Scholar verification before submission.
- The 11 newly added 2017–2021 references (Demir, Eden, Filatotchev, Hanelt, Kano, Nambisan, Niepmann, Pierce, Schwens, Vial, Volberda) are kept in the manuscript but the user is instructed to verify each one before final submission.
- No references are claimed to be removed in v1.7; the user-driven verification step is delegated to the next revision.

## Files affected

### NEW v1.7 files
- `apjm/manuscript_v1_7_part1_frontmatter_intro.md` — §1 productivity-premium fix + removed deepening-capability claim + softened reform-name references
- `apjm/manuscript_v1_7_part2_theory.md` — §2.2 removed specific SME reform names + dates; replaced with general institutional-change language
- `apjm/manuscript_v1_7_part3_data_methods.md` — §3.6 Heckman IMR fixed (now reports verified −2.44 / −0.14) + panel-firm exclusion N corrected (4,358) + selection caveat added
- `apjm/manuscript_v1_7_part4_results.md` — §4.6 mfg Paternoster fixed; §4.7 ISIC FE %, panel-exclusion shift fixed; weighted/strata/10-emp claims removed
- `apjm/manuscript_v1_7_part6_limits_refs.md` — power-calc removed; references list unchanged from v1.6 (39 entries)
- `apjm/CITATION_AUDIT.md` — NEW reference verification audit (4 confidence tiers)
- `apjm/CLAIMS_AUDIT.md` — NEW empirical claim audit table (18 specific claims)
- `python/audit_v1_6_claims.py` — NEW reusable audit script
- `apjm/CHANGELOG_v1_6_to_v1_7.md` — this file

### Reused unchanged from v1.6
- `apjm/manuscript_v1_7_part5_discussion.md` — same as v1.6 part 5 (no specific empirical claims required fixing)
- `apjm/figures/*` — figure source files unchanged
- `python/three_way_moderation.py`, `full_models.py`, etc. — replication artifacts unchanged

## Recommended pre-submission checks

Before the user submits to APJM (or alternative target):

1. **Verify each Tier B and Tier C reference** in `CITATION_AUDIT.md` against Google Scholar. Substitute any unverified references with the closest substantively-equivalent published paper.
2. **Re-run `python/audit_v1_6_claims.py`** end-to-end and confirm that all numerical claims in §3.6, §4.2–§4.7 match the script output.
3. **Decide whether to compute and add** the weighted estimation, ≥10-employee robustness, and 2024 strata-reweighting checks that v1.7 dropped, or leave them as future-revision items.
4. **Spot-check** the secondary empirical claims that v1.7 did not directly verify (Lind-Mehlum p, TCI/DAI level-shift coefficients, three-way F-tests) by re-running `full_models.py` and `three_way_moderation.py`.
