# CHUYÊN ĐỀ TIẾN SĨ SỐ 2 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 3: CHƯƠNG 6–9 + TLTK + PHỤ LỤC)

> Tiếp nối `thesis/17_cd2_part1_intro_theory_vi.md` và `thesis/18_cd2_part2_review_framework_hypotheses_vi.md`.
> **Phiên bản 1.1 (06/05/2026)**: Cập nhật §9.5 (Định hướng phát triển) và bổ sung §9.7 (Tích hợp CĐ2 với CĐ1 mở rộng) để bridge các phát hiện từ CĐ1 v2.10 (file 15) + v2.8.11 (file 16): 8-sub-regime classification, 5 industry hypotheses I1–I5, 2 specifications robustness, 2025 wave validation sample, 4 hàm ý chính sách Việt Nam.

---

## CHƯƠNG 6 — ĐẶC TẢ TÁM MÔ HÌNH THỰC NGHIỆM M0–M7

### 6.1 Tổng quan tám mô hình

**Bảng 6.1**. *Tóm tắt cấu trúc tám mô hình M0–M7.*

| Mô hình | Đặc tả rút gọn | Giả thuyết kiểm định | Số tham số chính |
|---|---|---|---|
| **M0** | P = α + β·I + Γ·X + ε | Linear baseline | 1 + k |
| **M1** | M0 + β₂·I² | Inverted-U (H1 partial) | 2 + k |
| **M2** | M1 + β₃·I³ | S-curve cubic (H1 full) | 3 + k |
| **M3** | M2 + γ₁·TCI + δ₁·(I×TCI) | + H2 TCI | 5 + k |
| **M4** | M3 + γ₂·DAI + δ₂·(I×DAI) | + H3 DAI riêng biệt | 7 + k |
| **M5** | M4 + γ₃·Manager + δ₃·(I×Manager) | + H4 Manager | 9 + k |
| **M6** | M5 + γ₄·Regime + δ₄·(I×Regime) | + H5 Institutional | 9 + 2·5 + k |
| **M7** | M6 + δ₅·(I×TCI×DAI) + δ₆·(DAI×Period₃) | + H6 + 3-way (capstone) | full |

> X gồm: log_employees, age, fdi10, sector_FE, country_FE, year_FE.

### 6.2 Đặc tả phương trình chi tiết

(Giữ nguyên — xem v1.0 commit history.)

### 6.3 Cấp độ phân tích và đơn vị quan sát

**Đơn vị quan sát**: doanh nghiệp i × quốc gia c × năm khảo sát t. Pool có 101.185 đơn vị quan sát.

**Cấu trúc dữ liệu**: pooled cross-section với 47 quốc gia × 107 năm. Một số quốc gia có panel ngắn (Trung Quốc 2012/2024, Việt Nam 2009/2015/2023, Mongolia 2009/2013/2019/2025).

**Trọng số khảo sát**. WBES sử dụng stratified random sampling. Cần trọng số `wmedian` khi tính thống kê tổng hợp.

### 6.4 Phương pháp ước lượng chính

**OLS với HC3 robust SE** (Long & Ervin, 2000); Two-way fixed effects (country × year); Cluster-robust SE; Quantile regression.

### 6.5 Kiểm định giả thuyết

H1 phi tuyến: Wald test β₂=β₃=0 với Bonferroni correction. H2 TCI: t-test δ₁ > 0. H3 DAI: t-test δ₂ > 0; F-test δ₁=δ₂. H4 Manager: t-test δ₃. H5 Institutional gradient: F-test joint. H6 Temporal: t-test δ₆ > 0.

### 6.6 Đóng góp về mô hình so với khung tham chiếu

