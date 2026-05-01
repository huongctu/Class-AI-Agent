# Response to Editor and Reviewers — P4 v4.4 Revision

**Manuscript:** *Digital Adoption, Technological Capability, and the Internationalisation–Performance Relationship in Vietnam: Evidence from a Transitional Digital Economy*

**Submission to:** *Journal of World Business* — v4.4 revision following Major Revision decision

**Date:** 30 April 2026

---

## Overview

We thank the Editor and the anonymous Reviewer team for the rigorous and constructive critique delivered with the Major Revision decision. The review identified six categories of mandatory methodological and theoretical upgrade and a clear evaluative threshold against which the next round will be assessed. We have responded to every point raised in the letter and provide below a point‑by‑point reply, indicating where each requirement is now addressed in the revised manuscript and supplying the specific numerical results that the upgraded analytic pipeline produced.

A summary of the eight‑commit incremental revision arc that produced the v4.4 manuscript is logged in `changelog_v4_3_to_v4_4.md` and visible in the timeline of pull request #2 on the manuscript repository. Throughout this response we adopt the linguistic and inferential discipline the review mandated: all claims about predictor–outcome relationships are stated as *associations* rather than *effects*, and we report verified numerical results rather than the v4.3 values referenced in the review letter.

A note on numerical consistency. Several of the reviewer's expected p‑values and coefficients (LM p = .060/.017/.029; exporter share 28.2% → 18.9%; DAI 2009 β = 0.251, DAI 2015 β = 0.022, DAI 2023 β = 0.176) reflect the v4.3 listwise convention that retained WBES non‑response code `-9` as numeric data. The verified spec adopted in v4.4 treats `-9` as missing, an alignment with WBES codebook guidance that we believe materially strengthens the integrity of the analysis. A second refinement, undertaken in response to a third‑party advisory between earlier internal review and the present submission, retired the two‑item DAI composite (`c22b` + `e6`) used in v4.3 and earlier v4.4 drafts in favour of a single‑item DAI_core operationalised by `c22b` (own‑website presence) only. The motivation is construct‑separation: `e6` (foreign‑licensed technology) is a Lall (1992) capability indicator and belongs theoretically in the TCI composite rather than in the digital‑adoption index, and its inclusion in DAI mechanically inflated the within‑wave TCI–DAI correlation (~0.6 under the two‑item composite, ~0.32 under DAI_core; see §4.1). Under the verified + decontaminated specification, DAI 2009 β = 0.175, DAI 2015 β = 0.008, DAI 2023 β = 0.113, DAI pooled β = 0.108. The §3.2 transparency paragraph explains both refinements, and where the reviewer asked us to "achieve" specific p‑values we have transparently reported the verified values rather than reverse‑engineering the analysis to match the v4.3 numbers.

---

## Point‑by‑point response

### Requirement 1 — Causal language and unobserved heterogeneity

**Reviewer's mandate.** "WBES dưới dạng pooled cross-section ... khiến việc kiểm soát unobserved heterogeneity là bất khả thi. Tác giả phải thay đổi toàn bộ ngôn từ: chuyển từ 'tác động' (effect) sang 'mối liên hệ' (association)."

**Response.** Adopted throughout. Section 3.3 now explicitly states: *"Throughout, we describe results as associations rather than effects, consistent with the inferential limits of repeated‑cross‑section data: in the absence of within‑firm panel structure we cannot identify causal effects within firms, only the cross‑sectional contemporaneous association between predictors and outcomes (Antonakis et al., 2010). This linguistic discipline is enforced even where it produces less elegant prose than the causal alternative."* Sections 4.3, 4.4, 4.6, and 5 use *association* / *associated with* in place of *effect* / *causes*. The Vietnamese gloss *tính không đồng nhất không quan sát được* is provided in §6 as part of the limitations discussion. Section 6 retains as its first principal limitation: *"the WBES microdata are repeated cross‑sections rather than a true firm panel; we cannot identify within‑firm change over time and cannot control for time‑invariant unobserved heterogeneity."*

**Manuscript locations.** §3.3 (paragraph 3); §4.3 heading + body; §4.4 heading + body; §4.6 paragraph 1; §5 throughout; §6 paragraph 1.

---

### Requirement 2 — Heckman selection with `a2` exclusion restriction; report Inverse Mills Ratio

**Reviewer's mandate.** "Sử dụng mô hình Heckman Selection Model. Sử dụng biến khu vực (a1) làm biến loại trừ ... Để kết quả OLS được chấp nhận, hệ số λ phải được chứng minh là không có ý nghĩa thống kê."

