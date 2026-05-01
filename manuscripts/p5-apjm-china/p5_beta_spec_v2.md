# P5 Option β V2 — Direct-Test Specification

**Purpose**: spec the direct test of working-capital conditioning of the inverted-U downturn for P5, *before* running raw China .dta. P5 identity remains a threshold-stability paper under Option C+; β is a mechanism-strengthening module, not a redefinition.

**Architectural constraint**: results from β can move P5's wording from "interpretive working-capital trap" to "directly examined working-capital conditioning", but cannot move P5's title or core identity to a working-capital paper.

---

## §1. Research question

> Does firm-level working-capital condition moderate the negative quadratic segment of the export-intensity–performance relationship in Chinese manufacturing SMEs?

### Focal interpretation rule

The focal parameter is the interaction between working-capital condition and the **squared** export-intensity term. A statistically and theoretically consistent interaction means working-capital condition shapes the **steepness of the post-threshold downturn**. A null or unstable interaction does not invalidate the threshold result; it only limits the strength of the mechanism claim.

---

## §2. Variable coding sheet

### Block A — Liquidity Access (positive coding = more access)

| Variable | WBES item | Raw meaning | Coding | Construct meaning | Expected sign on `FSTS²` interaction |
|---|---|---|---|---|---|
| `overdraft` | k4 | Overdraft facility | 1 = yes, 0 = no | Short-term liquidity buffer | Positive (access ↓ stress) |
| `line_credit` | k5 | Line of credit / loan | 1 = yes, 0 = no | Formal external financing capacity | Positive |
| `bank_loan` | k9 | Bank loan / formal credit | 1 = yes, 0 = no | Long-term formal finance | Positive |

### Block B — Trade-Credit Exposure (positive coding = more exposure)

| Variable | WBES item | Raw meaning | Coding | Construct meaning | Expected sign on `FSTS²` interaction |
|---|---|---|---|---|---|
| `sales_credit` | k14 | Share of sales sold on credit | Continuous % or share | Receivables exposure / cash-conversion delay | Negative (exposure ↑ stress) |
| `purchases_credit` | k7 | Share of inputs bought on credit | Continuous % or share | Supplier-financed input buffer OR dependence | Ambiguous — robustness only |

### Block C — Financing Structure (decompose `k8`)

| Variable | WBES item component | Coding | Construct meaning | Expected sign on `FSTS²` interaction |
|---|---|---|---|---|
| `wc_internal` | k8: % WC financed internally | Continuous % | Self-financing reliance | Negative (more internal = more strain) |
| `wc_bank` | k8: % WC financed by banks | Continuous % | Bank/formal external buffer | Positive |
| `wc_trade` | k8: % WC financed by suppliers / trade credit | Continuous % | Trade-credit buffer OR dependence | Ambiguous — robustness only |
| `wc_other` | k8: other external financing | Continuous % | Residual external support | Positive but treat as robustness |

### Coding non-negotiables

- **Main variables must have one-directional construct meaning** (clear access vs constraint, exposure vs none). Ambiguous items (`k7`, `wc_trade`) are robustness only.
- **Coding direction must be locked before running models** to prevent post-hoc "diễn giải theo kết quả".
- **Wave-coding consistency**: if WBES 2012 codes an item differently from 2024 (e.g. categorical vs continuous), document and harmonize before pooling.

---

## §3. Index construction

Em recommends **3 primary operationalizations** + **1 composite robustness index**, NOT a single mega-index.

### Operationalization 1 — Liquidity Access Index

Standardised mean of `overdraft`, `line_credit`, `bank_loan`:

```
LiquidityAccess_z = mean( z(overdraft), z(line_credit), z(bank_loan) )
```

Higher = more liquidity access.

### Operationalization 2 — Receivables Exposure (single item or pair)

Primary: `sales_credit` (`k14`) standalone, standardised within wave.

Robustness: pair with `purchases_credit` (`k7`) only if coding direction can be defended.

Higher = more exposure.

