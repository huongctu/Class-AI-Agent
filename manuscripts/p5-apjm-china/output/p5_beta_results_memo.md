# P5 Option β V2 — Results Memo

**Pipeline run**: 2026-04-30 via `manuscripts/p5-apjm-china/code/p5_beta_pipeline.py`
**Plan**: B1 (cross-wave clean: Block A Liquidity Access + Block C Financing Structure + Block D Access obstacle; Block B Receivables Exposure as 2012-only robustness)
**Spec discipline**: WBES `-9` and `-7` treated as missing; TCI_full requires ≥3 of 4 items (CNo1/CNo3 mapping for CHN 2012); WC interaction models drop TCI/DAI as covariates so 2012 runs.

---

## Baseline (M0) — threshold core

| Wave | N | Turning point | LM p | FSTS β (p) | FSTS² β (p) |
|---|---|---|---|---|---|
| CHN 2012 | 2,619 | **49.4%** | < .001 ✓ | +2.060 (< .001) | −2.085 (< .001) |
| CHN 2024 | 1,940 | **47.6%** | .037 ✓ | +1.428 (.014) | −1.502 (.035) |
| CHN pooled | 4,559 | **48.9%** | < .001 ✓ | +1.782 (< .001) | −1.821 (< .001) |

**Threshold replicated**: Yes (all three samples confirm inverted-U; TPs cluster at ~48%; well within prior P5 patch range 47.2-49.4%).

**Cross-wave stability**: Paternoster z-tests on FSTS / FSTS² (informal from coefficients): difference between waves is small relative to SEs → consistent with H2 structural-stability claim.

---

## Direct TCI / DAI effects (M0p)

| Wave | N | TCI β_z (p) | DAI β_z (p) |
|---|---|---|---|
| CHN 2012 | 1,633 | +0.206 (< .001) ✓ | **−0.064 (.044)** ⚠ |
| CHN 2024 | 1,915 | +0.286 (< .001) ✓ | +0.005 (.871) |
| CHN pooled | 3,548 | +0.266 (< .001) ✓ | **−0.064 (.004)** ⚠ |

**Note on DAI direct effect**: After applying spec-A discipline (drop `-9`/`-7` codes), DAI_thin direct effect is **negative** in 2012 and pooled. This contradicts H4 (positive direct association). Possible reasons:
- DAI_thin = mean(`c22b` website + `e6` foreign-licensed tech); the e6 component may behave heterogeneously in CHN 2012 sample
- Sample size dropped from 2,612 (P5 patch) to 1,633 (em spec-A) for CHN 2012 — 60% retention; selection effect possible
- In CHN 2024, DAI direct is null

This is a **substantive divergence from P5 patch numbers** (which reported DAI β_z 2012=+0.050*, 2024=+0.141*** under different spec). Em flags this for anh's decision: report the verified-spec-A finding honestly, or revert to P5 patch convention?

---

## Item-level WC × FSTS² (M1) and block-level (M3)

Expected signs per spec: positive for access (overdraft, line_credit, LA_idx, k3bc bank, k3f trade-as-buffer), negative for stress (k3a internal-funding dependence, k30 access obstacle).

