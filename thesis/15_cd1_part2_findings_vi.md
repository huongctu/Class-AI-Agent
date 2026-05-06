# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> **Phiên bản 2.5–2.6**: Pool 101.035 firms · 47 nước · 107 country-years · 2009–2025.
> **Phiên bản 2.7 (D1)**: Bổ sung §4.9 Sub-grouping Emerging — 3 sub-groups (FDI-driven SEA, large-population, resource).
> **Phiên bản 2.8 (D2)**: Bổ sung §4.10 2025 wave deep dive — 12 nước n=16.829, so sánh historical với panel 8 nước; phát hiện schema effects + SIDS digital leapfrog + sub-grouping Advanced data.

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi pool**. Sau hòa hợp 105 file WBES, pool dữ liệu bao gồm **101.035 doanh nghiệp** thuộc **47 nền kinh tế** ở châu Á và Pacific, trải khắp **107 đơn vị quốc gia × năm khảo sát** trong giai đoạn **2009–2025**. Pool này **kế thừa và mở rộng** từ pool 17 nền kinh tế châu Á mới nổi (~40.633 doanh nghiệp) đã được tác giả công bố trước đó (Đỗ & Phan, 2026 — VEFR) — gấp ~2,5 lần coverage địa lý và ~2,5 lần số doanh nghiệp. Phân bố theo regime ICRV: Emerging 47.803 (47%), Frontier 28.678 (28%), Upper-middle 16.693 (17%), Advanced 6.640 (7%), **SIDS 1.221 (1%)**. Đặc biệt, pool đã bao gồm **12 đợt khảo sát năm 2025** với 16.829 doanh nghiệp.

**Đặc điểm boundary case SIDS Pacific**: 6 quốc gia đảo nhỏ Thái Bình Dương đầy đủ — Fiji, PNG, Solomon Islands, Tonga, Vanuatu, Samoa → tổng n=1.221. Đặc điểm Tây Á mở rộng: 9 quốc gia bao gồm Vùng Vịnh dầu mỏ (SAU, QAT, KWT, BHR — Advanced) và các nền kinh tế Trung Đông trung bình (IRQ, JOR, LBN, YEM — Frontier; ISR, CYP — Advanced).

**Phân bố thời gian**. 14 mốc khảo sát từ 2009 đến 2025; **2025 (n=16.829) là largest single-year wave** trong pool. Phân bố ba giai đoạn schema: 2009–2012 (n=14.171), 2013–2017 (n=24.564), **2018–2025 (n=62.300 — 62% pool)**.

**Ba thế hệ schema**. (i) PICS3/MENA-WBES (2009–2012); (ii) Standardized (2013–2017); (iii) Standardized 2018+, BREADY 2023/2024/2025, BEE 2023, EAP Core (**2018–2025**).

**Hòa hợp**. Pipeline Python (`wbes/02_harmonize.py`); FSTS = `d3b + d3c`; winsorize log năng suất 1/99 trong country-year.

**Caveat đơn vị tiền tệ**. Doanh thu chưa chuyển USD PPP → bảng so sánh năng suất xuyên quốc gia chỉ trình bày **thước đo dispersion** bất biến đơn vị.

### 4.2 Thực trạng năng suất lao động — dispersion trong từng quốc gia

**Bảng 4.1**. *Dispersion năng suất lao động theo regime, bình quân có trọng số (n=107 cặp quốc gia × năm).*

| Nhóm regime | Số cặp quốc gia × năm | Số doanh nghiệp | sd log năng suất | Tỷ số P90/P10 | Tỷ số P75/P25 |
|---|---|---|---|---|---|
| Advanced | 13 | 5.921 | 0,86 | 10,8 | 3,1 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 20 | 45.388 | 1,24 | 30,6 | 5,1 |
| Frontier | 42 | 18.877 | 1,36 | 39,6 | 6,1 |
| **SIDS** | **9** | **947** | **1,29** | **27,6** | **5,4** |

