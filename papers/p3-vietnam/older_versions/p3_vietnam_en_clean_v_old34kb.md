# Technological Capability, Digital Adoption, and the Internationalisation–Performance Relationship: A Three-Wave Firm-Level Study of Vietnam (2009, 2015, 2023)

*Manuscript classification: research article. Word count (main text excluding abstract, references, tables, figures): approximately 6,800 words. Tables: 2 (Table 1 descriptives in supplementary appendix; Table 2 main empirical pattern in §4.4). Figures: 2 (conceptual model and predicted I–P curves).*

---

## Abstract

**Purpose** — This study revisits the internationalisation–performance relationship in an emerging market and examines how technological capability and digital adoption shape firms' productivity outcomes under conditions of institutional and digital transition. Focusing on Vietnam, the study asks whether export intensity exhibits a nonlinear association with labour productivity and whether technological capability and digital adoption condition that relationship in different ways.

**Design / methodology / approach** — The study uses three waves of World Bank Enterprise Survey microdata for Vietnam (2009, 2015 and 2023; analytic N = 989, 956 and 1,013, pooled 2,958) and estimates ordinary least squares models with HC1 robust standard errors, quadratic export-intensity terms and interaction specifications. The analysis distinguishes a Technological Capability Index (TCI_z, the within-wave standardised mean of internationally recognised quality certification and foreign-licensed technology) from a Digital Adoption Index (DAI_z, the within-wave standardised website-based indicator of basic digital presence). To preserve construct separation, no item is shared between the primary TCI and DAI specifications. Lind–Mehlum (Lind & Mehlum, 2010) curvature tests, Heckman two-step and control-function selection corrections, Paternoster (1998) cross-wave z-tests and richer measurement panels (TCI_full, DAI_rich, micro-firm exclusion, common-N) complement the baseline.

**Findings** — The internationalisation–performance relationship is robustly nonlinear: the Lind–Mehlum test rejects monotonicity in all three waves (2009 p = .006, 2015 p = .009, 2023 p = .013) and in the pooled sample (p < .001), with turning points clustered between 39 and 46 per cent of direct-export intensity. Technological capability is positively associated with productivity in all three waves and in the pooled sample (β = 0.215, 0.128, 0.123 and 0.179, all p ≤ .010), and moderates the curvature in three of four panels (M3 joint p = .040, .713, .027 and .003). Digital adoption is positive in 2009 (β = 0.175, p < .001), null in 2015 (β = −0.044, p = .377), positive in 2023 (β = 0.095, p = .038) and positive in the pooled sample (β = 0.078, p = .004); its moderation channel emerges most clearly in 2023 (FSTS_c × DAI_z = −0.912, p = .043; M8 joint p = .062, marginal). Paternoster cross-wave z-tests confirm that the DAI drop between 2009 and 2015 (z = 3.353, p < .001) and the DAI re-emergence between 2015 and 2023 (z = −2.051, p = .040) are statistically distinguishable shifts.

**Originality / value** — The study contributes to research on emerging markets by showing that the productivity returns to internationalisation depend not only on export intensity but also on how firms combine foreign-technology / standards capability with foundational website-based digital adoption under transitional institutional conditions. It also offers a cleaner measurement strategy by separating these two domains with no shared items, and shows that the wave-specific pattern of digital moderation is consistent with stage contingency, with detectable moderation concentrated in 2023.

**Keywords**: internationalisation–performance; emerging markets; digital adoption; technological capability; Vietnam; firm productivity.

**JEL classification**: F23 (multinational firms; international business); O33 (technological change: choices and consequences); D22 (firm behaviour: empirical analysis); L25 (firm performance); O53 (economy-wide country studies — Asia).

---

## Highlights

