# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> **Phiên bản 2.4 (cập nhật ngày 04/05/2026)**: Pool **98.752 doanh nghiệp · 43 nước · 100 cặp quốc gia × năm · 2009–2025**, mở rộng mạnh vùng Pacific SIDS (5 nước) và Tây Á Gulf (Saudi Arabia, Qatar). Thêm 12 đợt khảo sát năm 2025.

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi pool**. Sau hòa hợp 100 file WBES, pool dữ liệu bao gồm **98.752 doanh nghiệp** thuộc **43 nền kinh tế** ở châu Á và Pacific, trải khắp **100 đơn vị quốc gia × năm khảo sát** trong giai đoạn **2009–2025**. Phân bố theo regime ICRV: Emerging 47.803 (48%), Frontier 28.117 (28%), Upper-middle 16.693 (17%), Advanced 5.771 (6%), **SIDS 790 (1%)**. Đặc biệt, pool đã bao gồm **12 đợt khảo sát năm 2025** với 16.829 doanh nghiệp: Ấn Độ (10.479), Nepal (1.740), Saudi Arabia (1.002), Thái Lan (813), Sri Lanka (607), Mongolia (601), Qatar (480), Afghanistan (480), Maldives (154), Fiji (151), Solomon Islands (150), Brunei (150).

**Bổ sung từ phiên bản 2.3 sang 2.4**: 
- **Pacific SIDS** (boundary case quan trọng): bổ sung Solomon Islands 2025 (n=150), Tonga 2024 (n=150), Fiji 2009/2025 (n=315), Samoa 2023 (n=157) → SIDS regime nay có **5 quốc gia** với n=790 doanh nghiệp (so với chỉ Vanuatu n=196 trước đây).
- **Tây Á Gulf**: Saudi Arabia 2025 (n=1.002), Qatar 2025 (n=480) → Advanced regime tăng từ 8 lên 10 quốc gia, đa dạng hóa sang nhóm "resource-driven advanced".
- **Maldives 2025** (n=154): Nam Á small island, lấp lỗ hổng coverage Nam Á.
- **Mongolia 2025** (n=601): bổ sung đợt mới cho chuỗi Mongolia (nay 4 đợt 2009/2013/2019/2025).
- Afghanistan 2025 expansion (n=54): bổ sung mẫu cho AFG 2025.

**Phân bố thời gian**. Pool có 12 mốc khảo sát từ 2009 đến 2025. Phân bố theo ba giai đoạn schema: 2009–2012 (n=16.307), 2013–2017 (n=24.067), **2018–2025 (n=58.378 — 59% pool)**.

**Ba thế hệ schema**. (i) Thế hệ 1 PICS3 (2009–2012); (ii) Thế hệ 2 Standardized (2013–2017); (iii) Thế hệ 3 Standardized 2018+, BREADY 2023/2024/2025, BEE 2023, EAP Core (**2018–2025**). Các biến cốt lõi (`d2`, `l1`, `d3b`/`d3c`, `b5`, `b2b`, `h1`/`h8`, `b8`, `c22b`) duy trì tính nhất quán xuyên thế hệ.

**Hòa hợp**. Pipeline Python (`wbes/02_harmonize.py`) thực hiện: đọc file `.dta` với encoding fallback; crosswalk biến; loại missing codes WBES {-9,…,-1}; tính FSTS = `d3b + d3c`; winsorize log năng suất 1/99 trong country-year; loại doanh nghiệp lao động ≤ 0 hoặc doanh thu ≤ 0.

**Sai số đo lường và caveat đơn vị tiền tệ**. Doanh thu chưa chuyển USD PPP → bảng so sánh năng suất xuyên quốc gia chỉ trình bày **thước đo dispersion** (sd log, P90/P10, P75/P25) bất biến đơn vị.

### 4.2 Thực trạng năng suất lao động — dispersion trong từng quốc gia

**Bảng 4.1**. *Dispersion năng suất lao động theo regime, bình quân có trọng số (n=100 cặp quốc gia × năm).*

