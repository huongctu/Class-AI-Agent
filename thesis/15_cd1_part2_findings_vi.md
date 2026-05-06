# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> **Phiên bản 2.5–2.6**: Pool 101.035 firms · 47 nước · 107 country-years · 2009–2025.
> **Phiên bản 2.7 (D1)**: Bổ sung §4.9 Sub-grouping Emerging — 3 sub-groups.
> **Phiên bản 2.8 (D2)**: Bổ sung §4.10 2025 wave deep dive — 12 nước n=16.829.
> **Phiên bản 2.9 (D3)**: Bổ sung §4.8 Industry-level analysis framework — 9 ngành ISIC Rev. 4 + 5 hypotheses + roadmap CĐ2.

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi pool**. Sau hòa hợp 105 file WBES, pool dữ liệu bao gồm **101.035 doanh nghiệp** thuộc **47 nền kinh tế** ở châu Á và Pacific, trải khắp **107 đơn vị quốc gia × năm khảo sát** trong giai đoạn **2009–2025**. Pool này **kế thừa và mở rộng** từ pool 17 nền kinh tế châu Á mới nổi (~40.633 doanh nghiệp) đã được tác giả công bố trước đó (Đỗ & Phan, 2026 — VEFR) — gấp ~2,5 lần coverage địa lý và ~2,5 lần số doanh nghiệp. Phân bố theo regime ICRV: Emerging 47.803 (47%), Frontier 28.678 (28%), Upper-middle 16.693 (17%), Advanced 6.640 (7%), **SIDS 1.221 (1%)**. Đặc biệt, pool đã bao gồm **12 đợt khảo sát năm 2025** với 16.829 doanh nghiệp.

**Đặc điểm boundary case SIDS Pacific**: 6 quốc gia Pacific đầy đủ — Fiji, PNG, Solomon Islands, Tonga, Vanuatu, Samoa → tổng n=1.221. **Tây Á mở rộng**: 9 quốc gia bao gồm Vùng Vịnh dầu mỏ (SAU, QAT, KWT, BHR — Advanced) và các nền Trung Đông trung bình.

**Phân bố thời gian**: 14 mốc khảo sát từ 2009 đến 2025; **2025 (n=16.829) là largest single-year wave**. Phân bố ba giai đoạn schema: 2009–2012 (n=14.171), 2013–2017 (n=24.564), **2018–2025 (n=62.300 — 62% pool)**.

**Hòa hợp**. Pipeline Python (`wbes/02_harmonize.py`); FSTS = `d3b + d3c`; winsorize log năng suất 1/99 trong country-year. Doanh thu chưa chuyển USD PPP → bảng so sánh chỉ dùng dispersion.

### 4.2 Thực trạng năng suất lao động — dispersion trong từng quốc gia

**Bảng 4.1**. *Dispersion năng suất lao động theo regime (n=107 cặp quốc gia × năm).*

| Nhóm regime | Số cặp quốc gia × năm | n_firms | sd log năng suất | P90/P10 | P75/P25 |
|---|---|---|---|---|---|
| Advanced | 13 | 5.921 | 0,86 | 10,8 | 3,1 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 20 | 45.388 | 1,24 | 30,6 | 5,1 |
| Frontier | 42 | 18.877 | 1,36 | 39,6 | 6,1 |
| **SIDS** | **9** | **947** | **1,29** | **27,6** | **5,4** |

5 phát hiện: (1) Advanced dispersion giảm 1,00→0,86 do mở rộng Vùng Vịnh — heterogeneity Advanced; (2) Frontier dispersion cao nhất — misallocation hypothesis (Hsieh & Klenow, 2009, 2014); (3) SIDS dispersion trung bình; (4) P90/P10 đơn điệu Advanced→Frontier; (5) Pattern hệ thống — H5 institutional moderation evidence đồng nhất Đỗ & Phan (2026 — VEFR).

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

**Bảng 4.3**. *Cường độ quốc tế hóa, exporter share, tăng trưởng việc làm theo regime.*

| Nhóm regime | FSTS (%) | Exporter (%) | CAGR việc làm (%) |
|---|---|---|---|
| Advanced | 10,2 | 23,0 | 3,15 |
| Upper-middle | 10,3 | 21,7 | 4,25 |
| Emerging | 8,6 | 15,5 | 2,81 |
| Frontier | 10,1 | 16,6 | 3,65 |
| SIDS | 6,3 | 16,3 | 5,77 |

