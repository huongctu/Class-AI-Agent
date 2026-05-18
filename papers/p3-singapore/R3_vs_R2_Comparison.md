# Manuscript Comparison: R2 Original vs R3 Final

**Files compared:**
- R2 original: `Manuscript_Blinded_MIR_2_original.docx`
- R3 final: `Manuscript_Blinded_MIR_2_revised.docx`

**Date:** 2026-05-03
**Branch:** `claude/p3-r3-revision` · PR #6 (20 commits)

---

## 1. Quick stats

| Metric | R2 original | R3 final | Δ |
|---|---:|---:|---:|
| Total paragraphs | 148 | 163 | +15 |
| Manuscript words | 7,828 | 8,140 | +312 |
| Abstract words | 229 | 215 | -14 |
| Tables | 4 | 4 | +0 |

---

## 2. Title

**R2:** Technological Capability, Digital Adoption, and the Internationalization–Performance Relationship in Singapore

**R3:** Technological Capability, Digital Adoption, and the Internationalization–Performance Relationship: A Firm-Level Study of Singapore

**Diff:** R3 adds *': A Firm-Level Study of Singapore'*; removes implicit boundary-condition framing.

---

## 3. Section structure

### Sections only in R2 (removed/renamed in R3)

- `4.3 TCI direct effect supports H1; TCI moderation null supports H2`
- `4.4 DAI moderation: evidence concentrated in the high-export tail`
- `6 Limitations and Future Research`

### Sections only in R3 (newly added)

- `4.3 TCI results`
- `4.4 DAI results`
- `6 Conclusion`
- `7 Limitations and Future Research`
- `Data Availability Statement`

### Major structural changes

- **§4.3 renamed:** R2 *'TCI direct effect supports H1; TCI moderation null supports H2'* → R3 *'TCI results'* (narrower title because H2 has been demoted to a research question; section no longer claims to *support* H2).
- **§4.4 renamed:** R2 *'DAI moderation: evidence concentrated in the high-export tail'* → R3 *'DAI results'* (generalises section, includes new clarification paragraph about M8 centering arithmetic).
- **§6 NEW:** R3 adds a standalone *'6 Conclusion'* section. R2 went straight from §5 Discussion to §6 Limitations.
- **§7 renumbered:** R2 *'6 Limitations and Future Research'* → R3 *'7 Limitations and Future Research'* (because of the new §6 Conclusion above).
- **NEW: Data Availability Statement** added between §7 and References.

---

## 4. Abstract — full side-by-side

### R2 original (229 words, single paragraph)

> This study examines whether technological capability and digital adoption play distinct roles in shaping the internationalization–performance relationship in a digital-frontier economy. Using World Bank Enterprise Survey microdata for Singapore 2023 (N = 623), the analysis develops a two-construct measurement architecture that separates a Technological Capability Index (TCI), anchored in the Lall (1992) capability tradition, from a Digital Adoption Index (DAI), anchored in the digital strategy and digitalization literature (Bharadwaj et al., 2013; Verhoef et al., 2021). TCI is positively associated with labour productivity and operates as a level-shift effect on the productivity intercept rather than as a curvature-shaping moderator. The baseline internationalization–performance pattern is best characterized as primarily monotonic with mild quadratic curvature within the observed export-intensity range; given the thin right tail of the FSTS distribution, the inferred turning point should be read as suggestive rather than as formally identified evidence of a conventional inverted-U. DAI shows conditional relevance: its productivity association becomes more positive at higher levels of export intensity, although the evidence is concentrated in the high-export tail rather than distributed uniformly across the sample. These findings suggest that, in a digitally mature institutional environment, digital adoption may matter less as a universal firm-level productivity premium and more as a scale-enabling complement for firms facing more demanding cross-border coordination. The study contributes sharper construct validity and an initial boundary-condition argument for internationalization research in digital-frontier settings.
>

### R3 final (215 words, two paragraphs)

> This study examines how technological capability and digital adoption are associated with the internationalization–performance relationship among firms in Singapore, treated as an analytically informative, within-context setting of a digitally advanced economy. Using World Bank Enterprise Survey microdata for Singapore 2023, the analysis distinguishes a Technological Capability Index (TCI), capturing firm-internal capability depth, from a Digital Adoption Index (DAI), capturing foundational digital interfaces and transaction-enabling mechanisms.
>
> Three findings emerge. First, within the observed export-intensity range, the internationalization–performance relationship is better characterized as predominantly positive with mild quadratic curvature than as a formally identified inverted-U. The fitted quadratic implies a turning point in the upper tail, but that point is imprecisely located and falls in a sparsely populated region of the data. Second, TCI is positively associated with labour productivity, while no statistically distinguishable moderation by TCI is detected under the present design. Third, DAI does not exhibit a large uniform productivity premium across firms; instead, its association with productivity becomes more positive at higher levels of export intensity, with the clearest signal concentrated in the high-export tail. Taken together, the findings provide within-context evidence from Singapore that sharpens the distinction between technological capability and foundational digital adoption and suggests that digital adoption may function more as a contingent scaling resource than as a uniform productivity advantage.
>

