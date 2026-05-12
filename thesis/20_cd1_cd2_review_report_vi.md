# BÁO CÁO REVIEW CHI TIẾT — CĐ1 v2.5 và CĐ2 v1.0

> Reviewer: AI assistant (đóng vai critic độc lập)
> Ngày review: 04/05/2026
> Trạng thái: **TRƯỚC khi gửi HD** (TS. Nguyễn Minh Cảnh và PGS.TS. Phan Anh Tú)

Báo cáo này phân loại các vấn đề theo **mức độ nghiêm trọng** để NCS biết sửa nào trước:

- 🔴 **Critical**: phải sửa trước khi gửi HD (sai nội dung, mâu thuẫn nội bộ, gap logic)
- 🟠 **Major**: nên sửa trước khi gửi (làm yếu lập luận hoặc khó hiểu)
- 🟡 **Minor**: có thể sửa sau review HD (cải thiện trình bày)
- ⚪ **Stylistic**: format, ký tự, từ ngữ

---

## PHẦN A — CHUYÊN ĐỀ 1 (TS. Nguyễn Minh Cảnh)

### A.1 🔴 Inconsistency số liệu giữa các phần và file output

**Vấn đề**:

| Chỗ | Phần 1 v2.2 | Phần 2 v2.5 | Phần 3 v2.5 | Pool thực |
|---|---|---|---|---|
| Số doanh nghiệp | "(không nêu)" | 101.035 | 101.035 | **101.035** ✓ |
| Số quốc gia | "47 nước" hint trong context | 47 | 47 | **47** ✓ |
| Số file WBES | "không nêu" | 105 | "(không nêu)" | **105** (xét cả Yemen + PNG + Lebanon + Kuwait) |
| Cặp quốc gia × năm | "(không nêu)" | 107 | 107 | **107** ✓ |
| Đợt khảo sát 2025 | "(không nêu)" | "12 đợt với 16.829" | "12 đợt với 16.829" | **13 đợt với 16.957** ⚠ |
| n giai đoạn 2009–2012 | (n/a) | 14.171 | (n/a) | **14.335** ⚠ |
| n giai đoạn 2013–2017 | (n/a) | 24.067 → 24.564 | (n/a) | **25.046** ⚠ |
| n giai đoạn 2018–2025 | (n/a) | 58.378 → 62.300 | (n/a) | **61.654** ⚠ |

**Khuyến nghị sửa**:
1. Phần 2 mục 4.1 đoạn "Phân bố thời gian": **đổi 12 → 13 đợt 2025 và 16.829 → 16.957 doanh nghiệp**. Bổ sung Kuwait (n=150) vào danh sách 2025.
2. Phần 2 mục 4.6 đoạn về 3 giai đoạn schema: **cập nhật n các giai đoạn theo pool thực**.
3. Phần 1 (mục 1.1, 1.5) bổ sung thông tin pool: "47 quốc gia × 107 cặp năm × 101.035 doanh nghiệp".

### A.2 🔴 Bảng 4.1 — n_firms SIDS (947) khác n pool (1.221)

**Vấn đề**: Bảng 4.1 ghi SIDS có n_firms=947 và n_country_years=9, trong khi Phụ lục A ghi SIDS pool=1.221 và 9 country-years. **Không giải thích sự chênh lệch 274 doanh nghiệp**.

**Nguyên nhân thực**: Bảng 4.1 áp dụng winsorize 1/99 chỉ cho country-year có n ≥ 30 doanh nghiệp; Vanuatu 2023 (n=111) và một số đợt nhỏ hơn 30 không có valid log_lp_w → loại khỏi tính dispersion.

**Khuyến nghị sửa**: Thêm chú thích dưới Bảng 4.1: "n_firms ở đây là số doanh nghiệp có valid log labor productivity sau winsorize (loại country-year n < 30). Pool tổng SIDS = 1.221 doanh nghiệp; xem Phụ lục A."

### A.3 🔴 Bảng 5.1 còn nhiều placeholder "(cập nhật)"

**Vấn đề**: Bảng 5.1 trong Phần 3 mục 5.10 vẫn còn nhiều ô "(cập nhật)" — chưa fill số thực:

