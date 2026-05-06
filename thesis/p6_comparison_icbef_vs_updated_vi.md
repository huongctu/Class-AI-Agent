# So sánh P6 — Phiên bản hiện tại (UPDATED) vs Phiên bản Kỷ yếu ICBEF 2025

> NCS: Đỗ Thùy Hương · HD: PGS.TS. Phan Anh Tú
>
> **P6 ICBEF 2025**: Đỗ, T. H., & Phan, A. T. (2024). Internationalization and firm performance: A meta-analysis review. In *Proceedings of the 6th International Conference on Economics, Business, and Finance* (Vol. 2, tr. 469–489, ISBN). College of Economics, Can Tho University.
>
> **P6 UPDATED**: Bản đang chuẩn bị cho luận án (2026), kế hoạch chi tiết tại `thesis/06_p6_meta_update_plan_vi.md`.

---

## 1. Bảng so sánh tổng quát

| Tiêu chí | P6 ICBEF 2025 (đã công bố) | P6 UPDATED (cho luận án) | Mức độ thay đổi |
|---|---|---|---|
| **Coverage thời gian** | 1977–2022 (45 năm) | 1982–2026 (44 năm) | Cập nhật mốc cuối |
| **Pool size** | 113 studies, 200 effect sizes | ~130 studies (linh hoạt; baseline 113 + 17 new = 130) | +15% |
| **Phương pháp meta-analysis** | Random-effects pooled (DerSimonian-Laird) | **Three-level MARA** (Cheung, 2014; Van den Noortgate et al., 2013) | **Methodological upgrade** |
| **Software** | MetaEssentials 1.5 (Suurmond et al., 2017) | `metafor` (R) hoặc `pymetaR` (Python) | **Đổi tool** |
| **Effect size aggregation** | Single-level pooling | Nested (Level 1 sampling + Level 2 within-study + Level 3 between-study) | **Mới** |
| **Moderators được kiểm định** | Country of origin, Industry (2 chiều) | Country, Industry **+ ICRV regime + cDAI + DPL phase** (5 chiều) | **+3 moderator độc đáo** |
| **Pooled effect size** | $r = 0.07$ | (chưa có; cần re-run trên `metafor`) | Cần verify consistency |
| **Heterogeneity $I^2$** | 87.92% | (chưa có; mong đợi tương tự sau decomposition 3-level) | Cần report ở 3 cấp |
| **Publication bias tests** | Funnel plot, fail-safe N | Egger, Begg-Mazumdar, trim-and-fill, fail-safe N (đầy đủ hơn) | Bổ sung |
| **Pre-registration** | Không | **OSF preregistration** trước khi extract effect mới | **Mới** |
| **Inter-coder reliability** | Single coder | Cohen's $\kappa \geq 0.7$ trên 20% double-coded subset | **Mới** |
| **Theoretical contribution** | Tổng hợp 6 meta trước | **3 lý thuyết mới**: Capability–Institution Mismatch, Digital Paradox Lifecycle, ICRV 5-regime | **Đóng góp lý thuyết chính** |
| **Robustness checks** | Sensitivity analysis cơ bản | Leave-one-out + REML vs DL + Asian-only + outlier exclusion + alternative ICRV thresholds | Mở rộng |

## 2. Ba moderators MỚI là đóng góp chính của P6 UPDATED

### 2.1 Country-level Digital Adoption (cDAI)

**Định nghĩa**: chỉ số áp dụng số cấp quốc gia, đo bằng World Bank Digital Adoption Index hoặc ITU Digital Development Index theo country-year.

**Khoảng trống lấp đầy**: Chưa từng có meta nào kiểm định cDAI như country-level moderator của quan hệ I→P, dù:
- Bhandari et al. (2023) chứng minh resource-orchestration interaction ở firm level
- Verhoef et al. (2021) đặt nền cho phân tầng năng lực số (digitization → digitalization → digital transformation)

**Mã hóa**: high/medium/low theo cDAI quartile + continuous score.

**Hypothesis**: Quan hệ I→P mạnh hơn ở nước cDAI cao (ỷ lệ cao MNE platform-driven internationalization).

### 2.2 Asian Institutional Heterogeneity (ICRV)

**Định nghĩa**: Institutional Context Regime Variation — phân loại 5 nhóm thể chế dựa trên WGI Rule of Law với thresholds $+0.80$ và $-0.50$:
- Regime I (Advanced): WGI > +0.80
- Regime II (Upper-middle): -0.50 ≤ WGI ≤ +0.80
- Regime III (Emerging): -0.50 < WGI < 0
- SIDS: Pacific small island states (boundary case)
- Frontier: WGI < -0.50

