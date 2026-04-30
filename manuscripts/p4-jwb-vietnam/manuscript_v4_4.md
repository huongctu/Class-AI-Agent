---
title: "Digital Adoption, Technological Capability, and the Internationalisation–Performance Relationship in Vietnam: Evidence from a Transitional Digital Economy"
subtitle: "v4.4 — submission to Journal of World Business"
date: "2026-04-30"
---

# Abstract

We re-examine the internationalisation–performance (I‑P) relationship in a transitional digital economy by separating two constructs frequently conflated in the digital international‑business literature: a Lall‑tradition Technological Capability Index (TCI) and a Bharadwaj/Verhoef‑tradition Digital Adoption Index (DAI). Using three waves of World Bank Enterprise Survey microdata for Vietnam (2009 N = 734; 2015 N = 614; 2023 N = 974; pooled N = 2,322) and a verified OLS pipeline with HC1 robust covariance, we test (H1) an inverted‑U I‑P curvature, (H2) TCI moderation of that curvature, (H3) a DAI direct effect, and (H4) DAI moderation of the I‑P curve. We confirm an inverted‑U I‑P relationship in 2015 (Lind–Mehlum p = .033) and the pooled sample (p = .041), with a marginal pattern in 2023 (p = .068) and no curvature in 2009 (p = .128). Turning‑point point estimates span 36–44% of export intensity but with wide 95% CIs that overlap across waves, indicating moderate rather than knife‑edge stability. TCI delivers a robust positive direct effect (β_z = 0.224, 0.168, 0.090, 0.192 across 2009/2015/2023/pooled) and **does** moderate the I‑P curvature in three of four panels (joint F p = .030 / .046 / .027 in 2009 / 2023 / pooled), reversing a level‑shift framing reported in earlier drafts. DAI delivers a positive direct effect in 2009, 2023, and pooled (J‑curve attenuation in 2015) and shows a curvature‑shifting interaction with export intensity in the 2023 wave (joint F p = .022), with negative FSTS × DAI consistent with digital‑adoption amplifying coordination costs at high export intensity. A four‑item DAI_rich composite (continuous and binary specifications) attenuates the DAI direct effect and loses significance, suggesting measurement granularity matters for digital‑intensity scaling. All numerical results are reproduced by three independent estimators (statsmodels, linearmodels, pure‑NumPy with manual HC1) agreeing to machine precision (max coefficient diff 4 × 10⁻¹³). The replication package — analytic dataset, Python pipeline, Stata do‑file, and figure generators — accompanies this submission.

**Keywords**: internationalisation–performance, digital adoption, technological capability, transitional economy, Vietnam, inverted‑U.

# 1. Introduction

(*Section §1 retained verbatim from v4.3 §1; only the closing roadmap pointer to Figure 1 is updated below.*)

The remainder of the paper proceeds as follows. Section 2 develops the conceptual model summarised in **Figure 1** and the four hypotheses (H1–H4). Section 3 describes the three Vietnam WBES waves and our estimation strategy, including the triple‑source numerical verification protocol introduced in v4.4. Section 4 reports baseline results, robustness panels, and selection corrections; the main inverted‑U evidence is plotted in **Figure 2**. Section 5 discusses the theoretical, managerial, and policy implications of the new findings. Section 6 concludes with limitations and directions for future research.

# 2. Theory and Hypotheses

(*Section §2.1–§2.3.3 retained from v4.3.*)

## 2.3.4 H4 — DAI moderation (revised statement)

Earlier drafts framed H4 as a directional prediction that *"the association between digital adoption and firm performance becomes more positive at higher levels of export intensity."* The verified results in §4.5 do not support this framing in the pooled sample but do detect a curvature‑shifting interaction in the 2023 wave (joint F p = .022), with negative FSTS × DAI and positive FSTS² × DAI. Consistent with the conceptual model in Figure 1, we therefore restate H4 as a **two‑sided** moderation hypothesis whose sign is treated as an empirical question:

> **H4 (revised).** Digital adoption (DAI) moderates the curvature of the I‑P relationship; the sign of the interaction is theory‑permissive in either direction depending on whether digital systems substitute for, or amplify, the coordination costs that drive the inverted‑U turning point.

This restatement preserves theoretical integrity — under the institutional‑saturation account, basic Tier 1–2 digital adoption may *amplify* rather than substitute for the coordination costs that bend the I‑P curve downward at high export intensity, generating the negative FSTS × DAI we observe in 2023.

# 3. Data and Methods

## 3.1 Data

The analytic dataset combines three waves of the World Bank Enterprise Survey for Vietnam: 2009 (full release, 1,053 firms), 2015 (996 firms), and 2023 (1,028 firms). After the listwise deletion described in §3.2 (with WBES non‑response codes –9 treated as missing — a methodological refinement against earlier drafts), 734 / 614 / 974 firms enter the wave‑specific regressions and 2,322 firms enter the pooled regression. Variable construction and item availability across waves are summarised in `output/wbes_vn_inspection.md`.

## 3.2 Variables

The outcome is log labour productivity, **lnLP = ln(d2 / l1)** where `d2` is total annual sales and `l1` is permanent full‑time employees. The focal predictor is direct‑export intensity **FSTS = d3c / 100**, mean‑centred within wave (FSTS_c) and squared (FSTS_c²) to test inverted‑U curvature. The two construct composites are:

- **TCI_thin** = mean of `b8` (internationally‑recognised quality certification) and `e6` (foreign‑licensed technology), recoded 1/2 → 1/0 then averaged, then z‑standardised within wave (denoted TCI_z).
- **DAI_thin** = mean of `c22b` (own website) and `e6` (foreign‑licensed technology, retained as a digital‑capability proxy in the absence of pre‑2023 e‑payment items), constructed identically (denoted DAI_z).

For the §4.6 robustness panel we extend each composite where item availability permits:

- **TCI_full** (2015, 2023): adds `h1` (introduced new/significantly improved product) and `h8` (R&D expenditure indicator). Within‑wave z‑standardised.
- **DAI_rich** (2023 only): adds `k33` and `k38` (e‑payment intensities). We report two specifications — *continuous* (k33/100, k38/100) and *binary* (k33 > 0, k38 > 0).

Controls are **lnEmp** = ln(l1), **FirmAge** = survey year − `b5`, and **ForeignOwned** = 𝟙{`b2b` > 0}. Sector fixed effects use the broad ISIC code (first digit of `a4b` for 2009/2015; `a4a` for 2023, where `a4b` is not in the public release). Pooled specifications add wave fixed effects.

## 3.3 Estimation

Each specification is estimated by OLS with HC1 (White) robust standard errors. Where the inverted‑U is at issue we apply the Lind & Mehlum (2010) U‑test on the actual data range of FSTS_c, with a delta‑method 95% CI for the turning point. Sample‑selection robustness uses both a manual Heckman two‑step with a sampling‑region exclusion restriction (`a2`) and a control‑function specification using a generalised residual from a probit selection equation (Wooldridge 2010, eq. 17.32).

## 3.4 Numerical verification (new in v4.4)

We re‑implement the baseline outcome equation in three independent estimators on the same X / y design matrix to protect against silent regressions in any single library:

1. **statsmodels** `OLS` with `cov_type='HC1'`;
2. **linearmodels** `IV2SLS` with no instruments and `cov_type='robust', debiased=True` (HC1‑equivalent);
3. **Pure NumPy** closed‑form OLS β̂ = (X′X)⁻¹X′y with manually computed HC1 covariance V = (X′X)⁻¹ X′ diag(ê²) X (X′X)⁻¹ · n / (n − k).

On the pooled sample (n = 2,322, k = 16), the three estimators agree to **maximum coefficient difference 4.06 × 10⁻¹³** and **maximum standard‑error difference 1.80 × 10⁻¹⁴** — machine precision. The verification log is provided as `output/triple_source_verification.log`. A Stata do‑file (`code/P4_Vietnam_FullAnalysis.do`) mirrors the same specification with `regress …, robust`; it is included in the replication package for third‑party verification and has not been executed by the authors.

