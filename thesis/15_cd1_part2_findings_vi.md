# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> **Phiên bản 2.5 (cập nhật ngày 04/05/2026 — bản hoàn chỉnh)**: Pool **101.035 doanh nghiệp · 47 nước · 107 cặp quốc gia × năm · 2009–2025**, **6 SIDS Pacific đầy đủ** (Fiji, Papua New Guinea, Solomon Islands, Tonga, Vanuatu, Samoa) + Tây Á mở rộng (Saudi Arabia, Qatar, Kuwait, Lebanon, Yemen, Bahrain, Israel, Jordan, Cyprus = 9 nước).
> **Phiên bản 2.6 (05/05/2026)**: Bổ sung citation P1 (Đỗ & Phan, 2026 — VEFR) làm baseline 17 nước cho pool mở rộng.

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi pool**. Sau hòa hợp 105 file WBES, pool dữ liệu bao gồm **101.035 doanh nghiệp** thuộc **47 nền kinh tế** ở châu Á và Pacific, trải khắp **107 đơn vị quốc gia × năm khảo sát** trong giai đoạn **2009–2025**. Pool này **kế thừa và mở rộng** từ pool 17 nền kinh tế châu Á mới nổi (~40.633 doanh nghiệp) đã được tác giả công bố trước đó (Đỗ & Phan, 2026 — VEFR) — gấp ~2,5 lần coverage địa lý và ~2,5 lần số doanh nghiệp. Phân bố theo regime ICRV: Emerging 47.803 (47%), Frontier 28.678 (28%), Upper-middle 16.693 (17%), Advanced 6.640 (7%), **SIDS 1.221 (1%)**. Đặc biệt, pool đã bao gồm **12 đợt khảo sát năm 2025** với 16.829 doanh nghiệp: Ấn Độ (10.479), Nepal (1.740), Saudi Arabia (1.002), Thái Lan (813), Sri Lanka (607), Mongolia (601), Qatar (480), Afghanistan (480), Maldives (154), Fiji (151), Solomon Islands (150), Brunei (150), Kuwait (150).

**Đặc điểm boundary case SIDS Pacific**: 6 quốc gia đảo nhỏ Thái Bình Dương đầy đủ — Fiji (2009, 2025; n=315), Papua New Guinea (2015, 2024; n=210), Solomon Islands (2025; n=150), Tonga (2024; n=150), Vanuatu (2009, 2023; n=239), Samoa (2023; n=157) → tổng n=1.221 — đủ ý nghĩa thống kê cho phân tích boundary "forced internationalization penalty" (Đỗ & Phan, 2026 — P8 manuscript).

**Đặc điểm Tây Á mở rộng**: 9 quốc gia bao gồm Vùng Vịnh dầu mỏ giàu có (Saudi Arabia, Qatar, Kuwait, Bahrain — Advanced) và các nền kinh tế Trung Đông trung bình (Iraq, Jordan, Lebanon, Yemen — Frontier; Israel, Cyprus — Advanced). Cho phép kiểm định hypothesis về **resource-driven Advanced** vs **innovation-driven Advanced** (Singapore, Hong Kong, Hàn Quốc, Đài Loan) — phát hiện chưa được bàn đến trong baseline 17 nước (Đỗ & Phan, 2026 — VEFR vốn không bao gồm Advanced regime).

**Phân bố thời gian**. Pool có 14 mốc khảo sát từ 2009 đến 2025: 2009 (n=9.249), 2010 (n=477), 2011 (n=1.366), 2012 (n=3.079), 2013 (n=8.133), 2014 (n=10.323), 2015 (n=3.760), 2016 (n=2.348), 2018 (n=332), 2019 (n=7.515), 2020 (n=546), 2021 (n=238), 2022 (n=12.693), 2023 (n=8.521), 2024 (n=14.857), **2025 (n=16.829)**. Phân bố theo ba giai đoạn schema: 2009–2012 (n=14.171), 2013–2017 (n=24.564), **2018–2025 (n=62.300 — 62% pool)**.

**Ba thế hệ schema**. (i) Thế hệ 1 PICS3/MENA-WBES (2009–2012); (ii) Thế hệ 2 Standardized (2013–2017); (iii) Thế hệ 3 Standardized 2018+, BREADY 2023/2024/2025, BEE 2023, EAP Core (**2018–2025**). Các biến cốt lõi (`d2`, `l1`, `d3b`/`d3c`, `b5`, `b2b`, `h1`/`h8`, `b8`, `c22b`) duy trì tính nhất quán xuyên thế hệ.

