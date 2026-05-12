# Kế hoạch chi tiết P6 — Meta-Analytic Regression Analysis (MARA) update 1982–2026

File này trình bày kế hoạch triển khai P6 dựa trên kiến trúc đã có (script `run_search_agent.py`, `build_final_database.py`, 28 queries trong `search_queries.json`, database 46 studies hiện có, synthesis narrative). Mục tiêu là cập nhật phân tích meta-analytic và bổ sung **3 moderator độc đáo** (ICRV, cDAI, DPL) so với bản nền 2023.

> **Quan trọng về pool size**: các con số *k = 172* (target) và *k = 269* (MASTER) chỉ là **ước lượng tham khảo**, không phải hard deliverable. P6 được đánh giá bởi chất lượng coding 3 moderator mới và phương pháp three-level MARA, không phải số lượng paper thuần túy.

## 0. Lineage lịch sử của meta-analysis

P6 không phải nghiên cứu khởi tạo mới mà là bước phát triển thứ ba của một research stream đã được xây dựng từ 2023.

### 0.1 Mốc 1 — Phân tích gốc (18/07/2023)

NCS đã hoàn thành phân tích meta-analysis ban đầu ngày 18/07/2023 (`KÉT_QUẢ_PHÂN_TÍCH_TỔNG_HỌ̆P_NGÀY_18072023.docx`), sử dụng **MetaEssentials version 1.5** (Suurmond et al., 2017) với correlational data trong `MetaEssentials_Correlational_data_1.5...2022.xlsx`.

### 0.2 Mốc 2 — Tiểu luận tổng quan (31/12/2024)

NCS hoàn thiện tiểu luận tổng quan hỗ trợ cho conference paper.

### 0.3 Mốc 3 — Hội thảo ICBEF (12/12/2024) và công bố (ICBEF 2025)

Bài "Internationalization and firm performance: A meta-analysis review" được công bố trong Kỷ yếu ICBEF 2025 (Vol. 2, tr. 469–489, ISBN, NXB Đại học Cần Thơ) với 113 studies, 200 effect sizes, $r = 0.07$, $I^2 = 87.92\%$.

### 0.4 Mốc 4 — P6 update cho luận án (2026, hiện tại)

- **Coverage**: 1977–2022 → 1982–2026.
- **Pool**: 113 baseline + bổ sung (ước lượng tham khảo ~130–172, MASTER ~269; **không bắt buộc phải đạt**).
- **Method**: random-effects pooled → **three-level MARA** với nested effect sizes.
- **Moderators mới**: **cDAI**, **ICRV 5-regime**, **DPL phase** (đây là đóng góp chính).
- **Software**: chuyển từ MetaEssentials sang `metafor` (R) hoặc `pymetaR` (Python).

### 0.5 Vì sao lineage quan trọng

Ghi nhận lineage làm hai việc. Thứ nhất, nó bảo vệ tính độc lập của P6 trong luận án: P6 được xây từ bài conference đã công bố, không trùng lắp vì coverage, method và moderators đều mở rộng và cải tiến. Thứ hai, nó cho phép **kiểm định đối chiếu**: các kết quả P6 cần consistent với bản 2023 ở những điểm cơ bản.

## 1. Định vị và differentiation từ bài ICBEF 2025

### 1.1 Vai trò trong luận án

P6 thuộc **tầng synthesis** trong khung 4 tầng + digital lens. Kết quả P6 đi vào **Ch.4.1**, baseline literature vào **Ch.2.3**, integration ở **Ch.5.1**.

### 1.2 Differentiation từ bài ICBEF 2025

| Yếu tố | ICBEF 2025 (đã công bố) | P6 (cho luận án) |
|---|---|---|
| Coverage | 1977–2022, 113 studies, 200 effect sizes | **1982–2026, pool linh hoạt** |
| Moderators | Country of origin, industry | Thêm **cDAI, ICRV regime, DPL phase** (đóng góp chính) |
| Cấp độ | Random-effects pooled | **Three-level meta-analytic regression** |
| Software | MetaEssentials 1.5 | **`metafor` (R)** hoặc **`pymetaR` (Python)** |
| Kết quả chính | $r = 0.07$, $I^2 = 87.92\%$ | Cập nhật + moderator analysis cho 3 nhánh mới |

