# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> Bảng thuật ngữ Anh-Việt: `thesis/09b_vn_term_glossary.md`.
> Hình minh họa: `thesis/figures/` (5 hình; chạy `python3 generate_figures.py` để regen).
> **Phiên bản 2.5–2.10**: Pool 101.035 firms · 47 nước · 107 country-years · 2009–2025.
> **Phiên bản 3.0–3.1c**: Biên tập tiếng Việt + Quick Wins từ review report HD 07/05/2026.
> **Phiên bản 3.1d-fix (06/05/2026)**: Khôi phục full content §4.7-4.10 (đã bị rút gọn nhầm trong commit `36ecd13`) + giữ markdown image refs Hình 4.1.1 ở §4.1 và Hình 4.2 ở §4.2.

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi tổng hợp dữ liệu**. Nhóm dữ liệu (pool) gồm **101.185 doanh nghiệp**, 47 nền kinh tế, **108 cặp quốc gia × năm**, giai đoạn 2009–2025 (cập nhật v3.1 sau khi bổ sung Kiribati 2025: +150 doanh nghiệp, +1 cặp quốc gia × năm). Tổng hợp này kế thừa và mở rộng từ nhóm dữ liệu 17 nước châu Á mới nổi (~40.633 doanh nghiệp) của Đỗ & Phan (2026 — VEFR), gấp ~2,5 lần. Phân bố theo phân nhóm con (sub-regime) ICRV: Emerging 47.803 (47%), Frontier 28.678 (28%), Upper-middle 16.693 (17%), Advanced 6.640 (7%), **SIDS 1.371 (1,4% — gồm Kiribati 2025)**. Có **14 đợt khảo sát năm 2025** với 16.979 doanh nghiệp.

![Hình 4.1.1 — Phân bố pool 5 phân nhóm con thể chế (n=101.185 doanh nghiệp · 47 nước · 108 QG×năm · 2009–2025, v3.1)](figures/fig_4_1_pool_composition.png)

*Hình 4.1.1. Phân bố nhóm dữ liệu theo 5 phân nhóm con: Emerging (47.803, 47,2%), Frontier (28.678, 28,3%), Upper-middle (16.693, 16,5%), Advanced (6.640, 6,6%), SIDS Thái Bình Dương (1.371, 1,4%, gồm Kiribati 2025). Source: pipeline Python `wbes/02_harmonize.py`. Tái lập: `thesis/figures/generate_figures.py`.*

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

*Hình 4.2. Đồ thị mật độ kernel cho 6 phân nhóm con (sd log từ Bảng 4.1): Advanced innovation (sd 1,03), Advanced resource (sd 0,49), Upper-middle (1,29), Emerging (1,24), Frontier (1,36), SIDS (1,32). Phân nhóm tài nguyên dẫn dắt (Advanced resource, Vùng Vịnh) có phân tán hẹp nhất; Frontier rộng nhất. Tái lập: `thesis/figures/generate_figures.py` function `fig_4_2_productivity_density()`.*

5 phát hiện: (1) Phân tán phân nhóm Advanced gộp giảm từ 1,00 (chỉ innovation-driven) xuống 0,86 (sau khi bổ sung Vùng Vịnh resource-driven) — bằng chứng dị biệt nội bộ; (2) Frontier cao nhất — phù hợp giả thuyết **phân bổ sai nguồn lực (misallocation hypothesis)** của Hsieh & Klenow (2009, 2014); (3) SIDS ở mức trung bình ~1,32 (cập nhật v3.1); (4) tỷ số P90/P10 tăng đơn điệu theo phân nhóm con; (5) bằng chứng thực tiễn cho H5 — điều tiết thể chế (institutional moderation).

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

