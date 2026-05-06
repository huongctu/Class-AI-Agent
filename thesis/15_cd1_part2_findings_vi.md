# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> Bảng thuật ngữ Anh-Việt: `thesis/09b_vn_term_glossary.md`.
> **Phiên bản 2.5–2.6**: Pool 101.035 firms · 47 nước · 107 country-years · 2009–2025.
> **Phiên bản 2.7–2.9 (D1–D3)**: §4.9 Sub-grouping Emerging + §4.10 2025 wave deep dive + §4.8 Industry-level framework.
> **Phiên bản 2.10 (D4 — final)**: §4.7 expanded summary với 10 kết luận chính (thay vì 6 sơ bộ); integrate phát hiện D1–D3; finalize hàm ý CĐ2.
> **Phiên bản 3.0a (06/05/2026)**: Biên tập tiếng Việt §4.1–4.3.
> **Phiên bản 3.0b (06/05/2026)**: Biên tập tiếng Việt §4.4–4.6 — terminology consistency với glossary; "regime"→"phân nhóm con"; "exporter"→"doanh nghiệp xuất khẩu"; "tourism"→"du lịch"; "MNE-driven"→"dẫn dắt bởi doanh nghiệp đa quốc gia"; "leapfrog"→"nhảy vọt số (digital leapfrog)"; "đpt" được giải thích "điểm phần trăm" lần đầu.

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
| Advanced | 13 | 5.921 | 0,86 | 10,8 | 3,1 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 20 | 45.388 | 1,24 | 30,6 | 5,1 |
| Frontier | 42 | 18.877 | 1,36 | 39,6 | 6,1 |
| SIDS | 9 | 947 | 1,29 | 27,6 | 5,4 |

5 phát hiện: (1) Advanced 1,00→0,86 sau khi bổ sung Vùng Vịnh — chứng cứ dị biệt nội bộ Advanced; (2) Frontier cao nhất — phù hợp giả thuyết **phân bổ sai nguồn lực (misallocation hypothesis)** của Hsieh & Klenow (2009, 2014); (3) SIDS ở mức trung bình; (4) tỷ số P90/P10 tăng đơn điệu theo phân nhóm con; (5) bằng chứng thực tiễn cho H5 — điều tiết thể chế (institutional moderation).

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

Chương 4 cung cấp bức tranh thực trạng đa chiều dựa trên **101.035 doanh nghiệp ở 47 nền kinh tế châu Á và Pacific (107 cặp quốc gia × năm) trong giai đoạn 2009–2025** từ pool WBES sau hòa hợp. Đây là pool có **phạm vi địa lý và thời gian rộng nhất từng được tổng hợp** cho nghiên cứu I→P trong văn liệu IB, mở rộng từ pool 17 nước châu Á mới nổi (~40.633 firms) của Đỗ và Phan (2026 — VEFR) ~2,5×.

**Mười kết luận chính** (mở rộng từ 6 sơ bộ ở các phiên bản trước, integrate phát hiện D1–D3):

**(i) Dispersion năng suất nội bộ tăng đơn điệu theo regime declension**: Advanced 0,86 → Upper-middle 1,29 ≈ Emerging 1,24 ≈ SIDS 1,29 → Frontier 1,36. P90/P10 từ 10,8 lên 39,6 lần. Pattern khẳng định misallocation hypothesis (Hsieh & Klenow, 2009, 2014) và là cơ sở thực tiễn cho H5 (institutional moderation) trong CĐ2.

**(ii) Heterogeneity nội bộ Advanced — sub-grouping innovation vs resource**. Sự sụt giảm dispersion từ 1,00 (chỉ innovation-driven Asia) xuống 0,86 (sau khi thêm resource-driven Gulf) gợi ý cần **sub-grouping Advanced** trong CĐ2 (xem §5.2 file 16). Phát hiện mới so với baseline 17 nước (Đỗ & Phan, 2026 — VEFR vốn không bao gồm Advanced regime). Bằng chứng định lượng: dispersion ratio Singapore (1,03) / Vùng Vịnh (0,49) ≈ **2,1×**.