Năm phát hiện: (1) Advanced dispersion giảm từ 1,00 xuống 0,86 sau khi mở rộng Vùng Vịnh — heterogeneity nội bộ Advanced; (2) Frontier dispersion cao nhất (1,36) — misallocation hypothesis (Hsieh & Klenow, 2009, 2014); (3) SIDS 6 nước có dispersion trung bình (1,29); (4) P90/P10 đơn điệu Advanced→Frontier 10,8→39,6×; (5) Pattern hệ thống — bằng chứng cho H5 (institutional moderation) đồng nhất Đỗ & Phan (2026 — VEFR).

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

**Bảng 4.3**. *Cường độ quốc tế hóa, tỷ trọng exporter, tăng trưởng việc làm theo regime.*

| Nhóm regime | FSTS (%) | Exporter (%) | Tăng trưởng việc làm CAGR (%) |
|---|---|---|---|
| Advanced | 10,2 | 23,0 | 3,15 |
| Upper-middle | 10,3 | 21,7 | 4,25 |
| Emerging | 8,6 | 15,5 | 2,81 |
| Frontier | 10,1 | 16,6 | 3,65 |
| SIDS | 6,3 | 16,3 | 5,77 |

Trung vị FSTS = 0% xuyên năm regime — quốc tế hóa là hiện tượng phân cực; SIDS có tăng trưởng việc làm cao nhất (post-COVID phục hồi).

### 4.4 Thực trạng đổi mới sáng tạo và năng lực số

**Bảng 4.4**. *Tỷ lệ doanh nghiệp đổi mới sáng tạo và áp dụng số theo regime (%).*

| Nhóm regime | Sản phẩm mới | Quy trình mới | R&D dương | ISO | Website |
|---|---|---|---|---|---|
| Advanced | 22,3 | 52,3 | 16,7 | 29,9 | 59,3 |
| Upper-middle | 26,7 | 71,7 | 21,0 | 31,4 | 56,9 |
| Emerging | 17,5 | 65,2 | 16,4 | 24,9 | 49,2 |
| Frontier | 23,1 | 68,9 | 14,2 | 20,7 | 38,0 |
| **SIDS** | **41,5** | **65,1** | **11,8** | **16,5** | **58,9** |

SIDS innov_product 41,5% (cao nhất) + website 58,9% (gần Advanced) — pattern *adaptation + leapfrog*; đồng nhất phân tách TCI vs DAI mà Đỗ & Phan (2026 — VEFR) phát hiện "digital shield effect".

### 4.5 Thực trạng cấu trúc doanh nghiệp

**Bảng 4.5**. *Cấu trúc doanh nghiệp theo regime (%).*

| Nhóm regime | SME (<100 LĐ) | Exporter | FDI ≥10% |
|---|---|---|---|
| Advanced | 79,1 | 23,0 | 11,1 |
| Upper-middle | 76,2 | 21,7 | 8,4 |
| Emerging | 74,4 | 15,5 | 4,7 |
| Frontier | 85,0 | 16,5 | 5,9 |
| SIDS | **88,5** | 16,3 | **23,5** |

FDI U-shape với cực tiểu ở Emerging (4,7%); SIDS FDI cao nhất (23,5%) do tourism + viễn thông MNE-driven.

### 4.6 Bức tranh thay đổi theo thời gian — so sánh ba giai đoạn 2009–2025

**Bảng 4.6**. *Δ điểm phần trăm các chỉ số khi so sánh giai đoạn 2018–2025 với 2009–2012.*

| Nhóm regime | Δ Website | Δ Exporter | Δ FDI ≥10% | Δ R&D | Δ ISO |
|---|---|---|---|---|---|
| Advanced | n/a* | n/a* | n/a* | n/a* | n/a* |
| Upper-middle | -9,9 | +1,4 | +2,3 | +21,5 | -25,4 |
| Emerging | +20,3 | -7,5 | -10,9 | -42,1 | +1,9 |
| Frontier | +22,1 | +1,5 | -6,5 | -18,9 | +18,5 |
| SIDS | +35–43 | +6–11 | -5 đến -10 | (cập nhật) | -20 đến -25 |

\* n/a: thiếu dữ liệu giai đoạn 2009–2012 cho Advanced. Số hoá leapfrog +20–43 đpt website ở Frontier/Emerging/SIDS — bằng chứng tái định vị Uppsala cho kỷ nguyên số (Banalieva & Dhanaraj, 2019).

### 4.7 Tổng hợp Chương 4