**Response.** Implemented. Section 3.3 now makes the exclusion‑restriction logic explicit: *"sampling region affects the probability of export selection through differential access to logistical infrastructure (port proximity, trade‑finance availability, customs clearance throughput) but does not affect intrinsic firm productivity once firm capability and digital adoption are controlled for; this is the same exclusion logic used by Cuervo‑Cazurra & Genc (2008) for emerging‑market exporter studies."* We use `a2` (sampling region within country) rather than `a1` because `a1` is the country code in the WBES instrument and offers no within‑Vietnam variation; `a2` is the equivalent within‑country regional indicator the reviewer presumably had in mind.

Section 4.6 reports the Inverse Mills Ratio λ from the selection equation appended to the outcome equation:

| Wave | λ | p (λ) | n exporters | Verdict |
|---|---|---|---|---|
| 2009 | −0.066 | .900 | 264 | Insignificant |
| 2015 | −0.463 | .554 | 164 | Insignificant |
| 2023 | +0.726 | .364 | 178 | Insignificant |
| Pooled | +0.151 | .734 | 606 | Insignificant |

Per the reviewer's criterion that OLS is valid only if λ is statistically insignificant, the null λ across all four panels validates the OLS specification adopted in §4.2–§4.5. As an additional cross‑check, the §4.6 control‑function specification (Wooldridge 2010, eq. 17.32) replaces the IMR with the generalised residual from the same probit and yields the same direction of inference.

**Manuscript locations.** §3.3 (paragraph 2); §4.6 (paragraph 1).

---

### Requirement 3 — Construct validity (Thin → Rich): TCI must add `h1`/`h8`; DAI must add `k33`/`k38`

**Reviewer's mandate.** "Thang đo Thin hiện tại quá mỏng và không đạt chuẩn quốc tế. Tác giả phải nâng cấp lên thang đo Rich làm mô hình phân tích chính ... DAI phải tích hợp thanh toán điện tử (k33, k38) ... để phản ánh Tier 4 (Digital Dynamic Capability) theo Verhoef et al. (2021)."

**Response.** Partially adopted, with explicit justification for the partial adoption. Section 3.2 now describes both an extended TCI_full composite (adding `h1` innovation and `h8` R&D, capturing absorptive capacity per Lall 1992 and Cohen & Levinthal 1990) and an extended DAI_rich composite (adding `k33` and `k38` e‑payment intensities, capturing Tier 3–4 dynamic digital capability per Verhoef et al. 2021). Both composites are estimated and reported in the §4.6 robustness panel.

We do not adopt DAI_rich as the primary specification. The reasoning is structural: `k33` and `k38` are absent from the 2009 and 2015 WBES instruments — the public release of these waves does not include any e‑payment items at all (see `output/wbes_vn_inspection.md`, where the cross‑wave summary table shows `k33` and `k38` available in 2023 only). Promoting DAI_rich to the primary specification would force a choice between two undesirable alternatives: (a) restrict the analytic sample to the 2023 wave, eliminating the cross‑wave J‑curve evidence that motivates H3 in §2.3.3 and forfeiting the cross‑wave Paternoster panel on which the §5.1.2 capability‑convergence claim rests; or (b) impute pre‑2023 e‑payment data without a defensible scaffold, an imputation that would be more invasive than the reviewer's instrument‑integrity standard would tolerate.

The DAI_rich estimate is reported in §4.6 with full transparency:

| Specification | β_z | SE | p | Cf. DAI_thin (2023) |
|---|---|---|---|---|
| DAI_rich continuous (`c22b` + `k33` + `k38`; e6 dropped) | +0.049 | 0.050 | .327 | β_z = 0.113, p = .021 |
| DAI_rich binary (`c22b` + `k33` + `k38`; e6 dropped) | +0.042 | 0.044 | .336 | β_z = 0.113, p = .021 |

The DAI_rich attenuation below significance is itself a contribution: it documents the measurement‑granularity tension between binary and continuous digital‑adoption items (k33/k38 are continuous percentages; c22b/e6 are binary), and it argues for a field‑level convergence on a measurement standard that handles the binary/continuous mix consistently. Section 6 includes this point as a principal limitation.

The TCI_full estimate is reported in §4.6 paragraph 2: TCI_full attenuates by 62% relative to TCI_thin in the 2015 wave (β_full = 0.063 vs β_thin = 0.168) and by 38% in 2023 (β_full = 0.056 vs β_thin = 0.090). The thin‑vs‑full divergence is consistent with the two composites capturing distinct dimensions of capability — TCI_thin proxies foreign‑capability access (`b8` certification + `e6` foreign‑licensed technology), while TCI_full incorporates innovation outputs (`h1`, `h8`) that are themselves products of capability rather than direct measures of it.

**Manuscript locations.** §3.2 (variable construction); §4.6 (TCI_full and DAI_rich paragraphs).

---

### Requirement 4 — Lind–Mehlum p per wave + cross‑country TP comparison

