## 3. Data and Methods

### 3.1 Data

The analytic dataset combines two waves of the World Bank Enterprise Survey for China: 2012 (full release, 2,700 firms; World Bank, 2013) and 2024 (2,189 firms; World Bank, 2025). After listwise deletion on the focal set (sales, employees, export intensity) and treatment of WBES non‑response codes -9 and -7 as missing (and the additional 2024 refusal code -8), the analytic samples are 2,619 firms in 2012, 1,940 firms in 2024, and 4,559 firm‑year observations in the pooled sample.

The analytic sample is drawn from the broader private‑firm WBES frame for China rather than a manufacturing‑only subsample; firms in services, retail, IT, and construction are included alongside manufacturing because the manuscript's identification strategy depends on the full WBES private‑firm frame in which the threshold result is estimated. We control for sectoral composition through ISIC stratum dummies (`a4a`). A robustness check restricting the sample to manufacturing firms (ISIC Rev 3.1 codes 15-38 in 2012 and ISIC Rev 4 codes 10-33 in 2024) is reported in §4.6.

**Replication note.** The analytic samples reported throughout this paper (2012, N = 2,619; 2024, N = 1,940; pooled, N = 4,559) are constructed from the full WBES private‑firm frame for each wave, with World Bank nonresponse codes (−9 and −7 in 2012; −9, −8, and −7 in 2024) recoded as missing on focal variables and listwise deletion applied across `lnLP`, `FSTS`, `FSTS²`, `lnEmp`, firm age, and the foreign‑ownership indicator. Composite indices `TCI_full` and `DAI_core` are within‑wave z‑standardised before pooling. We have verified the analytic sample sizes, turning‑point estimates (49.4 % in 2012, 47.2 % in 2024, 48.8 % pooled), Paternoster cross‑wave equality results, and the joint F-tests for cross-wave shift and capability moderation in an independent Python replication of the Stata pipeline.

The WBES microdata are publicly available from https://www.enterprisesurveys.org/en/data subject to registration with the World Bank Enterprise Analysis Unit and acceptance of the WBES Data Access Protocol. The protocol prohibits transfer of the .dta files to third parties (including journals); accordingly, the replication package accompanying this manuscript references the WBES download endpoint rather than redistributing the data. Source: World Bank Enterprise Surveys, www.enterprisesurveys.org.

### 3.2 Variables

The dependent variable is log labour productivity, lnLP = ln(d2 / l1), where d2 is total annual sales (denominated in local currency unit) and l1 is the number of permanent full‑time employees, both reported in the WBES instrument (Avenyo, Tregenna, & Kraemer‑Mbula, 2021).

The focal independent variable is direct‑export intensity (FSTS), measured as d3c / 100, with FSTS² capturing the inverted‑U curvature.

Two construct composites enter the model as both direct effects and (per H4a/H4b) as candidate moderators of curvature:

**TCI_full** is the within‑wave z‑standardised mean of four binary indicators recoded from WBES 1/2 to 1/0: foreign‑licensed technology (e6), internationally‑recognised quality certification (b8), product innovation (h1 in 2024 / CNo1 in 2012), and R&D spending (h8 in 2024 / CNo3 in 2012). Following the convention of the China replication patch, TCI_full requires at least three of four items to be non‑missing.

**DAI_core** is the within‑wave z‑standardised value of a single binary indicator, own‑website presence (c22b). An earlier two‑item DAI composite that combined c22b with e6 (foreign‑licensed technology) was retired in this revision because e6 is theoretically a Lall (1992) capability indicator rather than a digital‑presence indicator, and its inclusion in the digital index mechanically inflated the within‑wave TCI–DAI correlation. The single‑item DAI_core specification we now adopt operationalises Tier 1 digital presence cleanly across the 2012 and 2024 waves; DAI_core should be read as a minimal cross‑wave digital‑adoption proxy rather than a full dynamic digital capability index, and e6 is reserved for the TCI composite where it belongs theoretically.

**Controls** include log permanent employees (lnEmp), firm age (survey year minus b5), and a foreign‑ownership dummy (1 if b2b ≥ 10 %). The pooled specification additionally includes a wave_2024 dummy (1 if 2024, 0 if 2012) and is estimated with cluster-robust standard errors on the firm identifier `idstd` to handle the 217 panel firms that appear in both 2012 and 2024 waves.