Sáu kết luận chính (sẽ được mở rộng trong D4):

(i) Dispersion theo regime đơn điệu (Advanced 0,86 < Emerging/SIDS 1,24–1,29 < Frontier 1,36).
(ii) Heterogeneity nội bộ Advanced — sub-grouping innovation vs resource (xem §5.2 file 16).
(iii) SIDS pattern adaptation + leapfrog (innov 41,5% + website 58,9%).
(iv) Quốc tế hóa phân cực (median FSTS = 0%).
(v) Số hoá leapfrog 2018–2025 ở Frontier/Emerging/SIDS.
(vi) Pattern phi tuyến FDI U-shape (Emerging cực tiểu).

### 4.9 Sub-grouping Emerging — phát hiện heterogeneity nội bộ

> **Mới ở v2.7 (D1)**: Emerging regime với 47.803 firms gộp 7 quốc gia heterogeneous (VNM, IDN, PHL, IND, LKA, JOR, MNG). Sub-grouping nội bộ là phát hiện phương pháp luận cho CĐ2 — song song với sub-grouping Advanced (§4.2).

**Bảng 4.9**. *Sub-grouping Emerging — số liệu pooled 2009–2025 (n=47.803).*

| Sub-group | Quốc gia | n_firms | FSTS (%) | Exporter (%) | FDI ≥10% (%) | Website (%) | R&D (%) | ISO (%) | sd log |
|---|---|---|---|---|---|---|---|---|---|
| **Emerging-FDI-driven SEA** | VNM, IDN, PHL | 13.779 | **13,2** | 22,1 | 11,4 | 47,3 | 4,8 | 18,8 | 1,53 |
| **Emerging-large-population** | IND, LKA, JOR | 32.119 | **7,2** | 13,8 | 1,9 | 49,5 | 19,8 | 27,6 | 1,16 |
| **Emerging-resource** | MNG | 1.905 | **5,0** | 9,7 | 4,7 | 50,1 | 20,8 | 15,4 | 1,16 |
| **Total Emerging** | 7 nước | **47.803** | **8,6** | 15,5 | 4,7 | 49,2 | 16,4 | 24,9 | 1,24 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

**Năm phát hiện chính từ sub-grouping Emerging**:

(1) **FSTS phân tầng rõ rệt 5,0% – 7,2% – 13,2%** — *che giấu* trong Emerging-aggregate (8,6%). ASEAN-3 cao 2,6× Mongolia do FDI-driven GVC integration (Samsung/Intel/Toyota).

(2) **FDI ≥10% chênh lệch 6× giữa ASEAN-3 (11,4%) và South+West Asia (1,9%)** — chính sách hạn chế sở hữu nước ngoài + thị trường nội địa lớn của IND.

(3) **TCI ngược dấu giữa sub-groups**: ASEAN-3 R&D thấp (4,8%) ISO mid (18,8%) — *FDI-induced learning*; South+West Asia R&D cao (19,8%) ISO cao (27,6%) — *autonomous learning*. Hai con đường công nghệ khác nhau → cùng output (innov_product 17,5% Emerging-aggregate). Phù hợp Cohen & Levinthal (1990) absorptive capacity.

(4) **Mongolia là boundary case** — resource curse + late-measured TCI; bằng chứng định lượng cho Emerging-resource standalone.

(5) **Dispersion sd log differential**: ASEAN-3 (1,53) > South+West (1,16) ~ MNG (1,16). ASEAN-3 two-tier FDI vs nội địa tạo dispersion cao hơn (Hsieh & Klenow, 2009).

**Hàm ý cho CĐ2**: Sub-grouping Emerging thành 3 sub-types là phát hiện phương pháp luận thứ hai (sau sub-grouping Advanced). Trong CĐ2, dummy variables cho 5 sub-groups (Advanced-innovation, Advanced-resource, Emerging-FDI-driven, Emerging-large-population, Emerging-resource) cùng với Upper-middle, Frontier, SIDS = **8-sub-regime classification** đầy đủ.

### 4.10 2025 wave deep dive — Phân tích đợt khảo sát 2025

