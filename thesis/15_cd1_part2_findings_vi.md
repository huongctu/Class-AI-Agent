# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> Bảng thuật ngữ Anh-Việt: `thesis/09b_vn_term_glossary.md`.
> **Phiên bản 2.5–2.6**: Pool 101.035 firms · 47 nước · 107 country-years · 2009–2025.
> **Phiên bản 2.7–2.9 (D1–D3)**: §4.9 Sub-grouping Emerging + §4.10 2025 wave deep dive + §4.8 Industry-level framework.
> **Phiên bản 2.10 (D4 — final)**: §4.7 expanded summary với 10 kết luận chính.
> **Phiên bản 3.0 (06/05/2026)**: Biên tập tiếng Việt học thuật toàn bộ Chương 4.
> **Phiên bản 3.1a (06/05/2026 — Quick Win 1 từ review report HD 07/05/2026)**: Tách Bảng 4.1 phân nhóm Advanced thành hai phân nhóm con (innovation-driven so với resource-driven) — bằng chứng định lượng tỷ số phân tán 2,1 lần (Singapore 1,03 so với Vùng Vịnh 0,49). Đáp ứng review point D.2(3): "Bảng 4.1 thiếu phân nhóm con Advanced".

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi tổng hợp dữ liệu**. Nhóm dữ liệu (pool) gồm 101.035 doanh nghiệp, 47 nền kinh tế, 107 cặp quốc gia × năm, giai đoạn 2009–2025. Tổng hợp này kế thừa và mở rộng từ nhóm dữ liệu 17 nước châu Á mới nổi (~40.633 doanh nghiệp) của Đỗ & Phan (2026 — VEFR), gấp ~2,5 lần. Phân bố theo phân nhóm con (sub-regime) ICRV: Emerging 47.803 (47%), Frontier 28.678 (28%), Upper-middle 16.693 (17%), Advanced 6.640 (7%), SIDS 1.221 (1%). Có 12 đợt khảo sát năm 2025 với 16.829 doanh nghiệp.

**Trường hợp biên (boundary cases)**: 6 SIDS Thái Bình Dương đầy đủ (FJI, PNG, SLB, TON, VUT, WSM) + Tây Á 9 nước (Vùng Vịnh + Trung Đông). Phân bố thời gian: 2009–2012 (n=14.171), 2013–2017 (n=24.564), 2018–2025 (n=62.300 — chiếm 62%). Ba thế hệ khung dữ liệu (schema): PICS3/MENA-WBES, Standardized, Standardized2018+/BREADY.

**Hài hòa**. Pipeline Python (`wbes/02_harmonize.py`); FSTS = `d3b + d3c`; giới hạn cực trị (winsorize) log năng suất ở mức 1/99 phân vị trong cụm quốc gia × năm. Doanh thu chưa quy đổi sang USD PPP.

### 4.2 Thực trạng năng suất lao động — phân tán trong từng quốc gia

**Bảng 4.1**. *Phân tán (dispersion) năng suất lao động theo phân nhóm con thể chế (n=107 cặp quốc gia × năm).*

| Phân nhóm con | Cặp QG×năm | n_firms | sd log | P90/P10 | P75/P25 |
|---|---|---|---|---|---|
| **Advanced — innovation-driven** *(SG, HK, KOR, TWN, ISR)* | ~8 | ~4.220 | **1,03** | (cập nhật GĐ1) | (cập nhật GĐ1) |
| **Advanced — resource-driven** *(SAU, QAT, KWT, BHR, BRN)* | ~5 | ~1.932 | **0,49** | (cập nhật GĐ1) | (cập nhật GĐ1) |
| *Advanced (gộp — tham chiếu)* | 13 | 5.921 | 0,86 | 10,8 | 3,1 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 20 | 45.388 | 1,24 | 30,6 | 5,1 |
| Frontier | 42 | 18.877 | 1,36 | 39,6 | 6,1 |
| SIDS | 9 | 947 | 1,29 | 27,6 | 5,4 |

