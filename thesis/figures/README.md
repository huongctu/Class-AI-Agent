# Hình minh họa CĐ1 v3.1 (06/05/2026)

Thư mục này chứa các hình được tạo từ dữ liệu WBES + ADB cho Chuyên đề tiến sĩ số 1, đáp ứng review report HD 07/05/2026 — Phần B (Hình, biểu đồ, bảng minh họa thống kê).

## Danh mục hình

### Hình 4.1.1 — Phân bố nhóm dữ liệu CĐ1
- File: `fig_4_1_pool_composition.svg` + `.png`
- Nội dung: Bar chart 5 phân nhóm con × n_firms (47.803 / 28.678 / 16.693 / 6.640 / 1.371)
- Pool tổng: 101.185 doanh nghiệp · 47 nước · 108 cặp QG×năm · 2009–2025 (cập nhật v3.1 với Kiribati 2025)
- Cited trong: §4.1

### Hình 5.6.1 — Mongolia evolution 2009–2025
- File: `fig_5_6_mongolia_evolution.svg` + `.png`
- Nội dung: 4-panel chart cho 4 đợt khảo sát Mongolia (2009, 2013, 2019, 2025)
  - Panel A: FSTS (cường độ xuất khẩu) đình trệ ở 4–6%
  - Panel B: FDI ≥10% giảm 7,2% → 3,2% (resource curse)
  - Panel C: Website tăng 39% → 65% (digital leapfrog) + R&D + ISO
  - Panel D: sd log năng suất (phân tán nội bộ)
- Source data: `mongolia_panel.csv`
- Cited trong: §5.6

### Hình 5.7.1 — Dị biệt nội bộ SIDS Thái Bình Dương
- File: `fig_5_7_sids_comparison.svg` + `.png`
- Nội dung: Bar chart so sánh 6 chỉ số (FSTS, FDI, R&D, ISO, Website, sd log) giữa:
  - Kiribati 2025 (isolated SIDS, n=150)
  - Fiji 2025 (high-digital SIDS, n=151)
  - Singapore 2023 (Advanced innovation, n=623)
- Phát hiện: Kiribati gần ZERO trên mọi chỉ số kết nối quốc tế (FSTS 1%, FDI 0,7%, ISO 1,3%, website 18,7%) — extreme boundary case bổ sung mạnh cho H6 forced internationalization penalty
- Cited trong: §5.7, §7.3.4 hàm ý CĐ2

## Replication

### Yêu cầu
```bash
pip install pandas matplotlib openpyxl
```

### Chạy
```bash
cd thesis/figures/
python3 generate_figures.py
```

### Dữ liệu nguồn
- `Mongolia-2009-full-data.dta`, `Mongolia-2013-full-data.dta`, `Mongolia-2019-full-data.dta`, `Mongolia-2025-full-data.dta` (tải từ www.enterprisesurveys.org)
- `Kiribati-2025-full-data.dta` (tải từ www.enterprisesurveys.org/en/data/exploreeconomies/2025/kiribati)

## Phiên bản

- v1.0 (06/05/2026): tạo 3 hình đầu tiên từ Mongolia panel + Kiribati 2025. Chạy trong session pandas + matplotlib local.

## Phụ lục — kế hoạch hình bổ sung (deadline 15/05/2026)

Theo review report HD Phần B.2, cần thêm 8–10 hình:
- [ ] Hình 4.1 — Heatmap năng suất × QG × ngành (cần `wbes/03_describe.py` xử lý full pool)
- [ ] Hình 4.2 — Phân phối năng suất theo nhóm (kernel density)
- [ ] Hình 4.3 — Phân phối ROS + outliers (box plot)
- [ ] Hình 4.4 — Lộ trình tăng trưởng 2009 vs 2025 (slope chart)
- [ ] Hình 4.5 — Heatmap đổi mới × ngành × nhóm
- [ ] Hình 4.6 — Phân phối quy mô DN (stacked bar)
- [ ] Hình 4.7 — Spider chart 5 chiều × 2 mốc
- [ ] Hình 5.1 — Định vị 7 tiểu cảnh (scatter bubble)
- [ ] Hình 6.1 — Scatter cặp biến nổi bật

3 hình trong commit này (4.1.1, 5.6.1, 5.7.1) là tiến độ ban đầu — đáp ứng phần ưu tiên cao của review report.
