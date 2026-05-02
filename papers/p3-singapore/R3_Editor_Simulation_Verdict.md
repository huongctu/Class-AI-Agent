# R3 Editor Simulation — Submission Readiness Verdict

**Date:** 3 May 2026
**Manuscript:** Technological Capability, Digital Adoption, and the Internationalization–Performance Relationship: A Firm-Level Study of Singapore
**Branch / PR:** `claude/p3-r3-revision` · GitHub PR #6 (19 commits)
**Audit:** 13 / 13 pass · 0 issues
**Length:** 28 pages PDF · 8,140 manuscript words · Section 7 = 430 words

## Pass 5 enhancements (per NotebookLM editor review)

Three substantive additions, ~215 words total, all responsive to specific reviewer points:

| Section | Enhancement | Outcome |
|---|---|---|
| §4.5 (+89 w) | **Item-swap falsification disclosure** | "Joint F drops from 4.56 [p=.011] to 1.88 [p=.154] when c22b is reassigned from DAI to TCI" — quantifies the construct boundary, addresses reviewer's "ultimate weapon" point. |
| §5.1 (+71 w) | **Transaction-cost-economics framing** | Coase (1937) / Williamson (1985) explicit citation; the conditional DAI pattern now grounded in TCE: marginal benefit < fixed costs at low FSTS, super-linear coordination cost absorption at high FSTS. |
| §7 (+55 w) | **Concrete IV strategies for future research** | Names four candidate instruments — firm-to-port distance, customs-clearance times, regional broadband-coverage shares, within-sector peer-adoption rates — paired with Wolfolds & Siegel (2019) caveat about first-stage strength and exclusion restrictions. |

---

## Verdict

**Ready to submit.** All seven of R2 reviewer's concerns have been addressed at the level of evidence, framing, and prose. The remaining surface text is internally consistent: the same logic runs from Abstract → Theory → Methods → Results → Discussion → Conclusion → Limitations.