Median FSTS = 0% xuyên năm regime — phân cực; SIDS CAGR cao nhất (post-COVID phục hồi).

### 4.4 Thực trạng đổi mới sáng tạo và năng lực số

**Bảng 4.4**. *Đổi mới sáng tạo và áp dụng số theo regime (%).*

| Nhóm regime | Sản phẩm mới | Quy trình mới | R&D dương | ISO | Website |
|---|---|---|---|---|---|
| Advanced | 22,3 | 52,3 | 16,7 | 29,9 | 59,3 |
| Upper-middle | 26,7 | 71,7 | 21,0 | 31,4 | 56,9 |
| Emerging | 17,5 | 65,2 | 16,4 | 24,9 | 49,2 |
| Frontier | 23,1 | 68,9 | 14,2 | 20,7 | 38,0 |
| **SIDS** | **41,5** | 65,1 | 11,8 | 16,5 | **58,9** |

SIDS innov_product 41,5% (cao nhất) + website 58,9% — pattern *adaptation + leapfrog*; phân tách TCI vs DAI (Đỗ & Phan, 2026 — VEFR).

### 4.5 Thực trạng cấu trúc doanh nghiệp

**Bảng 4.5**. *Cấu trúc doanh nghiệp theo regime (%).*

| Nhóm regime | SME | Exporter | FDI ≥10% |
|---|---|---|---|
| Advanced | 79,1 | 23,0 | 11,1 |
| Upper-middle | 76,2 | 21,7 | 8,4 |
| Emerging | 74,4 | 15,5 | 4,7 |
| Frontier | 85,0 | 16,5 | 5,9 |
| SIDS | **88,5** | 16,3 | **23,5** |

FDI U-shape Advanced→Emerging→SIDS với cực tiểu Emerging (4,7%); SIDS FDI cao nhất do tourism + viễn thông MNE-driven.

### 4.6 Bức tranh thay đổi theo thời gian — so sánh ba giai đoạn

**Bảng 4.6**. *Δ điểm phần trăm 2018–2025 vs 2009–2012.*

| Nhóm | Δ Website | Δ Exporter | Δ FDI | Δ R&D | Δ ISO |
|---|---|---|---|---|---|
| Upper-middle | -9,9 | +1,4 | +2,3 | +21,5 | -25,4 |
| Emerging | +20,3 | -7,5 | -10,9 | -42,1 | +1,9 |
| Frontier | +22,1 | +1,5 | -6,5 | -18,9 | +18,5 |
| SIDS | +35–43 | +6–11 | -5 đến -10 | (cập nhật) | -20 đến -25 |

Số hoá leapfrog +20–43 đpt website ở Frontier/Emerging/SIDS — Banalieva & Dhanaraj (2019).

### 4.7 Tổng hợp Chương 4

Sáu kết luận sơ bộ (sẽ mở rộng D4):

(i) Dispersion regime declension đơn điệu; (ii) Heterogeneity nội bộ Advanced; (iii) SIDS adaptation + leapfrog; (iv) Quốc tế hóa phân cực; (v) Số hoá leapfrog 2018–2025; (vi) Pattern phi tuyến FDI U-shape.

### 4.8 Industry-level analysis framework (kế hoạch CĐ2)

> **Mới ở v2.9 (D3)**: WBES schema phân loại doanh nghiệp theo `a3a` (sector code) và `a4a` (4-digit ISIC industry code). Trong CĐ1 hiện tại, phân tích ở regime/country level. Industry-level analysis cấp ngành sẽ được triển khai trong CĐ2 và Giai đoạn 2 hoàn thiện CĐ1 (tháng 7/2026 — xem §7.5 file 16). Phần này trình bày *khung phương pháp luận* + *5 hypotheses dựa trên literature* để định hình sub-analysis sắp tới.

**Bảng 4.8.1**. *Khung phân loại 9 ngành ISIC Rev. 4 cho pool WBES.*

