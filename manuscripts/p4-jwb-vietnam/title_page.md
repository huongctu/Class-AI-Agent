# Title Page — P4 (v4.4) submission to *Journal of World Business*

## Title

**Digital Adoption, Technological Capability, and the Internationalisation–Performance Relationship in Vietnam: Evidence from a Transitional Digital Economy**

## Authors

| # | Name | Affiliation | Email | ORCID |
|---|---|---|---|---|
| 1 | Do Thuy Huong | School of Economics, Can Tho University, Vietnam | huongp1323001@gstudent.ctu.edu.vn | [ORCID to be added] |
| 2 | Phan Anh Tu* | School of Economics, Can Tho University, Vietnam | patu@ctu.edu.vn | [ORCID to be added] |

\* Corresponding author. Phan Anh Tu, School of Economics, Can Tho University, Campus II, 3/2 Street, Ninh Kieu District, Can Tho City, Vietnam. Email: patu@ctu.edu.vn.

## Abstract

We re‑examine the internationalisation–performance (I‑P) relationship in a transitional digital economy by separating two constructs frequently conflated in the digital international‑business literature: a Lall‑tradition Technological Capability Index (TCI) and a Bharadwaj/Verhoef‑tradition Digital Adoption Index (DAI). Using three waves of World Bank Enterprise Survey microdata for Vietnam (2009 *N* = 734; 2015 *N* = 614; 2023 *N* = 974; pooled *N* = 2,322) and a verified OLS pipeline with HC1 robust covariance, we test (H1) an inverted‑U I‑P curvature, (H2) TCI moderation of that curvature, (H3) a DAI direct association, and (H4) DAI moderation of the I‑P curve. We confirm an inverted‑U pattern in 2015 (Lind–Mehlum *p* = .033) and pooled (.041), with a marginal pattern in 2023 (.068) and no curvature in 2009 (.128). Turning‑point point estimates span 31–44 % of export intensity with overlapping 95 % CIs. TCI is positively associated with productivity in all three waves and moderates the I‑P curvature in three of four panels (joint *F p* = .030 / .046 / .027). DAI displays a productivity J‑curve (positive 2009 and 2023; null 2015) and shows a curvature‑shifting interaction in the 2023 wave (joint *F p* = .022) with negative FSTS × DAI consistent with basic digital adoption *amplifying* coordination costs at high export intensity. A four‑item DAI_rich composite attenuates the DAI direct association below significance, suggesting measurement granularity matters. All numerical results are reproduced by three independent estimators (statsmodels, linearmodels, pure NumPy with manual HC1) agreeing to machine precision (max coefficient difference 4.06 × 10⁻¹³). The replication package — analytic dataset, Python pipeline, Stata do‑file, and figure generators — accompanies this submission.

## Keywords

internationalisation–performance; digital adoption; technological capability; transitional economy; Vietnam; inverted‑U; World Bank Enterprise Surveys

## Article type

Empirical research article

## Word count

Manuscript: 7,380 words excluding references, tables, and figures.

## Funding

The authors received no specific grant from any funding agency in the public, commercial, or not‑for‑profit sectors for the research, authorship, or publication of this article.

## Conflict of interest

The authors declare no conflicts of interest.

## Ethics statement

This study uses publicly released, de‑identified secondary data from the World Bank Enterprise Surveys; no primary data were collected from human subjects, and no ethical approval was required under the host institution's research‑ethics framework.

## Data availability statement

The analytic data are derived from the World Bank Enterprise Survey (WBES) microdata files for Vietnam (2009, 2015, 2023), which are publicly downloadable from <https://www.enterprisesurveys.org/en/data> subject to acceptance of the WBES Data Access Protocol. The Data Access Protocol prohibits redistribution of WBES microdata to third parties (including journals); accordingly, the replication package accompanying this manuscript provides the analytic code, Stata do‑file, regression tables, figures, and verification logs but does *not* redistribute the underlying `.dta` files. Researchers wishing to reproduce the results must obtain the WBES files directly from the World Bank.

## Replication package

The replication package — analytic Python pipeline, Stata do‑file mirror (provided unrun), figure generators, regression tables (CSV), Lind–Mehlum and Paternoster z‑test outputs, and the triple‑source numerical verification log — is permanently archived in the corresponding author's GitHub repository at `manuscripts/p4-jwb-vietnam/`. The eight‑commit revision arc that produced v4.4 is logged in `changelog_v4_3_to_v4_4.md` for editorial transparency.