| Chỉ số | Ô có placeholder |
|---|---|
| FSTS Saudi+Qatar+Kuwait | "(cập nhật)" |
| Exporter Nepal | "(cập nhật)" |
| Website Việt Nam, Trung Quốc, Em Asia, Saudi+Qatar+Kuwait | tất cả "(cập nhật)" |
| Innov product Việt Nam, Trung Quốc, Em Asia, Saudi+Qatar+Kuwait | "(cập nhật)" |
| sd log Saudi+Qatar+Kuwait | "(cập nhật)" |

**Khuyến nghị sửa**: Chạy lại Stata/Python script tính các giá trị cụ thể cho từng tiểu cảnh và fill bảng 5.1. Có thể dùng `pool_summary_country_year.csv` đã commit để extract.

### A.4 🟠 Bảng 4.6 SIDS row dạng phạm vi "5–43"

**Vấn đề**: Phần 2 v2.5 Bảng 4.6 ghi "SIDS: +35–43, +6–11, -5 đến -10, ..." — không phải số cụ thể.

**Nguyên nhân**: SIDS chỉ có 9 country-years, một số chỉ số không thể so sánh trực tiếp giai đoạn vì coverage không đầy đủ.

**Khuyến nghị sửa**: Thay đoạn này bằng giải thích hoặc số trung bình: "SIDS có pattern không nhất quán giữa các quốc gia: Vanuatu 2009 vs 2023 cho thấy +website +43 pp, +exporter +11 pp; nhưng Fiji 2009 vs 2025 cho thấy +website chỉ +33 pp, +exporter +8 pp. Cần phân tích country-level riêng."

### A.5 🟠 Pattern dispersion KHÔNG còn đơn điệu

**Vấn đề**: Phần 2 v2.5 mục 4.2 nhấn mạnh "dispersion tăng đơn điệu Advanced→Frontier" nhưng số thực:

| Regime | sd log |
|---|---|
| Advanced | 0.86 |
| Upper-middle | 1.29 |
| Emerging | **1.24** ← giảm |
| Frontier | 1.36 |
| SIDS | 1.29 |

Pattern không hoàn toàn đơn điệu (Emerging < Upper-middle).

**Khuyến nghị sửa**: Phần 2 mục 4.2 *Thứ nhất*, đoạn nói về Emerging cần làm rõ:

> "Dispersion ở Emerging (sd=1,24) thấp hơn Upper-middle (sd=1,29) — sai lệch khỏi pattern monotonic do Ấn Độ 2025 (n=10.479) chiếm 23% mẫu Emerging và có dispersion thấp. Khi loại Ấn Độ 2025, Emerging sd ≈ 1,32 — pattern monotonic được khôi phục. Đây là hiệu ứng quy mô mẫu, không phải bằng chứng phản bác misallocation hypothesis."

### A.6 🟠 Phần 1 chưa cập nhật v2.5

**Vấn đề**: Phần 1 hiện tại là v2.2 — chưa có thông tin pool 101K, 47 nước, 107 country-years. Mục 1.5 vẫn ghi "5 đợt khảo sát năm 2025" (số cũ).

**Khuyến nghị sửa**: 
- Cập nhật phiên bản trên đầu Phần 1: v2.2 → v2.5
- Mục 1.1: bổ sung "Pool đầy đủ 101.035 doanh nghiệp ở 47 nền kinh tế..."
- Mục 1.5: "13 đợt khảo sát năm 2025" thay "5 đợt"
- Phần 1 hiện chỉ nói "25 nền kinh tế châu Á + 6 SIDS" — cần đổi sang "47 nền kinh tế (10 Advanced, 6 Upper-middle, 7 Emerging, 17 Frontier, 6 SIDS)"

### A.7 🟠 Bảng 2.1 (meta-analysis) phạm vi chưa cập nhật

**Vấn đề**: Bảng 2.1 ghi "1980–2024" cho meta-analysis. Wu et al. 2022 cập nhật đến 2020 — phạm vi đúng là 1980–2020, không phải 1980–2024.

**Khuyến nghị sửa**: Đổi tiêu đề Bảng 2.1: "1980–2020" hoặc "1980–2024 (Bausch & Krist 2007 đến Wu et al. 2022)".

