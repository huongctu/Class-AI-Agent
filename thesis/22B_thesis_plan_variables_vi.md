# KẾ HOẠCH LUẬN ÁN — PHẦN 2B: CHƯƠNG 3 MỤC 3.3 — VARIABLES VỚI CITATIONS APA 7

> Tiếp nối `thesis/22A_thesis_plan_concept_method_data_vi.md`.
> Phần 2C (Estimation + Results): `thesis/22C_thesis_plan_estimation_results_vi.md`.
> Phần 2D (Discussion + Status + References): `thesis/22D_thesis_plan_discussion_status_refs_vi.md`.

---

## 3.3 ĐO LƯỜNG BIẾN — LOGIC VÀ CITATION

Mỗi biến đo lường trong luận án được lựa chọn dựa trên ba tiêu chí: (a) **bằng chứng thực nghiệm** từ văn liệu IB; (b) **tính có sẵn nhất quán** trong WBES qua ba thế hệ schema; (c) **khả năng tái lập** từ các bản thảo nội bộ P3 Singapore và P4 Việt Nam (Đỗ & Phan, 2026 — manuscripts).

### 3.3.1 Biến phụ thuộc — Hiệu quả hoạt động kinh doanh (P)

#### Biến chính: Năng suất lao động (ln Labor Productivity)

**Định nghĩa**:
$$
\text{lnLP}_{ict} = \ln\left(\frac{d2_{ict}}{l1_{ict}}\right)
$$

trong đó `d2` là tổng doanh thu năm tài chính gần nhất (LCU), `l1` là số lao động thường xuyên FTE cuối năm tài chính. Biến được **winsorize ở phân vị 1% và 99% trong từng cặp quốc gia × năm** để giảm ảnh hưởng outlier (Đỗ & Phan, 2026 — P3, P4 manuscripts).

**Lý do lựa chọn**:

(1) **Thước đo phổ biến nhất trong văn liệu IB**. Tỷ lệ sử dụng năng suất lao động trong các meta-analysis lớn về quan hệ I→P:
- Bausch và Krist (2007), k=87: 35%
- Kirca, Hult, Roth, Cavusgil et al. (2012), k=141: 36%
- Marano, Arregle, Hitt, Spadafora và van Essen (2016), k=359: 28%
- Wu, Wood và Khan (2022), k=359: 38%

(2) **Cơ sở lý thuyết misallocation**. Hsieh và Klenow (2009, 2014) chứng minh dispersion năng suất lao động xuyên doanh nghiệp trong cùng quốc gia phản ánh chất lượng phân bổ nguồn lực — cơ chế chính trong Institutional Theory (North, 1990; Khanna & Palepu, 2010). Doanh nghiệp có năng suất cao trong môi trường thể chế chưa hoàn thiện không thể mở rộng do constraints về tiếp cận tín dụng, đất đai, lao động.

(3) **Tính có sẵn xuyên ba thế hệ schema WBES**. Cả `d2` (doanh thu) và `l1` (lao động) đều có ở 14/14 mốc khảo sát từ 2009 đến 2025, đảm bảo tính so sánh thời gian (World Bank, 2010, 2016, 2024).

(4) **Bất biến đơn vị tiền tệ qua log transformation**. Mặc dù `d2` ở LCU, log năng suất cho phép so sánh xuyên quốc gia khi kết hợp với country fixed effects (Wooldridge, 2010).

(5) **Tiền lệ trong các bản thảo nội bộ**. Đỗ và Phan (2026 — P2 JFAR, P3 Singapore, P4 Việt Nam) đã sử dụng nhất quán `lnLP = ln(d2/l1)` — đảm bảo tính tái lập và so sánh chéo giữa luận án và các paper.

#### Biến phụ — Robustness checks

**Return on Sales (ROS)**:
$$
\text{ROS}_{ict} = \frac{\text{operating profit}_{ict}}{\text{sales}_{ict}}
$$