| Ngành | ISIC Rev. 4 (1-digit) | Đặc điểm | Pattern dự kiến (literature) |
|---|---|---|---|
| (a) **Sản xuất chế biến chế tạo** | C (10–33) | Capital-intensive; export-oriented | FSTS cao; R&D cao; ISO cao |
| (b) **Bán buôn & bán lẻ** | G (45–47) | Labor-intensive; domestic-focus | FSTS thấp; website cao; FDI thấp |
| (c) **Khách sạn & nhà hàng** | I (55–56) | Service tourism-dependent | FSTS phụ thuộc tourism; FDI cao ở SIDS |
| (d) **Vận tải & kho bãi** | H (49–53) | Network-economics | FDI cao; ISO cao (chuẩn quốc tế) |
| (e) **ICT** | J (58–63) | Knowledge-intensive | R&D cao; website ~100%; innov cao |
| (f) **Xây dựng** | F (41–43) | Project-based; domestic | FSTS thấp; FDI ở GCC |
| (g) **Khai khoáng** | B (05–09) | Resource-driven | FDI cao; ISO ở MNE-led |
| (h) **Tài chính** | K (64–66) | Regulated; cross-border | FDI cao; website ~100% |
| (i) **Khác** (Ag, energy, real estate) | A, D, L | Heterogeneous | Mixed |

**Phân bố ngành trong pool 101.035 firms**. WBES sample ưu tiên Manufacturing (chủ đạo trong PICS3 và Standardized 2013–2017) + Services (thêm vào từ Standardized 2018+). Phân bố ước tính: Manufacturing ~50%, Services ~30%, Retail ~10%, các ngành còn lại ~10%. (Bảng phân bố chi tiết sẽ được tính trong Giai đoạn 2 — tháng 7/2026 — với pipeline `wbes/03_describe.py` mở rộng nhóm theo `a3a`.)

**5 hypotheses về industry-level patterns** (kế thừa Bharadwaj et al., 2013; Banalieva & Dhanaraj, 2019; Lall, 1992; Stallkamp & Schotter, 2021):

**Hypothesis I1 (Manufacturing FSTS dominance)**: Manufacturing có FSTS cao nhất xuyên các ngành (>15% trung bình toàn pool), đặc biệt ở Em Asia FDI-driven (VNM, IDN). Cơ sở: truyền thống "tradeable goods" của internationalization theory; FDI MNE thường đặt nhà máy sản xuất ở Emerging Asia (Việt Nam: Samsung/Intel; Indonesia: Toyota/Honda). Hệ quả phương pháp luận: CĐ2 nên thử *Manufacturing-only subsample* (n≈50.000) làm robustness check cho specification chính.

**Hypothesis I2 (ICT digital-native)**: ICT có DAI cao nhất, R&D cao nhất, innov_product cao nhất xuyên các ngành. Cơ sở: pattern *digital-native sector* (Stallkamp & Schotter, 2021). Hệ quả: phát hiện DAI âm ở Advanced (−0,129 trong Bảng 6.1) có thể là *artifact của dis-aggregation* — Advanced bao gồm cả ICT (DAI dương) và Construction Vùng Vịnh (DAI yếu). CĐ2 cần *exclude ICT subsample* để kiểm chứng pattern thực của DAI.

**Hypothesis I3 (Tourism/Hotels ở SIDS dominate FDI)**: Tourism + Hotels (ngành I) chiếm tỷ lệ lớn trong sample SIDS Pacific và là nguồn gốc FDI 23,5% (§4.5). Việc không tách Tourism/Hotels khỏi Services aggregate có thể che giấu pattern. Hệ quả: sub-analysis SIDS Pacific (P8 manuscript Đỗ & Phan, 2026) cần dis-aggregate ngành I để xác định liệu pattern FDI×năng suất dương (+0,222) là pattern Tourism hay general SIDS.

**Hypothesis I4 (Mining drives resource cluster)**: Mining/Resource ngành ở MNG (đồng/vàng/than đá), SAU/QAT/KWT (dầu mỏ), PNG (khoáng sản) — driven sub-grouping resource (xem §4.9 + §5.6 file 16). Tuy nhiên, WBES sample thường KHÔNG bao gồm doanh nghiệp khai khoáng lớn (MNE state-owned hoặc joint venture với chính phủ). Hệ quả: pattern "resource curse" quan sát trong Mongolia + Vùng Vịnh là pattern *spillover effect lên doanh nghiệp ngoài khai khoáng* — không phải pattern doanh nghiệp khai khoáng trực tiếp. CĐ2 cần test interaction `country_resource_dependence × FSTS` thay vì `firm_sector_mining × FSTS`.