Chương 4 cung cấp bức tranh thực trạng đa chiều dựa trên **101.185 doanh nghiệp ở 47 nền kinh tế châu Á và Thái Bình Dương (108 cặp quốc gia × năm) trong giai đoạn 2009–2025** từ nhóm dữ liệu WBES sau hài hòa (cập nhật v3.1 với Kiribati 2025). Đây là nhóm dữ liệu có **phạm vi địa lý và thời gian rộng nhất từng được tổng hợp** cho nghiên cứu quan hệ quốc tế hóa → hiệu quả (I→P) trong văn liệu IB. Phạm vi này mở rộng từ nhóm dữ liệu 17 nước châu Á mới nổi (~40.633 doanh nghiệp) của Đỗ và Phan (2026 — VEFR) khoảng 2,5 lần.

**Mười kết luận chính**:

**(i) Phân tán năng suất nội bộ tăng đơn điệu khi phân nhóm con suy giảm**: Advanced 0,86 → Upper-middle 1,29 ≈ Emerging 1,24 ≈ SIDS 1,32 → Frontier 1,36. Tỷ số P90/P10 leo từ 10,8 lần lên 39,6 lần. Pattern này khẳng định **giả thuyết phân bổ sai nguồn lực (misallocation hypothesis)** của Hsieh & Klenow (2009, 2014) và là cơ sở thực tiễn cho H5 — điều tiết thể chế (institutional moderation) — trong CĐ2.

**(ii) Dị biệt nội bộ phân nhóm Advanced — phân nhóm con đổi mới sáng tạo dẫn dắt so với tài nguyên dẫn dắt**. Sự sụt giảm phân tán từ 1,00 (chỉ tính nhóm châu Á đổi mới sáng tạo dẫn dắt — innovation-driven) xuống 0,86 (sau khi thêm Vùng Vịnh tài nguyên dẫn dắt — resource-driven) gợi ý cần **phân nhóm con (sub-grouping) Advanced** trong CĐ2. Bằng chứng định lượng: tỷ số phân tán Singapore (1,03) so với Vùng Vịnh (0,49) ≈ **2,1 lần** — đã được tách trực quan trong **Bảng 4.1 (v3.1)**.

**(iii) Dị biệt nội bộ phân nhóm Emerging — 3 phân nhóm con** *(NEW D1, §4.9)*. Phân nhóm con FDI dẫn dắt Đông Nam Á (VNM+IDN+PHL, n=13.779; FSTS **13,2%**) khác biệt rõ với phân nhóm con dân số lớn (IND+LKA+JOR, n=32.119; FSTS **7,2%**) và phân nhóm con tài nguyên (MNG, n=1.905; FSTS **5,0%**). Phân tầng FSTS 5,0% – 7,2% – 13,2% bị *che giấu* trong số liệu tổng hợp Emerging (8,6%). Năng lực công nghệ (TCI) ngược dấu giữa ASEAN-3 (R&D 4,8%, ISO 18,8%) và Nam Á + Tây Á (R&D 19,8%, ISO 27,6%) — phản ánh hai cơ chế: học hỏi do FDI dẫn dắt (FDI-induced learning) so với học hỏi tự thân (autonomous learning) (Cohen & Levinthal, 1990).

**(iv) SIDS Thái Bình Dương (7 nước, n=1.371) có pattern đặc trưng "thích nghi và nhảy vọt"**: phân tán ở mức trung bình (sd log = 1,32), tỷ lệ đổi mới sản phẩm cao nhất nhóm (41,5%), tỷ lệ website cao bất ngờ ở 6 nước cũ (58,9% — gần ngang Advanced). **Kiribati 2025 là trường hợp biên CỰC ĐOAN nhất với FSTS chỉ 1,03%, FDI ≥10% chỉ 0,7%, website 18,7%, ISO 1,3% — gợi ý dị biệt nội bộ SIDS giữa "high digital leapfrog" (Fiji, Maldives) và "isolated rural" (Kiribati).** Pattern là cơ sở cho **H6 (forced internationalization penalty)** (Briguglio, 1995; Bertram, 2006; Đỗ & Phan, 2026 — bản thảo P8).