Differentiation rõ ràng để tránh phản biện "lặp lại". P6 phải có một mục "What's new compared to Do & Phan (2025)" trong manuscript.

## 2. Kiến trúc kế thừa (đã tồn tại)

### 2.1 Script và dữ liệu hiện có

- `scripts/run_search_agent.py`: orchestration cho 5 phases search
- `scripts/build_final_database.py`: tổng hợp `study_database.json` + `references_APA7.md` + `new_studies_only.csv`
- `data/study_database.json`: **46 studies** verify, 29 existing + 17 new
- `outputs/synthesis_narrative.md`: narrative với APA 7th citations
- `P6_Meta_Update_Template1.xlsx`: coding template
- `P6_Meta_MASTER_k269.xlsx`: MASTER pool size **k = 269** (ước lượng tham khảo, không bắt buộc)
- **Historical**: `MetaEssentials_Correlational_data_1.5...2022.xlsx`, `KÉT_QUẢ_PHÂN_TÍCH_TỔNG_HỌ̆P_NGÀY_18072023.docx`
- **OSF Package** (chuẩn bị pre-registration): `P6_OSF_Preregistration_Template.md`, `P6_Outline_Master_Detailed.md`, `P6_Section_by_Section_Guide.md`, `P6_Abstract_Template.md`, `P6_Cover_Letter_Template.md`, `P6_Citation_Verification_Log.md`, `P6_References_APA7_Verified.md`

### 2.2 28 search queries (theo `search_queries.json`)

Linh hoạt sử dụng — ưu tiên những nhóm query có liên quan đến 3 moderator mới (cDAI/Phase 3, Institutional/Phase 4) trước.

### 2.3 Inclusion/Exclusion criteria (theo `CLAUDE.md`)

Giữ nguyên 7 tiêu chí include + 6 tiêu chí exclude.

## 3. Ba khoảng trống nghiên cứu chưa có meta nào lấp

### Gap 1: country-level Digital Adoption (cDAI) moderator

**Country-level digital adoption (cDAI)** — proxied bằng World Bank Digital Adoption Index hoặc ITU Digital Development Index — chưa từng được kiểm định meta-analytic như country-level moderator của quan hệ I→P, dù Bhandari et al. (2023) chứng minh resource-orchestration interaction ở firm level và Verhoef et al. (2021) đặt nền cho phân tầng năng lực số (digitization → digitalization → digital transformation). cDAI tương ứng tier "digitalization" trong Verhoef framework, khác với firm-level technological capability (TCI) theo truyền thống Lall (1992) và Cohen & Levinthal (1990). P6 là meta đầu tiên kiểm định cDAI ở cấp quốc gia (Bharadwaj et al., 2013; Bhandari et al., 2023; Bustamante et al., 2022; Chen & Meng, 2022; Verhoef et al., 2021).

### Gap 2: Asian institutional heterogeneity

Áp dụng **ICRV 5-regime classification** theo WGI Rule of Law thresholds $+0.80$ và $-0.50$ (Khanna & Palepu, 2010; North, 1990; Do & Phan, 2025).

### Gap 3: Digital Paradox Lifecycle (DPL)

Mã hóa study theo **precede / span / follow** mốc 2009 inflection point (Brynjolfsson et al., 2021; David, 1990; Dzikowski et al., 2023).

## 4. Ưu tiên triển khai (không theo size, theo giá trị học thuật)

### 4.1 Thứ tự ưu tiên (mới)