> **Mới ở v2.8 (D2)**: Đợt 2025 chiếm 16.829 firms (16,7% pool); đây là *largest single-year wave* trong toàn bộ pool 2009-2025. Phân tích sâu cho phép phát hiện: (a) post-COVID structural shifts; (b) schema BREADY/Standardized2025+ effects; (c) NEW Advanced entrants (Vùng Vịnh + Brunei).

**Bảng 4.10**. *12 quốc gia trong đợt 2025 (n=16.829).*

| Quốc gia | ISO3 | Regime | n_firms | FSTS (%) | Exporter (%) | FDI ≥10% (%) | R&D (%) | Website (%) | sd log |
|---|---|---|---|---|---|---|---|---|---|
| Ấn Độ | IND | Emerging | 10.479 | 2,7 | 7,0 | 1,9 | 2,2 | 41,8 | 0,83 |
| Nepal¹ | NPL | Frontier | 1.740 | n/a | n/a | n/a | n/a | n/a | n/a |
| Saudi Arabia | SAU | Advanced | 1.002 | 2,7 | 11,2 | 9,5 | 1,7 | 30,2 | **0,47** |
| Thái Lan | THA | Upper-middle | 813 | 9,3 | 17,4 | 6,3 | 8,7 | 61,9 | 1,38 |
| Sri Lanka | LKA | Emerging | 607 | 16,1 | 21,3 | 1,8 | 4,1 | 48,8 | 1,00 |
| Mongolia | MNG | Emerging | 601 | 5,9 | 11,5 | 3,2 | **20,8** | 64,7 | 1,15 |
| Qatar | QAT | Advanced | 480 | 2,3 | 6,9 | 19,4 | 0,6 | 63,3 | **0,31** |
| Afghanistan | AFG | Frontier | 480 | 6,4 | 12,3 | 1,0 | **25,8** | 45,8 | 1,42 |
| Maldives | MDV | Frontier | 154 | 5,8 | 7,2 | 4,5 | 22,4 | **73,4** | 1,36 |
| Fiji | FJI | SIDS | 151 | 12,5 | **34,7** | 9,9 | 18,8 | **74,8** | 1,09 |
| Solomon Is. | SLB | SIDS | 150 | 4,8 | 9,3 | **20,0** | 11,3 | 53,3 | 1,25 |
| Brunei | BRN | Advanced | 150 | 5,1 | 10,8 | **26,2** | 18,9 | **80,7** | 1,10 |
| Kuwait | KWT | Advanced | 150 | **0,4** | 1,3 | **0,0** | 20,7 | 69,3 | 1,15 |
| **Tổng 2025** | — | — | **16.829** | **3,9** | **8,8** | **2,9** | **5,3** | **44,4** | **0,90** |

*Nguồn: Tính toán của tác giả từ pool WBES 2025 (12 quốc gia).*
*Ghi chú: ¹Nepal 2025 (n=1.740) có nhiều trường missing trong file `.dta` — schema BREADY 2025 chưa thống nhất với code book; cần re-process trong giai đoạn hoàn thiện (xem §4.7 hạn chế D4).*

**So sánh 2025 với historical 2009-2024 (panel 8 nước)**:

| Quốc gia | FSTS pre-2025 | FSTS 2025 | Δ FSTS (đpt) | Website pre-2025 | Website 2025 | Δ Website (đpt) |
|---|---|---|---|---|---|---|
| Ấn Độ (panel 2014/2022/2025) | 7,7 | 2,7 | **−5,0** | 56,8 | 41,8 | **−15,0** |
| Thái Lan (panel 2016/2025) | 12,5 | 9,3 | **−3,2** | 52,1 | 61,9 | +9,8 |
| Sri Lanka (panel 2011/2025) | 14,2 | 16,1 | +1,9 | 31,0 | 48,8 | **+17,8** |
| Mongolia (panel 2009/2013/2019/2025) | 4,5 | 5,9 | +1,4 | 43,3 | 64,7 | **+21,4** |
| Afghanistan (panel 2014/2025) | 3,4 | 6,4 | **+3,0** | 19,5 | 45,8 | **+26,3** |
| Fiji (panel 2009/2025) | 12,2 | 12,5 | +0,3 | 41,7 | 74,8 | **+33,1** |
| Saudi Arabia (chỉ 2025) | n/a | 2,7 | **NEW** | n/a | 30,2 | **NEW** |
| Qatar (chỉ 2025) | n/a | 2,3 | **NEW** | n/a | 63,3 | **NEW** |
| Kuwait (chỉ 2025) | n/a | 0,4 | **NEW** | n/a | 69,3 | **NEW** |
| Brunei (chỉ 2025) | n/a | 5,1 | **NEW** | n/a | 80,7 | **NEW** |