**(iii) Heterogeneity nội bộ Emerging — 3 sub-groups** *(NEW D1, §4.9)*. Emerging-FDI-driven SEA (VNM+IDN+PHL, n=13.779; FSTS **13,2%**) ≠ Emerging-large-population (IND+LKA+JOR, n=32.119; FSTS **7,2%**) ≠ Emerging-resource (MNG, n=1.905; FSTS **5,0%**). Phân tầng FSTS 5,0%–7,2%–13,2% *che giấu* trong aggregate 8,6%. Đây là phát hiện phương pháp luận thứ hai cho 8-sub-regime classification CĐ2 (§7.3.2 file 16). TCI ngược dấu giữa ASEAN-3 (R&D 4,8%, ISO 18,8%) và South+West Asia (R&D 19,8%, ISO 27,6%) — *FDI-induced learning* vs *autonomous learning* (Cohen & Levinthal, 1990).

**(iv) SIDS Pacific (6 nước, n=1.221) có pattern đặc trưng "adaptation + leapfrog"**: dispersion trung bình (sd=1,29), innov_product cao nhất (41,5%), website cao bất ngờ (58,9% — leapfrog gần Advanced) nhưng R&D thấp (11,8%) và ISO thấp (16,5%). Pattern "small open + adaptable + low invention" là cơ sở thực tiễn cho **H6 (forced internationalization penalty)** — bằng chứng đầu tiên trên dữ liệu firm-level WBES cho boundary case này (Briguglio, 1995; Bertram, 2006; Đỗ & Phan, 2026 — P8 manuscript).

**(v) Quốc tế hóa là hiện tượng phân cực ở mọi regime**: trung vị FSTS = 0% xuyên năm regime; chỉ 15–23% doanh nghiệp tham gia xuất khẩu. Quan hệ I→P ở cấp doanh nghiệp KHÔNG phải hiện tượng phổ quát mà tập trung vào tail bên phải phân phối — đặt ra yêu cầu phương pháp luận: phân tích **2-stage selection** (selection vào exporter pool + intensity FSTS) trong CĐ2 spec đầy đủ.

**(vi) Số hoá leapfrog 2018–2025 ở Frontier, Emerging và SIDS** (+20–43 đpt website) — bằng chứng tái định vị Uppsala cho kỷ nguyên số (Banalieva & Dhanaraj, 2019; Yang, Zhao & Wei, 2025); đồng nhất pattern "digital shield effect" trên 17 nước (Đỗ & Phan, 2026 — VEFR), nay được mở rộng cho 47 nước.

**(vii) Pattern phi tuyến FDI ≥10%** (U-shape với cực tiểu Emerging 4,7%): Advanced 11,1% → Upper-middle 8,4% → Emerging 4,7% → Frontier 5,9% → SIDS 23,5%. Gợi ý hai mô hình FDI khác nhau: ở Advanced (MNE hub + Vùng Vịnh restrict ownership) và SIDS (tourism-driven + viễn thông). Trong khi ở Emerging, thị trường nội địa lớn (IND, IDN) hấp thụ FDI thấp hơn dự kiến.

**(viii) 2025 wave là *largest single-year sample* và *most diverse* trong pool** *(NEW D2, §4.10)*. 12 nước × 16.829 firms (16,7% pool) đại diện đầy đủ 5 ICRV regime trong cùng đợt. Phát hiện chính:
- (a) **IND FSTS drop sốc** 7,7%→2,7% (Δ−5 đpt) — likely schema BREADY 2025 + Atmanirbhar Bharat post-COVID;
- (b) **Fiji digital leapfrog** website 74,8% > Singapore 66,1%;
- (c) **Vùng Vịnh + Brunei resource-driven Advanced confirmed** (FSTS 0,4–5,1% + Brunei website 80,7% cao nhất pool; sd log Saudi/Qatar 0,31–0,47);
- (d) **R&D schema-induced overestimation cảnh báo** (MNG/AFG/MDV/BRN/KWT đều 18–26% R&D ở 2025 — BREADY 2025 thay đổi cách hỏi).
CĐ2 nên dùng 2025-only sub-pool làm validation sample cho specification chính.