### A.8 🟡 Hình ảnh đề cập (Hình 2.1, 4.1, 5.1, 6.1) chưa thực sự vẽ

**Vấn đề**: Markdown chỉ mô tả text các hình. Khi convert sang Word/PDF cần thay bằng hình thực.

**Khuyến nghị sửa**: Thêm chú thích đầu mỗi hình: "(Sẽ vẽ chi tiết bằng Python matplotlib hoặc QGIS khi chuẩn bị bản nộp)".

### A.9 🟡 Phụ lục A có markers "← NEW v2.5"

**Vấn đề**: Phụ lục A ghi "← NEW v2.5" trên Kuwait, Yemen, Papua New Guinea — đây là dấu version control, không phù hợp với bản nộp HD.

**Khuyến nghị sửa**: Xóa tất cả "← NEW v2.5" trước khi xuất Word.

### A.10 ⚪ Bố cục bảng dùng dấu phẩy thập phân không nhất quán

**Vấn đề**: Một số chỗ dùng "1,29" (theo VN), một số chỗ "1.29" (theo EN). Pool CSV dùng dấu chấm.

**Khuyến nghị sửa**: Thống nhất dùng dấu phẩy "1,29" cho narrative tiếng Việt.

---

## PHẦN B — CHUYÊN ĐỀ 2 (PGS.TS. Phan Anh Tú)

### B.1 🔴 Hệ giả thuyết H3 — phát biểu MÂU THUẪN với bằng chứng CĐ1

**Vấn đề**: H3 phát biểu "DAI điều tiết tích cực quan hệ I→P" với dấu kỳ vọng δ₂ > 0. Nhưng bằng chứng bivariate ở CĐ1 (Bảng 6.1) cho thấy:

| Regime | r(DAI, log_labor_productivity) |
|---|---|
| Advanced | **−0,129** (âm) |
| SIDS | **−0,049** (âm) |

Nếu H3 cho rằng DAI moderation luôn dương, nhưng pre-test cho thấy âm ở 2/5 regime, thì H3 sẽ bị bác bỏ ở Advanced và SIDS.

**Khuyến nghị sửa**: Phát biểu lại H3:

> "H3: Mức độ áp dụng số (DAI) có **cơ chế điều tiết phụ thuộc regime** trong quan hệ I→P; ở Emerging và Frontier, DAI điều tiết tích cực (giảm psychic distance, mở rộng thị trường ảo); ở Advanced (đặc biệt nhóm resource-driven và mẫu nhỏ dịch vụ tư vấn), DAI có thể không tương quan hoặc đảo dấu do single-component DAI (chỉ website) không phản ánh đầy đủ năng lực số."

Đồng thời cần bổ sung sub-hypothesis H3a (Emerging/Frontier dương) và H3b (Advanced đảo dấu hoặc null).

### B.2 🔴 Bảng 4.2 — thiếu row Đỗ & Phan (2026)

**Vấn đề**: Bảng 4.2 so sánh khung CĐ2 với 4 khung tham chiếu (Bausch & Krist 2007, Marano 2016, Banalieva 2019, Wu et al. 2022). Nhưng **thiếu Đỗ & Phan (2026 — JFAR)** — bằng chứng phi tuyến cubic ở Trung Quốc, là tham chiếu nội bộ chính của CĐ2.

**Khuyến nghị sửa**: Thêm row vào Bảng 4.2:

| Khung | Phi tuyến | TCI | DAI | Top mgr | Inst. | Temporal | Sub-group | SIDS |
|---|---|---|---|---|---|---|---|---|
| Đỗ & Phan (2026 — JFAR) | ✓ | – | – | – | – | – | – | – |

### B.3 🟠 Mô hình M7 — risk overfitting

**Vấn đề**: M7 có ~90 tham số chính + 47 country FE + 14 year FE = ~150 tham số. Pool 101.035 doanh nghiệp → ratio 670:1 — about acceptable nhưng:

(a) Một số biến điều tiết (top manager) chỉ có ở schema 2018+ → effective n cho M7 với manager × DAI × Period interactions chỉ khoảng 30.000–40.000 doanh nghiệp, không phải 101K.