**Reviewer's mandate.** "Bắt buộc báo cáo chi tiết p-value của kiểm định Lind và Mehlum (2010) cho từng làn sóng dữ liệu riêng biệt (yêu cầu đạt ngưỡng: .060 cho 2009, .017 cho 2015, và .029 cho 2023)."

**Response — first part adopted, second part declined.** The wave‑specific Lind & Mehlum (2010) U‑test is reported in Section 4.2, with the delta‑method 95% CI for the turning point in each wave. The verified specification yields:

| Wave | LM p | TP point estimate (raw FSTS %) | 95% CI |
|---|---|---|---|
| 2009 | .128 | 43.6% | [24.8%, 62.4%] |
| 2015 | .033 | 36.3% | [23.9%, 48.7%] |
| 2023 | .068 | 40.6% | [26.3%, 55.0%] |
| Pooled | .041 | 31.4% | [16.4%, 46.4%] |

We must respectfully note that the reviewer's expected thresholds (.060 for 2009, .017 for 2015, and .029 for 2023) reflect the v4.3 listwise convention that retained WBES `-9` codes as numeric data. The verified spec — which we believe better satisfies the methodological transparency standards Antonakis et al. (2010) articulate — yields the values above. We have not reverse‑engineered the analysis to match the v4.3 thresholds; instead we have transparently documented the methodological refinement in §3.2 and let the verified results stand.

We have **declined the cross‑country turning‑point comparison** that the reviewer requested. The reasoning is one of empirical hygiene: this paper estimates only on the three Vietnam WBES waves and does not run the equivalent pipeline on any non‑Vietnamese sample, and we are unwilling to import comparison values from prior literature that was estimated under different specifications, on different vintages of WBES data, with different listwise conventions, and to different curvature tests. Citing such values would create a comparison whose components do not share a common analytic protocol, undermining the methodological discipline that the reviewer's other requirements (Antonakis et al. 2010, Heckman selection, Paternoster z‑test, triple‑source verification) explicitly demand. We have therefore reframed the institutional‑maturity discussion in §5 to apply *within* Vietnam — across the 2009/2015/2023 waves — rather than across countries. The wave‑by‑wave evolution of the Vietnamese turning point and the wave‑by‑wave Paternoster z‑tests on TCI_z and DAI_z together carry the institutional‑maturity argument without recourse to externally cited turning points. Cross‑country comparison remains a worthwhile empirical question for future work that estimates the same pipeline on multiple country samples; this paper does not undertake that work.

**Manuscript locations.** §4.2 (per‑wave LM p); §2.1 (single‑country institutional anchoring); §5.1.1 (within‑Vietnam wave evolution); §5.3 (Vietnam‑only policy implications).

---

### Requirement 5 — Paternoster (1998) z‑test for cross‑wave coefficient differences

**Reviewer's mandate.** "Sử dụng kiểm định z-test của Paternoster et al. (1998) để so sánh một cách khoa học sự thay đổi của các hệ số TCI và DAI qua các năm 2009, 2015 và 2023."

**Response.** Implemented. The Paternoster (1998) z‑test for the equality of regression coefficients, z = (β_A − β_B) / √(SE_A² + SE_B²), is applied to all pairwise wave comparisons of FSTS_c, FSTS_c², TCI_z, and DAI_z. The results are persisted to `tables/table_paternoster.csv` (12 z‑tests in total) and described in §4.6 paragraph 2 and §5.1.2.

| Coefficient | Pair | β_A | β_B | z | p |
|---|---|---|---|---|---|
| TCI_z | 2009 vs 2015 | +0.224 | +0.168 | +0.60 | .545 |
| TCI_z | 2009 vs 2023 | +0.224 | +0.090 | **+1.67** | **.095** |
| TCI_z | 2015 vs 2023 | +0.168 | +0.090 | +0.89 | .375 |
| DAI_z | 2009 vs 2015 | +0.175 | +0.008 | +2.15 | .032 |
| DAI_z | 2009 vs 2023 | +0.175 | +0.113 | +0.88 | .379 |
| DAI_z | 2015 vs 2023 | +0.008 | +0.113 | −1.36 | .173 |

The marginal TCI_z 2009‑vs‑2023 z‑test (z = +1.67, p = .095) provides scientific support for the capability‑convergence narrative in §5.1.2: the productivity association of capability declines over the 14‑year window, consistent with foreign technology becoming more readily accessible through global digital marketplaces and reducing the relative scarcity premium that high‑capability firms commanded in the early window.

**Manuscript locations.** §3.3 (introduction of the test); §4.6 (results paragraph); §5.1.2 (theoretical interpretation); `tables/table_paternoster.csv` (full panel).

---

### Requirement 6 — 2‑digit ISIC sector FE robustness + 35% turning‑point managerial advisory

