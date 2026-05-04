# Kế hoạch chi tiết P6 — Meta-Analytic Regression Analysis (MARA) update 1982–2026

File này trình bày kế hoạch triển khai P6 dựa trên kiến trúc đã có (script `run_search_agent.py`, `build_final_database.py`, 28 queries trong `search_queries.json`, database 46 studies hiện có, synthesis narrative). Mục tiêu là mở rộng pool lên **k ≥ 172 effect sizes** và tiến tới MASTER **k = 269** với kiểm định moderators FDCI, ICRV và DPL.

## 0. Lineage lịch sử của meta-analysis

P6 không phải nghiên cứu khởi tạo mới mà là bước phát triển thứ ba của một research stream đã được xây dựng từ 2023. Ghi nhớ đầy đủ lineage giúp bảo đảm tính minh bạch và cho phép đối chiếu kết quả qua các mốc thời gian.

### 0.1 Mốc 1 — Phân tích gốc (18/07/2023)

NCS đã hoàn thành phân tích meta-analysis ban đầu ngày 18/07/2023, lưu trong `KÉT_QUẢ_PHÂN_TÍCH_TỔNG_HỌ̆P_NGÀY_18072023.docx`. Phân tích gốc dùng **MetaEssentials version 1.5** (Suurmond et al., 2017) với correlational data và được mã hóa trong `MetaEssentials_Correlational_data_1.5...2022.xlsx`. Đây là bước khởi tạo của toàn bộ P6 stream.

### 0.2 Mốc 2 — Tiểu luận tổng quan (31/12/2024)

NCS hoàn thiện tiểu luận tổng quan trong `NỘ̆I_DUNG_TIỂU_LUẬN_TỔNG_QUAN_NCS_THÙY_HƯƠNG_31122024.docx`, tổng hợp literature tổng quan hỗ trợ cho conference paper.

### 0.3 Mốc 3 — Hyội thảo ICBEF (12/12/2024) và công byố (ICBEF 2025 proceedings)

Bài "Internationalization and firm performance: A meta-analysis review" được báo cáo tại Hội thảo quốc tế lần thứ 6 về Kinh tế, Kinh doanh và Tài chính ngày 12/12/2024 tại Trường Kinh tế, Đại học Cần Thơ, sau đó công bố trong Kỷ yếu ICBEF 2025 (Vol. 2, tr. 469–489, ISBN, NXB Đại học Cần Thơ) với 113 nghiên cứu và 200 effect sizes giai đoạn 1977–2022. Hiệu ứng pooled $r = 0.07$ và $I^2 = 87.92\%$.

### 0.4 Mốc 4 — P6 update cho luận án (2026, hiện tại)

P6 cập nhật và mở rộng:

- **Coverage**: 1977–2022 → 1982–2026.
- **Pool size**: 113 → target k = 172 → MASTER k = 269.
- **Method**: random-effects pooled → **three-level MARA** với nested effect sizes.
- **Moderators**: country + industry → bổ sung **FDCI**, **ICRV 5-regime**, **DPL phase**.
- **Software**: chuyển từ MetaEssentials sang `metafor` (R) hoặc `pymetaR` (Python) để hỗ trợ three-level model.

### 0.5 Vì sao lineage quan trọng

Ghi nhận lineage làm hai việc. Thứ nhất, nó bảo vệ tính độc lập của P6 trong luyận án: P6 được xây từ bài con férence đã công bố, không trùng lắp vì coverage, pool, method và moderators đều mở rộng và cải tiến (xem bảng đối chiếu ở mục 1.2). Thứ hai, nó cho phép **kiyểm định đối chiếu**: các kết quả P6 cần consistent với bản 2023 ở những điyểm cơ bản (signs, magnitude direction); nếu dịch chuyển lớn, phải giải thích được byảng dữ liệu 2023–2026 mới.

## 1. Định vị và differentiation từ bài ICBEF 2025 (bản nền)

### 1.1 Vai trò trong luận án

P6 thuộc **tầng synthesis** trong khung 4 tầng + digital lens (xem `02_theoretical_framework_vi.md`). Theo cấu trúc 5 chương trong `01_chapter_outline_vi.md`, kết quả P6 đi vào **Ch.4.1 — Kết quả meta-analysis**, đồng thời cung cấp baseline literature cho **Ch.2.3** và đối thoại kết quả tổng hợp ở **Ch.5.1**.

### 1.2 Differentiation từ bài ICBEF 2025