| Tính năng | M2 hiện hành | M3 (Marano 2016) | M5 (Banalieva 2019) | **M7 CĐ2** |
|---|---|---|---|---|
| Phi tuyến cubic | ✓ | – | – | **✓** |
| TCI moderation | – | – | – | **✓** |
| DAI moderation tách bạch | – | – | ✓ | **✓** |
| Manager moderation | – | – | – | **✓** |
| Institutional gradient | – | ✓ | – | **✓ (5 regime)** |
| Temporal heterogeneity | – | – | – | **✓** |
| Three-way I×TCI×DAI | – | – | – | **✓** |
| Sub-grouping Advanced | – | – | – | **✓** |

---

## CHƯƠNG 7 — THIẾT KẾ DỮ LIỆU VÀ CHIẾN LƯỢC NHẬN DẠNG

### 7.1 Nguồn dữ liệu

**Dữ liệu chính**: Pool WBES 101.185 doanh nghiệp ở 47 nền kinh tế châu Á và Pacific × 108 cặp quốc gia × năm × 14 mốc khảo sát giai đoạn 2009–2025.

**Dữ liệu bổ sung**: WB WDI (GDP/cap PPP, FDI/GDP), WGI 6 chiều, GII (WIPO 2024), ITU Digital Hub, Data360 API.

### 7.2 Mẫu nghiên cứu dự kiến

**Pool đầy đủ**: 101.185 doanh nghiệp.

**Sub-samples**: Manufacturing only (~45.000), SME only (~76.000), Exporters only (~17.000), by regime (Advanced 5.921; Upper-middle 15.174; Emerging 47.803; Frontier 28.678; SIDS 1.221).

**Power**: n=101.185 và effect size f²=0,02 → power > 0,99 cho mọi M0–M7. SIDS subsample n=1.221 đáp ứng cho M2 nhưng không đủ M7.

### 7.3 Đo lường biến

**P chính**: log labor productivity = log(d2/l1), winsorized 1/99.
**I chính**: FSTS = d3b + d3c.
**TCI**: 2-component (rd_active + iso_cert) ở schema cũ; 5-component (+ machinery + R&D intensity + engineer ratio) ở schema 2018+.
**DAI**: 1-component (website) ở schema cũ; 5-component (+ e-commerce + ERP + cloud + AI usage) ở schema 2018+.
**Manager**: experience_yrs, gender, intl_experience.
**Regime ICRV**: 6 nhóm (Advanced-innovation, Advanced-resource, Upper-middle, Emerging, Frontier, SIDS).

### 7.4 Hòa hợp dữ liệu xuyên thế hệ schema

Pipeline 5 bước (`wbes/02_harmonize.py`); 4 thay đổi schema lớn xuyên 3 thế hệ (PICS3, Standardized, BREADY).

### 7.5 Chiến lược nhận dạng đa tầng

5 tầng: Country × Year FE; Sector × Country × Year FE; IV-discussion (distance-to-port, region-mean export propensity); Subsample replication; Placebo test.

### 7.6 Power analysis chi tiết

| Mô hình | n cần thiết | n hiện có | Power |
|---|---|---|---|
| M0–M5 | 200–2.500 | 101.185 | >0,99 |
| M6 + Regime | 5.000 | 101.185 | >0,99 |
| **M7 capstone** | 30.000 | 101.185 | **0,99** |
| M7 SIDS | 5.000 | 1.221 | 0,4 (không đủ) |

→ M7 SIDS không đủ power; phải kiểm định H5 cho SIDS riêng bằng M0–M2.

---

## CHƯƠNG 8 — KẾ HOẠCH KIỂM ĐỊNH ĐỘ VỮNG

~30 robustness checks cho mỗi giả thuyết H1–H6: alt P (ROS, growth), alt I (dummy, bucket), sub-sample by type/regime, methods (HC1, cluster, bootstrap, quantile), dạng hàm khác, placebo, sensitivity design.

---

## CHƯƠNG 9 — ĐÓNG GÓP VỀ MÔ HÌNH VÀ KẾT LUẬN

### 9.1 Đóng góp về lý thuyết

**Khung tích hợp 4 tầng + Digital lens cho châu Á**: Chuyên đề 2 đề xuất khung lý thuyết tích hợp Uppsala + RBV + Institutional Theory + Upper Echelons + Digital Capability Lens — lần đầu được hệ thống hóa cho bối cảnh châu Á + Pacific với 47 nền kinh tế.