**Key changes:**
- Length cut from 229 to 215 words (+14 → much tighter, within MIR 250 limit).
- *'in a digital-frontier economy'* removed.
- *'level-shift effect on the productivity intercept'* removed.
- *'sharper construct validity and an initial boundary-condition argument for internationalization research in digital-frontier settings'* → *'within-context evidence from Singapore that ... suggests that digital adoption may function more as a contingent scaling resource than as a uniform productivity advantage.'*
- New explicit numbers in findings: *'imprecisely located and falls in a sparsely populated region'* signals the bootstrap CI work.

---

## 5. Hypotheses — claim register tightened

### H1 (TCI direct) — UNCHANGED
> **R2:** Hypothesis 1 (H1). Technological capability (TCI) is positively associated with firm performance in Singapore.
>
> **R3:** Hypothesis 1 (H1). Technological capability (TCI) is positively associated with firm performance in Singapore.

### H2 (TCI moderation) — DEMOTED to research question
> **R2:** Hypothesis 2 (H2). The TCI–productivity association in Singapore operates predominantly as a level-shift effect on the productivity intercept rather than as a curvature-shaping moderator of the internationalization–performance relationship.
>
> **R3:** *(no longer a labelled hypothesis)* — Whether technological capability (TCI) also moderates the internationalization–performance relationship is treated as an open empirical question and assessed in a supplementary specification rather than as a hypothesized moderation channel.

**Rationale:** R2 asserted TCI as a *level-shift* rather than moderator. Reviewer pointed out that a non-significant interaction does not establish absence of moderation. R3 drops the H2 label and treats TCI moderation as an open empirical question tested supplementarily.

### H3 (DAI direct) — REFRAMED
> **R2:** Hypothesis 3 (H3). Digital adoption (DAI) is positively associated with firm performance in Singapore on average, with the magnitude of this association expected to vary systematically with the firm’s internationalization intensity (formally tested in H4).
>
> **R3:** Hypothesis 3 (H3). The productivity association of digital adoption (DAI) in Singapore is conditional rather than uniform across firms.

**Rationale:** R2 predicted DAI is *positively associated on average*. M8 actually shows direct DAI null (β=0.019, p=.705); Table 4 shows DAI sig at FSTS=0, null in middle, sig in upper tail. R3 reframes from average premium to conditional non-uniformity, matching what the data actually estimate.

### H4 (DAI moderation by FSTS) — UNCHANGED
> **R2:** Hypothesis 4 (H4). The association between digital adoption (DAI) and firm performance becomes more positive at higher levels of export intensity in Singapore.
>
> **R3:** Hypothesis 4 (H4). The association between digital adoption (DAI) and firm performance becomes more positive at higher levels of export intensity in Singapore.

---

## 6. NEW Section 6 — Conclusion (was absent in R2)

**R2:** No standalone Conclusion section. Discussion (§5.1, §5.2) flowed directly into §6 Limitations.

**R3:** Adds three Conclusion paragraphs that:
- Restate the construct distinction (TCI = direct level effect; DAI = conditional scaling).
- Qualify the I-P literature interpretation in this setting without overturning it.
- Explicitly disavow generalising to all digitally advanced economies; close with call for comparative + longitudinal future research.

---

## 7. Section 7 (Limitations) — major rewrite

**R2 §6 Limitations:** ~700 words, defensive, included long Heckman / Wolfolds & Siegel tangent, equivalence-testing tangent, framing as 'extreme-case, within-context evidence'.

**R3 §7 Limitations:** 430 words, focused on three clean limitations:
1. Associational single-country cross-section (reverse causation, omitted variables, selection).
2. Thin upper-tail support (bootstrap CI [53%, 253%]; 96.3% inverted-U recovery; precision constraint in N=84).
3. Tier 1–2 measurement boundary (DAI captures foundational adoption, not deeper organizational capability or AI-grade dynamic capability).

**Plus:** Concrete future-research IV strategies — firm-to-port distance, customs-clearance times, regional broadband coverage, within-sector peer adoption — with Wolfolds & Siegel (2019) caveat (added in Pass 5).

---

