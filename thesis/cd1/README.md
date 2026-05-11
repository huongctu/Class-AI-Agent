# Chuyên đề tiến sĩ số 1 — Package hoàn thiện

> **Tiêu đề chính thức** (QĐ 4769/QĐ-ĐHCT, 15/10/2024): "Thực trạng về hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á"
> **NCS**: Đỗ Thùy Hương · P1323001 · Quản trị kinh doanh (9340101)
> **HD**: TS. Nguyễn Minh Cảnh · Trường Kinh tế, Trường Đại học Cần Thơ

## Cấu trúc package

```
thesis/cd1/
├── README.md                       # File này
├── 00_cd1_complete_vi.md           # Merged 3 phần thành 1 file (1.023 dòng · 140 KB)
├── 00_cd1_complete_vi.docx         # Word output sau build_docx.sh (92 KB · CTU format)
└── build_docx.sh                   # Pipeline MD → DOCX với format CTU

thesis/   (canonical sources — KHÔNG edit trong cd1/)
├── 14_cd1_part1_intro_theory_vi.md     # Phần 1: Bìa + Tóm tắt + CH1-3
├── 15_cd1_part2_findings_vi.md         # Phần 2: CH4 — Thực trạng WBES
├── 16_cd1_part3_cases_conclusion_vi.md # Phần 3: CH5-7 + TLTK + Phụ lục
├── 04_references_apa7.md               # Tài liệu tham khảo (v2.7 — 131 entries)
├── 09_academic_writing_standards_vi.md # Chuẩn viết học thuật
├── 09b_vn_term_glossary.md             # Bảng thuật ngữ Anh-Việt (68 mục, 7 nhóm)
└── figures/                            # 11 hình minh họa

scripts/  (quality control)
├── apply_ctu_format.py               # Apply TNR 13 / 1.2 spacing / L 3cm R/T/B 2cm
├── academic_language_check.py        # Hedging + voice + APA tense (English)
├── check-consistency.py              # Số liệu cốt lõi pool 101.185 / 108 cy / k=113
├── format-apa7.py                    # Cross-reference inline vs refs list
└── demo_turning_point.py             # Synthetic demo I-P turning point
```

## Quy trình build .docx từ markdown

```bash
# Từ repo root
bash thesis/cd1/build_docx.sh
```

Pipeline 2 bước:
1. **Pandoc**: markdown → DOCX với mục lục tự động (TOC depth 3)
2. **Post-process** (`scripts/apply_ctu_format.py`):
   - Margins: lề trái **3 cm**, các lề khác **2 cm**
   - Font: **Times New Roman** (ascii + East-Asian + complex script)
   - Body text: **13 pt**
   - Heading 1: 16 pt bold · Heading 2: 14 pt · Heading 3-4: 13 pt
   - Tables: 12 pt cho compactness
   - Line spacing: **1.2** (multiple)

## Format CTU (QĐ 1799/SH) — Checklist

