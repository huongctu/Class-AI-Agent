# CTU thesis dossier build templates

Bộ templates và scripts để build toàn bộ dossier luận án NCS Đỗ Thùy Hương (P1323001) thành DOCX theo format CTU.

## File trong folder này

| File | Mô tả |
|---|---|
| `build_ctu_reference.py` | Python script tạo 2 reference template DOCX (CTU thesis + CTU paper) qua python-docx |
| `build_dist.sh` | Bash script convert tất cả MD source → DOCX qua Pandoc + CTU template |
| `README.md` | File này |

## Yêu cầu

- **Pandoc 3.x+** — https://pandoc.org/installing.html
- **Python 3.8+** với `python-docx` — `pip install python-docx`
- **bash** (Linux/macOS) hoặc **Git Bash** (Windows)
- (Tùy chọn) **zip** để đóng gói

## Hướng dẫn build

```bash
# Bước 1: Clone repo
git clone -b claude/asia-internationalization-performance-2cYgO https://github.com/huongctu/Class-AI-Agent.git
cd Class-AI-Agent

# Bước 2: Tạo pandoc default reference
pandoc -o /tmp/pandoc_default.docx --print-default-data-file reference.docx

# Bước 3: Build 2 CTU template (xuất vào templates/)
python3 templates/build_ctu_reference.py /tmp/pandoc_default.docx templates/

# Bước 4: Convert tất cả MD → DOCX
bash templates/build_dist.sh

# Bước 5 (tùy chọn): Đóng gói thành zip
zip -rq luan_an_dossier_v1.zip dist/
```

Kết quả tiềm ánh:

- `templates/ctu_thesis_reference.docx` — CTU thesis template (TNR 13pt, lề 3-2-2-2, justify, line 1.5)
- `templates/ctu_paper_reference.docx` — CTU paper template (TNR 12pt, lề 2.5cm, justify, line 1.15)
- `dist/` folder với 27 file DOCX + source MD files
- `luan_an_dossier_v1.zip` — zip ~750KB đóng gói toàn bộ

## Cấu trúc dist/

```
dist/
├── 00_README.md
├── format_notes.md
├── luan_an/                       # 5 file plan luận án + README
├── chuyen_de_1/                   # CĐ1 (file 12, 14, 15, 16)
├── chuyen_de_2/                   # CĐ2 (file 13, 17, 18, 19)
└── manuscripts/
    ├── p3_vietnam/                # Vietnam manuscript (VI cô đọng + EN clean)
    ├── p4_singapore/              # Singapore manuscript (VI cô đọng + EN clean)
    ├── results/                   # Kết quả 4 công trình đã công bố
    └── reference/                 # QĐ, index, TLTQ, review report
```

Xem chi tiết format ở `dist/format_notes.md` (sau khi build).

## Format CTU được áp dụng

### CTU thesis template (luận án + 2 chuyên đề)

- Khổ giấy: A4 (21cm × 29.7cm)
- Lề: trái 3cm, phải 2cm, trên 2cm, dưới 2cm
- Font: Times New Roman 13pt, màu **đen** (#000000)
- Căn lề: **Justify** (canh đều)
- Line spacing: 1.5

### CTU paper template (bài báo EN P3, P4)

- Khổ giấy: A4
- Lề: 2.5cm tất cả
- Font: Times New Roman 12pt, màu **đen**
- Căn lề: Justify
- Line spacing: 1.15

## Verify format sau build

```python
from docx import Document
doc = Document("dist/luan_an/00_optimal_plan_vi.docx")
sec = doc.sections[0]
print(f"Lề L/R/T/B: {sec.left_margin.cm:.1f}/{sec.right_margin.cm:.1f}/{sec.top_margin.cm:.1f}/{sec.bottom_margin.cm:.1f} cm")
normal = doc.styles["Normal"]
print(f"Font: {normal.font.name} {normal.font.size.pt}pt color={normal.font.color.rgb}")
print(f"Alignment: {normal.paragraph_format.alignment}, line spacing: {normal.paragraph_format.line_spacing}")
```

Kết quả mong đợi:
```
Lề L/R/T/B: 3.0/2.0/2.0/2.0 cm
Font: Times New Roman 13.0pt color=000000
Alignment: JUSTIFY (3), line spacing: 1.5
```
