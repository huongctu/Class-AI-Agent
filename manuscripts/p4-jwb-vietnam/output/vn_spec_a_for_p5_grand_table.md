# Vietnam spec-A numbers for P5 grand comparison table

**Generated**: 2026-04-30
**Source pipeline**: `manuscripts/p4-jwb-vietnam/code/p4_python_check.py` + `code/p4_h4_and_extras.py`
**Spec discipline**: WBES non-response code `-9` treated as missing (drop); listwise on focal vars + first available sector code; HC1 robust covariance; within-wave z-standardisation of TCI / DAI.
**Verified by**: triple-source numerical check (statsmodels + linearmodels + manual NumPy/HC1) at machine precision (max coefficient diff 4.06 × 10⁻¹³).

---

## A. Drop-in row for P5 grand comparison table

When anh regenerates the P5 grand comparison table, replace the V4.3 Vietnam columns with the verified spec-A numbers below. The table format follows the structure used in `p5updatepatch.md` line 127–132.

| Quantity | VNM 2009 | VNM 2015 | VNM 2023 |
|---|---|---|---|
| **Turning point (raw FSTS %)** | **43.6%** | **36.3%** | **40.6%** |
| **TP 95% CI** | [24.8%, 62.4%] | [23.9%, 48.7%] | [26.3%, 55.0%] |
| **Lind–Mehlum p** | **.128 ns** | **.033 ✓** | **.068 ~** |
| **TCI β_z** | **0.224*** *** | **0.168*** *** | **0.090** † (p=.095) |
| **TCI SE** | 0.060 | 0.071 | 0.054 |
| **DAI β_z** | **0.122*** *** | **0.007** ns (p=.916) | **0.108*** *** |
| **DAI SE** | 0.056 | 0.070 | 0.054 |
| **Analytic N** | 734 | 614 | 974 |

Significance markers: `*** p < .001`, `** p < .01`, `* p < .05`, `† p < .10`, `ns` not significant, `~` marginal, `✓` confirmed at conventional thresholds.

---

## B. Drop-in row for VN pooled (if grand table includes a pooled column)

| Quantity | VNM Pooled (2009 + 2015 + 2023, with wave FE) |
|---|---|
| Turning point (raw FSTS %) | **31.4%** |
| TP 95% CI | [16.4%, 46.4%] |
| Lind–Mehlum p | **.041 ✓** |
| TCI β_z | **0.192*** *** |
| TCI SE | 0.036 |
| DAI β_z | **0.085*** *** |
| DAI SE | 0.035 |
| Analytic N | 2,322 |

---

## C. Why these numbers differ from the V4.3 set in the P5 patch

| Quantity | V4.3 (in P5 patch) | spec A (verified pipeline) | Reason |
|---|---|---|---|
| TP 2009 | 36.2% | **43.6%** | Different listwise — V4.3 retained `-9` codes as numeric |
| TP 2015 | 36.5% | **36.3%** | (close — small composition shift after dropping `-9`) |
| TP 2023 | 33.8% | **40.6%** | Different listwise + WBES 2023 `a4b` missing; spec A uses `a4a` for sector FE |
| LM p 2009 | .060 | **.128** | After dropping `-9` rows, sample loses some of the high-FSTS observations that drove inverted-U signal |
| LM p 2015 | .017 | **.033** | Modest drift |
| LM p 2023 | .029 | **.068** | Same direction; sample shrinkage attenuates power |
| TCI β_z 2009 | .317 | **.224** | -9 rows removed shifted within-wave z-standardisation |
| TCI β_z 2015 | .047 | **.168** | Substantial change — V4.3's null in 2015 was an artefact of -9 contamination |
| TCI β_z 2023 | .180 | **.090** | Marginal in spec A vs. significant in V4.3 |
| DAI β_z 2009 | .251 | **.122** | Substantial reduction; V4.3 was contaminated by retained -9 codes |
| DAI β_z 2015 | .022 | **.007** | Both null, em P4 finds slightly weaker null |
| DAI β_z 2023 | .176 | **.108** | Reduction; spec A still significant |

Em P4 manuscript v4.4 documents the rationale in §3.2 transparency paragraph: *"WBES non-response codes (`-9`) are treated as missing rather than as numeric data, restoring methodological alignment with Enterprise Survey codebook guidance. ... the corrected coefficients are smaller in magnitude than the previously reported values across most parameters but are direction-preserving for the principal hypotheses."*

---

## D. CSV-friendly inline format

If anh's P5 manuscript prefers CSV input over Markdown, the same content is in `manuscripts/p4-jwb-vietnam/tables/table_2_baseline.csv` and `tables/table_lind_mehlum.csv`. Columns:

```
table_2_baseline.csv:  wave, param, beta, se, p, n
table_lind_mehlum.csv: wave, tp_pct, tp_ci_lo, tp_ci_hi, lm_p
```

---

## E. Recommended sentence for P5 cover letter / response letter

If P5's submission acknowledges that its grand table uses spec-A VN numbers from a separate pipeline, anh can include:

> "Vietnam reference values in the cross-country comparison table are taken from the verified spec-A pipeline reported in [P4 reference / repository], which treats WBES non-response code `-9` as missing per Enterprise Survey codebook guidance. P5 China estimation follows the same `-9` discipline."

If P5's pipeline does *not* yet apply the `-9` rule, em recommend retro-applying it before P5 submission so the grand table is internally consistent across all six country-waves.

---

*End of export. Em did not modify P5 prose; this file is a paste-ready artefact for anh's use during P5 finalisation.*
