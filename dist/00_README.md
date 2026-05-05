# DOSSIER LUẬN ÁN TIẾN SĨ — NCS ĐỖ THÙY HƯƠNG (P1323001)

**Đề tài luận án (theo QĐ 4769/QĐ-ĐHCT, 15/10/2024)**: *Quốc tế hóa và hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á*

**HD luận án**: PGS.TS. Phan Anh Tú — Trường Kinh tế, Đại học Cần Thơ
**Mã ngành**: 9340101 · **Khóa**: 2023 đợt 1

---

## Cách tạo dossier DOCX (không cần NCS làm thao tác phức tạp)

Dossier gồm **27 file DOCX format chuẩn CTU** + source MD gốc, tổ chức theo 4 nhóm (luận án / CĐ1 / CĐ2 / manuscripts).

### Phương án 1 — NCS tự build (5 phút, cần Pandoc + Python)

```bash
# 1. Clone repo
git clone -b claude/asia-internationalization-performance-2cYgO https://github.com/huongctu/Class-AI-Agent.git
cd Class-AI-Agent

# 2. Cài Pandoc (nếu chưa có): https://pandoc.org/installing.html
# 3. Cài python-docx:
pip install python-docx

# 4. Tạo pandoc default reference
pandoc -o /tmp/pandoc_default.docx --print-default-data-file reference.docx

# 5. Build 2 CTU template
python3 templates/build_ctu_reference.py /tmp/pandoc_default.docx templates/

# 6. Convert tất cả MD → DOCX (xuất vào dist/)
bash templates/build_dist.sh

# 7. (Tùy chọn) Đóng gói thành zip
zip -rq luan_an_dossier_v1.zip dist/
```

Xem [`templates/README.md`](../templates/README.md) cho chi tiết.

### Phương án 2 — NCS download từng MD từ GitHub UI và tự mở trong Word

MS Word và LibreOffice đều mở được file `.md` (Markdown) trực tiếp. Sau khi mở:
- Format → Style → Apply "Normal" / "Heading 1-3"
- File → Page Setup → Margins: Custom (Left 3cm, Right/Top/Bottom 2cm)
- Format → Font: Times New Roman 13pt, Black
- Format → Paragraph: Justify, Line spacing 1.5

Chậm hơn nhưng không cần cài Pandoc.

### Phương án 3 — Yêu cầu Claude Code support

Nếu cần hỗ trợ build, NCS có thể yêu cầu Claude Code agent tiếp tục để push 2 CTU template DOCX (binary, ~10KB mỗi) vào `templates/` qua chunked base64. Sau đó NCS chỉ cần decode 1 lần là có thể dùng template trực tiếp với Pandoc.

---

## Cấu trúc dossier sau khi build

