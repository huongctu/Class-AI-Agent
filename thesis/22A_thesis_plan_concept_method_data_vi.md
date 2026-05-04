# KẾ HOẠCH LUẬN ÁN — PHẦN 2A: CONCEPTUAL MODEL + CHƯƠNG 3 MỤC 3.1–3.2

> Tiếp nối `thesis/21_thesis_plan_part1_intro_theory_vi.md`.
> Phần 2B (Variables): `thesis/22B_thesis_plan_variables_vi.md`.
> Phần 2C (Estimation + Results): `thesis/22C_thesis_plan_estimation_results_vi.md`.
> Phần 2D (Discussion + Status + References): `thesis/22D_thesis_plan_discussion_status_refs_vi.md`.

---

## CONCEPTUAL MODEL — BOX VÀ ARROW

### Sơ đồ chi tiết (ASCII art — chuẩn LaTeX TikZ)

```
                    ┌──────────────────────────────────────────────────┐
                    │   ICRV REGIME (6 nhóm thể chế cấp quốc gia)      │
                    │   ┌──────────────┐ ┌──────────────┐              │
                    │   │ Adv-Inn (5)  │ │ Adv-Res (5)  │              │
                    │   │ Upp-mid (6)  │ │ Emerging (7) │              │
                    │   │ Frontier(17) │ │  SIDS (6)    │              │
                    │   └──────────────┘ └──────────────┘              │
                    │   Theory: North 1990; Khanna&Palepu 2010;        │
                    │           Peng 2003; Marano et al. 2016          │
                    └────────────┬─────────────────────────────────────┘
                                 │
                                 │ moderates  (H5)
                                 ▼
   ┌─────────────────────────────────────────────────────────────────┐
   │                                                                 │
   │  INTERNATIONALIZATION (I)              FIRM PERFORMANCE (P)     │
   │  ┌─────────────────┐                   ┌─────────────────┐      │
   │  │ FSTS  = d3b+d3c │ ────►  H1  ────►  │ log(d2 / l1)    │      │
   │  │ FSTS²           │      (S-curve     │ Labor           │      │
   │  │ FSTS³           │       cubic       │ productivity    │      │
   │  └─────────────────┘       phi tuyến)  │ Robustness:     │      │
   │  Theory: Johanson&Vahlne 1977,2009;    │   ROS, growth   │      │
   │          Lu&Beamish 2004;              └─────────────────┘      │
   │          Contractor et al. 2003                                 │
   │  Test: Lind&Mehlum 2010                                         │
   └────┬────────┬─────────────┬────────────────┬───────────────┬────┘
        │        │             │                │               │
        │ moderates (H2-H4)    │                │               │
        ▼        ▼             ▼                ▼               ▼
    ┌────────┐ ┌────────┐  ┌───────────────┐ ┌───────────────┐ ┌──────────┐
    │  TCI   │ │  DAI   │  │ TOP MANAGER   │ │  Year-bucket  │ │ Controls │
    │ (deep) │ │(surf.) │  │ (UE Theory)   │ │ (Temporal H6) │ │          │
    ├────────┤ ├────────┤  ├───────────────┤ ├───────────────┤ ├──────────┤
    │R&D dum │ │website │  │ Experience b7 │ │ 2009–2012     │ │ size_log │
    │ISO cert│ │e-comm. │  │ Education     │ │ 2013–2017     │ │ age      │
    │For-tech│ │ ERP    │  │ Gender b7a    │ │ 2018–2025     │ │ fdi10    │
    │license │ │ Cloud  │  │ Intl exp dum  │ │               │ │ sector_FE│
    └────────┘ └────────┘  └───────────────┘ └───────────────┘ │ year_FE  │
    Theory:    Theory:     Theory:           Theory:           │ ctry_FE  │
    Barney91   Banalieva   Hambrick&Mason84  Banalieva         └──────────┘
    Wernerfelt &Dhanaraj   Hambrick 2007     &Dhanaraj 2019
    1984       2019        Cannella 2008     Wu et al. 2022
    Cohen &    Bharadwaj   Nielsen2011       Yang et al. 2025
    Levinthal  et al. 2013 Hsu et al. 2013
    1990       Verhoef
    Lall 1992  et al. 2021
               Nambisan
               et al. 2019

    NON-OVERLAPPING: TCI ∩ DAI = ∅
    (separate items per Bharadwaj et al. 2013;
     Verhoef et al. 2021; Đỗ & Phan 2026 P3, P4)
```

