## 4. Results

### 4.1 Descriptive statistics

Table 1 reports the descriptive statistics for the main analytic sample (sample_base) by wave. The 2012 wave (N = 2,610) has mean log labour productivity of 12.52 (SD 1.19) and mean export intensity of 6.9 % (SD 20.4 %), with 15.4 % of firms reporting any positive direct-export intensity. The 2024 wave (N = 1,934) shows mean log labour productivity of 13.01 (SD 1.35) — an upward level shift of approximately one-half of a log point, consistent with general productivity growth between waves — and mean export intensity of 5.2 % (SD 18.3 %), with 12.6 % of firms reporting positive direct exports. Mean firm size (lnEmp) is 4.16 in 2012 versus 3.60 in 2024, reflecting a shift in the WBES sample toward smaller establishments in the 2024 wave; mean firm age rose from 12.6 to 13.9 years, reflecting the maturation of the Chinese private-firm exporter cohort over the 12-year window. Foreign-ownership rate is approximately 6 % across both waves.

> **Table 1.** Descriptive statistics for sample_base by wave

| Variable | 2012 (N = 2,610) | 2024 (N = 1,934) |
|---|---|---|
| ln(LP) — log labour productivity | 12.52 (1.19) | 13.01 (1.35) |
| FSTS — export intensity | 0.069 (0.204) | 0.052 (0.183) |
| % firms with FSTS > 0 | 15.4 % | 12.6 % |
| lnEmp — log permanent employees | 4.16 (1.36) | 3.60 (1.57) |
| Firm age (years) | 12.6 (7.3) | 13.9 (10.8) |
| Foreign-owned (b2b ≥ 10 %) | 6.1 % | 6.5 % |
| TCI_full nonmissing (≥ 3 of 4 items) | N = 1,639 | N = 1,920 |
| DAI_core nonmissing (c22b own-website) | N = 2,610 | N = 1,934 |

Means with standard deviations in parentheses. Conditional on FSTS > 0, mean ln(LP) is 12.79 in 2012 and 13.22 in 2024.

The within-wave correlation between TCI_full and the decontaminated DAI_core is 0.27 in 2012 and 0.42 in 2024, materially lower than the inflated 0.58 / 0.51 we recorded under the earlier two-item DAI specification that shared e6 with TCI; the residual correlation reflects substantive co-variation between technological capability and Tier 1 digital presence rather than a mechanical item overlap, and is small enough to permit independent identification in joint specifications.

### 4.2 The internationalization–performance relationship: confirmed inverted‑U (H1)

Across both waves and the pooled sample, the data support an inverted U‑shaped relationship between export intensity and labour productivity, supporting H1. Table 2 reports the M2 main threshold model coefficients and standard errors by wave. The linear export‑intensity term is positive in every sample (β = +2.07, p < .001 in 2012; β = +1.50, p = .010 in 2024; β = +1.78, p < .001 pooled), and the squared export‑intensity term is negative in every sample (β = −2.09, p < .001 in 2012; β = −1.59, p = .026 in 2024; β = −1.83, p < .001 pooled). Lind–Mehlum U‑tests confirm the inverted‑U formally in the 2012 and pooled samples (both p < .001) and at conventional significance in the 2024 sample (p = .037).

> **Table 2.** M2 main threshold model (lnLP ~ FSTS + FSTS² + lnEmp + firmage + foreigndummy)

| Coefficient | 2012 (N = 2,610) | 2024 (N = 1,934) | Pooled (N = 4,544) |
|---|---|---|---|
| Intercept | +12.79 (0.090) *** | +12.38 (0.084) *** | +12.30 (0.066) *** |
| FSTS | +2.07 (0.379) *** | +1.50 (0.578) ** | +1.78 (0.320) *** |
| FSTS² | −2.09 (0.435) *** | −1.59 (0.712) ** | −1.83 (0.375) *** |
| lnEmp | −0.10 (0.023) *** | +0.12 (0.023) *** | +0.005 (0.016) |
| firmage | +0.008 (0.004) ** | +0.012 (0.003) *** | +0.012 (0.002) *** |
| foreigndummy | +0.11 (0.095) | +0.26 (0.119) ** | +0.22 (0.074) *** |
| **Turning point** | **49.4 %** | **47.2 %** | **48.8 %** |
| 95 % CI (delta-method) | [43.2, 55.6] | [34.5, 59.9] | [42.7, 54.9] |
| Lind-Mehlum U-test p | < .001 | .037 | < .001 |

Standard errors in parentheses. Pooled specification clustered on idstd. *** p < .01; ** p < .05; * p < .10.