| Yếu tố | ICBEF 2025 (đã công bố) | P6 (cho luận án) |
|---|---|---|
| Coverage | 1977–2022, 113 studies, 200 effect sizes | **1982–2026, target k = 172–269** |
| Moderators chính | Country of origin, industry | Thêm **FDCI, ICRV regime, DPL phase**, top management, sample period |
| Cấp độ phân tích | Random-effects pooled | **Three-level meta-analytic regression** với nested effect sizes |
| Software | MetaEssentials 1.5 | **`metafor` (R)** hoặc **`pymetaR` (Python)** |
| Kết quả chính | $r = 0.07$, $I^2 = 87.92\%$ | Cập nhật và bổ sung moderator analysis sau 4 năm |
| Kết quả mong đợi | Tác động dương nhỏ, dyị biệt cao | Giải thích heterogeneity bằng FDCI × ICRV × DPL |

Differentiation rõ ràng để tránh phản biện "lặp lại". P6 phải có một mục "What's new compared to Do & Phan (2025)" trong manuscript.

## 2. Kiến trúc kế thừa (đã tồn tại, không viết lại)

### 2.1 Script và dữ liệu hiện có

- `scripts/run_search_agent.py`: orchestration cho 5 phases search
- `scripts/build_final_database.py`: tổng hợp `study_database.json` + `references_APA7.md` + `new_studies_only.csv`
- `data/study_database.json`: **46 studies** đã verify, 29 existing + 17 new
- `outputs/synthesis_narrative.md`: narrative với APA 7th citations
- `P6_Meta_Update_Template1.xlsx`: coding template
- `P6_Meta_MASTER_k269.xlsx`: target MASTER pool size **k = 269**
- **Historical**: `MetaEssentials_Correlational_data_1.5...2022.xlsx` (mã hóa gốc 2023), `KÉT_QUẢ_PHÂN_TÍCH_TỔNG_HỌ̆P_NGÀY_18072023.docx` (kết quả gốc)

### 2.2 28 search queries đã thiết kế (theo `search_queries.json`)

| Phase | Mô tả | Query IDs | Mục tiêu |
|---|---|---|---|
| **1** | Core DOI–FP studies | Q01–Q08 | Inverted-U meta, panel ROA, FSTS curvilinear, S-curve, OFDI EMNE, geographic productivity, Tobin Q |
| **2** | Asian / EMNE | Q09–Q16 | Chinese, Japanese, Korean, Indian, ASEAN, Vietnam WBES, Taiwan SME, EMNE springboard |
| **3** | Digital capability moderator | Q17–Q22 | Digitalization × internationalization, IT capability, e-commerce SME, digital transformation, ICT, digital paradox |
| **4** | Institutional moderators | Q23–Q28 | Institutional quality, WGI, institutional voids, corruption, political stability, formal/informal institutions |
| **5** | Web supplemental | WS01–WS04 | Google Scholar, SSRN, MIR/JWB/IBR, WBES studies |

### 2.3 Inclusion/Exclusion criteria (theo `CLAUDE.md`)

**Include** nếu đủ 7 tiêu chí: empirical quantitative DOI–FP; DOI đo bằng FSTS/FATA/export intensity/scope/composite; FP đo bằng ROA/ROS/RoE/Tobin's Q/labor productivity/sales growth/EBIT; firm-level data; đủ statistics tính Pearson $r$; tiếng Anh peer-reviewed; sample không trùng.

**Exclude** nếu: qualitative/conceptual; country-level only; partial correlations không có bivariate; conference abstract only; subjective performance only; trùng sample.

## 3. Ba khoảng trống nghiên cứu chưa có meta nào lấp

Theo `synthesis_narrative.md`, ba gaps cụ thể:

### Gap 1: FDCI moderator chưa có trong meta nào

Mặc dù Bhandari et al. (2023) chứng minh digitalization × internationalization tạo J-shaped pattern với 571 doanh nghiệp sản xuất Mỹ, **interaction này chưa từng được kiyểm định meta-analytic xuyên studies**. P6 là meta-analysis đầu tiên tập hợp **Foundational Digital Capabilities Index (FDCI)** làm moderator cấp country-level (Bhandari et al., 2023; Bustamante et al., 2022; Chen & Meng, 2022; Verhoef et al., 2021).

### Gap 2: Asian institutional heterogeneity chưa được theory hóa đủ

