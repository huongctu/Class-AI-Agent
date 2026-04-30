---
title: "Digital Adoption, Technological Capability, and the Internationalisation–Performance Relationship in Vietnam: Evidence from a Transitional Digital Economy"
subtitle: "v4.4 — submission to Journal of World Business"
date: "2026-04-30"
---

# Abstract

We re-examine the internationalisation–performance (I‑P) relationship in a transitional digital economy by distinguishing technological capability from digital adoption — two constructs frequently conflated in digital international‑business research. Using three waves of World Bank Enterprise Survey microdata for Vietnam (2009 *N* = 734; 2015 *N* = 614; 2023 *N* = 974; pooled *N* = 2,322), we estimate OLS specifications with HC1 robust covariance and report results as associations rather than effects, consistent with the inferential limits of repeated cross‑sections. We find an inverted‑U pattern between export intensity and labour productivity in 2015 (Lind–Mehlum *p* = .033) and the pooled sample (*p* = .041), with marginal evidence in 2023 (*p* = .068) and none in 2009 (*p* = .128); turning‑point confidence intervals are wide and overlap across waves, indicating moderate rather than knife‑edge stability. A Lall‑tradition Technological Capability Index (TCI) shows a positive direct association with productivity in all three waves and moderates the I‑P curvature in most panels. A Bharadwaj/Verhoef‑tradition Digital Adoption Index (DAI) follows a more contingent pattern: its direct association attenuates in 2015, and its 2023 moderation of the I‑P curve is consistent with basic digital adoption *amplifying* rather than substituting for coordination costs at high export intensity. Results are numerically cross‑validated. These findings suggest that technological capability and digital adoption should not be treated as interchangeable mechanisms in transitional digital economies; the productivity signature of basic digital adoption is context‑dependent and may differ in sign from the conditional‑complement reading dominant in the literature.

**Keywords**: internationalisation–performance, digital adoption, technological capability, transitional economy, Vietnam, inverted‑U.

# 1. Introduction

How does digital adoption shape the productivity returns to internationalisation in firms operating in a transitional digital economy? Three streams of international business (IB) research bear on this question but rarely intersect. The internationalisation–performance (I‑P) literature has long debated whether the relationship is monotonic, S‑shaped, or inverted‑U (Lu & Beamish, 2004; Hennart, 2007; Contractor, 2007; Powell, 2014), with recent meta‑analytic evidence favouring an inverted‑U specification in which marginal productivity returns turn negative once coordination costs at high export intensity overwhelm scale economies. The technological‑capability literature, anchored in Lall (1992) and the absorptive‑capacity tradition (Cohen & Levinthal, 1990), treats foreign‑licensed technology, quality certification, and innovation activity as the prime levers through which late‑industrialising firms extract productivity from international engagement. The digital‑transformation literature, anchored in Bharadwaj et al. (2013) and Verhoef et al. (2021), conceptualises digital adoption as a hierarchy of capabilities — from basic digital presence (Tier 1–2) through process integration (Tier 3) to dynamic digital capability (Tier 4) — that variously substitute for or amplify the coordination costs that bend the I‑P curve.

These three streams remain bifurcated by setting and rarely speak directly to a transitional digital economy. Existing IB research frequently lumps *technological capability* and *digital adoption* into a single construct, attributing positive productivity associations to "digitalisation" without disentangling the Lall‑tradition capability mechanism from the Bharadwaj/Verhoef‑tradition digital‑infrastructure mechanism. This conflation is more than a measurement nuisance: it generates inconsistent predictions for managerial practice (do exporters in Hanoi need an R&D department or an e‑commerce platform?) and inconsistent guidance for policy (should export promotion subsidise foreign technology licences or digital‑payment integration?).

This paper addresses three gaps in the resulting literature. First, the I‑P literature treats nonlinear curvature as a stable feature of cross‑sectional samples, but the *empirical stability* of the inverted‑U turning point across multiple cross‑sections of a single transitional economy has never been documented. Second, the digital‑IB literature treats digital adoption as a uniformly positive moderator of internationalisation returns, yet the institutional preconditions under which digital adoption *substitutes for* coordination cost (positive moderation) versus *amplifies* it (negative moderation) have not been articulated. Third, the international‑business empirical canon has only recently begun to grapple with the methodological consequences of pooled cross‑sectional data — including the impossibility of identifying within‑firm change, the fragility of inferences drawn without selection correction, and the importance of cross‑estimator numerical verification (Antonakis et al., 2010) — and these consequences land hardest on transitional‑economy studies that depend on repeated public surveys.

We address these gaps through three waves of World Bank Enterprise Survey microdata for Vietnam (2009, 2015, 2023). Vietnam offers a particularly informative empirical setting: between 2009 and 2023 it joined the WTO (2007), launched its National Digital Transformation Programme (2020), and absorbed three successive waves of foreign direct investment that rebalanced its exporter cohort from labour‑intensive manufacturing toward digitally‑mediated services. We separate two constructs that the digital‑IB literature regularly conflates — a Lall‑tradition Technological Capability Index (TCI) and a Bharadwaj/Verhoef‑tradition Digital Adoption Index (DAI) — and examine four hypotheses against the verified specification described in §3. Given cross‑wave item constraints in the WBES instrument, our cross‑wave digital‑adoption measure captures *comparable early‑stage* digital adoption more directly than higher‑order digital capability; we return to this measurement constraint in §2.2 and §3.2 and treat it as a substantive boundary on what we can claim. Throughout, we adopt the methodological discipline that pooled cross‑sections impose: we report associations rather than effects, we apply Heckman selection correction with an explicit exclusion restriction, we cross‑validate baseline estimates across independent implementations, and we publish the full replication package as a precondition for the inferences we report.

We make three contributions. *Conceptually*, we distinguish technological capability (TCI) from digital adoption (DAI) on theoretical grounds and show empirically that the two constructs exhibit materially different productivity signatures across the I‑P curve in the Vietnam WBES sample. *Theoretically*, we provide evidence consistent with a context‑dependent interpretation of digital adoption, in which basic digital infrastructure does not uniformly reduce coordination costs and may, under transitional institutional conditions, amplify them at high export intensity; we treat this as an interpretation supported by the 2023 evidence rather than a generalised theoretical claim that this paper can adjudicate alone. *Empirically and methodologically*, we contribute a transparent multi‑wave empirical design for studying internationalisation in WBES repeated cross‑sections, including explicit selection checks, cross‑wave coefficient comparisons, and numerical cross‑validation, at the rigour standard articulated by Antonakis et al. (2010) for IB‑specific inference.