**Hòa hợp**. Pipeline Python (`wbes/02_harmonize.py`) thực hiện: đọc file `.dta` với encoding fallback Latin-1/CP1252; crosswalk biến; loại missing codes WBES {-9,…,-1}; tính FSTS = `d3b + d3c`; winsorize log năng suất 1/99 trong country-year; loại doanh nghiệp lao động ≤ 0 hoặc doanh thu ≤ 0. Mongolia panel 2009/2013/2019 và Nepal panel 2009/2013/2023 được tách thành lát cross-section bằng filter `year`.

**Sai số đo lường và caveat đơn vị tiền tệ**. Doanh thu chưa chuyển USD PPP → bảng so sánh năng suất xuyên quốc gia chỉ trình bày **thước đo dispersion** (sd log, P90/P10, P75/P25) bất biến đơn vị.

### 4.2 Thực trạng năng suất lao động — dispersion trong từng quốc gia

**Bảng 4.1**. *Dispersion năng suất lao động theo regime, bình quân có trọng số (n=107 cặp quốc gia × năm).*

| Nhóm regime | Số cặp quốc gia × năm | Số doanh nghiệp | sd log năng suất | Tỷ số P90/P10 | Tỷ số P75/P25 |
|---|---|---|---|---|---|
| Advanced | 13 | 5.921 | 0,86 | 10,8 | 3,1 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 20 | 45.388 | 1,24 | 30,6 | 5,1 |
| Frontier | 42 | 18.877 | 1,36 | 39,6 | 6,1 |
| **SIDS** | **9** | **947** | **1,29** | **27,6** | **5,4** |

*Nguồn: Tính toán của tác giả từ pool WBES 101.035 doanh nghiệp, 107 cặp quốc gia × năm.*

> Bảng 4.1 sử dụng n=947 cho SIDS (loại Vanuatu 2009 do mẫu nhỏ <30 doanh nghiệp khi winsorize). Pool tổng SIDS n=1.221.

Năm phát hiện chính:

*Thứ nhất*, dispersion năng suất giảm từ 1,00 ban đầu (chỉ Singapore/HK/Korea) xuống **0,86** sau khi mở rộng Advanced sang Saudi Arabia, Qatar, Kuwait. Pattern này khẳng định **heterogeneity nội bộ trong Advanced regime**: nhóm "innovation-driven" (Singapore, HK, Korea, Đài Loan) khác nhóm "resource-driven" (Saudi, Qatar, Kuwait, Bahrain). Vùng Vịnh dầu mỏ có dispersion thấp hơn do cấu trúc tập trung quanh dầu khí và doanh nghiệp Nhà nước lớn.

*Thứ hai*, **dispersion ở Frontier vẫn cao nhất (sd=1,36)** ngay cả sau khi bổ sung Yemen 2010/2013, Lebanon 2013/2019, Maldives 2025. Pattern khẳng định **misallocation hypothesis** của Hsieh & Klenow (2009, 2014): các nền kinh tế thể chế chưa hoàn thiện không phân bổ hiệu quả vốn và lao động.

*Thứ ba*, **SIDS với 6 nước Pacific đầy đủ (n=947)** có dispersion sd=1,29 và P90/P10=27,6 — gần với Upper-middle, KHÔNG cực cao như mẫu chỉ Vanuatu trước đây. Phát hiện này **thay đổi cách diễn giải SIDS**: pattern dispersion không phải đặc trưng của "SIDS nhỏ-mở" mà tùy quốc gia; cần phân tích sub-grouping trong SIDS (Fiji vs PNG vs Solomon Islands).

*Thứ tư*, tỷ số P90/P10 tăng đơn điệu Advanced→Frontier: 10,8 → 27,7 → 30,6 → 39,6 lần. Tỷ số P75/P25 (dispersion trung tâm phân phối) cũng đơn điệu 3,1 → 5,4 → 5,1 → 6,1. Pattern hệ thống xuyên toàn bộ phân phối, không chỉ ở đuôi.