Chỉ tính được cho schema 2018+ (BREADY/BEE). Thước đo phù hợp với **stakeholder view of performance** (Freeman, 1984; Venkatraman & Ramanujam, 1986).

**Sales Growth Rate (3 năm CAGR)**:
$$
\text{SalesGrowth}_{ict} = \left(\frac{d2_{ict}}{n3_{ict}}\right)^{1/3} - 1
$$

trong đó `n3` là doanh thu 3 năm trước. Phù hợp với **growth measure** (Coad, Segarra & Teruel, 2018).

**Employment Growth (3 năm CAGR)**:
$$
\text{EmplGrowth}_{ict} = \left(\frac{l1_{ict}}{l2_{ict}}\right)^{1/3} - 1
$$

trong đó `l2` là số lao động 3 năm trước. Phù hợp với labor demand measure trong văn liệu IB cho emerging markets (Tran & Pham, 2024).

### 3.3.2 Biến độc lập chính — Cường độ quốc tế hóa (I)

#### Biến chính: FSTS (Foreign Sales to Total Sales)

**Định nghĩa**:
$$
\text{FSTS}_{ict} = \frac{d3b_{ict} + d3c_{ict}}{100}, \quad \text{FSTS} \in [0, 1]
$$

trong đó `d3b` là phần trăm doanh thu xuất khẩu **gián tiếp** (qua trung gian thương mại) và `d3c` là phần trăm doanh thu xuất khẩu **trực tiếp**. FSTS được rescale về thang [0, 1].

**Lý do lựa chọn**:

(1) **Định nghĩa chuẩn trong văn liệu IB**. Hsu và Boggs (2003) cùng các meta-analysis lớn (Bausch & Krist, 2007; Kirca et al., 2012; Wu, Wood & Khan, 2022) sử dụng FSTS làm thước đo chính cho cường độ quốc tế hóa. Lu và Beamish (2004) trong nghiên cứu S-curve seminal cũng dùng FSTS.

(2) **Phù hợp với mô hình S-curve và Uppsala**. Theo Johanson và Vahlne (1977, 2009), quá trình quốc tế hóa được đo bằng mức cam kết thị trường — và FSTS là proxy trực tiếp nhất cho mức cam kết này. Contractor, Kundu và Hsu (2003) trong three-stage theory of international expansion lập luận rằng FSTS phản ánh đồng thời (i) lợi ích quy mô từ xuất khẩu, (ii) chi phí phối hợp xuyên thị trường, và (iii) học tập về thị trường nước ngoài — ba cơ chế chính tạo nên S-curve.

(3) **Bao gồm cả gián tiếp và trực tiếp**. WBES phân biệt `d3b` (qua intermediaries) và `d3c` (direct). Tổng `d3b + d3c` phản ánh **toàn bộ exposure xuất khẩu** của doanh nghiệp, phù hợp với định nghĩa "internationalization scope" của Hsu, Chen và Cheng (2013) cho SMEs.

(4) **Tính có sẵn xuyên 14 mốc khảo sát**. Cả `d3b` và `d3c` đều có ở 14/14 đợt khảo sát của 47 nền kinh tế trong pool — đảm bảo coverage đầy đủ (World Bank, n.d.).

(5) **Tiền lệ trong P2, P3, P4**. Đỗ và Phan (2026) sử dụng nhất quán FSTS với mean-centering trong P3 (Singapore) và P4 (Việt Nam).

#### Đặc tả phi tuyến — Polynomial của FSTS

**Mean-centering trước khi bình phương** (Aiken & West, 1991):
$$
\text{FSTS}_{c,ict} = \text{FSTS}_{ict} - \overline{\text{FSTS}}_{wave}
$$

Sau đó tính:
$$
\text{FSTS}^2_{c,ict} = (\text{FSTS}_{c,ict})^2, \quad \text{FSTS}^3_{c,ict} = (\text{FSTS}_{c,ict})^3
$$