**6 phát hiện chính từ 2025 wave**:

**Phát hiện 1 — FSTS Ấn Độ giảm sốc (7,7% → 2,7%, Δ −5,0 đpt)**. Đây là pattern bất ngờ nhất trong toàn bộ pool. Có 3 explanations khả dĩ: (a) **schema BREADY 2025 thay đổi định nghĩa** "main market" và "export share"; (b) **post-COVID domestic refocus** — chính sách "Atmanirbhar Bharat" (Tự lực Ấn Độ) 2020 khiến doanh nghiệp ưu tiên nội địa; (c) **mẫu BREADY 2025 nhắm đến SME nhỏ hơn** so với Standardized 2014/2022 → giảm exporter share. Hậu quả: phát hiện cho IND cần được kiểm chứng kỹ trước khi diễn giải nhân quả; có thể schema effect dominant. Việc xác định nguyên nhân chính là một phần của Giai đoạn 1 hoàn thiện CĐ1 (tháng 6/2026).

**Phát hiện 2 — Thái Lan FSTS giảm 3,2 đpt (2016 → 2025)** trong khi *website tăng 9,8 đpt* — pattern "digital up, exports down" tương tự Mongolia (§5.6 file 16) và Việt Nam (§5.3 file 16). Củng cố hypothesis **DAI là điều kiện cần nhưng không đủ** (§7.3.1 sub-point 3 file 16). Thái Lan đang chuyển dịch sang dịch vụ và thị trường nội địa (du lịch, xe máy, SME tài chính số) thay vì xuất khẩu hàng hóa.

**Phát hiện 3 — SIDS Pacific (Fiji) digital leapfrog cực mạnh trong 2025**. Fiji 2025 có website 74,8% — *cao hơn Singapore 2023 (66,1%) và gần Đài Loan 2024 (86,9%)*. Pattern này khẳng định: SIDS không *catching up*, mà *leapfrog* trực tiếp lên hạ tầng số tiên tiến (mobile money MPAiSA của Vodafone Fiji, satellite internet Starlink, e-commerce platforms). Đồng thời, FSTS chỉ 12,5% — pattern *digital leapfrog without internationalization breakthrough*. Bằng chứng cho H6 (forced internationalization penalty): cấu trúc kinh tế nhỏ-mở không thể mở rộng FSTS chỉ bằng digital adoption.

**Phát hiện 4 — Vùng Vịnh + Brunei mới gia nhập 2025 với pattern resource-driven Advanced rõ rệt**. Saudi Arabia, Qatar, Kuwait, Brunei đều có FSTS thấp (0,4–5,1%) nhưng website cao (30,2–80,7%). Brunei nổi bật với website 80,7% — *cao nhất trong pool 2025* và vượt cả Đài Loan 2024 (86,9%) gần kề. Tuy nhiên, sd log năng suất ở Vùng Vịnh cực thấp (Qatar 0,31; Saudi 0,47) — củng cố *misallocation đảo chiều* hypothesis (§5.2 file 16): trợ cấp tài chính từ rent làm phẳng dispersion một cách nhân tạo. Qatar có FDI cao 19,4% (mở cửa nhất trong Vùng Vịnh sau Vision 2030) trong khi Kuwait FDI = 0% (đóng cửa nhất).

**Phát hiện 5 — Tăng R&D ở các nước có schema mới đo lần đầu** (Mongolia 20,8%; Afghanistan 25,8%; Maldives 22,4%; Brunei 18,9%; Kuwait 20,7%). So với pre-2025, đây là số liệu *mới* được đo lần đầu (BREADY 2025 đo trực tiếp R&D dummy). **Cảnh báo phương pháp luận**: con số R&D 2025 cao chưa chắc phản ánh tăng năng lực thực — có thể là *schema-induced overestimation* do thay đổi cách hỏi (từ "did you spend on R&D in past 3 years?" sang "do you have any R&D activities?") — cần kiểm chứng bằng chỉ số đầu vào (chi tiêu R&D/doanh thu) trong CĐ2 Spec 2 (2018–2025 high-precision).