Các meta trước gop "emerging markets" làm một khối đồng nhất, bỏ qua khoả ng cách governance giữa Singapore (WGI Rule of Law $= +1.73$ năm 2022) và Myanmar (WGI RoL $= -1.39$). P6 áp dụng **ICRV 5-regime classification** theo WGI Rule of Law thresholds $+0.80$ và $-0.50$ (Khanna & Palepu, 2010; North, 1990; Do & Phan, 2025).

### Gap 3: Digital Paradox Lifecycle (DPL) phases chưa được operationalize

2009 được xác định là digital inflection point. P6 mã hóa từng study theo điyều kiện dữ liệu **precede / span / follow** mốc 2009 để kiểm định DPL effects (Brynjolfsson et al., 2021; David, 1990; Dzikowski et al., 2023).

## 4. Kế hoạch mở rộng database

### 4.1 Từ 46 → 172 → 269

| Giai đoạn | Pool size | Nguồn mở rộng |
|---|---|---|
| Hiện có | 46 (29 existing + 17 new) | Manual coding + Consensus search ban đầu |
| **Phase A** | 46 → ~120 | Backward citation scan của 6 meta trước (Kirca et al., 2012; Yang & Driffield, 2012; Marano et al., 2016; Schwens et al., 2018; Wu et al., 2022; Arte & Larimo, 2022) |
| **Phase B** | 120 → ~172 | Triển khai đầy đủ 28 queries trong `search_queries.json` qua Consensus + web supplemental |
| **Phase C** | 172 → 269 | Gap-fill: Scopus, SSRN, ResearchGate, journal-specific browsing (MIR, JWB, IBR, JIBS) cho 2023–2026 |

Mục tiêu k = 172 đủ cho three-level MARA với 11 moderators theo Borenstein et al. (2009) và Hedges et al. (2010); k = 269 (per MASTER) cho phép subgroup analysis robust.

### 4.2 Quy trình extraction cho mỗi study mới

Theo template trong `CLAUDE.md`:

```json
{
  "study_id": "SXXX",
  "authors": "Surname, Initial.",
  "year": YYYY,
  "title": "...",
  "journal": "...",
  "volume": "V", "issue": "N", "pages": "pp–pp",
  "doi": "10.XXXX/...",
  "country_sample": "...",
  "n_firms": ..., "n_obs": ..., "time_period": "YYYY-YYYY",
  "doi_measure": "FSTS|FATA|Composite|Scope|Other",
  "fp_measure": "ROA|ROS|TobinQ|LnLP|Other",
  "relationship_found": "InvU|U|Linear+|Linear-|S-curve|NS",
  "r_reported": ..., "beta_reported": ..., "t_stat": ...,
  "sample_size_for_r": ...,
  "digital_moderator": bool, "institutional_moderator": bool,
  "icrv_regime": "I|II|III|SIDS|Frontier|Multi",
  "q10_extractable": bool,
  "already_in_pool": bool,
  "apa7_citation": "..."
}
```

## 5. Phương pháp phân tích

### 5.1 Three-level MARA

Mô hình ba cấp:

- **Level 1**: sai số sampling trong từng effect size $r_{ij}$.
- **Level 2**: variance giữa effect sizes trong cùng study (do nhiều DOI/FP measures hoyặc subsamples).
- **Level 3**: variance giữa studies (true heterogeneity giải thích bởi moderators).

Cấu trúc này theo Cheung (2014) và Van den Noortgate et al. (2013), sử dụng package `metafor` trong R hoặc `pymetaR` trong Python.

**Lý do chuyển software từ MetaEssentials**: MetaEssentials (Suurmond et al., 2017) phù hợp cho random-effects pooled cơ bản nhưng không hỗ trợ three-level nested model. Với 11 moderators và nested effect sizes, cần công cụ mạnh hơn. Kết quả cơ bản của 2023 (MetaEssentials) sẽ được tái kiểm bằng `metafor` để đảm bảo consistency.

### 5.2 11 moderators theo kế hoạch

1. **Country of origin** (categorical: Asia, Europe, US, Other)
2. **ICRV regime** (categorical: I, II, III, SIDS, Frontier)
3. **Industry** (manufacturing, services, multi)
4. **DOI measure type** (FSTS, FATA, scope, composite)
5. **FP measure type** (accounting, market-based, productivity)
6. **DPL phase** (pre-2009, span-2009, post-2009)
7. **FDCI level** (high, medium, low country-level digital capability)
8. **Sample size** (continuous, log-transformed)
9. **Publication year** (continuous)
10. **Digital moderator presence** (binary)
11. **Institutional moderator presence** (binary)