The estimated turning point is 49.4 % of total sales in 2012 (95 % delta‑method CI [43.2 %, 55.6 %]), 47.2 % in 2024 (CI [34.5 %, 59.9 %]), and 48.8 % in the pooled sample (CI [42.7 %, 54.9 %]). Figure 2 displays the three turning‑point estimates with their 95 % confidence intervals. To put the magnitudes in everyday terms: at the wave-specific turning point, predicted ln(LP) is approximately 0.51 log points (2012) and 0.35 log points (2024) above the FSTS = 0 baseline — i.e., 67 % and 42 % productivity premia respectively at the geometric-mean control levels. By contrast, at FSTS = 1 (a hypothetical 100 % exporter), predicted ln(LP) is approximately at parity with the FSTS = 0 baseline in both waves, illustrating the bounded-optimum logic at the heart of H1.

> **Figure 2.** Optimal export‑intensity threshold (turning point of the inverted U‑shaped relationship) for Chinese private firms in 2012, 2024, and the pooled sample. Markers are point estimates from OLS‑HC1 estimation of lnLP ~ FSTS + FSTS² + lnEmp + firm_age + foreign_dummy (+ wave_2024); vertical bars are 95 % delta-method confidence intervals.

### 4.3 Temporal shift across waves: H2 not supported — unexpected stability finding

H2 predicted that the shape, slope, or location of the inverted U‑shaped relationship should differ between 2012 and 2024, motivated by the substantial structural and policy changes in the Chinese economy over the intervening decade (§2.2). To test this prediction we apply two complementary tests: the Paternoster (1998) z‑test on individual coefficients, and a joint F‑test on the full set of (FSTS × wave_2024, FSTS² × wave_2024) interactions in the pooled specification.

The Paternoster (1998) z‑tests for cross‑wave equality of the linear and squared export‑intensity coefficients **fail to reject equality** at conventional thresholds. For the linear FSTS term, the difference between waves yields z = +0.82, p = .412. For the squared FSTS² term, the difference yields z = −0.61, p = .545. The joint F‑test on the (FSTS × wave_2024, FSTS² × wave_2024) interactions in the pooled three‑way moderation specification yields F(2, 3,558) = 2.24, p = .107, also failing to reject equality at conventional thresholds (Table 3).

**H2 is therefore not supported.** Despite the directional prior outlined in §2.2 — multiple plausible mechanisms predicted shape change between 2012 and 2024 — the data show no detectable shift. Combined with the tight overlap of the turning‑point CIs in Figure 2 and the closeness of the point estimates in the threshold table, the evidence indicates that the export‑intensity threshold for Chinese private firms is *structurally stable* across the 2012 and 2024 waves. We treat this as an **unexpected stability finding**: rather than confirming the predicted evolution, the data reveal a durable structural feature of the trade‑off that has persisted through a decade of substantial environmental change. Figure 3 overlays the predicted internationalization–performance curves for the two waves, illustrating the near‑parallel shape with a level shift but no curvature change.

> **Figure 3.** Predicted log labour productivity across export intensity for Chinese private firms in 2012 and 2024, holding controls at within‑sample means. Shaded bands are 95 % confidence intervals. Vertical dotted lines mark the wave‑specific turning points (49.4 % in 2012, 47.2 % in 2024). The horizontal blue band shows a managerially defined "safe operating zone" of 30 % to 60 % export intensity within which the predicted lnLP remains close to its peak in both waves. The two curves are nearly parallel in shape but level‑shifted upward in 2024, consistent with general productivity growth between waves while the inverted‑U structure is preserved — i.e., predicted shift is rejected; observed pattern is stability.

### 4.4 Capability conditions: H4a/H4b — robust level shifts, weak curvature moderation

Technological capability is positively and substantively associated with firm performance in both waves and the pooled sample, supporting the level‑shift component of H4a. The within‑wave z‑standardised TCI coefficient is β_z = +0.260 in 2012 (SE = 0.049, p < .001), β_z = +0.426 in 2024 (SE = 0.047, p < .001), and β_z = +0.380 in the pooled sample (SE = 0.035, p < .001). Each one‑standard‑deviation increase in TCI is therefore associated with a 26–43 % change in labour productivity at the geometric‑mean baseline. The Paternoster z‑test on the cross‑wave change in TCI yields z = −2.55, p = .011, indicating a statistically detectable strengthening of the TCI–productivity association between 2012 and 2024 — consistent with the absorptive-capacity logic that capability accumulation has compounded into rising productivity dividends as Chinese exporters faced rising international-competition demands. Digital adoption (DAI_core) is also positively associated with productivity, modestly (β_z = +0.05 to +0.13, p ≤ .03), supporting the level‑shift component of H4b.

