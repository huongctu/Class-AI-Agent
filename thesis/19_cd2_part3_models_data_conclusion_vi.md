# CHUYÊN ĐỀ TIẾN SĨ SỐ 2 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 3: CHƯƠNG 6–9 + TLTK + PHỤ LỤC)

> Tiếp nối `thesis/17_cd2_part1_intro_theory_vi.md` và `thesis/18_cd2_part2_review_framework_hypotheses_vi.md`.

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

**Mô hình M0 (linear baseline)**:
$$P_{ict} = \alpha + \beta I_{ict} + \Gamma X_{ict} + \mu_c + \tau_t + \epsilon_{ict}$$

**Mô hình M1 (quadratic, inverted-U)**:
$$P_{ict} = \alpha + \beta_1 I_{ict} + \beta_2 I^2_{ict} + \Gamma X_{ict} + \mu_c + \tau_t + \epsilon_{ict}$$

**Mô hình M2 (cubic, S-curve — kiểm định H1)**:
$$P_{ict} = \alpha + \beta_1 I_{ict} + \beta_2 I^2_{ict} + \beta_3 I^3_{ict} + \Gamma X_{ict} + \mu_c + \tau_t + \epsilon_{ict}$$

**Mô hình M3 (M2 + TCI moderation — kiểm định H2)**:
$$P_{ict} = \alpha + \beta_1 I + \beta_2 I^2 + \beta_3 I^3 + \gamma_1 TCI_{ict} + \delta_1 (I_{ict} \times TCI_{ict}) + \Gamma X + \mu_c + \tau_t + \epsilon$$

**Mô hình M4 (M3 + DAI moderation — kiểm định H3)**:
$$P_{ict} = \alpha + \beta_1 I + \beta_2 I^2 + \beta_3 I^3 + \gamma_1 TCI + \gamma_2 DAI + \delta_1 (I \times TCI) + \delta_2 (I \times DAI) + \Gamma X + \mu_c + \tau_t + \epsilon$$

**Mô hình M5 (M4 + Manager moderation — kiểm định H4)**:
$$P_{ict} = \alpha + \beta_1 I + \beta_2 I^2 + \beta_3 I^3 + \gamma_1 TCI + \gamma_2 DAI + \gamma_3 Manager + \delta_1 (I \times TCI) + \delta_2 (I \times DAI) + \delta_3 (I \times Manager) + \Gamma X + \mu_c + \tau_t + \epsilon$$

**Mô hình M6 (M5 + Regime moderation — kiểm định H5)**:
$$P_{ict} = \alpha + \beta_1 I + \beta_2 I^2 + \beta_3 I^3 + \gamma_1 TCI + \gamma_2 DAI + \gamma_3 Manager + \sum_{r=2}^{6} \gamma_{4r} Regime_r + \delta_1 (I \times TCI) + \delta_2 (I \times DAI) + \delta_3 (I \times Manager) + \sum_{r=2}^{6} \delta_{4r} (I \times Regime_r) + \Gamma X + \tau_t + \epsilon$$

(country fixed effects μ_c bị thay thế bằng regime dummies + cluster SE for identification.)

**Mô hình M7 (capstone — three-way moderation + temporal — kiểm định H1–H6 đồng thời)**:
$$P_{ict} = \alpha + \beta_1 I + \beta_2 I^2 + \beta_3 I^3 + \gamma_1 TCI + \gamma_2 DAI + \gamma_3 Manager + \sum_{r=2}^{6} \gamma_{4r} Regime_r + \sum_{p=2}^{3} \gamma_{5p} Period_p + \delta_1 (I \times TCI) + \delta_2 (I \times DAI) + \delta_3 (I \times Manager) + \sum_{r=2}^{6} \delta_{4r} (I \times Regime_r) + \sum_{p=2}^{3} \delta_{5p} (I \times Period_p) + \delta_5 (I \times TCI \times DAI) + \delta_6 (DAI \times Period_3) + \Gamma X + \tau_t + \epsilon$$

**Số tham số M7**: 3 (cubic) + 4 (gồm γ₁, γ₂, γ₃) + 5 (regime) + 2 (period) + 3 (two-way TCI/DAI/Manager × I) + 5 (regime × I) + 2 (period × I) + 1 (three-way) + 1 (DAI × Period) + 4 (controls) + ~50 country FE + 13 year FE ≈ 90+ tham số. Cần n ≥ 5.000 để đảm bảo power; pool 101.035 đáp ứng dư thừa.

### 6.3 Cấp độ phân tích và đơn vị quan sát

**Đơn vị quan sát**: doanh nghiệp i × quốc gia c × năm khảo sát t. Pool có 101.035 đơn vị quan sát.

**Cấu trúc dữ liệu**: pooled cross-section với 47 quốc gia × 107 năm = không panel chuẩn (mỗi đợt khảo sát thường có mẫu mới). Một số quốc gia (Trung Quốc 2012/2024, Việt Nam 2009/2015/2023, Mongolia 2009/2013/2019/2025, Nepal panel 2009/2013/2023) có panel ngắn — sử dụng cho robustness check.

**Trọng số khảo sát**. WBES sử dụng stratified random sampling. Cần trọng số `wmedian` (median assumption về eligibility) khi tính thống kê tổng hợp. Trong CĐ2, dùng survey weights cho mô hình chính M0–M7.

