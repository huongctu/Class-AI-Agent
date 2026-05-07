# Hình minh họa CĐ1 v3.1d (06/05/2026, **11 figures** — cập nhật v3.0)

Thư mục này chứa 11 hình minh họa cho Chuyên đề tiến sĩ số 1 — đáp ứng review report HD 07/05/2026 Phần B (8-10 hình tối thiểu). Cập nhật từ 5 hình ban đầu (v1.0-v2.0).

## Danh mục 11 hình

| Hình | Tên | File | Cited ở | Nguồn dữ liệu |
|---|---|---|---|---|
| 2.1 | Sơ đồ 5 chiều đo lường HQKD | `fig_2_1_performance_dimensions` | file 14 §2.2 | Conceptual diagram |
| 4.0 | Pool distribution by survey year (3 schemas) | `fig_4_0_pool_by_year` | file 15 §4.1 | Pool 101.185 distribution |
| 4.1.1 | Pool composition (5 phân nhóm con) | `fig_4_1_pool_composition` | file 15 §4.1 | Pool counts |
| 4.2 | Density năng suất (6 phân nhóm con) | `fig_4_2_productivity_density` | file 15 §4.2 | sd log từ Bảng 4.1 |
| 4.4 | Slope chart 2009-2012 vs 2018-2025 | `fig_4_4_growth_pathway` | file 15 §4.6 | Bảng 4.6 deltas |
| 4.6 | Stacked bar SME composition | `fig_4_6_firm_size` | file 15 §4.5 | Bảng 4.5 SME% |
| 4.7 | Spider chart 5 chiều × 2 mốc | `fig_4_7_spider_chart` | file 15 §4.6 | Synthesized 2009-12 vs 2018-25 |
| 5.1 | Định vị 7 tiểu cảnh (Phân tán × FDI) | `fig_5_1_seven_scenes` | file 16 §5.8 | Bảng 5.1 |
| 5.6.1 | Mongolia evolution 2009–2025 | `fig_5_6_mongolia_evolution` | file 16 §5.6 | Mongolia 4 .dta panel |
| 5.7.1 | Kiribati vs Fiji vs Singapore | `fig_5_7_sids_comparison` | file 16 §5.7 | Kiribati 2025 .dta |
| 6.1 | Heatmap correlation 4 yếu tố × 5 nhóm | `fig_6_1_correlation_heatmap` | file 16 §6 | Bảng 6.1 |

## Chạy script (1 lệnh sinh tất cả 11 hình)

```bash
cd thesis/figures/
pip install pandas matplotlib openpyxl numpy
python3 generate_figures.py
```

Yêu cầu raw `.dta` files cho Mongolia panel (Hình 5.6.1) — tải từ https://www.enterprisesurveys.org/. Các hình khác chỉ cần data từ Bảng đã có trong CĐ1.

## Phiên bản

- v1.0 (06/05/2026): 3 hình ban đầu (4.1.1, 5.6.1, 5.7.1)
- v2.0: + 2 hình (4.2 density, 5.1 seven scenes) → 5 hình
- **v3.0 (06/05/2026)**: + 6 hình (2.1, 4.0, 4.4, 4.6, 4.7, 6.1) → **11 hình** đáp ứng review report B.2

## Hình còn lại (chưa generate trong v3.0)

Review report B.2 còn yêu cầu 2 hình cao cấp:
- Hình 4.1 — Heatmap năng suất × QG × ngành (cần `a4a` industry harmonized — Phase 2 7/2026)
- Hình 4.3 — Phân phối ROS + outliers (cần WBES profit data — Phase 1 6/2026)
- Hình 3.1 — Bản đồ 47 nước (cần geopandas + ISO3 mapping — manual creation)

11/14 hình hoàn thiện ≈ 79% target, vượt min review (8-10 hình).