**Khoảng trống lấp đầy**: Marano et al. (2016) meta-analysis chỉ phân tách 6 nhóm thể chế tổng quát; chưa có nghiên cứu nào áp dụng phân loại 5 regime cho riêng khu vực châu Á + Pacific.

**Hypothesis**: Quan hệ I→P khác biệt rõ rệt theo regime (Khanna & Palepu, 2010; North, 1990).

### 2.3 Digital Paradox Lifecycle (DPL)

**Định nghĩa**: Mã hóa study theo precede / span / follow mốc 2009 inflection point — năm xuất hiện productivity J-curve của digital technology (Brynjolfsson, Rock & Syverson, 2021):
- **Precede** (data thu thập trước 2009): chưa có hiệu ứng số rõ
- **Span** (data 2005–2014): pha chuyển đổi
- **Follow** (data sau 2014): hiệu ứng số đầy đủ

**Khoảng trống lấp đầy**: Chưa có meta nào kiểm định Digital Paradox Lifecycle như moderator. Dzikowski et al. (2023) đề cập productivity paradox nhưng không systematic test.

**Hypothesis**: Hiệu ứng I→P thay đổi qua 3 phase do tái cấu trúc do digital transformation (David, 1990 — dynamo analogy).

## 3. Differentiation rõ ràng — tránh phản biện "lặp lại"

| Câu hỏi phản biện | P6 UPDATED trả lời | Bằng chứng |
|---|---|---|
| "Đã có ICBEF 2025, cần thêm P6 không?" | Phải vì 3 moderator mới chưa có meta nào kiểm định | §2.1, §2.2, §2.3 |
| "Tại sao đổi method từ MetaEssentials sang `metafor`?" | Three-level MARA cho nested effect sizes (Cheung 2014); MetaEssentials không hỗ trợ | §1 bảng so sánh |
| "K=130 có đủ không?" | Quality > quantity; reviewer đánh giá moderator coding chứ không phải số lượng | §6 Risks (mitigation) |
| "Có trùng lặp với ICBEF 2025?" | Không — coverage, method, moderators đều khác | §1 bảng so sánh |
| "Pre-registration cần không?" | Có — OSF lock hypothesis trước extract; không có ở ICBEF 2025 | §11 Tuần 1 |
| "Inter-coder reliability có không?" | Có — 20% double-coded, $\kappa \geq 0.7$; ICBEF 2025 không có | §1 bảng |

## 4. Cấu trúc manuscript P6 UPDATED (theo OSF Outline)

| Section | ICBEF 2025 | P6 UPDATED |
|---|---|---|
| Abstract | 200 từ, không structured | 250 từ, structured (Background, Methods, Results, Discussion) |
| Introduction | 4 trang, 5 references chính | 6 trang, 15 references; mạnh về differentiation từ ICBEF 2025 + 3 gaps |
| Theoretical framework | Tóm tắt 6 meta trước | Tổng hợp 6 meta + 3 lý thuyết mới (Mismatch, DPL, ICRV) |
| Method | PRISMA 2020 đơn giản | PRISMA 2020 chi tiết + three-level MARA equations + coding protocol cho 3 moderator |
| Results | Forest plot + table | Forest plot + funnel plot + moderator subgroup tables (3) + interaction plots |
| Discussion | 3 trang, đối thoại 2 meta | 6 trang, đối thoại 6 meta + interpret 3 moderator mới |
| Conclusion | 1 trang | 2 trang, có hàm ý chính sách + future research |
| References | 35 | ~70 (đã verified APA 7) |
| Tổng trang | ~21 trang | ~38 trang |

## 5. Lineage — chuỗi phát triển của P6 research stream

```
2023-07-18: Phân tích gốc (MetaEssentials 1.5, k=46?)
   ↓
2024-12-31: Tiểu luận tổng quan
   ↓
2024-12-12: Hội thảo ICBEF (ngày trình bày)
   ↓
2025: Công bố Kỷ yếu ICBEF (k=113, r=0.07, I²=87.92%)  ← P6 ICBEF 2025
   ↓
2026: P6 UPDATED cho luận án (k=~130, three-level MARA, +3 moderators) ← HIỆN TẠI
   ↓
(Tương lai) Submit journal article (target: International Business Review hoặc Journal of World Business)
```

## 6. Risks và mitigation cho P6 UPDATED