| WC variable | Block | Wave | β_inter | p | n | Sign expected? | Verdict |
|---|---|---|---|---|---|---|---|
| overdraft | A — Liquidity Access (item) | 2012 | +0.268 | .050 | 2,531 | + (yes) | marginal correct |
| overdraft | A | 2024 | −0.384 | .081 | 1,888 | + | **WRONG sign** marginal |
| overdraft | A | pooled | +0.183 | .135 | 4,419 | + | null |
| line_credit | A | 2012 | −0.086 | .505 | 2,511 | + | null/wrong |
| line_credit | A | 2024 | −0.243 | .340 | 1,881 | + | null/wrong |
| line_credit | A | pooled | −0.143 | .223 | 4,392 | + | null/wrong |
| **LA_idx** | A — block | 2012 | +0.115 | .395 | 2,590 | + | null |
| **LA_idx** | A — block | 2024 | −0.352 | .136 | 1,924 | + | **WRONG sign** marginal |
| **LA_idx** | A — block | pooled | +0.001 | .994 | 4,514 | + | null |
| k3a internal | C — Financing (internal) | 2012 | +0.008 | .130 | 2,566 | − | wrong sign |
| k3a internal | C | 2024 | +0.005 | .353 | 1,873 | − | wrong sign null |
| k3a internal | C | pooled | +0.007 | .060 | 4,439 | − | **wrong sign** marginal |
| k3bc bank | C — Financing (bank) | 2012 | −0.006 | .441 | 2,559 | + | wrong sign null |
| k3bc bank | C | 2024 | −0.005 | .675 | 1,872 | + | wrong sign null |
| k3bc bank | C | pooled | −0.007 | .275 | 4,431 | + | wrong sign null |
| k3f trade-credit | C — Financing (trade) | 2012 | **−0.017** | **.009** | 2,559 | (ambiguous; interpret as dependence) | **correct sign significant** ✓ |
| k3f trade-credit | C | 2024 | −0.003 | .660 | 1,883 | | null |
| k3f trade-credit | C | pooled | −0.010 | .054 | 4,442 | | marginal |
| **k30 obstacle** | D — Access obstacle | 2012 | −0.007 | .968 | 2,593 | − | null |
| **k30 obstacle** | D | 2024 | **+1.639** | **< .001** | 1,620 | − | **WRONG sign, large magnitude — anomaly** |
| **k30 obstacle** | D | pooled | +0.091 | .595 | 4,213 | − | null |

### Key observations

1. **Block A (Liquidity Access)** — sign flip between 2012 and 2024 (positive 2012, negative 2024). Pooled null. Em's decision rule says sign flip triggers downgrade.

2. **Block C item k3a (internal funding)** — wrong sign throughout (positive when expected negative). The hypothesis "internal-funding dependence = stress" not supported.

3. **Block C item k3f (trade credit financing)** — only WC variable with **correct expected sign and significance in 2012 + marginal pooled**. Interpretation: firms more dependent on supplier trade credit experience steeper post-threshold downturn. Sign reading is "trade credit dependence" rather than "trade credit buffer." However, 2024 wave does NOT replicate (β=−0.003, p=.660), so cross-wave consistency fails.

4. **Block D (k30 obstacle)** — large positive significant interaction in 2024 (β=+1.639, p<.001) but null in 2012 and pooled. The sign is **opposite** em expected (em expected: more obstacle → steeper downturn, so negative interaction). The 2024 magnitude is implausibly large (0.04 × 4 × 1.639 = 0.26 log-productivity boost at FSTS=20% with severe obstacle), suggesting model misspecification or small-cell instability (only 128 firms at k30=2-4 in 2024). Em flags as **anomaly, not evidence**.

---

## Composite WC stress index (M4)

| Wave | β_inter | p | n |
|---|---|---|---|
| CHN 2012 | +0.058 | .612 | 2,619 |
| CHN 2024 | +0.259 | .168 | 1,934 |
| CHN pooled | +0.119 | .249 | 4,553 |

All null. Composite stress index does not predict steeper post-threshold downturn.

---

## Block B — 2012-only robustness (k1c, k2c)

| WC variable | β_inter | p | n |
|---|---|---|---|
| k1c (purchases on credit %) | −0.004 | .978 | 2,556 |
| k2c (sales on credit %) | +0.129 | .310 | 2,565 |

Both null. Receivables exposure (k2c) has wrong sign and is null. The most direct WC-trap proxy in WBES (sales on credit) provides no evidence of conditioning the post-threshold downturn.

---

## Final scenario classification

Per the Decision Rules in `p5_beta_spec_v2.md` §6:

