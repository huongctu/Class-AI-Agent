# Hình minh họa CĐ1 v3.1c (06/05/2026, 5 figures)

Thư mục này chứa 5 hình minh họa cho Chuyên đề tiến sĩ số 1, đáp ứng review report HD 07/05/2026 — Phần B (Hình, biểu đồ, bảng minh họa thống kê).

## Danh mục hình

| Hình | Tên | Các file | Cited ở |
|---|---|---|---|
| 4.1.1 | Pool composition (5 phân nhóm con) | `fig_4_1_pool_composition.png/.svg` | file 15 §4.1 |
| 4.2 | Density năng suất (6 phân nhóm con) | `fig_4_2_productivity_density.png/.svg` | file 15 §4.2 |
| 5.1 | Định vị 7 tiểu cảnh (Phân tán × FDI) | `fig_5_1_seven_scenes.png/.svg` | file 16 §5.8 |
| 5.6.1 | Mongolia evolution 2009–2025 | `fig_5_6_mongolia_evolution.png/.svg` | file 16 §5.6 |
| 5.7.1 | Kiribati vs Fiji vs Singapore | `fig_5_7_sids_comparison.png/.svg` | file 16 §5.7 |

## Hai cách sử dụng

### Cách 1: Chạy Python script (khuyến nghị — tạo cả PNG + SVG)

```bash
cd thesis/figures/
pip install pandas matplotlib openpyxl numpy
python3 generate_figures.py
```

Yêu cầu tải raw `.dta` cho Mông Cổ (4 đợt khảo sát) từ https://www.enterprisesurveys.org/en/data/exploreeconomies. Nếu không có, script sẽ fallback vào `mongolia_panel.csv` đã có sẵn.

### Cách 2: Decode base64 PNG (không cần Python)

Nếu repo có file `*.png.b64` (có thể push trong commit khác):

```bash
cd thesis/figures/
bash decode_figures.sh
```

Tạo ra các file `.png` tương ứng. Sau đó markdown image refs trong file 15/16 sẽ rác đổ ra tự động khi xuất DOCX.

## Markdown image references trong CĐ1

File 15 đã có references (commit này):
- §4.1: `![Hình 4.1.1](figures/fig_4_1_pool_composition.png)`
- §4.2: `![Hình 4.2](figures/fig_4_2_productivity_density.png)`

File 16 (commit tiếp theo):
- §5.6: `![Hình 5.6.1](figures/fig_5_6_mongolia_evolution.png)`
- §5.7: `![Hình 5.7.1](figures/fig_5_7_sids_comparison.png)`
- §5.8: `![Hình 5.1](figures/fig_5_1_seven_scenes.png)`

## Phiên bản

- v1.0 (06/05/2026): 3 hình ban đầu (4.1.1, 5.6.1, 5.7.1) + Python script
- **v2.0 (06/05/2026)**: Bổ sung 2 hình mới (4.2 density + 5.1 seven scenes), cập nhật script với 5 functions, decoder script

## Phụ lục — kế hoạch hình còn lại (deadline 15/05/2026)

Theo review report HD Phần B.2:
- [ ] Hình 4.3 — Phân phối ROS + outliers (box plot) — cần WBES profit data
- [ ] Hình 4.4 — Lộ trình tăng trưởng 2009 vs 2025 (slope chart) — cần full pool harmonized
- [ ] Hình 4.5 — Heatmap đổi mới × ngành × nhóm — cần a4a industry
- [ ] Hình 4.6 — Phân phối quy mô DN (stacked bar) — cần l1 employment data
- [ ] Hình 4.7 — Spider chart 5 chiều × 2 mốc — cần harmonized 2009-2012 vs 2018-2025
- [ ] Hình 6.1 — Scatter cặp biến nổi bật (FSTS × productivity, FDI × productivity) — cần full pool

5 hình đã có trong commit này đáp ứng ưu tiên cao của review report.