| Ưu tiên | Công việc | Tại sao |
|---|---|---|
| **P0 — cao nhất** | Verify + recode 113 baseline studies + 17 new = ~130 với 3 moderator mới (ICRV, cDAI, DPL) | Công việc cốt lõi; tạo ra đóng góp lý thuyết mới |
| **P1 — trung buình** | Three-level MARA + consistency check vs bản 2023 | Methodological upgrade |
| **P2 — tùy điều kiện** | Backward citation scan của 6 meta trước để tăng pool | Chỉ luùc thời gian cho phép |
| **P3 — tùy điều kiện** | Run 28 queries qua Consensus + web supplemental | Optional, làm sau defense nếu muốn journal version |

### 4.2 Ưu tiên theo loại nghiên cứu

Khi expand pool, ưu tiên studies theo thứ tự:

1. **Asian context** (Wu et al., 2022 backward scan; new 2023–2026 China/India/ASEAN papers)
2. **Digital moderation** (recent papers về digital transformation × internationalization)
3. **WBES-based** (đồng nhất methodology với P3, P4, P5, P7)
4. **Other contexts** (US, Europe, Latin America — ưu tiên thấp hơn)

## 5. Phương pháp phân tích (giữ nguyên)

### 5.1 Three-level MARA

Mô hình ba cấp:
- **Level 1**: sai số sampling trong từng effect size $r_{ij}$.
- **Level 2**: variance giữa effect sizes trong cùng study.
- **Level 3**: variance giữa studies (true heterogeneity).

Theo Cheung (2014) và Van den Noortgate et al. (2013), `metafor` package R.

### 5.2 Moderators ưu tiên (giảm từ 11 → 7)

**Core 3 (mới, bắt buộc)**: ICRV regime, cDAI level, DPL phase.

**Bổ sung 4 (chuẩn)**: country of origin, industry, DOI measure type, FP measure type.

Bỏ bớt cho versión dễ thuức hiện: sample size, publication year, digital_moderator presence, institutional_moderator presence (một phần redundant với 3 core).

### 5.3 Publication bias và robustness

- Egger's test, Begg-Mazumdar, trim-and-fill, funnel plot, fail-safe N.
- Leave-one-out, REML vs DL estimator, Asian-only subset, outlier exclusion.
- **Consistency check**: tái chạy 113 baseline subset bằng `metafor`.

## 6. Lộ trình triển khai realistic (14 tuần)

### Tuần 1–2: Audit + reconcile

- Verify 113 baseline studies trong MetaEssentials xlsx (DOI accuracy, complete coding)
- Reconcile với 46-study new database
- Plan: target ~130 deliverable studies
- Nếu MASTER xlsx đã có entries mới: import + verify

### Tuần 3–6: Recode 3 moderator mới cho ~130 studies

- **ICRV regime**: lấy WGI Rule of Law theo year cho mỗi country, classify I/II/III/SIDS/Frontier theo thresholds $+0.80/-0.50$
- **cDAI level**: lấy ITU DDI hoặc WB Digital Adoption Index theo country-year, classify high/medium/low
- **DPL phase**: mã hóa precede/span/follow theo mốc 2009
- ~3–4 tuần nếu có RA giúp; 5–6 tuần nếu solo
- **Inter-coder reliability**: double-code 20% subset, tính Cohen's $\kappa \geq 0.7$

### Tuần 7–8: Convert MetaEssentials → `metafor`

- Re-run baseline analysis trong R (`metafor::rma.mv`)
- Confirm consistency với 2023 results
- Setup three-level MARA structure

### Tuần 9–10: Moderator analysis

- ICRV subgroup (5 regimes)
- cDAI moderation (continuous và categorical)
- DPL phase comparison (pre-/span-/post-2009)
- Three-way interaction nếu dữ liệu cho phép
- Publication bias tests
- Robustness sensitivity

### Tuần 11–14: Viết manuscript theo OSF Outline

- **Tuần 11**: Introduction (mạnh về differentiation từ ICBEF 2025) + Method (PRISMA flow, three-level MARA detail)
- **Tuần 12**: Results (forest plot, funnel plot, moderator tables)
- **Tuần 13**: Discussion (đối thoại với 6 meta trước, cDAI gap, ICRV gap, DPL gap)
- **Tuần 14**: Conclusion + finalize cover letter + abstract template + verify all citations