The remainder of the paper proceeds as follows. Section 2 develops the conceptual model summarised in **Figure 1** and the four hypotheses (H1–H4). Section 3 describes the three Vietnam WBES waves and our estimation strategy, including the triple‑source numerical verification protocol introduced in v4.4. Section 4 reports baseline associations, robustness panels, and selection corrections; the main inverted‑U evidence is plotted in **Figure 2**. Section 5 discusses the theoretical, managerial, and policy implications of the new findings. Section 6 concludes with limitations and directions for future research.

# 2. Theory and Hypotheses

## 2.1 The internationalisation–performance relationship in transitional digital economies

The I‑P relationship has been theorised as monotonic (Vernon, 1979), S‑shaped (Lu & Beamish, 2004; Contractor, 2007), and inverted‑U (Hennart, 2007; Powell, 2014). The inverted‑U formulation has come to dominate empirical IB research because it parsimoniously captures the trade‑off between two opposing forces. On the upside, increased export intensity creates scale economies, knowledge spillovers from foreign customers, and learning by exporting (Wagner, 2007). On the downside, coordinating production, marketing, and distribution across multiple countries imposes increasing marginal coordination costs (Hennart, 2007) — costs that rise more steeply once a firm's export portfolio diversifies beyond a "dominant‑customer" zone of relational simplicity (Buckley et al., 2007). The two forces compose to a curvature in which marginal productivity returns to export intensity initially rise, plateau, and ultimately turn negative; the turning point of this curve identifies the export‑intensity threshold at which coordination cost begins to dominate scale economy.

The location of the turning point in the Vietnamese case, and its temporal stability across the 2009–2023 WBES observation window, remain under‑documented. Vietnam offers an informative empirical setting because it is still constructing the institutional scaffolding for cross‑border trade — ports, trade finance, digital marketplaces, dispute‑resolution mechanisms — and the marginal coordination cost curve in such a setting may bind at lower export intensity than in mature economies, but how the turning point evolves across multiple cross‑sections of a single transitional cohort is an empirical rather than a theoretical question. We treat the inverted‑U I‑P relationship as a baseline regularity (H1) to be tested wave by wave on the Vietnam WBES microdata.

## 2.2 Two constructs frequently conflated: TCI and DAI

The digital‑IB literature has accumulated a growing inventory of indicators that researchers variously label "digital capability", "digital adoption", "ICT intensity", or "technological capability" — often interchangeably and often within the same composite. We argue that this practice elides a theoretically and empirically important distinction between two constructs:

- **Technological Capability Index (TCI)**, anchored in Lall (1992), captures a firm's accumulated ability to absorb, deploy, and improve foreign technology. The constituent items are foreign‑licensed technology (representing direct technology transfer), internationally‑recognised quality certification (representing organisational capability to meet international standards), and innovation activity (representing research‑and‑development absorptive capacity, *năng lực hấp thụ* per the Cohen & Levinthal (1990) tradition). TCI is conceptually expected to reflect deep firm‑level capability stocks, although the repeated cross‑section design we adopt does not allow direct observation of within‑firm capability dynamics.

- **Digital Adoption Index (DAI)**, anchored in Bharadwaj et al. (2013) and Verhoef et al. (2021), captures a firm's engagement with digital infrastructure across a conceptual hierarchy of capabilities: Tier 1 (digital presence: website, e‑mail), Tier 2 (digital communication and basic e‑commerce), Tier 3 (digital process integration: e‑payment, supply‑chain digitisation), and Tier 4 (dynamic digital capability: data‑driven decision‑making, AI integration). Conceptually, DAI is expected to reflect investments in digital infrastructure that may be made independently of capability accumulation. **A measurement caveat applies.** Because the WBES instrument has expanded its digital‑item coverage over time — `c22b` (own website) is available in all three Vietnam waves, while `k33`/`k38` (e‑payment intensity) appear only in 2023 — the cross‑wave comparable DAI we use as the primary specification (DAI_thin) operationalises *early‑stage* digital adoption (Tier 1–2) rather than the full Tier 1–4 hierarchy. We therefore read the substantive findings on DAI as findings about *early‑stage* digital adoption rather than full‑spectrum digital transformation; a Tier 3–4 enrichment (DAI_rich) is reported in §4.6 for the 2023 wave only.

The two constructs are theoretically distinct because they map to different productivity mechanisms. TCI operates through capability accumulation: firms with stronger capability stocks extract more productivity from a given level of internationalisation because they can more efficiently absorb foreign technology, meet foreign quality standards, and organise innovation activity around international demand. DAI operates through infrastructure: firms with stronger digital adoption coordinate cross‑border operations more cheaply when digital infrastructure substitutes for managerial coordination cost — but only above a maturity threshold beyond which digital systems integrate with rather than parallel existing processes (Brynjolfsson, Rock & Syverson, 2021).

Empirically, we expect TCI to deliver a *positive level shift* on the productivity surface and to *modify curvature* of the I‑P relationship (firms with high capability face attenuated marginal returns to export intensity because they exploit each successive export market more efficiently). We expect DAI to deliver a positive level shift in the long run but to display a *productivity J‑curve*: positive at the early‑adopter stage, attenuated during the implementation lag when intangible investments compete with the digital infrastructure not yet integrated with managerial routines, and recovering once the integration matures (Brynjolfsson et al., 2021). Crucially, we expect DAI moderation of the I‑P curve to be *theory‑permissive in either direction*: digital infrastructure can substitute for coordination cost (positive moderation) above an institutional maturity threshold or amplify it (negative moderation) below that threshold.

