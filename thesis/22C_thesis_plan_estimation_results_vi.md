# KẾ HOẠCH LUẬN ÁN — PHẦN 2C: ESTIMATION + ROBUSTNESS + CHƯƠNG 4 KẾT QUẢ

> Tiếp nối `thesis/22B_thesis_plan_variables_vi.md`.
> Phần 2D (Discussion + Status + References): `thesis/22D_thesis_plan_discussion_status_refs_vi.md`.

---

## 3.4 CHIẾN LƯỢC ƯỚC LƯỢNG VÀ NHẬN DẠNG

### 3.4.1 Tám mô hình M0–M7 — chuỗi tăng dần độ phức tạp

**Bảng 3.2**. *Chuỗi đặc tả tám mô hình M0–M7.*

| Mô hình | Đặc tả rút gọn | Giả thuyết kiểm định | Số tham số chính |
|---|---|---|---|
| **M0** | $P = \alpha + \beta I + \Gamma X + \mu_c + \tau_t + \varepsilon$ | Linear baseline | 1 |
| **M1** | M0 + $\beta_2 I^2$ | H1 partial (inverted-U) | 2 |
| **M2** | M1 + $\beta_3 I^3$ | **H1 full (S-curve cubic)** | 3 |
| **M3** | M2 + $\gamma_1 \text{TCI} + \delta_1 (I \times \text{TCI})$ | + **H2 TCI moderation** | 5 |
| **M4** | M3 + $\gamma_2 \text{DAI} + \delta_2 (I \times \text{DAI})$ | + **H3 DAI moderation riêng biệt** | 7 |
| **M5** | M4 + $\gamma_3 \text{Manager} + \delta_3 (I \times \text{Manager})$ | + **H4 Manager moderation** | 9 |
| **M6** | M5 + $\gamma_4 \text{Regime}_r + \delta_4 (I \times \text{Regime}_r)$ | + **H5 Institutional gradient** | 19 |
| **M7** | M6 + $\delta_5 (I \times \text{TCI} \times \text{DAI}) + \delta_6 (\text{DAI} \times \text{Period}_3)$ | + **H6 + 3-way capstone** | ~30 |

> Plus: country FE (47), year FE (14), sector FE (1-digit ISIC) — tổng cộng ~90 tham số ở M7.

### 3.4.2 Phương pháp ước lượng chính

