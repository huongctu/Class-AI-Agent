# Portfolio Consistency Audit — P3 Singapore / P4 Vietnam / P5 China

**Status**: read-only audit produced 2026-04-30. **Em did not edit any P3/P4/P5 manuscript prose** in producing this document. All three papers remain at the author's current draft state; this audit is a checklist anh can use when finalising P3 and P5.

**Constraint**: per anh's standalone-paper rule, none of the inconsistencies below should be resolved by adding *cross-paper links* inside any manuscript. Resolution should happen at the level of (a) shared variable definitions, (b) numerical inputs to any side-by-side comparison table, and (c) terminological consistency.

---

## 1. Three-paper positioning (per anh's directive)

| Paper | Country / target | Identity |
|---|---|---|
| **P3** | Singapore (MIR) | **Boundary-condition paper** — digital-frontier economy; DAI as scale-contingent complement; TCI as level-shift |
| **P4** | Vietnam (JWB) | **Transition-dynamics paper** — wave-specific instability; TCI both level + curvature; DAI J-curve in direct association; DAI moderation reframed as Proposition P1 |
| **P5** | China (APJM) | **Temporal-evolution paper** — TCI/DAI strengthening 2012→2024; stable inverted-U TP ~48%; Paternoster z-test as central evidence |

---

## 2. Variable construction across the three papers

The pooled WBES dataset (`pooled_wbes_6waves_v2.csv`, 8,589 firms, 6 country-waves) ships harmonised variable names: `foreign_tech` (= WBES `e6`), `product_innov` (= `h1`), `rd_spending` (= `h8`), `quality_cert` (= `b8`), `website` (= `c22b`), `epayment_pct` (= `k33`), `epay_supp_pct` (= `k38`).

### TCI — primary specification per paper

| Paper | TCI primary composite | Item count | Filter |
|---|---|---|---|
| P3 SGP | formative composite — items not yet inspected at variable-definition level (see `Manuscript_Blinded_MIR.docx` §3.2.3) | TBD | — |
| **P4 VNM** | **TCI_thin = (`quality_cert` + `foreign_tech`) / 2** | **2 items** | none |
| **P5 CHN** | **TCI_full = (`foreign_tech` + `product_innov` + `rd_spending` + `quality_cert`) / 4** | **4 items** | **require ≥ 3 non-missing** |

**Inconsistency (REAL).** P4 uses a 2-item TCI as its primary cross-wave specification because `product_innov`/`rd_spending` are absent from the WBES Vietnam 2009 release. P5 uses a 4-item TCI as its primary. This means **the same construct name ("TCI") refers to a measurably different latent quantity** in P4 vs P5. A reviewer reading both papers will rightly object.

**Resolution options for anh's consideration:**

(a) Rename P4's TCI to **TCI_thin** and P5's to **TCI_full** in their respective manuscripts; explicitly acknowledge the difference in measurement scope. (Em P4 already does this — uses "TCI_thin" as the label.) P5 demo currently calls it TCI_full but the manuscript prose may not be explicit yet.

(b) Force both papers to a 2-item composite (P5 would lose `product_innov` + `rd_spending` and N would change). Not recommended — P5 has higher item availability and can support a richer measure.

(c) Force both papers to a 4-item composite (P4 would lose 2009 entirely or impute). Not recommended — destroys P4's temporal-evolution story.

**Em recommends (a).** Distinct labels, explicit measurement-scope acknowledgement. Em P4 manuscript already does this via the §2.2 measurement caveat (commit `c294bc4`).

### DAI — primary and rich specifications

| Paper | DAI primary | DAI rich | Status |
|---|---|---|---|
| P3 SGP | (`website` + `foreign_tech`) / 2 | n/a in prose | — |
| **P4 VNM** | **DAI_thin = (`website` + `foreign_tech`) / 2** | **DAI_rich = (`website` + `foreign_tech` + `epayment_pct/100` + `epay_supp_pct/100`) / 4** | — |
| **P5 CHN** | **DAI_thin = (`website` + `foreign_tech`) / 2** | **DAI_rich = (`website` + `epayment_pct/100` + `epay_supp_pct/100`) / 3** *(no `foreign_tech`)* | **MISMATCH P4 ↔ P5** |

**Inconsistency (REAL).** Both papers use the same DAI_thin construction ✓. But the *rich* specifications differ — P4 includes `foreign_tech` in DAI_rich, P5 excludes it. The exclusion in P5 makes some sense (`foreign_tech` arguably belongs more to TCI than DAI), but consistency requires anh to choose one definition for the portfolio.