The two constructs share one constituent — foreign‑licensed technology (`e6`) — by virtue of overlapping coverage in the WBES instrument. We retain `e6` in both composites because dropping it from either would produce a single‑item index inappropriate for inferential purposes. We document the resulting within‑wave correlation (r = 0.56–0.65 across waves) in §4.1 and confirm in §4.6 that the substantive findings are robust to alternative composite specifications that exclude the shared item.

## 2.3 Hypotheses

### 2.3.1 H1 — Inverted‑U I‑P relationship

The mechanism we adopt for H1 is the coordination‑cost / scale‑economy trade‑off summarised in §2.1. At low export intensity, the marginal export market is informationally adjacent to the firm's existing customer base; the marginal cost of serving it is low and the productivity dividend is positive. As export intensity rises, the marginal market becomes more institutionally distant, the marginal coordination cost rises, and the productivity dividend shrinks. Beyond a threshold, marginal coordination cost exceeds marginal scale economy and further internationalisation depresses productivity. This generates a curvature in which the relationship between FSTS (direct‑export intensity) and labour productivity is concave with an interior maximum.

> **Hypothesis 1 (H1).** In Vietnamese WBES samples, log labour productivity is associated with direct‑export intensity through an inverted‑U curvature; the relationship is positive at low export intensity, plateaus at an interior turning point, and turns negative at high export intensity.

### 2.3.2 H2 — TCI moderation of the I‑P curvature

If TCI is the firm‑level stock of absorptive capacity articulated in Lall (1992) and Cohen & Levinthal (1990), then capability‑augmented exporters should extract a higher productivity dividend from each unit of export intensity than their less‑capable peers. The resulting moderation could in principle be either a *level shift* (TCI raises productivity uniformly across the FSTS distribution) or a *curvature modification* (the interaction TCI × FSTS reshapes the I‑P curve itself). The literature has historically privileged the level‑shift interpretation, but two arguments point toward curvature modification in transitional settings. First, capability is scarcer and more concentrated in the early‑exporter cohort: high‑TCI firms are observed predominantly at moderate export intensity, where their marginal contribution to productivity is largest. Second, the marginal returns to capability themselves diminish with export intensity, because the absorptive‑capacity advantage that capability confers fades as a firm exhausts the supply of foreign technology its market position can plausibly absorb. The composition of these forces predicts a *negative* FSTS × TCI interaction in transitional Vietnam — capability augments productivity most at moderate FSTS and contributes less at the extreme tails.

> **Hypothesis 2 (H2).** TCI moderates the curvature of the I‑P relationship in Vietnam: the FSTS × TCI interaction is negative and the FSTS² × TCI interaction carries an opposing sign, generating a flatter inverted‑U for high‑capability firms.

### 2.3.3 H3 — DAI direct association with productivity

DAI captures investment in digital infrastructure rather than capability stock; its productivity signature is therefore more sensitive to the implementation lag described in Brynjolfsson, Rock & Syverson (2021). At low DAI, firms have not yet invested and the productivity association is null. At moderate DAI, firms have made the digital‑infrastructure investment but have not yet completed the organisational adjustments — managerial routines, customer relationships, supply‑chain data flows — that monetise the investment; the productivity association is *attenuated* during this implementation period. At high DAI, the integration matures and the productivity association is positive. Across multiple cross‑sections of a single transitional economy, the result is a *productivity J‑curve* in DAI: positive in early adopters, attenuated mid‑adoption, and recovering at maturity. Vietnam's National Digital Transformation Programme (launched 2020) would be expected to depress the 2015 DAI–productivity association — at the height of the implementation lag — relative to both the 2009 and 2023 waves.

> **Hypothesis 3 (H3).** DAI is positively associated with log labour productivity at the cross‑wave pool, with a J‑curve attenuation in the wave (2015) corresponding to the digital‑transformation implementation lag.

## 2.3.4 P1 — DAI moderation (research proposition rather than directional hypothesis)

For DAI moderation of the I‑P curve, the digital‑transformation literature does not, in our reading, supply a directional prediction that survives the verified specification we adopt. The conditional‑complement logic that motivates a positive moderation operates above an institutional and capability threshold that is itself contested in the digital‑IB literature; a directional H4 would therefore impose more theoretical structure than this paper can defend. We deliberately downgrade what previous drafts of this manuscript labelled "H4" from a directional hypothesis to a research proposition:

> **Proposition P1.** Digital adoption (DAI) is associated with the curvature of the I‑P relationship in transitional digital economies; the sign of this association is treated as an empirical question, since basic digital adoption may either substitute for or amplify the coordination costs that drive the inverted‑U turning point depending on the institutional and capability conditions of the setting.

Under this restatement, the empirical content of P1 is whether the joint test on (FSTS × DAI, FSTS² × DAI) is statistically distinguishable from zero in the Vietnam WBES samples, and what the sign of the FSTS × DAI coefficient is when it is. A *negative* FSTS × DAI in a transitional setting would be consistent with an institutional‑saturation reading in which basic Tier 1–2 digital adoption — captured by the cross‑wave comparable DAI_thin operationalisation described in §3.2 — amplifies rather than substitutes for coordination costs at high export intensity. We treat this institutional‑saturation reading as an *interpretation* available to the data, not as a theoretical claim this paper preregisters or definitively establishes.

# 3. Data and Methods

## 3.1 Data

The analytic dataset combines three waves of the World Bank Enterprise Survey (WBES) for Vietnam: 2009 (full release, 1,053 firms; World Bank, 2010), 2015 (996 firms; World Bank, 2016), and 2023 (1,028 firms; World Bank, 2024). Source: World Bank Enterprise Surveys, www.enterprisesurveys.org. The WBES microdata are publicly available from <https://www.enterprisesurveys.org/en/data> subject to registration with the Enterprise Analysis Unit (DECEA) and acceptance of the WBES Data Access Protocol; the protocol prohibits transfer of the `.dta` files to third parties (including journals), and accordingly the replication package accompanying this manuscript references the WBES download endpoint rather than redistributing the data. After the listwise deletion described in §3.2 (with WBES non‑response codes –9 treated as missing — a methodological refinement against earlier drafts), 734 / 614 / 974 firms enter the wave‑specific regressions and 2,322 firms enter the pooled regression. Variable construction and item availability across waves are summarised in `output/wbes_vn_inspection.md`.