*Ghi chú: Phân nhóm Advanced được tách thành hai phân nhóm con (innovation-driven so với resource-driven) ở v3.1 theo phát hiện (ii) §4.7. **Tỷ số phân tán Singapore (1,03) so với Vùng Vịnh (0,49) ≈ 2,1 lần** — bằng chứng định lượng cho phân nhóm con (sub-grouping) Advanced. Số liệu chi tiết P90/P10 và P75/P25 cho từng phân nhóm con sẽ được cập nhật ở Giai đoạn 1 hoàn thiện CĐ1 (tháng 6/2026 — sau khi pool có biến quy đổi USD PPP). Hàng "Advanced (gộp)" giữ lại để tham chiếu so sánh xuyên các phiên bản trước.*

5 phát hiện: (1) Phân tán phân nhóm Advanced gộp giảm từ 1,00 (chỉ innovation-driven) xuống 0,86 (sau khi bổ sung Vùng Vịnh resource-driven) — bằng chứng dị biệt nội bộ; (2) Frontier cao nhất — phù hợp giả thuyết **phân bổ sai nguồn lực (misallocation hypothesis)** của Hsieh & Klenow (2009, 2014); (3) SIDS ở mức trung bình; (4) tỷ số P90/P10 tăng đơn điệu theo phân nhóm con; (5) bằng chứng thực tiễn cho H5 — điều tiết thể chế (institutional moderation).

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

**Bảng 4.3**. *Cường độ xuất khẩu (FSTS), tỷ lệ doanh nghiệp xuất khẩu và tốc độ tăng trưởng kép hàng năm (CAGR — Compound Annual Growth Rate) việc làm theo phân nhóm con.*

| Phân nhóm con | FSTS (%) | Doanh nghiệp xuất khẩu (%) | CAGR việc làm (%) |
|---|---|---|---|
| Advanced | 10,2 | 23,0 | 3,15 |
| Upper-middle | 10,3 | 21,7 | 4,25 |
| Emerging | 8,6 | 15,5 | 2,81 |
| Frontier | 10,1 | 16,6 | 3,65 |
| SIDS | 6,3 | 16,3 | 5,77 |

Trung vị FSTS bằng 0% — phân phối phân cực mạnh; SIDS có CAGR việc làm cao nhất.

### 4.4 Thực trạng đổi mới sáng tạo và năng lực số

**Bảng 4.4**. *Đổi mới sáng tạo và áp dụng số (%).*

| Phân nhóm con | Sản phẩm mới | Quy trình mới | R&D | ISO | Website |
|---|---|---|---|---|---|
| Advanced | 22,3 | 52,3 | 16,7 | 29,9 | 59,3 |
| Upper-middle | 26,7 | 71,7 | 21,0 | 31,4 | 56,9 |
| Emerging | 17,5 | 65,2 | 16,4 | 24,9 | 49,2 |
| Frontier | 23,1 | 68,9 | 14,2 | 20,7 | 38,0 |
| SIDS Thái Bình Dương | **41,5** | 65,1 | 11,8 | 16,5 | **58,9** |

SIDS Thái Bình Dương thể hiện pattern **thích nghi và nhảy vọt số (adaptation + digital leapfrog)**; phân tách rõ Năng lực công nghệ (TCI) so với Năng lực số (DAI) — kế thừa Đỗ & Phan (2026 — VEFR).

### 4.5 Thực trạng cấu trúc doanh nghiệp

**Bảng 4.5**. *Cấu trúc doanh nghiệp theo phân nhóm con (%).*

| Phân nhóm con | SME | Doanh nghiệp xuất khẩu | FDI ≥10% |
|---|---|---|---|
| Advanced | 79,1 | 23,0 | 11,1 |
| Upper-middle | 76,2 | 21,7 | 8,4 |
| Emerging | 74,4 | 15,5 | 4,7 |
| Frontier | 85,0 | 16,5 | 5,9 |
| SIDS Thái Bình Dương | **88,5** | 16,3 | **23,5** |

Tỷ lệ FDI có dạng chữ U với cực tiểu ở Emerging. SIDS cao nhất do du lịch (tourism) và viễn thông được dẫn dắt bởi doanh nghiệp đa quốc gia (MNE-driven).

### 4.6 Bức tranh thay đổi theo thời gian

**Bảng 4.6**. *Δ điểm phần trăm (đpt) khi so sánh 2018–2025 với 2009–2012.*