**Hypothesis I5 (Construction dominate Vùng Vịnh)**: Trong các nước Vùng Vịnh, doanh nghiệp xây dựng chiếm >40% mẫu WBES (Hertog, 2010). Pattern "low FSTS + low R&D + medium ISO" của Vùng Vịnh có thể *là pattern Construction*, không phải "rentier state pattern" thuần túy. Hệ quả: CĐ2 cần *dis-aggregate Construction subsample* ở Vùng Vịnh để kiểm chứng "rentier state hypothesis" — nếu pattern duy trì sau khi loại Construction → resource curse là explanation chính; nếu pattern biến mất → Construction artifact.

**Hàm ý phương pháp luận cho CĐ2**:

(a) **Industry fixed effects**: thay vì gộp tất cả ngành, CĐ2 sẽ thêm dummy variables cho 9 ngành ISIC Rev. 4 (G làm reference) — control biến quan trọng cho heterogeneity. Hệ số sub-regime trong §7.3.2 file 16 cần được re-estimate sau khi thêm industry FE.

(b) **Manufacturing-only subsample** (n≈50.000): làm robustness check cho phát hiện chính từ full pool. Phát hiện chính (sub-grouping Advanced, resource cluster, DAI conditional) phải replicate ở Manufacturing-only mới được coi là robust ngành-độc-lập.

(c) **Tách Tourism/Hotels khỏi Services aggregate**: cần thiết cho phân tích SIDS Pacific (Đỗ & Phan, in preparation — P8 manuscript). Tourism là *driver hypothesis* cho FDI×năng suất ở SIDS; nếu không tách thì confound với Retail/Wholesale.

(d) **Construction subsample test ở Vùng Vịnh**: dis-aggregate ở 5 nước Advanced-resource (SAU, QAT, KWT, BHR, BRN) để kiểm chứng "rentier state pattern" có phải artifact Construction.

(e) **ICT subsample exclusion test**: làm robustness cho phát hiện DAI âm ở Advanced (−0,129) trong Bảng 6.1. Nếu DAI−0,129 biến mất khi loại ICT → DAI âm là artifact của Vùng Vịnh Construction (single-component bias); nếu duy trì → DAI single-component thật sự không phù hợp ở Advanced.

**Phạm vi không làm trong chuyên đề 1**: Không trình bày industry-level descriptive tables (Bảng 4.1–4.6 hiện chỉ ở regime level) do (i) thiếu data harmonization xuyên schema cho `a4a` 4-digit ISIC; (ii) một số schema 2009–2017 dùng coding khác (PICS3 dùng A1–A9, MENA-WBES 2010 dùng GroupSector); (iii) cần thêm pipeline `wbes/industry_harmonize.py` để map 4 thế hệ ISIC codes → ISIC Rev. 4. Hoàn thiện trong **Giai đoạn 2 (tháng 7/2026)** theo §7.5 file 16; output sẽ được tích hợp vào CĐ2 và luận án Chương 4.

### 4.9 Sub-grouping Emerging — phát hiện heterogeneity nội bộ

> **Mới ở v2.7 (D1)**: Emerging regime với 47.803 firms gộp 7 quốc gia heterogeneous. Sub-grouping nội bộ là phát hiện phương pháp luận thứ hai cho CĐ2.

**Bảng 4.9**. *Sub-grouping Emerging — số liệu pooled 2009–2025 (n=47.803).*

| Sub-group | Quốc gia | n_firms | FSTS (%) | Exporter (%) | FDI ≥10% (%) | Website (%) | R&D (%) | ISO (%) | sd log |
|---|---|---|---|---|---|---|---|---|---|
| **Emerging-FDI-driven SEA** | VNM, IDN, PHL | 13.779 | **13,2** | 22,1 | 11,4 | 47,3 | 4,8 | 18,8 | 1,53 |
| **Emerging-large-population** | IND, LKA, JOR | 32.119 | **7,2** | 13,8 | 1,9 | 49,5 | 19,8 | 27,6 | 1,16 |
| **Emerging-resource** | MNG | 1.905 | **5,0** | 9,7 | 4,7 | 50,1 | 20,8 | 15,4 | 1,16 |
| **Total Emerging** | 7 nước | **47.803** | **8,6** | 15,5 | 4,7 | 49,2 | 16,4 | 24,9 | 1,24 |