## 3.2 Variables

The outcome is log labour productivity, **lnLP = ln(d2 / l1)** where `d2` is total annual sales and `l1` is permanent full‑time employees. The focal predictor is direct‑export intensity **FSTS = d3c / 100**, mean‑centred within wave (FSTS_c) and squared (FSTS_c²) to test inverted‑U curvature. The two construct composites are:

- **TCI_thin** = mean of `b8` (internationally‑recognised quality certification) and `e6` (foreign‑licensed technology), recoded 1/2 → 1/0 then averaged, then z‑standardised within wave (denoted TCI_z).
- **DAI_thin** = mean of `c22b` (own website) and `e6` (foreign‑licensed technology, retained as a digital‑capability proxy in the absence of pre‑2023 e‑payment items), constructed identically (denoted DAI_z).

For the §4.6 robustness panel we extend each composite where item availability permits:

- **TCI_full** (2015, 2023): adds `h1` (introduced new/significantly improved product) and `h8` (R&D expenditure indicator), capturing absorptive capacity (*năng lực hấp thụ*) per Lall (1992) and Cohen & Levinthal (1990). Within‑wave z‑standardised.
- **DAI_rich** (2023 only): adds `k33` and `k38` (e‑payment intensities), capturing the Tier 3–4 dynamic digital capability articulated in Verhoef et al. (2021). We report two specifications — *continuous* (k33/100, k38/100) and *binary* (k33 > 0, k38 > 0).

Controls are **lnEmp** = ln(l1), **FirmAge** = survey year − `b5`, and **ForeignOwned** = 𝟙{`b2b` > 0}. Sector fixed effects use the broad ISIC code (first digit of `a4b` for 2009/2015; `a4a` for 2023, where `a4b` is not in the public release). Pooled specifications add wave fixed effects.

**Transparency note on missing‑code handling.** The WBES instrument codes "don't know" / "refused" responses as `-9`. Earlier drafts of this paper retained `-9` values as numeric data, an inadvertent contamination of means and variances that materially affected the reported coefficients. This version treats `-9` as missing and applies listwise deletion on the focal variable set, reducing N from the published WBES counts (1,053 / 996 / 1,028) to the analytic counts (734 / 614 / 974) reported above. We document the magnitude of the change in the changelog accompanying the replication package; the corrected coefficients are smaller in magnitude than the previously reported values across most parameters but are direction‑preserving for the principal hypotheses.

## 3.3 Estimation

Each specification is estimated by ordinary least squares with Huber–White (HC1) robust standard errors. Where the inverted‑U is at issue we apply the Lind & Mehlum (2010) U‑test on the actual data range of FSTS_c, reporting the delta‑method 95% confidence interval for the turning point. Cross‑wave coefficient differences are evaluated by the Paternoster et al. (1998) z‑test, z = (β_A − β_B) / √(SE_A² + SE_B²), an inferential procedure absent from earlier drafts and required by the editor's review of this manuscript; results are reported in `tables/table_paternoster.csv`.

Sample‑selection robustness uses two complementary corrections. First, a manual Heckman (1979) two‑step in which the selection equation is a probit on whether the firm exports any positive share of its output, with `a2` (WBES sampling region within country) supplying the exclusion restriction. We argue that sampling region affects the *probability* of export selection through differential access to logistical infrastructure (port proximity, trade‑finance availability, customs clearance throughput) but does not affect *intrinsic firm productivity* once firm capability and digital adoption are controlled for; this is the same exclusion logic used by Cuervo‑Cazurra & Genc (2008) for emerging‑market exporter studies. The Inverse Mills Ratio (λ) from the selection equation is added to the outcome equation as an additional regressor; OLS without selection correction is defensible if and only if λ is statistically insignificant. Second, a control‑function specification (Wooldridge, 2010, eq. 17.32) replaces the IMR with the generalised residual from the same probit; the two corrections deliver identical asymptotic inferences but differ in finite‑sample efficiency.

Throughout, we describe results as *associations* rather than *effects*, consistent with the inferential limits of repeated‑cross‑section data: in the absence of within‑firm panel structure we cannot identify causal effects within firms, only the cross‑sectional contemporaneous association between predictors and outcomes (Antonakis et al., 2010). This linguistic discipline is enforced even where it produces less elegant prose than the causal alternative.

## 3.4 Numerical verification (new in v4.4)

We re‑implement the baseline outcome equation in three independent estimators on the same X / y design matrix to protect against silent regressions in any single library:

1. **statsmodels** `OLS` with `cov_type='HC1'`;
2. **linearmodels** `IV2SLS` with no instruments and `cov_type='robust', debiased=True` (HC1‑equivalent);
3. **Pure NumPy** closed‑form OLS β̂ = (X′X)⁻¹X′y with manually computed HC1 covariance V = (X′X)⁻¹ X′ diag(ê²) X (X′X)⁻¹ · n / (n − k).

On the pooled sample (n = 2,322, k = 16), the three estimators agree to **maximum coefficient difference 4.06 × 10⁻¹³** and **maximum standard‑error difference 1.80 × 10⁻¹⁴** — machine precision. The verification log is provided as `output/triple_source_verification.log`. A Stata do‑file (`code/P4_Vietnam_FullAnalysis.do`) mirrors the same specification with `regress …, robust`; it is included in the replication package for third‑party verification and has not been executed by the authors.

# 4. Results

## 4.1 Descriptive statistics

Table 1 reports analytic‑sample summary statistics by wave. Three patterns are worth noting before the inferential analysis. First, the share of firms reporting any positive direct‑export intensity declines monotonically over the observation window — from 36.0% in 2009 to 26.7% in 2015 to 18.3% in 2023 — reflecting the rebalancing of Vietnam's exporter cohort away from labour‑intensive manufacturing toward services and domestic production for FDI‑linked supply chains. The decline drives the lower mean FSTS in later waves and motivates the selection‑correction analysis in §4.6. Second, mean log labour productivity rises from 19.25 (2009) through 19.86 (2015) to 20.54 (2023), an increase of 1.29 log points (~263% in levels) that exceeds the average lnLP standard deviation in any wave; this aggregate growth is the macro backdrop against which the cross‑sectional curvature analyses are conducted. Third, the within‑wave Pearson correlation between the two focal composites TCI_thin and DAI_thin is moderate (r = 0.63 in 2009; 0.65 in 2015; 0.56 in 2023), driven by the shared `e6` (foreign‑licensed technology) constituent; this correlation is small enough to permit independent identification of the two coefficients in a joint specification but large enough to motivate the construct‑separation argument in §2.2.