### Pre-registration trên OSF (Tuần 1, làm song song)

Lấy `P6_OSF_Preregistration_Template.md`, fill ngay với:
- Title, hypotheses, eligibility criteria
- Search strategy (28 queries đã thiết kế)
- Coding protocol (3 moderator mới)
- Analysis plan (three-level MARA, moderator subgroups)
- Submit ngay khi bắt đầu phân tích → lock hypotheses trước khi extract effect sizes mới

## 7. Đóng góp kỳ vọng (không đổi)

### 7.1 Methodological

- Meta-analysis đầu tiên trên DOI–FP sử dụng **three-level MARA**.
- Lần đầu kiểm định **cDAI** như country-level moderator.
- Lần đầu opérer **ICRV 5-regime classification**.

### 7.2 Theoretical

- Evidence cho **Capability–Institution Mismatch**.
- Kiểm định **Digital Paradox Lifecycle**.
- Mở rộng tranh luận internalization theory cho digital era.

### 7.3 Empirical

- Pool ~130 studies focused on 3 moderator mới (kết hợp quality > quantity).
- Cung cấp baseline cho các chapter tiếp theo.
- Reference list APA 7th đầy đủ.

## 8. Risks và mitigation

| Risk | Mitigation |
|---|---|
| Pool không đạt k=172 | **Không vấn đề**: pool size flexible; chấp nhận k=130 với quality coding cao |
| Reverse causality (Schmuck et al., 2022) | Coding biến study design (cross-section vs panel) và lag structure |
| cDAI proxy variation giữa countries | Dùng ITU DDI và WB DAI như country-level proxies; coding rationale minh bạch |
| ICRV regime thresholds cần biện minh | Robustness với alternative thresholds ($+0.5/-0.3$ vs $+0.8/-0.5$) |
| Trùng lặp sample | Coding "sample_id" đồng nhất; chỉ giữ effect size có trọng số cao nhất |
| Inconsistency với bản 2023 sau khi tái chạy `metafor` | Document trong appendix; giải thích (estimator, data updates, v.v.) |
| Three-level MARA fails to converge với k nhỏ | Fallback two-level random-effects với cluster-robust SE |
| Inter-coder reliability thấp cho 3 moderator mới | Double-code 20% subset, target Cohen's $\kappa \geq 0.7$ |

## 9. Kết nối với các file khác trong `/thesis/`

- `00_optimal_plan_vi.md`: P6 đóng góp methodological novelty
- `01_chapter_outline_vi.md`: Kết quả P6 vào Ch.4.1; baseline literature vào Ch.2.3
- `02_theoretical_framework_vi.md`: P6 cung cấp evidence cho H1, H6
- `03_methodology_vi.md`: Mục 4.1 chi tiết three-level MARA kế thừa file này
- `04_references_apa7.md`: Tất cả reference
- `05_p5_china_design_vi.md`: P5 và P6 cùng kiểm định H6
- `07_p7_capstone_design_vi.md`: P6 và P7 cùng được vào Ch.4 (P6 = synthesis, P7 = empirical)

## 10. Tham khảo chính (đầy đủ trong `04_references_apa7.md`)

Arte, P., & Larimo, J. (2022). Moderating influence of product diversification on the international diversification–performance relationship. *Journal of Business Research, 139*, 1408–1423.

Banalieva, E. R., & Dhanaraj, C. (2019). Internalization theory for the digital economy. *Journal of International Business Studies, 50*(8), 1372–1387.

Bausch, A., & Krist, M. (2007). The effect of context-related moderators on the internationalization–performance relationship. *Management International Review, 47*(3), 319–347.

Begg, C. B., & Mazumdar, M. (1994). Operating characteristics of a rank correlation test for publication bias. *Biometrics, 50*(4), 1088–1101.

