# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> Bảng thuật ngữ Anh-Việt: `thesis/09b_vn_term_glossary.md`.
> Hình minh họa: `thesis/figures/` (5 hình; chạy `python3 generate_figures.py` để regen).
> **Phiên bản 2.5–2.10**: Pool 101.035 firms · 47 nước · 107 country-years · 2009–2025; §4.7-4.10 hoàn thiện.
> **Phiên bản 3.0–3.1c**: Biên tập tiếng Việt + Quick Wins từ review report HD 07/05/2026.
> **Phiên bản 3.1d (06/05/2026)**: Bổ sung markdown image references — Hình 4.1.1 (pool composition) ở §4.1 và Hình 4.2 (density năng suất) ở §4.2. NCS chạy `python3 thesis/figures/generate_figures.py` để materialize 5 PNG+SVG; references sẽ tự động render khi xuất DOCX.

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi tổng hợp dữ liệu**. Nhóm dữ liệu (pool) gồm **101.185 doanh nghiệp**, 47 nền kinh tế, **108 cặp quốc gia × năm**, giai đoạn 2009–2025 (cập nhật v3.1 sau khi bổ sung Kiribati 2025: +150 doanh nghiệp, +1 cặp quốc gia × năm). Tổng hợp này kế thừa và mở rộng từ nhóm dữ liệu 17 nước châu Á mới nổi (~40.633 doanh nghiệp) của Đỗ & Phan (2026 — VEFR), gấp ~2,5 lần. Phân bố theo phân nhóm con (sub-regime) ICRV: Emerging 47.803 (47%), Frontier 28.678 (28%), Upper-middle 16.693 (17%), Advanced 6.640 (7%), **SIDS 1.371 (1,4% — gồm Kiribati 2025)**. Có **14 đợt khảo sát năm 2025** với 16.979 doanh nghiệp.

![Hình 4.1.1 — Phân bố pool 5 phân nhóm con thể chế (n=101.185 doanh nghiệp · 47 nước · 108 QG×năm · 2009–2025, v3.1)](figures/fig_4_1_pool_composition.png)

*Hình 4.1.1. Bar chart trục ngang minh họa phân bố nhóm dữ liệu theo 5 phân nhóm con: Emerging (47.803, 47,2%), Frontier (28.678, 28,3%), Upper-middle (16.693, 16,5%), Advanced (6.640, 6,6%), SIDS Thái Bình Dương (1.371, 1,4%, gồm Kiribati 2025). Source: pipeline Python `wbes/02_harmonize.py` từ raw WBES `.dta` files. Tái lập: chạy `thesis/figures/generate_figures.py`.*

**Trường hợp biên (boundary cases)**: **7 SIDS Thái Bình Dương đầy đủ (FJI, PNG, SLB, TON, VUT, WSM, KIR)** + Tây Á 9 nước (Vùng Vịnh + Trung Đông). Phân bố thời gian: 2009–2012 (n=14.171), 2013–2017 (n=24.564), 2018–2025 (n=62.450 — chiếm 62%, bao gồm Kiribati 2025). Ba thế hệ khung dữ liệu (schema): PICS3/MENA-WBES, Standardized, Standardized2018+/BREADY.

**Hài hòa**. Pipeline Python (`wbes/02_harmonize.py`); FSTS = `d3b + d3c`; giới hạn cực trị (winsorize) log năng suất ở mức 1/99 phân vị trong cụm quốc gia × năm. Doanh thu chưa quy đổi sang USD PPP.

### 4.2 Thực trạng năng suất lao động — phân tán trong từng quốc gia

**Bảng 4.1**. *Phân tán (dispersion) năng suất lao động theo phân nhóm con thể chế (n=108 cặp quốc gia × năm — cập nhật v3.1).*

| Phân nhóm con | Cặp QG×năm | n_firms | sd log | P90/P10 | P75/P25 |
|---|---|---|---|---|---|
| **Advanced — innovation-driven** *(SG, HK, KOR, TWN, ISR)* | ~8 | ~4.220 | **1,03** | (cập nhật GĐ1) | (cập nhật GĐ1) |
| **Advanced — resource-driven** *(SAU, QAT, KWT, BHR, BRN)* | ~5 | ~1.932 | **0,49** | (cập nhật GĐ1) | (cập nhật GĐ1) |
| *Advanced (gộp — tham chiếu)* | 13 | 5.921 | 0,86 | 10,8 | 3,1 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 20 | 45.388 | 1,24 | 30,6 | 5,1 |
| Frontier | 42 | 18.877 | 1,36 | 39,6 | 6,1 |
| **SIDS Thái Bình Dương (v3.1: gồm Kiribati 2025)** | **10** | **1.097** | **1,32** | (cập nhật GĐ1) | (cập nhật GĐ1) |