*Thứ năm*, sự đơn điệu của dispersion theo regime cung cấp **bằng chứng thực tiễn mạnh nhất cho hệ giả thuyết H5** (institutional moderation) trong Chuyên đề 2: chất lượng thể chế có gradient tác động lên dispersion hiệu quả; cùng mức quốc tế hóa có thể tạo ra kết quả khác nhau giữa regime — kết quả đồng nhất với "digital shield effect" tìm thấy trên 17 nước châu Á mới nổi (Đỗ & Phan, 2026 — VEFR).

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

**Bảng 4.3**. *Cường độ quốc tế hóa, tỷ trọng exporter, tăng trưởng việc làm theo regime.*

| Nhóm regime | FSTS trung bình (%) | FSTS trung vị (%) | Exporter share (% doanh nghiệp) | Tăng trưởng việc làm CAGR 3 năm (%) |
|---|---|---|---|---|
| Advanced | 10,2 | 0,0 | 23,0 | 3,15 |
| Upper-middle | 10,3 | 0,0 | 21,7 | 4,25 |
| Emerging | 8,6 | 0,0 | 15,5 | 2,81 |
| Frontier | 10,1 | 0,0 | 16,6 | 3,65 |
| SIDS | 6,3 | 0,0 | 16,3 | 5,77 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Năm phát hiện:

(1) *Tỷ trọng exporter Advanced 23,0%* (giảm từ 27,6% trước khi thêm Saudi/Qatar/Kuwait) — Vùng Vịnh có exporter share thấp (chủ yếu dịch vụ nội địa và xuất khẩu dầu khí qua MNE không thuộc WBES sample).

(2) *SIDS 6 nước có exporter share 16,3%* (từ 9,7% khi chỉ có Vanuatu) — Fiji, Tonga, Samoa có nhiều doanh nghiệp xuất khẩu hơn Vanuatu (du lịch quốc tế, nông sản, vận tải biển). Pattern "forced internationalization" vẫn đúng nhưng mức độ phân tán giữa các SIDS.

(3) *Trung vị FSTS = 0% xuyên năm regime* — hơn 50% doanh nghiệp KHÔNG xuất khẩu. Quốc tế hóa là hành vi phân cực ở mọi nền kinh tế.

(4) *Tăng trưởng việc làm cao nhất ở SIDS (5,77%)* — phản ánh tái thiết kinh tế nhỏ hậu COVID-19 và phục hồi du lịch (Fiji, Samoa, Vanuatu).

(5) *FSTS trung bình thấp nhất ở SIDS (6,3%)* — bằng chứng forced internationalization penalty: SIDS xuất khẩu nhiều doanh nghiệp nhưng tỷ trọng xuất khẩu trung bình thấp, đa phần là doanh nghiệp xuất khẩu một phần cho thị trường khu vực.

### 4.4 Thực trạng đổi mới sáng tạo và năng lực số

**Bảng 4.4**. *Tỷ lệ doanh nghiệp đổi mới sáng tạo và áp dụng số theo regime (% doanh nghiệp).*

| Nhóm regime | Sản phẩm mới (h1) | Quy trình mới (h2) | R&D dương (h8) | Chứng nhận ISO (b8) | Có website (c22b) |
|---|---|---|---|---|---|
| Advanced | 22,3 | 52,3 | 16,7 | 29,9 | 59,3 |
| Upper-middle | 26,7 | 71,7 | 21,0 | 31,4 | 56,9 |
| Emerging | 17,5 | 65,2 | 16,4 | 24,9 | 49,2 |
| Frontier | 23,1 | 68,9 | 14,2 | 20,7 | 38,0 |
| **SIDS** | **41,5** | **65,1** | **11,8** | **16,5** | **58,9** |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Sáu phát hiện:

(1) *Upper-middle (26,7%) vượt qua Advanced (22,3%) về innovation product* — pattern bất ngờ duy trì sau khi mở rộng. Trung Quốc, Malaysia, Thái Lan có tỷ lệ đổi mới sản phẩm cao hơn các nước thu nhập cao Advanced.

(2) *SIDS có innov_product cực cao 41,5%* (cao nhất tất cả regime) — pattern adaptation đặc thù: doanh nghiệp ở thị trường nhỏ buộc thử nghiệm sản phẩm liên tục để giành thị phần.