| Phân nhóm con | Δ Website | Δ Doanh nghiệp xuất khẩu | Δ FDI | Δ R&D | Δ ISO |
|---|---|---|---|---|---|
| Upper-middle | -9,9 | +1,4 | +2,3 | +21,5 | -25,4 |
| Emerging | +20,3 | -7,5 | -10,9 | -42,1 | +1,9 |
| Frontier | +22,1 | +1,5 | -6,5 | -18,9 | +18,5 |
| SIDS Thái Bình Dương | +35–43 | +6–11 | -5 đến -10 | (cập nhật) | -20 đến -25 |

Nhảy vọt số (digital leapfrog): website tăng +20–43 đpt ở Frontier, Emerging và SIDS Thái Bình Dương — phù hợp luận điểm digital leapfrog của Banalieva & Dhanaraj (2019).

### 4.7 Tổng hợp Chương 4 (mở rộng D4 — 10 kết luận chính)

Chương 4 cung cấp bức tranh thực trạng đa chiều dựa trên **101.035 doanh nghiệp ở 47 nền kinh tế châu Á và Thái Bình Dương (107 cặp quốc gia × năm) trong giai đoạn 2009–2025** từ nhóm dữ liệu WBES sau hài hòa. Đây là nhóm dữ liệu có **phạm vi địa lý và thời gian rộng nhất từng được tổng hợp** cho nghiên cứu quan hệ quốc tế hóa → hiệu quả (I→P) trong văn liệu IB. Phạm vi này mở rộng từ nhóm dữ liệu 17 nước châu Á mới nổi (~40.633 doanh nghiệp) của Đỗ và Phan (2026 — VEFR) khoảng 2,5 lần.

**Mười kết luận chính** (mở rộng từ 6 kết luận sơ bộ ở các phiên bản trước, tích hợp các phát hiện D1–D3):

**(i) Phân tán năng suất nội bộ tăng đơn điệu khi phân nhóm con suy giảm**: Advanced 0,86 → Upper-middle 1,29 ≈ Emerging 1,24 ≈ SIDS 1,29 → Frontier 1,36. Tỷ số P90/P10 leo từ 10,8 lần lên 39,6 lần. Pattern này khẳng định **giả thuyết phân bổ sai nguồn lực (misallocation hypothesis)** của Hsieh & Klenow (2009, 2014) và là cơ sở thực tiễn cho H5 — điều tiết thể chế (institutional moderation) — trong CĐ2.

**(ii) Dị biệt nội bộ phân nhóm Advanced — phân nhóm con đổi mới sáng tạo dẫn dắt so với tài nguyên dẫn dắt**. Sự sụt giảm phân tán từ 1,00 (chỉ tính nhóm châu Á đổi mới sáng tạo dẫn dắt — innovation-driven) xuống 0,86 (sau khi thêm Vùng Vịnh tài nguyên dẫn dắt — resource-driven) gợi ý cần **phân nhóm con (sub-grouping) Advanced** trong CĐ2 (xem §5.2 file 16). Đây là phát hiện mới so với cơ sở 17 nước (Đỗ & Phan, 2026 — VEFR vốn không bao gồm phân nhóm Advanced). Bằng chứng định lượng: tỷ số phân tán Singapore (1,03) so với Vùng Vịnh (0,49) ≈ **2,1 lần** — đã được tách trực quan trong **Bảng 4.1 (v3.1)**.

**(iii) Dị biệt nội bộ phân nhóm Emerging — 3 phân nhóm con** *(NEW D1, §4.9)*. Phân nhóm con FDI dẫn dắt Đông Nam Á (VNM+IDN+PHL, n=13.779; FSTS **13,2%**) khác biệt rõ với phân nhóm con dân số lớn (IND+LKA+JOR, n=32.119; FSTS **7,2%**) và phân nhóm con tài nguyên (MNG, n=1.905; FSTS **5,0%**). Phân tầng FSTS 5,0% – 7,2% – 13,2% bị *che giấu* trong số liệu tổng hợp Emerging (8,6%). Đây là phát hiện phương pháp luận thứ hai cho phân loại 8 phân nhóm con trong CĐ2 (§7.3.2 file 16). Năng lực công nghệ (TCI) ngược dấu giữa ASEAN-3 (R&D 4,8%, ISO 18,8%) và Nam Á + Tây Á (R&D 19,8%, ISO 27,6%) — phản ánh hai cơ chế: học hỏi do FDI dẫn dắt (FDI-induced learning) so với học hỏi tự thân (autonomous learning) (Cohen & Levinthal, 1990).