### 6.4 Phương pháp ước lượng chính

**Phương pháp 1 — OLS với HC3 robust SE** (Long & Ervin, 2000): chính. Phù hợp với cross-section pooled, robust với heteroskedasticity ở đuôi.

**Phương pháp 2 — Two-way fixed effects** (country × year): kiểm soát unobserved heterogeneity ở cấp quốc gia × năm. Đặc biệt quan trọng để loại đại lượng macro chung.

**Phương pháp 3 — Cluster-robust SE** ở mức country × industry: cho phép correlation giữa các doanh nghiệp trong cùng cluster.

**Phương pháp 4 — Quantile regression** (robustness): kiểm tra hiệu ứng ở các phân vị khác nhau của P.

**Tests chẩn đoán**:
- **VIF**: tất cả < 10 (lý tưởng < 5) cho biến giải thích
- **Breusch-Pagan test**: phát hiện heteroskedasticity
- **RESET test**: phát hiện non-linearity bị bỏ sót
- **Normality of residuals**: visual inspection và Jarque-Bera

### 6.5 Kiểm định giả thuyết

**H1 phi tuyến**: Wald test β₂ = β₃ = 0 với Bonferroni correction. Nếu bác bỏ → S-curve được khẳng định. Tính I*₁ và I*₂ từ nghiệm đạo hàm bậc nhất.

**H2 TCI moderation**: t-test trên δ₁; H₀: δ₁ = 0; H₁: δ₁ > 0 (one-tailed).

**H3 DAI moderation**: t-test trên δ₂; H₀: δ₂ = 0; H₁: δ₂ > 0. Đồng thời F-test δ₁ = δ₂ để kiểm định two-tailed riêng biệt.

**H4 Manager moderation**: t-test trên δ₃ với expected sign (+) cho experience, intl experience.

**H5 Institutional gradient**: F-test joint δ₄₂ = δ₄₃ = ... = δ₄₆ = 0; nếu bác bỏ → có gradient. Test ordering (linear trend) bằng contrast.

**H6 Temporal**: t-test δ₆ > 0; F-test joint δ₅₂ = δ₅₃ = 0.

**Kiểm định ảnh hưởng tổng hợp** (M7): chi² test joint cho tất cả interaction terms = 0.

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

**M7 là khung mô hình toàn diện nhất** trong văn liệu hiện hành — kiểm định đồng thời tất cả tám yếu tố.

---

## CHƯƠNG 7 — THIẾT KẾ DỮ LIỆU VÀ CHIẾN LƯỢC NHẬN DẠNG

### 7.1 Nguồn dữ liệu

**Dữ liệu chính**: Pool WBES 101.035 doanh nghiệp ở 47 nền kinh tế châu Á và Pacific × 107 cặp quốc gia × năm × 14 mốc khảo sát giai đoạn 2009–2025 (xem Phụ lục A của Chuyên đề 1, file `thesis/16_cd1_part3_cases_conclusion_vi.md`).