**(v) Quốc tế hóa là hiện tượng phân cực ở mọi phân nhóm con thể chế**: trung vị FSTS = 0% xuyên năm phân nhóm con; chỉ 15–23% doanh nghiệp tham gia xuất khẩu. Yêu cầu phương pháp luận: cần phân tích **lựa chọn hai giai đoạn (2-stage selection)** trong đặc tả đầy đủ của CĐ2.

**(vi) Nhảy vọt số (digital leapfrog) 2018–2025 ở Frontier, Emerging và SIDS Thái Bình Dương** (+20–43 đpt website). Bằng chứng tái định vị Uppsala cho kỷ nguyên số (Banalieva & Dhanaraj, 2019; Yang, Zhao & Wei, 2025); đồng nhất pattern hiệu ứng lá chắn số (digital shield effect) trên 17 nước (Đỗ & Phan, 2026 — VEFR). *Kiribati 2025 không thể hiện digital leapfrog (website chỉ 18,7%) — gợi ý leapfrog đòi hỏi điều kiện hạ tầng cơ bản tối thiểu mà Kiribati chưa đạt.*

**(vii) Pattern phi tuyến của FDI ≥10%** — dạng chữ U với cực tiểu ở Emerging (4,7%): Advanced 11,1% → Upper-middle 8,4% → Emerging 4,7% → Frontier 5,9% → SIDS 23,5%. Hai mô hình FDI khác nhau: (a) Advanced — MNE hub + Vùng Vịnh hạn chế; (b) SIDS — du lịch + viễn thông.

**(viii) Đợt khảo sát 2025 là *mẫu đơn năm lớn nhất* và *đa dạng nhất* trong nhóm dữ liệu** *(NEW D2)*. **14 nước × 16.979 doanh nghiệp** (16,8% pool) đại diện đầy đủ 5 phân nhóm con ICRV: (a) IND FSTS sụt 7,7%→2,7% (schema effect + Atmanirbhar Bharat); (b) Fiji website 74,8% > Singapore 66,1%; **Kiribati đối lập với website 18,7%, FSTS 1,03%**; (c) Vùng Vịnh + Brunei resource-driven Advanced confirmed; (d) R&D schema-induced overestimation cảnh báo.

**(ix) Khung phân tích cấp ngành (industry-level) chưa được thực hiện ở CĐ1** *(NEW D3, §4.8)*. 9 ngành ISIC Rev. 4: Manufacturing-only subsample (n≈50.000), ICT exclusion test cho DAI âm Advanced, Construction subsample test Vùng Vịnh, Tourism/Hotels separation cho SIDS. 5 giả thuyết I1-I5 đặt cho CĐ2.

**(x) Pipeline tái lập được cho 4 thế hệ khung dữ liệu WBES**. Pipeline 5 bước Python (`wbes/01_inventory.py` → `02_harmonize.py` → `03_describe.py` → `merge_macro_with_pool.py` → `fetch_macro_indicators.py`); xử lý 4 thay đổi khung dữ liệu lớn. Tất cả Bảng 4.1–4.10 và 5.1, 6.1, Phụ lục A đều tái tạo được. **Gói tái lập (replication package)** mở cho cộng đồng tiếng Việt.

**Hàm ý cho CĐ2 và luận án**:

(a) **Hệ giả thuyết H1–H6** đã có đủ bằng chứng hai biến: H1 phi tuyến; H2 TCI điều tiết; H3 DAI có điều kiện; H4 phân nhóm con thể chế (5+8 phân nhóm con); H5 cụm tài nguyên; H6 chi phí buộc phải quốc tế hóa (**7 SIDS gồm Kiribati extreme**).

(b) **8 phân nhóm con với hiệu ứng cố định** cho CĐ2 (3 Emerging sub-groups + 2 Advanced + Upper-middle + Frontier + SIDS).

(c) **Hai đặc tả mô hình kiểm định vững**: Đặc tả 1 — phạm vi đầy đủ (n=101.185, DAI/TCI đơn thành phần); Đặc tả 2 — 2018-2025 (n≈50.000, DAI/TCI 5 thành phần).