**Tách bạch TCI và DAI**: Phân biệt năng lực công nghệ NỘI TẠI khỏi năng lực số NGOẠI TẠI.

**Sub-grouping Advanced regime**: Innovation-driven (Singapore, HK, Korea, TWN) khác resource-driven (Saudi, Qatar, Kuwait, Bahrain) — confirmed bằng dispersion ratio 2,1× ở CĐ1 v2.10 §4.2.

### 9.2 Đóng góp về mô hình

Tám mô hình M0–M7 với three-way moderation + temporal heterogeneity. Boundary case Pacific SIDS (6 nước) cho forced internationalization penalty.

### 9.3 Đóng góp về phương pháp

Pool 101.185 firms × 47 nước × 107 country-years × 14 mốc khảo sát; pipeline reproducible 5 bước Python.

### 9.4 Hạn chế của mô hình

(1) WBES không panel chuẩn → khó nhận dạng nhân quả mạnh; (2) Một số biến (psychic distance, network embeddedness) không đo được; (3) IV chưa sẵn có; (4) DAI/TCI multi-component chỉ ở schema 2018+; (5) Top manager characteristics không nhất quán xuyên đợt.

### 9.5 Định hướng phát triển — *Cập nhật v1.1 với CĐ1 expansion findings*

**Hướng 1 — Hoàn thiện CĐ2 với 6 đóng góp kế thừa từ CĐ1 v2.10**:

(a) **8-sub-regime classification** (kế thừa CĐ1 §7.3.2 sub-point 3 file 16 + §4.9 file 15):
- 1. Advanced-innovation (SGP, HKG, KOR, TWN, ISR, CYP) ~4.508
- 2. Advanced-resource (SAU, QAT, KWT, BHR, BRN) ~1.932
- 3. Upper-middle (CHN, MYS, THA, KAZ, ARM, GEO) ~16.693
- 4. Emerging-FDI-driven SEA (VNM, IDN, PHL) ~13.779
- 5. Emerging-resource (MNG) 1.905
- 6. Emerging-large-population (IND, LKA, JOR) ~32.119
- 7. Frontier (16 nước) ~28.678
- 8. SIDS (FJI, PNG, SLB, TON, VUT, WSM) 1.221

3 sub-regime-specific testable hypotheses từ CĐ1: (i) DAI âm CHỈ ở Advanced-innovation (không phải Advanced-resource); (ii) FDI dương mạnh CHỈ ở SIDS (+0,222 vs Frontier +0,068); (iii) Resource cluster (regimes 2+5+partial SIDS) có pattern riêng. Trong CĐ2, các fixed effects sẽ ở 8-sub-regimes thay vì 5-ICRV thô.

(b) **2 specifications robustness check** (kế thừa CĐ1 §7.3.2 sub-point 2):
- *Spec 1 — full coverage 2009–2025*: pool 101.185 firms với DAI single-component (website) + TCI 2-component (R&D + ISO).
- *Spec 2 — high precision 2018–2025*: sub-pool ~50.000 firms với DAI 5-component (website + e-commerce + ERP + cloud + AI usage) + TCI 5-component (R&D dummy + R&D intensity + ISO + imported machinery + engineer ratio).

Phát hiện chính phải replicate ở cả 2 specs — tiêu chí replication theo Aguinis et al. (2011) — đặc biệt: dispersion ratio 2,1×, Mongolia DAI tăng nhưng FSTS không tăng, SIDS digital leapfrog + low FSTS.

