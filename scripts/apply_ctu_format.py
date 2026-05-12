#!/usr/bin/env python3
"""Apply CTU format (QĐ 1799/SH) to a pandoc-generated DOCX file.
- Font: Times New Roman 13pt (Headings: 13-16pt bold)
- Line spacing: 1.2
- Margins: left 3 cm, top/right/bottom 2 cm
"""
import sys
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

DOCX = sys.argv[1] if len(sys.argv) > 1 else "/home/user/Class-AI-Agent/thesis/cd1/00_cd1_complete_vi.docx"

doc = Document(DOCX)

# 1. Page margins (override pandoc defaults)
for section in doc.sections:
    section.left_margin = Cm(3)
    section.right_margin = Cm(2)
    section.top_margin = Cm(2)
    section.bottom_margin = Cm(2)

def force_font(run, name="Times New Roman", size_pt=None, bold=None):
    run.font.name = name
    rpr = run._element.get_or_add_rPr()
    rFonts = rpr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rpr.insert(0, rFonts)
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:eastAsia"), name)
    rFonts.set(qn("w:cs"), name)
    if size_pt is not None:
        run.font.size = Pt(size_pt)
    if bold is not None:
        run.font.bold = bold

def force_para(para, line_spacing=1.2, size_pt=13, bold=None):
    pf = para.paragraph_format
    pf.line_spacing = line_spacing
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    for run in para.runs:
        force_font(run, size_pt=size_pt, bold=bold)

HEADING_SIZES = {
    "Heading1": 16, "heading 1": 16, "Heading 1": 16,
    "Heading2": 14, "heading 2": 14, "Heading 2": 14,
    "Heading3": 13, "heading 3": 13, "Heading 3": 13,
    "Heading4": 13, "heading 4": 13, "Heading 4": 13,
    "Title": 18,
}

# 2. Apply to all paragraphs
for para in doc.paragraphs:
    style_name = para.style.name if para.style else "Normal"
    size = HEADING_SIZES.get(style_name)
    if size:
        force_para(para, size_pt=size, bold=True)
    else:
        force_para(para, size_pt=13)

# 3. Apply to tables
def apply_to_tables(tables):
    for tbl in tables:
        for row in tbl.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    style_name = para.style.name if para.style else "Normal"
                    size = HEADING_SIZES.get(style_name, 12)  # tables: 12pt for compactness
                    force_para(para, size_pt=size)
                # Recurse into nested tables
                apply_to_tables(cell.tables)

apply_to_tables(doc.tables)

# 4. Update default Normal style for any new paragraphs
try:
    normal = doc.styles["Normal"]
    normal.font.name = "Times New Roman"
    normal.font.size = Pt(13)
    normal.paragraph_format.line_spacing = 1.2
    normal.paragraph_format.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    rpr = normal.element.get_or_add_rPr()
    rFonts = rpr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rpr.insert(0, rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rFonts.set(qn(attr), "Times New Roman")
except KeyError:
    pass

doc.save(DOCX)

# Verify
d = Document(DOCX)
s = d.sections[0]
print(f"✓ Margins: L={s.left_margin.cm:.1f}cm R={s.right_margin.cm:.1f}cm T={s.top_margin.cm:.1f}cm B={s.bottom_margin.cm:.1f}cm")
sample_para = next((p for p in d.paragraphs if p.runs), None)
if sample_para and sample_para.runs:
    r = sample_para.runs[0]
    sz = r.font.size.pt if r.font.size else "inherit"
    print(f"✓ Sample paragraph: font={r.font.name}, size={sz}pt")
print(f"✓ Paragraphs: {len(d.paragraphs):,} | Tables: {len(d.tables)}")
print(f"✓ Saved → {DOCX} ({__import__('os').path.getsize(DOCX) / 1024:.1f} KB)")