**Em recommends:** P5's exclusion of `foreign_tech` from DAI_rich is the more defensible choice on construct-validity grounds (Verhoef et al. 2021's Tier 3-4 capability does not include foreign technology licensing). Em P4 manuscript currently uses `foreign_tech` in DAI_rich and reports it as a robustness check that *attenuates* the DAI direct association below significance — anh may wish to drop `foreign_tech` from DAI_rich in P4 for consistency with P5, but doing so changes P4's §4.6 robustness numbers.

---

## 3. Numerical inconsistency — VN data appearing twice

The P5 update patch (`p5updatepatch.md` line 127-132) contains a *Grand Comparison Table* listing all six country-waves side-by-side. The Vietnam entries in that table use the **V4.3 listwise convention** (which retained WBES `-9` codes as numeric data), not em's verified spec A.

| Quantity | V4.3 numbers (in P5 patch grand table) | Verified spec A (in em P4 v4.4) | Diff |
|---|---|---|---|
| TP 2009 | 36.2% | **43.6%** | +7.4pp |
| TP 2015 | 36.5% | **36.3%** | −0.2pp |
| TP 2023 | 33.8% | **40.6%** | +6.8pp |
| LM p 2009 | .060 | **.128** | +0.068 |
| LM p 2015 | .017 | **.033** | +0.016 |
| LM p 2023 | .029 | **.068** | +0.039 |
| TCI β_z 2009 | .317 | **.224** | −0.093 |
| TCI β_z 2015 | .047 | **.168** | +0.121 |
| TCI β_z 2023 | .180 | **.090** | −0.090 |
| DAI β_z 2009 | .251 | **.122** | −0.129 |
| DAI β_z 2015 | .022 | **.007** | −0.015 |
| DAI β_z 2023 | .176 | **.108** | −0.068 |

**Implication.** If P3 / P4 / P5 are submitted simultaneously and the editor or any reviewer looks at the V4.3-grand-table inside any P5 supplementary file alongside em's verified P4 v4.4, the same Vietnam data will appear with two materially different sets of numbers.

**Resolution required.** When anh finalises P5, either (i) regenerate the grand comparison table for P5 using em's verified P4 spec-A VN numbers, or (ii) drop the grand table from P5 entirely. Em recommends (i) — the grand table's substantive value for P5 (showing temporal evolution comparisons across countries) is real, but the VN entries must reflect the verified pipeline.

Em can produce the spec-A VN numbers in a single CSV export ready for paste into the P5 grand table when anh is ready. (Already in `manuscripts/p4-jwb-vietnam/tables/table_2_baseline.csv` and `tables/table_lind_mehlum.csv`.)

---

## 4. Theoretical positioning — H2 / H4 framing differences

| Hypothesis | P3 SGP | P4 VNM | P5 CHN |
|---|---|---|---|
| **H2** (TCI moderation) | **Predicted level-shift; supported** as level-shift only — H2 confirms the interaction is null. | Revised to "TCI does both level + curvature"; reported as supported in 3/4 panels with negative FSTS × TCI in 2009/2023/pooled. | Not the focal hypothesis (P5 frames TCI as direct effect, no moderation focus). |
| **H4** (DAI moderation) | Directional positive; supported in high export tail (FSTS² × DAI > 0). | Downgraded to **Proposition P1** (sign treated as empirical question after verified spec did not support directional hypothesis). 2023 FSTS × DAI is negative. | Not the focal hypothesis. |

**Reading.** The H2/H4 sign differences across P3 and P4 *can* be theoretically defended as cross-context boundary conditions (Singapore digital-frontier vs Vietnam transitional → different DAI moderation signs). But the **architectural difference** — P3 carries directional H4, P4 has Proposition P1 — is harder to defend as a portfolio if reviewers expect a shared theoretical scaffold.

**Em flags this for anh's editorial decision.** No automatic resolution; this is a co-author judgement call about whether the three papers operate on a shared hypothesis architecture or each builds its own.

---

## 5. Numerical-verification discipline across papers

| Paper | -9 / non-response handling | Triple-source numerical verification | Heckman selection | Paternoster z-test | Lind-Mehlum CI for TP |
|---|---|---|---|---|---|
| **P3 SGP** | not yet inspected (em did not read the data section line-by-line) | not documented | — (single wave) | — (single wave) | reported (no formal support) |
| **P4 VNM** | drop `-9` (transparency note in §3.2) | ✓ statsmodels + linearmodels + manual NumPy/HC1 | ✓ a2 exclusion | ✓ 12-pair table | ✓ delta-method 95% CI |
| **P5 CHN** | not documented in do-file | ✓ Stata-only (single estimator) | not in do-file | ✓ TCI / DAI / FSTS pairs | reported via nlcom |

**Em recommends** anh consider whether to retro-apply the **same** verification discipline (-9 handling + Heckman + triple-source) to P3 and P5 before submission. The integrity gain is real; the time cost is several days of additional work per paper. If the three papers will be submitted same-time and reviewers cross-reference them, having P4 alone document `-9` handling while P3/P5 do not creates a consistency hole.