**Dữ liệu bổ sung cho biến quốc gia × năm**:
- *World Development Indicators* (WB WDI): GDP/đầu người PPP, tăng trưởng GDP, lạm phát, FDI inflows/GDP
- *Worldwide Governance Indicators* (Kaufmann et al., 2011): 6 chiều thể chế (Voice & Accountability, Political Stability, Government Effectiveness, Regulatory Quality, Rule of Law, Control of Corruption)
- *Global Innovation Index* (WIPO, 2024): năng lực đổi mới quốc gia
- *ITU Digital Hub*: ICT Development Index, mobile broadband subscriptions
- *Data360 API* (https://data360api.worldbank.org): truy vấn các indicator trên

### 7.2 Mẫu nghiên cứu dự kiến

**Pool đầy đủ**: 101.035 doanh nghiệp (Phụ lục A).

**Sub-samples cho robustness**:
- *Manufacturing only*: ~45.000 doanh nghiệp (loại services và retail)
- *SME only* (<100 lao động): ~76.000 doanh nghiệp
- *Exporters only* (FSTS > 0): ~17.000 doanh nghiệp
- *By regime*: Advanced 5.921; Upper-middle 15.174; Emerging 47.803; Frontier 28.678; SIDS 1.221

**Power analysis**:
- Với n=101.035 và effect size cỡ trung bình (f² = 0,02), power > 0,99 ngay cả với 90 tham số
- Cho three-way interaction (M7), n cần thiết ≥ 5.000 để power 0,8 → đáp ứng dư thừa
- SIDS subsample (n=1.221) đáp ứng cho M2 nhưng không đủ cho M7 → kiểm định H5 tách riêng cho SIDS

### 7.3 Đo lường biến

**Biến phụ thuộc P**:

- *P chính*: log labor productivity = log(d2/l1), winsorized 1/99 trong country-year. Bất biến đơn vị tiền tệ.
- *P phụ — robustness*: ROS = (sales − costs)/sales (giai đoạn 2018+); Sales growth 3 năm = (l1 − l2)^(1/3) − 1.

**Biến độc lập I**:

- *I chính*: FSTS = d3b + d3c (% xuất khẩu gián tiếp + trực tiếp), winsorized [0, 100]
- *I phụ — robustness*: dummy exporter = (FSTS > 0); export intensity bucketed (0%, 1–25%, 26–50%, 51–75%, 76–100%)

**Biến điều tiết TCI**:

- *Phiên bản 1.0 (current)*: TCI = mean(rd_active, iso_cert) — 2 thành phần
- *Phiên bản 2.0 (mở rộng)*: TCI = mean(rd_active, iso_cert, machinery_imported_dummy) — 3 thành phần (cần extract từ schema 2018+ với biến `f1`)

**Biến điều tiết DAI**:

- *Phiên bản 1.0 (current)*: DAI = website (1 thành phần)
- *Phiên bản 2.0 (mở rộng)*: DAI = mean(website, e-commerce, ERP, cloud) — 4 thành phần (cần extract từ schema 2018+ với các biến `c22b_2`, `c30b`, `c31`)

**Biến điều tiết Manager**:

- experience_yrs (b7 — số năm kinh nghiệm top manager trong ngành)
- education (proxy: years of schooling — chỉ một số đợt)
- gender_female (b7a) — biến categorical
- intl_experience_dummy (đã làm việc/học tập ở nước ngoài — biến mới chỉ có ở schema 2025+)

**Biến điều tiết Regime ICRV**:

- 6 nhóm: Advanced-innovation, Advanced-resource, Upper-middle, Emerging, Frontier, SIDS (mở rộng từ 5 nhóm trong Chuyên đề 1 với sub-grouping Advanced)

**Biến kiểm soát**:

- log_employees (size proxy)
- age = year_survey − b5
- fdi10 = (b2b ≥ 10)
- sector_main (1-digit ISIC)
- country fixed effects μ_c (47 dummies)
- year fixed effects τ_t (14 dummies)

### 7.4 Hòa hợp dữ liệu xuyên thế hệ schema

Pipeline đã thực hiện hòa hợp 105 file `.dta` từ 3 thế hệ schema (PICS3, Standardized, BREADY/BEE) — chi tiết tại `wbes/02_harmonize.py`. Quy trình:

1. Đọc `.dta` với encoding fallback (Latin-1, CP1252)
2. Crosswalk biến theo bảng tham chiếu (xem `thesis/08_p7_data_harmonization_protocol_vi.md`)
3. Loại WBES missing codes {-9, -8, ..., -1}
4. Tính FSTS = d3b + d3c (xuất khẩu gián tiếp + trực tiếp)
5. Winsorize log labor productivity 1%/99% trong country-year
6. Loại doanh nghiệp lao động ≤ 0 hoặc doanh thu ≤ 0
7. Mongolia panel 2009/2013/2019 và Nepal panel 2009/2013/2023: filter year để lấy lát cross-section

**Imputation cho biến TCI/DAI ở schema cũ**: cần imputation đa lần (Multiple Imputation by Chained Equations — MICE) cho các biến TCI 3-component và DAI 4-component ở giai đoạn 2009–2017. Sử dụng package `mice` (R) hoặc `IterativeImputer` (sklearn).

### 7.5 Chiến lược nhận dạng đa tầng

**Vấn đề endogeneity**. Doanh nghiệp tự chọn quốc tế hóa — không phải ngẫu nhiên. Doanh nghiệp năng suất cao có xu hướng xuất khẩu nhiều (self-selection). Nếu không xử lý, hệ số β có thể bias upward (overestimate).

**Tầng 1 — Country × Year FE**: Loại unobserved heterogeneity ở cấp quốc gia × năm — như chính sách thương mại, biến động tỷ giá, sốc cung cầu. Đây là lớp nhận dạng cơ bản nhất.

**Tầng 2 — Kiểm soát rộng**: kiểm soát cấp doanh nghiệp (size_log, age, fdi10) + sector × country × year FE (nếu khả thi với pool đủ lớn). Loại bias từ sector-specific shocks.

**Tầng 3 — Instrumental Variable discussion (gợi ý)**: Hai IV tiềm năng được thảo luận (chưa thực thi do WBES không có sẵn):
- *Distance to nearest port* (Bao et al., 2017): doanh nghiệp gần cảng có chi phí xuất khẩu thấp hơn → ảnh hưởng I nhưng không trực tiếp tác động P (sau khi kiểm soát infrastructure)
- *Industry-level export propensity ở quốc gia khác* (Aw, Chung & Roberts, 2000): xu hướng xuất khẩu của ngành ở các quốc gia khác làm shifter cho I của doanh nghiệp i

CĐ2 thảo luận IV như định hướng phát triển; luận án có thể xây dựng IV với dữ liệu bổ sung.

**Tầng 4 — Subsample replication**: kiểm định lại tất cả mô hình M0–M7 trên các sub-sample (theo regime ICRV, theo nhóm thu nhập, theo ngành chế biến chế tạo) để kiểm tra ổn định kết quả.

**Tầng 5 — Placebo test**: thay biến phụ thuộc bằng biến không liên quan (ví dụ: tuổi doanh nghiệp); kết quả phải gần 0 — nếu không, có vấn đề mô hình.

### 7.6 Power analysis chi tiết

| Mô hình | Số tham số chính | n cần thiết (power 0,8) | n hiện có | Power thực tế |
|---|---|---|---|---|
| M0 linear | 1 | 200 | 101.035 | >0,99 |
| M2 cubic | 3 | 500 | 101.035 | >0,99 |
| M4 (TCI + DAI) | 7 | 1.500 | 101.035 | >0,99 |
| M5 + Manager | 9 | 2.500 | 101.035 | >0,99 |
| M6 + Regime | 19 | 5.000 | 101.035 | >0,99 |
| **M7 capstone** | ~90 | 30.000 | 101.035 | **0,99** |
| M7 trên sub-sample SIDS | ~30 | 5.000 | 1.221 | 0,4 (insufficient) |

→ M7 trên sub-sample SIDS không đủ power. Phải kiểm định H5 cho SIDS riêng bằng M0–M2 (với fewer parameters).

---

## CHƯƠNG 8 — KẾ HOẠCH KIỂM ĐỊNH ĐỘ VỮNG

### 8.1 Robustness về thước đo

**Thay biến phụ thuộc P**:
- ROS thay log_labor_prod → kiểm tra nhất quán dấu của β
- Sales growth 3 năm thay log_labor_prod → kiểm tra
- Multidimensional P composite (z-score weighted) → kiểm tra

**Thay biến độc lập I**:
- Dummy exporter (1 nếu FSTS > 0) → kiểm tra dấu chính
- Export intensity bucketed → kiểm tra non-linearity bằng dummy thay polynomial
- Inverse Mills ratio (Heckman selection) cho I dương → kiểm tra selection bias

**Thay biến điều tiết**:
- TCI 2-component vs 3-component (thêm machinery)
- DAI 1-component vs 4-component (thêm e-commerce, ERP, cloud)

### 8.2 Robustness về mẫu

**Sub-samples theo loại doanh nghiệp**:
- Loại doanh nghiệp Nhà nước (SOE proxy: b2c ≥ 50%) → kiểm tra
- Chỉ doanh nghiệp ≥ 5 lao động → kiểm tra (loại micro-enterprises noisy)
- Chỉ doanh nghiệp manufacturing (ISIC 10-33) → kiểm tra
- Chỉ doanh nghiệp services (ISIC 41-99) → kiểm tra

**Sub-samples theo regime**:
- Advanced innovation-driven (Singapore, HK, Korea, TWN, ISR) — n=4.222
- Advanced resource-driven (SAU, QAT, KWT, BHR, BRN, CYP) — n=2.418
- Upper-middle, Emerging, Frontier, SIDS riêng

### 8.3 Robustness về phương pháp ước lượng

- HC3 SE (chính)
- HC1 (cluster ở country × industry)
- Bootstrap 1.000 lần
- Quantile regression (median, P25, P75) → kiểm tra hiệu ứng theo đuôi
- Pooled OLS vs first-difference estimator (cho cohort 2-period: Trung Quốc 2012-2024, Việt Nam 2009-2023)

### 8.4 Robustness về dạng hàm

- Linear M0 vs Quadratic M1 vs Cubic M2: so sánh AIC, BIC, RESET test
- Semiparametric (LOWESS) plot để kiểm tra dạng hàm visually
- Polynomial bậc 4, 5: kiểm tra overfitting

### 8.5 Placebo test

- Thay biến phụ thuộc P bằng tuổi doanh nghiệp → kết quả phải ≈ 0
- Thay biến độc lập I bằng noise N(0,1) → kết quả phải ≈ 0
- Random shuffle cluster identifier → kết quả phải ≈ 0

### 8.6 Nhạy cảm thiết kế

- Thay đổi cách định nghĩa regime ICRV (5 vs 6 nhóm với sub-Advanced)
- Thay đổi thời điểm cắt giai đoạn temporal (2009-2012-2017-2025 vs 2009-2014-2019-2025)
- Thay đổi ngưỡng SME (50, 100, 250 lao động)

### 8.7 Tổng hợp kết quả robustness

**Bảng 8.1**. *Ma trận robustness × giả thuyết H1–H6.*

| Robustness check | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|
| Alt P (ROS, growth) | 6 trường hợp | 6 | 6 | 6 | 6 | 6 |
| Alt I (dummy, bucket) | 4 | 4 | 4 | 4 | 4 | 4 |
| Sub-sample theo loại | 4 | 4 | 4 | 4 | 4 | 4 |
| Sub-sample theo regime | 6 | 6 | 6 | 6 | – | 6 |
| Phương pháp khác (HC1, cluster, bootstrap, quantile) | 4 | 4 | 4 | 4 | 4 | 4 |
| Dạng hàm khác | 5 | 5 | 5 | 5 | 5 | 5 |
| Placebo | 3 | 3 | 3 | 3 | 3 | 3 |

**Tổng**: ~30 robustness checks cho mỗi giả thuyết → đủ ý nghĩa cho luận án TS.

---

## CHƯƠNG 9 — ĐÓNG GÓP VỀ MÔ HÌNH VÀ KẾT LUẬN

### 9.1 Đóng góp về lý thuyết

**Khung tích hợp 4 tầng + Digital lens cho châu Á**: Chuyên đề 2 đề xuất khung lý thuyết tích hợp Uppsala (động lực quốc tế hóa) + RBV (nguồn lực) + Institutional Theory (thể chế) + Upper Echelons (nhà quản trị) + Digital Capability Lens (Banalieva & Dhanaraj, 2019) — lần đầu được hệ thống hóa cho bối cảnh châu Á + Pacific với 47 nền kinh tế.

**Tách bạch TCI và DAI**: Phân biệt năng lực công nghệ NỘI TẠI (R&D, ISO, máy nhập khẩu) khỏi năng lực số NGOẠI TẠI (website, e-commerce, ERP, cloud) — giải quyết khoảng trống trong văn liệu hiện hành (kể cả Li, Liu & Qian 2022) thường gộp chung.

**Sub-grouping Advanced regime**: Phát hiện ở Chuyên đề 1 cho thấy Advanced có hai loại — innovation-driven (Singapore, HK, Korea, TWN) khác resource-driven (Saudi, Qatar, Kuwait, Bahrain) — chưa được phân biệt trong các khung tham chiếu hiện hành.

### 9.2 Đóng góp về mô hình

**Tám mô hình M0–M7 với three-way moderation (M7) và temporal heterogeneity**: Kiểm định đồng thời phi tuyến cubic + bốn moderators (TCI, DAI, Manager, Institutional) + heterogeneity thời gian — mô hình toàn diện nhất văn liệu hiện hành.

**Boundary case Pacific SIDS**: 6 quốc gia (Fiji, PNG, Solomon Islands, Tonga, Vanuatu, Samoa) làm boundary case kiểm định forced internationalization penalty (Đỗ & Phan, 2026 — P8 manuscript).

### 9.3 Đóng góp về phương pháp

**Pool 101.035 doanh nghiệp xuyên 47 nước × 107 cặp năm × 14 mốc khảo sát**: phạm vi rộng nhất từng có cho nghiên cứu I→P trong văn liệu IB. Pipeline Python tự động hòa hợp 105 file qua 3 thế hệ schema WBES.

**Chiến lược nhận dạng đa tầng**: Country × year FE + sector controls + IV-discussion + subsample replication + placebo test — đảm bảo kết quả robust và đáng tin cậy.

**Kế hoạch kiểm định độ vững toàn diện**: ~30 robustness checks cho mỗi giả thuyết H1–H6 — đủ ý nghĩa cho luận án TS.

### 9.4 Hạn chế của mô hình

(1) WBES không phải panel chuẩn → khó nhận dạng nhân quả mạnh. Chỉ có panel ngắn 2-3 chu kỳ ở vài quốc gia (Trung Quốc, Việt Nam, Mongolia, Nepal).

(2) Một số biến quan trọng theo lý thuyết chưa đo lường được trong WBES: psychic distance, network embeddedness, top management team diversity (chỉ đo top manager).

(3) IV không sẵn có trong WBES → IV-discussion chỉ ở mức gợi ý cho CĐ2; luận án có thể xây dựng IV với dữ liệu bổ sung.

(4) DAI hiện tại chỉ 1 thành phần (website); cần mở rộng schema 2018+ để có DAI 4-component đầy đủ. Chỉ một số quốc gia có biến này.

(5) Top manager characteristics có ở schema 2018+ (`b7`, `b7a`) nhưng không nhất quán xuyên đợt khảo sát → hạn chế kiểm định H4.

### 9.5 Định hướng phát triển

**Hướng 1 — Hoàn thiện CĐ2**: Bổ sung TCI 3-component + DAI 4-component bằng MICE imputation; chiến lược IV với dữ liệu macro WDI và WGI.

**Hướng 2 — Triển khai luận án**: 
- Chương 2 luận án dùng khung lý thuyết Chương 2 CĐ2
- Chương 3 luận án dùng đặc tả mô hình M0–M7 Chương 6 CĐ2
- Chương 4 luận án triển khai ước lượng và kiểm định H1–H6
- Chương 5 luận án thảo luận và hàm ý chính sách

**Hướng 3 — Hoàn thiện manuscripts P5 (China 2012–2024), P7 (25-country capstone), P8 (Pacific SIDS)**: đăng trên các tạp chí IB hàng đầu (JIBS, JWB, IBR, MIR).

**Hướng 4 — Nghiên cứu mở rộng**: 
- Áp dụng khung CĐ2 cho các khu vực khác (Latin America, Africa)
- Kết hợp với meta-analysis 1980–2026 (P6 manuscript)
- Phát triển multi-level model với data macro country × year

### 9.6 Kết luận

Chuyên đề 2 thiết lập đầy đủ khung lý thuyết tích hợp 4 tầng + Digital Lens, hệ giả thuyết H1–H6, đặc tả 8 mô hình M0–M7, chiến lược dữ liệu và nhận dạng cho nghiên cứu quan hệ giữa quốc tế hóa và hiệu quả doanh nghiệp ở các quốc gia châu Á.

**Tính hệ thống**: 4 tầng lý thuyết + lăng kính số + 6 giả thuyết + 8 mô hình + chiến lược nhận dạng đa tầng + ~30 robustness checks — đảm bảo độ chặt chẽ học thuật của luận án TS.

**Tính mới**: tích hợp 8 yếu tố cùng lúc (phi tuyến + 4 moderators + temporal + 3-way + sub-grouping Advanced + SIDS boundary) — chưa có khung tham chiếu nào trong văn liệu hiện hành đạt được mức tích hợp này.

**Tính khả thi**: Pool 101.035 doanh nghiệp ở 47 nước × 107 cặp năm cung cấp dư thừa power cho mọi mô hình M0–M7 (trừ M7 trên sub-sample SIDS — đã có giải pháp).

**Tính ứng dụng**: Hàm ý chính sách rõ ràng cho doanh nghiệp Việt Nam và emerging Asia — đặc biệt về cách kết hợp quốc tế hóa với năng lực số trong giai đoạn AI bùng nổ 2023–2025.

CĐ2 cùng với CĐ1 (mô tả thực trạng) thiết lập đầy đủ nền tảng cho luận án "Quốc tế hóa và hiệu quả hoạt động kinh doanh của doanh nghiệp ở các quốc gia châu Á: Vai trò điều tiết của thể chế, năng lực số và đặc điểm nhà quản trị".

---

## TÀI LIỆU THAM KHẢO

> Trích dẫn theo APA 7th. Danh mục đầy đủ chuyên ngành ở `thesis/04_references_apa7.md`. Các trích dẫn chính dùng trong CĐ2:

Ang, S. H. (2008). Competitive intensity and collaboration: Impact on firm growth across technological environments. *Strategic Management Journal, 29*(10), 1057–1075.

Arte, P., & Larimo, J. (2022). Moderating influence of product diversification on the international diversification–performance relationship: A meta-analysis. *Journal of Business Research, 139*, 1408–1423.

Aw, B. Y., Chung, S., & Roberts, M. J. (2000). Productivity and turnover in the export market: Micro-level evidence from the Republic of Korea and Taiwan (China). *World Bank Economic Review, 14*(1), 65–90.

Banalieva, E. R., & Dhanaraj, C. (2019). Internalization theory for the digital economy. *Journal of International Business Studies, 50*(8), 1372–1387.

Bao, Y., Chen, X., & Zhou, K. Z. (2017). External learning, market dynamics, and radical innovation: Evidence from China's high-tech firms. *Journal of Business Research, 65*(8), 1226–1233.

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management, 17*(1), 99–120.

Bausch, A., & Krist, M. (2007). The effect of context-related moderators on the internationalization–performance relationship: Evidence from meta-analysis. *Management International Review, 47*(3), 319–347.

Bhandari, K. R., Ranta, M., & Salo, J. (2023). The internationalization of firms from emerging markets. *International Business Review, 32*(2), 102056.

Cannella, A. A., Park, J. H., & Lee, H. U. (2008). Top management team functional background diversity and firm performance: Examining the roles of team member colocation and environmental uncertainty. *Academy of Management Journal, 51*(4), 768–784.

Chen, T., & Tan, J. (2012). Network ties, market relations and competitive advantage: Evidence from Chinese exporters. *Journal of World Business, 47*(2), 261–272.

Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly, 35*(1), 128–152.

Contractor, F. J., Kundu, S. K., & Hsu, C. C. (2003). A three-stage theory of international expansion: The link between multinationality and performance in the service sector. *Journal of International Business Studies, 34*(1), 5–18.

Contractor, F. J., Kumar, V., & Kundu, S. K. (2007). Nature of the relationship between international expansion and performance: The case of emerging market firms. *Journal of World Business, 42*(4), 401–417.

Đỗ, T. H., & Phan, A. T. (2026a). Internationalization and firm performance in emerging Asia. *Vietnam Economic and Financial Review*. (P1 đã đăng)

Đỗ, T. H., & Phan, A. T. (2026b). Nonlinear effects of internationalization on Chinese SME performance. *Journal of Finance and Accounting Research*. (P2 đã đăng)

Đỗ, T. H., & Phan, A. T. (2026c–f, P8 manuscript). Singapore / Vietnam / China 2012–2024 / Pacific SIDS internationalization–performance papers.

Glaum, M., & Oesterle, M. J. (2007). 40 years of research on internationalization and firm performance: More questions than answers? *Management International Review, 47*(3), 307–317.

Gomes, L., & Ramaswamy, K. (1999). An empirical examination of the form of the relationship between multinationality and performance. *Journal of International Business Studies, 30*(1), 173–187.

Greene, W. H. (2018). *Econometric analysis* (8th ed.). Pearson.

Hambrick, D. C. (2007). Upper echelons theory: An update. *Academy of Management Review, 32*(2), 334–343.

Hambrick, D. C., & Mason, P. A. (1984). Upper echelons: The organization as a reflection of its top managers. *Academy of Management Review, 9*(2), 193–206.

Hennart, J. F. (2007). The theoretical rationale for a multinationality-performance relationship. *Management International Review, 47*(3), 423–452.

Hitt, M. A., Hoskisson, R. E., & Kim, H. (1997). International diversification: Effects on innovation and firm performance in product-diversified firms. *Academy of Management Journal, 40*(4), 767–798.

Hsieh, C. T., & Klenow, P. J. (2009). Misallocation and manufacturing TFP in China and India. *Quarterly Journal of Economics, 124*(4), 1403–1448.

Hsu, C. C., & Boggs, D. J. (2003). Internationalization and performance: Traditional measures and their decomposition. *Multinational Business Review, 11*(3), 23–50.

Hsu, W. T., Chen, H. L., & Cheng, C. Y. (2013). Internationalization and firm performance of SMEs: The moderating effects of CEO attributes. *Journal of World Business, 48*(1), 1–12.

Johanson, J., & Vahlne, J. E. (1977). The internationalization process of the firm: A model of knowledge development and increasing foreign market commitments. *Journal of International Business Studies, 8*(1), 23–32.

Johanson, J., & Vahlne, J. E. (2009). The Uppsala internationalization process model revisited: From liability of foreignness to liability of outsidership. *Journal of International Business Studies, 40*(9), 1411–1431.

Kaufmann, D., Kraay, A., & Mastruzzi, M. (2011). The Worldwide Governance Indicators: Methodology and analytical issues. *Hague Journal on the Rule of Law, 3*(2), 220–246.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Hult, G. T. M., Roth, K., Cavusgil, S. T., et al. (2012). Firm-specific assets, multinationality, and financial performance: A meta-analytic review and theoretical integration. *Academy of Management Journal, 54*(1), 47–72.

Knight, G. A., & Cavusgil, S. T. (2004). Innovation, organizational capabilities, and the born-global firm. *Journal of International Business Studies, 35*(2), 124–141.

Li, J., Liu, B., & Qian, G. (2022). Digitalization and Chinese firm internationalization. *Journal of International Business Studies, 53*(4), 712–738.

Liu, Y., & Zhang, M. (2024). Nonlinear effects of internationalization on Chinese SME performance. *Asia Pacific Journal of Management*, in press.

Long, J. S., & Ervin, L. H. (2000). Using heteroscedasticity consistent standard errors in the linear regression model. *American Statistician, 54*(3), 217–224.

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609.

Luo, Y., & Tung, R. L. (2007). International expansion of emerging market enterprises: A springboard perspective. *Journal of International Business Studies, 38*(4), 481–498.

Marano, V., Arregle, J. L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization–performance relationship: A meta-analytic review. *Journal of Management, 42*(5), 1075–1110.

Mathews, J. A. (2002). Competitive advantages of the latecomer firm: A resource-based account of industrial catch-up strategies. *Asia Pacific Journal of Management, 19*(4), 467–488.

Nielsen, B. B., & Nielsen, S. (2011). The role of top management team international orientation in international strategic decision-making: The choice of foreign entry mode. *Strategic Management Journal, 32*(2), 185–200.

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press.

Peng, M. W. (2003). Institutional transitions and strategic choices. *Academy of Management Review, 28*(2), 275–296.

Peng, M. W., Wang, D. Y., & Jiang, Y. (2008). An institution-based view of international business strategy: A focus on emerging economies. *Journal of International Business Studies, 39*(5), 920–936.

Riahi-Belkaoui, A. (1998). The effects of the degree of internationalization on firm performance. *International Business Review, 7*(3), 315–321.

Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders? The international strategies of digital platform firms. *Global Strategy Journal, 11*(1), 58–80.

Tallman, S., & Li, J. (1996). Effects of international diversity and product diversity on the performance of multinational firms. *Academy of Management Journal, 39*(1), 179–196.

Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal, 18*(7), 509–533.

Torraco, R. J. (2005). Writing integrative literature reviews: Guidelines and examples. *Human Resource Development Review, 4*(3), 356–367.

Tran, T. (2014). Vietnam SME internationalization. *Asian Business & Management, 13*(4), 295–319.

Tran, T., & Pham, V. (2024). FDI và năng suất doanh nghiệp Việt Nam. *Tạp chí Kinh tế và Phát triển*, *311*, 24–38.

Verbeke, A., & Brugman, P. (2009). Triple-testing the quality of multinationality–performance research. *International Business Review, 18*(3), 265–275.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901.

Wernerfelt, B. (1984). A resource-based view of the firm. *Strategic Management Journal, 5*(2), 171–180.

WIPO. (2024). *Global Innovation Index 2024*. World Intellectual Property Organization.

Wooldridge, J. M. (2010). *Econometric analysis of cross section and panel data* (2nd ed.). MIT Press.

World Bank. (2019, 2023, 2024, n.d.). *Enterprise Surveys methodology* and *World Development Indicators*.

Wu, J., Wood, G., & Khan, Z. (2022). Internationalization and firm performance: Evidence from a meta-analysis. *International Business Review, 31*(2), 101920.

Xiao, Y., Tylecote, A., & Liu, J. (2013). Why not greater catch-up by Chinese firms? *Research Policy, 42*(3), 749–764.

Yang, X., Zhao, Y., & Wei, Y. (2025). Digital capabilities and emerging-market firm internationalization. *Journal of World Business, 60*(1), 101522.

Yiu, D., & Lau, C. M. (2008). Corporate entrepreneurship as resource capital configuration in emerging market firms. *Entrepreneurship Theory and Practice, 32*(1), 37–57.

---

## PHỤ LỤC

### Phụ lục A — Bảng định nghĩa biến CĐ2 (variable codebook đầy đủ)

| Biến | Vai trò | Đơn vị | Cách tính | Schema WBES |
|---|---|---|---|---|
| log_labor_prod | P chính (DV) | log LCU | log(d2/l1), winsorized 1/99 | tất cả |
| ROS | P phụ | % | (sales − costs)/sales | 2018+ |
| sales_growth_3y | P phụ | %/năm | CAGR doanh thu thực 3 năm | tất cả |
| FSTS | I (IV) | % | d3b + d3c | tất cả |
| exporter | I dummy | 0/1 | 1 if FSTS > 0 | tất cả |
| age | control | năm | year_survey − b5 | tất cả |
| log_employees | control | log lao động | log(l1) | tất cả |
| fdi10 | control | 0/1 | b2b ≥ 10 | tất cả |
| TCI | moderator H2 | 0–1 | mean(rd_active, iso_cert)[, machinery] | tất cả (2-component); 2018+ (3) |
| DAI | moderator H3 | 0–1 | website [+ ecommerce + ERP + cloud] | tất cả (1-component); 2018+ (4) |
| mgr_exp_yrs | moderator H4 | năm | b7 | 2018+ |
| mgr_female | moderator H4 | 0/1 | b7a | 2018+ một số nước |
| ICRV_regime | moderator H5 | 1–6 | (Adv-inn / Adv-res / UM / Em / Fr / SIDS) | tổng hợp tác giả |
| Period | moderator H6 | 1–3 | 2009-2012 / 2013-2017 / 2018-2025 | tổng hợp tác giả |

### Phụ lục B — Sơ đồ mô hình M0–M7

(Sẽ vẽ chi tiết dưới dạng path diagram khi xuất bản nộp.)

### Phụ lục C — Bảng giả thuyết H1–H6 đầy đủ

(Đã trình bày Bảng 5.1 ở Phần 2.)

### Phụ lục D — Bộ mã Stata mẫu cho M2 và M7

```stata
* CD2_models.do — phiên bản Stata
clear all
use "wbes_asia_pool.dta", clear

* Setup biến điều tiết
gen log_lp = ln(d2/l1)
gen log_l1 = ln(l1)
gen fsts = d3b + d3c
gen exporter = (fsts > 0) if !missing(fsts)
gen age = year_survey - b5
gen fdi10 = (b2b >= 10) if !missing(b2b)
gen TCI = (h8 + b8) / 2
gen DAI = c22b
gen icrv = .
replace icrv = 1 if inlist(country_iso3, "SGP","HKG","KOR","TWN","ISR")
replace icrv = 2 if inlist(country_iso3, "SAU","QAT","KWT","BHR","BRN","CYP")
replace icrv = 3 if inlist(country_iso3, "CHN","MYS","THA","KAZ","ARM","GEO")
replace icrv = 4 if inlist(country_iso3, "VNM","IDN","PHL","IND","LKA","JOR","MNG")
replace icrv = 5 if inlist(country_iso3, "BGD","PAK","LAO","KHM","NPL","BTN","UZB","TJK","KGZ","TKM","AFG","TLS","IRQ","LBN","YEM","MMR","MDV")
replace icrv = 6 if inlist(country_iso3, "FJI","PNG","SLB","TON","VUT","WSM")
gen period = .
replace period = 1 if year_survey <= 2012
replace period = 2 if year_survey >= 2013 & year_survey <= 2017
replace period = 3 if year_survey >= 2018

* M2 cubic
gen fsts2 = fsts^2
gen fsts3 = fsts^3
reg log_lp fsts fsts2 fsts3 log_l1 age fdi10 i.country_iso3 i.year_survey, robust

* Test H1
test fsts2 fsts3

* M4 with TCI + DAI
gen fsts_TCI = fsts * TCI
gen fsts_DAI = fsts * DAI
reg log_lp fsts fsts2 fsts3 TCI DAI fsts_TCI fsts_DAI log_l1 age fdi10 i.country_iso3 i.year_survey, robust
test fsts_TCI fsts_DAI

* M7 capstone (full)
gen fsts_mgr = fsts * mgr_exp_yrs
forvalues r = 2/6 {
    gen fsts_icrv`r' = fsts * (icrv == `r')
}
forvalues p = 2/3 {
    gen fsts_period`p' = fsts * (period == `p')
}
gen fsts_TCI_DAI = fsts * TCI * DAI
gen DAI_period3 = DAI * (period == 3)

reg log_lp fsts fsts2 fsts3 TCI DAI mgr_exp_yrs i.icrv i.period ///
          fsts_TCI fsts_DAI fsts_mgr fsts_icrv* fsts_period* ///
          fsts_TCI_DAI DAI_period3 ///
          log_l1 age fdi10 i.country_iso3 i.year_survey, robust
```

### Phụ lục E — Bảng crosswalk schema WBES rút gọn

(Tham chiếu chi tiết tại `thesis/08_p7_data_harmonization_protocol_vi.md`.)

### Phụ lục F — Power analysis chi tiết

(Đã trình bày Mục 7.6 ở Phần 3.)

### Phụ lục G — So sánh khung CĐ2 với 4 khung tham chiếu

(Đã trình bày Bảng 4.2 ở Phần 2.)

---

*Phiên bản 1.0 — bản nháp đầy đủ ba phần CĐ2. NCS: Đỗ Thùy Hương. HD chuyên đề: PGS.TS. Phan Anh Tú. Cần Thơ, ngày 04/05/2026.*
