# Cover Letter — P4 (v4.4) submission to Journal of World Business

[Date]

Editor-in-Chief
*Journal of World Business*

Dear Editor,

We are pleased to submit our manuscript, *"Digital Adoption, Technological Capability, and the Internationalisation–Performance Relationship in Vietnam: Evidence from a Transitional Digital Economy,"* for consideration at the *Journal of World Business*. The paper makes three contributions to the digital international-business literature.

First, we **separate two constructs that the digital-IB literature frequently conflates**: a Lall-tradition Technological Capability Index (TCI) anchored in foreign-licensed technology and quality certification, and a Bharadwaj/Verhoef-tradition Digital Adoption Index (DAI) anchored in basic digital presence and electronic-payment intensity. The two constructs deliver materially different productivity signatures across the I–P curve: TCI is both a level shifter and a curvature modifier, while DAI follows a productivity J-curve and — in the most recent (2023) wave — moderates the I–P curvature in a direction that *inverts* the conditional-complement logic dominant in the literature on digital-frontier economies.

Second, we **document an institutional-saturation account** of the H4 inversion. In a transitional digital economy where digital adoption is concentrated at Tier 1–2 (presence rather than dynamic capability), basic digitalisation appears to *amplify* rather than substitute for the coordination costs that bend the I–P curve downward at high export intensity. This finding is internally consistent with our reading of Brynjolfsson, Rock & Syverson's (2021) productivity J-curve and reframes the cross-paper prediction that DAI moderation is a digital-frontier phenomenon detectable only when institutional digital maturity crosses a threshold.

Third, we **provide a verified, reproducible analytic pipeline**. We re-implemented the analytic pipeline as an independent Python script and verified numerical reproducibility using three OLS estimators — `statsmodels` with HC1 robust covariance, `linearmodels` `IV2SLS` with `cov_type='robust', debiased=True`, and a pure-NumPy closed-form OLS with manual HC1 robust covariance V = (X′X)⁻¹ X′ diag(ê²) X (X′X)⁻¹ · n / (n − k). The three implementations agree to machine precision (maximum coefficient difference 4.06 × 10⁻¹³, maximum standard-error difference 1.80 × 10⁻¹⁴) on the pooled outcome equation. A Stata do-file mirroring the same specification is included in the replication package for independent third-party verification; it has not been executed by the authors. The replication package is hosted on the corresponding author's GitHub repository under `manuscripts/p4-jwb-vietnam/`.

Relative to the v4.3 manuscript circulated for internal review, v4.4 incorporates three substantive corrections that emerged from this verification protocol:

- WBES non-response codes (`-9`) are treated as missing rather than as numeric data, restoring methodological alignment with Enterprise Survey codebook guidance.
- The H1 inverted-U is reported as confirmed in the 2015 wave (LM p = .033) and pooled sample (p = .041), marginal in 2023 (p = .068), and not statistically significant in 2009 (p = .128), against a previous "confirmed in all three waves" framing.
- The H2 TCI moderation is reported as significant in three of four panels (joint F p = .030 / .046 / .027 in 2009 / 2023 / pooled), reversing a previous "level-shift only" framing; the H4 DAI moderation is reported as significant in 2023 (joint F p = .022) with a negative FSTS × DAI consistent with the institutional-saturation interpretation, against a previous "null" framing.

The manuscript is approximately 9,500 words excluding references, two figures (a conceptual model and the predicted I–P curves by wave), and three CSV tables exported by the replication pipeline. The paper has not been published or submitted elsewhere. All authors have reviewed and approved the submitted version.

We thank you for considering our work and look forward to your editorial assessment.

Sincerely,

[Corresponding author name]
[Affiliation]
[Email]

On behalf of the co-author team.