**Phát hiện 6 — 2025 wave là *most diverse single-year sample* trong pool**. 12 nước × 16.829 firms × tất cả 5 ICRV regime (Advanced 4 nước SAU/QAT/KWT/BRN; Upper-middle 1 nước THA; Emerging 3 nước IND/LKA/MNG; Frontier 3 nước AFG/MDV/NPL; SIDS 2 nước FJI/SLB) — đầu tiên có representation đầy đủ trong cùng đợt. Đây là cơ hội độc nhất để chạy *cross-sectional CĐ2 spec 1* trên đợt 2025 alone (n=16.829) — kiểm định nonlinear + moderation cubic mà không cần lo lắng schema heterogeneity giữa các đợt. CĐ2 có thể tận dụng 2025-only sub-pool như một *validation sample* cho phát hiện chính từ full pool.

**Hàm ý cho CĐ2 và luận án**:

(a) **2025 wave như test bed**: chạy specification cubic + moderation trên 2025-only (n=16.829) làm robustness check cho specification full pool (n=101.035). Phát hiện chính (sub-grouping Advanced, resource cluster, DAI conditional) phải replicate ở 2025-only mới được coi là robust.

(b) **Cảnh báo schema effects**: Ấn Độ FSTS drop 5 đpt và R&D measurement changes ở các nước mới — cần *fixed effects schema-generation* trong CĐ2 để kiểm soát artifact. Đặc biệt, biến *PostBREADY2024* dummy (1 nếu khảo sát thuộc thế hệ schema BREADY 2024+) sẽ được thử nghiệm.

(c) **NEW Advanced data**: Vùng Vịnh (SAU, QAT, KWT, BRN) + BHR 2024 cung cấp evidence quan trọng cho sub-grouping Advanced (innovation vs resource); kết hợp với HKG 2023 + KOR 2024 + TWN 2024 + ISR 2024 + CYP 2024 + SGP 2023 = **11 quốc gia × 5.921 firms** — đủ để test sub-grouping Advanced trong CĐ2 với power thống kê đủ.

(d) **SIDS digital leapfrog trong 2025**: Fiji + SLB website 53–75%; kết hợp TON 2024 (+ tương tự pattern) + WSM 2023 + VUT 2023 cho thấy leapfrog rõ rệt xuyên SIDS. Mở rộng evidence cho H6 (forced internationalization penalty) ở P8 manuscript (Đỗ & Phan, in preparation — Pacific SIDS).

(e) **Two-wave panel cho 6 nước Emerging/Frontier**: IND, LKA, MNG, AFG, FJI có ≥2 đợt khảo sát — cho phép panel analysis trong CĐ2 (mặc dù không phải full panel, là repeated cross-section). Kết hợp với Việt Nam (3 đợt) và Trung Quốc (2 đợt) → ít nhất 8 nước có panel data cho test temporal heterogeneity.

---

*Tiếp tục ở Phần 3 (Chương 5 — bảy tiểu cảnh điển hình bao gồm Pacific SIDS; Chương 6 — yếu tố giải thích sơ bộ; Chương 7 — kết luận; Tài liệu tham khảo) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*

> **Phần Chương 4 sẽ được mở rộng thêm trong D3–D4**:
> - **D3**: §4.8 Industry-level analysis framework (manufacturing vs services + 9 ngành chính)
> - **D4**: §4.7 expanded summary với 8 kết luận thay vì 6

---

*Phiên bản 2.8 (D2) — bổ sung §4.10 2025 wave deep dive (12 nước n=16.829); 6 phát hiện chính: Ấn Độ FSTS drop 5 đpt (schema effect), Thái Lan digital up exports down, Fiji website 74,8% leapfrog, Vùng Vịnh dispersion 0,31–0,47, R&D schema-induced overestimation cảnh báo, 2025 wave most diverse single-year sample. NCS: Đỗ Thùy Hương. HD: TS. Nguyễn Minh Cảnh. Cần Thơ, ngày 06/05/2026.*
