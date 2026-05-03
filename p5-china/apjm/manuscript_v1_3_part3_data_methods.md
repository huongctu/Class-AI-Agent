## 3. Data and Methods

### 3.1 Data

The analytic dataset combines two waves of the World Bank Enterprise Survey for China: 2012 (full release, 2,700 firms; The World Bank Group, 2013) and 2024 (2,189 firms; The World Bank Group, 2025). After listwise deletion on the focal set (sales, employees, export intensity) and treatment of WBES non‑response codes -9 and -7 as missing (and the additional 2024 refusal code -8), the analytic samples are 2,619 firms in 2012, 1,940 firms in 2024, and 4,559 firm‑year observations in the pooled sample.

The analytic sample is drawn from the broader private‑firm WBES frame for China rather than a manufacturing‑only subsample; firms in services, retail, IT, and construction are included alongside manufacturing because the manuscript's identification strategy depends on the full WBES private‑firm frame in which the threshold result is estimated. We control for sectoral composition through ISIC stratum dummies (`a4a`).

**Replication note.** The analytic samples reported throughout this paper (2012, N = 2,619; 2024, N = 1,940; pooled, N = 4,559) are constructed from the full WBES private‑firm frame for each wave, with World Bank nonresponse codes (−9 and −7 in 2012; −9, −8, and −7 in 2024) recoded as missing on focal variables and listwise deletion applied across `lnLP`, `FSTS`, `FSTS²`, `lnEmp`, firm age, and the foreign‑ownership indicator. Composite indices `TCI_full` and `DAI_core` are within‑wave z‑standardised before pooling. We have verified the analytic sample sizes, turning‑point estimates (49.4 % in 2012, 47.6 % in 2024, 48.9 % pooled), and Paternoster cross‑wave equality results in an independent Python replication of the Stata pipeline.

The WBES microdata are publicly available from https://www.enterprisesurveys.org/en/data subject to registration with the World Bank Enterprise Analysis Unit and acceptance of the WBES Data Access Protocol. The protocol prohibits transfer of the .dta files to third parties (including journals); accordingly, the replication package accompanying this manuscript references the WBES download endpoint rather than redistributing the data. Source: World Bank Enterprise Surveys, www.enterprisesurveys.org.

### 3.2 Variables

The dependent variable is log labour productivity, lnLP = ln(d2 / l1), where d2 is total annual sales (denominated in local currency unit) and l1 is the number of permanent full‑time employees, both reported in the WBES instrument (Avenyo, Tregenna & Kraemer‑Mbula, 2021).

The focal independent variable is direct‑export intensity (FSTS), measured as d3c / 100, with FSTS² capturing the inverted‑U curvature.

Two construct composites enter the model as level‑shift conditions:

**TCI_full** is the within‑wave z‑standardised mean of four binary indicators recoded from WBES 1/2 to 1/0: foreign‑licensed technology (e6), internationally‑recognised quality certification (b8), product innovation (h1 in 2024 / CNo1 in 2012), and R&D spending (h8 in 2024 / CNo3 in 2012). Following the convention of the China replication patch, TCI_full requires at least three of four items to be non‑missing.

**DAI_core** is the within‑wave z‑standardised value of a single binary indicator, own‑website presence (c22b). An earlier two‑item DAI composite that combined c22b with e6 (foreign‑licensed technology) was retired in this revision because e6 is theoretically a Lall (1992) capability indicator rather than a digital‑presence indicator, and its inclusion in the digital index mechanically inflated the within‑wave TCI–DAI correlation. The single‑item DAI_core specification we now adopt operationalises Tier 1 digital presence cleanly across the 2012 and 2024 waves; DAI_core should be read as a minimal cross‑wave digital‑adoption proxy rather than a full dynamic digital capability index, and e6 is reserved for the TCI composite where it belongs theoretically.

**Controls** include log permanent employees (lnEmp), firm age (survey year minus b5), and a foreign‑ownership dummy (1 if b2b ≥ 10 %).

For the supplementary working‑capital analysis (Plan B1, see §3.4), we operationalise three blocks of cross‑wave‑comparable WBES items:

- **Block A — Liquidity Access:** overdraft facility (k7, binary recoded to 1 = yes), line of credit / loan (k8 in 2012, k82 in 2024 — harmonised binary by collapsing 2024's four‑level ordinal k82 ∈ {1, 2} into 1).
- **Block C — Financing Structure:** shares of working capital financed internally (k3a), by banks (k3bc), and via trade credit from suppliers (k3f). These are continuous percentage variables that the WBES validation check confirms sum to within [95 %, 105 %] for 97 % of firms in 2012 and 94 % of firms in 2024.
- **Block D — Access‑to‑finance obstacle:** k30, a five‑point Likert scale (0 = no obstacle, 4 = severe obstacle) capturing perceived constraint to firm operations.

A 2012‑only robustness extension (Block B) uses purchases on credit (k1c) and sales on credit (k2c) percentages; these items are absent from the 2024 release and therefore cannot enter cross‑wave specifications.

**Transparency note on missing‑code handling.** WBES uses -9 for "don't know" and -7 for refusal in many items; the 2024 release additionally separates -8 for refusal from -9 for don't know. These codes are treated as missing in the present analysis, restoring methodological alignment with the WBES codebook guidance. Sample sizes in the present paper are therefore smaller than in some earlier replication tables that retained these codes as numeric data; coefficients differ correspondingly in magnitude across that comparison, but the principal threshold result is direction‑preserving.

### 3.3 Estimation

Each specification is estimated by ordinary least squares with Huber–White (HC1) robust standard errors (MacKinnon & White, 1985). Where the inverted‑U is at issue we apply the Lind & Mehlum (2010) U‑test on the [0, 1] range of FSTS, reporting the delta‑method 95 % confidence interval for the turning point (Haans, Pieters & He, 2016). Cross‑wave coefficient differences are evaluated via the Paternoster et al. (1998) z‑test, z = (β_A − β_B) / √(SE_A² + SE_B²), with two‑sided p‑values from the standard normal distribution.

Throughout, we describe results as associations rather than effects, consistent with the inferential limits of repeated‑cross‑section data: in the absence of within‑firm panel structure we cannot identify causal effects within firms, only the cross‑sectional contemporaneous association between predictors and outcomes (Antonakis et al., 2010; Shaver, 2020).

### 3.4 Supplementary mechanism‑oriented analyses (Plan B1)

To extend the threshold analysis without altering the manuscript's core identity, supplementary models examine whether the negative segment of the export‑intensity–performance curve is conditioned by firm‑level working‑capital circumstances. Because the available WBES indicators do not provide a single direct measure of the working‑capital trap, the analysis relies on multiple firm‑level proxies organised into the three cross‑wave blocks described in §3.2 (Liquidity Access, Financing Structure, Access‑to‑Finance Obstacle). These blocks are tested at the item level (M1 specifications), at the block level via a Liquidity Access Index (M3), via a composite working‑capital stress index (M4), and finally for a 2012‑only Receivables Exposure block (purchases / sales on credit). The supplementary specifications maintain the baseline quadratic structure and introduce each working‑capital measure together with its interaction with the squared export‑intensity term; the focal parameter is the interaction between the squared export‑intensity term and the working‑capital measure, because the theoretical argument concerns the steepness of the post‑threshold downturn rather than the initial upward phase alone.

The supplementary analyses are interpreted hierarchically. Evidence from the threshold models remains primary; evidence from the working‑capital interactions is used to evaluate the paper's proposed economic interpretation; evidence from technological‑capability and digital‑adoption terms is used mainly to assess level shifts and robustness rather than to redefine the manuscript's theoretical center.
