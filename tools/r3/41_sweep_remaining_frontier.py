"""
R3 Phase 4 sweep — replace remaining "digital-frontier" mentions with
extreme-case / digitally-mature framing across the manuscript.

Replacements applied in priority order (first-match wins per paragraph
substitution); each phrase is replaced globally within the doc.
"""
from pathlib import Path
from docx import Document

REPO = Path(__file__).resolve().parents[2]
DOC = REPO / "papers" / "p3-singapore" / "Manuscript_Blinded_MIR_2_revised.docx"

# Order matters: longer phrases first to avoid premature shorter matches.
SUBSTITUTIONS = [
    ("digital-frontier institutional environment as the relevant boundary condition",
     "extreme-case, within-context setting of a digitally mature economy"),
    ("digital-frontier institutional environment",
     "extreme-case Singapore setting"),
    ("Singapore's digital-frontier environment",
     "Singapore's digitally mature setting"),
    ("Singapore’s digital-frontier environment",
     "Singapore’s digitally mature setting"),
    ("digital-frontier environments",
     "digitally mature economies"),
    ("digital-frontier environment",
     "digitally mature setting"),
    ("digital-frontier economies",
     "digitally mature economies"),
    ("digital-frontier economy",
     "digitally mature economy"),
    ("digital-frontier settings",
     "digitally mature settings"),
    ("digital-frontier setting",
     "digitally mature setting"),
    ("in digital-frontier",
     "in digitally mature"),
    ("digital-frontier",  # catch-all
     "digitally mature"),
    ("a generalized boundary condition",
     "a generalized pattern across digitally mature economies"),
    ("the relevant boundary condition",
     "the relevant scope condition"),
]


def replace_paragraph(p, new_text):
    if not p.runs:
        p.text = new_text
        return
    p.runs[0].text = new_text
    for r in p.runs[1:]:
        r.text = ""


def main():
    doc = Document(DOC)
    n_changed = 0
    n_subs = 0
    examples = []
    for i, p in enumerate(doc.paragraphs):
        old = p.text
        new = old
        for src, dst in SUBSTITUTIONS:
            if src in new:
                new = new.replace(src, dst)
                n_subs += 1
        if new != old:
            replace_paragraph(p, new)
            n_changed += 1
            if len(examples) < 5:
                examples.append((i, new[:120]))

    doc.save(DOC)
    print(f"Sweep complete: {n_subs} substitutions across {n_changed} paragraphs")
    for i, sample in examples:
        print(f"  [para {i}] {sample}...")


if __name__ == "__main__":
    main()
