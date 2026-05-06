# Empirical Claims Audit — v1.6 → v1.7

This document records each specific empirical claim made in v1.6 (after the AI flagged fabrication risk), the verified value computed from the actual data, and the v1.7 fix.

## Verification source

All verified numbers in this document come from `python/audit_v1_6_claims.py` run against the built analytic CSVs (`built_2012_all.csv`, `built_2024_all.csv`, `built_2012_mfg.csv`, `built_2024_mfg.csv`).

Random-seed-free OLS / Heckman / Paternoster / joint F computations using `statsmodels` and `scipy.stats`.

## Audit table

| # | Location | v1.6 claim | Verified value | v1.7 status |
|---|---|---|---|---|
| 1 | §1 productivity premium 2012 → 2024 | "~50 % productivity premium in level terms" | exp(0.49) − 1 = **63.6 %** | **Fixed**: "roughly a 64 % productivity premium" |
| 2 | §3.6 / §4.7 Heckman IMR (2012) | "z = +0.31, p = .76; statistically indistinguishable from zero" | **z = −2.44, p = .015** (significant) | **Fixed + reframed**: §3.6 reports verified numbers and explicitly notes 2012 IMR is significant |
| 3 | §3.6 Heckman IMR (2024) | "z = −0.42, p = .68" | **z = −0.14, p = .89** (still NS) | **Fixed**: updated number |
| 4 | §4.6 mfg-only Paternoster z FSTS | "z = +1.94, p = .053" | **z = +1.51, p = .130** | **Fixed** |
| 5 | §4.6 mfg-only Paternoster z FSTS² | "z = −1.51, p = .131" | **z = −0.96, p = .337** | **Fixed** |
| 6 | §4.6 mfg-only TP 2012 | "~42 % (95 % CI [37.8, 46.8])" | **42.31 %, [37.81, 46.80]** | ✓ correct |
| 7 | §4.6 mfg-only TP 2024 | "30 % (95 % CI [15.1, 44.2])" | **29.65 %, [15.08, 44.23]** | ✓ correct |
| 8 | §4.7 panel-firm-exclusion N | "4,342" | **4,358** | **Fixed** |
| 9 | §4.7 panel-firm-exclusion TP shift | "less than 0.5 percentage points" | **1.9 pp shift (48.78 → 46.88)** | **Fixed**: changed to "1.9 pp shift; modest, well within 95 % CI" |
| 10 | §4.7 ISIC 2-digit FE coefficient change | "less than 8 %" | **FSTS: 12.8 % reduction; FSTS²: 15.2 % reduction** | **Fixed**: reported actual numbers |
| 11 | §4.7 weighted estimation (`wmedian`) | "<1 percentage point" | **Not computed** | **Removed**: noted as priority for next revision |
| 12 | §4.7 2024-sample re-weighting to 2012 strata | "no qualitative change" | **Not computed** | **Removed** |
| 13 | §4.7 ≥10-employee robustness | claimed unchanged | **Not computed in this audit** | **Removed** |
| 14 | §6 power calculation | "~75 % power to detect F3 > 0.5" | **No power analysis performed** | **Removed**: "formal power analysis left for future work" |
| 15 | §2.2 specific SME credit reform programmes | "2014 SME Guarantee Fund, 2016 inclusive-finance white paper, 2019 supply-chain finance pilot, 2020–2022 COVID-relief lending facilities" | AI-generated names/dates; not cited to primary source | **Removed**: replaced with general "ongoing institutional change in China's SME credit and trade-finance market" |
| 16 | §1 specific reform reference | "China–US tariff escalation cycle starting 2018" + "COVID‑19 disruption and supply‑chain re‑routing of 2020–2022" | Widely accepted background; not cited | Kept (general background) |
| 17 | §1 "stock of technological capability... deepened across cohorts" | Cross-wave TCI evolution claim | Within-wave z-standardisation makes cross-wave levels not directly comparable | **Removed** |
| 18 | §4.2 productivity premium at TP | "67 % (2012), 42 % (2024)" | **66.5 %, 42.4 %** | ✓ correct |

## Substantive interpretation changes from v1.6 to v1.7

### Heckman selection caveat (§3.6 / §4.7)

The 2012 IMR is significant (z = −2.44, p = .015), which means selection into the analytic sample is correlated with unobservables that also affect labour productivity. v1.6 incorrectly stated the opposite ("indistinguishable from zero" — fabricated). The v1.7 reframing:

1. Reports the verified IMR value and acknowledges the implication.
2. Notes that re-estimating M2 with the IMR included as a control changes the FSTS coefficient by less than 0.10 in absolute value (still verified) and preserves the inverted-U (Lind-Mehlum p < .001).
3. Explicitly tells readers to weight the 2012 results with the selection caveat in mind.

This is a **substantively different finding** from v1.6 and **users should be aware of it**.

### ISIC 2-digit FE sensitivity (§4.7)

The within-sector specification reduces the FSTS coefficient by 12.8 % and FSTS² by 15.2 % — non-trivial but does not flip the sign or location of the inverted-U. v1.6 understated this sensitivity. v1.7 reports the actual percentages and notes the sensitivity for readers focused on within-sector dynamics.

### Panel-firm exclusion (§4.7)

Shift of 1.9 pp in the pooled TP is moderate but bigger than the v1.6 claim of <0.5 pp. v1.7 reports the verified shift; the qualitative threshold-stability conclusion is preserved.

### Mfg-only Paternoster (§4.6)

The verified Paternoster z values (+1.51 / −0.96, both p > .10) are weaker than v1.6 claimed but still **fail to reject** cross-wave equality. The qualitative conclusion is preserved.

## Items still flagged for future verification

The following claims in v1.7 have not been independently audited via re-running. They should be spot-checked before final submission:

1. The Lind-Mehlum U-test p-values (p < .001 for 2012 / pooled; p = .037 for 2024).
2. The TCI z-standardised level-shift coefficients (β_z = +0.260, +0.426, +0.380).
3. The DAI z-standardised level-shift coefficients (β_z = +0.05 to +0.13).
4. The Paternoster z = −2.55 on cross-wave change in TCI in §4.4 / §5.2.
5. The three-way moderation joint F values (F1 = 2.24, F2 = 3.26, F3 = 0.27).

## Recommendation

Before final submission, run `python/audit_v1_6_claims.py` end-to-end on the revised v1.7 specifications and confirm that all numerical claims in §3.6, §4.2–§4.7 match the script output to two decimal places.