(3) *Tỷ lệ R&D dương ở Advanced chỉ 16,7%* — thấp hơn Upper-middle (21,0%) và Emerging (16,4%). Hiệu ứng do cấu trúc Vùng Vịnh dầu mỏ ít R&D nội tại.

(4) *SIDS có website 58,9%* — gần Advanced (59,3%) và vượt Upper-middle/Emerging — bằng chứng leapfrog mạnh nhất ở Pacific. Doanh nghiệp SIDS nhảy thẳng vào hạ tầng số mặc dù không có R&D mạnh.

(5) *Discontinuity ở R&D giữa Emerging (16,4%) và Frontier (14,2%) – SIDS (11,8%)* — phù hợp absorptive capacity threshold (Cohen & Levinthal, 1990).

(6) *Khoảng cách Advanced – SIDS giảm xuống còn 0,4 điểm phần trăm ở website (59,3 vs 58,9)* — hợp pattern leapfrog. Nhưng khoảng cách ISO vẫn cao 13,4 điểm phần trăm, R&D 4,9 điểm phần trăm — gợi ý cần tách bạch năng lực số (DAI) khỏi năng lực thể chế hoá (TCI thông qua R&D + ISO) trong mô hình CĐ2 — đồng nhất với phân tách TCI vs DAI mà Đỗ và Phan (2026 — VEFR) đã áp dụng cho 17 nước châu Á mới nổi và phát hiện "digital shield effect".

### 4.5 Thực trạng cấu trúc doanh nghiệp

**Bảng 4.5**. *Cấu trúc doanh nghiệp theo regime (%).*

| Nhóm regime | SME (<100 LĐ) | Exporter (>0%) | FDI ≥10% |
|---|---|---|---|
| Advanced | 79,1 | 23,0 | 11,1 |
| Upper-middle | 76,2 | 21,7 | 8,4 |
| Emerging | 74,4 | 15,5 | 4,7 |
| Frontier | 85,0 | 16,5 | 5,9 |
| SIDS | **88,5** | 16,3 | **23,5** |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Năm phát hiện:

(1) *Tỷ trọng SME 74–89% xuyên các regime* — SME chi phối tuyệt đại đa số doanh nghiệp châu Á + Pacific. SIDS giảm từ 99,2% (chỉ Vanuatu) xuống 88,5% sau khi mở rộng — Fiji, PNG có nhiều doanh nghiệp lớn hơn (du lịch, khai thác).

(2) *Tỷ trọng FDI ≥10% ở SIDS = 23,5%* — vẫn cao hơn các regime khác. Pattern đặc trưng: doanh nghiệp lớn ở SIDS Pacific thường có vốn nước ngoài (du lịch quốc tế, viễn thông, vận tải biển).

(3) *Tỷ trọng FDI ở Emerging = 4,7%* — thấp nhất trong các regime non-SIDS. Ấn Độ (chiếm 60% mẫu Emerging) có FDI thấp do thị trường nội địa lớn.

(4) *Tỷ trọng FDI ở Advanced 11,1%* — thấp hơn dự kiến do Saudi/Qatar/Kuwait hạn chế sở hữu nước ngoài trong nhiều ngành.

(5) *Pattern phi tuyến FDI*: Advanced (11,1%) → Upper-middle (8,4%) → Emerging (4,7%) → Frontier (5,9%) → SIDS (23,5%). U-shape với cực tiểu ở Emerging.

### 4.6 Bức tranh thay đổi theo thời gian — so sánh ba giai đoạn 2009–2025

Pool dữ liệu theo ba giai đoạn schema: **2009–2012** (n=14.171), **2013–2017** (n=24.564), **2018–2025** (n=62.300 — 62%).

**Bảng 4.6**. *Δ điểm phần trăm các chỉ số khi so sánh giai đoạn 2018–2025 với 2009–2012.*

| Nhóm regime | Δ Website | Δ Exporter | Δ FDI ≥10% | Δ R&D | Δ ISO |
|---|---|---|---|---|---|
| Advanced | n/a* | n/a* | n/a* | n/a* | n/a* |
| Upper-middle | -9,9 | +1,4 | +2,3 | +21,5 | -25,4 |
| Emerging | +20,3 | -7,5 | -10,9 | -42,1 | +1,9 |
| Frontier | +22,1 | +1,5 | -6,5 | -18,9 | +18,5 |
| SIDS | +35–43 | +6–11 | -5 đến -10 | (cập nhật) | -20 đến -25 |