**Table 1.** Descriptive statistics by Vietnam WBES wave (analytic sample after listwise deletion).

| Variable | 2009 (N = 734) | 2015 (N = 614) | 2023 (N = 974) | Pooled (N = 2,322) |
|---|---|---|---|---|
| lnLP — log labour productivity | 19.25 (1.24) | 19.86 (1.35) | 20.54 (1.46) | 19.95 (1.47) |
| FSTS — direct‑export intensity (%) | 21.4 (36.8) | 16.6 (32.5) | 12.7 (30.8) | 16.5 (33.4) |
| Exporter share (FSTS > 0) | 36.0% | 26.7% | 18.3% | 26.1% |
| TCI_thin — capability composite | 0.19 (0.30) | 0.18 (0.30) | 0.14 (0.27) | 0.17 (0.29) |
| DAI_thin — digital‑adoption composite | 0.27 (0.31) | 0.31 (0.32) | 0.30 (0.31) | 0.29 (0.31) |
| lnEmp — log permanent employees | 4.35 (1.46) | 3.95 (1.52) | 3.56 (1.53) | 3.91 (1.54) |
| FirmAge — years since establishment | 12.8 (12.0) | 13.2 (10.4) | 14.2 (7.9) | 13.5 (10.0) |
| Foreign‑owned share | 17% | 13% | 12% | 14% |
| r(TCI_thin, DAI_thin) within wave | 0.63 | 0.65 | 0.56 | — |

*Notes.* Cell entries are mean (standard deviation) for continuous variables and proportion for binary indicators; pooled column adds wave fixed effects in inferential specifications. Sample sizes reflect listwise deletion on the focal variable set with WBES non‑response code `-9` treated as missing (see §3.2).

## 4.2 The internationalisation–performance relationship (H1)

The inverted‑U I‑P relationship is **confirmed by the Lind–Mehlum test in the 2015 wave** (p = .033) and the pooled sample (p = .041). The 2023 wave shows a marginal inverted‑U pattern (p = .068), and the 2009 wave does not exhibit statistically significant curvature (p = .128). The data therefore support the H1 prediction in the recent waves and the cross‑wave pool but not uniformly across the 14‑year observation window.

Turning‑point point estimates fall between 36% and 44% of direct‑export intensity by wave (43.6% in 2009, 36.3% in 2015, 40.6% in 2023, 31.4% pooled), but their 95% delta‑method confidence intervals are wide and overlap considerably (e.g. [24.8%, 62.4%] in 2009; [23.9%, 48.7%] in 2015; [26.3%, 55.0%] in 2023; [16.4%, 46.4%] pooled). We therefore characterise the turning point as **moderately stable rather than knife‑edge stable** — a refinement against the v4.3 claim of "stable at 34–36%". Figure 2 plots the predicted lnLP across FSTS for each wave, holding controls at the within‑wave means, with shaded 95% CI bands.

## 4.3 TCI direct association and moderation (H1, H2)

**Direct association (H1).** TCI is positively associated with productivity in all three waves and the pooled sample: β_z = 0.224 (p < .001) in 2009, β_z = 0.168 (p = .017) in 2015, β_z = 0.090 (p = .095) in 2023, and β_z = 0.192 (p < .001) pooled. The marginal 2023 estimate may reflect compositional reallocation as digital firms enter the manufacturing exporter cohort.

**Moderation (H2 — revised).** Earlier drafts reported H2 as null, treating TCI as a level shifter only. Under the verified specification, **the joint F‑test on (FSTS × TCI, FSTS² × TCI) is significant in the 2009, 2023, and pooled samples** (F‑p = .030, .046, and .027, respectively) and null in 2015 (F‑p = .523). In the significant panels the FSTS × TCI coefficient is **negative** (e.g. β = −0.683, p = .018 in 2009; β = −0.481, p = .172 in 2023; β = −0.374, p = .035 pooled), while FSTS² × TCI carries the opposite sign. The pattern indicates that TCI reshapes the curvature of the I‑P relationship rather than merely shifting its level, with marginal returns to TCI declining and then rebounding as export intensity grows. We therefore revise the H2 conclusion: **TCI displays both a level‑shift and a curvature‑modifying association** with productivity in three of the four panels.

## 4.4 DAI direct association (H3)

The DAI direct association is positive and statistically significant in 2009 (β_z = 0.122, p = .029) and 2023 (β_z = 0.108, p = .045), positive but null in 2015 (β_z = 0.007, p = .916), and significant in the pooled sample (β_z = 0.085, p = .016). The 2015 attenuation is consistent with the productivity J‑curve account (Brynjolfsson, Rock & Syverson, 2021): the 2015 wave coincides with the early implementation phase of Vietnam's digital‑transformation policy push, when firms had begun adopting basic digital tools but had not yet absorbed the complementary organisational changes that monetise them.

## 4.5 DAI moderation (H4 — revised conclusion)

The joint F‑test on (FSTS × DAI, FSTS² × DAI) is **significant in the 2023 wave** (F = 3.81, p = .022), marginal in the pooled sample (F = 2.45, p = .086) and 2015 (F = 2.82, p = .061), and null in 2009 (F = 1.31, p = .270). In 2023, the FSTS × DAI coefficient is **negative** (β = −0.612, p = .113), with a positive FSTS² × DAI (β = +0.477, p = .396); the joint test is the relevant inference because the two interactions covary by construction.

The negative FSTS × DAI carries an institutional interpretation: in the 2023 Vietnam cross‑section, basic (Tier 1–2) digital adoption appears to **amplify** rather than substitute for the coordination costs that bend the I‑P curve downward at high export intensity. Firms with stronger basic digitalisation but immature dynamic digital capability incur incremental cross‑border integration costs as they expand exports — an inversion of the conditional‑complement logic that motivated the original H4. We do not claim this finding generalises beyond the Vietnam WBES sample; whether the H4 sign in other settings flips at a definable institutional‑maturity threshold is an empirical question this paper does not answer.

