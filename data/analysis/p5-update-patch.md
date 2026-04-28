# P5 APJM Manuscript Update Patch — CNo3 Fix

**Date**: 28 April 2026
**Applies to**: P5_APJM_SUBMIT_FINAL_CORRECTED.docx
**Reason**: CHN 2012 h8 variable was mapped to CNo8 (computer use) instead of CNo3 (R&D spending). All CHN 2012 TCI coefficients affected.

---

## A. Table 4 — Replace CHN 2012 column

### CHN 2012 (N changes from ~2,684 to 1,613 for TCI models due to n_valid≥3 filter)

| Model | Variable | OLD (CNo8 bug) | NEW (CNo3 correct) |
|-------|----------|----------------|---------------------|
| M2 | fsts | — | 2.057*** (0.379) |
| M2 | fsts_sq | — | −2.082*** (0.434) |
| M2 | N | 2,684 | 2,612 |
| M2 | R² | — | 0.021 |
| M2 | TP | 46.7% | **49.4%** |
| M5 | tci_full_z | 0.458*** | **0.171*** (0.027)** |
| M5 | N | ~2,684 | **1,613** |
| M5 | R² | — | 0.045 |
| M6 | dai_thin_z | 0.139* | **0.050* (0.022)** |
| M7 | tci_full_z | — | 0.165*** (0.028) |
| M7 | dai_thin_z | — | 0.028 ns (0.025) |
| M8 | tci_full_z | — | 0.164*** (0.028) |
| M8 | dai_thin_z | — | 0.034 ns (0.028) |
| M8 | fsts×dai | — | −0.523 ns (0.357) |
| M8 | fsts²×dai | — | 0.645† (0.379) |

### CHN 2024 (unchanged — CNo3 fix only affects 2012)

| Model | Variable | Value |
|-------|----------|-------|
| M5 | tci_full_z | 0.291*** (0.032) |
| M5 | N | 1,920 |
| M6 | dai_thin_z | 0.141*** (0.034) |
| M8 | tci_full_z | 0.271*** (0.035) |
| M8 | dai_thin_z | 0.084* (0.038) |

### CHN Pooled

| Model | Variable | Value |
|-------|----------|-------|
| M2 | TP | **48.8%** |
| M2 | LM p | **<.001 ✓** |
| M5 | tci_full_z | **0.238*** (0.022)** |
| M6 | dai_thin_z | **0.085*** (0.021)** |

---

## B. Paternoster z-tests — Replace in Results §4.4

### OLD values (with CNo8 bug):
- TCI: z = ?, p = ?
- DAI: z = ?, p = ?

### NEW values (CNo3 correct):

| Comparison | CHN 2012 β (SE) | CHN 2024 β (SE) | z | p |
|------------|-----------------|-----------------|---|---|
| **TCI direct** | 0.171 (0.027) | 0.291 (0.032) | **−2.845** | **.004**** |
| **DAI direct** | 0.050 (0.022) | 0.141 (0.034) | **−2.219** | **.027*** |
| FSTS linear | 2.057 (0.379) | 1.498 (0.578) | 0.808 | .419 ns |
| FSTS² quadratic | −2.082 (0.434) | −1.587 (0.712) | −0.594 | .553 ns |

**Interpretation**: Both TCI and DAI direct effects **strengthened significantly** from 2012 to 2024 (Paternoster z < −2, p < .05). The I-P curve shape (FSTS, FSTS²) did **not** change significantly between waves.

---

## C. Results Section Text Changes

### §4.2 TCI Direct Effect — REPLACE paragraph:

> OLD: "TCI exerts a strong direct effect on labor productivity in both waves (β₂₀₁₂ = 0.458, p < .001; β₂₀₂₄ = 0.936, p < .001)"

> NEW: "TCI exerts a significant direct effect on labor productivity in both waves (β_z,2012 = 0.171, p < .001; β_z,2024 = 0.291, p < .001). The z-standardized coefficients indicate that a one-standard-deviation increase in TCI is associated with a 17.1% and 29.1% increase in labor productivity in 2012 and 2024, respectively."