### Chú thích sơ đồ

- **Mũi tên thẳng (→)**: tác động trực tiếp (direct effect).
- **Mũi tên đứt nét (▼)**: tác động điều tiết (moderation).
- **Box vuông**: biến quan sát được (observed variable).
- **Box bo tròn / chứa lý thuyết**: nguồn gốc lý thuyết.
- **H1–H6**: ánh xạ tới sáu giả thuyết (xem Mục 2.4 Phần 1).
- **Non-overlapping**: nguyên tắc TCI và DAI không chia sẻ item — bảo đảm construct purity (Bhandari, Ranta & Salo, 2023; Hair, Hult, Ringle & Sarstedt, 2022).

### Phương trình tổng quát (M7 capstone)

$$
\begin{aligned}
P_{ict} = \alpha &+ \underbrace{\beta_1 I_{ict} + \beta_2 I^2_{ict} + \beta_3 I^3_{ict}}_{\text{H1: phi tuyến S-curve}} \\
&+ \underbrace{\gamma_1 \text{TCI}_{ict} + \delta_1 (I \times \text{TCI})_{ict}}_{\text{H2: TCI moderation}} \\
&+ \underbrace{\gamma_2 \text{DAI}_{ict} + \delta_2 (I \times \text{DAI})_{ict}}_{\text{H3: DAI moderation regime-dependent}} \\
&+ \underbrace{\gamma_3 \text{Manager}_{ict} + \delta_3 (I \times \text{Manager})_{ict}}_{\text{H4: Top manager moderation}} \\
&+ \underbrace{\sum_{r=2}^{6} \gamma_{4r} \text{Regime}_r + \sum_{r=2}^{6} \delta_{4r} (I \times \text{Regime}_r)}_{\text{H5: Institutional gradient ICRV}} \\
&+ \underbrace{\sum_{p=2}^{3} \gamma_{5p} \text{Period}_p + \sum_{p=2}^{3} \delta_{5p} (I \times \text{Period}_p)}_{\text{H6: Temporal heterogeneity}} \\
&+ \underbrace{\delta_5 (I \times \text{TCI} \times \text{DAI}) + \delta_6 (\text{DAI} \times \text{Period}_3)}_{\text{Three-way + Digital × AI era}} \\
&+ \Gamma X_{ict} + \mu_c + \tau_t + \varepsilon_{ict}
\end{aligned}
$$

Trong đó:
- $i$ — doanh nghiệp; $c$ — quốc gia; $t$ — năm khảo sát.
- $X_{ict}$ — vector biến kiểm soát (size, age, FDI, sector).
- $\mu_c$ — country fixed effects (47 dummies).
- $\tau_t$ — year fixed effects (14 dummies).
- $\varepsilon_{ict}$ — sai số ngẫu nhiên với HC3 robust SE clustered ở country × industry.

---

## CHƯƠNG 3 — PHƯƠNG PHÁP NGHIÊN CỨU

### 3.1 Thiết kế nghiên cứu — Mixed synthesis-empirical

Luận án áp dụng thiết kế **mixed synthesis-empirical** kết hợp bốn cấu phần phương pháp luận:

**Cấu phần 1 — Meta-analysis update 1980–2026** (Chương 4 mục 4.1, ánh xạ Paper P6). Tổng hợp định lượng các nghiên cứu thực nghiệm về quan hệ I→P theo PRISMA 2020 protocol (Page et al., 2021). Random-effects meta-analysis với robust variance estimation (Hedges, Tipton & Johnson, 2010); three-level meta-analysis (MARA) khi có nhiều effect sizes trong cùng nghiên cứu (Cheung, 2014; Van den Noortgate, López-López, Marín-Martínez & Sánchez-Meca, 2013); kiểm tra publication bias bằng Egger test và trim-and-fill (Egger, Davey Smith, Schneider & Minder, 1997; Duval & Tweedie, 2000). Số nghiên cứu dự kiến k ≈ 130 sau filter PRISMA.