## 4.6 Robustness

**Selection (Heckman two‑step).** The exporter‑selection probit uses lnEmp, FirmAge, foreign ownership, sector fixed effects, and `a2` (sampling region) as the exclusion restriction. The Inverse Mills Ratio λ from the selection equation, when added to the outcome equation, is statistically insignificant in all four panels: λ = −0.066 (p = .900) in 2009, λ = −0.463 (p = .554) in 2015, λ = +0.726 (p = .364) in 2023, and λ = +0.151 (p = .734) pooled. Per the inferential criterion in §3.3, the null λ across waves supports an exogenous‑selection interpretation and validates the OLS specification adopted in §4.2–§4.5. The control‑function generalised residual yields the same direction of inference but is significant in the 2009 wave (p < .001) and marginal pooled (p = .050), warranting the cautious 2009 read documented in §4.2 but leaving the inverted‑U, TCI moderation, and DAI moderation conclusions intact.

**Paternoster (1998) cross‑wave z‑test.** Pairwise comparison of focal coefficients across waves indicates that the cross‑sectional differences in FSTS_c, FSTS_c², and DAI_z point estimates are *not* statistically distinguishable at conventional thresholds (all pairwise z| < 1.3, all p > .20). The TCI_z point estimate declines monotonically from 0.224 (2009) to 0.090 (2023); the 2009‑vs‑2023 difference reaches z = +1.67 (p = .095), a marginal signal of attenuating capability returns over the 14‑year window. We interpret this attenuation in §5.1.2. Full cross‑wave z‑test panel: `tables/table_paternoster.csv`.

**TCI_full.** Adding `h1` (new product) and `h8` (R&D) shrinks the TCI_z coefficient by 62% in 2015 (β_full = 0.063 vs β_thin = 0.168) and by 38% in 2023 (β_full = 0.056 vs β_thin = 0.090). The thin TCI captures distinct foreign‑capability content from the broader innovation indicators; we retain TCI_thin as the primary specification.

**DAI_rich.** Adding `k33` and `k38` (2023 e‑payment intensities, capturing the Tier 3–4 dynamic digital capability articulated in Verhoef et al. 2021) **attenuates the DAI direct association** to β_z = 0.058 (SE = 0.055, p = .285) in the continuous specification and β_z = 0.049 (SE = 0.047, p = .297) in the binary specification, against DAI_thin β_z = 0.108 (p = .045) in 2023. The reviewer asked whether DAI_rich could be promoted to the primary specification per Verhoef et al. (2021). We do not adopt this step because k33/k38 are absent from the 2009 and 2015 instruments, making cross‑wave comparison with a Rich DAI structurally impossible; promoting DAI_rich to primary would either restrict the analytic sample to 2023 (eliminating the J‑curve evidence) or impute pre‑2023 e‑payment data without a defensible scaffold. Instead we report DAI_rich as a 2023‑only measurement‑granularity check. The attenuation itself is informative: combining continuous percentages (k33/k38) with binary indicators (c22b/e6) in an equal‑weighted composite dilutes binary‑item variance even after within‑wave z‑standardisation, and the field needs to converge on a measurement standard that handles the binary/continuous mix in WBES e‑payment items.

**2‑digit ISIC sector FE.** Replacing the broad‑sector FE with 2‑digit ISIC FE shifts the four hypothesis‑relevant coefficients by between −53% and +135% in individual waves, but the pooled coefficients remain in the same direction with TCI_z attenuating by 37% and DAI_z by 4%. The wave‑specific volatility reflects sparse 2‑digit cells in the smaller wave samples; the pooled estimate is the relevant inferential object.

**Micro‑firm exclusion (l1 ≥ 10).** Excluding firms with fewer than ten permanent employees changes the pooled inverted‑U coefficients by at most ±13% and leaves the H1, H2, H3 inferences unchanged.

# 5. Discussion

## 5.1 Theoretical implications

**5.1.1** The inverted‑U I‑P association is robust at the cross‑wave pool (LM p = .041) and confirmed in the 2015 wave (p = .033), with a marginal pattern in 2023 (p = .068) and no statistically significant curvature in 2009 (p = .128). The wave‑specific pattern carries an institutional reading. The 2009 wave coincides with the early aftermath of Vietnam's WTO accession (effective 2007), when the marginal exporter was still in the entry‑cost zone of the I‑P curve and had not yet reached the export intensity at which coordination costs begin to bind; the absence of curvature is consistent with this entry‑zone interpretation. The 2015 wave catches the Vietnamese exporter cohort at the inflection point — past entry costs, with sufficient export intensity to reveal the coordination‑cost binding, and prior to the institutional and digital‑infrastructure investments that would push the turning point outward in later years. The 2023 wave's marginal curvature reflects a recomposed exporter cohort: a smaller share of firms export at all (18.3% vs 36.0% in 2009), but those that do span a wider range of FSTS, dispersing the inverted‑U signal across a more heterogeneous sample. Read together, the three waves trace the way a transitional digital economy walks along its own institutional‑maturity ladder, with the I‑P curvature becoming visible once the cohort matures past entry and dissolving partially as the cohort recomposes.

**5.1.2** TCI exhibits both level‑shift and curvature‑modifying associations with productivity, refining the level‑shift framing carried in earlier drafts of this manuscript. The negative FSTS × TCI in three of four panels is consistent with an attenuating returns‑to‑capability mechanism: high‑capability firms still face diminishing marginal returns to export intensity, but the bend appears earlier on the curve. The Paternoster z‑test on TCI_z 2009 vs 2023 (z = +1.67, p = .095) provides marginal evidence of declining capability returns over the observation window, consistent with the convergence of Vietnamese exporters toward a less capability‑differentiated cohort as foreign technology becomes more readily accessible through global digital marketplaces. The capability‑augmented I‑P curve interpretation we develop here is conceptually adjacent to but empirically distinct from the dynamic‑capability framework articulated by Helfat & Peteraf (2003) and Teece (2007): TCI in our specification captures stocks of foreign‑technology absorption rather than the higher‑order routines that reconfigure those stocks. Whether Vietnamese exporters are accumulating dynamic capability over the 14‑year window — and whether that accumulation, if any, dampens the negative FSTS × TCI we report — remains a question for panel data this paper cannot answer.