### §4.4 Temporal Evolution — REPLACE paragraph:

> OLD: "The Paternoster z-test confirms that TCI's direct effect nearly doubled from 2012 to 2024..."

> NEW: "The Paternoster z-test confirms that TCI's direct effect strengthened significantly from 2012 to 2024 (z = −2.845, p = .004), with the standardized coefficient increasing from β_z = 0.171 to β_z = 0.291 — a 70% increase. Similarly, DAI's direct effect strengthened significantly (z = −2.219, p = .027), rising from β_z = 0.050 to β_z = 0.141 — a 2.8× increase. These temporal shifts support the productivity J-curve hypothesis (Brynjolfsson et al. 2021): digital and technological capabilities generate increasing returns as the institutional environment matures."

### §4.1 Inverted-U — REPLACE TP values:

> OLD: "turning point at approximately 47%"

> NEW: "turning point at approximately 49% in 2012 and 47% in 2024 (pooled TP = 48.8%), with Lind-Mehlum tests confirming the inverted-U shape in both waves and the pooled sample (all p < .03)"

---

## D. Discussion Section Changes

### §5.1 TCI Capability Complementarity:

> REPLACE any reference to "TCI β = 0.458" with "TCI β_z = 0.171"
> REPLACE any reference to "TCI β = 0.936" with "TCI β_z = 0.291"
> REPLACE "TCI effect doubles" with "TCI effect increases by 70%"

### §5.2 Digital Dividend:

> REPLACE "DAI β = 0.139" with "DAI β_z = 0.050"
> REPLACE "DAI β = 0.506" with "DAI β_z = 0.141"
> REPLACE "3.6× increase" with "2.8× increase"

---

## E. Abstract — REPLACE key numbers:

> OLD: "TCI direct effect significant in both waves (β₂₀₁₂ = 0.458, β₂₀₂₄ = 0.936)"

> NEW: "TCI direct effect significant in both waves (β_z = 0.171 and 0.291, p < .001), strengthening 70% from 2012 to 2024 (Paternoster z = −2.85, p = .004)"

---

## F. Sample Size Note

CHN 2012 N drops from ~2,684 to **1,613** for TCI models because `build_tci_full` now requires ≥3 of 4 items non-missing. With CNo3 (R&D spending binary, N_valid = 1,679) instead of CNo8 (computer use %, N_valid = 2,683), more firms have missing R&D data → TCI_full computed for fewer firms.

Add footnote to Table 4: "N for models including TCI is lower in 2012 (N = 1,613) because R&D spending (CNo3) was asked only to firms that reported innovation activities, following the WBES skip pattern."

---

## G. Grand Comparison Table (if included in dissertation chapter)

| | SGP 23 | CHN 12 | CHN 24 | VNM 09 | VNM 15 | VNM 23 |
|---|---|---|---|---|---|---|
| TP | 83.0% | 49.4% | 47.2% | 36.2% | 36.5% | 33.8% |
| LM p | .301 | .000 ✓ | .029 ✓ | .060 ~ | .017 ✓ | .029 ✓ |
| TCI β_z | .200*** | .171*** | .291*** | .317*** | .047 ns | .180*** |
| DAI β_z | .114** | .050* | .141*** | .251*** | .022 ns | .176*** |

---

## Pre-Submission Checklist

- [ ] Table 4 CHN 2012 column updated with CNo3 numbers
- [ ] Table 4 footnote added re: N=1,613 for TCI models
- [ ] Paternoster z-tests updated (TCI z=−2.845, DAI z=−2.219)
- [ ] Abstract numbers updated
- [ ] Results §4.2 TCI paragraph updated
- [ ] Results §4.4 temporal evolution paragraph updated
- [ ] Discussion §5.1 TCI numbers updated
- [ ] Discussion §5.2 DAI numbers updated
- [ ] TP values updated (49.4%, 47.2%, 48.8%)
- [ ] All "0.458" references replaced with "0.171"
- [ ] All "0.936" references replaced with "0.291"