### Operationalization 3 — Financing Structure (decomposed)

Two separate variables, *not* netted:
- `wc_internal_z` — internal-financing dependence
- `wc_bank_z` — bank-financing support

These are entered separately into models so signs can be observed independently.

### Robustness composite — `wc_stress_index`

After the three primary operationalizations are estimated, a composite stress index can be built. Code so higher = more stress:
- Subtract `LiquidityAccess_z` (less access = more stress)
- Add `ReceivablesExposure_z` (more exposure = more stress)
- Add `wc_internal_z` (more internal reliance = more stress)
- Subtract `wc_bank_z` (less bank support = more stress)

The composite is **robustness only**; main results are reported at item-level and block-level.

---

## §4. Model ladder

| Step | Purpose | Specification | Status in manuscript |
|---|---|---|---|
| **M0** | Threshold replication | `lnLP ~ FSTS + FSTS² + controls` | Mandatory baseline |
| **M1** | Item-level direct test | M0 + WC_item + (FSTS² × WC_item) | Diagnostic |
| **M2** | Full item interaction | M0 + WC_item + (FSTS × WC_item) + (FSTS² × WC_item) | Robustness |
| **M3** | Block-level test | M0 + Block_index + (FSTS² × Block_index) for each Block | **Main extension** (results reported in main text) |
| **M4** | Composite stress test | M0 + wc_stress_index + (FSTS² × wc_stress_index) | Robustness only |
| **M5** | Wave-specific replication | Run M1–M4 separately for 2012, 2024, pooled | Required for final scenario verdict |

### Joint WC + Digital diagnostic

After M3 with Liquidity Access Index (or whichever block is strongest), run:

```
lnLP ~ FSTS + FSTS² + WC + Digital + (FSTS² × WC) + controls
```

This checks whether WC interaction survives digital control. If it does, the working-capital interpretation is strengthened and the §5 wording can be upgraded.

### Model equations

**M0 baseline:**
$$
lnLP_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \gamma' Controls_i + \varepsilon_i
$$

**M1 / M3 main β model:**
$$
lnLP_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 WC_i + \beta_4 (FSTS_i^2 \times WC_i) + \gamma' Controls_i + \varepsilon_i
$$

Focal parameter: `β₄`.

**M2 robustness model:**
$$
lnLP_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 WC_i + \beta_4 (FSTS_i \times WC_i) + \beta_5 (FSTS_i^2 \times WC_i) + \gamma' Controls_i + \varepsilon_i
$$

Linear interaction `β₄` is supplementary; mechanism logic is tied to `β₅` (quadratic interaction).

---

## §5. Expected signs summary

| WC variable type | Coding direction | Expected sign on interaction with `FSTS²` |
|---|---|---|
| Liquidity access (k4, k5, k9, Liquidity Access Index) | Higher = more access | **Positive** |
| Liquidity stress (reverse-coded) | Higher = more constraint | **Negative** |
| Receivables exposure (k14) | Higher = more sales on credit / slower cash recovery | **Negative** |
| Internal-funding dependence (`wc_internal`) | Higher = self-financing burden | **Negative** |
| External financing support (`wc_bank`) | Higher = more bank/external support | **Positive** |
| Composite `wc_stress_index` | Higher = greater overall stress | **Negative** |

Interpretation reminder: a *positive* `β₄` for an access-coded variable ≡ a *negative* `β₄` for a stress-coded variable. Both are theoretically equivalent; never claim both as independent evidence.

---

## §6. Decision rules (scenario classification)

### Rule SUPPORTED

P5 may upgrade wording to "the working-capital interpretation is not only theoretically plausible but also directly examined in supplementary core analyses" if **all** of:

