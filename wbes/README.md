# wbes/ — Pipeline phân tích WBES cho Chuyên đề 1

Pipeline Python phân tích pool WBES châu Á phục vụ Chuyên đề 1 ("Thực trạng về hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á") — NCS Đỗ Thùy Hương, mã NCS P1323001, HD chuyên đề: TS. Nguyễn Minh Cảnh.

## Phụ thuộc

```bash
pip install pandas pyreadstat numpy
```

## Quy trình ba bước

### Bước 1 — `01_inventory.py`

Quét tất cả file `.dta` trong thư mục upload, deduplicate theo cặp (country, year) bằng cách giữ file lớn nhất, lưu kết quả ra `/tmp/wbes/manifest.json`.

```bash
python3 01_inventory.py
```

Đầu ra:
- `/tmp/wbes/manifest.json` — danh sách 85 entries (country × year → đường dẫn file lớn nhất).

### Bước 2 — `02_harmonize.py`

Đọc 85 file `.dta` theo manifest, trích các biến cốt lõi WBES theo mapping:

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

Build pool 81.957 dòng (1 dòng = 1 doanh nghiệp), tính các biến phái sinh: `labor_prod`, `log_labor_prod`, `log_employees`, `empl_growth_3y`, `is_sme`, `TCI`, `DAI`, `exporter`, `fdi10`.

Encoding fallback: thử mặc định → `latin1` → `cp1252` → `utf-8`.

```bash
python3 02_harmonize.py
```

Đầu ra:
- `/tmp/wbes/pool.csv` (~12 MB) — pool đầy đủ.

### Bước 3 — `03_describe.py`

Tính tất cả bảng descriptive cho Chương 4–6 của Chuyên đề 1.

Within-country winsorize log năng suất ở mức 1%/99% cho mỗi cặp quốc gia × năm trước khi tính dispersion.

Bảng 4.1: dispersion theo regime, tính per-country trước rồi bình quân theo trọng số n_firms — tách hiệu ứng dispersion nội bộ trong nước khỏi hiệu ứng đơn vị tiền tệ cross-country.

```bash
python3 03_describe.py
```

Đầu ra (lưu vào `/tmp/wbes/output/`):

| File | Nội dung |
|---|---|
| `Bang_4_1_Dispersion.csv` | Dispersion năng suất theo regime |
| `Bang_4_3_Growth.csv` | Tăng trưởng việc làm + FSTS + exporter |
| `Bang_4_4_Innovation.csv` | Đổi mới + R&D + ISO + website |
| `Bang_4_5_Structure.csv` | SME + exporter + FDI |
| `Bang_4_6_Period_Delta.csv` | Δ pp 2018-2024 vs 2007-2012 |
| `Bang_5_1_Four_archetypes.csv` | SGP, VNM, CHN, EmAsia composite |
| `Bang_6_1_Correlation.csv` | Tương quan với log năng suất |
| `Phu_luc_A_Coverage.csv` | Coverage 35 nước × 84 cặp năm |

## Tóm tắt pool hiện tại

- **81.957 doanh nghiệp** từ **35 nền kinh tế châu Á + Vanuatu**, **84 cặp quốc gia × năm**, giai đoạn **2009–2025**.
- Phân bố ICRV regime: Emerging 36.141 (44%) · Frontier 23.876 (29%) · Upper-middle 15.174 (19%) · Advanced 4.289 (5%) · SIDS 196 (0,2%).

## Còn thiếu (cần upload thêm)

| Quốc gia | Lý do |
|---|---|
| Nhật Bản | Chưa có WBES |
| Maldives | Chưa upload |
| Myanmar | Chưa upload |
| Fiji | SIDS — cần để hoàn chỉnh boundary case |
| Samoa | SIDS |
| Tonga | SIDS |
| Solomon Islands | SIDS |
| Papua New Guinea | SIDS |

## Hạn chế đã biết và kế hoạch khắc phục

1. **Doanh thu chưa chuyển sang USD PPP**. Phiên bản hiện tại trình bày dispersion (bất biến đơn vị); sẽ bổ sung tỷ giá PPP từ World Development Indicators để có thể trình bày năng suất tuyệt đối.

2. **TCI chỉ có 2 thành phần** (R&D + ISO). Cần thêm machinery imports cho phù hợp định nghĩa P3, P4, P5.

3. **DAI chỉ có 1 thành phần** (website). Cần thêm e-commerce, ERP, cloud từ schema 2018+ (chỉ một số nước có).

4. **WBES không phải panel chuẩn** — phần lớn là cross-section lặp; chỉ một số nước có panel ngắn.

## Tương đương Stata

Đoạn Stata tương đương đã được đính kèm trong Phụ lục E của `thesis/16_cd1_part3_cases_conclusion_vi.md`.

## Liên kết

- Outline CĐ1: `thesis/12_chuyen_de_1_outline_vi.md`
- Bản nháp CĐ1 (3 phần): `thesis/14_cd1_part1_intro_theory_vi.md` · `thesis/15_cd1_part2_findings_vi.md` · `thesis/16_cd1_part3_cases_conclusion_vi.md`
- Giao thức hòa hợp: `thesis/08_p7_data_harmonization_protocol_vi.md`

---

*Pipeline phiên bản 1.0 — 04/05/2026.*