**Reviewer's mandate.** "Bổ sung hiệu ứng cố định ngành (Sector Fixed Effects) ở mức chi tiết 2 chữ số ISIC ... Doanh nghiệp cần hiểu rằng vượt qua ngưỡng này [35%] mà không có sự đầu tư tương xứng vào năng lực động số sẽ dẫn đến sự sụt giảm năng suất do chi phí điều phối tăng vọt."

**Response.** Implemented. The 2‑digit ISIC FE robustness is reported in §4.6 (paragraph 4): *"Replacing the broad‑sector FE with 2‑digit ISIC FE shifts the four hypothesis‑relevant coefficients by between −91% and +156% in individual waves, but the pooled coefficients remain in the same direction with TCI_z attenuating by 31% and DAI_z by 12%. The wave‑specific volatility reflects sparse 2‑digit cells in the smaller wave samples; the pooled estimate is the relevant inferential object."*

A data‑access caveat noted in §3.2: the public release of the 2023 Vietnam WBES wave does not include the `a4b` (2‑digit ISIC) variable; the wave is shipped with `a4a` only, which carries 1‑digit ISIC granularity. The pipeline falls back to `a4a` for 2023 sector FE, so the reported "2‑digit ISIC" robustness in fact uses 2‑digit FE for 2009 and 2015 and 1‑digit FE for 2023. We document this transparently and treat it as a reason to weight the pooled estimate over wave‑specific 2‑digit panels.

The 35% turning‑point managerial advisory is developed in §5.2 and §5.3:

> "Managers should evaluate digital‑adoption decisions against the firm's existing dynamic‑capability stock and the maturity of the surrounding digital ecosystem rather than treating digital adoption as a generic productivity lever." (§5.2)

> "The turning‑point point estimates (43.6% in 2009, 36.3% in 2015, 40.6% in 2023, 31.4% pooled) have implications for the design of the export‑intensity ceiling that Vietnam's industrial policy implicitly enforces … the wide and overlapping 95% confidence intervals on these estimates argue against treating any single threshold value as a knife‑edge target." (§5.3)

**Manuscript locations.** §3.2 (data caveat); §4.6 (paragraph 4); §5.2; §5.3.

---

## Stylistic and citation conformity

**APA 7th references.** The full reference list at the end of the manuscript adopts APA 7th formatting and includes all key references the reviewer cited: Lall (1992), Verhoef et al. (2021), Brynjolfsson Rock & Syverson (2021), Lind & Mehlum (2010), Paternoster et al. (1998), Heckman (1979), and Antonakis et al. (2010). It also includes Cohen & Levinthal (1990) for the absorptive‑capacity grounding of TCI and Cuervo‑Cazurra & Genc (2008) for the Heckman exclusion‑restriction logic. Cross‑country‑comparison references (Banalieva & Dhanaraj 2019; Eckhardt et al. 2018) have been removed from the reference list because the cross‑country comparison itself is not undertaken in this paper.

**Vietnamese gloss for key concepts.** *Năng lực hấp thụ* (absorptive capacity) appears in §3.2; *tính không đồng nhất không quan sát được* (unobserved heterogeneity) appears in §6; the *chi phí điều phối biên* (marginal coordination cost) concept threads §2.1, §5.1.1, §5.1.4, and §5.3 in English‑language form anchored to Hennart (2007) and Buckley et al. (2007).

**Markdown tables.** Every numerical table in the manuscript and in this response letter is formatted as standard Markdown for transparency and pandoc round‑trippability. The replication package includes the raw CSV inputs (`tables/table_2_baseline.csv`, `tables/table_3_robustness.csv`, `tables/table_lind_mehlum.csv`, `tables/table_paternoster.csv`) so that any reviewer or third party can reproduce or audit any cell.

---

## Replication artefact

The full v4.4 replication package — analytic dataset, Python pipeline, Stata do‑file (provided unrun for third‑party verification), figure generators, regression tables, and triple‑source numerical verification log — is hosted at `manuscripts/p4-jwb-vietnam/` in the corresponding author's GitHub repository. Pull request #2 against the same repository contains the eight‑commit revision arc that produced v4.4 from v4.3, with each commit message documenting the substantive change. The triple‑source verification (statsmodels, linearmodels, pure NumPy with manual HC1) agrees to machine precision (max coefficient difference 4.06 × 10⁻¹³, max standard‑error difference 1.80 × 10⁻¹⁴) on the pooled outcome equation; the verification log is provided as `output/triple_source_verification.log`.

We thank the Editor and Reviewers again for the detailed and substantive review. We hope the v4.4 manuscript meets the standard the journal expects of revised submissions and look forward to the Editor's assessment.

Sincerely,

[Corresponding author name]

On behalf of the co‑author team.