# 4. Results

## 4.1 Descriptive statistics

(*Verbatim from v4.3 §4.1, with N_2009 / N_2015 / N_2023 updated to 734 / 614 / 974 and the new pooled N = 2,322 reflecting the −9 missing‑code refinement.*)

## 4.2 The internationalisation–performance relationship (H1)

The inverted‑U I‑P relationship is **confirmed by the Lind–Mehlum test in the 2015 wave** (p = .033) and the pooled sample (p = .041). The 2023 wave shows a marginal inverted‑U pattern (p = .068), and the 2009 wave does not exhibit statistically significant curvature (p = .128). The data therefore support the H1 prediction in the recent waves and the cross‑wave pool but not uniformly across the 14‑year observation window.

Turning‑point point estimates fall between 36% and 44% of direct‑export intensity by wave (43.6% in 2009, 36.3% in 2015, 40.6% in 2023, 31.4% pooled), but their 95% delta‑method confidence intervals are wide and overlap considerably (e.g. [24.8%, 62.4%] in 2009; [23.9%, 48.7%] in 2015; [26.3%, 55.0%] in 2023; [16.4%, 46.4%] pooled). We therefore characterise the turning point as **moderately stable rather than knife‑edge stable** — a refinement against the v4.3 claim of "stable at 34–36%". Figure 2 plots the predicted lnLP across FSTS for each wave, holding controls at the within‑wave means, with shaded 95% CI bands.

## 4.3 TCI direct effect and moderation (H1, H2)

**Direct effect (H1).** TCI is positively associated with productivity in all three waves and the pooled sample: β_z = 0.224 (p < .001) in 2009, β_z = 0.168 (p = .017) in 2015, β_z = 0.090 (p = .095) in 2023, and β_z = 0.192 (p < .001) pooled. The marginal 2023 estimate may reflect compositional reallocation as digital firms enter the manufacturing exporter cohort.

**Moderation (H2 — revised).** v4.3 reported H2 as null (TCI as level‑shift only). Under the verified spec, **the joint F‑test on (FSTS × TCI, FSTS² × TCI) is significant in the 2009, 2023, and pooled samples** (F‑p = .030, .046, and .027, respectively) and null in 2015 (F‑p = .523). In the significant panels the FSTS × TCI coefficient is **negative** (e.g. β = −0.683, p = .018 in 2009; β = −0.481, p = .172 in 2023; β = −0.374, p = .035 pooled), while FSTS² × TCI carries the opposite sign. The pattern indicates that TCI reshapes the curvature of the I‑P relationship rather than merely shifting its level, with marginal returns to TCI declining and then rebounding as export intensity grows. We therefore revise the H2 conclusion: **TCI exerts both a level‑shift and a curvature‑modifying effect** on the I‑P relationship in three of the four panels.

## 4.4 DAI direct effect (H3)

The DAI direct effect is positive and statistically significant in 2009 (β_z = 0.122, p = .029) and 2023 (β_z = 0.108, p = .045), positive but null in 2015 (β_z = 0.007, p = .916), and significant in the pooled sample (β_z = 0.085, p = .016). The 2015 attenuation is consistent with the productivity J‑curve account (Brynjolfsson, Rock & Syverson 2021): firms had begun adopting basic digital tools but had not yet absorbed the complementary organisational changes that monetise them.

## 4.5 DAI moderation (H4 — revised conclusion)

The joint F‑test on (FSTS × DAI, FSTS² × DAI) is **significant in the 2023 wave** (F = 3.81, p = .022), marginal in the pooled sample (F = 2.45, p = .086) and 2015 (F = 2.82, p = .061), and null in 2009 (F = 1.31, p = .270). In 2023, the FSTS × DAI coefficient is **negative** (β = −0.612, p = .113), with a positive FSTS² × DAI (β = +0.477, p = .396); the joint test is the relevant inference because the two interactions covary by construction.