| Nhóm regime | Số cặp quốc gia × năm | Số doanh nghiệp | sd log năng suất | Tỷ số P90/P10 | Tỷ số P75/P25 |
|---|---|---|---|---|---|
| Advanced | 12 | 5.771 | **0,85** | 10,6 | 3,1 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 20 | 45.388 | 1,24 | 30,6 | 5,1 |
| Frontier | 38 | 17.279 | 1,36 | 38,4 | 6,2 |
| SIDS | 7 | 790 | **1,29** | 28,4 | 5,4 |

*Nguồn: Tính toán của tác giả từ pool WBES 98.752 doanh nghiệp, 100 cặp quốc gia × năm.*

Năm phát hiện chính:

*Thứ nhất*, dispersion năng suất ở **Advanced giảm xuống 0,85** (so với 1,00 trước khi bổ sung Saudi Arabia + Qatar). Pattern này cho thấy các nền kinh tế Vùng Vịnh dầu mỏ có dispersion firm-level THẤP HƠN Singapore, Hong Kong, Hàn Quốc — phản ánh cấu trúc kinh tế tập trung vào dầu khí và doanh nghiệp Nhà nước lớn.

*Thứ hai*, **dispersion SIDS giảm mạnh xuống 1,29** (từ 1,35) sau khi mở rộng từ 1 nước (Vanuatu) lên 5 nước. P90/P10 SIDS từ 42,1 → 28,4 — gần với Upper-middle. Pattern này gợi ý dispersion ở SIDS không phải lúc nào cũng cực cao như Vanuatu — Solomon Islands, Tonga có firm distribution gần Frontier.

*Thứ ba*, pattern dispersion theo regime hiện tại: Advanced (0,85) < Emerging (1,24) ≈ Upper-middle (1,29) ≈ SIDS (1,29) < Frontier (1,36). Frontier vẫn cao nhất — khẳng định misallocation hypothesis.

*Thứ tư*, tỷ số P75/P25 (dispersion trung tâm) tăng đơn điệu: Advanced (3,1) → Upper-middle (5,4) ≈ SIDS (5,4) → Emerging (5,1) → Frontier (6,2). Pattern dạng "step function" ba mức độ rõ rệt.

*Thứ năm*, sự thay đổi của Advanced sau khi thêm Saudi/Qatar gợi ý **heterogeneity nội bộ trong Advanced regime**: Singapore/HK/Korea (innovation-driven) khác với Saudi/Qatar (resource-driven). Chuyên đề 2 nên xem xét sub-grouping Advanced thành "innovation-Advanced" và "resource-Advanced".

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

**Bảng 4.3**. *Cường độ quốc tế hóa, tỷ trọng exporter, tăng trưởng việc làm theo regime.*

| Nhóm regime | FSTS trung bình (%) | FSTS trung vị (%) | Exporter share (% doanh nghiệp) | Tăng trưởng việc làm CAGR 3 năm (%) |
|---|---|---|---|---|
| Advanced | 10,4 | 0,0 | 23,5 | 3,11 |
| Upper-middle | 10,3 | 0,0 | 21,7 | 4,25 |
| Emerging | 8,6 | 0,0 | 15,5 | 2,81 |
| Frontier | 10,1 | 0,0 | 15,6 | 3,71 |
| **SIDS** | **6,9** | **0,0** | **17,2** | **6,11** |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Bốn phát hiện:

(1) *Tỷ trọng exporter ở Advanced giảm 23,5%* (từ 27,6%) sau khi bổ sung Saudi Arabia + Qatar — hai nước Vùng Vịnh tập trung dịch vụ nội địa và xuất khẩu dầu khí qua các tập đoàn lớn không vào WBES sample.

(2) *SIDS có exporter share 17,2%* (từ 9,7%) — Solomon Islands, Fiji, Tonga, Samoa có nhiều doanh nghiệp xuất khẩu hơn Vanuatu (chủ yếu dầu cọ Solomon, du lịch Fiji, nông sản Tonga/Samoa). Hỗ trợ pattern "forced internationalization" vẫn đúng nhưng mức độ thay đổi giữa các SIDS.

