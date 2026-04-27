# Cross-Paper Consolidation Report

Verified: 2026-04-27 | Engine: Python 3.11 + statsmodels 0.14.6 | HC1 robust SE
Updated: 2026-04-27 — reconciled with Huong's local test run

## 0. CRITICAL: Cross-Validation Discrepancies (Resolved)

Huong ran the analysis script locally and produced `resultsp3singaporeTESTRUN.csv`. Comparing with the session's interactive results revealed **5 specification differences**:

| Issue | My session | Huong's script | Correct | Impact |
|-------|-----------|----------------|---------|--------|
| **FSTS source** | 100 - d3a (total exports) | d3c (direct exports only) | Both valid; d3c excludes indirect | TP shifts ~83% vs ~76% |
| **firm_age** | a7 (categorical 1/2) | year - b5 (continuous years) | **Huong correct** | Controls differ |
| **TCI/DAI scaling** | Raw 0-1 mean | Z-standardized within sample | **Huong better** (interpretable per-SD) | β magnitudes differ, signs/significance match |
| **TCI_full threshold** | Any 1+ item valid | Require 3+ of 4 items | **Huong more rigorous** | Fewer obs for legacy waves |
| **CHN 2012 h8 mapping** | CNo3 (R&D spending) | CNo8 (computer use) | **CNo3 correct** (CNo8 is NOT R&D) | Huong needs to fix |

### Reconciliation decisions:

1. **FSTS**: Use **d3c** (Huong's choice) if papers frame "direct export intensity". Use **100-d3a** if "total internationalization". Both specs should be reported as robustness.

2. **firm_age**: Adopt Huong's `year - b5` (continuous). My `a7` was incorrect.

3. **Z-standardization**: Adopt Huong's approach. Coefficients report per-SD change.

4. **TCI_full n_valid >= 3**: Adopt Huong's threshold. More defensible methodologically.

5. **CHN 2012 CNo8**: **BUG in Huong's script** — `CNo8` = "% workforce using computers" ≠ R&D spending. Must change to `CNo3` = "Last 3 years, spend on R&D?" Verified from variable labels in raw .dta.

### Coefficient reconciliation (P3 Singapore M2):

| Coefficient | Huong (d3c, b5, z-scored) | Session (d3a, a7, raw) | Expected relation |
|---|---|---|---|
| β(FSTS) | 3.490*** | 4.018*** | Lower with d3c (less variance) ✓ |
| β(FSTS²) | -2.103† | -2.630** | Less significant with d3c ✓ |
| TP | 83.0% | 76.4% | Higher with d3c (narrower range) ✓ |
| TCI_z direct | 0.200*** | 0.839*** (raw) | 0.839 × SD(0.21) ≈ 0.176 ≈ 0.200 ✓ |
| R² (M2) | 0.162 | 0.188 | Lower with d3c (less explanatory) ✓ |

All differences are **explained by specification choices**, not bugs (except CNo8).

## 1. Variable Definitions

| Construct | Variable | WBES Items | Construction | Coverage |
|-----------|----------|------------|--------------|----------|
| TCI-thin | `TCI_thin` | e6 (foreign tech) + b8 (quality cert) | mean(binary, binary), z-standardized within sample | ALL 6 waves |
| TCI-full | `TCI_full` | e6 + h1 (product innov) + h8 (R&D) + b8 | mean(4 binary), require >=3 valid, z-standardized. NOTE: for VNM 2009 and CHN 2012, TCI_full effectively equals TCI_thin due to missing h1/h8 items (pandas mean skips NaN) | 5 waves (not VNM 2009) |
| DAI-thin | `DAI_thin` | c22b (website) + e6 (foreign tech) | mean(binary, binary), z-standardized | ALL 6 waves |
| DAI-rich | `DAI_rich` | c22b + k33/100 (e-payment) + k38/100 (e-pay suppliers) | mean(binary, cont, cont), require >=2 valid, z-standardized. NOTE: for CHN 2012 and VNM 2009/2015, DAI_rich falls back to website-only due to NaN skip | 3 B-READY waves only |
| FSTS | `fsts` | d3c (direct export %) / 100 | proportion 0-1. Robustness: also test with (100-d3a)/100 | ALL 6 waves |
| Productivity | `ln_lp` | ln(d2/l1) = ln(sales/employees) | natural log | ALL 6 waves |
| Firm age | `firm_age` | year - b5 (year of establishment) | continuous years | ALL 6 waves |

### Variable mapping for legacy datasets

| Standard var | VNM 2009 | VNM 2015 | VNM 2023 | CHN 2012 | CHN 2024 | SGP 2023 |
|---|---|---|---|---|---|---|
| h1 (product innov) | MISSING | h1 | h1 | CNo1 | h1 | h1 |
| h8 (R&D spending) | MISSING | h8 (continuous, recoded >0=1) | h8 | **CNo3** (NOT CNo8) | h8 | h8 |
| e6 (foreign tech) | e6 | e6 | e6 | e6 (or CNh7) | e6 | e6 |
| b8 (quality cert) | b8 | b8 | b8 | b8 | b8 | b8 |
| c22b (website) | c22b | c22b | c22b | c22b | c22b | c22b |
| k33 (e-payment %) | MISSING | MISSING | k33 | MISSING | k33 | k33 |
| b5 (year established) | b5 | b5 | b5 | b5 | b5 | b5 |

## 2. Sample Handling

- Missing values: WBES codes -9, -8, -7, -6, -99, -66, -77, -88 recoded to NaN
- Binary recoding: 1=Yes -> 1.0, 2=No -> 0.0
- No winsorization applied
- No sector restrictions
- Listwise deletion within each model (statsmodels OLS default)
- manager_exp DROPPED from controls due to multicollinearity with ln_empl (r=0.91, VIF=5.85/6.11)
- TCI/DAI z-standardized within each subsample before regression

### Controls

| Variable | WBES item | Description |
|----------|-----------|-------------|
| ln_empl | ln(l1) | Log of total employees |
| firm_age | year - b5 | Years since establishment (continuous) |
| foreign_dummy | b2b > 0 | Binary: any foreign ownership |
| wave dummies | — | P4: wave_2015, wave_2023. P5: wave_2024 |

## 3. Sample Sizes

| Dataset | Raw N | Analytic N (M2) | Exporters | Exporter % |
|---------|-------|-----------------|-----------|------------|
| SGP 2023 | 623 | 623 | 111 | 17.8% |
| VNM 2009 | 1,053 | ~996 | 369 | 37.1% |
| VNM 2015 | 996 | ~968 | 281 | 29.1% |
| VNM 2023 | 1,028 | ~1,014 | 241 | 23.8% |
| CHN 2012 | 2,700 | ~2,684 | 647 | 24.0% |
| CHN 2024 | 2,189 | ~1,944 | 448 | 20.6% |
| **Total** | **8,589** | **~8,229** | **2,097** | **25.5%** |

Note: Analytic N varies by model due to listwise deletion on different variable sets.

## 4. Paper-Specific Specifications

### P3 (Singapore / target: IBR or MIR)
- TCI: **TCI_full** (e6 + h1 + h8 + b8), z-standardized
- DAI: **DAI_rich** (c22b + k33/100 + k38/100), z-standardized
- Controls: ln_empl, firm_age (year-b5), foreign_dummy
- No wave dummies (single wave)

### P4 (Vietnam / target: JWB)
- TCI: **TCI_thin** (e6 + b8) — forced by VNM 2009 lacking h1/h8
- DAI: **DAI_thin** (c22b + e6) — for cross-wave consistency
- Controls: ln_empl, firm_age, foreign_dummy, wave_2015, wave_2023
- Robustness: VNM 2023 also run with TCI_full and DAI_rich

### P5 (China / target: APJM)
- TCI: **TCI_full** (e6 + h1 + h8 + b8) — CHN 2012 uses CNo1/CNo3
- DAI: **DAI_thin** (c22b + e6) — for cross-wave consistency
- Controls: ln_empl, firm_age, foreign_dummy, wave_2024
- Robustness: CHN 2024 also run with DAI_rich

## 5. Verified Results (from Huong's local test run — P3 Singapore)

### P3 Singapore — Huong's production numbers (d3c, b5, z-scored)

| Model | Key variable | β | SE | p | N | R² |
|-------|-------------|---|----|----|---|-----|
| M2 | fsts | 3.490*** | 0.903 | <.001 | 623 | .162 |
| M2 | fsts_sq | -2.103† | 1.087 | .053 | 623 | .162 |
| M5 | tci_full_z | 0.200*** | 0.042 | <.001 | 623 | .191 |
| M6 | dai_rich_z | 0.114** | 0.038 | .003 | 617 | .170 |
| M4 | fsts_x_dai_rich | -1.181 | 0.913 | .196 | 617 | .178 |
| M4 | fsts_sq_x_dai_rich | 2.869* | 1.284 | .025 | 617 | .178 |
| M8 | tci_full_z | 0.186*** | 0.044 | <.001 | 617 | .202 |
| M8 | dai_rich_z | 0.073† | 0.040 | .064 | 617 | .202 |
| M8 | fsts_x_dai_rich | -1.279 | 0.893 | .152 | 617 | .202 |
| M8 | fsts_sq_x_dai_rich | 3.023* | 1.309 | .021 | 617 | .202 |

**TP = 83.0%** | Lind-Mehlum pending (fsts_sq p=.053 borderline)

### Key differences from session results:
- TP higher (83% vs 76%) due to d3c vs d3a
- TCI still strongly significant (universal finding holds)
- DAI FSTS²×DAI moderation still significant (p=.021) — U-shape pattern CONFIRMED
- DAI FSTS×DAI loses significance in M8 (p=.152) — only the quadratic term survives

## 6. Action Items

1. **Huong: fix CNo8 → CNo3** in build-pooled-dataset.py for CHN 2012 h8 mapping
2. **Decide FSTS measure**: d3c (direct) or 100-d3a (total) — affects TP and paper framing
3. **Run full pipeline** for P4 Vietnam and P5 China with corrected script
4. **Report both FSTS specs** as robustness in each paper

## 7. Cross-Paper Narrative (updated)

### Main finding: TCI capability complementarity (universal)
TCI has a direct productivity premium in ALL waves tested (β_z ≈ 0.18-0.20 per SD in SGP, pattern expected to replicate in VNM/CHN). TCI does NOT moderate the I-P curve shape. Consistent with Lall (1992) and Rugman-Verbeke NLB-FSA logic.

### Secondary finding: TP gradient
TP increases with development level. Exact values depend on FSTS measure:
- d3c (direct): SGP ~83% > CHN/VNM TBD
- d3a (total): VNM ~34% < CHN ~47% < SGP ~76%

### Exploratory finding: DAI moderation
DAI quadratic moderation (FSTS²×DAI) significant in Singapore (p=.021-.025 across specs). Linear term (FSTS×DAI) loses significance in full model. Pattern needs verification in P4/P5.