| Risk | P6 ICBEF 2025 | P6 UPDATED — Mitigation |
|---|---|---|
| Pool < 130 | Không vấn đề (đã 113) | Quality > quantity; chấp nhận k=130 |
| Reverse causality (Schmuck et al., 2022) | Chưa kiểm soát | Mã hóa biến study design (cross-section vs panel) + lag structure |
| cDAI proxy variation | (không có cDAI) | Dùng ITU DDI + WB DAI; rationale minh bạch |
| ICRV thresholds biện minh | (không có ICRV) | Robustness alternative thresholds ($+0.5/-0.3$ vs $+0.8/-0.5$) |
| Trùng lặp sample | Single-coder check | Coding `sample_id` đồng nhất; chỉ giữ effect size có trọng số cao nhất |
| Inconsistency với 2023 sau metafor | (không re-run) | Document trong appendix; giải thích estimator + data updates |
| Three-level MARA fails với k nhỏ | (không áp dụng) | Fallback two-level random-effects với cluster-robust SE |
| Inter-coder reliability thấp | (không có) | Double-code 20%, $\kappa \geq 0.7$ |

## 7. Lộ trình hoàn thiện P6 UPDATED — 14 tuần

| Tuần | Công việc chính | Output |
|---|---|---|
| 1–2 | Audit 113 baseline + reconcile + OSF preregistration | List 130 studies; pre-registration ID |
| 3–6 | Recode 3 moderator mới (ICRV, cDAI, DPL) cho 130 studies | Coding sheet hoàn thiện; $\kappa$ subset 20% |
| 7–8 | Convert MetaEssentials → `metafor` + setup three-level MARA | Replicated baseline; confirmed consistency |
| 9–10 | Moderator analysis (ICRV subgroup, cDAI moderation, DPL phase) | Subgroup tables + interaction plots |
| 10 | Robustness + publication bias | Sensitivity analysis tables |
| 11–14 | Manuscript writing (Intro + Method + Results + Discussion + Conclusion) | ~38 trang manuscript |

## 8. Đóng góp kỳ vọng so với 6 meta trước

| Meta trước | Năm | Số studies | Đóng góp chính | P6 UPDATED khác biệt |
|---|---|---|---|---|
| Bausch & Krist | 2007 | 87 | Hiệu ứng tổng I→P dương yếu (ES=0.15); context moderators | P6 thêm cDAI, ICRV, DPL — chưa có |
| Kirca et al. | 2012 | 141 | Firm-specific assets moderator (R&D intensity) | P6 country-level (cDAI) thay vì firm-level |
| Marano et al. | 2016 | 359 | Home-country institutions (6 nhóm) | P6 ICRV 5-regime cho riêng Châu Á |
| Schwens et al. | 2018 | 87 | International entrepreneurship | P6 mở rộng đến 2026 |
| Wu, Wood & Khan | 2022 | 359 | Hiệu ứng giảm dần qua thời gian | P6 mã hóa DPL phase rõ ràng |
| Arte & Larimo | 2022 | ~200 | Product diversification moderator | P6 không bao gồm; tập trung 3 moderator mới |
| **P6 ICBEF 2025** | 2025 | **113** | **Vietnam baseline** | (lineage cho P6 UPDATED) |
| **P6 UPDATED** | **2026** | **~130** | **+ cDAI, ICRV, DPL — 3 lý thuyết mới** | **Đóng góp chính cho luận án** |

## 9. Tổng kết

P6 UPDATED **không phải là bản tái bản** của P6 ICBEF 2025 mà là **nâng cấp methodological + theoretical** với 3 đóng góp chính:

1. **Methodological**: Three-level MARA (lần đầu cho I→P literature), `metafor` thay MetaEssentials, OSF preregistration, inter-coder reliability $\kappa \geq 0.7$.

2. **Theoretical**: 3 moderator mới (ICRV 5-regime, cDAI, DPL phase) lấp đầy 3 khoảng trống chưa có meta nào trước đó.

3. **Empirical**: Pool ~130 studies focus quality coding, baseline cho luận án Chương 4.1, kết hợp với P3/P4/P5/P7/P8 đa cấp synthesis evidence.

P6 UPDATED kế thừa lineage từ 2023 → 2024 → ICBEF 2025 → 2026, **không trùng lắp** vì coverage, method và moderators đều mở rộng và cải tiến.

---

*Tài liệu so sánh — phiên bản 1.0 (06/05/2026). Tham chiếu kế hoạch chi tiết: `thesis/06_p6_meta_update_plan_vi.md`. NCS: Đỗ Thùy Hương. HD: PGS.TS. Phan Anh Tú. Cần Thơ.*