**Cấu phần 2 — Country-level empirical analysis** (Chương 4 mục 4.2, ánh xạ Papers P3 Singapore + P4 Việt Nam + P5 Trung Quốc). Ba quốc gia trọng tâm cung cấp three-way comparison theo gradient phát triển:
- **P3 Singapore** (n=623, đợt 2023): doanh nghiệp Advanced innovation-driven, kiểm định I→P trên cross-section duy nhất với DAI 4-component đầy đủ (B-READY methodology).
- **P4 Việt Nam** (n=2.958, ba đợt 2009/2015/2023): doanh nghiệp Emerging hội nhập sâu, kiểm định temporal evolution với three-wave comparison.
- **P5 Trung Quốc** (n=4.889, hai đợt 2012/2024): doanh nghiệp Upper-middle chuyển đổi, kiểm định trước/sau chiến tranh thương mại Mỹ-Trung 2018+.

Ba paper dùng OLS HC1 robust SE (Long & Ervin, 2000), Lind-Mehlum monotonicity test (Lind & Mehlum, 2010), Heckman two-step selection correction (Heckman, 1979), và Paternoster cross-coefficient z-test cho temporal comparison (Paternoster, Brame, Mazerolle & Piquero, 1998).

**Cấu phần 3 — Multi-country empirical analysis** (Chương 4 mục 4.3, ánh xạ Paper P7 capstone). Pool 101.035 doanh nghiệp xuyên 47 nền kinh tế × 107 cặp quốc gia × năm × 14 mốc khảo sát. Ước lượng tám mô hình M0–M7 từ baseline tuyến tính đến three-way moderation. Chiến lược nhận dạng đa tầng: country × year fixed effects + sector controls + IV với *distance to nearest international port* (Bao, Chen & Zhou, 2017) + subsample replication theo regime ICRV.

**Cấu phần 4 — Boundary case Pacific SIDS** (Chương 4 mục 4.4, ánh xạ Paper P8). Sub-sample 6 SIDS Pacific (n=1.221) kiểm định **forced internationalization penalty** — pattern β₁ < 0 do thị trường nội địa quá nhỏ buộc doanh nghiệp xuất khẩu không vì lợi thế cạnh tranh (Đỗ & Phan, 2026 — P8 manuscript).

**Cấu phần 5 (synthesis) — Cross-paper integration**. Chương 4 mục 4.5 tổng hợp năm pattern từ bốn cấu phần trên trên một sơ đồ "institutional gradient" liên kết Singapore (đỉnh) → Trung Quốc (chuyển đổi) → Việt Nam (transitional) → Frontier mainland → Pacific SIDS (boundary).

### 3.2 Dữ liệu — Pool 47 nền kinh tế × 107 cặp quốc gia × năm

#### 3.2.1 Nguồn dữ liệu chính

**World Bank Enterprise Surveys (WBES)** là cơ sở dữ liệu vi mô tin cậy nhất hiện có cho doanh nghiệp emerging và frontier markets (World Bank, 2010, 2016, 2024, n.d.). WBES sử dụng **stratified random sampling** với ba chiều phân tầng (industry classification ISIC Rev.4, establishment size, subnational region) — đảm bảo tính đại diện cho khu vực doanh nghiệp ngoài nông nghiệp đăng ký chính thức.

#### 3.2.2 Phạm vi 47 nền kinh tế theo ICRV regime

Pool dữ liệu phân theo sáu sub-regime của ICRV classification:

**Regime I — Advanced innovation-driven (5 nền kinh tế, n ≈ 4.220)**:
- Singapore (đợt 2023, n=623), Hong Kong SAR (2023, n=598), Hàn Quốc (2024, n=1.518), Đài Loan (2024, n=612), Israel (2013 + 2024, n=871).

> Cyprus (CYP) cũng thuộc nhóm này nhưng phụ thuộc EU; được phân riêng làm Advanced Mediterranean.

**Regime I' — Advanced resource-driven (5 nền kinh tế, n ≈ 1.932)**:
- Saudi Arabia (2025, n=1.002), Qatar (2025, n=480), Kuwait (2025, n=150), Bahrain (2024, n=150), Brunei (2025, n=150).

