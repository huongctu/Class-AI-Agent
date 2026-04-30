# Cover Letter — P4 (v4.4) revised submission to Journal of World Business

30 April 2026

Editor‑in‑Chief
*Journal of World Business*

**From:**
Do Thuy Huong (huongp1323001@gstudent.ctu.edu.vn)
Phan Anh Tu, corresponding author (patu@ctu.edu.vn)
School of Economics, Can Tho University, Can Tho, Vietnam

Dear Editor,

We are pleased to submit the revised manuscript, *"Digital Adoption, Technological Capability, and the Internationalisation–Performance Relationship in Vietnam: Evidence from a Transitional Digital Economy,"* for the second round of review at the *Journal of World Business*, following the Major Revision decision. A point‑by‑point response to the Editor's letter is provided as `response_to_reviewer_v4_4.md` in the accompanying replication package; the eight‑commit revision arc that produced v4.4 is logged in `changelog_v4_3_to_v4_4.md` and visible on pull request #2 of the manuscript repository. The paper makes three contributions to the digital international‑business literature.

First, we **separate two constructs that the IB literature frequently conflates**: a Lall-tradition Technological Capability Index (TCI) anchored in foreign-licensed technology and quality certification, and a Bharadwaj/Verhoef-tradition Digital Adoption Index (DAI) anchored in basic digital presence and electronic-payment intensity. The two constructs deliver materially different productivity signatures across the I–P curve in the three Vietnam WBES waves: TCI is both a level shifter and a curvature modifier, while DAI follows a productivity J-curve and — in the most recent (2023) wave — moderates the I–P curvature in a direction that qualifies the conditional-complement reading of digital adoption.

Second, we **document an institutional-saturation account** of the 2023 H4 inversion within the Vietnam sample. Where digital adoption is concentrated at Tier 1–2 (presence rather than dynamic capability), basic digitalisation appears to *amplify* rather than substitute for the coordination costs that bend the I–P curve downward at high export intensity. This pattern is internally consistent with our reading of Brynjolfsson, Rock & Syverson's (2021) productivity J-curve. We do not claim the pattern generalises beyond the Vietnam WBES sample; whether it obtains in other settings is an empirical question for separate work.

Third, we **provide a verified, reproducible analytic pipeline**. We re-implemented the analytic pipeline as an independent Python script and verified numerical reproducibility using three OLS estimators — `statsmodels` with HC1 robust covariance, `linearmodels` `IV2SLS` with `cov_type='robust', debiased=True`, and a pure-NumPy closed-form OLS with manual HC1 robust covariance V = (X′X)⁻¹ X′ diag(ê²) X (X′X)⁻¹ · n / (n − k). The three implementations agree to machine precision (maximum coefficient difference 4.06 × 10⁻¹³, maximum standard-error difference 1.80 × 10⁻¹⁴) on the pooled outcome equation. A Stata do-file mirroring the same specification is included in the replication package for independent third-party verification; it has not been executed by the authors. The replication package is hosted on the corresponding author's GitHub repository under `manuscripts/p4-jwb-vietnam/`.

Relative to the v4.3 manuscript circulated for internal review, v4.4 incorporates three substantive corrections that emerged from this verification protocol:

- WBES non-response codes (`-9`) are treated as missing rather than as numeric data, restoring methodological alignment with Enterprise Survey codebook guidance.
- The H1 inverted-U is reported as confirmed in the 2015 wave (LM p = .033) and pooled sample (p = .041), marginal in 2023 (p = .068), and not statistically significant in 2009 (p = .128), against a previous "confirmed in all three waves" framing.
- The H2 TCI moderation is reported as significant in three of four panels (joint F p = .030 / .046 / .027 in 2009 / 2023 / pooled), reversing a previous "level-shift only" framing; the H4 DAI moderation is reported as significant in 2023 (joint F p = .022) with a negative FSTS × DAI consistent with the institutional-saturation interpretation, against a previous "null" framing.

The manuscript is approximately 7,400 words excluding references, two figures (a conceptual model and the predicted I–P curves by wave), and the regression tables exported by the replication pipeline. The paper has not been published or submitted elsewhere. Both authors have reviewed and approved the submitted version. The authors received no specific grant from any funding agency in the public, commercial, or not‑for‑profit sectors for this work and declare no conflicts of interest.

The data underlying this manuscript are drawn from the World Bank Enterprise Surveys (WBES) and were used in compliance with the WBES Data Access Protocol; per that protocol, the replication package does not redistribute the WBES `.dta` files. The Acknowledgements include the wording the World Bank Enterprise Analysis Unit recommends for studies that use WBES microdata.

We thank you for considering our work and look forward to your editorial assessment.

Sincerely,

**Phan Anh Tu** (corresponding author)
School of Economics, Can Tho University
Campus II, 3/2 Street, Ninh Kieu District, Can Tho City, Vietnam
Email: patu@ctu.edu.vn

On behalf of the co‑author team.