- The internationalisation–performance relationship in Vietnamese firms is robustly nonlinear: the Lind–Mehlum test rejects monotonicity in all three waves (2009 p = .006, 2015 p = .009, 2023 p = .013) and in the pooled sample (p < .001), with turning points clustered between 39 and 46 % of direct-export intensity.
- Technological capability and digital adoption are separated as non-overlapping primary measures: TCI_z is the within-wave standardised mean of quality certification and foreign-licensed technology, whereas DAI_z is the within-wave standardised website-based digital-presence indicator.
- TCI_z is positively associated with productivity in all three waves (β = 0.215, 0.128, 0.123) and pooled (β = 0.179, p < .001), and moderates the curvature in three of four panels (M3 joint p = .040, .713, .027 and .003).
- DAI_z is strongest in 2009 (β = 0.175, p < .001), null in 2015 (β = −0.044, p = .377), positive in 2023 (β = 0.095, p = .038) and pooled (β = 0.078, p = .004); the cross-wave shifts are statistically distinguishable (Paternoster z = 3.353 between 2009 and 2015; z = −2.051 between 2015 and 2023).
- DAI moderation is concentrated in 2023, where FSTS_c × DAI_z = −0.912 (p = .043) and the M8 joint test is marginal (p = .062); the pooled M8 joint test is also marginal (p = .083), driven by 2023 rather than by a stable cross-period moderation.

---

## 1. Introduction

### 1.1 Background and motivation

Vietnam offers an analytically valuable setting for revisiting the internationalisation–performance (I–P) relationship because firms expand abroad under conditions of institutional transition, uneven capability accumulation, and rapidly changing digital infrastructure. In such settings, internationalisation should not be assumed to generate a simple linear performance premium. Firms may gain access to larger markets, benefit from learning, and diversify revenue streams, but they may also face rising coordination costs, information-processing burdens, and organisational strain as their foreign involvement deepens (Wright et al., 2005; Cuervo-Cazurra & Genc, 2008; Wu et al., 2016).

A long tradition of research has argued that internationalisation can improve performance at lower and intermediate levels through scale, learning, and diversification, while also generating diminishing or negative returns at higher levels because of complexity and coordination burdens. Meta-analytic evidence strongly supports the view that nonlinearity is a central feature of this relationship rather than an empirical anomaly (Vernon, 1979; Lu & Beamish, 2004; Hennart, 2007; Coviello et al., 2017; Marano et al., 2016).

Digitalisation adds a further layer of complexity. Digital tools can reduce communication frictions, accelerate transactions, and support coordination across borders. Yet those benefits do not arise automatically: their realised value depends on whether firms possess the organisational depth, absorptive capacity, and complementary routines needed to translate digital adoption into productivity gains (Cohen & Levinthal, 1990; Vial, 2019; Verhoef et al., 2021).

Three institutional turning points shape the observation window. Vietnam acceded to the World Trade Organization in early 2007. The 2015 wave captures a transitional middle phase. The 2023 wave follows the launch of the National Digital Transformation Programme (NDTP) in 2020 and the rapid expansion of cross-border e-payment and e-commerce platforms.

### 1.2 Research gap

Three gaps motivate this study. *First*, existing work often treats digitalisation as a broadly positive resource without paying sufficient attention to temporal and contextual variation in its payoff. *Second*, the distinction between technological capability and digital adoption remains underdeveloped. Technological capability refers to deeper firm-internal stocks of learning, problem-solving, process improvement, and innovation capacity (Lall, 1992); foundational digital adoption reflects a more basic layer of digital readiness and digitally enabled interfaces (Bharadwaj et al., 2013; Verhoef et al., 2021; Hanelt et al., 2021). *Third*, pooled estimates may obscure substantial lifecycle heterogeneity.

### 1.3 Contribution

This study makes three contributions. First, it refines the I–P debate by showing that the Vietnamese evidence supports a nonlinear relationship, but that the salience and visibility of that relationship vary across time. Second, the study improves construct validity by separating technological capability from foundational digital adoption. Third, the study introduces a *lifecycle interpretation* of digital internationalisation: digital capability is neither a universally stable premium nor a uniformly ineffective resource, but an uneven and stage-dependent source of performance heterogeneity.

### 1.4 Roadmap

The remainder of the paper is organised as follows. Section 2 develops the theoretical framework and hypotheses. Section 3 describes the data, variables, and empirical strategy. Section 4 presents the results. Section 5 discusses the theoretical and managerial implications. Section 6 concludes.

---

## 2. Theory and Hypotheses

### 2.1 Internationalisation and firm performance

The relationship between internationalisation and firm performance is unlikely to be linear in a transitional economy such as Vietnam. Two opposing forces underpin the curvature. On the upside, increasing direct-export intensity creates scale economies, knowledge spillovers, and learning-by-exporting effects that lift productivity (Wagner, 2007). On the downside, coordinating production for institutionally distant markets imposes information-processing costs that grow non-linearly. In a transitional setting where ports, trade-finance institutions, digital marketplaces, and dispute-resolution mechanisms are still maturing, this threshold may bind at a lower level of export intensity than in mature economies (Hennart, 2007; Wagner, 2007; Marano et al., 2016).