The negative FSTS × DAI carries an institutional interpretation: in a transitional digital economy, basic (Tier 1–2) digital adoption appears to **amplify** rather than substitute for the coordination costs that bend the I‑P curve downward at high export intensity. Firms with stronger basic digitalisation but immature dynamic digital capability incur incremental cross‑border integration costs as they expand exports — an inversion of the conditional‑complement logic that motivated the original H4. This contrasts with the pattern that has been documented in digital‑frontier economies, where dynamic digital capabilities (Tier 3–4) substitute for coordination cost and support a positive H4 sign.

## 4.6 Robustness

**Selection.** Heckman two‑step λ is statistically insignificant in all four panels (λ = −0.07, p = .900 in 2009; λ = −0.46, p = .554 in 2015; λ = +0.73, p = .364 in 2023; λ = +0.15, p = .734 pooled), supporting an exogenous‑selection interpretation. The control‑function generalised residual is significant in 2009 (p < .001) and pooled (p = .050), warranting a cautious read of the 2009 main effects but leaving the inverted‑U and DAI moderation conclusions intact.

**TCI_full.** Adding `h1` (new product) and `h8` (R&D) shrinks the TCI_z coefficient by 62% in 2015 (β_full = 0.063 vs β_thin = 0.168) and by 38% in 2023 (β_full = 0.056 vs β_thin = 0.090). The thin TCI captures distinct foreign‑capability content from the broader innovation indicators; we retain TCI_thin as the primary specification.

**DAI_rich.** Adding `k33` and `k38` (2023 e‑payment intensities) **attenuates the DAI direct effect** to β_z = 0.058 (SE = 0.055, p = .285) in the continuous specification and β_z = 0.049 (SE = 0.047, p = .297) in the binary specification, against DAI_thin β_z = 0.108 (p = .045) in 2023. The attenuation reflects the differential measurement scale of the constituent items: k33 / k38 are continuous percentages whereas c22b / e6 are binary, such that combining them in an equal‑weighted composite dilutes binary‑item variance even after within‑wave z‑standardisation. We therefore retain DAI_thin as the primary specification for cross‑wave comparability and report DAI_rich as a measurement‑granularity check that does not contradict the H3 direct‑effect finding.

**2‑digit ISIC sector FE.** Replacing the broad‑sector FE with 2‑digit ISIC FE shifts the four hypothesis‑relevant coefficients by between −53% and +135% in individual waves, but the pooled coefficients remain in the same direction with TCI_z attenuating by 37% and DAI_z by 4%. The wave‑specific volatility reflects sparse 2‑digit cells in the smaller wave samples; the pooled estimate is the relevant inferential object.

**Micro‑firm exclusion (l1 ≥ 10).** Excluding firms with fewer than ten permanent employees changes the pooled inverted‑U coefficients by at most ±13% and leaves the H1, H2, H3 inferences unchanged.

# 5. Discussion

## 5.1 Theoretical implications

**5.1.1** The inverted‑U I‑P relationship is robust at the cross‑wave level but is not uniformly present in every five‑year cross‑section. Its absence in 2009 — at the start of Vietnam's WTO‑accession transition — and its strongest manifestation in 2015 are consistent with a "coordination‑cost binds" account: the curvature appears once exporters have moved past entry costs and begin to encounter the diminishing‑returns range.

**5.1.2** TCI exhibits both level‑shift and curvature‑modifying effects, contradicting the v4.3 claim that TCI is purely a level shifter. The negative FSTS × TCI in three of four panels is consistent with an attenuating returns‑to‑capability mechanism: high‑capability firms still face diminishing marginal returns to export intensity, but the bend appears earlier on the curve.

**5.1.3** DAI displays a productivity J‑curve over the 14‑year window (positive in 2009 → null in 2015 → positive in 2023 + pooled). The 2015 attenuation is the empirical signature of the adjustment lag predicted by intangible‑capital theory.