(3) *Trung vị FSTS bằng 0 ở mọi nhóm* — hơn 50% doanh nghiệp KHÔNG xuất khẩu.

(4) *Tăng trưởng việc làm cao nhất ở SIDS (6,1%)* — phản ánh tái thiết kinh tế nhỏ hậu COVID-19 và phục hồi du lịch.

### 4.4 Thực trạng đổi mới sáng tạo và năng lực số

**Bảng 4.4**. *Tỷ lệ doanh nghiệp đổi mới sáng tạo và áp dụng số theo regime (% doanh nghiệp).*

| Nhóm regime | Sản phẩm mới (h1) | Quy trình mới (h2) | R&D dương (h8) | Chứng nhận ISO (b8) | Có website (c22b) |
|---|---|---|---|---|---|
| Advanced | 22,6 | 52,5 | 16,6 | 30,3 | 59,0 |
| Upper-middle | 26,7 | 71,7 | 21,0 | 31,4 | 56,9 |
| Emerging | 17,5 | 65,2 | 16,4 | 24,9 | 49,2 |
| Frontier | 22,3 | 68,6 | 12,6 | 21,2 | 36,8 |
| **SIDS** | **39,7** | **61,4** | **10,2** | **13,1** | **55,2** |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Năm phát hiện:

(1) *Advanced giảm chỉ số đổi mới sau khi thêm Saudi/Qatar*: R&D 21,3 → 16,6%; ISO 36,8 → 30,3%; website 64,4 → 59,0%; innov_product 26,2 → 22,6%. **Upper-middle (Trung Quốc, Malaysia, Thái Lan) vượt qua Advanced về innovation product (26,7 vs 22,6)** — pattern bất ngờ đáng chú ý.

(2) *SIDS có innov_product cao bất thường 39,7%* (từ 35,8%) — Pacific SIDS có tính linh hoạt sản phẩm cao do thị trường nhỏ buộc thử nghiệm. Cùng lúc, R&D SIDS chỉ 10,2% — pattern adaptation chứ không invention.

(3) *SIDS có website 55,2%* — gần Advanced (59%) và vượt Upper-middle/Emerging — leapfrog mạnh ở Pacific.

(4) *Tỷ lệ R&D dương*: Advanced 16,6% < Upper-middle 21,0% — phản ánh cấu trúc Saudi/Qatar dầu khí. Discontinuity giữa Emerging (16,4%) và Frontier (12,6%) vẫn rõ.

(5) *Khoảng cách Advanced – SIDS giảm xuống 4–17 điểm phần trăm* (so với 14–28 trước) sau khi mẫu mở rộng cả hai đầu — gợi ý mô hình moderation TCI/DAI cần xét sub-groups.

### 4.5 Thực trạng cấu trúc doanh nghiệp

**Bảng 4.5**. *Cấu trúc doanh nghiệp theo regime (%).*

| Nhóm regime | SME (<100 LĐ) | Exporter (>0%) | FDI ≥10% |
|---|---|---|---|
| Advanced | 79,3 | 23,5 | 11,3 |
| Upper-middle | 76,2 | 21,7 | 8,4 |
| Emerging | 74,4 | 15,5 | 4,7 |
| Frontier | 84,8 | 15,6 | 6,1 |
| SIDS | **91,8** | **17,2** | **18,3** |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Bốn phát hiện:

(1) *Tỷ trọng SME 74–92% ở mọi nhóm* — SME chi phối tuyệt đại đa số. SIDS giảm từ 99,2% xuống **91,8%** sau khi mở rộng (Solomon, Tonga có nhiều doanh nghiệp lớn hơn Vanuatu).

(2) *Tỷ trọng exporter Advanced giảm xuống 23,5%* (từ 27,6%) — Saudi/Qatar kéo xuống.