## 8. Tables — what changed

| Table | R2 | R3 | Status |
|---|---|---|---|
| Table 1 (Descriptive + Correlations) | Same | Same | ✓ Unchanged |
| Table 2 (Hierarchical OLS M0–M8) | Same structure | Same structure; M8 R²/AdjR² text aligned with table | ✓ Numerical consistency fixed (Pass 3 D1) |
| Table 3 (Robustness, 6 specs) | All 6 rows had stale numbers from earlier draft | All 6 rows re-estimated from raw .dta with locked spec; baseline now matches Table 2 M8 exactly | ✓ Major fix (Pass 0) |
| Table 4 (Marginal effects of DAI) | Same | Same; §4.4 prose now consistent with FSTS=0 row +0.080 (p=.045) | ✓ Internal consistency fixed (Pass 3) |

---

## 9. Figures — all three regenerated from canonical data

| Figure | R2 | R3 |
|---|---|---|
| Figure 1 (Conceptual) | Old IB-style with 'Boundary condition: Digital-frontier institutional environment' panel at bottom | Redesigned IV/DV/Moderator/Control framework; bottom panel now 'Scope: extreme-case, within-context evidence from Singapore' |
| Figure 2 (DAI marginal effect) | Plain marginal-effect curve | **Support-aware version**: rug strip + decile counts + thin-tail (>70%) shaded grey; reader sees exactly where the high-tail signal sits relative to data density |
| Figure 3 (Predicted I-P curve) | Plain quadratic with TP at 88.6% | **Bootstrap-aware version**: 95% CI band for predicted line + red shaded vertical band for the turning-point CI [52.8%, 252.9%] + in-figure note '96.3% of bootstrap replications recover an inverted-U shape' |

---

## 10. Five reviewer concerns — disposition

| Reviewer issue | R2 status | R3 status |
|---|---|---|
| #1 Digital-frontier overclaim | Title: *'in Singapore'* (neutral but Abstract used 'digital-frontier economy'); Abstract closed with 'boundary-condition argument for digital-frontier settings' | Title: *'A Firm-Level Study of Singapore'*; Abstract drops boundary-condition wording entirely; framed as 'within-context evidence' throughout |
| #2 TCI/DAI fungibility | Construct architecture stated but no item-level sensitivity disclosed in prose | Cross-construct r=0.106 reported; SWAP1 falsification in §4.5 (joint F drops .011 → .154 when c22b reassigned to TCI); deeper item-to-construct theory in §3.2.3 |
| #3 Extensive vs intensive margin | Full-sample polynomial used as primary I-P test | §3.3 explicitly frames full-sample polynomial as descriptive baseline; Stage-1 logit (extensive) + Stage-2 OLS on N=84 exporters (intensive) added |
| #4 Right-tail leverage | Acknowledged in passing | Cook's D + LOO + trimmed-tail + bootstrap CI all implemented; figures support-aware; §7 explicitly grounds caution in thin upper tail |
| #5 Hypothesis ↔ estimate mismatch | H2 claimed level-shift; H3 claimed positive-on-average | H2 demoted to research question; H3 reframed to conditional non-uniformity; §4.4 includes M8-centering clarification |
| D1 Table 3 baseline mismatch | Stale numbers across all 6 rows | All 6 rows re-estimated from raw .dta and corrected (Pass 0) |
| D2 Mis-grounded caveat | Used adj-R² across samples | §7 limitation 2 grounded in thin upper-tail support and small-subsample precision instead |

---

## Bottom line

R3 is **substantially different from R2** in framing, claim register, structure, and numerical consistency. Specifically:

- **Framing:** Singapore is now a within-context, analytically informative case rather than a basis for a general boundary condition for digitally mature economies.
- **Claims:** H2 demoted to research question; H3 reframed to non-uniformity; *'level-shift effect'* and *'inverted-U is robust'* phrasing fully removed.
- **Structure:** New §6 Conclusion; §7 Limitations cut to 430 words; §3.2.3 deeper item-to-construct theory; §4.5 item-swap falsification visible.
- **Numerical consistency:** Table 3 fully re-estimated (all 6 rows); §4.4 prose matches Table 2 M8 (R²=0.211, adj R²=0.196) and Table 4 (FSTS=0 effect=+0.080 p=.045).
- **New theory:** TCE (Coase 1937; Williamson 1985) framing for the conditional DAI mechanism in §5.1.
- **Figures:** All three regenerated from canonical data; Figures 2 and 3 are now support-aware; Figure 1 redesigned to standard IB IV-DV-Moderator-Control framework.

Final consistency audit: **13 / 13 pass · 0 issues**.