The FSTS variable is bounded at zero and is heavily zero-inflated (the non-exporter share is 71.6 % in 2009, 79.3 % in 2015 and 81.2 % in 2023; pooled 77.4 %). The I–P relationship therefore comprises two analytically distinct margins: the *participation margin* (FSTS = 0 → FSTS > 0) and the *intensity margin* (variation of FSTS within the exporter subsample) (Bernard et al., 2007; Wagner, 2007).

> **H1.** The internationalisation–performance relationship in Vietnam is non-monotonic and operates through two distinct margins. (H1a) Crossing from non-exporting to exporting is positively associated with labour productivity. (H1b) Within the exporter subsample, additional direct-export intensity exhibits diminishing or non-significant marginal returns.

### 2.2 Foreign-technology and standards capability and firm performance

Following the Lall (1992) tradition, this paper uses a measurement-tight reading of technological capability: a foreign-technology and standards capability that captures a firm's exposure to externally validated technological inputs — internationally recognised quality certification and foreign-licensed technology. This is one observable facet of the broader Cohen-Levinthal (1990) absorptive-capacity construct and the dynamic-capability construct of Teece (2007).

The primary TCI_z is built from two items: internationally recognised quality certification (b8) and foreign-licensed technology (e6). A broader innovation-augmented composite (TCI_full, adding product innovation h1 and R&D activity h8) is reported in §4.5 Panel A as a boundary condition.

> **H2.** Foreign-technology / standards capability (TCI_z) is positively associated with firm performance in Vietnam.

### 2.3 Website-based digital presence and firm performance

The primary DAI_z is a website-based digital presence measure: a binary indicator of whether the firm has its own website. This is a foundational and cross-wave-comparable marker of digital adoption — it does not measure transaction-level digital integration, electronic payment infrastructure, or digital transformation in the Bharadwaj et al. (2013) / Verhoef et al. (2021) / Vial (2019) sense.

In the Verhoef et al. (2021) hierarchy, digital capability can be located on a four-tier hierarchy: Tier 1 — digital presence (websites, e-mail); Tier 2 — digital communication and basic e-commerce; Tier 3 — digital process integration; Tier 4 — dynamic digital capability. The primary DAI_z anchors at Tier 1. A Tier 3-style extension (DAI_rich) is reported in §4.5 Panel B for the 2023 wave.

> **H3.** Website-based digital presence (DAI_z) is positively associated with firm performance in Vietnam on average.

### 2.4 Stage-contingent digital value

The core theoretical claim of this study is that digital capability is *stage contingent*. In early phases of internationalisation, digital tools may create relatively direct gains by helping firms communicate faster, access markets more easily, and manage transactions more efficiently. In later phases, however, the benefits of digitalisation may become more conditional because firms face more complex coordination demands.

> **H4 (exploratory).** The performance relevance of website-based digital presence (DAI_z) in Vietnam varies across stages of internationalisation; we treat the within-wave moderation as exploratory and concentrate the test on 2023, where the post-NDTP environment plausibly enables a moderation channel.

---

## 3. Data, variables, and empirical strategy

### 3.1 Data structure

The empirical analysis uses harmonised firm-level evidence for Vietnam across three waves of the World Bank Enterprise Survey: 2009, 2015 and 2023 (World Bank, 2010, 2016, 2024). The effective estimation samples are 989 observations for 2009, 956 for 2015, and 1,013 for 2023. The pooled full model contains 2,958 observations.

### 3.2 Variables

Firm performance is measured by log labour productivity (lnLP = ln(d2 / l1), where d2 is total annual sales and l1 is permanent full-time employees). Internationalisation is measured by direct-export intensity (FSTS = d3c / 100), mean-centred within wave (FSTS_c) and squared (FSTS_c²).

The primary Technological Capability Index (TCI_z) is the within-wave standardised mean of b8 (internationally recognised quality certification) and e6 (foreign-licensed technology), each recoded from WBES 1/2 to 1/0 binary form. The primary Digital Adoption Index (DAI_z) is the within-wave standardised website-presence indicator c22b. Under this revised primary specification, no item is shared between the TCI and DAI composites.

