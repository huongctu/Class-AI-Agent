# P3 Upgrade Plan: From MIR Submission to Q1 Publication

**Date**: 29 April 2026
**Source**: 16 strategy PDFs + 2 rounds Refine AI + Manuscript REVISED-17

---

## Current Status

P3 manuscript REVISED-17 is **near submit-ready** for MIR with:
- Sector FE included
- 10 Refine AI R2 critiques addressed
- Associational framing throughout
- ~7,600 words

## 3 Upgrade Paths (from 16 strategy documents)

### Path 1: Identification Strategy (Priority: HIGH for R&R)

**Problem**: Cross-sectional OLS cannot establish causality. Reviewers at JIBS/JWB/MIR will demand stronger identification.

**Options ranked by feasibility**:

| Option | Data needed | Feasibility | Impact |
|--------|------------|-------------|--------|
| **A. Heckman two-stage** | Current data | **HIGH** — can do now | Controls selection into exporting |
| **B. PSM (propensity score matching)** | Current data | **HIGH** | Match exporters vs non-exporters on observables |
| **C. IV (instrumental variables)** | External data (broadband rollout, e-gov index) | MEDIUM | Strongest causal claim if valid instruments found |
| **D. Panel DiD** | WBES VNM 2009/2015/2023 | MEDIUM — data exists for P4 | Exploit WTO/digital policy shocks |
| **E. WBES × Orbis linkage** | Orbis subscription | LOW — anonymization barrier | Firm-level financials + IT spending |

**Recommended for R&R**: Option A (Heckman) + B (PSM) — both feasible with current Singapore data.

### Path 2: DAI Measurement Upgrade (Priority: MEDIUM — for dissertation defense)

**Problem**: DAI = website + e-payment = Tier 1-2 digitalization only. Cannot claim "digital capability" (Tier 3-4).

**Current defense** (already in manuscript): "We deliberately label our construct 'digital adoption' rather than 'digital capability' to match the content domain of WBES indicators" — this is honest and defensible.

**Upgrade for future papers**:

| Tier | Indicators | Source | Available? |
|------|-----------|--------|-----------|
| 1. Infrastructure | Website, broadband | WBES c22b, c36 | ✓ Current |
| 2. Transactions | E-payment, e-tax | WBES k33, j37 | ✓ Current |
| 3. Integration | ERP, CRM, SCM software | FAT survey / Orbis | ✗ Need new data |
| 4. Dynamic capability | AI, cloud, platform business | Custom survey | ✗ Need fieldwork |

**Action**: In §6 Limitations, frame Tier 1-2 as "foundation" and propose Tier 3-4 for future research.

### Path 3: Multi-Country Comparative Design (Priority: HIGH — dissertation centerpiece)

**Problem**: Single-country design cannot prove "digital-frontier" institutional effect.

**Solution already in hand**: P3 (SGP) + P4 (VNM) + P5 (CHN) = 3-country evidence.

**Evidence for dissertation integration chapter**:

| Country | TP | Digital maturity | DAI moderation |
|---------|-----|-----------------|---------------|
| Vietnam | 34-36% | Low-transitional | NULL |
| China | 47-49% | Transitional-mature | NULL |
| Singapore | 89% | Frontier | Significant (scale-tail) |

**Cross-country TP gradient** (34% → 48% → 89%) is the strongest empirical evidence that digital institutional maturity raises the optimal export threshold.

**Action**: Dissertation Chapter 5 (Integration) should foreground this gradient as the cross-paper finding.

---

## Immediate Actions for P3 MIR

### Before Submit (this week)

1. ☐ Sync all Table 2/3/4 numbers with text (Refine AI R2 #1)
2. ☐ Fix Figure 2 ↔ 3 swap (Refine AI R2 #7)
3. ☐ Fix Figure 1 moderation arrows (Refine AI R2 #5)
4. ☐ TP = 89% uncentered (Refine AI R2 #3)
5. ☐ Final blinding check
6. ☐ Show thầy Tú → get approval
7. ☐ Submit MIR

### If R&R from MIR

1. Add Heckman two-stage selection model
2. Add PSM matching (exporters vs non-exporters)
3. Add finer sector controls (ISIC 2-digit from a4b_v4)
4. Compute equivalence test for H2 null (TOST procedure)
5. Add within-sector robustness (manufacturing-only, services-only)

### If Desk-Reject → Resubmit to IBR/APJM

1. Apply same R&R upgrades
2. Add cross-country context paragraph citing P4/P5 (as companion papers)
3. Strengthen §5.1 with Heckman-corrected estimates

---

## Dissertation Integration (Chapter 4-5)

### Chapter 4: Three Empirical Studies
- P3 (Singapore): boundary condition in digital frontier
- P4 (Vietnam): temporal evolution across 3 waves
- P5 (China): digital paradox → dividend transition

### Chapter 5: Cross-Paper Synthesis
- **Finding 1**: TCI universal capability complementarity (5/6 waves significant)
- **Finding 2**: TP gradient (VNM 34% < CHN 48% < SGP 89%)
- **Finding 3**: DAI moderation = Singapore-specific boundary condition
- **Finding 4**: DAI direct effect temporal strengthening

### Chapter 6: Limitations & Future Research
- Phase 1 (current): cross-sectional associational evidence
- Phase 2 (proposed): panel DiD with VNM data
- Phase 3 (proposed): WBES × Orbis linkage for Tier 3-4 measurement
- Phase 4 (proposed): multi-country institutional interaction model

---

## Repository Structure for DOI-FP-IN-ASIAN-IN-ASIA

```
DOI-FP-IN-ASIAN-IN-ASIA/
├── data/
│   ├── raw/                    # .dta files (gitignored)
│   ├── analysis/
│   │   ├── pooled_wbes_6waves.csv
│   │   ├── results-p3-singapore.csv
│   │   ├── results-p4-vietnam.csv
│   │   └── results-p5-china.csv
├── scripts/
│   ├── build-pooled-dataset.py
│   ├── analyze-ip-regression.py
│   ├── P3_MIR_Singapore_Analysis.do
│   ├── P4_JWB_Vietnam_Analysis.do
│   └── P5_APJM_China_Analysis.do
├── manuscripts/
│   ├── P3_MIR/
│   ├── P4_JWB/
│   └── P5_APJM/
├── docs/
│   └── cross-paper-consolidation.md
└── README.md
```