**(iv) SIDS Thái Bình Dương (6 nước, n=1.221) có pattern đặc trưng "thích nghi và nhảy vọt"**: phân tán ở mức trung bình (sd log = 1,29), tỷ lệ đổi mới sản phẩm cao nhất nhóm (41,5%), tỷ lệ website cao bất ngờ (58,9% — gần ngang Advanced) nhưng R&D thấp (11,8%) và ISO thấp (16,5%). Pattern "nền kinh tế nhỏ – mở – thích nghi – ít sáng tạo gốc" là cơ sở thực tiễn cho **H6 (chi phí buộc phải quốc tế hóa — forced internationalization penalty)**. Đây là bằng chứng đầu tiên trên dữ liệu firm-level WBES cho trường hợp biên này (Briguglio, 1995; Bertram, 2006; Đỗ & Phan, 2026 — bản thảo P8).

**(v) Quốc tế hóa là hiện tượng phân cực ở mọi phân nhóm con thể chế**: trung vị FSTS = 0% xuyên năm phân nhóm con; chỉ 15–23% doanh nghiệp tham gia xuất khẩu. Quan hệ quốc tế hóa → hiệu quả (I→P) ở cấp doanh nghiệp KHÔNG phải hiện tượng phổ quát — nó tập trung ở đuôi phải (right tail) của phân phối. Yêu cầu phương pháp luận: cần phân tích **lựa chọn hai giai đoạn (2-stage selection)** — giai đoạn 1 lựa chọn vào nhóm doanh nghiệp xuất khẩu, giai đoạn 2 cường độ FSTS — trong đặc tả đầy đủ của CĐ2.

**(vi) Nhảy vọt số (digital leapfrog) 2018–2025 ở Frontier, Emerging và SIDS Thái Bình Dương** (+20–43 đpt website). Đây là bằng chứng tái định vị Uppsala cho kỷ nguyên số (Banalieva & Dhanaraj, 2019; Yang, Zhao & Wei, 2025); đồng nhất với pattern hiệu ứng lá chắn số (digital shield effect) đã ghi nhận trên 17 nước (Đỗ & Phan, 2026 — VEFR), nay được mở rộng cho 47 nước.

**(vii) Pattern phi tuyến của FDI ≥10%** — dạng chữ U với cực tiểu ở Emerging (4,7%): Advanced 11,1% → Upper-middle 8,4% → Emerging 4,7% → Frontier 5,9% → SIDS 23,5%. Điều này gợi ý hai mô hình FDI khác nhau: (a) ở Advanced — trung tâm doanh nghiệp đa quốc gia (MNE hub) cộng với Vùng Vịnh hạn chế tỷ lệ sở hữu nước ngoài; (b) ở SIDS — du lịch dẫn dắt (tourism-driven) cộng với viễn thông. Trong khi đó, ở Emerging, thị trường nội địa lớn (IND, IDN) hấp thụ FDI thấp hơn dự kiến.

**(viii) Đợt khảo sát 2025 là *mẫu đơn năm lớn nhất* và *đa dạng nhất* trong nhóm dữ liệu** *(NEW D2, §4.10)*. 12 nước × 16.829 doanh nghiệp (16,7% tổng nhóm dữ liệu) đại diện đầy đủ 5 phân nhóm con ICRV trong cùng đợt. Bốn phát hiện chính:
- (a) **Ấn Độ — sụt FSTS bất thường** từ 7,7% xuống 2,7% (Δ−5 đpt) — nhiều khả năng do thay đổi khung dữ liệu BREADY 2025 cộng chính sách Atmanirbhar Bharat sau COVID;
- (b) **Fiji — nhảy vọt số** với website 74,8% > Singapore 66,1%;
- (c) **Vùng Vịnh và Brunei xác nhận thuộc nhóm Advanced tài nguyên dẫn dắt** (FSTS 0,4–5,1%; Brunei website 80,7% cao nhất nhóm dữ liệu; sd log Saudi/Qatar 0,31–0,47);
- (d) **Cảnh báo R&D đánh giá vượt ngưỡng do thay đổi khung dữ liệu (schema-induced overestimation)** — MNG/AFG/MDV/BRN/KWT đều ghi nhận R&D 18–26% ở năm 2025, do BREADY 2025 thay đổi cách hỏi.
CĐ2 nên dùng tiểu nhóm dữ liệu 2025-only làm mẫu xác thực (validation sample) cho đặc tả mô hình chính.