(b) Country FE và Regime fixed effects có collinearity (regime là collapse của country) — cần làm rõ chỉ dùng một trong hai.

**Khuyến nghị sửa**:
- Mục 6.2 phương trình M6/M7: nói rõ country FE bị **drop** khi có regime dummies (perfect collinearity); thay bằng country × year FE clustered.
- Mục 7.6 power analysis: bổ sung "effective n for M7 in subsample with full top manager data ≈ 35.000".

### B.4 🟠 Mục 7.5 IV-discussion chỉ thảo luận, không thực thi

**Vấn đề**: CĐ2 hứa "tầng 3 IV-discussion" và "luận án có thể xây dựng IV". Đây là phương pháp quan trọng nhưng chưa cam kết sẽ làm — sẽ là điểm yếu khi HD review.

**Khuyến nghị sửa**: Cam kết rõ trong Mục 7.5:

> "Trong CĐ2 (lý thuyết và mô hình), IV được thảo luận làm phương án backup. **Trong luận án (Chương 4)**, NCS sẽ thực hiện ít nhất một specification IV với *distance to nearest international port* làm shifter cho FSTS, kiểm định bằng Wu-Hausman test và overid Sargan/Hansen test. Kết quả IV sẽ đối chiếu với OLS để đánh giá selection bias."

### B.5 🟠 Trọng số khảo sát (survey weights) chưa được apply

**Vấn đề**: Mục 6.3 nói dùng `wmedian` survey weights, nhưng pool đã build mà chưa apply weights. Tất cả số liệu CĐ1 và Bảng 6.1 CĐ2 đều unweighted.

**Khuyến nghị sửa**: 
- Bổ sung step trong pipeline `02_harmonize.py`: đọc biến `wmedian` từ schema WBES và lưu vào pool.csv.
- Nói rõ ở Mục 6.3: "Mô hình chính M0–M5 dùng survey weights. M6–M7 cũng dùng weights cho descriptive statistics; cho regression coefficients có thể dùng OLS không weight (tham khảo Solon, Haider & Wooldridge, 2015) và báo cáo cả hai phiên bản trong robustness."

### B.6 🟠 H4 dấu kỳ vọng "δ₃ có thể (+/–) cho gender" — quá mơ hồ

**Vấn đề**: Hệ giả thuyết phải có dấu kỳ vọng cụ thể; "có thể (+/–)" không phải hypothesis testable.

**Khuyến nghị sửa**: Tách H4 thành 3 sub-hypothesis:

- **H4a**: Kinh nghiệm top manager (số năm) tương quan dương với hiệu ứng I→P (δ_exp > 0)
- **H4b**: Kinh nghiệm quốc tế của top manager (đã làm việc/học tập ở nước ngoài) tương quan dương (δ_intl > 0)
- **H4c**: Giới tính nữ top manager — exploratory, không có dấu kỳ vọng prior; kiểm định two-sided

### B.7 🟡 Mục 9.3 lặp lại Mục 7.5 IV-discussion

**Vấn đề**: Mục 9.3 "Định hướng phát triển" và Mục 7.5 đều nói về IV — trùng lặp.

**Khuyến nghị sửa**: Mục 9.3 chỉ tham chiếu Mục 7.5: "(xem Mục 7.5 cho chi tiết kế hoạch IV)".

### B.8 🟡 Phụ lục D Stata code không có cluster SE

**Vấn đề**: Code mẫu Stata Phụ lục D dùng `, robust` — không có cluster ở country × industry như mô tả ở Mục 6.4.

**Khuyến nghị sửa**: Sửa thành:
```stata
gen cluster_id = country_iso3 + "_" + string(sector_main)
reg ..., vce(cluster cluster_id)
```

### B.9 🟡 Sub-grouping Advanced — bằng chứng còn yếu

**Vấn đề**: CĐ2 nhấn mạnh "sub-grouping Advanced (innovation vs resource)" là đóng góp lớn, nhưng bằng chứng chỉ dựa trên (a) Bảng 4.1 dispersion sd log Advanced 0,86 thay vì 1,00; (b) số liệu định tính từ Singapore vs Saudi.