(d) **Industry FE + 5 kiểm định vững mẫu con** *(NEW D3)*.

**Phạm vi không trình bày**: hồi quy đa biến (CĐ2); panel/IV identification (CĐ2); industry-level descriptive tables (Phase 2 7/2026); năng suất USD PPP (Phase 1 6/2026); resource dependence trực tiếp (Phase 1).

### 4.8 Khung phân tích cấp ngành (industry-level) — kế hoạch CĐ2

> **Mới ở v2.9 (D3)**: Khung dữ liệu (schema) WBES phân loại theo `a3a` (mã ngành) và `a4a` (mã ISIC 4 chữ số). CĐ1 phân tích ở cấp phân nhóm con / quốc gia; phân tích cấp ngành dành cho CĐ2 và Giai đoạn 2 hoàn thiện CĐ1 (tháng 7/2026).

**Bảng 4.8.1**. *Khung phân loại 9 ngành ISIC Rev. 4 cho nhóm dữ liệu WBES.*

| Ngành | Mã ISIC | Đặc điểm | Pattern dự kiến |
|---|---|---|---|
| Manufacturing | C (10–33) | Thâm dụng vốn, định hướng xuất khẩu | FSTS cao; R&D cao; ISO cao |
| Wholesale/retail | G (45–47) | Thâm dụng lao động, định hướng trong nước | FSTS thấp; website cao; FDI thấp |
| Tourism/hotels | I (55–56) | Dịch vụ phụ thuộc du lịch | FDI cao ở SIDS |
| Transport | H (49–53) | Kinh tế mạng lưới | FDI cao; ISO cao |
| ICT | J (58–63) | Thâm dụng tri thức | R&D cao; website ~100% |
| Construction | F (41–43) | Theo dự án, định hướng trong nước | FSTS thấp; FDI ở GCC |
| Mining | B (05–09) | Tài nguyên dẫn dắt | FDI cao; ISO ở MNE-led |
| Finance | K (64–66) | Có quy chế, xuyên biên giới | FDI cao; website ~100% |
| Khác | A, D, L | Đa dạng | Hỗn hợp |

**5 giả thuyết cấp ngành cho CĐ2**: I1 Manufacturing FSTS dominance; I2 ICT digital-native (DAI−0,129 artifact?); I3 Tourism drive FDI ở SIDS; I4 Mining drive resource cluster (spillover); I5 Construction dominate Vùng Vịnh (rentier vs Construction artifact).

**5 hàm ý phương pháp luận cho CĐ2**: (a) Industry FE 9 ngành ISIC; (b) Manufacturing-only subsample robustness check; (c) Tourism/Hotels separation; (d) Construction subsample test Vùng Vịnh; (e) ICT exclusion test cho DAI Advanced.

### 4.9 Phân nhóm con Emerging — phát hiện dị biệt nội bộ

> **Mới ở v2.7 (D1)**: Phát hiện phương pháp luận thứ hai cho CĐ2 sau khi đã có phân nhóm con Advanced.

**Bảng 4.9**. *Phân nhóm con Emerging — số liệu tổng hợp 2009–2025 (n=47.803).*

| Phân nhóm con | Quốc gia | n_firms | FSTS (%) | DN xuất khẩu (%) | FDI ≥10% (%) | Website (%) | R&D (%) | ISO (%) | sd log |
|---|---|---|---|---|---|---|---|---|---|
| Emerging — FDI dẫn dắt SEA | VNM, IDN, PHL | 13.779 | **13,2** | 22,1 | 11,4 | 47,3 | 4,8 | 18,8 | 1,53 |
| Emerging — dân số lớn | IND, LKA, JOR | 32.119 | **7,2** | 13,8 | 1,9 | 49,5 | 19,8 | 27,6 | 1,16 |
| Emerging — tài nguyên | MNG | 1.905 | **5,0** | 9,7 | 4,7 | 50,1 | 20,8 | 15,4 | 1,16 |
| **Tổng Emerging** | 7 nước | **47.803** | 8,6 | 15,5 | 4,7 | 49,2 | 16,4 | 24,9 | 1,24 |