**(ix) Khung phân tích cấp ngành (industry-level) chưa được thực hiện ở CĐ1** *(NEW D3, §4.8)*. Nhóm dữ liệu 101.035 doanh nghiệp cần phân rã theo 9 ngành ISIC Rev. 4 cho đặc tả mô hình CĐ2 — đặc biệt: (a) mẫu con Manufacturing-only (n≈50.000) làm kiểm định vững (robustness check); (b) kiểm định loại trừ ICT cho phát hiện DAI âm ở Advanced; (c) **kiểm định mẫu con Construction ở Vùng Vịnh** để phân biệt giữa "nhà nước tô (rentier state)" và "hiện vật ngành xây dựng (Construction artifact)" (Hertog, 2010); (d) tách Tourism/Hotels cho SIDS Thái Bình Dương (bản thảo P8). 5 giả thuyết I1–I5 đã được đặt ra để kiểm định trong CĐ2 và Giai đoạn 2 hoàn thiện CĐ1 (tháng 7/2026 — xem §7.5 file 16).

**(x) Pipeline tái lập được cho 4 thế hệ khung dữ liệu WBES**. Nhóm dữ liệu 101.035 doanh nghiệp được tạo qua pipeline 5 bước Python (`wbes/01_inventory.py` → `02_harmonize.py` → `03_describe.py` → `merge_macro_with_pool.py` → `fetch_macro_indicators.py`); xử lý 4 thay đổi khung dữ liệu lớn (website, R&D, kênh xuất khẩu, thị trường chính). Tất cả Bảng 4.1–4.10 và Bảng 5.1, 6.1, Phụ lục A đều tái tạo được từ tệp dữ liệu thô `.dta`. Đây là **gói tái lập (replication package)** mở cho cộng đồng tiếng Việt — kế thừa thực hành mở (Page et al., 2021 PRISMA 2020) và mở đường cho luận án cùng 3 bài báo thành phần trong `papers/` (P3 Singapore — MIR, P4 Việt Nam — IJoEM, P5 Trung Quốc — APJM).

**Hàm ý cho CĐ2 và luận án**:

(a) **Hệ giả thuyết H1–H6** (xây dựng trong CĐ2 §7.3.4 file 16) đã có đầy đủ bằng chứng hai biến (bivariate) ở Chương 4: H1 quan hệ phi tuyến (4 lần đảo dấu — sign-reversals); H2 TCI điều tiết (TCI × năng suất theo phân nhóm con); H3 DAI có điều kiện (bằng chứng Mongolia + Việt Nam + Thái Lan); H4 phân nhóm con thể chế (5 + 8 phân nhóm con); H5 cụm tài nguyên (MNG + Vùng Vịnh + PNG); H6 chi phí buộc phải quốc tế hóa (6 SIDS Thái Bình Dương).

(b) **8 phân nhóm con với hiệu ứng cố định (fixed effects)** cho CĐ2 đã được hoàn thiện ở §4.9 (3 phân nhóm con Emerging) cộng §5.2 file 16 (2 phân nhóm con Advanced) cộng Upper-middle, Frontier và SIDS — tổng 8 phân nhóm con. Đây là một trong 3 cải tiến phương pháp luận chính của CĐ1 (cùng với pipeline tái lập được và đo lường khái niệm đa thành phần — xem §7.3.2 file 16).

(c) **Hai đặc tả mô hình kiểm định vững** cho CĐ2: Đặc tả 1 — phạm vi đầy đủ 2009–2025 (n=101.035, DAI/TCI đơn thành phần); Đặc tả 2 — độ chính xác cao 2018–2025 (n≈50.000, DAI/TCI đa thành phần 5 chiều). Bằng chứng hai biến ở Chương 4 chỉ ra: phát hiện chính ở Đặc tả 1 phải tái lập được ở Đặc tả 2 (theo tiêu chí của Aguinis et al., 2011) — đặc biệt: (i) tỷ số phân tán phân nhóm con Advanced 2,1 lần; (ii) Mongolia DAI tăng nhưng FSTS không tăng; (iii) SIDS nhảy vọt số nhưng FSTS thấp.