(c) **Industry FE + 5 subsample tests** (kế thừa CĐ1 §4.8 file 15):
- *Hypothesis I1*: Manufacturing FSTS dominance → Manufacturing-only subsample n≈50.000
- *Hypothesis I2*: ICT digital-native — DAI−0,129 ở Advanced có thể là artifact → ICT exclusion subsample
- *Hypothesis I3*: Tourism drives FDI ở SIDS → Tourism/Hotels separation cho P8 manuscript
- *Hypothesis I4*: Mining drives resource cluster (spillover, không phải direct) → country_resource_dependence × FSTS thay vì firm_sector × FSTS
- *Hypothesis I5*: Construction dominate Vùng Vịnh — "rentier state pattern" có thể là Construction artifact → dis-aggregate Construction trong 5 nước Vùng Vịnh + Brunei

(d) **2025 wave validation sample** (kế thừa CĐ1 §4.10 file 15): chạy CĐ2 cubic+moderation specification trên 2025-only sub-pool (n=16.829, 12 nước với tất cả 5 ICRV regimes represented) làm robustness check cho specification full pool. Schema fixed effects (PostBREADY2024 dummy) cần được thử nghiệm để kiểm soát artifact (đặc biệt IND FSTS drop −5 đpt).

(e) **Resource × Institution × Internationalization framework** (kế thừa CĐ1 §7.3.1 sub-point 2):
- Resource curse (Auty, 1993; Sachs & Warner, 2001) cần mở rộng với institutional moderation (North, 1990; Khanna & Palepu, 2010)
- Test: `Resource_dependence × FSTS` interaction với biến đo trực tiếp resource rent share trong GDP (WDI NY.GDP.TOTL.RT.ZS)
- Mongolia + Vùng Vịnh + PNG cùng "resource-dependent" nhưng FSTS 0,4–11% — institutional moderation explains divergence (Hertog, 2010; Hvidt, 2013; Gerelmaa & Kotani, 2016)

(f) **DAI điều kiện cần nhưng không đủ** (kế thừa CĐ1 §7.3.1 sub-point 3):
- Mongolia DAI 39%→65% nhưng FSTS không tăng; Việt Nam tương tự
- Bẫy *digital theatre* — tăng adoption chỉ số nhưng không tạo giá trị xuất khẩu thật
- Trong CĐ2, hypothesis: DAI moderation hiệu lực CHỈ khi đi kèm với TCI đủ cao (multi-component DAI × TCI three-way interaction trong M7)

**Hướng 2 — Triển khai luận án với 6 panels Chương 4** (kế thừa CĐ1 §7.3.4 file 16):
- *Panel A*: Full pool descriptive (101.185 firms × 47 nước × 107 country-years)
- *Panel B*: 8-sub-regime split với fixed effects
- *Panel C*: Cubic + interaction (S-curve + 4 moderators)
- *Panel D*: DAI/TCI moderation (Spec 1 vs Spec 2)
- *Panel E*: Resource cluster (sub-regimes 2+5+partial SIDS)
- *Panel F*: SIDS boundary case (forced internationalization penalty H6)

**Hướng 3 — Hoàn thiện manuscripts** (cập nhật từ CĐ1 §7.3.4 file 16):
- P3 Singapore (MIR R3 ready, R4 sẵn sàng resubmit)
- P4 Vietnam (IJoEM v5.9 round 2 ready)
- P5 China (APJM v1.8 ready)
- P8 Pacific SIDS (theory-development; preliminary evidence trong CĐ1 §5.7)
- Submission packages tại `papers/`: p3-singapore/, p4-vietnam/, p5-china/

**Hướng 4 — Hàm ý chính sách Việt Nam** (kế thừa CĐ1 §7.3.3 file 16, 4 đoạn chính sách):
- (i) Pattern two-tier không hội tụ — bộ chỉ tiêu khác biệt FDI vs nội địa (Nghị quyết 41-NQ/TW 2023, Quyết định 1414/QĐ-TTg)
- (ii) DAI multi-component cho SME — 4 chỉ số mới cho TCTK (ERP/CRM, B2B e-commerce, e-payment integration, cloud SCM); kết hợp Quyết định 749/QĐ-TTg + Đề án 06
- (iii) TCI cho SME hướng xuất khẩu — Luật 67/2025/QH15 ưu đãi thuế R&D 1,5×–2,0× + Quyết định 1851/QĐ-TTg quỹ đổi mới sáng tạo + sector-specific ISO + technical workforce (Lall, 1992)
- (iv) Sub-grouping cho ngoại giao kinh tế — 5 chiến lược FTA khác biệt theo sub-regime đối tác (RCEP, CPTPP, VKFTA, ACFTA, GCC framework, PIF Đối tác)