Two enriched composites are used in the §4.5 robustness panel. **TCI_full** adds h1 (introduced new or significantly improved product) and h8 (R&D expenditure indicator) to the TCI items in 2015 and 2023. **DAI_rich**, constructed only for 2023, extends the website-presence indicator with k33 (share of sales received via electronic payment) and k38 (share of supplier payments made via electronic payment).

Controls: lnEmp = ln(l1) (firm size); FirmAge = survey year minus b5 (year established); ForeignOwned = 1 if b2b > 0 (% foreign equity). Sector fixed effects use the first digit of a4b (broad ISIC code) for 2009 and 2015 and a4a for 2023. Pooled specifications add wave fixed effects.

### 3.3 Model sequence

The empirical strategy follows a nested sequence of models, all estimated by OLS with HC1 robust standard errors. M0 establishes the controls baseline. M1 introduces FSTS_c. M2 adds FSTS_c² to test for curvature. Additional models introduce TCI_z and DAI_z separately, first in moderation specifications and then in direct-effect specifications. The full model M8 includes the nonlinear internationalisation terms, both direct capability measures, and the DAI interaction terms.

### 3.4 Replication and reproducibility

The full pipeline is implemented as a 10-step Stata blueprint distributed with the manuscript. Build steps (01–04) clean each WBES wave, harmonise the focal variable set, and append the three waves. Estimation steps (05–09) cover the M0–M8 nested sequence, the Lind–Mehlum check, manual Heckman selection probes, Paternoster (1998) cross-wave z-tests, and the §4.5 robustness panels. The export step (10) writes the manuscript-facing tables and figures.

---

## 4. Results

Three patterns are worth noting before the inferential analysis. The share of firms reporting any positive direct-export intensity declines from 28.4 % in 2009 to 20.7 % in 2015 to 18.8 % in 2023. The within-wave mean of basic digital adoption (c22b website indicator) rises from 0.425 in 2009 to 0.483 in 2015 and 0.498 in 2023. The mean of log labour productivity rises monotonically (19.41 / 20.04 / 20.55), consistent with broader Vietnamese productivity convergence.

### 4.1 Wave-specific findings

**The 2009 wave** displays a clearly nonlinear I–P relationship together with strong direct capability and digital-adoption effects. The inverted-U specification (M2) yields a positive linear term (β = 1.045, p = .015) and a negative quadratic term (β = −1.774, p = .009); Lind–Mehlum p = .006. In the dual-direct M7, both TCI_z (β = 0.215, p < .001) and DAI_z (β = 0.175, p < .001) are positive. TCI moderation is statistically distinguishable from zero (M3 joint p = .040; FSTS_c × TCI_z = −0.579, p = .087); DAI moderation is not (M4 joint p = .825).

**The 2015 wave** shows the curvature cleanly but the weakest digital channel. M2 produces FSTS_c β = 1.159 (p = .029) and FSTS_c² β = −2.115 (p = .004), Lind–Mehlum p = .009. TCI_z retains a positive direct association (β = 0.128, p = .010) but at roughly 60 per cent of the 2009 magnitude. DAI_z loses direct salience entirely (β = −0.044, p = .377). Read as a phase characterisation, 2015 looks like a wave in which the I–P curvature is unusually sharp while the digital channel compresses entirely — consistent with the productivity J-curve account (Brynjolfsson et al., 2021).

**The 2023 wave** is where the digital-moderation signal emerges most sharply. M2 again indicates a clear inverted-U (FSTS_c β = 0.962, p = .039; FSTS_c² β = −1.686, p = .008; Lind–Mehlum p = .013). In M7, both capability dimensions are positive and significant (TCI_z β = 0.123, p = .006; DAI_z β = 0.095, p = .038). When the DAI interaction terms are added in M8, the linear interaction is negative and individually significant (FSTS_c × DAI_z = −0.912, p = .043), the quadratic interaction is positive and marginal (FSTS_c² × DAI_z = 1.043, p = .099), and the joint test sits at marginal significance (M4 joint p = .102; M8 joint p = .062).