Bhandari, K. R., Zámborský, P., Ranta, M., & Salo, J. (2023). Digitalization, internationalization, and firm performance. *International Business Review, 32*(4), 102027.

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009). *Introduction to meta-analysis*. Wiley.

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve. *American Economic Journal: Macroeconomics, 13*(1), 333–372.

Cheung, M. W.-L. (2014). Modeling dependent effect sizes with three-level meta-analyses. *Psychological Methods, 19*(2), 211–229.

David, P. A. (1990). The dynamo and the computer. *American Economic Review, 80*(2), 355–361.

Duval, S., & Tweedie, R. (2000). Trim and fill. *Biometrics, 56*(2), 455–463.

Dzikowski, P., Tomczyk, E., & Chlebus, M. (2023). Do digital technologies pay off? *Technovation, 128*, 102838.

Egger, M., Davey Smith, G., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *British Medical Journal, 315*(7109), 629–634.

Hedges, L. V., Tipton, E., & Johnson, M. C. (2010). Robust variance estimation in meta-regression. *Research Synthesis Methods, 1*(1), 39–65.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets*. Harvard Business Press.

Kirca, A. H., Roth, K., Hult, G. T. M., & Cavusgil, S. T. (2012). The role of context in the multinationality–performance relationship. *Global Strategy Journal, 2*(2), 108–121.

Marano, V., Arregle, J. L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization–performance relationship. *Journal of Management, 42*(5), 1075–1110.

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press.

Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ, 372*, n71.

Schmuck, D., Lagerström, K., & Sallis, J. (2022). Turning the tables. *Management International Review, 62*(6), 847–878.

Schwens, C., et al. (2018). International entrepreneurship: A meta-analysis. *Entrepreneurship Theory and Practice, 42*(5), 734–768.

Suurmond, R., van Rhee, H., & Hak, T. (2017). Introduction, comparison, and validation of Meta-Essentials. *Research Synthesis Methods, 8*(4), 537–553. https://doi.org/10.1002/jrsm.1260

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594.

Verhoef, P. C., et al. (2021). Digital transformation. *Journal of Business Research, 122*, 889–901.

Wu, J., Fan, D., & Chen, X. (2022). Revisiting the internationalization–performance relationship. *Management International Review, 62*(2), 199–231.

Yang, Y., & Driffield, N. (2012). Multinationality–performance relationship. *Management International Review, 52*(1), 23–47.

## 11. Realistic execution path — Checklist 14 tuần

Liệt kê công việc cụ thể cho từng tuần. NCS có thể cập nhật status [ ] thay bằng [x] khi hoàn thành.

### Tuần 1 — Audit + OSF preregistration

- [ ] Muở MetaEssentials xlsx, verify 113 baseline studies; đánh dấu DOI sai/missing
- [ ] Muở `study_database.json` (46 studies), reconcile với 113 baseline
- [ ] Lên danh sách ~130 deliverable studies
- [ ] Lấy `P6_OSF_Preregistration_Template.md`, fill in (RQs, hypotheses, eligibility, search strategy, coding protocol, analysis plan)
- [ ] Submit pre-registration trên OSF

### Tuần 2 — Reconcile + plan extraction

- [ ] Tạo coding sheet thống nhất (bằng `P6_Meta_Update_Template1.xlsx`)
- [ ] Tách ~130 studies vào 3 nhóm: "đã có effect size + moderators" (nên ~90), "cần re-extract effect size" (nên ~30), "cần lấy full text + extract" (nên ~10)
- [ ] Setup R environment với `metafor`, `dplyr`, `ggplot2`
- [ ] Tải WGI Rule of Law data (World Bank); ITU DDI hoặc WB DAI cho cDAI

### Tuần 3 — Recode batch 1 (40 studies)

- [ ] Coder 1 (NCS): 40 studies — ICRV + cDAI + DPL
- [ ] Coder 2 (RA nếu có): double-code 8/40 (20%)
- [ ] Tính Cohen's $\kappa$ cho double-coded subset
- [ ] Resolve disagreements