**Hướng 5 — Nghiên cứu mở rộng** (cập nhật):
- Áp dụng khung CĐ2 cho Latin America, Africa
- Kết hợp với meta-analysis 1980–2026 (P6 manuscript)
- Phát triển multi-level model với data macro country × year (WDI rent share, WGI 6 dims, GII)

### 9.6 Kết luận

Chuyên đề 2 thiết lập đầy đủ khung lý thuyết tích hợp 4 tầng + Digital Lens, hệ giả thuyết H1–H6, đặc tả 8 mô hình M0–M7, chiến lược dữ liệu và nhận dạng cho nghiên cứu quan hệ giữa quốc tế hóa và hiệu quả doanh nghiệp ở các quốc gia châu Á.

**Tính hệ thống**: 4 tầng lý thuyết + lăng kính số + 6 giả thuyết + 8 mô hình + chiến lược nhận dạng đa tầng + ~30 robustness checks.

**Tính mới**: tích hợp 8 yếu tố cùng lúc (phi tuyến + 4 moderators + temporal + 3-way + sub-grouping Advanced + SIDS boundary).

**Tính khả thi**: Pool 101.185 firms × 47 nước × 107 country-years cung cấp dư thừa power cho mọi M0–M7.

**Tính ứng dụng**: 4 hàm ý chính sách Việt Nam được CĐ1 §7.3.3 phát triển với 7 văn bản pháp lý cited (Nghị quyết 41-NQ/TW, Luật 67/2025/QH15, các Quyết định 749, 1414, 1851, 06, 493).

**Tính tích hợp với CĐ1**: 6 đóng góp kế thừa được tích hợp vào CĐ2 (8-sub-regime, 2 specifications, industry FE + 5 subsample tests, 2025 validation, Resource×Institution framework, DAI conditional). Xem chi tiết §9.7.

CĐ2 cùng với CĐ1 (mô tả thực trạng + sub-grouping Emerging + 2025 wave deep dive + industry framework) thiết lập đầy đủ nền tảng cho luận án "Quốc tế hóa và hiệu quả hoạt động kinh doanh của doanh nghiệp ở các quốc gia châu Á: Vai trò điều tiết của thể chế, năng lực số và đặc điểm nhà quản trị".

### 9.7 Tích hợp CĐ2 với CĐ1 mở rộng — *Mới ở v1.1*

**Bảng 9.1**. *Ánh xạ phát hiện CĐ1 v2.10 → ứng dụng trong CĐ2.*

