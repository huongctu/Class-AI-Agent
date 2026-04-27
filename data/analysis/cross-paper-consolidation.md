# Cross-Paper Consolidation Report

Verified: 2026-04-27 | Engine: Python 3.11 + statsmodels 0.14.6 | HC1 robust SE

## 1. Variable Definitions

| Construct | Variable | WBES Items | Construction | Coverage |
|-----------|----------|------------|--------------|----------|
| TCI-thin | `TCI_thin` | e6 (foreign tech) + b8 (quality cert) | mean(binary, binary) | ALL 6 waves |
| TCI-full | `TCI_full` | e6 + h1 (product innov) + h8 (R&D) + b8 | mean(4 binary) | 5 waves (not VNM 2009) |
| DAI-thin | `DAI_thin` | c22b (website) + e6 (foreign tech) | mean(binary, binary) | ALL 6 waves |
| DAI-rich | `DAI_rich` | c22b + k33/100 (e-payment) + k38/100 (e-pay suppliers) | mean(binary, cont, cont) | 3 B-READY waves only |
| FSTS | `export_pct/100` | 100 - d3a (domestic sales %) | proportion 0-1 | ALL 6 waves |
| Productivity | `ln_labor_prod` | ln(d2/l1) = ln(sales/employees) | natural log | ALL 6 waves |

### Variable mapping for legacy datasets

| Standard var | VNM 2009 | VNM 2015 | VNM 2023 | CHN 2012 | CHN 2024 | SGP 2023 |
|---|---|---|---|---|---|---|
| h1 (product innov) | MISSING | h1 | h1 | CNo1 | h1 | h1 |
| h8 (R&D spending) | MISSING | h8 (continuous, recoded >0=1) | h8 | CNo3 | h8 | h8 |
| e6 (foreign tech) | e6 | e6 | e6 | e6 | e6 | e6 |
| b8 (quality cert) | b8 | b8 | b8 | b8 | b8 | b8 |
| c22b (website) | c22b | c22b | c22b | c22b | c22b | c22b |
| k33 (e-payment %) | MISSING | MISSING | k33 | MISSING | k33 | k33 |

## 2. Sample Handling

