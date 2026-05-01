# DAI Decontamination — Numerical Memo (P4 + P5)

**Date**: 2026-05-01
**Trigger**: anh's directive — "cần điều chỉnh p4 và p5 ở chọn biến digital" (drop `e6` from DAI; keep `e6` only in TCI to avoid construct contamination).
**Pipelines re-run**:
- `manuscripts/p4-jwb-vietnam/code/p4_python_check.py` → `manuscripts/p4-jwb-vietnam/output_dai_decontam/`
- `manuscripts/p5-apjm-china/code/p5_beta_pipeline.py` → `manuscripts/p5-apjm-china/output/`

**Stop point**: Em surfaces these numbers BEFORE rewriting any manuscript prose. Confirm before Phase D.

---

## 1 · TCI–DAI within-wave correlation (decontamination check)

| Wave | OLD r (DAI = c22b + e6) | NEW r (DAI = c22b only) | Δ |
|---|---|---|---|
| **P4 — VNM 2009** | 0.63 (paper-reported) | **0.384** | −0.25 |
| **P4 — VNM 2015** | 0.65 | **0.351** | −0.30 |
| **P4 — VNM 2023** | 0.56 | **0.254** | −0.31 |
| **P4 — pooled** | 0.61 | **0.319** | −0.29 |
| **P5 — CHN 2012** | 0.575 | **0.266** | −0.31 |
| **P5 — CHN 2024** | 0.505 | **0.418** | −0.09 |

**Verdict**: decontamination works as intended. Cross-construct correlations drop ~0.25–0.31 in P4 and 0.09–0.31 in P5. The remaining correlation (~0.25–0.42) reflects *substantive* shared variance between technological capability and digital presence — not the *mechanical* contamination from the shared `e6` item.

---

## 2 · P4 — DAI direct effect by wave (β_z, OLS-HC1; baseline + controls)

| Wave | N | OLD DAI_thin β (p) | NEW DAI_core β (p) | Direction change |
|---|---|---|---|---|
| 2009 | 734 | +0.122 (em verified spec-A; paper Table 2 reported +0.251) | **+0.175 (.0004)** | strengthened, same direction |
| 2015 | 614 | +0.007 (.870, em spec-A) | **+0.008 (.887)** | unchanged null |
| 2023 | 974 | +0.108 (em spec-A; paper +0.176) | **+0.113 (.021)** | similar magnitude, same direction |
| pooled | 2,322 | +0.116 (em spec-A; paper +0.154) | **+0.108 (.0004)** | similar magnitude, same direction |

**P4 read**: DAI direct effect is robust to dropping `e6`. The 2009 effect strengthens (+0.122 → +0.175); 2015 stays null; 2023 and pooled essentially unchanged. **No qualitative shift in P4 conclusions.**

---

## 3 · P4 — DAI_rich for 2023 (no `e6`; just c22b + k33 + k38)

| Spec | N | β_z (p) | Verdict |
|---|---|---|---|
| continuous (k33/k38 as %) | 801 | +0.049 (.327) | null |
| binary (k33/k38 indicator) | 974 | +0.042 (.336) | null |

**P4 read**: DAI_rich attenuates to null when e6 is dropped — same direction as the original v4.4 DAI_rich finding (β=0.084, p=.091). The §4.6 attenuation paragraph stands; magnitude updates from 0.084 to ~0.045.

---

## 4 · P5 — DAI direct effect by wave (β_z, OLS-HC1; M0p baseline)

| Wave | N | OLD DAI_thin β (p) | NEW DAI_core β (p) | **Qualitative shift** |
|---|---|---|---|---|
| 2012 | 1,645 (was 1,633) | **−0.064 (.044)** ⚠ | **+0.027 (.273)** | **SIGN FLIP** sig. negative → null positive |
| 2024 | 1,916 (was 1,915) | +0.005 (.871) | **+0.068 (.044)** ✓ | null → **sig. positive** |
| pooled | 3,561 (was 3,548) | **−0.064 (.004)** ⚠ | **+0.062 (.006)** ✓ | **SIGN FLIP** sig. negative → sig. positive |

**P5 read — material change.** The negative-DAI puzzle in P5 (which em flagged as "substantive divergence" from P5 patch numbers in `p5_beta_results_memo.md`) was largely an artefact of e6 contamination. With DAI = c22b only, H4b (positive level shift from digital adoption) is now **supported** in 2024 and pooled, **null but positive** in 2012.

This implies §4.4 of `manuscript_p5_v1.md` needs substantial rewriting — the "DAI direct effect is **negative** in 2012 and pooled" claim no longer holds.

### P5 — Paternoster z-test (cross-wave 2012 ↔ 2024)