---

## 6. Sample-frame disclosure

| Paper | Filter that shrinks N | Disclosure quality |
|---|---|---|
| **P3 SGP** | (single wave 2023, N = 623) | not yet inspected |
| **P4 VNM** | listwise on focal vars + drop `-9` codes (N drops 1,053→734, 996→614, 1,028→974) | ✓ explicit transparency note in §3.2 |
| **P5 CHN** | TCI_full requires ≥3 non-missing items → 2012 N drops 2,684→1,613 because `rd_spending` (CNo3) is asked only after innovation gate per WBES skip pattern | ✓ explicit Table 4 footnote in patch ("CNo3 fix") |

**Both P4 and P5 have explicit sample-frame transparency notes.** Good portfolio discipline. P3 needs to be checked when anh finalises the SGP draft.

---

## 7. WBES citation discipline

WB recommends citation: *"Source: World Bank Enterprise Surveys, www.enterprisesurveys.org"* and acknowledgement: *"We thank the Enterprise Analysis Unit of the Development Economics Global Indicators Group of the World Bank for the data."* (per em's earlier audit at https://www.enterprisesurveys.org/en/citing-the-data).

| Paper | WB-style citation | WB-style acknowledgement | Data Access Protocol non-redistribution note |
|---|---|---|---|
| **P3 SGP** | "World Bank. (2024). World Bank Enterprise Survey: Singapore 2023. https://www.enterprisesurveys.org" — close to WB form but uses "World Bank" not "Source: World Bank Enterprise Surveys" prefix | not yet inspected | not yet inspected |
| **P4 VNM** | ✓ exact WB-recommended form (3 wave entries) | ✓ verbatim | ✓ §3.1 + §3.2 + Title page + README |
| **P5 CHN** | not yet checked in patch (the do-file does not have a manuscript section for citations) | not yet checked | not yet checked |

**Em recommends** P3 and P5 both adopt em P4's WBES citation block (Acknowledgement paragraph + 3 wave references in WB recommended form + non-redistribution note). Em P4 uses the wording verbatim from the WB citing-the-data page; identical wording across all three papers in the portfolio is appropriate and unproblematic since WB *itself* asks for this wording.

---

## 8. Concrete portfolio checklist for anh

When finalising P3 and P5, em recommends going through this checklist:

- [ ] Decide TCI label discipline: P3 SGP and P5 CHN use **TCI_full** (4-item); P4 VNM uses **TCI_thin** (2-item, due to 2009 data limitation). Make this distinction explicit in each paper's §3.2.
- [ ] Resolve DAI_rich definition: drop `foreign_tech` from DAI_rich in P4 to match P5's definition, OR add `foreign_tech` to P5's DAI_rich to match P4. Em recommends the former (drop from P4).
- [ ] Regenerate any cross-country comparison table (e.g. the P5 grand table) using em's verified P4 spec-A VN numbers, **not** the V4.3 numbers currently in the patch.
- [ ] Decide H4 architecture: keep directional H4 in P3, downgrade to Proposition in P4 (already done), and choose framing for P5. Document in each paper's §2.3 why the framing differs across countries (or align across all three).
- [ ] Apply em P4's WBES citation block (Acknowledgement + 3 wave entries + non-redistribution note) verbatim to P3 and P5.
- [ ] Apply em P4's `-9` transparency rule to P3 and P5 — re-run analyses with `-9` treated as missing. If numbers shift, document via a transparency paragraph.
- [ ] Consider applying em P4's triple-source numerical verification to P3 and P5 before submission. If anh prefers to skip this for P3/P5, em recommends mentioning in the cover letter that "P4's verified pipeline produced numerical agreement to machine precision; P3/P5 use Stata-only single-estimator analysis."
- [ ] Decide whether to commit P3 and P5 manuscripts into this same repo (would enable em to do similar audits as final drafts come in) or keep them in separate repos.

---

## 9. What em did NOT do in this audit

- Em did **not** edit any P3, P4, or P5 manuscript prose.
- Em did **not** re-run any pipeline.
- Em did **not** propose adding a "research programme" or "cross-paper" sentence to any manuscript (per anh's standalone-paper rule).
- Em did **not** export verified VN numbers for paste into P5's grand table (em can do this on request).
- Em did **not** read every paragraph of P3 SGP. Specifically, em did not inspect P3's §3.2.3 line-by-line variable definitions or P3's data preparation script (if any). The TCI / DAI item list for P3 is therefore listed as TBD in this audit.

---

*End of audit. Last updated 2026-04-30 by em (Claude in this session). Generated read-only from PR-#2 source files; no manuscript prose modified.*