| Rule | Condition | Met? |
|---|---|---|
| **SUPPORTED** | ≥1 primary operationalization yields expected sign with p < .05 in pooled, no sign reversals across waves | ✗ NO — k3f is closest (p=.054 marginal) but 2024 fails replication |
| **LIMITED** | Composite or some block significant but item-level mixed; OR sign correct in pooled+one wave but flips/fades | ⚠ partial via k3f only |
| **NULL** | No consistent signal; sign inconsistent across operationalizations; OR results disappear under robustness | ✓ all three triggers met |

### Em final classification: **NULL** (with one weak hint via k3f trade-credit dependence in 2012 only)

**Justification**:
- Block A (Liquidity Access) — sign flip between waves, all marginal/null
- Block C item k3a (internal financing) — wrong sign throughout, marginal pooled
- Block C item k3f (trade credit) — correct sign significant in 2012, marginal pooled, fails 2024 (cross-wave inconsistency violates Rule SUPPORTED)
- Block D (k30 obstacle) — wrong sign anomaly in 2024 only; null elsewhere
- Composite WC stress index — null in all three samples
- Block B 2012-only (sales on credit) — null

Per em's anti-HARKing safeguard (decision rules pre-registered before β ran), em classifies as **NULL** rather than chase the k3f marginal pooled signal.

---

## Implications for manuscript

| Decision | Action |
|---|---|
| Title to use (per scenario) | **Tier 1 / null-safe** — *The Export Intensity–Performance Relationship in Chinese Manufacturing SMEs: A Threshold-Stability Perspective* |
| Abstract version | **null** scenario from `p5_writing_pack_option_c_plus.md §1` |
| Results §4.X subsection | **null** scenario template |
| Discussion §5.1 | **null** scenario template |
| Conclusion §6 | **null** scenario template |
| Working-capital trap framing | retained as **interpretive theoretical mechanism only**; direct test reported as exploratory robustness |
| §6 Limitations | add explicit sentence: *"Direct examination of working-capital conditioning using WBES proxies (k7, k8/k82, k3 series, k30, plus 2012-only k1c/k2c) did not yield robust support for the trap mechanism; receivables-exposure measures (k2c) absent from the 2024 release further constrained cross-wave testing."* |
| Future work sentence in Conclusion | elevated: *"Future research should test the liquidity interpretation with more direct measures of receivables turnover, trade-finance access, and cash-cycle pressure that are not yet captured in cross-sectional WBES microdata."* |

---

## Substantive note for anh's review

1. **Threshold core fully replicates** P5 patch numbers (TP ~48%, all LM p significant). The threshold-stability contribution stands robustly.

2. **TCI direct effect fully replicates** P5 patch's direction (positive significant in both waves; magnitudes em finds 0.206 → 0.286 vs patch 0.171 → 0.291 — small differences from spec-A `-9` cleanup but qualitatively identical).

3. **DAI direct effect** under spec-A is **negative or null**, vs P5 patch's positive significant. This is the first material divergence and matches the same pattern em saw for VN P4 spec-A vs spec-B. Em recommends adopting spec-A and noting the difference; alternatively anh can restore P5's listwise convention if cross-portfolio consistency is preferred.

4. **β working-capital interpretation: NULL.** Across 7 primary cross-wave WC variables, no operationalization yields expected sign + significance + cross-wave stability. Block C k3f trade credit shows isolated 2012 signal. The k30 obstacle anomaly in 2024 is implausibly large and likely a small-cell artefact.

5. **P5 should remain a threshold-stability paper with interpretive working-capital framing** — exactly the Option C+ identity em recommended in the audit. Direct mechanism test does not strengthen this framing but also does not invalidate the theoretical interpretation.

6. **Receivables exposure (k1c / k2c) absent from WBES China 2024** is a substantive data limitation. P5 §6 Limitations should disclose this and propose future work on richer financial microdata.

---

*End of memo. Em proceeds to Phase C (figures) and Phase D (manuscript draft) using the null-scenario templates from `p5_writing_pack_option_c_plus.md`.*