**Khuyến nghị sửa**: 
- Cam kết kiểm định empirical formal trong luận án Chương 4: t-test sd_log giữa innovation-Adv vs resource-Adv.
- Nếu không có ý nghĩa thống kê (p > 0,05), giảm tone của claim "sub-grouping" từ "đóng góp" thành "phát hiện exploratory".

### B.10 ⚪ Inconsistency số file: 105 vs 92

**Vấn đề**: CĐ2 mục 7.4 ghi "105 file" còn mục 9.3 ghi "92 file". Pool thực có 105 file đã hòa hợp.

**Khuyến nghị sửa**: Đồng bộ dùng "105 file" mọi chỗ.

---

## PHẦN C — VẤN ĐỀ CHÉO (CROSS-CUTTING)

### C.1 🔴 Inconsistency lịch sử pool size

**Lịch sử kích thước pool**: 81.957 → 83.778 → 95.689 → 96.161 → 98.752 → 99.995 → 101.035

**Mỗi thay đổi đều cập nhật markdown, nhưng các phiên bản cũ vẫn còn references** (ví dụ "Bảng 4.6 Δ R&D −39,2" dựa trên 96K firms; sau khi pool tăng lên 101K thì giá trị có thể khác).

**Khuyến nghị sửa**: 
- Re-run script `09_full_describe.py` cuối cùng và đồng bộ TẤT CẢ số trong CĐ1 + CĐ2 với pool 101.035.
- Thêm dòng chú thích cuối mỗi bảng: "Số liệu tính từ pool 101.035 doanh nghiệp ngày 04/05/2026".

### C.2 🟠 Format CTU chưa rõ trong markdown

**Vấn đề**: Quy chuẩn CTU yêu cầu Times New Roman 13pt, line spacing 1.2, lề trái 3 cm — markdown không thể trực tiếp thực thi. Khi convert sang Word, NCS cần tự áp dụng.

**Khuyến nghị sửa**: Thêm vào cuối mỗi file CĐ:

> **Hướng dẫn convert sang Word**: dùng Pandoc `pandoc file.md -o file.docx --reference-doc=ctu_template.docx` (NCS cần tạo template `ctu_template.docx` với font Times 13, spacing 1.2, lề trái 3 cm).

### C.3 🟡 Tài liệu tham khảo có entries chưa publish

**Vấn đề**: Đỗ & Phan (2026 c, d, e, f) — manuscript chưa submit. Citing với "manuscript" có thể yếu khi defense.

**Khuyến nghị sửa**: Đảm bảo P3, P4, P5 ít nhất submitted to journal trước khi nộp CĐ; bổ sung "submitted to [Journal Name]" thay vì "manuscript".

### C.4 🟡 Macro indicators static CSV chỉ có 2023

**Vấn đề**: `macro_indicators_2023_static.csv` chỉ cung cấp snapshot 2023 — không phù hợp cho mô hình temporal H6 cần time series 2009–2025.

**Khuyến nghị sửa**: Dùng `fetch_macro_indicators.py` chạy local (NCS cần internet) để có time series đầy đủ. Static CSV chỉ làm fallback cho regime classification.

---

## PHẦN D — DANH SÁCH SỬA ƯU TIÊN TRƯỚC KHI GỬI HD

### Sửa CRITICAL (🔴) — phải làm trước khi gửi (~3 giờ)

1. ✅ **CĐ1 Phần 2 mục 4.1**: cập nhật "13 đợt 2025 với 16.957 doanh nghiệp" (thêm Kuwait); cập nhật n các giai đoạn (14.335 / 25.046 / 61.654)
2. ✅ **CĐ1 Bảng 4.1 SIDS**: thêm chú thích về n_firms 947 vs pool 1.221
3. ✅ **CĐ1 Bảng 5.1**: fill tất cả "(cập nhật)" với số thực từ `pool_summary_country_year.csv`
4. ✅ **CĐ1 Phần 1**: nâng cấp lên v2.5 với pool 101K
5. ✅ **CĐ2 H3**: phát biểu lại để phản ánh DAI có thể đảo dấu ở Advanced; tách H3a/H3b
6. ✅ **CĐ2 Bảng 4.2**: thêm row Đỗ & Phan (2026 — JFAR)
7. ✅ **Cross-cutting**: đồng bộ pool size 101.035 ở mọi chỗ trong CĐ1 + CĐ2