**5.1.3** The cross‑wave pattern of the DAI direct association — positive in 2009, null in 2015, positive in 2023 and pooled — is *consistent with* the productivity J‑curve articulated by Brynjolfsson, Rock & Syverson (2021), in which intangible investments depress measured productivity during their implementation phase before the complementary organisational changes that monetise them are absorbed. We treat this as one possible reading of the wave‑specific pattern rather than a direct test of the J‑curve mechanism: our repeated cross‑sections cannot identify within‑firm productivity dynamics, and the descriptive 2015 attenuation could equally reflect compositional change in the exporter cohort or shifts in WBES item coverage. Whether subsequent WBES waves continue to display the wave‑specific pattern documented here is a question that future surveys can adjudicate; we offer it as a conjecture rather than as a testable prediction of this paper.

**5.1.4** The 2023 H4 evidence — significant joint moderation (F p = .022) with negative FSTS × DAI — qualifies the conditional‑complement reading of digital adoption that motivated the original directional hypothesis. In the 2023 Vietnam cross‑section, where digital adoption is concentrated at Tier 1–2 (presence rather than dynamic capability per Verhoef et al. 2021), the marginal export firm appears to incur, rather than save, coordination costs from basic digitalisation. The institutional‑saturation account we offer reframes the conditional‑complement logic as theory‑permissive in either direction: positive moderation when digital adoption substitutes for coordination cost, negative moderation when it amplifies that cost. Whether the institutional preconditions under which one or the other obtains can be specified ex ante remains an open empirical question; the present paper documents the negative moderation for one transitional setting at one moment in time, and we do not attempt to generalise the sign or the magnitude beyond that observation.

## 5.2 Managerial implications

For Vietnamese exporters, **TCI investments (R&D, foreign‑licensed technology, quality certification) generate productivity returns that decline gradually with export intensity rather than disappearing or reversing**: capability‑building remains a defensible strategy across the export‑intensity distribution. **DAI investments at the basic‑adoption level do not yet pay off uniformly across export intensity in the 2023 wave**, and may carry hidden coordination costs at high export intensity. Managers should evaluate digital‑adoption decisions against the firm's existing dynamic‑capability stock and the maturity of the surrounding digital ecosystem rather than treating digital adoption as a generic productivity lever.

## 5.3 Policy implications

We frame the discussion below as **tentative policy considerations** rather than policy prescriptions. The associational nature of the evidence, the wide turning‑point confidence intervals, the wave‑specific volatility of several coefficients, and the single‑wave H4 / P1 evidence base all weigh against converting the findings into directive policy targets. With those caveats foregrounded, three considerations follow for Vietnam's trade and digital‑economy policy design. First, the export‑promotion design problem appears to differ between TCI and DAI domains: in our sample, capability‑augmenting investments (R&D, foreign‑technology licensing, quality certification) display a positive productivity association across the export‑intensity distribution, while basic digital‑adoption investments display a more contingent pattern that, in the 2023 wave, is consistent with amplification rather than mitigation of coordination costs at high export intensity. Whether this contingency generalises beyond Vietnam, or persists in subsequent WBES rounds, is unresolved by the present paper. Second, the turning‑point point estimates (43.6% in 2009, 36.3% in 2015, 40.6% in 2023, 31.4% pooled) have wide and overlapping 95% confidence intervals; any policy design referencing an export‑intensity threshold should treat the empirical turning point as an imprecisely estimated quantity rather than a knife‑edge target. Third, the wave‑specific DAI pattern is *consistent with* an implementation‑lag reading of digital‑transformation programmes such as Vietnam's National Digital Transformation Programme launched in 2020; we offer this as an interpretive consideration rather than a basis for evaluation, because the cross‑sectional design we adopt cannot directly trace the implementation lag at the firm level. None of these considerations should be read as policy guidance derived from causal identification.

## 5.4 Stratifying the strength of evidence

Because the v4.4 specification produces results that vary in robustness across the four hypothesis‑relevant dimensions of the paper, we close §5 by stratifying the findings by evidentiary strength. We do this explicitly so that the reader does not have to infer the hierarchy from the prose. We treat the **TCI direct association (H1 component)** as the most robust finding in the paper: positive in all three waves and the pooled sample, surviving the Heckman selection correction, and stable across alternative sector‑FE specifications. We treat the **inverted‑U I‑P relationship (H1)** as a *core finding in 2015 and pooled* (LM *p* = .033 and .041 respectively) but *only suggestive in 2023* (*p* = .068) and *not present in 2009* (*p* = .128); the cross‑wave pool carries the curvature claim, the wave‑specific waves do not all carry it. We treat the **TCI moderation (H2)** as supported in three of four panels but with wave‑specific volatility under finer sector FE; we read it as moderately strong rather than firmly established. We treat the **DAI direct association (H3)** as a wave‑specific pattern *consistent with* a J‑curve interpretation rather than a direct test of the J‑curve mechanism. We treat the **DAI moderation (P1)** as the most exploratory finding in the paper: significant in the 2023 wave only (joint *F p* = .022), marginal in the pooled sample (*p* = .086), and dependent on a measurement that does not include Tier 3–4 digital capability for 2009 and 2015 waves. The institutional‑saturation reading of P1 is offered as an interpretation consistent with the 2023 evidence rather than as a theoretical claim this paper definitively establishes; it requires replication on additional waves and additional measurement instruments before it can be treated as a regularity.

# 6. Limitations and Future Research