### 5.3 Publication bias

Tất cả kiểm định chuẩn: Egger's test (Egger et al., 1997), Begg-Mazumdar (Begg & Mazumdar, 1994), trim-and-fill (Duval & Tweedie, 2000), funnel plot, fail-safe N.

### 5.4 Robustness

- Leave-one-out sensitivity
- Subgroup theo Asian-only sample
- Excluding outliers (effect size > 3 SD)
- Restricted Maximum Likelihood (REML) vs DerSimonian-Laird estimator
- **Consistency check** với bản 2023 (MetaEssentials) cho cụm 113 studies gốc

## 6. Lộ trình triển khai

### Tuần 1–2: Verify hiện trạng và đối chiếu lineage

- Kiyểm tra `study_database.json` (46 studies hiện có) và verify DOI accuracy
- Đối chiếu với MASTER `P6_Meta_MASTER_k269.xlsx` (kể cả 269 entries)
- **Đối chiếu với `MetaEssentials_Correlational_data_1.5...2022.xlsx`** để đảm bảo database 46 có đầy đủ 113 studies gốc
- Nếu MASTER đã có 269 entries: ưu tiên import + verify, không search lại từ đầu

### Tuần 3–6: Phase A — Backward citation scan

- Triển khai 6 meta-analyses cor (Kirca et al., 2012; Yang & Driffield, 2012; Marano et al., 2016; Schwens et al., 2018; Wu et al., 2022; Arte & Larimo, 2022)
- Extract reference lists, verify DOI và inclusion criteria
- Mục tiêu: tăng pool từ 46 → ~120

### Tuần 7–10: Phase B — 28 queries

- Chạy `python scripts/run_search_agent.py --phase all --max_per_query 20`
- Thực hiện mỗi query qua Consensus MCP + verify kết quả
- Mục tiêu: tăng pool lên ~172

### Tuần 11–12: Phase C — Gap-fill

- Web search supplemental (WS01–WS04)
- Scopus/SSRN browsing cho 2023–2026
- Mục tiêu: pool MASTER ~269

### Tuần 13–16: Coding và phân tích

- Hoàn thiện coding cho 11 moderators
- Three-level MARA trong R (`metafor`) hoặc Python
- Publication bias tests
- Robustness sensitivity analysis
- **Consistency check**: tái chạy 113-study subset bằng `metafor` và đối chiếu với bản 2023

### Tuần 17–20: Viết manuscript

- Introduction (mạnh về differentiation từ ICBEF 2025)
- Method (PRISMA flow, three-level MARA detail)
- Results (forest plot, funnel plot, moderator tables)
- Discussion (đối thoại với 6 meta trước, FDCI gap, ICRV gap, DPL gap)

## 7. Đóng góp kỳ vọng của P6

### 7.1 Methodological

- Meta-analysis đầu tiên trên DOI–FP sử dụng **three-level MARA** với nested effect sizes ở Asian context.
- Lần đầu tiên kiểm định **FDCI** như country-level moderator.
- Lần đầu tiên opérer **ICRV 5-regime classification** theo WGI thresholds định lượng.

### 7.2 Theoretical

- Bằng chứng systematic cho **Capability–Institution Mismatch** trong bối cảnh emerging Asia.
- Kiểm định **Digital Paradox Lifecycle** (DPL) qua mốc 2009 inflection.
- Mở rộng tranh luận về internalization theory cho digital era (Banalieva & Dhanaraj, 2019).

### 7.3 Empirical

- Pool 172–269 studies là quy mô cao hơn các meta trước cho châu Á.
- Cung cấp baseline cho các chapter tiếp theo của luận án.
- Reference list APA 7th đầy đủ cho tác giả và cộng đồng nghiên cứu.

## 8. Risks và mitigation

| Risk | Mitigation |
|---|---|
| Pool 172 không đạt do thiếu high-quality 2023–2026 papers | Muốn flexible: chấp nhận k = 150 nếu Asian/digital coverage đủ mạnh |
| Reverse causality (Schmuck et al., 2022) | Coding biến study design (cross-section vs panel) và lag structure |
| FDCI proxy variation giữa countries | Dùng ITU DDI và World Bank Digital Adoption Index như country-level proxies; coding rationale minh bạch |
| ICRV regime thresholds cần biyện minh | Robustness với alternative thresholds ($+0.5/-0.3$ vs $+0.8/-0.5$) |
| Trung lặp sample (vd: nhiều nghiên cứu Lu & Beamish data Japan) | Coding "sample_id" đồng nhất; chỉ giữ effect size có trọng số cao nhất cho mỗi sample-construct combination |
| Inconsistency với bản 2023 sau khi tái chạy `metafor` | Nếu có inconsistency, document trong appendix và giải thích (do estimator khác, do data updates, v.v.) |

