# Declarations — APJM Submission

> *Some journals accept declarations embedded in the cover letter; others require a separate declarations document. Upload as a separate file in the APJM portal if the slot exists, or paste into the cover letter if not.*

## 1. Conflict of interest

The authors declare no conflicts of interest, financial or otherwise, that could be perceived to influence the conduct, analysis, or reporting of the research presented in this manuscript. No author has any current or pending consulting, advisory, equity, employment, board-membership, or other commercial relationship with any party that has a direct stake in the empirical setting (Chinese private firms, the World Bank Enterprise Surveys programme, or the financial-institution actors discussed in the working-capital interpretation).

## 2. Funding

The authors received no specific grant from any funding agency in the public, commercial, or not-for-profit sectors for the research, authorship, or publication of this article. The research was conducted as part of the authors' standard academic activities.

> *If a specific institutional grant or fellowship has supported any portion of the work — even modestly — replace the above paragraph with: "This work was supported by [agency name] under grant [grant ID]." Always disclose any funding even if the funder had no role in study design / analysis / decision-to-publish. APJM will reject manuscripts later found to have undisclosed funding.*

## 3. Authorship contributions (CRediT taxonomy)

> *The detailed per-author contribution list is in `01_title_page.md` §"Author contributions (CRediT taxonomy)". Reproduce verbatim here once filled.*

All listed authors meet the four ICMJE criteria for authorship: (1) substantial contributions to the conception or design of the work, or to the acquisition, analysis, or interpretation of data; (2) drafting the work or reviewing it critically for important intellectual content; (3) final approval of the version to be published; and (4) agreement to be accountable for all aspects of the work.

## 4. Data availability

The World Bank Enterprise Survey microdata used in this study are publicly available from https://www.enterprisesurveys.org/en/data subject to registration with the World Bank Enterprise Analysis Unit and acceptance of the WBES Data Access Protocol. Specific files used:

- **China 2012 wave:** WBES China 2012 full release (2,700 private firms; analytic sample 2,619 after listwise deletion on focal variables and treatment of WBES non-response codes -9 / -7 as missing).
- **China 2024 wave:** WBES China 2024 release (2,189 firms, including 217 panel observations re-interviewed from 2012; analytic sample 1,940 after listwise deletion on focal variables and treatment of WBES non-response codes -9 / -8 / -7 as missing).

The WBES Data Access Protocol prohibits redistribution of the .dta files to third parties; we therefore reference the public WBES download endpoint rather than redistributing the source data. The replication code (Stata do-files for sample construction; Python scripts for verification of M0–M8 coefficients, three-way moderation, Paternoster z-tests, and figure rendering) and all auxiliary materials (audit tables, citation-verification documents, claims-audit documents, build script for the manuscript docx) are available from the corresponding author on reasonable request, and we will deposit them in a public repository (DOI-issued via Zenodo or similar) upon manuscript acceptance.

## 5. Ethics approval and consent to participate

The study uses publicly available, de-identified establishment-level microdata distributed by the World Bank Enterprise Surveys programme under the WBES Data Access Protocol. The WBES instrument collects firm-level information (sales, employees, export intensity, technology adoption, financing structure, etc.) from the establishment's senior management; no personally identifying information about individual respondents is released to data users. Because no primary data collection from human subjects was conducted by the authors, institutional ethics review was not required. The authors obtained data access in compliance with WBES protocol terms and have acknowledged the data source as required.

## 6. Consent for publication

Not applicable. The manuscript does not contain any individual-level information from identifiable persons (no case studies, qualitative interview material, or person-level images).

## 7. Permission to reproduce material

No third-party copyrighted material is reproduced in the manuscript. All figures and tables are original outputs constructed by the authors from WBES microdata using Graphviz (Figure 1 conceptual model) and matplotlib (Figures 2–4 analytical plots).

## 8. AI assistance disclosure

In line with COPE and APJM transparency expectations regarding AI assistance in scholarly writing, the authors disclose the following:

- **AI tooling used.** A large-language-model assistant (Anthropic Claude, accessed via authorised software harness) was used during manuscript preparation as a structured drafting and revision aid: helping organise prose, surfacing potential reference candidates, drafting initial table layouts, and assisting with the construction of replication code (Stata do-files and Python verification scripts).
- **Verification protocol.** The authors retained full intellectual responsibility for the conceptualisation, empirical design, results interpretation, and final wording. To control for known LLM failure modes (citation hallucination, fabricated empirical numbers, plausible-sounding but unverified policy details), the authors:
    1. Audited every empirical claim in the manuscript against the verified Stata–Python replication outputs (`CLAIMS_AUDIT.md`) and corrected ~13 specific numbers in the v1.6 → v1.7 revision; one further citation correction (Demir & Javorcik, 2018) was applied in the v1.7 → v1.8 revision after WebSearch verification of all Tier-C references (`VERIFICATION_RESULTS.md`).
    2. Removed AI-generated specific Chinese SME policy-reform names, dates, and programme acronyms that lacked verifiable primary sources.
    3. Verified all 39 references in the manuscript against ScienceDirect, Wiley, Springer, and journal homepages; all DOIs resolve to the cited record.
- **Authorship attribution.** No part of the AI-assistant output is included in the manuscript without author review, modification, and verification. The AI assistant is not listed as an author and does not meet ICMJE authorship criteria. The authors take full responsibility for the integrity of the work.

## 9. Preprint policy

This manuscript has not been deposited as a preprint at the time of submission. The authors are willing to comply with APJM's preprint policy (currently, APJM generally permits preprints prior to submission and during review, provided the journal version is the version of record on acceptance). The authors will not deposit the manuscript on a preprint server during APJM review without prior editorial agreement.

## 10. Other journal submissions

This manuscript is original work. It has not been published previously, in whole or in part, in any other journal, conference proceedings, or book chapter. It is not currently under consideration at any other journal. The earlier work by the same authors cited in the manuscript (Do & Tu, 2025 in *ICBEF 2025 proceedings*; Do & Tu, 2026 in *Vietnam Economic Financial Review*) addresses adjacent but distinct questions (meta-analytic synthesis and country-cluster heterogeneity in emerging Asia respectively) and does not overlap with the within-country threshold-stability test that is the specific contribution of the present paper.