Taken together, the wave-specific results trace two patterns consistent with stage contingency. Foreign-technology / standards capability is positive across all three waves with a modestly attenuating magnitude (TCI_z = 0.215 → 0.128 → 0.123). Website-based digital presence follows a non-monotonic trajectory — strong in 2009, null in 2015, and re-emerging in 2023 — and its moderation channel materialises only in 2023. Paternoster cross-wave z-tests confirm that the 2009-to-2015 fall in DAI (z = 3.353, p < .001) and the 2015-to-2023 recovery (z = −2.051, p = .040) are statistically distinguishable.

### 4.2 Pooled findings

The pooled estimates confirm that the I–P relationship is nonlinear on average. In the pooled M2, the linear FSTS_c term is positive (β = 0.984, p < .001) and the quadratic FSTS_c² term is negative (β = −1.909, p < .001); Lind–Mehlum p < .001 with an estimated turning point at 39.7 % of direct-export intensity. The curvature persists in the full M8 (FSTS_c β = 0.845, p = .006; FSTS_c² β = −1.650, p < .001).

In the pooled M7, TCI_z is positive (β = 0.179, p < .001), and DAI_z is positive (β = 0.078, p = .004). In M8, the TCI_z coefficient is essentially unchanged (β = 0.184, p < .001), while the DAI_z direct coefficient becomes statistically indistinguishable from zero (β = 0.032, p = .537) once the interaction terms are entered.

TCI moderation is more uniformly distributed: M3 joint test is statistically distinguishable from zero in three of four panels (2009 p = .040, 2023 p = .027, pooled p = .003) and null only in 2015 (p = .713). Pooled, the linear interaction is negative (FSTS_c × TCI_z = −0.587, p = .003) and the quadratic is positive (FSTS_c² × TCI_z = 0.640, p = .031), indicating that the inverted-U flattens for high-capability firms.

### 4.3 Interpretation of the hypothesis tests

**H1** is strongly supported. The Lind–Mehlum test rejects the monotonicity null in all three waves and in the pooled sample, with implied turning points clustered between 39.3 per cent (2015) and 46.2 per cent (2009).

**H2** is supported by the positive TCI_z direct association in the pooled sample (β = 0.179, p < .001) and in all three waves, reinforced by statistically distinguishable TCI moderation in three of four panels.

**H3** is supported on average: the pooled M7 estimate of DAI_z is positive and significant (β = 0.078, p = .004), but DAI_z varies sharply across waves.

**H4** receives exploratory support concentrated in the 2023 wave. The DAI joint moderation test is null in 2009 (M4 p = .825) and 2015 (M4 p = .125), and reaches the edge of significance in 2023 (M4 p = .102; M8 p = .062). We do not treat this as a confirmed cross-wave moderation pattern; the formal pooled wave × focal interaction test (Panel I) does not detect cross-wave differences in the FSTS × DAI moderation terms.

### 4.4 Main empirical pattern: participation × intensity

The full-sample inverted-U is informative about the joint participation-and-intensity pattern, but its curvature is identified primarily through the participation margin: only ~1.0 % of pooled firms sit within ±5 percentage-points of the wave-specific turning points. When we re-fit M2 / M7 / M8 on the exporter-only sub-sample (FSTS > 0; pooled N = 669, §4.5 Panel H), the linear FSTS_c term is negative (β = −0.861, p < .001) but the quadratic term is not significant (FSTS_c² β = −0.200, p = .660). H1a (participation margin) is therefore the dominant productivity-relevant margin in this dataset.

### 4.5 Robustness (summary of nine panels)

Nine panels (A–K) plus Oster (2019) bounds test whether the central inferences depend on measurement choices, sample composition, or cross-wave alignment. Key findings: (i) **TCI_full** with h1 and h8 attenuates the direct effect — TCI_thin is retained as the primary measure; (ii) **DAI_rich** with k33 and k38 produces a similar directional moderation pattern but weaker individual significance; (iii) **micro-firm exclusion** leaves the substantive inferences intact; (iv) **Heckman / control-function** corrections detect no selection bias on the exporter sub-sample; (v) **PSM** confirms positive ATT of website ownership (0.30) and certification / foreign-tech (0.61–0.64); (vi) **IV / 2SLS** with leave-one-out industry × region peer adoption: TCI_z reinforces under IV (β = 1.64, p < .001), while DAI_z attenuates to null (β = 0.02, p = .94); (vii) **Oster (2019) δ = 1 bounds**: no coefficient changes sign or collapses to zero.