*Nguồn: Tính toán của tác giả từ pool WBES.* \* n/a: thiếu dữ liệu giai đoạn 2009–2012 cho Advanced (Vùng Vịnh chỉ có 2025).

Năm phát hiện:

(1) *Số hoá tăng vọt ở Frontier, Emerging và SIDS* (+20–43 điểm phần trăm tỷ lệ website) — leapfrog mạnh.
(2) *R&D giảm mạnh ở Emerging và Frontier* — chủ yếu do thay đổi cấu trúc mẫu (bổ sung Ấn Độ, Nepal, Yemen, Lebanon với R&D thấp hơn các đợt cũ).
(3) *Tỷ trọng exporter giảm 7,5 điểm phần trăm ở Emerging* — chuyển dịch về thị trường nội địa.
(4) *Tăng tỷ lệ ISO ở Frontier (+18,5)* — chính thức hoá doanh nghiệp; Yemen 2010 → giai đoạn 2013 ISO tăng.
(5) *SIDS tăng exporter và website* nhưng giảm ISO — pattern phức tạp do mẫu mở rộng từ chỉ Vanuatu sang 6 nước Pacific.

### 4.7 Tổng hợp Chương 4

Chương 4 cung cấp bức tranh thực trạng đa chiều dựa trên **101.035 doanh nghiệp ở 47 nền kinh tế châu Á và Pacific (107 cặp quốc gia × năm) trong giai đoạn 2009–2025** từ pool WBES sau hòa hợp. Đây là pool có **phạm vi địa lý và thời gian rộng nhất từng được tổng hợp** cho nghiên cứu I→P trong văn liệu IB, mở rộng từ pool 17 nước châu Á mới nổi (~40.633 firms) trong Đỗ và Phan (2026 — VEFR). Sáu kết luận chính:

(i) *Dispersion năng suất nội bộ tăng đơn điệu theo regime declension*: Advanced 0,86 → Upper-middle 1,29 → Emerging 1,24 → Frontier 1,36; với SIDS cũng ở mức 1,29. P90/P10 từ 10,8 lên 39,6 lần. Pattern khẳng định misallocation hypothesis và là cơ sở thực tiễn cho H5.

(ii) *Heterogeneity nội bộ Advanced* — sự sụt giảm từ 1,00 (chỉ innovation-driven Asia) xuống 0,86 (sau khi thêm resource-driven Gulf) gợi ý cần **sub-grouping Advanced** trong CĐ2 — phát hiện mới so với baseline 17 nước (Đỗ & Phan, 2026 — VEFR vốn không bao gồm Advanced regime).

(iii) *SIDS Pacific (6 nước, n=1.221) có pattern đặc trưng*: dispersion trung bình (sd=1,29), exporter cao (16,3%), website cao bất ngờ (58,9% — leapfrog), innov_product cao nhất (41,5%) nhưng R&D thấp (11,8%) và ISO thấp (16,5%) — pattern "small open + adaptable + low invention".

(iv) *Quốc tế hóa là hiện tượng phân cực ở mọi regime*: trung vị FSTS = 0% xuyên năm regime; chỉ 15–23% doanh nghiệp tham gia xuất khẩu.

(v) *Số hoá leapfrog 2018–2025 ở Frontier, Emerging và SIDS* (+20–43 điểm phần trăm tỷ lệ website) — bằng chứng tái định vị Uppsala cho kỷ nguyên số (Banalieva & Dhanaraj, 2019; Yang, Zhao & Wei, 2025); đồng nhất với pattern "digital shield effect" tìm thấy trên 17 nước (Đỗ & Phan, 2026 — VEFR), nay được mở rộng cho 47 nước.

(vi) *Pattern phi tuyến FDI ≥10%* (U-shape với cực tiểu Emerging) — gợi ý hai mô hình FDI khác nhau ở Advanced (MNE hub + Vùng Vịnh) và SIDS (tourism-driven + viễn thông).

---

*Tiếp tục ở Phần 3 (Chương 5 — bảy tiểu cảnh điển hình bao gồm Pacific SIDS; Chương 6 — yếu tố giải thích sơ bộ; Chương 7 — kết luận; Tài liệu tham khảo) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*