5 phát hiện: (1) FSTS phân tầng 5,0%–7,2%–13,2% che giấu trong aggregate 8,6%; (2) FDI chênh lệch 6× ASEAN-3 vs South+West Asia; (3) TCI ngược dấu — FDI-induced learning vs autonomous learning (Cohen & Levinthal, 1990); (4) Mongolia boundary case; (5) Dispersion sd log 1,53 vs 1,16 — two-tier (Hsieh & Klenow, 2009).

### 4.10 2025 wave deep dive — Phân tích đợt khảo sát 2025

> **Mới ở v2.8 (D2)**: Đợt 2025 chiếm 16.829 firms (16,7% pool); largest single-year wave; phát hiện schema effects + SIDS digital leapfrog + sub-grouping Advanced data.

**Bảng 4.10**. *12 quốc gia trong đợt 2025 (n=16.829).*

| Quốc gia | ISO3 | Regime | n_firms | FSTS (%) | FDI (%) | R&D (%) | Website (%) | sd log |
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

*Ghi chú: ¹Nepal 2025 schema BREADY chưa thống nhất — re-process Giai đoạn 1 (tháng 6/2026).*

**6 phát hiện chính từ 2025 wave**:

(1) **IND FSTS drop sốc 7,7%→2,7% (Δ−5,0 đpt)** — schema BREADY 2025 + Atmanirbhar Bharat post-COVID + SME sample shift; cần kiểm chứng Giai đoạn 1.

(2) **THA "digital up, exports down"** (FSTS −3,2 đpt, Website +9,8 đpt) — confirms DAI điều kiện cần nhưng không đủ (§7.3.1 sub-point 3 file 16).

(3) **Fiji digital leapfrog** (Website 74,8% > Singapore 66,1%) — *digital leapfrog without internationalization breakthrough* (FSTS chỉ 12,5%) → bằng chứng cho H6 forced internationalization penalty.

(4) **Vùng Vịnh + Brunei resource-driven Advanced** — FSTS 0,4–5,1% nhưng Website 30,2–80,7%; sd log Saudi/Qatar 0,31–0,47 — *misallocation đảo chiều*; QAT FDI 19,4% (mở cửa) vs KWT 0% (đóng cửa).

(5) **R&D schema-induced overestimation cảnh báo**: MNG/AFG/MDV/BRN/KWT đều 18–26% R&D ở 2025 — BREADY 2025 thay đổi cách hỏi; CĐ2 Spec 2 cần kiểm chứng với R&D intensity.

(6) **2025 wave là *most diverse single-year sample***: 12 nước × tất cả 5 ICRV regimes — có thể chạy CĐ2 cubic+moderation 2025-only làm validation.

**5 hàm ý cho CĐ2**: (a) 2025 validation test bed; (b) Schema fixed effects (PostBREADY2024 dummy); (c) 11-country Advanced sub-grouping test feasible (n=5.921); (d) SIDS digital leapfrog evidence cho H6; (e) Two-wave panel cho 6 nước Em/Frontier enables temporal tests.

---

*Tiếp tục ở Phần 3 (Chương 5–7 + TLTK) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*

> **Phần Chương 4 sẽ được mở rộng thêm trong D4**: §4.7 expanded summary với 8–10 kết luận thay vì 6 sơ bộ.

---

*Phiên bản 2.9 (D3) — bổ sung §4.8 Industry-level analysis framework: 9 ngành ISIC Rev. 4, 5 hypotheses (Manufacturing FSTS dominance, ICT digital-native, Tourism FDI driver, Mining resource cluster, Construction Vùng Vịnh artifact), 5 hàm ý phương pháp luận cho CĐ2 (industry FE, Manufacturing-only subsample, Tourism dis-aggregate, Construction test, ICT exclusion test). NCS: Đỗ Thùy Hương. HD: TS. Nguyễn Minh Cảnh. Cần Thơ, ngày 06/05/2026.*