```
dist/
├── 00_README.md                   # File này
├── format_notes.md                # Quy chuẩn CTU áp dụng
│
├── luan_an/                       # 5 file plan luận án + README (DOCX + bản gốc MD)
│   ├── 00_optimal_plan_vi.docx           # Kế hoạch tổng thể
│   ├── 01_chapter_outline_vi.docx        # Dàn ý 5 chương
│   ├── 02_theoretical_framework_vi.docx  # Khung lý thuyết + H1-H6
│   ├── 03_methodology_vi.docx            # Phương pháp mixed synthesis-empirical
│   ├── 04_references_apa7.docx           # Tài liệu tham khảo APA 7th
│   ├── 00_README_thesis.docx             # README luận án
│   └── source_md/                        # Bản markdown gốc
│
├── chuyen_de_1/                   # CĐ1 — TS. Nguyễn Minh Cảnh hướng dẫn
│   ├── 12_outline.docx                       # Dàn ý
│   ├── 14_part1_intro_theory.docx            # Phần 1: Bìa + Tóm tắt + Ch.1-3
│   ├── 15_part2_findings.docx                # Phần 2: Ch.4 thực trạng từ WBES
│   ├── 16_part3_cases_conclusion.docx        # Phần 3: Ch.5-7 + TLTK + Phụ lục
│   └── source_md/
│
├── chuyen_de_2/                   # CĐ2 — PGS.TS. Phan Anh Tú hướng dẫn
│   ├── 13_outline.docx
│   ├── 17_part1_intro_theory.docx
│   ├── 18_part2_review_framework_hypotheses.docx
│   ├── 19_part3_models_data_conclusion.docx
│   └── source_md/
│
└── manuscripts/                   # Các bản thảo bài báo và tham chiếu
    ├── 00_README_manuscripts.docx
    ├── p3_vietnam/                          # Vietnam manuscript (3 đợt panel 2009/2015/2023, n=2.958)
    │   ├── p3_vietnam_vi_concise.docx       # Bản tiếng Việt học thuật cô đọng
    │   ├── p3_vietnam_en_clean.docx         # Bản tiếng Anh chuẩn hóa
    │   └── source_md/
    ├── p4_singapore/                        # Singapore manuscript (single-wave 2023, n=623)
    │   ├── p4_singapore_vi_concise.docx
    │   ├── p4_singapore_en_clean.docx
    │   └── source_md/
    ├── results/                             # Kết quả tóm tắt 4 công trình đã công bố
    │   ├── p1_emerging_asia_results.docx       # P1 VEFR 2026
    │   ├── p2_china_smes_results.docx          # P2 JFAR 2026
    │   ├── p_india_book_chapter_results.docx   # India IntechOpen 2025
    │   └── p_meta_analysis_kyyeu_results.docx  # Meta-analysis Kỷ yếu CTU 2024
    └── reference/                           # Tham chiếu hành chính
        ├── QD_legal_reference.docx             # QĐ 4768 + 4769
        ├── published_works_index.docx          # Index 4 công trình
        ├── 11_TLTQ_dissertation_positioning.docx
        └── 20_cd1_cd2_review_report.docx
```

---

## Format áp dụng

### Luận án và 2 Chuyên đề (CTU standard)

- **Khổ giấy**: A4 (21cm × 29.7cm)
- **Lề**: trái 3cm, phải 2cm, trên 2cm, dưới 2cm
- **Font**: Times New Roman 13pt, màu **đen** (#000000)
- **Căn lề**: **Justify** (canh đều)
- **Line spacing**: 1.5
- **Trích dẫn**: APA 7th

### Bài báo tiếng Anh (P3 Vietnam, P4 Singapore)

- **Lề**: 2.5cm tất cả
- **Font**: Times New Roman 12pt, đen
- **Justify**, **line spacing 1.15**
- Phù hợp submission cho IB journals (JIBS, GSJ, IBR, JBR)

### P5 China 2012-2024 (đã upload, chưa review)

- **Skip** trong build hiện tại
- NCS yêu cầu Claude Code review kết quả P5 trước khi đóng gói

---

## Trạng thái xuất bản của 4 công trình đã công bố

| Mã | Công trình | Tạp chí/NXB | Trạng thái |
|---|---|---|---|
| **P1** | Firm Performance Heterogeneity in Emerging Asia | Vietnam Economic and Financial Review (VEFR) | ✅ Đã công bố 2026 |
| **P2** | Unveiling the impact of Chinese manufacturing SMEs' internationalization on performance | Journal of Finance & Accounting Research, No. 02 (39) - 2026, pp. 287-291 | ✅ Đã công bố 2026 |
| **P_India** | Internationalization and Firm Performance of Firms in India: The Role of Top Management | IntechOpen Book Chapter | ✅ Đã công bố 23/06/2025 |
| **P_Meta** | Internationalization and firm performance: A meta-analysis review | Kỷ yếu Hội thảo quốc tế lần thứ 6, CTU | ✅ Đã chấp nhận 12/12/2024 |

## Liên hệ

- **NCS**: Đỗ Thùy Hương — thuyhuongctu@gmail.com — 0987.962.542
- **HD luận án**: PGS.TS. Phan Anh Tú — patu@ctu.edu.vn — 0988.263.778
- **Đơn vị**: Trường Kinh tế, Đại học Cần Thơ

---

*Bundle plan: 05/05/2026 — Build infrastructure: `templates/build_ctu_reference.py` + `templates/build_dist.sh`*
