# P3 MIR Skeleton Patch — Align v3 with Production Spec Numbers

**Applies to**: P3_v3_MIR_Skeleton.docx
**Date**: 28 April 2026
**Reason**: Skeleton v3 contains numbers from session-1 (d3a, a7, raw scale). Must update to production spec (d3c, b5, z-standardized).

---

## FIND-AND-REPLACE LIST

### Abstract

| Find | Replace with |
|------|-------------|
| `negative at 3% < FSTS < 56%` | `negative between 7% and 35% of export intensity` |
| `DAI joint p = .024` | `DAI moderation joint F(2, 607) = 3.38, p = .035` |
| `turning point at approximately 76%` (if present) | `turning point at approximately 83%` |
| `Lind-Mehlum p = .141` (if present) | `Lind-Mehlum p = .301 (not significant at conventional levels)` |

### §1 Introduction

| Find | Replace with |
|------|-------------|
| Any reference to `TP = 76%` | `TP = 83%` |
| Any reference to `inverted-U confirmed` | `primarily monotonic positive relationship with mild quadratic curvature (Lind-Mehlum p = .301)` |

### §4.1 Results — I-P Relationship

| Find | Replace with |
|------|-------------|
| `β_FSTS = 3.995` or `4.018` | `β_FSTS = 3.490*** (SE = 0.903)` |
| `β_FSTS² = -2.609` or `-2.630` | `β_FSTS² = −2.103† (SE = 1.087, p = .053)` |
| `turning point of 76.4%` or `76.6%` | `turning point of 83.0%` |
| `Lind-Mehlum p = .141` or `.137` | `Lind-Mehlum p = .301` |
| `inverted-U is confirmed` | `the quadratic term is marginally significant (p = .053), suggesting mild curvature rather than a confirmed inverted-U. Following Haans, Pieters and He (2016), we characterize the I-P relationship as primarily monotonic positive with a plateau at high export intensities` |

### §4.2 Results — TCI Direct Effect

| Find | Replace with |
|------|-------------|
| `β = 0.839***` or `0.836***` | `β_z = 0.200*** (SE = 0.042, p < .001)` |
| `TCI raises productivity by 83.9%` | `a one-standard-deviation increase in TCI is associated with a 0.200 unit increase in ln(labor productivity)` |
| `R² increases from .180 to .202` | `R² increases from .162 to .191` |

### §4.3 Results — TCI Moderation (null)

| Find | Replace with |
|------|-------------|
| `FSTS × TCI p = .67` or similar | `FSTS × TCI: β_z = 0.650, p = .399; FSTS² × TCI: β_z = −0.944, p = .364` |

### §4.4 Results — DAI Moderation (KEY SECTION)

**REPLACE ENTIRE §4.4 with:**

> DAI exerts a significant direct effect on labor productivity (β_z = 0.114, SE = 0.038, p = .002), indicating that a one-standard-deviation increase in digital adoption is associated with an 11.4% increase in productivity. When both TCI and DAI are included (Model 5), the DAI coefficient attenuates to marginal significance (β_z = 0.073, p = .057), suggesting partial overlap with TCI's explanatory power.
>
> The DAI moderation specification (Model 6) reveals a significant quadratic interaction: FSTS² × DAI (β_z = 2.869, SE = 1.284, p = .025), while the linear interaction FSTS × DAI is not individually significant (β_z = −1.181, SE = 0.913, p = .196). The joint F-test for the two DAI interaction terms is significant (F(2, 607) = 3.38, p = .035), supporting H4.
>
> In the full model (Model 7), TCI remains strongly significant (β_z = 0.186, p < .001) while the DAI quadratic moderation term is also significant (FSTS² × DAI: β_z = 3.023, SE = 1.309, p = .021). The marginal effect of DAI varies across export intensity levels (Table 4; Figure 1): it is marginally positive for non-exporters (β = +0.073, p = .064), turns mildly negative in the 7–35% FSTS range (trough at FSTS ≈ 21%, β ≈ −0.06, not individually significant), and becomes significantly positive for high-intensity exporters (FSTS = 70%: β = +0.660, p = .041; FSTS = 100%: β = +1.818, p = .009).
>
> The coordination trough is shallow and not individually significant at any FSTS level within the 7–35% range. The substantive interpretation therefore emphasizes the scale-economy tail: digital adoption generates significant productivity gains primarily for firms with export intensities exceeding 70%, where digital infrastructure amortization across multiple markets yields economies of scale (Banalieva & Dhanaraj, 2019).

### §4.5 Results — Effect Sizes

| Find | Replace with |
|------|-------------|
| `Cohen's f² = 0.029 (TCI)` | `Cohen's f² = 0.036 (TCI direct, Models 2→3)` — verify from R² difference |
| `Cohen's f² = 0.018 (DAI mod)` | `Cohen's f² = 0.018 (DAI moderation, Models 5→6)` — confirm |

### §5.1 Discussion — DAI Mechanism

| Find | Replace with |
|------|-------------|
| `significant negative effect at moderate internationalization (FSTS 15–30%)` | `a shallow, non-significant coordination trough at moderate internationalization (FSTS 7–35%), followed by significant positive scale economies at high export intensity (FSTS > 70%)` |
| `78 firms (12.5%) in coordination-cost zone` | recount: firms with 7% < FSTS < 35% |
| `burden at intermediate intensities` | `the moderation pattern is driven primarily by the scale-economy tail rather than the coordination trough. This suggests that DAI's primary channel in Singapore is enabling high-intensity exporters to leverage digital infrastructure across markets, rather than penalizing moderate exporters` |

### §5.3 Discussion — Cross-Paper Hook

| Find | Replace with |
|------|-------------|
| `TP gradient: VNM 34% < CHN 47% < SGP 76%` | `TP gradient: VNM ≈ 34% < CHN ≈ 48% < SGP ≈ 83%` |

### §6 Limitations

| Find | Replace with |
|------|-------------|
| `Lind-Mehlum p = .141 (borderline)` | `Lind-Mehlum p = .301 (not significant). The I-P relationship in Singapore is better characterized as monotonic positive with mild curvature than as a confirmed inverted-U` |
| `only 3.2% of firms have FSTS > 75%` | `only 18% of firms are exporters (FSTS > 0), and merely 3% exceed FSTS = 50%. This thin right tail limits power for the inverted-U test and for evaluating marginal effects at high export intensities` |

---

## NUMBERS NOT TO CHANGE (already correct in v3)

- N = 623 ✓
- 4 hypotheses structure ✓
- TCI moderation null ✓
- Reference list ✓
- Methods section composite construction ✓ (already describes z-standardization)

---

## PRE-SUBMISSION CHECKLIST

- [ ] All `76.4%` or `76.6%` TP references → `83.0%`
- [ ] All `Lind-Mehlum .141` → `.301`
- [ ] All raw-scale β (0.839, −8.104, +13.695) → z-scaled β (0.200, −1.279, +3.023)
- [ ] §4.4 replaced with full paragraph above
- [ ] Abstract zero-crossings: 3%/56% → 7%/35%
- [ ] Joint F: 4.37/.024 → 3.38/.035
- [ ] Tables 1-4 pasted from chat output (tab-delimited)
- [ ] Figure 1 (marginal effects) + Figure 2 (I-P curve) inserted
- [ ] TP gradient updated: 76% → 83%
- [ ] Discussion §5.1 trough language weakened (shallow, ns)