**OLS với HC1 robust SE** (Long & Ervin, 2000):
$$
\hat{\boldsymbol{\beta}}_{OLS} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{y}, \quad \widehat{\text{Var}}(\hat{\boldsymbol{\beta}}) = (\mathbf{X}'\mathbf{X})^{-1} \mathbf{X}'\hat{\boldsymbol{\Omega}}\mathbf{X} (\mathbf{X}'\mathbf{X})^{-1}
$$

trong đó $\hat{\boldsymbol{\Omega}}$ là HC1 với hiệu chỉnh degree-of-freedom (Long & Ervin, 2000). Đây là phương pháp chính trong P3 (Singapore) và P4 (Việt Nam) của Đỗ và Phan (2026).

**Cluster-robust SE ở mức country × industry**:
$$
\widehat{\text{Var}}_{cluster}(\hat{\boldsymbol{\beta}}) = (\mathbf{X}'\mathbf{X})^{-1} \left(\sum_{g=1}^{G} \mathbf{X}_g'\hat{\boldsymbol{\varepsilon}}_g\hat{\boldsymbol{\varepsilon}}_g'\mathbf{X}_g\right) (\mathbf{X}'\mathbf{X})^{-1}
$$

trong đó $g$ là cluster (country × industry). Phù hợp với Cameron và Miller (2015) cho dữ liệu có structure phân tầng.

**Two-way fixed effects** (country × year): kiểm soát unobserved heterogeneity ở cấp quốc gia × năm — đặc biệt quan trọng để loại đại lượng macro chung như tỷ giá, chính sách thương mại, sốc cung cầu (Wooldridge, 2010).

**Survey weights** `wmedian`: áp dụng cho M0–M5 (descriptive); với M6–M7 (capstone đa tầng) báo cáo cả weighted và unweighted theo Solon, Haider và Wooldridge (2015).

### 3.4.3 Chiến lược nhận dạng đa tầng

Vấn đề chính: **endogeneity của FSTS** — doanh nghiệp năng suất cao có xu hướng xuất khẩu nhiều (self-selection, Bernard & Jensen, 1999; Melitz, 2003). Nếu không xử lý, β₁ trong các phương trình sẽ bias upward. Luận án áp dụng năm tầng nhận dạng:

**Tầng 1 — Country × Year FE**. Loại unobserved heterogeneity ở cấp quốc gia × năm (chính sách thương mại, biến động tỷ giá, sốc địa chính trị). Phương pháp chính của P3, P4.

**Tầng 2 — Sector × Country × Year FE** (cho subset có đủ data). Kiểm soát thêm sector-specific shocks. Điều kiện: số doanh nghiệp trong mỗi cell ≥ 30 (Wooldridge, 2010).

**Tầng 3 — Heckman two-step selection correction** (Heckman, 1979). Selection equation:
$$
P(\text{Exporter}_{ict} = 1) = \Phi(\mathbf{Z}_{ict} \boldsymbol{\xi})
$$

với $\mathbf{Z}_{ict}$ chứa exclusion restriction *distance to nearest international port* (Bao, Chen & Zhou, 2017) — biến ảnh hưởng decision to export nhưng không trực tiếp tác động P sau khi kiểm soát infrastructure. Inverse Mills Ratio:
$$
\lambda_{ict} = \frac{\phi(\mathbf{Z}_{ict} \boldsymbol{\xi})}{\Phi(\mathbf{Z}_{ict} \boldsymbol{\xi})}
$$

được thêm vào outcome equation để correct selection bias. Phương pháp được sử dụng trong P4 (Đỗ & Phan, 2026 — Việt Nam manuscript).

**Tầng 4 — Control function approach**. Specification:
$$
\hat{e}_{ict} = \text{FSTS}_{ict} - \mathbf{Z}_{ict} \hat{\boldsymbol{\xi}}
$$

residual từ first-stage được thêm vào outcome equation — phù hợp với cubic specification (Wooldridge, 2015). Robustness cho Heckman.

**Tầng 5 — Subsample replication**. Kiểm định lại tất cả M0–M7 trên các sub-sample:
- Theo regime ICRV (6 nhóm)
- Theo nhóm thu nhập (Advanced/Upper/Emerging/Frontier)
- Theo ngành (manufacturing vs services)
- Theo giai đoạn thời gian (3 periods)

Nếu kết quả ổn định xuyên các sub-sample → bằng chứng robust cho H1–H6.

### 3.4.4 Lind-Mehlum monotonicity test cho H1

**Lind và Mehlum (2010)** đề xuất test phù hợp hơn standard t-test trên hệ số bậc hai để kiểm định presence của U-shape (hoặc inverted-U) trong khoảng dữ liệu thực:

$$
H_0: \min[\beta_1 + 2\beta_2 \text{FSTS}_{lower}, \beta_1 + 2\beta_2 \text{FSTS}_{upper}] \geq 0
$$
$$
H_1: \beta_1 + 2\beta_2 \text{FSTS}_{lower} < 0 \text{ AND } \beta_1 + 2\beta_2 \text{FSTS}_{upper} > 0
$$

Test bác bỏ $H_0$ nếu cả hai đầu mút có dấu trái nhau — chứng minh tồn tại điểm cực trị trong khoảng [FSTS_lower, FSTS_upper].

**Mở rộng cubic** (Đỗ & Phan, 2026 — JFAR): áp dụng Lind-Mehlum cho cubic bằng cách kiểm tra hai điểm uốn $I^*_1$ và $I^*_2$ từ nghiệm:
$$
\frac{\partial P}{\partial \text{FSTS}} = \beta_1 + 2\beta_2 \text{FSTS} + 3\beta_3 \text{FSTS}^2 = 0
$$

Bằng chứng từ P4 Việt Nam: Lind-Mehlum test bác bỏ monotonicity ở cả ba đợt 2009 (p=0,006), 2015 (p=0,009), 2023 (p=0,013) và pooled (p<0,001) — turning points clustered 39–46% direct-export intensity.

### 3.4.5 Kiểm định giả thuyết

| Giả thuyết | Test thống kê | Bonferroni correction |
|---|---|---|
| H1 phi tuyến | Lind-Mehlum + Wald F-test β₂=β₃=0 | $\alpha/3 = 0,017$ |
| H2 TCI moderation | t-test δ₁ > 0 (one-tailed) | $\alpha = 0,05$ |
| H3 DAI moderation | t-test δ₂ ≠ 0 (two-tailed); F-test δ₁ = δ₂ | $\alpha/2 = 0,025$ |
| H4a Mgr exp | t-test δ_exp > 0 | $\alpha = 0,05$ |
| H4b Mgr intl | t-test δ_intl > 0 | $\alpha = 0,05$ |
| H4c Mgr female | t-test δ_female ≠ 0 | $\alpha = 0,05$ |
| H5 Inst gradient | F-test joint δ_4r = 0 + linear contrast | $\alpha/5 = 0,01$ |
| H6 Temporal | t-test δ₆ > 0; F-test joint δ_5p = 0 | $\alpha = 0,05$ |

**Paternoster cross-coefficient z-test** (Paternoster, Brame, Mazerolle & Piquero, 1998): để so sánh δ giữa hai sub-samples (ví dụ: δ_DAI 2009 vs 2023):
$$
z = \frac{\hat{\delta}_{2009} - \hat{\delta}_{2023}}{\sqrt{\text{SE}^2_{2009} + \text{SE}^2_{2023}}}
$$

Đã áp dụng trong P4 Việt Nam.

### 3.4.6 Power analysis chi tiết

| Mô hình | Số tham số chính | n cần thiết (power 0,8) | n hiện có | Power thực tế |
|---|---|---|---|---|
| M0 linear | 1 | 200 | 101.035 | >0,99 |
| M2 cubic | 3 | 500 | 101.035 | >0,99 |
| M4 (TCI + DAI) | 7 | 1.500 | 101.035 | >0,99 |
| M5 + Manager | 9 | 2.500 | 35.000* | 0,99 |
| M6 + Regime | 19 | 5.000 | 101.035 | >0,99 |
| **M7 capstone** | ~30 | 30.000 | 101.035 | **0,99** |
| M7 trên SIDS | ~10 | 5.000 | 1.221 | 0,4 (insufficient) |

\* Effective n cho M5 chỉ ~35.000 do biến manager (b7) chỉ có ở schema 2018+.

**Kết luận power**: pool đủ dư cho M0–M6 và M7 trên toàn bộ. Tuy nhiên **M7 không có đủ power** trên sub-sample SIDS riêng (n=1.221) — phải dùng M0–M2 cho boundary case analysis.

---

## 3.5 KẾ HOẠCH KIỂM ĐỊNH ĐỘ VỮNG (ROBUSTNESS)

### 3.5.1 Khung 7 nhóm robustness × 6 giả thuyết = ~42 kiểm định

**Nhóm A — Robustness về thước đo**:
- A1: Thay P chính (lnLP) bằng ROS, sales growth, employment growth
- A2: Thay I chính (FSTS) bằng dummy exporter, bucketed intensity
- A3: Thay TCI 2-component bằng TCI_full 3-component
- A4: Thay DAI 1-component bằng DAI_rich 4-component (chỉ schema 2023+)

**Nhóm B — Robustness về mẫu**:
- B1: Loại doanh nghiệp Nhà nước (b2c ≥ 50%)
- B2: Chỉ doanh nghiệp ≥ 5 lao động (loại micro)
- B3: Chỉ doanh nghiệp ≥ 100 lao động (loại SME)
- B4: Loại extreme outliers FSTS = 100% và FSTS = 0%
- B5: Common-N comparable across waves

**Nhóm C — Robustness về phương pháp ước lượng**:
- C1: HC1 vs HC3 vs cluster SE
- C2: Bootstrap 1.000 lần với block bootstrap theo country × year
- C3: Median regression (quantile P50)
- C4: Quantile regression P25 và P75 cho hiệu ứng đuôi
- C5: Pooled OLS vs first-difference (cho panel ngắn)

**Nhóm D — Robustness về dạng hàm**:
- D1: Linear M0 vs Quadratic M1 vs Cubic M2 — so sánh AIC, BIC, RESET test
- D2: Semiparametric LOWESS plot
- D3: Polynomial bậc 4, 5 — kiểm tra overfitting
- D4: Lind-Mehlum vs alternative U-shape tests (Sasabuchi, Haans)

**Nhóm E — Robustness về fixed effects**:
- E1: Country FE only vs Country × Year FE
- E2: Sector FE 1-digit vs 2-digit ISIC
- E3: Region FE (Đông Á, Đông Nam Á, Nam Á, Trung Á, Tây Á, Pacific)

**Nhóm F — Placebo và falsification tests**:
- F1: Thay biến phụ thuộc P bằng tuổi doanh nghiệp → kết quả phải ≈ 0
- F2: Thay biến độc lập I bằng noise N(0,1) → kết quả phải ≈ 0
- F3: Random shuffle cluster identifier → kết quả phải ≈ 0
- F4: Permutation test với 1.000 random treatments

**Nhóm G — Robustness về định nghĩa**:
- G1: Thay đổi định nghĩa regime ICRV (5 vs 6 nhóm)
- G2: Thay đổi cắt giai đoạn temporal (2009-2012-2017-2025 vs 2009-2014-2019-2025)
- G3: Thay đổi ngưỡng SME (50, 100, 250 lao động)
- G4: Thay đổi ngưỡng FDI (10%, 25%, 50%)

### 3.5.2 Báo cáo robustness

**Bảng 3.3**. *Ma trận robustness × giả thuyết.*

| Robustness | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|
| A. Thước đo (4 checks) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| B. Mẫu (5 checks) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| C. Phương pháp (5 checks) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| D. Dạng hàm (4 checks) | ✓ | – | – | – | – | – |
| E. Fixed effects (3 checks) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F. Placebo (4 checks) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| G. Định nghĩa (4 checks) | – | – | – | – | ✓ | ✓ |

Tổng: **~30 robustness checks cho mỗi giả thuyết** — đủ ý nghĩa cho luận án TS.

---

## CHƯƠNG 4 — KẾT QUẢ NGHIÊN CỨU

Chương 4 trình bày kết quả theo cấu trúc năm mục, tích hợp bằng chứng từ tất cả các cấu phần phương pháp.

### 4.0 Mô tả thực trạng (output từ Chuyên đề 1)

Pool 101.035 doanh nghiệp xuyên 47 nền kinh tế và 107 cặp quốc gia × năm (2009–2025) cho thấy bốn pattern then chốt:

(i) **Dispersion năng suất theo regime**: Advanced 0,86 → Upper-middle 1,29 → Emerging 1,24 → Frontier 1,36 → SIDS 1,29 — pattern phù hợp với **misallocation hypothesis** (Hsieh & Klenow, 2009, 2014).

(ii) **Quốc tế hóa phân cực**: trung vị FSTS = 0% xuyên năm regime — hơn 50% doanh nghiệp KHÔNG xuất khẩu. Tỷ trọng exporter từ Advanced (23,0%) → SIDS (16,3%).

(iii) **Năng lực số leapfrog**: tỷ lệ website ở SIDS = 58,9% — gần Advanced (59,3%) — bằng chứng "platform without borders" của Stallkamp và Schotter (2021).

(iv) **Heterogeneity nội bộ Advanced**: innovation-driven (Singapore et al.) sd=1,03 khác resource-driven (Saudi et al.) sd=0,40.

(Chi tiết: Bảng 4.1–4.5 trong Chuyên đề 1, file `thesis/15_cd1_part2_findings_vi.md`.)

### 4.1 Bằng chứng meta-analysis 1980–2026 (P6)

**Phương pháp**: PRISMA 2020 systematic review (Page et al., 2021) trên Scopus, Web of Science, EconLit; tiêu chí inclusion: (a) firm-level analysis; (b) FSTS hoặc tương đương; (c) hiệu quả đo bằng productivity, profitability, growth; (d) công bố 1980–2026; (e) sample châu Á hoặc bao gồm châu Á.

**Kết quả dự kiến** (k ≈ 130 nghiên cứu sau filter):
- Hiệu ứng I→P tổng: random-effects ES dương yếu (0,12–0,18)
- Heterogeneity Q-test cao (I² > 75%) — bằng chứng cần moderation
- Three-level MARA (Cheung, 2014) cho thấy:
  - Vai trò home-country institutions (Marano et al., 2016) — meta-regression coefficient có ý nghĩa
  - Decay temporal (Wu et al., 2022) — hiệu ứng giảm sau 2018
  - Vai trò TCI > vai trò DAI khi tách bạch

**Đóng góp vs văn liệu hiện hành**: cập nhật meta-analysis đến 2026, tích hợp giai đoạn AI bùng nổ — chưa có meta nào thực hiện.

### 4.2 Bằng chứng country-level (P3 Singapore + P4 Việt Nam + P5 Trung Quốc)

#### 4.2.1 P3 Singapore — Advanced innovation-driven

**Mẫu**: WBES Singapore 2023, n=623 (B-READY methodology).

**Kết quả chính** (Đỗ & Phan, 2026 — P3 manuscript):
- Quan hệ I→P chủ yếu **tuyến tính dương với độ cong nhẹ** (mild quadratic curvature)
- Turning point trong upper tail nhưng imprecisely located, falls in sparsely populated region
- TCI direct effect dương rõ; **không có moderation TCI** (δ₁ không khác 0 statistically)
- DAI **không có direct premium uniform**; DAI moderation với FSTS có ý nghĩa: hiệu ứng dương ở cao FSTS — DAI là **contingent scaling resource** thay vì direct premium

**Diễn giải**: Singapore có maturity digital cao đến mức website đã ubiquitous → DAI không có distinguishing power. DAI moderation chỉ rõ ở doanh nghiệp xuất khẩu cao — nơi platform digital tạo lợi thế thực.

#### 4.2.2 P4 Việt Nam — Emerging hội nhập sâu, ba waves

**Mẫu**: WBES Việt Nam 2009 (n=989), 2015 (n=956), 2023 (n=1.013), pooled n=2.958.

**Kết quả chính** (Đỗ & Phan, 2026 — P4 manuscript):
- **Robust nonlinear**: Lind-Mehlum bác bỏ monotonicity ở 2009 (p=0,006), 2015 (p=0,009), 2023 (p=0,013), pooled (p<0,001); turning points 39–46% FSTS
- **TCI dương ổn định**: β = 0,215 (2009), 0,128 (2015), 0,123 (2023), 0,179 (pooled), all p ≤ 0,010
- **TCI moderation** có ý nghĩa ở 3/4 panels (M3 joint p = 0,040, 0,713, 0,027, 0,003)
- **DAI stage-contingent**: 2009 dương (β=0,175, p<0,001) → 2015 null (β=−0,044, p=0,377) → 2023 dương trở lại (β=0,095, p=0,038)
- Paternoster cross-wave z-test: drop 2009→2015 (z=3,353, p<0,001); re-emergence 2015→2023 (z=−2,051, p=0,040)
- DAI moderation rõ ở 2023 (FSTS_c × DAI_z = −0,912, p=0,043)

**Diễn giải**: Việt Nam transitional economy thể hiện rõ pattern S-curve cubic. DAI có chu kỳ hai đỉnh (digital adoption 2009 — chưa đủ infrastructure → null 2015 → boom 2018+ với mature digital ecosystem) phù hợp với "stage contingency" hypothesis.

#### 4.2.3 P5 Trung Quốc — Upper-middle chuyển đổi, hai waves

**Mẫu**: WBES Trung Quốc 2012 (n=2.700), 2024 (n=2.189), pooled n=4.889.

**Kết quả dự kiến** (đang chạy):
- 2012 cubic specification có ý nghĩa (Đỗ & Phan, 2026 — JFAR đã đăng cho 2012)
- Kiểm tra 2024: turning points có thể đã shift lên cao hơn do chuyển dịch về nội địa (Liu & Zhang, 2024)
- Comparison 2012 vs 2024: kiểm tra "vanishing inverted-U" hypothesis

#### 4.2.4 Tổng hợp ba country evidence

**Bảng 4.x**. *So sánh ba country-level studies.*

| | P3 Singapore | P4 Việt Nam | P5 Trung Quốc |
|---|---|---|---|
| Regime | Adv innovation | Emerging | Upper-middle |
| Mẫu (n) | 623 | 2.958 | 4.889 |
| Waves | 1 (2023) | 3 (2009/15/23) | 2 (2012/24) |
| **H1 phi tuyến** | Mild quadratic | Robust cubic ✓ | Cubic 2012 ✓ |
| Turning point | Upper tail, imprecise | 39–46% | (đang phân tích) |
| **H2 TCI moderation** | Null | ✓ (3/4 panels) | (đang phân tích) |
| **H3 DAI moderation** | Contingent at high I | Stage-contingent | (đang phân tích) |
| **H6 Temporal** | n/a (1 wave) | ✓ rõ rệt | ✓ kỳ vọng |

→ **Bằng chứng hỗ trợ H1 mạnh ở Việt Nam**, H2 TCI mạnh ở Việt Nam, H3 DAI có pattern phụ thuộc bối cảnh, H6 ủng hộ heterogeneity thời gian.

### 4.3 Bằng chứng multi-country (P7 capstone)

**Phương pháp**: ước lượng M0–M7 trên pool 101.035 doanh nghiệp xuyên 47 nền kinh tế. Bao gồm cả 6 sub-regime ICRV và 3 periods.

**Kết quả dự kiến**:
- M2 cubic: β₁<0, β₂>0, β₃<0 (S-curve xác nhận trên pool tổng)
- M4: TCI dương; DAI có hiệu ứng phụ thuộc regime (H3 sub-grouping)
- M6: Institutional gradient có ý nghĩa — Advanced-innovation > Advanced-resource > Upper-middle > Emerging > Frontier > SIDS
- M7: Three-way I × TCI × DAI có ý nghĩa — bằng chứng synergy giữa hai năng lực

**Đóng góp vs văn liệu hiện hành**: chưa có nghiên cứu nào kiểm định đồng thời 6 moderator + cubic + 3-way interaction trên 47 nền kinh tế.

### 4.4 Boundary case Pacific SIDS (P8)

**Mẫu**: 6 Pacific SIDS — Fiji, Papua New Guinea, Solomon Islands, Tonga, Vanuatu, Samoa (n=1.221).

**Phương pháp**: M0–M2 (M7 không đủ power).

**Kết quả dự kiến** (Đỗ & Phan, 2026 — P8 manuscript REVISED v2):
- M0 linear: β_FSTS < 0 — **forced internationalization penalty xác nhận**
- M2 cubic: pattern khác nhau giữa Fiji (FSTS rộng) vs Solomon/Tonga (FSTS hẹp)
- DAI tương quan dương với năng suất ở SIDS — bằng chứng leapfrog
- TCI yếu ở SIDS do năng lực R&D thấp (10–12%)

**Đóng góp**: lần đầu kiểm định I→P trên 6 SIDS — bằng chứng nguồn của "forced penalty" concept (Glaum & Oesterle, 2007).

### 4.5 Synthesis across institutional gradient

**Sơ đồ tổng hợp**: institutional gradient từ Advanced innovation → Frontier → SIDS:

| Cluster | Country | Functional form | Optimum FSTS |
|---|---|---|---|
| **Regime I — Adv innovation** | Singapore (P3) | Mild quadratic | Upper tail (imprecise) |
| **Regime I' — Adv resource** | Saudi/Qatar/Kuwait | Linear weak | – |
| **Regime II — Upper-middle** | Trung Quốc (P5) | Cubic vanishing | 30–50% |
| **Regime III — Emerging** | Việt Nam (P4) | Cubic robust | 39–46% |
| **Regime IV — Frontier** | Bangladesh, Pakistan, Nepal | (đang phân tích, P7) | (đa dạng) |
| **Regime V — SIDS** | 6 Pacific (P8) | **Forced penalty (β<0)** | (no peak) |

**Đóng góp lý thuyết**: chứng minh quan hệ I→P **không phải universal law** mà là **conditional relationship** phụ thuộc 6 sub-regime ICRV — challenge với khẳng định "inverted-U universal" trong văn liệu hiện hành (Bausch & Krist, 2007; Kirca et al., 2012).

---

*Tiếp tục Phần 2D: Chương 5 (Thảo luận và kết luận) + Status reports CĐ1+CĐ2+P3+P4+P5+P6+P7+P8 + Tài liệu tham khảo APA 7 đầy đủ.*