- [x] Font Times New Roman 13pt body
- [x] Giãn dòng 1.2
- [x] Lề trái 3 cm, các lề khác 2 cm
- [x] Đánh số mục max 3 cấp (#, ##, ###)
- [x] APA 7th references (131 entries, Sections A-R)
- [ ] Mục lục tự động (sau khi mở Word: F9 update)
- [ ] Danh mục bảng + hình + từ viết tắt
- [ ] Hình minh họa nhúng từ `thesis/figures/` (cần insert thủ công trong Word)
- [ ] Trang bìa + lời cam đoan (đã có sẵn trong markdown — verify lại format)

## Quality control trước khi nộp

```bash
# 1. Kiểm tra nhất quán số liệu cốt lõi (pool 101.185 / 47 economies / 108 c-y / 14 waves)
python3 scripts/check-consistency.py --file thesis/cd1/00_cd1_complete_vi.md

# 2. Kiểm tra citations cross-reference inline vs danh mục
python3 scripts/format-apa7.py \
    --paper thesis/cd1/00_cd1_complete_vi.md \
    --refs thesis/04_references_apa7.md

# 3. Kiểm tra ngôn ngữ học thuật (chỉ áp dụng cho phiên bản dịch tiếng Anh)
python3 scripts/academic_language_check.py \
    --file <english-version>.md --suggest --min-severity warning
```

**Quality report cuối cùng** (11/05/2026, sau merge v3.x):

| Script | Phạm vi | Kết quả |
|---|---|---|
| check-consistency | files 14, 15, 16 + complete | 2 false-positive (số "101.035" trong version history metadata, không phải claim hiện hành — bỏ qua) |
| format-apa7 | files 14, 15, 16 | File 14: ✅ clean. File 15: 1 false-positive parse "Advanced innovation-driven, đợt 2023" → "(Advanced innovation, 2023)". File 16: 1 missing `(Schumpeter, 1942)` — cần add Schumpeter vào refs khi finalize |
| apply_ctu_format | DOCX output | ✅ Margins L:3cm Others:2cm · Font TNR 13pt · 409 paragraphs · 27 tables |

## Bảy chương + Phụ lục

| Chương | Tiêu đề | Nguồn file |
|---|---|---|
| CH1 | Giới thiệu (đặt vấn đề, mục tiêu, phạm vi, phương pháp, đóng góp, kết cấu) | file 14 §1.1-1.6 |
| CH2 | Cơ sở lý luận về hiệu quả hoạt động kinh doanh (§2.1-2.7 với §2.6 U-curve 3 trạng thái + §2.7 CDCM 4-Tier Verhoef) | file 14 §2 |
| CH3 | Khung phân loại 6 phân nhóm con ICRV | file 14 §3 |
| CH4 | Thực trạng hiệu quả doanh nghiệp châu Á 2009-2025 (§4.1-4.11, 6 hình embedded) | file 15 |
| CH5 | Bảy tiểu cảnh điển hình (Singapore · Gulf · Việt Nam · TQ · Em Asia · Mongolia · PICs) | file 16 §5 |
| CH6 | Các yếu tố giải thích sơ bộ (§6.1 Gender pattern EAP, §6.2 U-curve digital) | file 16 §6 |
| CH7 | Khoảng trống thực tiễn và kết luận (8 hàm ý chính sách) | file 16 §7 |
| TLTK | 131 entries APA 7th (Sections A-R) | thesis/04_references_apa7.md |
| Phụ lục H | Bảng thuật ngữ Anh-Việt (68 mục, 7 nhóm) | thesis/09b_vn_term_glossary.md |

## Số liệu cốt lõi (canonical — KHÔNG đổi)

- **Pool**: 101.185 doanh nghiệp
- **Economies**: 47 (41 châu Á thuần + 7 SIDS Pacific boundary case extension)
- **Country-year pairs**: 108
- **Survey waves**: 14 (2009-2025)
- **Generation schemas**: 3 (PICS3, Standardized, BREADY)
- **Wave 2025**: 14 nước · 16.979 doanh nghiệp (gồm Kiribati 2025 — extreme boundary)

## Phụ thuộc Phase tiếp theo

- **CĐ2** (`thesis/17/18/19_cd2_*.md`): mô hình H1-H7 với 8 phân nhóm con
- **Luận án 5 chương** (`thesis/21/22*_thesis_plan_*.md`): aggregation CĐ1 → tổng quan + CĐ2 → results
- **Manuscripts**: P3 Singapore (MIR) · P4 Vietnam (JFAR) · P5 China (APJM) · P6 meta-analysis · P7 capstone · P8 Pacific SIDS

## Tham chiếu chéo

- **Chuẩn văn phong tiếng Việt**: `thesis/09_academic_writing_standards_vi.md` (5 conventions + 5 anti-patterns + 12-point checklist)
- **Bảng thuật ngữ Anh-Việt**: `thesis/09b_vn_term_glossary.md` (68 mục · 7 nhóm · ưu tiên thuật ngữ chính thức WB)
- **PhD writing demo**: `writing_guides/demo_phd_rewrite_india_discussion.md` (template MSc → PhD voice elevation)