Năm phát hiện: (1) FSTS phân tầng 5,0%-7,2%-13,2% bị che giấu; (2) FDI chênh lệch 6 lần ASEAN-3 vs Nam Á+Tây Á; (3) TCI ngược dấu — FDI-induced vs autonomous learning; (4) Mongolia boundary case; (5) sd log 1,53 vs 1,16 — two-tier (Hsieh & Klenow, 2009).

### 4.10 Phân tích sâu đợt khảo sát 2025

> **Mới ở v2.8 (D2)**: Đợt 2025 chiếm 16.979 doanh nghiệp (16,8% pool — cập nhật v3.1 với Kiribati 2025).

**Bảng 4.10**. *14 quốc gia trong đợt 2025 (n=16.979 — cập nhật v3.1 với Kiribati 2025).*

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
| **Kiribati (mới v3.1)²** | **KIR** | **SIDS** | **150** | **1,0** | **0,7** | **14,0** | **18,7** | **1,48** |
| **Tổng 2025** | — | — | **16.979** | **3,8** | **2,9** | **5,4** | **44,2** | **0,90** |

*Ghi chú: ¹Nepal 2025 — khung dữ liệu BREADY chưa thống nhất. ²Kiribati 2025: WBES Country Profile 2025 + phân tích `Kiribati-2025-full-data.dta`; Lower Middle Income; phụ thuộc viện trợ Australia/New Zealand ~30% GDP.*

**Bảy phát hiện**: (1) IND FSTS sụt 5 đpt (schema effect); (2) THA "digital up, exports down"; (3) Fiji website 74,8% > Singapore (digital leapfrog); (4) Vùng Vịnh + Brunei resource-driven Advanced confirmed; (5) R&D schema-induced overestimation; (6) 2025 wave validation sample CĐ2; **(7) Kiribati extreme — FSTS 1,03%, FDI 0,7%, website 18,7%, ISO 1,3%, sd log 1,48 — đối lập với Fiji digital leapfrog. Bằng chứng dị biệt SIDS rõ rệt: "high-digital" (FJI, MDV) vs "isolated rural" (KIR) — CĐ2 cần tách 2 phân nhóm con SIDS.**

**Sáu hàm ý cho CĐ2**: (a) 2025 validation test bed; (b) Schema FE PostBREADY2024; (c) Advanced sub-grouping test trên 11 quốc gia; (d) SIDS digital leapfrog evidence cho H6; (e) Two-wave panel cho 6 nước; **(f) tách phân nhóm con SIDS — "high-digital" vs "isolated" — mở rộng 8 → 9 phân nhóm con**.

---

*Tiếp tục ở Phần 3 (Chương 5–7 + TLTK) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*

**Chương 4 nay HOÀN THIỆN với 10 mục (4.1–4.10)** — sẵn sàng trình HD TS. Nguyễn Minh Cảnh duyệt cùng Chương 5–7 (file 16).

---

*Phiên bản 3.0 (06/05/2026) — Biên tập tiếng Việt §4.1–4.10. NCS: Đỗ Thùy Hương. HD: TS. Nguyễn Minh Cảnh.*

*Phiên bản 3.1c (06/05/2026 — QW5) — Bổ sung Kiribati 2025 vào nhóm SIDS.*

*Phiên bản 3.1d-fix (06/05/2026) — Bổ sung markdown image references: Hình 4.1.1 ở §4.1 + Hình 4.2 ở §4.2. Khôi phục full content §4.7-4.10 đã bị rút gọn nhầm trong commit `36ecd13`. NCS chạy `thesis/figures/generate_figures.py` (commit `ff977f8`) để materialize 5 PNG/SVG.*
