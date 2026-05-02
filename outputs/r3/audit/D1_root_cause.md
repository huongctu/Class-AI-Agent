# D1 Root-Cause Diagnosis — Table 3 Mismatch

**Date:** 2026-05-02
**Reviewer issue:** Manuscript Table 3 baseline row reports values that do
not match Manuscript Table 2 Model M8 despite both being labeled as the
same specification on the same N=617 sample.

---

## What the reviewer flagged

Manuscript Table 3, baseline row:
- TCI β_z = **0.187***
- FSTS² × DAI = **2.972***
- Adj. R² = **0.192**

Manuscript Table 2, Model M8:
- TCI β_z = **0.153***
- FSTS² × DAI = **3.119***
- Adj. R² = **0.196**

Both rows claim N = 617 and the same TCI_full + DAI_rich specification.

---

## Audit findings

### 1. Canonical M8 (locked spec) reproduces Table 2 M8 exactly.

`tools/r3/00_canonical_m8.py` re-estimates M8 from the raw `.dta` using
the locked specification (4-component TCI, 3-component DAI with k33/k38
single-missing imputation, HC1 robust SE, broad-sector NACE buckets,
1/99 winsorized ln-labor-productivity). Result:

| Term | Coefficient | SE | p |
|---|---|---|---|
| TCI | 0.1528 | 0.0412 | <0.001 |
| DAI | 0.0188 | 0.0454 | 0.679 |
| FSTS² × DAI | 3.1185 | 1.1236 | 0.006 |
| **N** | **617** | | |
| **Adj. R²** | **0.196** | | |

→ Matches Table 2 M8 exactly. Canonical M8 is therefore the single source
  of truth for all subsequent R3 work.

### 2. No alternative specification reproduces the Table 3 baseline row.

`tools/r3/01_diagnose_table3_baseline.py` and
`tools/r3/03_diagnose_tci_spec.py` test ten plausible alternative specs:

- DAI variants (drop k33, drop k38, drop c22b)
- TCI variants (drop one of b8/e6/h1/h8)
- TCI standardization variants (z-then-avg-then-z; simple avg then z;
  z-then-avg only; sum-of-z then z)
- Robust-SE variants (HC0, HC1, HC3)

Closest match (V2_simple_avg_then_z) yields TCI=0.159 and FSTS²×DAI=3.110,
which still disagrees with Table 3 baseline (0.187 / 2.972). No spec
reproduces the joint triple (0.187, 2.972, 0.192).

### 3. All six rows of Table 3 contain transcription errors.

`tools/r3/02_audit_table3.py` re-estimates each Table 3 row from raw data:

| Row | Spec | N (rep/man) | TCI (rep/man) | FSTS²×DAI (rep/man) | AdjR² (rep/man) |
|---|---|---|---|---|---|
| Baseline | TCI_full + DAI_rich | 617/617 ✓ | 0.153/0.187 ✗ | 3.119/2.972 ✗ | 0.196/0.192 ✓ |
| R1 | DAI_thin (c22b only) | 623/623 ✓ | 0.180/0.211 ✗ | 1.552/1.563 ✓ | 0.188/0.184 ✓ |
| R2 | TCI_thin (e6 + b8) | 617/617 ✓ | 0.159/0.171 ✗ | 2.930/2.749 ✗ | 0.199/0.188 ✗ |
| R3 | Excl micro-firms (<10 empl) | 464/464 ✓ | 0.170/0.218 ✗ | 3.521/3.535 ✓ | 0.219/0.226 ✗ |
| R4 | SMEs only (≤200 empl) | 595/595 ✓ | 0.156/0.180 ✗ | 3.505/3.483 ✓ | 0.199/0.197 ✓ |
| R5 | Exporters only (FSTS > 0) | 84/84 ✓ | 0.130/0.143 ✗ | **2.821**/1.308 ✗ | 0.165/0.140 ✗ |

Ns are correct in all six rows. Coefficients deviate systematically:
- TCI is consistently **higher** in the manuscript than canonical (0.012 to 0.048).
- The R5 (exporters-only) FSTS²×DAI is off by **+1.513** (manuscript reports 1.308 but canonical is 2.821) — this is the single largest deviation.

### 4. Most plausible explanation

The Table 3 numbers appear to be a **stale snapshot from an earlier
manuscript draft** that used a slightly different TCI or sample-build
pipeline. The subsequent revision updated Table 2 M8 to the locked spec
but did not propagate the change to Table 3, leaving Table 3 with stale
coefficients across all rows.

This matches the reviewer's observation that "the baseline row in Table
3 appears intended to represent the same full specification as Model
M8" yet does not match.

---

## Recommended fix

**Replace the entire Table 3 with the canonical re-estimation
(corrected six-row block produced by `02_audit_table3.py`).**

Corrected Table 3:

| Specification | N | TCI β_z | FSTS² × DAI | Joint F (p) | Adj. R² |
|---|---|---|---|---|---|
| Baseline (TCI_full + DAI_rich) | 617 | +0.153*** | +3.119** | 4.56 (.011) | 0.196 |
| R1: DAI_thin (website c22b only) | 623 | +0.180*** | +1.552 | 4.01 (.019) | 0.188 |
| R2: TCI_thin (e6 + b8) | 617 | +0.159*** | +2.930** | 4.27 (.014) | 0.199 |
| R3: Excl micro-firms (<10 empl) | 464 | +0.170*** | +3.521** | 4.61 (.010) | 0.219 |
| R4: SMEs only (≤200 empl) | 595 | +0.156*** | +3.505** | 5.30 (.005) | 0.199 |
| R5: Exporters only (FSTS > 0) | 84 | +0.130 | +2.821 | 6.32 (.003) | 0.165 |

Significance stars: † p<.10, * p<.05, ** p<.01, *** p<.001.

### Implication for narrative (R5 exporters-only row in particular)

The corrected R5 row (FSTS²×DAI = +2.821, joint F = 6.32, p = .003)
**strengthens** rather than weakens the moderation finding within the
exporter subsample. The previously reported R5 (FSTS²×DAI = +1.308,
joint F = 3.18, p = .048) suggested the result was attenuated when
restricting to exporters. The canonical re-estimation shows the
opposite: the moderation pattern is stronger and more significant
within the exporter subsample.

This affects how Section 7 caveats should be worded. The reviewer's
warning that R5 "illustrates how the dynamics change when non-exporters
are excluded" relied on the (incorrect) attenuation. With the corrected
numbers, the dynamic is **reinforcement, not attenuation**.

This finding will also be central to Phase 1's extensive–intensive
split design: the intensive-margin (exporter-only) test now has a
stronger basis.

---

## Provenance

- Raw data: `data/raw/Singapore2023fulldata.dta` (WBES Singapore 2023, 623 firms)
- Locked spec: `tools/r3/00_canonical_m8.py`
- Diagnosis: `tools/r3/01_diagnose_table3_baseline.py`,
  `tools/r3/03_diagnose_tci_spec.py`
- Full audit: `tools/r3/02_audit_table3.py`
- Audit JSON: `outputs/r3/audit/m8_canonical.json`,
  `outputs/r3/audit/D1_diagnosis.json`,
  `outputs/r3/audit/table3_audit.json`