**(ix) Industry-level analysis framework chưa được thực hiện ở CĐ1** *(NEW D3, §4.8)*. Pool 101.035 firms cần industry breakdown 9 ngành ISIC Rev. 4 cho specification CĐ2 — đặc biệt: (a) Manufacturing-only subsample n≈50.000 robustness check; (b) ICT exclusion test cho phát hiện DAI âm ở Advanced; (c) **Construction subsample test ở Vùng Vịnh** để phân biệt "rentier state" vs "Construction artifact" (Hertog, 2010); (d) Tourism/Hotels separation cho SIDS Pacific (P8 manuscript). 5 hypotheses I1–I5 đã được đặt ra để test trong CĐ2 và Giai đoạn 2 hoàn thiện CĐ1 (tháng 7/2026 — xem §7.5 file 16).

**(x) Pipeline reproducible cho 4 thế hệ schema WBES**. Pool 101.035 firms được tạo qua pipeline 5 bước Python (`wbes/01_inventory.py` → `02_harmonize.py` → `03_describe.py` → `merge_macro_with_pool.py` → `fetch_macro_indicators.py`); xử lý 4 thay đổi schema lớn (website, R&D, export channels, main market). Tất cả Bảng 4.1–4.10 và Bảng 5.1, 6.1, Phụ lục A tái tạo được từ raw `.dta`. Đây là *replication package* mở cho cộng đồng tiếng Việt — kế thừa thực hành mở (Page et al., 2021 PRISMA 2020) và mở đường cho luận án + 3 sub-papers trong `papers/` (P3 Singapore MIR, P4 Vietnam IJoEM, P5 China APJM).

**Hàm ý cho CĐ2 và luận án**:

(a) **Hệ giả thuyết H1–H6** (xây dựng trong CĐ2 §7.3.4 file 16) đã có đủ bivariate evidence ở Chương 4: H1 phi tuyến (4 sign-reversals); H2 TCI moderation (TCI×năng suất theo regime); H3 DAI conditional (Mongolia + VN + Thái Lan evidence); H4 institutional regime (5+8 sub-regimes); H5 resource cluster (MNG + Vùng Vịnh + PNG); H6 forced internationalization penalty (6 SIDS Pacific).

(b) **8 sub-regime fixed effects** cho CĐ2 đã được hoàn thiện ở §4.9 (3 Emerging sub-groups) + §5.2 file 16 (2 Advanced sub-groups) + Upper-middle + Frontier + SIDS = 8 sub-regimes. Đây là một trong 3 cải tiến phương pháp luận chính của CĐ1 (cùng với pipeline reproducible và multi-component construct measurement — xem §7.3.2 file 16).

(c) **2 specifications robustness** cho CĐ2: Spec 1 full coverage 2009–2025 (n=101.035, single-component DAI/TCI); Spec 2 high precision 2018–2025 (n≈50.000, multi-component DAI/TCI 5-chiều). Bivariate evidence Chương 4 chỉ ra: phát hiện chính ở Spec 1 phải replicate ở Spec 2 (criterion theo Aguinis et al., 2011) — đặc biệt: (i) sub-grouping Advanced dispersion ratio 2,1×; (ii) Mongolia DAI tăng nhưng FSTS không tăng; (iii) SIDS digital leapfrog + low FSTS.

(d) **Industry FE + 5 subsample robustness tests** *(NEW D3)*: Manufacturing-only, ICT-excluded, Tourism-separated SIDS, Construction-tested Gulf, Mining-excluded resource cluster — 5 hypotheses I1–I5 cần được test trong CĐ2 spec mở rộng.