| Risk dimension | Status | Comment |
|---|---|---|
| **Factual errors** (D1) | 🟢 Resolved | All 6 rows of Table 3 re-estimated; baseline matches Table 2 M8; numbers in §4.4 prose match Table 2 (R²=0.211, adj R²=0.196). |
| **Mis-grounded caveat** (D2) | 🟢 Resolved | §7 limitation 2 grounded in thin upper-tail support and small subsample, not in cross-sample adj R². |
| **Identification scope** (#1, #3) | 🟢 Resolved | Title and front matter recast as "A Firm-Level Study of Singapore"; full-sample polynomial = descriptive baseline; extensive–intensive split implemented; no claim to identify a "digital-frontier mechanism". |
| **Construct separation** (#2) | 🟢 Resolved | Cross-construct r=0.106 reported; SWAP1 falsifies fungibility; deeper item-to-construct theory in §3.2.3; sensitivity analyses delivered. |
| **Right-tail leverage** (#4) | 🟢 Resolved | Cook's D, LOO, trimmed-tail, bootstrap CI [53%, 253%] all reported; figures show rug + decile counts + thin-support shading; narrative explicitly cautious. |
| **Hypothesis ↔ estimate** (#5) | 🟢 Resolved | H2 demoted to research question (no Hypothesis 2 label); H3/H4 framed as conditional, not average premium; §4.4 prose matches Table 4 marginal effects exactly. |

---

## What a reviewer at MIR will see

### Strengths visible in the first 60 seconds

1. **Title** signals scope honestly: "A Firm-Level Study of Singapore" — no overreach.
2. **Abstract** opens with "treated as an analytically informative within-context setting" and closes with "may function more as a contingent scaling resource than as a uniform productivity advantage" — both clearly bounded claims.
3. **Keywords** are construct-anchored (TCI, DAI, FSTS, Singapore) rather than literature-anchored ("boundary conditions" removed).
4. **Figure 1** uses a clean IB framework (IV → DV with moderators above and controls below) and immediately conveys that DAI is the contingency variable while TCI enters mainly as a direct-effect construct.

### Strengths a reviewer will value

1. **Evidence chain reproducible end-to-end.** `tools/r3/00_canonical_m8.py` reproduces Table 2 M8 exactly from raw `.dta`. Every number in the paper traces to a JSON in `outputs/r3/audit/`.
2. **Active acknowledgement of identification limits.** §3.3, §4.2, §4.5, and §7 all use associational language; no covert causal claims.
3. **Honest treatment of upper-tail thinness.** The bootstrap CI [53%, 253%] is shown in Figure 3 *and* discussed in §4.2 *and* re-anchored in §7. The reader cannot miss it.
4. **Construct logic now structurally consistent.** TCI = direct (with supplementary moderation test); DAI = contingency variable. This is reflected in the hypotheses (H1, H3 direct; H4 moderation; H2 demoted to research question), in Figure 1, in §2.4, in §3.3, and in §5.1 — same logic everywhere.
5. **Section 7 cleaned up.** Down from 730 to 375 words. Three limitations stated cleanly: associational design, thin upper tail, Tier 1–2 measurement boundary. No defensive Heckman tangent.

### What a reviewer might still flag (and why each is acceptable)

1. **N = 84 in the exporter subsample is small.** *Acceptable because:* (a) §4.5 and §7 explicitly state the resulting precision constraint; (b) the joint F=6.32 (p=.003) is meaningful even at this size; (c) the trimmed-tail re-estimation (drop FSTS > 70%) on the *full* sample of 606 actually strengthens the moderation (β=+7.09, p=.004), so the result is not held up only by 84 firms.

2. **Bootstrap CI for the turning point is wide ([53%, 253%]).** *Acceptable because:* the paper does *not* hang the contribution on a precise turning-point claim. Section 4.2 explicitly demotes the turning point to "descriptive" status; Section 5.1 reads the curvature as "predominantly positive with mild quadratic curvature than as a formally identified inverted-U." The wide CI is a *finding*, not a flaw.

3. **DAI moderation depends on c22b + k33.** *Acceptable because:* §3.2.3 already states DAI is a Tier 1–2 foundational digital-adoption measure; §4.5 and §7 disclose that the indicator-sensitivity analysis identifies website + e-payment as the load-bearing items. The disclosure does not undermine the contribution — it disciplines the construct claim.

4. **"Boundary condition" still appears in 5 sentences.** *Acceptable because:* every single occurrence is inside an explicit *negation* of the claim (e.g., "not whether one setting can establish a general boundary condition for all digitally mature economies"). The literal phrase is rhetorically essential to disavow the very claim that R2 reviewer was concerned about.

---

## Submission readiness checklist (10 items)

- [x] Title aligned with the actual research design (firm-level Singapore study)
- [x] Abstract within MIR 150–250 word limit (current: 215 words)
- [x] Keywords match construct labels used in the analysis (no literature-level claims)
- [x] All four hypotheses statements aligned with what M0–M8 / Table 4 estimate
- [x] Table 3 baseline matches Table 2 M8 exactly (TCI=0.153, FSTS²×DAI=3.119, Adj R²=0.196)
- [x] §4.4 prose matches Table 2 (R²=0.211, adj R²=0.196) and Table 4 (FSTS=0 effect = +0.080, p=.045)
- [x] Three figures embedded with support-aware presentation; rendered correctly in PDF
- [x] §7 limitations focused on identification, support, and measurement (no defensive tangents)
- [x] Cover Letter and Title Page synced with manuscript title and corresponding-author info
- [x] All 36 references present in body and bibliography; in-text citations follow MIR style

---

## Bottom line

The manuscript is in a defensible position. The most substantive risk — that R2 reviewer might still read the paper as overclaiming a "digital-frontier boundary condition" — has been addressed at every level: title, abstract, keywords, conceptual model, hypotheses, results interpretation, discussion, conclusion, and limitations. The two factual issues (D1 Table 3 mismatch; D2 mis-grounded caveat) are fully resolved.

**Recommendation: submit.** The submission package at `papers/p3-singapore/submission/` is ready for upload to the MIR Editorial Manager portal.