## 9. Kết nối với các file khác trong `/thesis/`

- `00_optimal_plan_vi.md`: P6 đóng góp meta-analytic synthesis cho tính mới về phương pháp
- `01_chapter_outline_vi.md`: Kết quả P6 vào Ch.4.1; baseline literature vào Ch.2.3; integration vào Ch.5.1
- `02_theoretical_framework_vi.md`: P6 cung cấp evidence cho hệ giả thuyết (đặc biệt H1 phi tuyến và H6 temporal)
- `03_methodology_vi.md`: Mục 4.1 chi tiết three-level MARA kế thừa file này
- `04_references_apa7.md`: Tất cả reference từ P6 đã được đưa vào danh mục chung
- `05_p5_china_design_vi.md`: P5 và P6 cùng kiyểm định H6 (temporal heterogeneity) ở hai cấp độ khác nhau

## 10. Tham khảo chính (đầy đủ trong `04_references_apa7.md`)

Arte, P., & Larimo, J. (2022). Moderating influence of product diversification on the international diversification–performance relationship: A meta-analysis. *Journal of Business Research, 139*, 1408–1423.

Banalieva, E. R., & Dhanaraj, C. (2019). Internalization theory for the digital economy. *Journal of International Business Studies, 50*(8), 1372–1387.

Bausch, A., & Krist, M. (2007). The effect of context-related moderators on the internationalization–performance relationship: Evidence from meta-analysis. *Management International Review, 47*(3), 319–347.

Begg, C. B., & Mazumdar, M. (1994). Operating characteristics of a rank correlation test for publication bias. *Biometrics, 50*(4), 1088–1101.

Bhandari, K. R., Zámborský, P., Ranta, M., & Salo, J. (2023). Digitalization, internationalization, and firm performance. *International Business Review, 32*(4), 102027.

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009). *Introduction to meta-analysis*. Wiley.

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics, 13*(1), 333–372.

Cheung, M. W.-L. (2014). Modeling dependent effect sizes with three-level meta-analyses: A structural equation modeling approach. *Psychological Methods, 19*(2), 211–229.

David, P. A. (1990). The dynamo and the computer: An historical perspective on the modern productivity paradox. *American Economic Review, 80*(2), 355–361.

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot-based method of testing and adjusting for publication bias in meta-analysis. *Biometrics, 56*(2), 455–463.

Dzikowski, P., Tomczyk, E., & Chlebus, M. (2023). Do digital technologies pay off? A meta-analytic review of the digital technologies/firm performance nexus. *Technovation, 128*, 102838.

Egger, M., Davey Smith, G., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *British Medical Journal, 315*(7109), 629–634.

Hedges, L. V., Tipton, E., & Johnson, M. C. (2010). Robust variance estimation in meta-regression with dependent effect size estimates. *Research Synthesis Methods, 1*(1), 39–65.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Roth, K., Hult, G. T. M., & Cavusgil, S. T. (2012). The role of context in the multinationality–performance relationship: A meta-analytic review. *Global Strategy Journal, 2*(2), 108–121.

Marano, V., Arregle, J. L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization–performance relationship: A meta-analytic review. *Journal of Management, 42*(5), 1075–1110.

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71.

Schwens, C., Zapkau, F. B., Bierwerth, M., Isidor, R., Knight, G., & Kabst, R. (2018). International entrepreneurship: A meta-analysis. *Entrepreneurship Theory and Practice, 42*(5), 734–768.

Suurmond, R., van Rhee, H., & Hak, T. (2017). Introduction, comparison, and validation of Meta-Essentials: A free and simple tool for meta-analysis. *Research Synthesis Methods, 8*(4), 537–553. https://doi.org/10.1002/jrsm.1260

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901.

Wu, J., Fan, D., & Chen, X. (2022). Revisiting the internationalization–performance relationship: A twenty-year meta-analysis of emerging market multinationals. *Management International Review, 62*(2), 199–231.

Yang, Y., & Driffield, N. (2012). Multinationality–performance relationship. *Management International Review, 52*(1), 23–47.