(d) **Hiệu ứng cố định ngành (Industry FE) cộng 5 kiểm định vững mẫu con** *(NEW D3)*: Manufacturing-only, loại trừ ICT, tách Tourism cho SIDS, kiểm định Construction Vùng Vịnh, loại trừ Mining cho cụm tài nguyên — 5 giả thuyết I1–I5 cần được kiểm định trong đặc tả mở rộng của CĐ2.

**Phạm vi không trình bày trong Chương 4**:
- (a) Hồi quy đa biến (dành cho CĐ2 — §7.3.4 file 16);
- (b) Định danh nhân quả qua dữ liệu mảng và biến công cụ — Panel/IV identification (dành cho CĐ2);
- (c) Bảng mô tả cấp ngành (industry-level descriptive tables) — Phase 2 tháng 7/2026, pipeline `wbes/industry_harmonize.py`;
- (d) Năng suất quy đổi USD PPP (Phase 1 — tháng 6/2026 — Data360 WDI);
- (e) Phụ thuộc tài nguyên trực tiếp (WDI NY.GDP.TOTL.RT.ZS + UN Comtrade — Phase 1).

### 4.8 Khung phân tích cấp ngành (industry-level) — kế hoạch CĐ2

> **Mới ở v2.9 (D3)**: Khung dữ liệu (schema) WBES phân loại theo `a3a` (mã ngành) và `a4a` (mã ISIC 4 chữ số). CĐ1 phân tích ở cấp phân nhóm con / quốc gia; phân tích cấp ngành (industry-level) dành cho CĐ2 và Giai đoạn 2 hoàn thiện CĐ1 (tháng 7/2026).

**Bảng 4.8.1**. *Khung phân loại 9 ngành ISIC Rev. 4 cho nhóm dữ liệu WBES.*

| Ngành | Mã ISIC | Đặc điểm | Pattern dự kiến |
|---|---|---|---|
| Manufacturing (chế biến chế tạo) | C (10–33) | Thâm dụng vốn, định hướng xuất khẩu | FSTS cao; R&D cao; ISO cao |
| Wholesale/retail (bán buôn/bán lẻ) | G (45–47) | Thâm dụng lao động, định hướng trong nước | FSTS thấp; website cao; FDI thấp |
| Tourism/hotels (du lịch/khách sạn) | I (55–56) | Dịch vụ phụ thuộc du lịch | FDI cao ở SIDS |
| Transport (vận tải) | H (49–53) | Kinh tế mạng lưới (network-economics) | FDI cao; ISO cao |
| ICT (công nghệ thông tin) | J (58–63) | Thâm dụng tri thức | R&D cao; website ~100% |
| Construction (xây dựng) | F (41–43) | Theo dự án, định hướng trong nước | FSTS thấp; FDI ở GCC |
| Mining (khai khoáng) | B (05–09) | Tài nguyên dẫn dắt | FDI cao; ISO ở doanh nghiệp do MNE dẫn dắt |
| Finance (tài chính) | K (64–66) | Có quy chế, xuyên biên giới | FDI cao; website ~100% |
| Khác | A, D, L | Đa dạng | Hỗn hợp |

Phân bố ước tính: Manufacturing (~50%), Services (~30%), Retail (~10%), Other (~10%) — chi tiết ở Giai đoạn 2.

**5 giả thuyết cấp ngành cho CĐ2** (kế thừa Bharadwaj et al., 2013; Banalieva & Dhanaraj, 2019; Lall, 1992; Stallkamp & Schotter, 2021; Hertog, 2010):

**I1 (Manufacturing chiếm ưu thế về FSTS)**: Manufacturing có FSTS cao nhất (trung bình > 15%), đặc biệt ở khu vực Em Asia do FDI dẫn dắt. **Kiểm định**: mẫu con Manufacturing-only (n≈50.000).

**I2 (ICT — bản chất số ngay từ đầu, digital-native)**: ICT có DAI, R&D và đổi mới sáng tạo cao nhất. Hệ số DAI = -0,129 ở Advanced có thể là **hiện vật thống kê (artifact)** do không tách ICT khỏi mẫu. **Kiểm định**: mẫu con loại trừ ICT (ICT exclusion subsample).

**I3 (Du lịch dẫn dắt FDI ở SIDS)**: SIDS có FDI 23,5% có thể chủ yếu từ ngành Tourism. **Kiểm định**: phân tách Tourism cho bản thảo P8.