- Missing values: WBES codes -9 (don't know), -7 (refused), -99 recoded to NaN
- Binary recoding: 1=Yes -> 1.0, 2=No -> 0.0
- No winsorization applied
- No sector restrictions
- Listwise deletion within each model (statsmodels OLS default)
- manager_exp DROPPED from controls due to multicollinearity with ln_empl (r=0.91, VIF=5.85/6.11)

### Controls

| Variable | WBES item | Description |
|----------|-----------|-------------|
| ln_empl | ln(l1) | Log of total employees |
| firm_age | a7 | Years of operation |
| foreign_dummy | b2b > 0 | Binary: any foreign ownership |
| wave dummies | — | P4: wave_2015, wave_2023. P5: wave_2024 |

## 3. Sample Sizes

| Dataset | Raw N | Analytic N (M2) | Exporters | Exporter % |
|---------|-------|-----------------|-----------|------------|
| SGP 2023 | 623 | 623 | 111 | 17.8% |
| VNM 2009 | 1,053 | 996 | 369 | 37.1% |
| VNM 2015 | 996 | 968 | 281 | 29.1% |
| VNM 2023 | 1,028 | 1,014 | 241 | 23.8% |
| CHN 2012 | 2,700 | 2,684 | 647 | 24.0% |
| CHN 2024 | 2,189 | 1,944 | 448 | 20.6% |
| **Total** | **8,589** | **8,229** | **2,097** | **25.5%** |

## 4. Paper-Specific Specifications

### P3 (Singapore / target: IBR or MIR)
- TCI: **TCI_full** (e6 + h1 + h8 + b8)
- DAI: **DAI_rich** (c22b + k33/100 + k38/100)
- Controls: ln_empl, firm_age, foreign_dummy
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

## 5. Verified Results

### 5.1 Inverted-U I-P Relationship

| Wave | β(FSTS) | β(FSTS²) | p(FSTS²) | TP | LM p | LM Status |
|------|---------|----------|----------|----|------|-----------|
| SGP 2023 | 4.018*** | -2.630** | .002 | **76.4%** | .137 | NOT CONFIRMED |
| CHN 2012 | 1.200*** | -1.284*** | .000 | **46.7%** | .001 | CONFIRMED |
| CHN 2024 | 1.301** | -1.344** | .008 | **48.4%** | .011 | CONFIRMED |
| CHN pooled | 1.102*** | -1.160*** | .000 | **47.5%** | .000 | CONFIRMED |
| VNM 2009 | 1.247† | -1.854** | .006 | **33.6%** | .028 | CONFIRMED |
| VNM 2015 | 1.719** | -2.478*** | .000 | **34.7%** | .003 | CONFIRMED |
| VNM 2023 | 1.641* | -2.300** | .001 | **35.7%** | .010 | CONFIRMED |
| VNM pooled | 1.189** | -1.899*** | .000 | **31.3%** | .002 | CONFIRMED |

TP gradient: VNM ~34% < CHN ~47% < SGP ~76%

### 5.2 TCI Direct Effect (from M3)

| Wave | TCI var | β | SE | p | Sig |
|------|---------|---|----|----|-----|
| SGP 2023 | TCI_full | 0.839 | 0.201 | <.001 | *** |
| CHN 2012 | TCI_full | 0.458 | 0.072 | <.001 | *** |
| CHN 2024 | TCI_full | 0.936 | 0.106 | <.001 | *** |
| CHN pooled | TCI_full | 0.529 | 0.061 | <.001 | *** |
| VNM 2009 | TCI_thin | 0.905 | 0.144 | <.001 | *** |
| VNM 2015 | TCI_thin | 0.352 | 0.159 | .027 | * |
| VNM 2023 | TCI_thin | 0.656 | 0.173 | <.001 | *** |
| VNM pooled | TCI_thin | 0.671 | 0.098 | <.001 | *** |

**UNIVERSAL: Significant in 8/8 specifications.**

### 5.3 TCI Moderation (from M4)

All 8 specifications: FSTS x TCI and FSTS² x TCI **NOT SIGNIFICANT** (all p > .17).
TCI moderation is NULL across all country-waves — consistent NLB-FSA prediction.

### 5.4 DAI Direct Effect (from M5)

| Wave | DAI var | β | SE | p | Sig |
|------|---------|---|----|----|-----|
| SGP 2023 | DAI_rich | 0.342 | 0.144 | .018 | * |
| CHN 2012 | DAI_thin | 0.139 | 0.059 | .018 | * |
| CHN 2024 | DAI_thin | 0.506 | 0.117 | <.001 | *** |
| CHN pooled | DAI_thin | -0.013 | 0.051 | .805 | ns |
| VNM 2009 | DAI_thin | 0.691 | 0.106 | <.001 | *** |
| VNM 2015 | DAI_thin | 0.196 | 0.121 | .105 | ns |
| VNM 2023 | DAI_thin | 0.552 | 0.162 | .001 | *** |
| VNM pooled | DAI_thin | 0.522 | 0.076 | <.001 | *** |

**Significant 6/8 standalone, but loses significance when combined with TCI in some specs.**

### 5.5 DAI Moderation (from M8)

| Wave | FSTS x DAI β | p | FSTS² x DAI β | p | Pattern |
|------|-------------|---|---------------|---|---------|
| SGP 2023 | **-8.058** | **.003** | **13.644** | **<.001** | **U-SHAPE** |
| CHN 2012 | -0.774 | .401 | 1.091 | .311 | NULL |
| CHN 2024 | 1.580 | .336 | -2.513 | .205 | NULL |
| CHN pooled | -0.672 | .401 | 0.453 | .630 | NULL |
| VNM 2009 | -2.619 | .373 | 2.492 | .416 | NULL |
| VNM 2015 | -1.793 | .435 | 1.516 | .542 | NULL |
| VNM 2023 | -3.388 | .074† | 2.808 | .145 | NULL(†) |
| VNM pooled | -1.144 | .421 | 1.169 | .434 | NULL |

**DAI U-shape moderation is SINGAPORE-ONLY.** VNM 2023 shows marginal FSTS x DAI (p=.074) but FSTS² x DAI not significant — insufficient for U-shape claim.

## 6. Effect Sizes (Cohen's f², P3 Singapore)

| Effect | ΔR² | f² | Size |
|--------|-----|----|----|
| FSTS + FSTS² (I-P) | 0.1443 | 0.178 | Medium |
| TCI (direct) | 0.0229 | 0.029 | Small |
| DAI (direct) | 0.0065 | 0.008 | Negligible |
| TCI + DAI (joint) | 0.0250 | 0.032 | Small |
| All interactions | 0.0136 | 0.018 | Negligible |

## 7. Key Methodological Decisions

### 7.1 Why manager_exp dropped
- ln_empl and manager_exp: r = 0.91 in SGP 2023
- VIF before: ln_empl = 6.11, manager_exp = 5.85
- VIF after dropping manager_exp: ln_empl = 1.13
- Results stable: TCI β changes <0.003, TP changes <0.2pp

### 7.2 Why TCI_thin for P4
- VNM 2009 standardized dataset LACKS h1, h5, h8 (innovation module not in standardized questionnaire)
- CHN 2012 has innovation items under country-specific prefix (CNo1, CNo3)
- For P4 cross-wave panel: TCI_thin (e6 + b8) is the ONLY consistent 2-item index
- Robustness: VNM 2023 separately run with TCI_full shows same pattern

### 7.3 FSTS/FSTS² VIF
- FSTS and FSTS² inherently collinear (VIF 10-42 depending on sample)
- Standard for quadratic specifications — mean-centering reduces to VIF ~7
- Mean-centered robustness confirms: all substantive results unchanged

### 7.4 Lind-Mehlum for Singapore
- FSTS² significant (p=.002) but LM test p=.137
- Reason: only 20 firms (3.2%) have FSTS > 75% — right tail too thin
- Right-side slope = -1.222 (t=-1.075, p=.141) — negative but not significant
- Frame: "consistent with inverted-U shape; right-side slope lacks statistical power" per Haans, Pieters & He (2016, SMJ)

## 8. Cross-Paper Narrative

### Main finding: TCI capability complementarity (universal)
TCI has a direct productivity premium in ALL 6 country-waves (β range: 0.35–0.94, all p<.05). TCI does NOT moderate the I-P curve shape. This is consistent with Lall (1992) technological capability theory and Rugman-Verbeke NLB-FSA logic: capability raises the productivity LEVEL regardless of internationalization stage.

### Secondary finding: TP gradient
Turning point increases with development: VNM ~34% → CHN ~47% → SGP ~76%. Firms in more institutionally developed economies can internationalize further before hitting diminishing returns.

### Exploratory finding: DAI moderation (Singapore-specific)
DAI U-shape moderation significant only in SGP (advanced digital-frontier economy). In developing economies (VNM, CHN), DAI does not alter I-P curve shape. Interpretation: coordination-cost channel (Contractor et al. 2003) is activated only when digital infrastructure is sufficiently mature to create integration burdens at moderate internationalization.

### Temporal evolution
- TCI effect strengthens over time in China (0.458→0.936)
- DAI direct effect strengthens over time in China (0.139→0.506)
- Vietnam shows non-monotonic DAI pattern (0.691→0.196→0.552) — possible productivity J-curve trough in 2015