**Lý do mean-centering**: 
- Giảm đa cộng tuyến giữa FSTS và FSTS² (Aiken & West, 1991, p. 35)
- Variance Inflation Factor (VIF) duy trì dưới 3 trong các specification của P3, P4 — dưới ngưỡng cảnh báo VIF=10 của O'Brien (2007).

**Đặc tả cubic cho H1 phi tuyến S-curve**:
$$
P_{ict} = \alpha + \beta_1 \text{FSTS}_{c} + \beta_2 \text{FSTS}^2_{c} + \beta_3 \text{FSTS}^3_{c} + \Gamma X + \mu_c + \tau_t + \varepsilon
$$

Với S-curve được dự đoán: $\beta_1 < 0$ (giai đoạn 1 chi phí học tập), $\beta_2 > 0$ (giai đoạn 2 lợi ích quy mô), $\beta_3 < 0$ (giai đoạn 3 chi phí phối hợp).

**Kiểm định monotonicity** bằng Lind-Mehlum test (Lind & Mehlum, 2010): kiểm tra tồn tại điểm cực trị trong khoảng dữ liệu thay vì chỉ kiểm tra hệ số bậc hai.

#### Biến phụ — Robustness

**Dummy Exporter**:
$$
\text{Exporter}_{ict} = \mathbb{1}[\text{FSTS}_{ict} > 0]
$$

Phù hợp với extensive margin literature (Aw, Chung & Roberts, 2000) — phân biệt doanh nghiệp xuất khẩu vs không xuất khẩu trước khi xét cường độ.

**Bucketed Export Intensity**:
- Bucket 1: FSTS = 0% (non-exporter)
- Bucket 2: 0% < FSTS ≤ 25%
- Bucket 3: 25% < FSTS ≤ 50%
- Bucket 4: 50% < FSTS ≤ 75%
- Bucket 5: FSTS > 75%

Cho phép kiểm định non-linearity bằng dummy thay vì polynomial — robustness cho specification choice (Wooldridge, 2010).

### 3.3.3 Biến điều tiết — Năng lực công nghệ (TCI)

#### Định nghĩa và lý do

**Technological Capability Index (TCI)** đo năng lực công nghệ **NỘI TẠI** của doanh nghiệp — phản ánh chiều sâu năng lực thông qua absorptive capacity, đổi mới, và chứng nhận chất lượng.

**Phiên bản primary (TCI_z, 2-component)** — sử dụng nhất quán xuyên P3, P4, P5 và luận án Chương 4 mục 4.3:
$$
\text{TCI}_{c,wave} = \text{z-standardize}\left(\frac{b8 + e6}{2}\right)_{wave}
$$

trong đó:
- `b8` = chứng nhận chất lượng quốc tế (ISO certification dummy, recoded từ WBES 1/2 sang 1/0)
- `e6` = công nghệ được cấp phép từ nước ngoài (foreign-licensed technology dummy)

**Z-standardize trong từng wave** để hệ số có thể so sánh xuyên đợt khảo sát.

**Lý do lựa chọn 2-component**:

(1) **Cơ sở lý thuyết Cohen-Levinthal absorptive capacity**. Cohen và Levinthal (1990) định nghĩa absorptive capacity là "the ability of a firm to recognize the value of new, external information, assimilate it, and apply it to commercial ends". ISO certification (`b8`) phản ánh năng lực doanh nghiệp đáp ứng chuẩn quốc tế — thể hiện đã absorptive standards bên ngoài. Foreign-licensed technology (`e6`) phản ánh năng lực absorption công nghệ mới từ nước ngoài.

(2) **Lall (1992) capability building trong emerging markets**. Lall (1992) lập luận năng lực công nghệ ở emerging markets thường được xây dựng qua hai kênh: (i) chứng nhận chất lượng quốc tế (ISO) làm cầu nối tham gia chuỗi giá trị toàn cầu; (ii) licensing công nghệ từ MNE phát triển. Hai kênh này phản ánh **capability depth** thay vì surface adoption.

