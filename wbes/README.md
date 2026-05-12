# wbes/ — Pipeline phân tích WBES cho Chuyên đề 1, Chuyên đề 2 và Luận án

Pipeline Python phân tích pool WBES châu Á + Pacific phục vụ chương trình nghiên cứu của NCS Đỗ Thùy Hương (mã NCS P1323001), CTU. HD chuyên đề 1: TS. Nguyễn Minh Cảnh. HD chuyên đề 2 và luận án: PGS.TS. Phan Anh Tú.

**Phiên bản 2.5 (04/05/2026 — bản hoàn chỉnh)**.

## Pool tổng kết

| Chỉ số | Giá trị |
|---|---|
| Doanh nghiệp | **101.035** |
| Quốc gia | **47** (Châu Á + Pacific) |
| Cặp quốc gia × năm | **107** |
| Mốc khảo sát | **14** (từ 2009 đến 2025) |
| Đợt khảo sát năm 2025 | **12 quốc gia** (16.829 doanh nghiệp) |
| Pacific SIDS | **6 nước đầy đủ** (Fiji, PNG, Solomon Islands, Tonga, Vanuatu, Samoa; n=1.221) |
| Phân bố ICRV | Emerging 47.803 (47%) · Frontier 28.678 (28%) · Upper-middle 16.693 (17%) · Advanced 6.640 (7%) · SIDS 1.221 (1%) |

## Phụ thuộc

```bash
pip install pandas pyreadstat numpy requests
```

## Quy trình bốn bước

### Bước 1 — `01_inventory.py`

Quét tất cả file `.dta` trong thư mục upload, deduplicate theo cặp (country, year), lưu kết quả ra `/tmp/wbes/manifest.json`.

```bash
python3 wbes/01_inventory.py
```

### Bước 2 — `02_harmonize.py`

Đọc các file `.dta` theo manifest, trích biến cốt lõi WBES theo mapping (xem `thesis/08_p7_data_harmonization_protocol_vi.md`), build pool. Encoding fallback Latin-1/CP1252.

| Biến canonical | Variable WBES | Mô tả |
|---|---|---|
| `sales` | `d2` (fallback `d2x`, `n3`) | Doanh thu năm gần nhất |
| `employees` | `l1` (fallback `l11a`, `l10`) | Lao động thường xuyên FTE |
| `fsts_pct` | `d3b + d3c` | % xuất khẩu gián tiếp + trực tiếp |
| `b5` | `b5` | Năm thành lập |
| `b2b` | `b2b` | % sở hữu nước ngoài |
| `h1, h2` | `h1, h2` | Đổi mới sản phẩm/quy trình |
| `h8` | `h8` | R&D dummy |
| `b8` | `b8` | ISO certification |
| `c22b` | `c22b` | Có website |
| `a6a` | `a6a` | Stratification size |
| `l2` | `l2` | Lao động 3 năm trước |

```bash
python3 wbes/02_harmonize.py
```

Đầu ra: `/tmp/wbes/pool.csv` (~14 MB; 101.035 dòng × 24 cột).

### Bước 3 — `03_describe.py`

Tính bảng descriptive cho Chương 4–6 CĐ1.

```bash
python3 wbes/03_describe.py
```

Đầu ra (lưu vào `wbes/output/`):

| File | Nội dung |
|---|---|
| `Bang_4_1_Dispersion.csv` | Dispersion năng suất theo regime ICRV |
| `Bang_4_3_Growth.csv` | Tăng trưởng việc làm + FSTS + exporter |
| `Bang_4_4_Innovation.csv` | R&D + ISO + website + innovation |
| `Bang_4_5_Structure.csv` | SME + exporter + FDI |
| `Bang_4_6_Period_Delta.csv` | Δ pp 2018-2025 vs 2009-2012 |
| `Bang_5_1_Four_archetypes.csv` | Tiểu cảnh điển hình |
| `Bang_6_1_Correlation.csv` | Tương quan với log năng suất |
| `Phu_luc_A_Coverage.csv` | Coverage 47 nước × 107 cặp năm |
| `pool_summary_country_year.csv` | Stats per country-year (107 rows × 17 metrics) — snapshot v2.5 |

### Bước 4 — `fetch_macro_indicators.py` + `merge_macro_with_pool.py`

Bổ sung biến macro country-year (WGI, WDI, ITU) cho mô hình CĐ2.

```bash
# Fetch (cần internet kết nối api.worldbank.org và data360api.worldbank.org)
python3 wbes/fetch_macro_indicators.py

# Merge với pool firm-level
python3 wbes/merge_macro_with_pool.py
```

Đầu ra:
- `wbes/macro/macro_indicators_long.csv` — long format
- `wbes/macro/macro_indicators_wide.csv` — wide format country-year
- `/tmp/wbes/pool_with_macro.csv` — pool firm-level + macro merged

**Fallback** nếu không có internet: dùng `wbes/macro/macro_indicators_2023_static.csv` (giá trị 2023 cho 47 nước, đã commit). Static CSV chỉ chứa snapshot 2023; cần fetch thực để có time series 2009–2025.

## Macro indicators bổ sung (CĐ2 và luận án)

10 chỉ số được fetch:

| Code | Mô tả | Database |
|---|---|---|
| `RL.EST` | WGI Rule of Law (z-score, -2.5 to 2.5) | WB_WGI |
| `GE.EST` | WGI Government Effectiveness | WB_WGI |
| `RQ.EST` | WGI Regulatory Quality | WB_WGI |
| `CC.EST` | WGI Control of Corruption | WB_WGI |
| `NY.GDP.PCAP.PP.KD` | GDP per capita PPP (constant 2017 USD) | WB_WDI |
| `NY.GDP.MKTP.KD.ZG` | GDP growth (%) | WB_WDI |
| `BX.KLT.DINV.WD.GD.ZS` | FDI net inflows (% of GDP) | WB_WDI |
| `NE.EXP.GNFS.ZS` | Exports of goods and services (% of GDP) | WB_WDI |
| `FP.CPI.TOTL.ZG` | Inflation, consumer prices (annual %) | WB_WDI |
| `IT.NET.USER.ZS` | Internet users (% of population) | WB_WDI / ITU |

## Coverage WBES — danh sách 47 nước trong pool

**Advanced (11 nước, n=6.640)**: Bahrain, Brunei, Cyprus, Hong Kong SAR, Israel, Korea (Republic of), Kuwait, Qatar, Saudi Arabia, Singapore, Đài Loan.

**Upper-middle (6 nước, n=16.693)**: Armenia, China, Georgia, Kazakhstan, Malaysia, Thailand.

**Emerging (7 nước, n=47.803)**: India, Indonesia, Jordan, Mongolia, Philippines, Sri Lanka, Vietnam.

**Frontier (17 nước, n=28.678)**: Afghanistan, Bangladesh, Bhutan, Cambodia, Iraq, Kyrgyz Republic, Lao PDR, Lebanon, Maldives, Myanmar, Nepal, Pakistan, Tajikistan, Timor-Leste, Turkmenistan, Uzbekistan, Yemen.

**SIDS Pacific (6 nước, n=1.221)**: Fiji, Papua New Guinea, Samoa, Solomon Islands, Tonga, Vanuatu.

## Đợt khảo sát năm 2025 (12 quốc gia, n=16.829)

Ấn Độ (10.479), Nepal (1.740), Saudi Arabia (1.002), Thái Lan (813), Sri Lanka (607), Mongolia (601), Qatar (480), Afghanistan (480), Maldives (154), Fiji (151), Solomon Islands (150), Brunei (150), Kuwait (150).

## Hạn chế đã biết

1. **Doanh thu chưa chuyển sang USD PPP**. Phiên bản hiện tại trình bày dispersion (bất biến đơn vị); sẽ bổ sung tỷ giá PPP từ WDI ở luận án.

2. **TCI chỉ có 2 thành phần** (R&D + ISO). Cần thêm machinery imports.

3. **DAI chỉ có 1 thành phần** (website). Cần thêm e-commerce, ERP, cloud từ schema 2018+ (chỉ một số nước có).

4. **WBES không phải panel chuẩn** — phần lớn là cross-section lặp; panel ngắn 2-3 chu kỳ ở Trung Quốc, Việt Nam, Mongolia, Nepal.

5. **Top manager characteristics** chỉ có ở schema 2018+ (`b7`, `b7a`); chưa nhất quán xuyên đợt khảo sát.

6. **Lebanon 2009 và Lebanon COVID follow-ups** dùng schema MENA cũ (0/13 biến cốt lõi) — không hòa hợp được vào pool chuẩn.

7. **Nhật Bản chưa có WBES** — sẽ bổ sung từ METI/JIP nếu cần thiết cho luận án.

## Tương đương Stata

Đoạn Stata tương đương cho CĐ1 đính kèm trong Phụ lục F của `thesis/16_cd1_part3_cases_conclusion_vi.md`.
Đoạn Stata cho mô hình CĐ2 (M0–M7) đính kèm Phụ lục D của `thesis/19_cd2_part3_models_data_conclusion_vi.md`.

## Liên kết các tài liệu

**Chuyên đề 1** (HD: TS. Nguyễn Minh Cảnh):
- Outline: `thesis/12_chuyen_de_1_outline_vi.md`
- Bản nháp đầy đủ v2.5: `thesis/14_cd1_part1_intro_theory_vi.md` · `thesis/15_cd1_part2_findings_vi.md` · `thesis/16_cd1_part3_cases_conclusion_vi.md`

**Chuyên đề 2** (HD: PGS.TS. Phan Anh Tú):
- Outline: `thesis/13_chuyen_de_2_outline_vi.md`
- Bản nháp đầy đủ v1.0: `thesis/17_cd2_part1_intro_theory_vi.md` · `thesis/18_cd2_part2_review_framework_hypotheses_vi.md` · `thesis/19_cd2_part3_models_data_conclusion_vi.md`

**Tài liệu hỗ trợ**:
- Giao thức hòa hợp: `thesis/08_p7_data_harmonization_protocol_vi.md`
- Kế hoạch CĐ1 viết theo tuần: `thesis/12_chuyen_de_1_outline_vi.md` (Phụ lục F)
- Kế hoạch CĐ2 viết theo tuần: `thesis/13_chuyen_de_2_outline_vi.md` (Phụ lục G)

---

*Pipeline phiên bản 2.5 — 04/05/2026. Pool 101.035 doanh nghiệp · 47 nước · 107 country-years · giai đoạn 2009–2025.*