| Variable | β_2012 | β_2024 | z | p | Interpretation |
|---|---|---|---|---|---|
| TCI_full_z | +0.163 | +0.274 | −2.55 | **.011** | TCI strengthens significantly between waves |
| DAI_core_z | +0.027 | +0.068 | −0.96 | .335 | DAI_core cross-wave stable |
| FSTS | +1.658 | +0.751 | +1.31 | .192 | FSTS slope cross-wave stable |
| FSTS² | −1.991 | −0.804 | −1.45 | .148 | curvature cross-wave stable |

H2 threshold-stability claim: still supported (FSTS / FSTS² coefficients statistically indistinguishable across waves).

---

## 5 · P5 — Threshold core (M0) — UNCHANGED

| Sample | N | TP | LM_p | FSTS β (p) | FSTS² β (p) |
|---|---|---|---|---|---|
| CHN 2012 | 2,619 | 49.4% | <.001 | +2.060 (<.001) | −2.085 (<.001) |
| CHN 2024 | 1,940 | 47.6% | .037 | +1.428 (.014) | −1.502 (.035) |
| CHN pooled | 4,559 | 48.9% | <.001 | +1.782 (<.001) | −1.821 (<.001) |

Identical to pre-decontamination — DAI is not in the M0 core. Threshold-stability contribution stands robustly.

---

## 6 · P5 — Working-capital interactions (M1/M3/M4) — UNCHANGED

All WC × FSTS² coefficients identical to prior run (`p5_beta_results_memo.md`). β classification stays **NULL** (with weak k3f hint in 2012 only). DAI decontamination does not affect WC trap test — different sub-models entirely.

---

## 7 · Net effect on P4 vs P5 portfolio framing

| Paper | Pre-decontamination DAI story | Post-decontamination DAI story | Manuscript impact |
|---|---|---|---|
| **P4 (JWB)** | DAI direct = positive in 2009/2023/pooled, null 2015; DAI_rich attenuates | Same direction; magnitudes refined | **Minor** — update numbers in §3.2/§4.4/§4.6/§6 + Table 2/3 |
| **P5 (APJM)** | DAI direct = NEGATIVE significant 2012 + pooled; null 2024 (puzzling) | DAI direct = **POSITIVE** significant 2024 + pooled; null 2012 | **Material** — rewrite §4.4 DAI paragraph; flip the "DAI is null/contradictory in transitional setting" framing in §5; H4b moves from "not supported" toward "supported in modern wave + pooled" |

---

## 8 · Recommended next steps

1. **Em pauses for anh's confirmation on the P5 H4b reframing.** P5 was filed as null-scenario (Tier 1 / null-safe title: "Threshold-Stability Perspective"). If H4b now goes from null to supported, em can either:
   - **(a) Keep null-scenario title and framing** — DAI is a *secondary* explanatory layer per Option C+; threshold stability remains the central contribution. Add a short paragraph in §4.4 disclosing the upgrade and one sentence in §5 noting that the modernised digital-presence proxy is more consistent with productivity J-curve theory once measurement decontamination is applied.
   - **(b) Upgrade to limited-support scenario** — modify title (e.g. *"...A Threshold-Stability Perspective with Emerging Digital Adoption Effects"*) and rewrite §4.4 / §5 / §6 with limited-scenario templates from `p5_writing_pack_option_c_plus.md`.
   - Em recommends **(a)** — title and structural identity are anchored by Option C+; H4b is a level-shift control, not the focal hypothesis. The discovery that decontamination flips DAI sign is itself a methodological contribution worth a paragraph but doesn't restructure the paper.
2. **P4 prose update is mechanical** — magnitudes change but sign/significance pattern survives. No editorial decision needed; em can proceed in Phase D.
3. **DAI_rich** — em proposes adding a new subsection in P4 §4.6 explicitly contrasting old (c22b+e6+k33+k38) vs new (c22b+k33+k38) DAI_rich and noting both attenuate to null vs original v4.4 marginal-positive. Same J-curve interpretation holds.

---

## 9 · Outputs ready for re-use

- `manuscripts/p4-jwb-vietnam/output_dai_decontam/p4_python_baseline.csv` — analytic dataset with `dai_core` column
- `manuscripts/p4-jwb-vietnam/output_dai_decontam/p4_python_check.md` — full report (Block 1–7)
- `manuscripts/p5-apjm-china/output/p5_beta_results.csv` — 260 rows, includes M0p with DAI_core
- `manuscripts/p5-apjm-china/output/p5_beta_paternoster.csv` — 4 rows, cross-wave z-tests
- `manuscripts/p5-apjm-china/output/p5_beta_run.log` — stdout log

Em ready to proceed to Phase D once anh confirms (a) or (b) for P5 framing.
