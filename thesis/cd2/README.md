# Chuyên đề tiến sĩ số 2 — Package hoàn thiện

> **Tiêu đề CĐ2**: Mô hình lý thuyết và thực nghiệm về mối quan hệ giữa quốc tế hóa và hiệu quả hoạt động kinh doanh của doanh nghiệp ở Châu Á
> **NCS**: Đỗ Thùy Hương · P1323001 · Quản trị kinh doanh (9340101)
> **HD**: TS. Nguyễn Minh Cảnh · Trường Kinh tế, Trường Đại học Cần Thơ

## Cấu trúc package

```
thesis/cd2/
├── README.md                       # File này
├── 00_cd2_complete_vi.md           # NCS-merged 3 phần thành 1 file (1,566 dòng · 182 KB)
├── 00_cd2_complete_vi.docx         # Word output (105 KB · 522 paragraphs · 26 tables · CTU format)
└── build_docx.sh                   # Pipeline MD → DOCX

thesis/   (canonical sources — KHÔNG edit trong cd2/)
├── 17_cd2_part1_intro_theory_vi.md          # Phần 1: Bìa + CH1 (giới thiệu) + CH2 (lý thuyết)
├── 18_cd2_part2_review_framework_hypotheses_vi.md  # Phần 2: CH3 (review) + CH4 (framework) + H1-H7
├── 19_cd2_part3_models_data_conclusion_vi.md       # Phần 3: CH5 (mô hình) + CH6 (data) + CH7 (kết luận)
└── 20_cd1_cd2_review_report_vi.md           # Review report
```

## Quy trình build .docx (giống CĐ1)

```bash
bash thesis/cd2/build_docx.sh
```

Pipeline: pandoc + `scripts/apply_ctu_format.py` với CTU format (TNR 13pt, line spacing 1.2, lề trái 3cm, lề khác 2cm).

## Format CTU (QĐ 1799/SH)

- [x] Times New Roman 13pt body | Headings 13-16pt bold
- [x] Giãn dòng 1.2
- [x] Lề trái 3 cm, các lề khác 2 cm
- [x] Đánh số mục max 3 cấp
- [x] APA 7th references (131 entries trong `thesis/04_references_apa7.md`)
- [ ] Mở Word → F9 update mục lục
- [ ] Insert 11 hình từ `thesis/figures/`

## Quality control results (11/05/2026)

| Script | Phạm vi | Kết quả |
|---|---|---|
| check-consistency | 00_cd2_complete_vi.md | ✅ Không phát hiện số liệu không nhất quán |
| format-apa7 | 00_cd2_complete_vi.md vs 04_references_apa7.md | ⚠️ 10 cảnh báo: 4 ref thực sự cần add (Adner 2017, Angrist & Pischke 2009, Contractor 2012, Dosi 1982); 6 là false-positive parser (Hambrick & Mason 1984, Sullivan 1994, Briguglio 1995 đã có trong refs) |
| apply_ctu_format | DOCX output | ✅ Margins L:3cm Others:2cm · TNR 13pt verified |

### 4 references cần add vào `thesis/04_references_apa7.md` trước khi nộp

```
Adner, R. (2017). Ecosystem as structure: An actionable construct for strategy. 
  Journal of Management, 43(1), 39–58. https://doi.org/10.1177/0149206316678451

Angrist, J. D., & Pischke, J.-S. (2009). Mostly harmless econometrics: An 
  empiricist's companion. Princeton University Press.

Contractor, F. J. (2012). Why do multinational firms exist? A theory note 
  about the effect of multinational expansion on performance and recent 
  methodological critiques. Global Strategy Journal, 2(4), 318–331. 
  https://doi.org/10.1111/j.2042-5805.2012.01045.x

Dosi, G. (1982). Technological paradigms and technological trajectories. 
  Research Policy, 11(3), 147–162. 
  https://doi.org/10.1016/0048-7333(82)90016-6
```

## Kết quả phân tích P7 — backbone của Chương 4 luận án

Pool **84,910 firms · 47 economies** (multi-country WBES Asia + Pacific). 11 models M0-M11.

| Model | n | R² adj | TP | L-M p | Note |
|---|---|---|---|---|---|
| M0 (baseline) | 84,910 | 0.000 | — | — | Mean-only |
| M1 (linear FSTS) | 84,910 | 0.0003 | — | — | Tiny linear effect |
| M2 (quadratic FSTS) | 84,910 | 0.0026 | **36.4%** | <.001 | Inverted-U xác nhận pool tổng |
| M3 (+ controls) | 38,342 | 0.015 | 33.8% | <.001 | |
| M5 (country-year FE) | 38,342 | **0.677** | 40.0% | <.001 | High explanatory power w/ FE |
| M6 (+ TCI main) | 38,051 | 0.024 | 32.7% | <.001 | TCI β=0.32, p<.001 |
| M7 (TCI mod) | 38,051 | 0.025 | 33.9% | <.001 | TCI×FSTS joint p=.0001 |
| M8 (TCI + DAI mod) | 37,940 | 0.030 | 33.8% | <.001 | **DAI×FSTS² joint p=.0007** ← H3 confirmed |
| M9 (+ mgr characteristics) | 35,568 | 0.035 | 36.1% | <.001 | Female mgr β=+0.19, p<.001 |
| M10 (+ ICRV regime) | 31,928 | 0.050 | — | — | U-shape (b₂>0) — regime distort |
| M11 (full three-way) | 29,840 | 0.068 | **34.6%** | .002 | Final spec — H1-H6 holds |

**Vị trí trong luận án**:
- §4.1 RQ1 meta-analysis (P6 backbone)
- **§4.3 Capstone multi-country (P7 = bằng chứng chính)** — dùng `p7_summary_focal.csv` + `p7_model_fit.csv` + `p7_coefs_all_models.csv`
- §4.4 H3 DAI moderation: M8 DAI×FSTS² joint F=7.26 p=.0007 → bằng chứng kết luận
- §4.5 ICRV regime sub-grouping (M10/M11)

## CĐ1 ↔ CĐ2 link

- **CĐ1** (descriptive 101.185 firms 47 nước): pattern điển hình + 6 ICRV sub-regimes
- **CĐ2** (theoretical + empirical 84.910 firms 47 nước): H1-H7 + 11 models + boundary case
- **P7 manuscript** (capstone): build từ CSV outputs + section design trong `thesis/07_p7_capstone_design_vi.md`

## Bước tiếp theo

1. NCS add 4 missing refs vào `04_references_apa7.md`
2. F9 update mục lục trong DOCX
3. Insert 11 hình từ `thesis/figures/`
4. P7 manuscript drafting → target MIR/JIBS (xem `writing_guides/author_guidelines_IBR_JWB_APJM_compared.pdf`)
