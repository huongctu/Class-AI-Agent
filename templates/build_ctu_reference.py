"""Build CTU-formatted DOCX reference templates.

Two outputs:
  1. ctu_thesis_reference.docx  — for luận án + chuyên đề (Times New Roman 13pt, justify, line spacing 1.5, lề 3-2-2-2)
  2. ctu_paper_reference.docx   — for English papers P3, P4 (Times New Roman 12pt, justify, line spacing 1.15, lề 2.5cm)

Builds from pandoc default reference.docx and modifies via python-docx.

Run:
    pip install python-docx
    pandoc -o /tmp/pandoc_default.docx --print-default-data-file reference.docx
    python3 templates/build_ctu_reference.py /tmp/pandoc_default.docx templates/
"""

import sys
import shutil
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


def set_default_font(doc, font_name="Times New Roman", font_size=13, color_rgb=None):
    if color_rgb is None:
        color_rgb = RGBColor(0, 0, 0)
    for style in doc.styles:
        try:
            font = style.font
            font.name = font_name
            font.size = Pt(font_size)
            font.color.rgb = color_rgb
            rPr = style.element.get_or_add_rPr()
            rFonts = rPr.find(qn('w:rFonts'))
            if rFonts is None:
                rFonts = OxmlElement('w:rFonts')
                rPr.insert(0, rFonts)
            rFonts.set(qn('w:eastAsia'), font_name)
            rFonts.set(qn('w:ascii'), font_name)
            rFonts.set(qn('w:hAnsi'), font_name)
        except (AttributeError, ValueError):
            continue


def set_paragraph_format_default(doc, line_spacing=1.5, alignment=WD_ALIGN_PARAGRAPH.JUSTIFY):
    for style in doc.styles:
        try:
            pf = style.paragraph_format
            pf.line_spacing = line_spacing
            pf.alignment = alignment
        except (AttributeError, ValueError):
            continue


def set_page_layout(doc, top=2.0, bottom=2.0, left=3.0, right=2.0, papersize_a4=True):
    for section in doc.sections:
        section.top_margin = Cm(top)
        section.bottom_margin = Cm(bottom)
        section.left_margin = Cm(left)
        section.right_margin = Cm(right)
        if papersize_a4:
            section.page_height = Cm(29.7)
            section.page_width = Cm(21.0)
        section.orientation = WD_ORIENT.PORTRAIT


def set_heading_styles(doc, font_name="Times New Roman", color_rgb=None):
    if color_rgb is None:
        color_rgb = RGBColor(0, 0, 0)
    heading_sizes = {"Heading 1": 16, "Heading 2": 14, "Heading 3": 13, "Heading 4": 13}
    for hname, hsize in heading_sizes.items():
        try:
            style = doc.styles[hname]
            font = style.font
            font.name = font_name
            font.size = Pt(hsize)
            font.bold = True
            font.color.rgb = color_rgb
            pf = style.paragraph_format
            pf.line_spacing = 1.5
            pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
            rPr = style.element.get_or_add_rPr()
            rFonts = rPr.find(qn('w:rFonts'))
            if rFonts is None:
                rFonts = OxmlElement('w:rFonts')
                rPr.insert(0, rFonts)
            rFonts.set(qn('w:ascii'), font_name)
            rFonts.set(qn('w:hAnsi'), font_name)
            rFonts.set(qn('w:eastAsia'), font_name)
        except KeyError:
            continue


def build_ctu_thesis_template(input_docx, output_docx):
    """CTU thesis/CĐ: TNR 13pt, lề 3-2-2-2, line 1.5, justify, đen."""
    shutil.copy(input_docx, output_docx)
    doc = Document(output_docx)
    set_page_layout(doc, top=2.0, bottom=2.0, left=3.0, right=2.0)
    set_default_font(doc, "Times New Roman", 13, RGBColor(0, 0, 0))
    set_paragraph_format_default(doc, 1.5, WD_ALIGN_PARAGRAPH.JUSTIFY)
    set_heading_styles(doc, "Times New Roman", RGBColor(0, 0, 0))
    doc.save(output_docx)
    print(f"[OK] CTU thesis template: {output_docx}")


def build_ctu_paper_template(input_docx, output_docx):
    """Paper reference (P3, P4 EN): TNR 12pt, lề 2.5cm, line 1.15, justify, đen."""
    shutil.copy(input_docx, output_docx)
    doc = Document(output_docx)
    set_page_layout(doc, top=2.5, bottom=2.5, left=2.5, right=2.5)
    set_default_font(doc, "Times New Roman", 12, RGBColor(0, 0, 0))
    set_paragraph_format_default(doc, 1.15, WD_ALIGN_PARAGRAPH.JUSTIFY)
    set_heading_styles(doc, "Times New Roman", RGBColor(0, 0, 0))
    doc.save(output_docx)
    print(f"[OK] CTU paper template: {output_docx}")


if __name__ == "__main__":
    if len(sys.argv) >= 3:
        pandoc_default = sys.argv[1]
        out_dir = sys.argv[2].rstrip("/")
    else:
        pandoc_default = "/tmp/pandoc_default.docx"
        out_dir = "templates"
    build_ctu_thesis_template(pandoc_default, f"{out_dir}/ctu_thesis_reference.docx")
    build_ctu_paper_template(pandoc_default, f"{out_dir}/ctu_paper_reference.docx")
    print("[DONE] CTU templates built.")