| CĐ1 phát hiện | File / Mục | CĐ2 ứng dụng |
|---|---|---|
| Sub-grouping Advanced (innovation-driven vs resource-driven, dispersion ratio 2,1×) | file 16 §5.2 + file 15 §4.2 | M6/M7 fixed effects 8 sub-regimes (Advanced-innovation D₁ + Advanced-resource D₂) |
| Sub-grouping Emerging (3 sub-groups: FDI-driven SEA, large-population, resource) | file 15 §4.9 | M6/M7 fixed effects 8 sub-regimes (Emerging-FDI D₄ + Emerging-resource D₅ + Emerging-large D₆) |
| 8 sub-regime classification chi tiết | file 16 §7.3.2 sub-point 3 | M6 institutional moderation H5 với 8 dummies thay vì 5 ICRV thô |
| 2 specifications robustness (full coverage 2009–2025 vs high precision 2018–2025) | file 16 §7.3.2 sub-point 2 | Spec 1 (M0–M7 single-component) + Spec 2 (M3–M7 multi-component); criterion theo Aguinis et al. (2011) |
| 5 industry hypotheses I1–I5 | file 15 §4.8 | CĐ2 industry FE + 5 subsample tests (Manufacturing-only, ICT-excluded, Tourism-separated, Construction-tested Gulf, Mining-excluded) |
| 2025 wave deep dive (12 nước, n=16.829, all 5 ICRV regimes) | file 15 §4.10 | CĐ2 validation sample — 2025-only specification làm robustness check; PostBREADY2024 fixed effects |
| Mongolia DAI tăng nhưng FSTS không tăng | file 16 §5.6 + file 15 §4.10 | H3 DAI conditional + H5 resource cluster pattern; CĐ2 test `Resource_dependence × FSTS × DAI` 3-way |
| Resource cluster (Mongolia + Vùng Vịnh + PNG) | file 16 §5.2 + §5.6 + §5.7 | H5 resource cluster sub-hypothesis trong M7; biến đo trực tiếp resource rent share |
| 4 hàm ý chính sách Việt Nam | file 16 §7.3.3 | CĐ2 Hướng 4 (chính sách); luận án Chương 5 thảo luận |
| 7 văn bản pháp lý Việt Nam | file 04 Section O | CĐ2 + luận án Chương 5 cite |
| Khung "Resource × Institution × Internationalization" | file 16 §7.3.1 sub-point 2 | M7 capstone với three-way `Resource × Institution × FSTS` |
| Bẫy *digital theatre* | file 16 §7.3.1 sub-point 3 | H3 DAI conditional + cảnh báo policy ở Hướng 4 |
| 7 sản phẩm khoa học (2 published + 3 in preparation + 1 sub-pool + 1 dissertation) | file 16 §7.3.4 | CĐ2 + luận án triangulation evidence |

**Workflow CĐ1 → CĐ2 → Luận án**:

```
CĐ1 v2.10 (101.185 firms descriptive + 8 sub-regimes + 5 industry hypotheses)
    ↓
CĐ2 v1.1 (M0–M7 với 8 sub-regime FE + 2 specs + industry FE + 2025 validation)
    ↓
Luận án 5 chương (kế thừa CĐ1+CĐ2 + 6 panels Chương 4 + 4 hàm ý chính sách)
    ↓
3 sub-papers (P3 SG MIR, P4 VN IJoEM, P5 CN APJM) tại `papers/` triangulation
```

**Lộ trình hoàn thiện Q2 2026 → Q3 2027** (kế thừa CĐ1 §7.5):
- Q2 2026: CĐ1 v2.10 + CĐ2 v1.1 hoàn thiện
- Q3 2026: Bảo vệ chuyên đề trước Hội đồng CTU (tháng 8–9/2026)
- Q4 2026: Luận án Chương 1–3 (kế thừa lý thuyết + phương pháp luận từ CĐ1+CĐ2)
- Q1 2027: Luận án Chương 4 (Kết quả) — pool 101.185 × 8 sub-regimes × 2 specs × 6 panels
- Q2 2027: Luận án Chương 5 (Thảo luận + Kết luận) — triangulation 3 sub-papers
- Q3 2027: Bảo vệ luận án cấp Trường

CĐ2 nay tích hợp đầy đủ với CĐ1 mở rộng — cùng tạo *programme of research* có cấu trúc với 7 sản phẩm khoa học, không phải chuỗi paper rời rạc.

---

## TÀI LIỆU THAM KHẢO

> Trích dẫn theo APA 7th. Danh mục đầy đủ ở `thesis/04_references_apa7.md` (đã mở rộng v2.0 với Section N — Lý thuyết tài nguyên + thể chế + boundary cases và Section O — Văn bản pháp lý Việt Nam).

**Các tham khảo chính cited trong CĐ2** (đầy đủ trong file 04):