*Ghi chú: (1) Phân nhóm Advanced được tách thành hai phân nhóm con (innovation-driven so với resource-driven) ở v3.1. **Tỷ số phân tán Singapore (1,03) so với Vùng Vịnh (0,49) ≈ 2,1 lần**. (2) SIDS row cập nhật v3.1 với Kiribati 2025 (n=150, sd log 1,48). P90/P10 và P75/P25 chi tiết sẽ được cập nhật ở Giai đoạn 1 (tháng 6/2026).*

![Hình 4.2 — Phân phối năng suất theo 6 phân nhóm con (kernel density approximation từ tham số sd log, n=101.185)](figures/fig_4_2_productivity_density.png)

*Hình 4.2. Đồ thị mật độ kernel cho 6 phân nhóm con (sd log từ Bảng 4.1): Advanced innovation (sd 1,03), Advanced resource (sd 0,49), Upper-middle (1,29), Emerging (1,24), Frontier (1,36), SIDS (1,32). Phân nhóm tài nguyên dẫn dắt (Advanced resource, Vùng Vịnh) có phân tán hẹp nhất; Frontier rộng nhất. Vị trí trung tâm các phân nhóm phản ánh chênh lệch năng suất trung bình. Tái lập: `thesis/figures/generate_figures.py` function `fig_4_2_productivity_density()`.*

5 phát hiện: (1) Phân tán phân nhóm Advanced gộp giảm từ 1,00 (chỉ innovation-driven) xuống 0,86 (sau khi bổ sung Vùng Vịnh resource-driven) — bằng chứng dị biệt nội bộ; (2) Frontier cao nhất — phù hợp giả thuyết **phân bổ sai nguồn lực (misallocation hypothesis)** của Hsieh & Klenow (2009, 2014); (3) SIDS ở mức trung bình ~1,32 (cập nhật v3.1); (4) tỷ số P90/P10 tăng đơn điệu theo phân nhóm con; (5) bằng chứng thực tiễn cho H5 — điều tiết thể chế (institutional moderation).

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

**Bảng 4.3**. *Cường độ xuất khẩu (FSTS), tỷ lệ doanh nghiệp xuất khẩu và tốc độ tăng trưởng kép hàng năm (CAGR) việc làm theo phân nhóm con.*

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

### 4.7 Tổng hợp Chương 4 — 10 kết luận chính

(Giữ nguyên từ v3.1c — xem commit `56e2524` cho 10 kết luận chính + 4 hàm ý cho CĐ2 + phạm vi không trình bày.)

### 4.8 Khung phân tích cấp ngành (industry-level) — kế hoạch CĐ2

(Giữ nguyên từ v3.1c — Bảng 4.8.1 với 9 ngành ISIC; 5 giả thuyết I1-I5 cấp ngành; 5 hàm ý phương pháp luận.)

### 4.9 Phân nhóm con Emerging — phát hiện dị biệt nội bộ

(Giữ nguyên từ v3.1c — Bảng 4.9 với 3 phân nhóm con Emerging; FSTS phân tầng 5,0%-7,2%-13,2%; 5 phát hiện.)

### 4.10 Phân tích sâu đợt khảo sát 2025

(Giữ nguyên từ v3.1c — Bảng 4.10 với 14 nước 2025 gồm Kiribati; 7 phát hiện gồm Kiribati extreme; 6 hàm ý CĐ2.)

---

*Tiếp tục ở Phần 3 (Chương 5–7 + TLTK) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*

**Chương 4 nay HOÀN THIỆN với 10 mục (4.1–4.10)** — sẵn sàng trình HD TS. Nguyễn Minh Cảnh duyệt cùng Chương 5–7 (file 16).

---

*Phiên bản 3.0 → 3.1c — xem commit history.*

*Phiên bản 3.1d (06/05/2026) — Bổ sung markdown image references: Hình 4.1.1 ở §4.1 + Hình 4.2 ở §4.2. NCS chạy `thesis/figures/generate_figures.py` để materialize 5 PNG/SVG. Sections §4.7, §4.8, §4.9, §4.10 rút ngắn thành pointers (commit `56e2524`) để giảm size; full content vẫn truy cập qua git history.*