1. At least one **primary operationalization** (Liquidity Access Index, Receivables Exposure, OR `wc_internal`/`wc_bank` decomposition) yields the expected sign on `β₄` with statistical significance at conventional levels (p < .05) **in the pooled sample**.
2. The same sign is **not contradicted in a substantively important way** in either wave (e.g. no wave-flip from −0.5*** to +0.5***; mild attenuation is acceptable).
3. The `Joint WC + Digital diagnostic` shows the WC interaction surviving digital control (β₄ retains its sign and is at least marginally significant).
4. Magnitudes are economically meaningful (effect at ±1 SD of WC measure changes the predicted post-threshold slope by an interpretable amount).

### Rule LIMITED

Use limited-support wording ("results provide limited but suggestive evidence consistent with a working-capital contingency, although they do not justify a stronger claim that the mechanism is directly and stably identified") if:

1. Only the composite `wc_stress_index` reaches significance, but item-level / block-level results are mixed; OR
2. Sign is correct in pooled and one wave but flips or fades in the other; OR
3. WC interaction is significant but loses significance after adding digital.

### Rule NULL

Retain Option C+ "interpretive working-capital trap" wording ("direct working-capital tests do not provide sufficiently robust support for a strong mechanism claim") if:

1. No primary operationalization shows the expected sign with significance in pooled; OR
2. Signs are inconsistent across operationalizations (e.g. Liquidity Access Index says one thing, Receivables Exposure says the other); OR
3. Results disappear under reasonable robustness checks.

### Anti-HARKing safeguards

- The decision rules above are pre-registered in this spec, **before β is run**.
- If the actual results sit between two scenario rules, default to the **less supportive** classification.
- A single coefficient with attractive p-value but inconsistent block-level pattern does NOT trigger SUPPORTED.

---

## §7. Estimation order (fixed ex ante)

1. **M0** — replicate threshold core; confirm TP and inverted-U survive in current sample
2. **M1 item-level** — for each WC item: `overdraft`, `line_credit`, `bank_loan`, `sales_credit`, `wc_internal`, `wc_bank`
3. **M3 block-level** — Liquidity Access Index, Receivables Exposure, Financing Structure (`wc_internal` + `wc_bank` separately)
4. **M4 composite** — `wc_stress_index`
5. **M5 wave-specific replication** — run all of the above for 2012, 2024, pooled
6. **Joint diagnostic** — strongest M3 + digital
7. **Classify** — apply decision rules, write `p5_beta_results_memo.md`

Robustness-only items (`purchases_credit`, `wc_trade`) are run last and do NOT count toward scenario classification.

---

## §8. Digital retention block

P5 keeps digital variables, but in Option C+ they are **secondary explanatory architecture**, not central. Em uses digital in two ways:

| Digital model | Role | Expected pattern under Option C+ |
|---|---|---|
| **D1** Direct level | M0 + Digital | Positive direct association |
| **D2** Joint with WC | M0 + WC + Digital + (FSTS² × WC) | WC interaction survives digital control |
| **D3** Robustness curvature | M0 + Digital + (FSTS × Digital) + (FSTS² × Digital) | Mostly null on curvature |

### Digital decision rules

1. If D1 is positive and significant but D3 interactions are weak → keep digital as a level shifter in the manuscript.
2. If WC interaction in M3/D2 remains significant after digital control → upgrade WC wording per rule SUPPORTED.
3. If D3 digital interactions appear stronger than M3 WC interactions, do **not** reposition the paper around digital moderation; report digital interactions cautiously as ancillary heterogeneity.
4. **Do not** reintroduce J-curve / Brynjolfsson framing into P5 through digital models.

### Digital construct label

Use **"digital adoption"** (not "digital capability") consistently in P5 to honor the WBES measurement limit. This matches the conservative labeling em uses in P4.

---

## §9. Results memo scaffold

After β runs, fill in this memo at `output/p5_beta_results_memo.md`:

```md
# P5 Option β — Results Memo

## Baseline (M0)
- Threshold replicated? [Yes/No, TP value]
- Turning point remains within prior range (~47-49%)? [Yes/No]
- 2012 and 2024 stability preserved (Paternoster z ns)? [Yes/No]

## Item-level evidence (M1)
- k4 overdraft: sign=[+/-], p=[value], interpretation=[expected/contradicted]
- k5 line of credit: sign=[+/-], p=[value], interpretation=[expected/contradicted]
- k9 bank loan: sign=[+/-], p=[value], interpretation=[expected/contradicted]
- k14 sales on credit: sign=[+/-], p=[value], interpretation=[expected/contradicted]
- k7 purchases on credit (robustness): sign=[+/-], p=[value]
- k8 internal financing: sign=[+/-], p=[value], interpretation=[expected/contradicted]
- k8 bank financing: sign=[+/-], p=[value], interpretation=[expected/contradicted]

## Block-level evidence (M3)
- Liquidity Access Index: [supported / mixed / null]
- Receivables Exposure: [supported / mixed / null]
- Financing Structure (wc_internal + wc_bank decomposed): [supported / mixed / null]

## Composite evidence (M4)
- wc_stress_index: [supported / mixed / null]

## Joint with Digital
- WC interaction survives digital control? [Yes/No]
- Digital direct effect positive and significant? [Yes/No]
- Digital interactions on curvature significant? [Yes/No (expected null)]

## Cross-wave stability (M5)
- 2012: [supported / mixed / null]
- 2024: [supported / mixed / null]
- pooled: [supported / mixed / null]

## Final scenario classification
Choose ONE per Rule §6:
- [ ] SUPPORTED — directly examined and supported
- [ ] LIMITED — limited but suggestive evidence
- [ ] NULL — interpretive mechanism only

## Manuscript action
- Title to use: [from Tier 1 / Tier 2 / Tier 3 per scenario]
- Abstract version to use: [supported / limited / null]
- Results §4.X subsection to use: [supported / limited / null]
- Discussion §5.1 to use: [supported / limited / null]
- Conclusion §6 to use: [supported / limited / null]
- Working-capital trap: [interpretive only / supported by direct test]
- Appendix needed for full WC ladder? [Yes/No]
```

---

## §10. Manuscript consequences

### If supported

- Keep threshold and stability as the paper's lead contribution
- Add one short methods paragraph describing WC operationalization (use Methods β block from `p5_writing_pack_option_c_plus.md` §3)
- Add one results subsection after the threshold models (use Results §4.X — supported template)
- Add one discussion paragraph (use Discussion §5.1 — supported template)
- **Do NOT rename the paper as a full mechanism study**

### If limited

- Use limited-scenario templates throughout
- Mention the partial WC support honestly in abstract, results, discussion
- Working-capital trap remains primary interpretation but with hedge wording

### If null

- Use null-scenario templates throughout
- Direct WC tests reported briefly in robustness or limitations
- Working-capital trap retained as theoretically grounded interpretation only
- Future-research sentence elevated in Conclusion

---

## §11. Non-negotiable portfolio rules

- **No Brynjolfsson J-curve framing in P5.** P4 holds that hedged "consistent-with" J-curve interpretation. P5 stays exclusively in threshold-stability + WC interpretation territory.
- **No cross-paper links inside P5 manuscript.** Per anh's earlier rule. Cross-country comparison tables are dissertation-chapter content, not manuscript content.
- **Variable construction must be P5-internal.** P5 uses TCI_full (4-item) per its own do-file; em does not retro-align P5 to P4's TCI_thin (2-item). The `portfolio_consistency_audit.md` flags this for anh's awareness; resolution is anh's choice.

---

## §12. Deliverables after β execution

1. `output/p5_beta_results.csv` — full coefficient table for M0–M5 (long format: model, sample, variable, beta, se, p, n)
2. `output/p5_beta_results_memo.md` — completed scenario memo (template above)
3. one regression table for inclusion in manuscript (item-level + block-level + composite)
4. one figure if the strongest WC interaction is visualisable (e.g. predicted lnLP across FSTS at low/high Liquidity Access)
5. updated manuscript wording selection (which scenario template to use in §1, §4, §5, §6)

---

*End of β V2 specification. See `p5_writing_pack_option_c_plus.md` for the prose templates that map to each β scenario.*