**I4 (Khai khoáng dẫn dắt cụm tài nguyên)**: Mẫu WBES không bao gồm các MNE khai khoáng lớn — pattern "lời nguyền tài nguyên (resource curse)" là **lan tỏa (spillover)** lên các doanh nghiệp ngoài khai khoáng. **Kiểm định**: tương tác giữa phụ thuộc tài nguyên quốc gia × FSTS thay vì ngành doanh nghiệp × FSTS.

**I5 (Construction chiếm ưu thế ở Vùng Vịnh)**: Theo Hertog (2010), Construction chiếm hơn 40% mẫu Vùng Vịnh; pattern "nhà nước tô (rentier state)" có thể là **hiện vật ngành xây dựng (Construction artifact)**. **Kiểm định then chốt**: phân tách Construction trong 5 nước Vùng Vịnh và Brunei. Nếu pattern duy trì → lời nguyền tài nguyên thật; nếu biến mất → hiện vật ngành xây dựng.

**5 hàm ý phương pháp luận cho CĐ2**: (a) hiệu ứng cố định ngành (Industry FE) cho 9 ngành ISIC, lấy G — Wholesale/retail làm tham chiếu; (b) kiểm định vững mẫu con Manufacturing-only; (c) tách Tourism/Hotels cho SIDS; (d) kiểm định mẫu con Construction cho Vùng Vịnh; (e) kiểm định loại trừ ICT cho hệ số DAI = -0,129 ở Advanced.

**Phạm vi không trình bày**: Bảng mô tả cấp ngành (industry-level descriptive tables) — cần hài hòa biến `a4a` xuyên 4 thế hệ khung dữ liệu; pipeline `wbes/industry_harmonize.py` thực hiện ở Giai đoạn 2 tháng 7/2026.

### 4.9 Phân nhóm con Emerging — phát hiện dị biệt nội bộ

> **Mới ở v2.7 (D1)**: Phát hiện phương pháp luận thứ hai cho CĐ2 sau khi đã có phân nhóm con Advanced.

**Bảng 4.9**. *Phân nhóm con Emerging — số liệu tổng hợp 2009–2025 (n=47.803).*

| Phân nhóm con | Quốc gia | n_firms | FSTS (%) | Doanh nghiệp xuất khẩu (%) | FDI ≥10% (%) | Website (%) | R&D (%) | ISO (%) | sd log |
|---|---|---|---|---|---|---|---|---|---|
| **Emerging — FDI dẫn dắt Đông Nam Á (SEA)** | VNM, IDN, PHL | 13.779 | **13,2** | 22,1 | 11,4 | 47,3 | 4,8 | 18,8 | 1,53 |
| **Emerging — dân số lớn** | IND, LKA, JOR | 32.119 | **7,2** | 13,8 | 1,9 | 49,5 | 19,8 | 27,6 | 1,16 |
| **Emerging — tài nguyên** | MNG | 1.905 | **5,0** | 9,7 | 4,7 | 50,1 | 20,8 | 15,4 | 1,16 |
| **Tổng Emerging** | 7 nước | **47.803** | 8,6 | 15,5 | 4,7 | 49,2 | 16,4 | 24,9 | 1,24 |

Năm phát hiện: (1) FSTS phân tầng 5,0% – 7,2% – 13,2% bị che giấu trong số liệu tổng hợp; (2) FDI chênh lệch 6 lần giữa ASEAN-3 và Nam Á + Tây Á; (3) Năng lực công nghệ (TCI) ngược dấu — học hỏi do FDI dẫn dắt (FDI-induced learning) so với học hỏi tự thân (autonomous learning) (Cohen & Levinthal, 1990); (4) Mongolia là trường hợp biên (boundary case); (5) phân tán sd log 1,53 so với 1,16 — cấu trúc hai tầng (two-tier) (Hsieh & Klenow, 2009).

### 4.10 Phân tích sâu đợt khảo sát 2025

> **Mới ở v2.8 (D2)**: Đợt 2025 chiếm 16.829 doanh nghiệp (16,7% nhóm dữ liệu) — đợt khảo sát đơn năm lớn nhất. Phát hiện chính: tác động khung dữ liệu (schema effects), nhảy vọt số ở SIDS Thái Bình Dương, và dữ liệu cho phân nhóm con Advanced.

**Bảng 4.10**. *12 quốc gia trong đợt 2025 (n=16.829).*