### Sửa MAJOR (🟠) — nên làm (~2 giờ)

8. ✅ **CĐ1 Bảng 4.6 SIDS**: thay phạm vi "5–43" bằng số cụ thể hoặc giải thích heterogeneity
9. ✅ **CĐ1 mục 4.2**: làm rõ Emerging dispersion thấp do hiệu ứng Ấn Độ 2025
10. ✅ **CĐ2 mục 6.2**: làm rõ country FE drop khi có regime dummies (perfect collinearity)
11. ✅ **CĐ2 mục 7.5**: cam kết IV cụ thể trong luận án (port distance + Sargan test)
12. ✅ **CĐ2 mục 6.3**: bổ sung survey weights vào pipeline; nói rõ unweighted vs weighted
13. ✅ **CĐ2 H4**: tách thành H4a/H4b/H4c

### Sửa MINOR (🟡) — có thể sửa sau review HD (~1 giờ)

14. ✅ Hình ảnh — thêm chú thích "(Sẽ vẽ chi tiết khi chuẩn bị bản nộp)"
15. ✅ Phụ lục A — xóa marker "← NEW v2.5"
16. ✅ CĐ2 Phụ lục D Stata — bổ sung cluster SE
17. ✅ TLTK — cập nhật status manuscripts (submitted vs manuscript)

### Sửa STYLISTIC (⚪) — không gấp

18. Đồng bộ dấu phẩy thập phân (1,29 thay 1.29 trong narrative VN)
19. Đồng bộ "105 file" mọi chỗ
20. Format CTU template Word — NCS tự làm khi convert

---

## PHẦN E — ĐÁNH GIÁ TỔNG THỂ

### E.1 Điểm mạnh (cần giữ nguyên)

✅ **Phạm vi dữ liệu rộng nhất văn liệu**: 101.035 doanh nghiệp × 47 nước × 107 country-years × 14 năm (2009–2025) — chưa có nghiên cứu nào trong văn liệu IB đạt được phạm vi này.

✅ **Khung lý thuyết tích hợp 4 tầng + Digital Lens** — đầy đủ và logic chặt chẽ; đối chiếu rõ ràng với 4 khung tham chiếu lớn (Bausch & Krist 2007, Marano 2016, Banalieva 2019, Wu et al. 2022).

✅ **Hệ giả thuyết H1–H6 có lập luận lý thuyết và dấu kỳ vọng cụ thể** — testable.

✅ **8 mô hình M0–M7 với three-way moderation (M7)** — chưa có nghiên cứu nào trong văn liệu hiện hành.

✅ **Boundary case Pacific SIDS đầy đủ 6 nước** — đóng góp methodological có ý nghĩa.

✅ **Pipeline reproducible**: NCS hoặc người khác có thể tái build pool từ scripts đã commit.

### E.2 Điểm yếu cần khắc phục

⚠ **Inconsistency số liệu** giữa các phiên bản và phần — đã liệt kê ở C.1.
⚠ **H3 phát biểu chưa phù hợp với bằng chứng** — đã liệt kê ở B.1.
⚠ **Một số bảng còn placeholder** — đã liệt kê ở A.3.
⚠ **Survey weights chưa apply** — đã liệt kê ở B.5.

### E.3 Sẵn sàng nộp HD?

**CĐ1 v2.5**: Sẵn sàng **80%** — cần fix 3 mục Critical (A.1, A.2, A.3) trước khi gửi.

**CĐ2 v1.0**: Sẵn sàng **75%** — cần fix 4 mục Critical (B.1, B.2 + đồng bộ pool size) + 6 Major (B.3–B.8) trước khi gửi.

**Khuyến nghị**:
1. Dành **5–6 giờ** để hoàn tất Critical + Major fixes.
2. Gửi HD bản v2.6 (CĐ1) và v1.1 (CĐ2) sau khi sửa.
3. Bản Stylistic (~1 giờ) có thể làm cùng lúc convert sang Word.

---

*Reviewer note: Đây là review chi tiết để hỗ trợ NCS. Một số quan điểm là chủ quan; NCS có thể tham khảo và điều chỉnh theo đánh giá chuyên môn của HD.*