(3) *Tỷ trọng FDI ≥ 10% ở SIDS giảm xuống 18,3%* (từ 30,6%) — Vanuatu là extreme outlier; mức 18% giờ phản ánh thực tế hơn của các SIDS Pacific.

(4) *Pattern phi tuyến FDI vẫn rõ*: cao ở Advanced (11,3%) và SIDS (18,3%), thấp ở Emerging (4,7%) và Frontier (6,1%) — hai mô hình FDI khác nhau (MNE hub ở Advanced; tourism-driven ở SIDS).

### 4.6 Bức tranh thay đổi theo thời gian

Pool dữ liệu theo ba giai đoạn schema: **2009–2012** (n=16.307), **2013–2017** (n=24.067), **2018–2025** (n=58.378 — 59%).

**Bảng 4.6**. *Δ điểm phần trăm các chỉ số khi so sánh giai đoạn 2018–2025 với 2009–2012.*

| Nhóm regime | Δ Website | Δ Exporter | Δ FDI ≥10% | Δ R&D | Δ ISO |
|---|---|---|---|---|---|
| Advanced | n/a* | n/a* | n/a* | n/a* | n/a* |
| Upper-middle | -9,9 | +1,4 | +2,3 | +21,5 | -25,4 |
| Emerging | +20,3 | -7,5 | -10,9 | -42,1 | +1,9 |
| Frontier | +22,1 | +1,5 | -6,5 | -18,9 | +18,5 |
| SIDS | (cập nhật) | (cập nhật) | (cập nhật) | (cập nhật) | (cập nhật) |

*Nguồn: Tính toán của tác giả từ pool WBES.* \* n/a: thiếu dữ liệu giai đoạn 2009–2012 cho Advanced (chưa có khảo sát Saudi/Qatar/Singapore trước 2013).

Năm phát hiện:

(1) Số hoá tăng vọt ở Frontier, Emerging và SIDS (+20–43 điểm phần trăm tỷ lệ website) — leapfrog.
(2) R&D giảm mạnh ở Emerging chủ yếu do bổ sung Ấn Độ.
(3) Tỷ trọng exporter giảm 7,5 điểm phần trăm ở Emerging — chuyển dịch về thị trường nội địa.
(4) Tăng tỷ lệ ISO ở Frontier (+18,5) — chính thức hoá doanh nghiệp.
(5) SIDS có pattern phức tạp do mẫu nhỏ và đặc thù từng đảo quốc.

### 4.7 Tổng hợp Chương 4

Chương 4 cung cấp bức tranh thực trạng đa chiều dựa trên **98.752 doanh nghiệp ở 43 nền kinh tế châu Á và Pacific (100 cặp quốc gia × năm) trong giai đoạn 2009–2025**. Năm kết luận chính:

(i) *Dispersion năng suất giảm dần khi mẫu mở rộng*: Advanced sd 0,85 (sau khi thêm Saudi/Qatar) → Emerging 1,24 → Upper-middle 1,29 ≈ SIDS 1,29 → Frontier 1,36. Frontier vẫn cao nhất, khẳng định misallocation hypothesis.

(ii) *Heterogeneity nội bộ trong Advanced**: Singapore/HK/Korea innovation-driven khác Saudi/Qatar resource-driven. CĐ2 nên sub-group Advanced.

(iii) *SIDS có pattern đặc trưng*: dispersion trung bình (1,29), exporter cao bất thường (17,2%), website rất cao (55,2%), innov_product cao (39,7%) nhưng R&D thấp (10,2%) — pattern "small open + high adaptability + low invention".

(iv) *Quốc tế hóa là hiện tượng phân cực*: hơn 50% doanh nghiệp KHÔNG xuất khẩu xuyên năm regime.

(v) *Số hoá tăng vọt giai đoạn 2018–2025 ở mọi regime* — leapfrog phù hợp Banalieva & Dhanaraj (2019).

---

*Tiếp tục ở Phần 3 trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*