(3) **Tính có sẵn xuyên ba thế hệ schema**. Cả `b8` và `e6` đều có ở 14/14 mốc khảo sát; có thể recode từ schema cũ (1/2) sang chuẩn (1/0) (Đỗ & Phan, 2026 — P3, P4 harmonization protocol).

(4) **Construct purity với nguyên tắc non-overlapping**. Bhandari, Ranta và Salo (2023) cùng Hair, Hult, Ringle và Sarstedt (2022) khuyến nghị các formative composite không nên chia sẻ items để bảo đảm construct distinctiveness. TCI 2-component (b8, e6) **không trùng lấp** với DAI (xem Mục 3.3.4).

#### Phiên bản TCI_full (3-component) — robustness

Trong P4 Việt Nam và Chương 4 mục 4.5 robustness, TCI được mở rộng thành 3-component:
$$
\text{TCI}_{full,c,wave} = \text{z-standardize}\left(\frac{b8 + e6 + h8}{3}\right)_{wave}
$$

trong đó `h8` là chi R&D dương (R&D expenditure dummy). Chỉ áp dụng cho schema 2015+ (h8 không có ở 2009).

#### Phiên bản P3 Singapore (4-component) — chỉ cho 2023

Trong P3 (Đỗ & Phan, 2026 — Singapore manuscript), TCI được mở rộng thành 4-component nhờ B-READY 2023 methodology:
$$
\text{TCI}_{P3} = \text{z-standardize}\left(\frac{b8 + e6 + h1 + h8}{4}\right)
$$

trong đó `h1` là sản phẩm mới (innovation product dummy). Phù hợp với **innovation output** trong Cohen-Levinthal framework.

### 3.3.4 Biến điều tiết — Mức độ áp dụng số (DAI)

#### Định nghĩa và lý do

**Digital Adoption Index (DAI)** đo mức độ áp dụng hạ tầng số **NGOẠI TẠI** của doanh nghiệp — phản ánh mức tham gia digital transactions và interfaces.

**Phiên bản primary (DAI_z, 1-component)** — sử dụng nhất quán xuyên P4, P7 capstone:
$$
\text{DAI}_{c,wave} = \text{z-standardize}(c22b)_{wave}
$$

trong đó `c22b` = website doanh nghiệp dummy.

**Lý do lựa chọn 1-component cho cross-wave comparability**:

(1) **Chỉ `c22b` có ở cả 14/14 đợt khảo sát**. Các biến số hóa khác như e-commerce (k33), ERP, cloud chỉ xuất hiện từ schema 2018+ (BREADY 2023, BEE 2023). Để đảm bảo **temporal comparability** trong cubic specification của H1 và H6, DAI primary phải dùng item có sẵn xuyên cả ba thế hệ schema (Đỗ & Phan, 2026 — P4 Việt Nam manuscript).

(2) **Cơ sở lý thuyết Bharadwaj et al. digital business strategy**. Bharadwaj, El Sawy, Pavlou và Venkatraman (2013) đề xuất digital business strategy là "organizational strategy formulated and executed by leveraging digital resources to create differential value". Website doanh nghiệp là **foundational digital interface** — bước đầu tiên của digital adoption. Mặc dù đơn giản, website phản ánh đã quyết định tham gia kinh tế số ở mức nền tảng.

(3) **Verhoef et al. digital transformation framework**. Verhoef, Broekhuizen, Bart, Bhattacharya, Dong, Fabian và Haenlein (2021) phân biệt ba tier của digital transformation: (i) digitization (số hoá tài liệu), (ii) digitalization (số hoá quy trình), (iii) digital transformation (chuyển đổi mô hình kinh doanh). Website thuộc Tier 1–2 — vì vậy DAI primary nên được diễn giải là **Tier 1–2 digital adoption construct** thay vì broader digital transformation.