> Sub-grouping này là **đóng góp mới của luận án** — phát hiện từ Chuyên đề 1 cho thấy hai nhóm có pattern hiệu quả khác nhau (sd log năng suất Advanced-Inn ≈ 1,03 cao hơn Advanced-Res ≈ 0,40).

**Regime II — Upper-middle income (6 nền kinh tế, n=15.174)**:
- Trung Quốc (2012 + 2024, n=4.889), Malaysia (2015, 2019, 2024, n=3.200), Thái Lan (2016 + 2025, n=1.813), Kazakhstan (4 đợt 2009–2024, n=3.603), Armenia (4 đợt 2009–2024, n=1.655), Georgia (3 đợt 2013–2023, n=1.533).

**Regime III — Emerging income (7 nền kinh tế, n=47.803)**:
- Ấn Độ (3 đợt 2014/2022/2025, n=29.136 — chiếm 61% Emerging), Indonesia (3 đợt 2009/2015/2023, n=7.039), Philippines (2 đợt 2009/2023, n=3.663), Việt Nam (3 đợt 2009/2015/2023, n=3.077), Mongolia (4 đợt 2009/2013/2019/2025, n=1.905), Jordan (3 đợt 2013/2019/2024, n=1.766), Sri Lanka (2 đợt 2011/2025, n=1.217).

**Regime IV — Frontier income (17 nền kinh tế, n=28.678)**:
- Bangladesh (2 đợt, n=2.440), Pakistan (2 đợt, n=2.547), Lào (6 đợt 2009–2024, n=2.163), Campuchia (4 đợt, n=3.426), Myanmar (2 đợt 2014/2016, n=1.239), Nepal (5 đợt 2009–2025, n=5.707), Bhutan (3 đợt, n=658), Maldives (2025, n=154), Uzbekistan (3 đợt, n=2.637), Tajikistan (3 đợt, n=1.075), Kyrgyz Republic (4 đợt, n=1.219), Turkmenistan (2024, n=311), Afghanistan (2014 + 2025, n=890), Timor-Leste (3 đợt, n=514), Iraq (2 đợt, n=1.775), Lebanon (2013 + 2019, n=1.093), Yemen (2010 + 2013, n=830).

**Regime V — Pacific SIDS (6 nền kinh tế, n=1.221)** — boundary case:
- Fiji (2009 + 2025, n=315), Papua New Guinea (2015 + 2024, n=210), Solomon Islands (2025, n=150), Tonga (2024, n=150), Vanuatu (2009 + 2023, n=239), Samoa (2023, n=157).

**Tổng**: **47 nền kinh tế · 107 cặp quốc gia × năm · 101.035 doanh nghiệp · 14 mốc khảo sát giai đoạn 2009–2025**.

#### 3.2.3 Phạm vi thời gian — ba thế hệ schema WBES

Pool có 14 mốc khảo sát từ 2009 đến 2025, phân theo ba thế hệ schema:

- **Thế hệ 1 (2009–2012, n=14.335)**: schema PICS3 và BREADY ban đầu.
- **Thế hệ 2 (2013–2017, n=25.046)**: schema WBES Standardized chính thức.
- **Thế hệ 3 (2018–2025, n=61.654 — 61% pool)**: schema Standardized 2018+, BREADY 2023/2024/2025, BEE 2023, EAP Core, B-READY 2023.

Đặc biệt, **năm 2025 có 13 nền kinh tế khảo sát với 16.957 doanh nghiệp** — pool cập nhật nhất từng có cho nghiên cứu I→P sau làn sóng AI bùng nổ 2023+: Ấn Độ (10.479), Nepal (1.740), Saudi Arabia (1.002), Thái Lan (813), Sri Lanka (607), Mongolia (601), Qatar (480), Afghanistan (480), Maldives (154), Fiji (151), Solomon Islands (150), Brunei (150), Kuwait (150).

#### 3.2.4 Đặc điểm sampling và trọng số