| Quốc gia | ISO3 | Phân nhóm con | n_firms | FSTS (%) | FDI (%) | R&D (%) | Website (%) | sd log |
|---|---|---|---|---|---|---|---|---|
| Ấn Độ | IND | Emerging | 10.479 | 2,7 | 1,9 | 2,2 | 41,8 | 0,83 |
| Nepal¹ | NPL | Frontier | 1.740 | n/a | n/a | n/a | n/a | n/a |
| Saudi Arabia | SAU | Advanced | 1.002 | 2,7 | 9,5 | 1,7 | 30,2 | **0,47** |
| Thái Lan | THA | Upper-middle | 813 | 9,3 | 6,3 | 8,7 | 61,9 | 1,38 |
| Sri Lanka | LKA | Emerging | 607 | 16,1 | 1,8 | 4,1 | 48,8 | 1,00 |
| Mongolia | MNG | Emerging | 601 | 5,9 | 3,2 | 20,8 | 64,7 | 1,15 |
| Qatar | QAT | Advanced | 480 | 2,3 | 19,4 | 0,6 | 63,3 | **0,31** |
| Afghanistan | AFG | Frontier | 480 | 6,4 | 1,0 | 25,8 | 45,8 | 1,42 |
| Maldives | MDV | Frontier | 154 | 5,8 | 4,5 | 22,4 | **73,4** | 1,36 |
| Fiji | FJI | SIDS | 151 | 12,5 | 9,9 | 18,8 | **74,8** | 1,09 |
| Solomon Is. | SLB | SIDS | 150 | 4,8 | 20,0 | 11,3 | 53,3 | 1,25 |
| Brunei | BRN | Advanced | 150 | 5,1 | 26,2 | 18,9 | **80,7** | 1,10 |
| Kuwait | KWT | Advanced | 150 | **0,4** | 0,0 | 20,7 | 69,3 | 1,15 |
| **Tổng 2025** | — | — | **16.829** | **3,9** | **2,9** | **5,3** | **44,4** | **0,90** |

*Ghi chú: ¹Nepal 2025 — khung dữ liệu BREADY chưa thống nhất, sẽ xử lý lại ở Giai đoạn 1.*

Sáu phát hiện: (1) Ấn Độ — FSTS sụt 5 đpt do tác động khung dữ liệu (schema effect); (2) Thái Lan — "số tăng, xuất khẩu giảm" (digital up, exports down); (3) Fiji — website 74,8% vượt Singapore, minh chứng nhảy vọt số (digital leapfrog); (4) Vùng Vịnh và Brunei — xác nhận thuộc nhóm Advanced tài nguyên dẫn dắt (sd log 0,31–0,47); (5) R&D bị đánh giá vượt ngưỡng do thay đổi khung dữ liệu (schema-induced overestimation); (6) Năm 2025 — đợt khảo sát đơn năm đa dạng nhất, có thể dùng làm mẫu xác thực (validation sample) cho CĐ2.

Năm hàm ý cho CĐ2: (a) đợt 2025 làm mẫu xác thực (validation test bed); (b) hiệu ứng cố định khung dữ liệu hậu BREADY 2024 (Schema FE PostBREADY2024); (c) khả thi kiểm định phân nhóm con Advanced trên 11 quốc gia; (d) bằng chứng nhảy vọt số ở SIDS phục vụ H6; (e) dữ liệu mảng hai sóng (two-wave panel) cho 6 nước Emerging/Frontier.

---

*Tiếp tục ở Phần 3 (Chương 5–7 + TLTK) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*

**Chương 4 nay HOÀN THIỆN với 10 mục (4.1–4.10)** — sẵn sàng trình HD TS. Nguyễn Minh Cảnh duyệt cùng Chương 5–7 (file 16).

---

*Phiên bản 3.0 (06/05/2026) — Biên tập tiếng Việt §4.1–4.10. NCS: Đỗ Thùy Hương. HD: TS. Nguyễn Minh Cảnh.*

*Phiên bản 3.1a (06/05/2026 — Quick Win 1 từ review report HD 07/05/2026) — Tách Bảng 4.1 phân nhóm Advanced thành 2 phân nhóm con (innovation-driven 1,03 so với resource-driven 0,49 — tỷ số 2,1×). Đáp ứng review point D.2(3).*