(4) **Nambisan, Wright và Feldman (2019) digital innovation logic**. Doanh nghiệp adoption digital interfaces tham gia ecosystem rộng hơn các doanh nghiệp không có. Stallkamp và Schotter (2021) chứng minh website là tiền đề cho platform-based internationalization — cho phép doanh nghiệp emerging markets tiếp cận thị trường nước ngoài qua e-commerce platforms (Amazon, Alibaba, Shopify).

(5) **Construct purity non-overlapping với TCI**. DAI 1-component (c22b) **không chia sẻ item nào** với TCI (b8, e6, h8). Đây là điểm khác biệt quan trọng với các nghiên cứu trước đây (Li, Liu & Qian, 2022) thường gộp chung digital và technological capability vào composite — vi phạm construct distinctiveness (Bhandari, Ranta & Salo, 2023).

#### Phiên bản DAI_rich (4-component) — chỉ cho 2023+

Trong P3 (Singapore 2023) và P4 robustness 2023 wave, DAI được mở rộng:
$$
\text{DAI}_{rich,P3} = \text{z-standardize}\left(\frac{c22b + k33/100 + k38/100 + \text{ecomm}}{4}\right)
$$

trong đó:
- `k33` = phần trăm doanh thu nhận qua điện tử (electronic payment receipts)
- `k38` = phần trăm thanh toán nhà cung cấp qua điện tử (electronic payment to suppliers)
- `ecomm` = bán hàng e-commerce dummy

DAI_rich phản ánh **transaction-enabling digital adoption** thay vì basic digital presence — phù hợp với Tier 2 trong khung Verhoef et al. (2021).

#### H3 stage-contingent từ bằng chứng P4 Việt Nam

Bằng chứng từ P4 (Đỗ & Phan, 2026 — Việt Nam) cho thấy DAI có pattern **stage-contingent**:
- 2009 wave: β_DAI = 0,175, p < 0,001 (dương mạnh)
- 2015 wave: β_DAI = −0,044, p = 0,377 (null)
- 2023 wave: β_DAI = 0,095, p = 0,038 (dương trở lại)
- Pooled: β_DAI = 0,078, p = 0,004 (dương)

Paternoster cross-wave z-test (Paternoster, Brame, Mazerolle & Piquero, 1998):
- DAI 2009 vs 2015: z = 3,353, p < 0,001 (drop có ý nghĩa)
- DAI 2015 vs 2023: z = −2,051, p = 0,040 (re-emergence có ý nghĩa)

Pattern này hỗ trợ **H3 phụ thuộc bối cảnh thời gian** thay vì uniform positive moderation — củng cố tách H3a (Emerging dương khi điều kiện thuận lợi) và H3b (có thể null/đảo dấu khi điều kiện không phù hợp).

### 3.3.5 Biến điều tiết — Đặc điểm nhà quản trị

#### Cơ sở lý thuyết Upper Echelons

Theo Hambrick và Mason (1984) và Hambrick (2007), các đặc điểm nhân khẩu học của top manager phản ánh quan điểm chiến lược và năng lực ra quyết định của doanh nghiệp.

**Bốn biến đo lường** (chỉ có ở schema 2018+):

**Manager Experience (years)**: `b7` — số năm kinh nghiệm của top manager trong ngành. Cơ sở: Cannella, Park và Lee (2008) — TMT functional experience. Dấu kỳ vọng δ_exp > 0.

**Manager Education**: proxy bằng years of schooling (chỉ một số đợt). Cơ sở: Hambrick và Mason (1984) — education proxy cho cognitive complexity.

**Manager Gender**: `b7a` — dummy nữ top manager. Cơ sở: Nielsen và Nielsen (2011) — TMT diversity. Exploratory không có dấu kỳ vọng prior.

**International Experience**: dummy doanh nghiệp có top manager đã làm việc/học tập ở nước ngoài (chỉ schema 2025+). Cơ sở: Nielsen và Nielsen (2011) — international orientation. Dấu kỳ vọng δ_intl > 0.

#### Hạn chế đo lường