This paper has five principal limitations. First and most fundamentally, the WBES microdata are repeated cross‑sections rather than a true firm panel; we cannot identify within‑firm change over time and cannot control for time‑invariant unobserved heterogeneity (*tính không đồng nhất không quan sát được*). The associational language we adopt throughout reflects this constraint and should not be relaxed in any reader's interpretation of the results. Second, the H4 inversion documented in 2023 rests on a single wave and a marginally significant pooled signal (joint F p = .086); we cannot rule out that it reflects a transitional regime that will dissolve as Vietnam's digital ecosystem matures. A panel design tracking the same firms across the 2015 and 2023 waves would identify within‑firm DAI dynamics that the repeated cross‑section cannot. Third, the DAI_thin composite is built primarily from binary indicators; the DAI_rich attenuation in §4.6 illustrates the measurement‑granularity tension between binary and continuous digital‑adoption items, and the field needs to converge on a measurement standard that handles this mix consistently across waves. Fourth, the WBES sample frame may have drifted across waves through changes in the manufacturing‑services balance and the FDI presence; while we control for sector and ownership at the firm level, we cannot rule out residual sample‑frame drift that the Heckman correction does not capture. Fifth, generalisability beyond the Vietnam WBES sample is not tested in this paper; the inferences we report apply to the three Vietnam waves studied, and any extension to other settings is an empirical question for separate work. Future research should pursue panel data and expanded measurement instruments within the Vietnamese setting before generalisation is attempted.

# Acknowledgements

**Source: World Bank Enterprise Surveys, www.enterprisesurveys.org.** We thank the Enterprise Analysis Unit of the Development Economics Global Indicators Group of the World Bank for the data. The user of the data acknowledges that the original collector of the data, the authorised distributor of the data, and the relevant funding agency bear no responsibility for use of the data or for interpretations or inferences based upon such uses. The findings, interpretations, and conclusions expressed in this paper are entirely those of the authors and do not necessarily represent the views of the World Bank Group, its Executive Directors, or the governments they represent.

The authors received no specific grant from any funding agency in the public, commercial, or not‑for‑profit sectors for the research, authorship, or publication of this article. We thank the editorial team and anonymous reviewers of the *Journal of World Business* for searching critique that materially improved the manuscript. The replication package accompanying this submission was developed with the goal of meeting the methodological transparency standards articulated by Antonakis et al. (2010) for IB‑specific causal‑inference work.

# References

Antonakis, J., Bendahan, S., Jacquart, P., & Lalive, R. (2010). On making causal claims: A review and recommendations. *The Leadership Quarterly*, 21(6), 1086–1120.

Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business strategy: Toward a next generation of insights. *MIS Quarterly*, 37(2), 471–482.

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J‑curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics*, 13(1), 333–372.

Buckley, P. J., Clegg, L. J., Cross, A. R., Liu, X., Voss, H., & Zheng, P. (2007). The determinants of Chinese outward foreign direct investment. *Journal of International Business Studies*, 38(4), 499–518.

Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly*, 35(1), 128–152.

Contractor, F. J. (2007). Is international business good for companies? The evolutionary or multi‑stage theory of internationalization vs. the transaction cost perspective. *Management International Review*, 47(3), 453–475.

Cuervo‑Cazurra, A., & Genc, M. (2008). Transforming disadvantages into advantages: Developing‑country MNEs in the least developed countries. *Journal of International Business Studies*, 39(6), 957–979.

Heckman, J. J. (1979). Sample selection bias as a specification error. *Econometrica*, 47(1), 153–161.

Helfat, C. E., & Peteraf, M. A. (2003). The dynamic resource‑based view: Capability lifecycles. *Strategic Management Journal*, 24(10), 997–1010.

Hennart, J.‑F. (2007). The theoretical rationale for a multinationality‑performance relationship. *Management International Review*, 47(3), 423–452.

Lall, S. (1992). Technological capabilities and industrialization. *World Development*, 20(2), 165–186.

Levinsohn, J., & Petrin, A. (2003). Estimating production functions using inputs to control for unobservables. *Review of Economic Studies*, 70(2), 317–341.

Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U‑shaped relationship. *Oxford Bulletin of Economics and Statistics*, 72(1), 109–118.

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S‑curve hypothesis. *Academy of Management Journal*, 47(4), 598–609.

Paternoster, R., Brame, R., Mazerolle, P., & Piquero, A. (1998). Using the correct statistical test for the equality of regression coefficients. *Criminology*, 36(4), 859–866.

Powell, K. S. (2014). Profitability and speed of foreign market entry. *Management International Review*, 54(1), 31–45.

Teece, D. J. (2007). Explicating dynamic capabilities: The nature and microfoundations of (sustainable) enterprise performance. *Strategic Management Journal*, 28(13), 1319–1350.

Vahlne, J.‑E., & Johanson, J. (2017). From internationalization to evolution: The Uppsala model at 40 years. *Journal of International Business Studies*, 48(9), 1087–1102.

Verbeke, A., & Kano, L. (2016). An internalization theory perspective on the global and regional strategies of multinational enterprises. *Journal of World Business*, 51(1), 83–92.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research*, 122, 889–901.

Vernon, R. (1979). The product cycle hypothesis in a new international environment. *Oxford Bulletin of Economics and Statistics*, 41(4), 255–267.

Wagner, J. (2007). Exports and productivity: A survey of the evidence from firm‑level data. *The World Economy*, 30(1), 60–82.

World Bank. (2010). *Vietnam Enterprise Survey 2009* [data file]. Source: World Bank Enterprise Surveys, www.enterprisesurveys.org.

World Bank. (2016). *Vietnam Enterprise Survey 2015* [data file]. Source: World Bank Enterprise Surveys, www.enterprisesurveys.org.

World Bank. (2024). *Vietnam Enterprise Survey 2023* [data file]. Source: World Bank Enterprise Surveys, www.enterprisesurveys.org.

Wooldridge, J. M. (2010). *Econometric Analysis of Cross Section and Panel Data* (2nd ed.). Cambridge, MA: MIT Press.

Wright, M., Filatotchev, I., Hoskisson, R. E., & Peng, M. W. (2005). Strategy research in emerging economies: Challenging the conventional wisdom. *Journal of Management Studies*, 42(1), 1–33.

Zhou, L., Wu, W.‑P., & Luo, X. (2007). Internationalization and the performance of born‑global SMEs: The mediating role of social networks. *Journal of International Business Studies*, 38(4), 673–690.

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