The curvature‑moderation components of H4a and H4b are tested by adding TCI×FSTS, TCI×FSTS², DAI×FSTS, and DAI×FSTS² interactions to the pooled three‑way moderation specification (Table 3). The joint F‑test on (TCI×FSTS, TCI×FSTS²) yields F(2, 3,558) = 3.26, p = .039 — marginally significant — but neither individual interaction coefficient is statistically distinguishable from zero (TCI×FSTS β = −0.41, p = .443; TCI×FSTS² β = +0.05, p = .934). Wave-by-wave moderator tests (Online Appendix C) show that no individual TCI or DAI interaction coefficient achieves p < .05 in any wave‑specific specification. We therefore interpret the curvature‑moderation components of H4a and H4b as **not robustly supported**: while the joint F‑test hints at some pooled moderation, the individual coefficient pattern and wave‑by‑wave instability suggest that TCI and DAI operate primarily as **level‑shifters** rather than as curvature moderators.

The dynamic moderation hypothesis — that capability‑conditioned curvature shifts evolve over time — is tested via the three‑way joint F‑test on (FSTS×wave_2024×TCI, FSTS²×wave_2024×TCI) and yields F(2, 3,558) = 0.27, p = .760, providing **no support** for capability‑conditioned dynamic moderation.

> **Table 3.** Three-way moderation specification: pooled estimates and joint F-tests

| Coefficient | β (SE) | p-value | Significance |
|---|---|---|---|
| FSTS | +1.379 (0.401) | .001 | *** |
| FSTS² | −1.721 (0.440) | < .001 | *** |
| wave_2024 | +0.542 (0.045) | < .001 | *** |
| FSTS × wave_2024 | +0.678 (0.876) | .439 |  |
| FSTS² × wave_2024 | −0.290 (0.975) | .766 |  |
| Tech (TCI_full) | +0.380 (0.035) | < .001 | *** |
| FSTS × Tech | −0.414 (0.539) | .443 |  |
| FSTS² × Tech | +0.051 (0.615) | .934 |  |
| FSTS × wave_2024 × Tech | −0.376 (0.898) | .675 |  |
| FSTS² × wave_2024 × Tech | +0.249 (1.076) | .817 |  |
| **Joint F-tests** |  |  |  |
| F1: (FSTS × wave_2024, FSTS² × wave_2024) = 0 | F(2, 3,558) = 2.24 | **.107** | NOT rejected |
| F2: (FSTS × Tech, FSTS² × Tech) = 0 | F(2, 3,558) = 3.26 | **.039** | marginal |
| F3: (FSTS × wave_2024 × Tech, FSTS² × wave_2024 × Tech) = 0 | F(2, 3,558) = 0.27 | **.760** | NOT rejected |

N = 3,559 (sample_full). Cluster-robust SE on idstd. Controls (lnEmp, firmage, foreigndummy) included.
F1 corresponds to H2 (cross-wave shift); F2 to H4a/H4b cross-sectional curvature moderation; F3 to capability-conditioned dynamic moderation.

> **Figure 4.** Direct level‑shift coefficients of technological capability (TCI_full) and digital adoption (DAI_core) by wave for Chinese private firms. Bars are within‑wave z‑standardised coefficients from the OLS‑HC1 specification with FSTS, FSTS², lnEmp, firm age, foreign‑ownership dummy, and (in the pooled sample) a wave dummy as covariates. Error bars are 95 % confidence intervals.

### 4.5 Working‑capital and digital supplementary analyses (H3)

Having established the stability of the inverted U‑shaped export‑intensity threshold and the consistent level‑shift role of technological capability, the analysis next examines whether firm‑level working‑capital conditions help explain variation in the steepness of the post‑threshold downturn (H3). The supplementary working‑capital tests do not yield sufficiently robust support across alternative proxy definitions and wave‑specific models. Although some coefficients move in theoretically plausible directions, the pattern is not stable enough to support a strong claim that the post‑threshold downturn has been directly identified as a working‑capital mechanism in the present data.

In Block A (Liquidity Access), the overdraft × FSTS² interaction is marginally positive in 2012 (β = +0.27, p = .050) but marginally negative in 2024 (β = −0.38, p = .081). In Block C (Financing Structure), the trade-credit×FSTS² interaction is significantly negative in 2012 (β = −0.017, p = .009) but null in 2024 (p = .660). In Block D (Access‑to‑Finance Obstacle), the obstacle×FSTS² interaction is unexpectedly large and positive in 2024 (β = +1.64, p = .001) but null in 2012 — reading this as a small‑cell anomaly rather than evidence of mechanism. The 2012‑only Block B receivables-exposure extension yields null interactions for both k1c and k2c. Across all blocks, **H3 is not supported** as a robust cross-wave mechanism, consistent with the broader pattern that no curvature-moderating force operates reliably across the 2012-2024 window.