---

## 5. Discussion

### 5.1 Reinterpreting digital capability in Vietnam

Both TCI_z and DAI_z are beneficial on average, but their empirical salience changes across waves. Digitalisation is therefore not simply a constant background advantage but a *context-sensitive and stage-dependent source of performance heterogeneity*. This interpretation helps reconcile the coexistence of positive pooled effects and uneven wave-specific results.

### 5.2 Why the distinction between TCI and DAI matters

The PSM and IV evidence sharpens the distinction. TCI is robust under both matching and instrumentation: the 2SLS estimate is 1.64 (p < .001) under a strong instrument (first-stage F = 22.1), and the matching ATT for cert / foreign-tech is 0.61–0.64. By contrast, the OLS-detected DAI direct association is reproduced under PSM (matching ATT = 0.30–0.32, p < .001) but attenuates to a null under 2SLS (β = 0.02, p = .94). The two constructs identify structurally different productivity channels.

#### 5.2.1 An alternative reading: proxy obsolescence

A complementary explanation is *proxy obsolescence*: the c22b indicator measures something different in 2009, 2015 and 2023. In 2009, having a corporate website was a relatively distinguishing market interface; by 2023 it is closer to a routine marker of basic digital presence. We do not view proxy obsolescence and stage contingency as mutually exclusive.

### 5.3 The significance of the 2015 dip

The 2015 pattern is especially revealing: even when the nonlinear I–P structure becomes clearer, the direct payoff from website-based digital presence can compress to a null. Public secondary indicators support a digital-infrastructure trough in 2015 relative to 2009 and 2023 anchors: WDI records Vietnam's individuals-using-the-Internet share at ~26 % in 2009, 45 % in 2015 and over 78 % by 2023; ITU's fixed-broadband subscriptions per 100 people grew from ~3 in 2009 to 8 in 2015 and to over 20 by 2023. The NDTP was issued in 2020.

### 5.4 Managerial implications

Digitalisation should be aligned with organisational readiness and international scale. Foundational digital tools may create value, but the payoff depends on whether those tools are embedded in routines that support export coordination and performance. Managers should also avoid conflating basic digital adoption with deeper technological capability.

### 5.5 Policy implications

We frame the policy reading as tentative considerations. *First*, export-promotion instruments designed around a uniformly positive internationalisation premium will overshoot in transitional periods such as 2015. *Second*, digital-economy programmes that treat foundational adoption as a sufficient policy lever are likely to be attenuated by implementation lag. *Third*, the lifecycle reading suggests that policy evaluation windows matter.

---

## 6. Limitations and Future Research

The findings should be read against five limitations. *First*, the WBES microdata are repeated cross-sections rather than a true firm panel. *Second*, the DAI_z composite captures a foundational layer of digital adoption rather than the full depth of digitally integrated organisational capability. *Third*, the analysis is conducted on a single transitional economy. *Fourth*, the lifecycle narrative relies more on the directional consistency of wave-specific estimates and the joint moderation tests than on uniformly significant pairwise z-tests. *Fifth*, the sector fixed effects in the main models are intentionally broad to keep the cross-wave specification comparable.

---

## 7. Conclusion

This study revisits the I–P relationship in Vietnam by distinguishing technological capability from foundational digital adoption and by comparing pooled and wave-specific evidence. The findings show that the I–P relationship is nonlinear on average, that both TCI_z and DAI_z are positively associated with performance in pooled models, and that the temporal pattern behind those average effects is highly uneven. The central theoretical implication is that digital capability in a transitional economy is best understood as a *stage-contingent resource*.

---

## Conflict of interest

The authors declare no conflict of interest.

## Funding

This research received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors.

## Data availability statement

The data that support the findings of this study are from the World Bank Enterprise Surveys and are available subject to registration and compliance with the WBES Data Access Protocol. Replication materials are available from the authors upon reasonable request.

## Use of generative AI in the writing process

Generative AI tools were used during manuscript preparation to assist with language editing, structure suggestions, and the assembly of the replication package documentation. All conceptual framing, hypothesis development, empirical analysis, results interpretation, and final wording were authored by the human authors, who take full responsibility for the content of the publication.

## Acknowledgements