Ang (2008); Arte & Larimo (2022); Auty (1993); Aw, Chung & Roberts (2000); Banalieva & Dhanaraj (2019); Bao, Chen & Zhou (2017); Barney (1991); Bausch & Krist (2007); Beblawi (1987); Bell & Pavitt (1995); Bertram (2006); Bhandari, Ranta & Salo (2023); Briguglio (1995); Cannella, Park & Lee (2008); Chen & Tan (2012); Cohen & Levinthal (1990); Coltman et al. (2008); Contractor, Kundu & Hsu (2003); Contractor, Kumar & Kundu (2007); Đỗ & Phan (2026 — VEFR P1; JFAR P2; in preparation P3 SG, P4 VN, P5 CN, P8 Pacific SIDS); Gerelmaa & Kotani (2016); Glaum & Oesterle (2007); Gomes & Ramaswamy (1999); Greene (2018); Hall & Soskice (2001); Hambrick (2007); Hambrick & Mason (1984); Hennart (2007); Hertog (2010); Hitt, Hoskisson & Kim (1997); Hsieh & Klenow (2009, 2014); Hsu & Boggs (2003); Hsu, Chen & Cheng (2013); Hvidt (2013); Johanson & Vahlne (1977, 2009); Kaufmann, Kraay & Mastruzzi (2011); Khanna & Palepu (2010); Kirca et al. (2012); Knight & Cavusgil (2004); Lall (1992); Li, Liu & Qian (2022); Lind & Mehlum (2010); Liu & Zhang (2024); Long & Ervin (2000); Lu & Beamish (2004); Luo & Tung (2007); Marano et al. (2016); Mathews (2002); Nielsen & Nielsen (2011); North (1990); Page et al. (2021); Peng (2003); Peng, Wang & Jiang (2008); Pierce & Aguinis (2013); Riahi-Belkaoui (1998); Sachs & Warner (2001); Stallkamp & Schotter (2021); Tallman & Li (1996); Teece, Pisano & Shuen (1997); Torraco (2005); Tran (2014); Tran & Pham (2024); Verbeke & Brugman (2009); Verhoef et al. (2021); Wernerfelt (1984); WIPO (2024); Wooldridge (2010); World Bank (2019, 2023, 2024, n.d.); Wu, Wood & Khan (2022); Xiao, Tylecote & Liu (2013); Yang, Zhao & Wei (2025); Yiu & Lau (2008).

**Văn bản pháp lý Việt Nam** (cited trong §9.5 Hướng 4): Nghị quyết 41-NQ/TW (2023); Luật 67/2025/QH15; Quyết định 749/QĐ-TTg (2020); Quyết định 1414/QĐ-TTg (2021a); Quyết định 1851/QĐ-TTg (2021b); Quyết định 06/QĐ-TTg (2022a); Quyết định 493/QĐ-TTg (2022b). Hiệp định FTA: CPTPP, VKFTA, RCEP, ACFTA, AEC, GCC-VN, PIF.

---

## PHỤ LỤC

### Phụ lục A — Bảng định nghĩa biến CĐ2

(Giữ nguyên — xem v1.0 commit history.)

### Phụ lục B – G

(Sơ đồ mô hình M0–M7; Bảng giả thuyết H1–H6; Bộ mã Stata mẫu cho M2 và M7; Bảng crosswalk schema WBES; Power analysis chi tiết; So sánh khung CĐ2 với 4 khung tham chiếu — giữ nguyên v1.0.)

---

*Phiên bản 1.1 (06/05/2026) — bản nháp đầy đủ ba phần CĐ2; cập nhật §9.5 (6 đóng góp kế thừa từ CĐ1) + §9.6 (kết luận tích hợp) + §9.7 (mới: tích hợp CĐ2 với CĐ1 mở rộng) — bridge các phát hiện CĐ1 v2.10 (file 15) + v2.8.11 (file 16) vào CĐ2: 8-sub-regime classification, 5 industry hypotheses I1–I5, 2 specifications robustness, 2025 wave validation sample, 4 hàm ý chính sách Việt Nam, Resource×Institution framework, bẫy digital theatre. NCS: Đỗ Thùy Hương. HD chuyên đề: PGS.TS. Phan Anh Tú. Cần Thơ, ngày 06/05/2026.*