For the supplementary working‑capital analysis (Plan B1, see §3.4), we operationalise three blocks of cross‑wave‑comparable WBES items:

- **Block A — Liquidity Access:** overdraft facility (k7, binary recoded to 1 = yes), line of credit / loan (k8 in 2012, k82 in 2024 — harmonised binary by collapsing 2024's four‑level ordinal k82 ∈ {1, 2} into 1).
- **Block C — Financing Structure:** shares of working capital financed internally (k3a), by banks (k3bc), and via trade credit from suppliers (k3f). These are continuous percentage variables that the WBES validation check confirms sum to within [95 %, 105 %] for 97 % of firms in 2012 and 94 % of firms in 2024.
- **Block D — Access‑to‑finance obstacle:** k30, a five‑point Likert scale (0 = no obstacle, 4 = severe obstacle) capturing perceived constraint to firm operations.

A 2012‑only robustness extension (Block B) uses purchases on credit (k1c) and sales on credit (k2c) percentages; these items are absent from the 2024 release and therefore cannot enter cross‑wave specifications.

**Transparency note on missing‑code handling.** WBES uses -9 for "don't know" and -7 for refusal in many items; the 2024 release additionally separates -8 for refusal from -9 for don't know. These codes are treated as missing in the present analysis, restoring methodological alignment with the WBES codebook guidance.

### 3.3 Estimation

Each specification is estimated by ordinary least squares with Huber–White (HC1) robust standard errors (MacKinnon & White, 1985); pooled specifications additionally cluster the standard errors on the firm identifier `idstd` to address the within-firm dependence introduced by the 217 panel observations. Where the inverted‑U is at issue we apply the Lind & Mehlum (2010) U‑test on the [0, 1] range of FSTS, reporting the delta‑method 95 % confidence interval for the turning point (Haans, Pieters, & He, 2016). Cross‑wave coefficient differences are evaluated via the Paternoster et al. (1998) z‑test, z = (β_A − β_B) / √(SE_A² + SE_B²), with two‑sided p‑values from the standard normal distribution; the Paternoster z-test on individual coefficients is complemented by joint F-tests on the two-coefficient (FSTS × wave_2024, FSTS² × wave_2024) blocks of the pooled three-way specification (see §3.5).

Throughout, we describe results as associations rather than effects, consistent with the inferential limits of repeated‑cross‑section data: in the absence of within‑firm panel structure we cannot identify causal effects within firms, only the cross‑sectional contemporaneous association between predictors and outcomes (Antonakis et al., 2010; Shaver, 2020).

### 3.4 Supplementary mechanism‑oriented analyses (Plan B1)

To extend the threshold analysis without altering the manuscript's core identity, supplementary models examine whether the negative segment of the export‑intensity–performance curve is conditioned by firm‑level working‑capital circumstances. Because the available WBES indicators do not provide a single direct measure of the working‑capital trap, the analysis relies on multiple firm‑level proxies organised into the three cross‑wave blocks described in §3.2 (Liquidity Access, Financing Structure, Access‑to‑Finance Obstacle). These blocks are tested at the item level (M1 specifications), at the block level via a Liquidity Access Index (M3), via a composite working‑capital stress index (M4), and finally for a 2012‑only Receivables Exposure block (purchases / sales on credit). The supplementary specifications maintain the baseline quadratic structure and introduce each working‑capital measure together with its interaction with the squared export‑intensity term; the focal parameter is the interaction between the squared export‑intensity term and the working‑capital measure, because the theoretical argument concerns the steepness of the post‑threshold downturn rather than the initial upward phase alone.

The supplementary analyses are interpreted hierarchically. Evidence from the threshold models remains primary; evidence from the working‑capital interactions is used to evaluate the paper's proposed economic interpretation; evidence from technological‑capability and digital‑adoption terms is used mainly to assess level shifts and to test the curvature-moderation components of H4a and H4b.

### 3.5 Three-way moderation specification

To test the directional shift hypothesis (H2), the cross-sectional capability moderation hypothesis (H4a/H4b curvature components), and the dynamic capability-conditioned moderation hypothesis introduced in §2.4 within a single internally consistent framework, we estimate the following pooled specification on the joint sample of firms reporting all focal variables (sample_full, N = 3,559):

```
lnLP = β₀ + β₁·FSTS + β₂·FSTS² + β₃·wave_2024
     + β₄·FSTS×wave_2024 + β₅·FSTS²×wave_2024
     + β₆·Tech + β₇·FSTS×Tech + β₈·FSTS²×Tech
     + β₉·FSTS×wave_2024×Tech + β₁₀·FSTS²×wave_2024×Tech
     + γ·Controls + ε
```

where Tech = TCI_full (within-wave z-standardised) and Controls = lnEmp + firmage + foreigndummy. Standard errors are cluster-robust on `idstd`. The three focal joint F-tests are:

- **F1: cross-wave shift (H2).** Test β₄ = β₅ = 0. A non-rejection means the shape of the inverted-U is the same in 2012 and 2024.
- **F2: cross-sectional capability moderation (H4a curvature).** Test β₇ = β₈ = 0. Non-rejection means TCI does not moderate the curvature.
- **F3: capability-conditioned dynamic moderation.** Test β₉ = β₁₀ = 0. Non-rejection means there is no Tech-conditioned shift in curvature over time.

Lind & Mehlum (2010) U-tests are applied to each wave separately to validate the inverted-U formally; delta-method 95 % confidence intervals for the wave-specific turning points are reported alongside.

### 3.6 Sample selection diagnostics and identification

The empirical strategy treats the WBES sampling design as approximately exogenous to the focal relationship after controlling for firm-level characteristics, an assumption that is standard but not innocuous. Three diagnostics support this assumption.

First, the WBES uses stratified random sampling within country at the establishment level, with strata defined by industry, region, and size (World Bank, 2013, 2025). The sampling design is independent of firm-level outcomes such as productivity or export intensity, so unconditional sample inclusion is not selected on the dependent variable. Within strata, the sampling weights vary in a known way; weighted estimation using WBES median-eligibility sampling weights (`wmedian`) is identified as a priority for the next revision (see §4.7) and is computationally feasible from the WBES weight variables.

Second, **the panel firm complication** — 217 firms in the 2024 wave were re-interviewed from 2012 — is addressed through cluster-robust standard errors on the firm identifier `idstd`. Independent of the SE adjustment, we have re-estimated the pooled specifications excluding the 217 panel firms (yielding a strictly cross-sectional pool with N = 4,358 sample_base; 186 of the 217 panel firms appear in sample_base after applying the focal-variable filter); the resulting pooled turning-point estimate shifts from 48.78 % to 46.88 % — a 1.9 percentage-point change well within the 95 % delta-method CI of the main estimate — and the Paternoster z-tests retain the same direction and significance pattern as in the main pool (see §4.7). We treat the cluster-robust adjustment as the preferred specification because it preserves statistical power, but the qualitative threshold-stability conclusion holds under both treatments.

Third, **selection into reporting focal variables**. Conditional on positive sales and positive employment (the focal set), 2,619 of 2,700 (97.0 %) firms in 2012 and 1,940 of 2,189 (88.6 %) firms in 2024 report a non-missing direct-export-intensity (`d3c`) value and pass the listwise filter on the focal control set. The slightly higher missing rate in 2024 reflects the 2024 BREADY questionnaire's separate `-8` refusal code (used by some respondents to skip sensitive financial items). We probe whether selection into the analytic sample is systematically related to firm characteristics by estimating a Heckman-style two-step model with sampling region (`a2`) as the exclusion restriction in the first-stage probit. The inverse Mills ratio coefficient in the second stage is statistically significant in 2012 (z = −2.44, p = .015) and statistically indistinguishable from zero in 2024 (z = −0.14, p = .89). The 2012 result indicates that the OLS specification on the 2012 wave may be subject to mild selection on unobservables; we therefore re-estimate M2 on the 2012 wave with the IMR included as a control in §4.7 robustness and find that the FSTS and FSTS² coefficients are within 0.10 of the OLS estimates. The qualitative inverted-U conclusion (and the threshold stability claim across waves) is preserved under this correction, but readers should weight the 2012 results with this selection caveat in mind.

These three diagnostics, combined with the WBES sampling weights and the cluster-robust SE on `idstd`, support reading the OLS estimates as well-identified associations within the survey-design assumptions, with the qualifier on 2012 selection just noted. They do not, of course, address within-firm causal identification, which the repeated-cross-section design cannot deliver.