WBES không phải **TMT survey** — chỉ đo top manager (CEO/owner), không phải toàn bộ team. Do đó luận án không thể kiểm định **TMT diversity** theo nghĩa rộng của Hambrick và Mason (1984). Hạn chế này được nêu rõ ở Chương 5 mục 5.4 và là khoảng trống cho nghiên cứu tiếp theo.

### 3.3.6 Biến điều tiết — Regime thể chế ICRV

#### Định nghĩa 6 sub-regime

ICRV (Institutional Context Regime Variation) classification dựa trên sự kết hợp:
- World Bank Income Classification (WB, 2024)
- Worldwide Governance Indicators Rule of Law (Kaufmann, Kraay & Mastruzzi, 2011)
- Asian Development Bank Regional Classification (ADB, 2024)

**Regime 1 — Advanced innovation-driven** (5 nước, n=4.222): SGP, HKG, KOR, TWN, ISR.
**Regime 1' — Advanced resource-driven** (5 nước, n=1.932): SAU, QAT, KWT, BHR, BRN.
**Regime 2 — Upper-middle income** (6 nước, n=15.174): CHN, MYS, THA, KAZ, ARM, GEO.
**Regime 3 — Emerging income** (7 nước, n=47.803): IND, IDN, PHL, VNM, LKA, JOR, MNG.
**Regime 4 — Frontier income** (17 nước, n=28.678): BGD, PAK, LAO, KHM, MMR, NPL, BTN, MDV, UZB, TJK, KGZ, TKM, AFG, TLS, IRQ, LBN, YEM.
**Regime 5 — SIDS Pacific** (6 nước, n=1.221): FJI, PNG, SLB, TON, VUT, WSM.

#### Lý do sub-grouping Advanced

Phát hiện từ Chuyên đề 1 cho thấy hai sub-group Advanced có pattern khác biệt rõ rệt:
- sd log năng suất Advanced-Innovation ≈ 1,03 (cao hơn)
- sd log năng suất Advanced-Resource ≈ 0,40 (thấp hơn)
- R&D dương Advanced-Innovation ≈ 21% (cao)
- R&D dương Advanced-Resource ≈ 9% (thấp)
- Cấu trúc kinh tế: Innovation-driven dựa trên dịch vụ tài chính + công nghệ; Resource-driven dựa trên dầu khí + tài chính.

Sub-grouping này là **đóng góp lý thuyết mới** của luận án so với Marano et al. (2016) và Wu, Wood và Khan (2022) chỉ phân biệt theo income.

### 3.3.7 Biến kiểm soát

| Biến | Variable WBES | Đơn vị | Cơ sở lý thuyết |
|---|---|---|---|
| `log_employees` | log(l1) | log lao động | Penrose (1959) — firm size; Coad et al. (2018) |
| `age` | year_survey − b5 | năm | Coad, Segarra & Teruel (2018) — firm age effects |
| `fdi10` | b2b ≥ 10% | dummy | Aitken & Harrison (1999) — FDI spillover |
| `sector_main` | a4a/a4b 1-digit | categorical | Sector-specific productivity (Hsieh & Klenow, 2014) |
| `country_FE` | 47 dummies | – | Unobserved country heterogeneity |
| `year_FE` | 14 dummies | – | Time-varying macro shocks |

**Lý do dùng log_employees thay vì size_strat**: Penrose (1959) lập luận log size capture diminishing returns to scale tốt hơn linear size. Đỗ và Phan (2026 — P4 Việt Nam) đã kiểm tra cả hai và log_employees có VIF thấp hơn.

**Lý do fdi10 dummy thay vì continuous b2b**: Aitken và Harrison (1999) sử dụng ngưỡng 10% như định nghĩa chuẩn cho FDI affiliate trong văn liệu IB và OECD. Doanh nghiệp với foreign ownership <10% được coi là portfolio investment, không phải MNE affiliate.

**Sector fixed effects**: Hsieh và Klenow (2014) chứng minh dispersion năng suất khác nhau xuyên các ngành. Sử dụng 1-digit ISIC để kiểm soát sector heterogeneity — phù hợp với P3, P4, P5 specifications.

