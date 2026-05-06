# P5 China — Replicated Results Summary

All estimates from the Python pipeline on the **full WBES private-firm frame** (matches manuscript v1.2). Standard errors in parentheses (HC1 robust for wave-specific; cluster on `idstd` for pooled).

## M2 — Main inverted-U threshold model

| | 2012 (N=2,610) | 2024 (N=1,934) | Pooled (N=4,544) |
|---|---|---|---|
| Intercept | +12.7925 (0.0896) | +12.3760 (0.0841) | +12.2955 (0.0656) |
| FSTS | +2.0654 (0.3790) | +1.4980 (0.5783) | +1.7843 (0.3195) |
| FSTSsq | −2.0919 (0.4345) | −1.5873 (0.7117) | −1.8289 (0.3753) |
| lnEmp | −0.1023 (0.0229) | +0.1180 (0.0234) | +0.0047 (0.0164) |
| firmage | +0.0076 (0.0039) | +0.0124 (0.0030) | +0.0118 (0.0023) |
| foreigndummy | +0.1120 (0.0947) | +0.2566 (0.1186) | +0.2172 (0.0742) |

## Turning points (delta-method 95% CI)

| Sample | Turning point | 95% CI | N |
|---|---|---|---|
| 2012 | **49.37 %** | [43.17 %, 55.57 %] | 2,610 |
| 2024 | **47.19 %** | [34.46 %, 59.92 %] | 1,934 |
| Pooled | **48.78 %** | [42.65 %, 54.91 %] | 4,544 |

v1.2 reports 49.4 / 47.6 / 48.9 — replication matches within ≤0.4 pp.

## Paternoster z-test — cross-wave coefficient equality on M2

| Coefficient | b (2012) | b (2024) | z | p | Verdict |
|---|---|---|---|---|---|
| FSTS | +2.065 (0.379) | +1.498 (0.578) | +0.821 | **0.412** | Equality NOT rejected → **stable** |
| FSTSsq | −2.092 (0.435) | −1.587 (0.712) | −0.605 | **0.545** | Equality NOT rejected → **stable** |

Both p-values > 0.10 → fail to reject equality → **threshold-stability claim verified**.

## Files in this directory

- `results_coefs.csv` — long-format coefficients for M1–M8 across 3 samples (51 rows)
- `M2_table.csv` — wide-format M2 main threshold table
- `summary.md` — this file