**Phạm vi không trình bày trong Chương 4**:
- (a) Hồi quy đa biến (dành cho CĐ2 — §7.3.4 file 16);
- (b) Panel/IV identification (dành cho CĐ2);
- (c) Industry-level descriptive tables (Phase 2 — tháng 7/2026 — `wbes/industry_harmonize.py`);
- (d) Năng suất USD PPP (Phase 1 — tháng 6/2026 — Data360 WDI);
- (e) Resource dependence trực tiếp (WDI NY.GDP.TOTL.RT.ZS + UN Comtrade — Phase 1).

### 4.8 Industry-level analysis framework (kế hoạch CĐ2)

> **Mới ở v2.9 (D3)**: WBES schema phân loại theo `a3a` (sector code) và `a4a` (4-digit ISIC). CĐ1 phân tích regime/country level; industry-level cấp ngành dành cho CĐ2 + Giai đoạn 2 hoàn thiện CĐ1 (tháng 7/2026).

**Bảng 4.8.1**. *Khung phân loại 9 ngành ISIC Rev. 4 cho pool WBES.*

| Ngành | ISIC | Đặc điểm | Pattern dự kiến |
|---|---|---|---|
| Manufacturing | C (10–33) | Capital-intensive, export-oriented | FSTS cao; R&D cao; ISO cao |
| Wholesale/retail | G (45–47) | Labor-intensive, domestic | FSTS thấp; website cao; FDI thấp |
| Tourism/hotels | I (55–56) | Service tourism-dependent | FDI cao ở SIDS |
| Transport | H (49–53) | Network-economics | FDI cao; ISO cao |
| ICT | J (58–63) | Knowledge-intensive | R&D cao; website ~100% |
| Construction | F (41–43) | Project-based, domestic | FSTS thấp; FDI ở GCC |
| Mining | B (05–09) | Resource-driven | FDI cao; ISO ở MNE-led |
| Finance | K (64–66) | Regulated, cross-border | FDI cao; website ~100% |
| Khác | A, D, L | Heterogeneous | Mixed |

Phân bố ước tính: Manufacturing ~50%, Services ~30%, Retail ~10%, Other ~10% (chi tiết Phase 2).

**5 hypotheses industry-level cho CĐ2** (kế thừa Bharadwaj et al., 2013; Banalieva & Dhanaraj, 2019; Lall, 1992; Stallkamp & Schotter, 2021; Hertog, 2010):

**I1 (Manufacturing FSTS dominance)**: Manufacturing có FSTS cao nhất (>15% trung bình), đặc biệt Em Asia FDI-driven. Test: Manufacturing-only subsample (n≈50.000).

**I2 (ICT digital-native)**: ICT có DAI/R&D/innov cao nhất. DAI−0,129 ở Advanced có thể là artifact của *không tách ICT*. Test: ICT exclusion subsample.

**I3 (Tourism drive FDI ở SIDS)**: SIDS FDI 23,5% có thể chủ yếu từ Tourism. Test: dis-aggregate Tourism cho P8 manuscript.

**I4 (Mining drive resource cluster)**: WBES sample không bao gồm large mining MNEs → "resource curse" pattern là spillover lên non-mining firms. Test: country_resource_dependence × FSTS thay vì firm_sector × FSTS.

**I5 (Construction dominate Vùng Vịnh)**: Hertog (2010) — Construction >40% Gulf samples; "rentier state pattern" có thể là Construction artifact. **Critical test**: dis-aggregate Construction trong 5 nước Vùng Vịnh + Brunei. Nếu pattern duy trì → resource curse thật; nếu biến mất → Construction artifact.

**5 hàm ý phương pháp luận cho CĐ2**: (a) Industry FE 9 ngành ISIC (G reference); (b) Manufacturing-only subsample robustness check; (c) Tourism/Hotels separation cho SIDS; (d) Construction subsample test cho Vùng Vịnh; (e) ICT exclusion test cho Advanced DAI−0,129.