### 3.3.8 Biến macro country-year (cho luận án Chương 4 mục 4.3)

Bổ sung từ World Bank Data360 API và ITU Digital Hub:

| Biến | Code | Cơ sở |
|---|---|---|
| WGI Rule of Law | RL.EST | Kaufmann, Kraay & Mastruzzi (2011) |
| WGI Government Effectiveness | GE.EST | Kaufmann et al. (2011) |
| GDP per capita PPP | NY.GDP.PCAP.PP.KD | World Bank WDI |
| GDP growth | NY.GDP.MKTP.KD.ZG | World Bank WDI |
| FDI inflow %GDP | BX.KLT.DINV.WD.GD.ZS | World Bank WDI |
| Internet users % | IT.NET.USER.ZS | ITU |

Các biến này cho phép kiểm định H5 institutional moderation ở cấp country-year (thay vì chỉ regime dummies cấp country) — robustness cho luận án.

### 3.3.9 Tóm tắt bảng định nghĩa biến

**Bảng 3.1**. *Codebook các biến chính dùng trong luận án.*

| Vai trò | Biến | Định nghĩa | Schema | Cơ sở lý thuyết |
|---|---|---|---|---|
| **DV chính** | lnLP | log(d2/l1), winsor 1/99 | Tất cả | Hsieh & Klenow (2009) |
| DV robust | ROS | profit/sales | 2018+ | Venkatraman & Ramanujam (1986) |
| DV robust | SalesGrowth | CAGR 3y | Tất cả (có n3) | Coad et al. (2018) |
| DV robust | EmplGrowth | CAGR 3y | Tất cả (có l2) | Tran & Pham (2024) |
| **IV chính** | FSTS_c | (d3b+d3c)/100, mean-cent | Tất cả | Hsu & Boggs (2003); Lu & Beamish (2004) |
| IV phi tuyến | FSTS_c² | bình phương | Tất cả | Aiken & West (1991) |
| IV cubic | FSTS_c³ | lập phương | Tất cả | Contractor et al. (2003) |
| IV robust | Exporter | dummy FSTS>0 | Tất cả | Aw, Chung & Roberts (2000) |
| **Mod H2** | TCI_z | z(b8 + e6)/2 | Tất cả | Cohen & Levinthal (1990); Lall (1992) |
| Mod H2 ext | TCI_full | z(b8+e6+h8)/3 | 2015+ | Cohen & Levinthal (1990) |
| **Mod H3** | DAI_z | z(c22b) | Tất cả | Bharadwaj et al. (2013); Verhoef et al. (2021) |
| Mod H3 rich | DAI_rich | z(c22b+k33+k38+ecomm) | 2023+ | Nambisan et al. (2019) |
| **Mod H4** | mgr_exp | b7 (years) | 2018+ | Hambrick & Mason (1984) |
| Mod H4 | mgr_intl | dummy intl experience | 2025+ | Nielsen & Nielsen (2011) |
| Mod H4 | mgr_female | b7a dummy | 2018+ | Cannella et al. (2008) |
| **Mod H5** | ICRV_regime | 6-category | Tất cả | North (1990); Marano et al. (2016) |
| **Mod H6** | Period | 3 buckets | Tất cả | Wu et al. (2022); Yang et al. (2025) |
| Control | log_emp | log(l1) | Tất cả | Penrose (1959) |
| Control | age | year − b5 | Tất cả | Coad et al. (2018) |
| Control | fdi10 | b2b ≥ 10% | Tất cả | Aitken & Harrison (1999) |
| Control | sector | 1-digit ISIC | Tất cả | Hsieh & Klenow (2014) |

---

*Tiếp tục Phần 2C: Chương 3 mục 3.4 (Estimation strategy + Identification 5 tầng) + Mục 3.5 (Robustness plan 30+ checks) + Chương 4 (Kết quả 5 mục).*