WBES sử dụng **survey weights** `wmedian` (median assumption về eligibility) — cho phép tổng quát hóa từ mẫu khảo sát ra dân số doanh nghiệp đăng ký chính thức (World Bank, n.d.). Luận án dùng:
- **Mô hình chính M0–M5**: weighted regression với `wmedian`.
- **Mô hình M6–M7** (capstone đa tầng): unweighted với robust cluster SE — phù hợp Solon, Haider và Wooldridge (2015) khi mô hình có nhiều fixed effects và interactions. Báo cáo cả hai phiên bản trong Phụ lục robustness.

#### 3.2.5 Đặc điểm cấu trúc dữ liệu

WBES **không phải panel chuẩn** — phần lớn các đợt khảo sát là cross-section lặp với mẫu mới. Một số quốc gia (Trung Quốc, Việt Nam, Mongolia, Nepal) có panel ngắn 2–3 chu kỳ. Cấu trúc này phù hợp với:
- **Pooled cross-section** với country × year fixed effects (Wooldridge, 2010).
- **First-difference estimator** trong subsample panel khả dụng (cho robustness).

Hòa hợp ba thế hệ schema được thực hiện qua **pipeline Python** (`wbes/02_harmonize.py` — repository `huongctu/Class-AI-Agent`): đọc 105 file `.dta` với encoding fallback Latin-1/CP1252; crosswalk biến theo bảng tham chiếu (xem `thesis/08_p7_data_harmonization_protocol_vi.md`); loại WBES missing codes {-9, …, -1}; tính FSTS = `d3b + d3c`; winsorize log năng suất 1%/99% trong country-year.

#### 3.2.6 Sai số đo lường và caveat đơn vị tiền tệ

**Sai số đo lường chính** của WBES là tự khai báo về doanh thu, lao động, lợi nhuận. WBES sử dụng quy trình kiểm soát chất lượng nhiều lớp (giám sát viên, kiểm tra logic, gọi điện xác thực) — đảm bảo độ tin cậy cho phân tích so sánh xuyên quốc gia (World Bank, n.d.).

**Caveat đơn vị tiền tệ**. Doanh thu (`d2`) tự khai báo theo local currency unit (LCU). Để chuẩn hóa xuyên quốc gia, luận án sử dụng:
- **Năng suất lao động dispersion** (sd của log, P90/P10 ratio) — bất biến với đơn vị tiền tệ — cho phân tích cross-country chính.
- **PPP conversion** với tỷ giá từ World Development Indicators (WB WDI series `PA.NUS.PPP`) — cho subsample analysis ở Chương 4 mục 4.5.

#### 3.2.7 Bổ sung biến macro country-year

Pool firm-level được merge với 10 chỉ số macro country-year từ World Bank Data360 API (https://data360api.worldbank.org) — pipeline `wbes/fetch_macro_indicators.py`:

**Worldwide Governance Indicators (WGI)** — Kaufmann, Kraay và Mastruzzi (2011):
- `RL.EST` Rule of Law (z-score, −2,5 đến 2,5)
- `GE.EST` Government Effectiveness
- `RQ.EST` Regulatory Quality
- `CC.EST` Control of Corruption

**World Development Indicators (WDI)**:
- `NY.GDP.PCAP.PP.KD` GDP per capita PPP (constant 2017 USD)
- `NY.GDP.MKTP.KD.ZG` GDP growth (%)
- `BX.KLT.DINV.WD.GD.ZS` FDI net inflows (% GDP)
- `NE.EXP.GNFS.ZS` Exports of goods and services (% GDP)
- `FP.CPI.TOTL.ZG` Inflation, consumer prices (annual %)

**ITU Digital Hub**:
- `IT.NET.USER.ZS` Internet users (% population) — proxy cho ICT infrastructure

Các biến macro này được sử dụng:
- **ICRV regime classification**: dựa trên WGI Rule of Law quartile + WDI income classification.
- **Macro controls**: GDP growth, inflation cho phương trình M6–M7.
- **Heterogeneity moderators**: GDP per capita PPP × FSTS (luận án Chương 4 mục 4.3).

---

*Tiếp tục Phần 2B: Chương 3 mục 3.3 — Variables (Firm Performance + Internationalization + Moderators) với giải thích lý do và citations APA 7 chi tiết, dựa trên Đỗ & Phan (2026 — P3 Singapore manuscript) và Đỗ & Phan (2026 — P4 Vietnam manuscript).*