**Phạm vi không trình bày**: Industry-level descriptive tables (cần `a4a` harmonization xuyên 4 thế hệ schema; pipeline `wbes/industry_harmonize.py` — Phase 2 tháng 7/2026).

### 4.9 Sub-grouping Emerging — phát hiện heterogeneity nội bộ

> **Mới ở v2.7 (D1)**: Phát hiện phương pháp luận thứ hai cho CĐ2 sau sub-grouping Advanced.

**Bảng 4.9**. *Sub-grouping Emerging — số liệu pooled 2009–2025 (n=47.803).*

| Sub-group | Quốc gia | n_firms | FSTS (%) | Exporter (%) | FDI ≥10% (%) | Website (%) | R&D (%) | ISO (%) | sd log |
|---|---|---|---|---|---|---|---|---|---|
| **Emerging-FDI-driven SEA** | VNM, IDN, PHL | 13.779 | **13,2** | 22,1 | 11,4 | 47,3 | 4,8 | 18,8 | 1,53 |
| **Emerging-large-population** | IND, LKA, JOR | 32.119 | **7,2** | 13,8 | 1,9 | 49,5 | 19,8 | 27,6 | 1,16 |
| **Emerging-resource** | MNG | 1.905 | **5,0** | 9,7 | 4,7 | 50,1 | 20,8 | 15,4 | 1,16 |
| **Total Emerging** | 7 nước | **47.803** | 8,6 | 15,5 | 4,7 | 49,2 | 16,4 | 24,9 | 1,24 |

5 phát hiện: (1) FSTS phân tầng 5,0%–7,2%–13,2% che giấu trong aggregate; (2) FDI chênh lệch 6× ASEAN-3 vs South+West Asia; (3) TCI ngược dấu — FDI-induced learning vs autonomous learning (Cohen & Levinthal, 1990); (4) Mongolia boundary case; (5) Dispersion sd log 1,53 vs 1,16 — two-tier (Hsieh & Klenow, 2009).

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

*Ghi chú: ¹Nepal 2025 schema BREADY chưa thống nhất — re-process Phase 1.*

6 phát hiện: (1) IND FSTS drop sốc 5 đpt — schema effect; (2) THA "digital up, exports down"; (3) Fiji website 74,8% > Singapore — digital leapfrog; (4) Vùng Vịnh+Brunei resource-driven Advanced confirmed (sd log 0,31–0,47); (5) R&D schema-induced overestimation; (6) 2025 most diverse single-year — validation sample CĐ2.

5 hàm ý CĐ2: (a) 2025 validation test bed; (b) Schema FE PostBREADY2024; (c) 11-country Advanced sub-grouping test feasible; (d) SIDS digital leapfrog evidence cho H6; (e) Two-wave panel cho 6 nước Em/Frontier.

---

*Tiếp tục ở Phần 3 (Chương 5–7 + TLTK) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*

**Chương 4 nay HOÀN THIỆN với 10 mục (4.1–4.10)** — sẵn sàng trình HD TS. Nguyễn Minh Cảnh duyệt cùng Chương 5–7 (file 16).

---

*Phiên bản 2.10 (D4 — final) — §4.7 expanded summary từ 6 → 10 kết luận chính, integrate phát hiện D1 (sub-grouping Emerging), D2 (2025 wave deep dive), D3 (industry-level framework) + 4 hàm ý cho CĐ2 (H1–H6, 8 sub-regime FE, 2 specifications, industry FE + 5 subsample tests). Chương 4 hoàn thiện với 10 sub-sections (4.1–4.10). NCS: Đỗ Thùy Hương. HD: TS. Nguyễn Minh Cảnh. Cần Thơ, ngày 06/05/2026.*

*Phiên bản 3.0a (06/05/2026) — Biên tập tiếng Việt §4.1–4.3.*
*Phiên bản 3.0b (06/05/2026) — Biên tập tiếng Việt §4.4–4.6.*