### Tuần 4 — Recode batch 2 (40 studies)

- [ ] Coder 1: 40 studies
- [ ] Coder 2: double-code 8/40
- [ ] $\kappa$ check

### Tuần 5 — Recode batch 3 (40 studies)

- [ ] Coder 1: 40 studies
- [ ] Coder 2: double-code 8/40
- [ ] $\kappa$ check
- [ ] Tuần này có thể gồm re-extract effect sizes cho ~10 studies khó

### Tuần 6 — Recode batch 4 (bổ sung) + verify hoàn thiện

- [ ] Recode ~10 studies khó (full text extraction)
- [ ] Final verify tất cả 130 studies có đủ 4 fields: effect_size, ICRV, cDAI, DPL
- [ ] Update `study_database.json`

### Tuần 7 — Convert sang `metafor`

- [ ] Import `study_database.json` vào R
- [ ] Tính Fisher's $z$ cho từng effect size
- [ ] Setup `rma.mv()` cho three-level model
- [ ] Re-run baseline pooled effect; so sánh với bản 2023

### Tuần 8 — Three-level MARA setup

- [ ] Kiểm định nested structure (level 1 sampling, level 2 within-study, level 3 between-study)
- [ ] Estimate $\sigma^2_{level2}$, $\sigma^2_{level3}$
- [ ] Compute pooled effect, $I^2$ at each level
- [ ] Forest plot tổng hợp

### Tuần 9 — Moderator analysis

- [ ] ICRV regime subgroup (5 regimes)
- [ ] cDAI moderation (continuous và categorical)
- [ ] DPL phase comparison (pre/span/post 2009)
- [ ] Two-way interactions nếu dữ liệu cho phép

### Tuần 10 — Robustness + publication bias

- [ ] Egger's test, Begg-Mazumdar
- [ ] Trim-and-fill, fail-safe N, funnel plot
- [ ] Leave-one-out sensitivity
- [ ] Asian-only subset
- [ ] Alternative ICRV thresholds robustness

### Tuần 11 — Viết Introduction + Method

- [ ] Introduction (mạnh về differentiation từ ICBEF 2025; nêu 3 gaps)
- [ ] Method (PRISMA 2020 flow diagram, three-level MARA detail, coding protocol)
- [ ] Update `P6_References_APA7_Verified.md`

### Tuần 12 — Viết Results

- [ ] Forest plot, funnel plot, moderator tables
- [ ] Subgroup analysis tables
- [ ] Interaction plots

### Tuần 13 — Viết Discussion

- [ ] Đối thoại với 6 meta trước (Kirca, Yang, Marano, Schwens, Wu, Arte)
- [ ] cDAI gap discussion
- [ ] ICRV gap discussion
- [ ] DPL gap discussion
- [ ] Limitations + future research

### Tuần 14 — Conclusion + finalize

- [ ] Conclusion section
- [ ] Verify tất cả citations theo `P6_Citation_Verification_Log.md`
- [ ] Fill `P6_Cover_Letter_Template.md`
- [ ] Fill `P6_Abstract_Template.md`
- [ ] Final review
- [ ] Update OSF với final outcomes (deviations from preregistration)

## 12. Quality > Quantity — Kết luận

P6 được đánh giá bởi:

1. **Chất lượng coding 3 moderator mới** (ICRV, cDAI, DPL) — đây là đóng góp khoa học.
2. **Methodological upgrade**: three-level MARA thay vì pooled random-effects.
3. **Consistency với bản 2023**: bảo vệ lineage research stream.
4. **OSF preregistration**: trước khi phân tích để transparency.
5. **Asian focus**: subgroup analysis cho từng ICRV regime.

Không quan trọng pool size = 130, 172 hay 269. Reviewer quan tâm **mô hình + theoretical contribution**, không phải số paper thuần túy. K=130 với quality coding cho 3 moderator mới là publishable và có đóng góp đáng kể.