This study uses data from the World Bank Enterprise Surveys. We thank the Enterprise Analysis Unit of the Development Economics Global Indicators Group of the World Bank for providing access to the data. The findings, interpretations, and conclusions expressed in this article are those of the authors and do not necessarily represent the views of the World Bank Group.

---

## References

Antonakis, J., Bendahan, S., Jacquart, P., & Lalive, R. (2010). On making causal claims: A review and recommendations. *The Leadership Quarterly, 21*(6), 1086–1120.

Banalieva, E. R., & Dhanaraj, C. (2019). Internalization theory for the digital economy. *Journal of International Business Studies, 50*(8), 1372–1387.

Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business strategy: Toward a next generation of insights. *MIS Quarterly, 37*(2), 471–482.

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics, 13*(1), 333–372.

Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly, 35*(1), 128–152.

Coviello, N., Kano, L., & Liesch, P. W. (2017). Adapting the Uppsala model to a modern world: Macro-context and microfoundations. *Journal of International Business Studies, 48*(9), 1151–1164.

Cuervo-Cazurra, A., & Genc, M. (2008). Transforming disadvantages into advantages: Developing-country MNEs in the least developed countries. *Journal of International Business Studies, 39*(6), 957–979.

Hanelt, A., Bohnsack, R., Marz, D., & Antunes Marante, C. (2021). A systematic review of the literature on digital transformation: Insights and implications for strategy and organizational change. *Journal of Management Studies, 58*(5), 1159–1197.

Heckman, J. J. (1979). Sample selection bias as a specification error. *Econometrica, 47*(1), 153–161.

Helfat, C. E., & Peteraf, M. A. (2003). The dynamic resource-based view: Capability lifecycles. *Strategic Management Journal, 24*(10), 997–1010.

Hennart, J.-F. (2007). The theoretical rationale for a multinationality–performance relationship. *Management International Review, 47*(3), 423–452.

Lall, S. (1992). Technological capabilities and industrialization. *World Development, 20*(2), 165–186.

Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U-shaped relationship. *Oxford Bulletin of Economics and Statistics, 72*(1), 109–118.

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609.

Marano, V., Arregle, J.-L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization–performance relationship: A meta-analytic review. *Journal of Management, 42*(5), 1075–1110.

Nambisan, S., Wright, M., & Feldman, M. (2019). The digital transformation of innovation and entrepreneurship: Progress, challenges and key themes. *Research Policy, 48*(8), article 103773.

Oster, E. (2019). Unobservable selection and coefficient stability: Theory and evidence. *Journal of Business & Economic Statistics, 37*(2), 187–204.

Paternoster, R., Brame, R., Mazerolle, P., & Piquero, A. (1998). Using the correct statistical test for the equality of regression coefficients. *Criminology, 36*(4), 859–866.

Teece, D. J. (2007). Explicating dynamic capabilities: The nature and microfoundations of (sustainable) enterprise performance. *Strategic Management Journal, 28*(13), 1319–1350.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901.

Vial, G. (2019). Understanding digital transformation: A review and a research agenda. *Journal of Strategic Information Systems, 28*(2), 118–144.

Vernon, R. (1979). The product cycle hypothesis in a new international environment. *Oxford Bulletin of Economics and Statistics, 41*(4), 255–267.

Wagner, J. (2007). Exports and productivity: A survey of the evidence from firm-level data. *The World Economy, 30*(1), 60–82.

Wooldridge, J. M. (2010). *Econometric analysis of cross section and panel data* (2nd ed.). MIT Press.

World Bank. (2010, 2016, 2024). Vietnam Enterprise Survey 2009 / 2015 / 2023: Data file. World Bank Enterprise Surveys. https://www.enterprisesurveys.org

Wright, M., Filatotchev, I., Hoskisson, R. E., & Peng, M. W. (2005). Strategy research in emerging economies: Challenging the conventional wisdom. *Journal of Management Studies, 42*(1), 1–33.

Wu, J., Wang, C., Hong, J., Piperopoulos, P., & Zhuo, S. (2016). Internationalization and innovation performance of emerging market enterprises: The role of host-country institutional development. *Journal of World Business, 51*(2), 251–263.

*Full table content (Table 1 descriptives by wave; Table 2 directional pattern; Table 3 robustness panels A–K; Table LM Lind–Mehlum turning points) and figures are available in the original docx upload `manuscript_blinded_3.docx`.*