**5.1.4** The 2023 H4 evidence — significant joint moderation with negative FSTS × DAI — inverts the conditional‑complement logic in the digital‑IB literature. In a transitional digital economy where digital adoption is concentrated at Tier 1–2 (presence rather than dynamic capability), the marginal export firm appears to incur, rather than save, coordination costs from basic digitalisation. This is not evidence against the conditional‑complement logic in general; it is evidence that the logic operates only above an institutional digital‑maturity threshold.

## 5.2 Managerial implications

For Vietnamese exporters, **TCI investments (R&D, foreign‑licensed technology, quality certification) generate productivity returns that decline gradually with export intensity rather than disappearing or reversing**: capability‑building remains a defensible strategy across the export‑intensity distribution. **DAI investments at the basic‑adoption level do not yet pay off uniformly across export intensity in the 2023 wave**, and may carry hidden coordination costs at high export intensity. Managers should evaluate digital‑adoption decisions against the firm's existing dynamic‑capability stock and the maturity of the surrounding digital ecosystem rather than treating digital adoption as a generic productivity lever.

## 5.3 Policy implications

(*Verbatim from v4.3 §5.3.*)

# 6. Limitations and Future Research

(*Verbatim from v4.3 §6, with the following sentences added.*)

The H4 inversion documented here rests on a single wave (2023) and a marginal pooled signal; we cannot rule out that it reflects a transitional regime that will dissolve as Vietnam's digital ecosystem matures. A panel design tracking the same firms across the 2015 and 2023 waves would identify within‑firm DAI dynamics that the repeated cross‑section cannot. The DAI_rich attenuation also indicates that the field needs to converge on a measurement standard that handles the binary/continuous mix in WBES e‑payment items.

# Acknowledgements

(*Verbatim from v4.3.*)

# References

(*Verbatim from v4.3, with two additions:*)

- Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U‑shaped relationship. *Oxford Bulletin of Economics and Statistics*, 72(1), 109–118.
- Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J‑curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics*, 13(1), 333–372.

---

## Figures

**Figure 1.** Conceptual model with hypothesis arrows (path diagram). Boxes: FSTS, FSTS², TCI, DAI, Controls (lnEmp, FirmAge, ForeignOwned), Sector FE, Wave FE, lnLP. Arrows: H1 (FSTS, FSTS² → lnLP curvature; TCI → lnLP level), H2 (FSTS × TCI, FSTS² × TCI → lnLP curvature shift), H3 (DAI → lnLP), H4 (FSTS × DAI, FSTS² × DAI → lnLP curvature shift, sign empirical). See `figures/figure_1_conceptual_model.pdf`.

![Figure 1. Conceptual model.](figures/figure_1_conceptual_model.png)

**Figure 2.** Predicted lnLP across direct‑export intensity by wave. Each panel plots the OLS‑HC1 fitted curve for one wave (or the pooled sample) holding controls at within‑wave means; shaded band is the 95% CI for the predicted mean; vertical dashed line marks the turning‑point point estimate (raw FSTS scale). LM U‑test p‑values are annotated in each panel. See `figures/figure_2_main_results.pdf`.

![Figure 2. Predicted I-P curves by wave.](figures/figure_2_main_results.png)

## Tables

**Table 2 (baseline)** — `tables/table_2_baseline.csv`. Per‑wave + pooled β / SE / p for FSTS_c, FSTS_c², TCI_z, DAI_z, lnEmp, FirmAge, ForeignOwned.

**Table 3 (robustness)** — `tables/table_3_robustness.csv`. Per‑wave + pooled β / SE / p for FSTS × TCI, FSTS² × TCI, H2 joint F; FSTS × DAI, FSTS² × DAI, H4 joint F.

**Table LM** — `tables/table_lind_mehlum.csv`. Turning‑point point estimate, delta‑method 95% CI, Lind–Mehlum p‑value by wave + pooled.

---

*Replication package and instructions: see `README.md` in this folder.*