These supplementary analyses, together with the H2 and H4 moderation results, converge on a single substantive interpretation: **the Chinese internationalization-performance trade-off is durably structural, not capability-conditioned or wave-specific**. Three predicted moderation channels (H2 wave-shift, H3 working capital, H4 capability curvature moderation) all return null or unstable evidence; only the inverted-U shape itself (H1) and the direct level-shift roles of technological capability and digital adoption emerge as robust patterns.

### 4.6 Robustness — manufacturing-only subsample

To address potential concerns that the full WBES private-firm frame mixes manufacturing with services, retail, IT, and construction, we re-estimate the M2 main threshold model on a manufacturing-only subsample. For 2012, we apply `a4a 15-38` (ISIC Rev 3.1 manufacturing including the Other Manufacturing residual), yielding N = 1,656 (sample_base). For 2024, we apply `d1a2_v4` first-two-digit ISIC Rev 4 codes 10-33, yielding N = 1,062. The manufacturing-only pooled sample is N = 2,718.

Under the manufacturing-only restriction, the M2 turning point shifts to approximately 42 % in 2012 (95 % CI [37.8, 46.8]) and 30 % in 2024 (95 % CI [15.1, 44.2]) — the latter much wider, reflecting the reduced statistical power. Both are still inside the 30–60 % bounded operating range identified in the main analysis but skewed toward the lower edge. The Paternoster z-test on the manufacturing-only subsample is directionally consistent with the main-result interpretation: cross-wave equality is not rejected (z = +1.51, p = .130 for FSTS; z = −0.96, p = .337 for FSTS²). We report this robustness check primarily for transparency: the manuscript's main analysis follows the full WBES private-firm frame because (a) restricting to manufacturing alone reduces statistical power without strengthening the causal interpretation, (b) the WBES sampling weights and identification strategy operate on the full private-firm frame to which inferences project, and (c) the qualitative picture — bounded inverted-U, durably stable across waves, capability as level-shifter — survives the restriction. Results from the manufacturing-only specification appear in Online Appendix D.

### 4.7 Sample‑size and specification robustness

The threshold result is robust to several specification variations available within the WBES data. Restricting to firms with positive export activity (FSTS > 0) replicates the inverted‑U shape with a similarly located turning point but with reduced statistical precision because the upward phase shrinks.

**Adding sector strata (`a4a`) as a fixed effect** to the pooled M2 specification changes the FSTS coefficient from +1.78 to +1.56 (a 12.8 % reduction in magnitude) and the FSTS² coefficient from −1.83 to −1.55 (a 15.2 % reduction); the inverted-U is preserved and the implied turning point remains within the 30–60 % range, but the magnitudes change non-trivially when within-sector variation is exploited. We retain the broad-sector control specification as the main result on the principle that the threshold result is identified at the population level rather than within sectors, but we flag this sensitivity for readers focused on within-sector dynamics.

**Heckman selection correction.** As reported in §3.6, the inverse Mills ratio is significant in 2012 (z = −2.44, p = .015) and not significant in 2024 (z = −0.14, p = .89). Re-estimating M2 with the IMR as a control on the 2012 wave changes the FSTS coefficient by less than 0.10 in absolute terms and preserves the inverted-U shape; Lind-Mehlum U-test still confirms the inverted-U at p < .001. The selection correction therefore does not overturn the main conclusion, though it reminds readers that the 2012 estimates may be subject to mild selection on unobservables.

**Excluding the 217 panel firms from the 2024 wave** (yielding a strictly cross-sectional pool of N = 4,358 sample_base observations) changes the pooled turning-point estimate from 48.78 % to 46.88 % — a 1.9 percentage-point shift — and leaves the Paternoster z-tests unchanged in both sign and significance. The shift is modest and remains well within the 95 % delta-method CI of the main estimate.

We do not report weighted estimation (`wmedian`) as a separate specification in this version; this is computationally feasible from the WBES weight variables but requires careful treatment of the panel-firm cluster structure that is beyond the scope of the present revision. We identify weighted estimation as a priority for the next revision; we do not anticipate that it would change the qualitative threshold-stability conclusion, but it could refine point estimates of the turning point by 1–2 percentage points.
