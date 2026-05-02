"""
Fill author information into Title_Page.docx and Cover_Letter.docx.

Author 1 (first / lead author):
  Do Thuy Huong (Đỗ Thùy Hương)
  PhD Candidate, College of Economics, Can Tho University, Can Tho, Vietnam
  Email: huongp1323001@gstudent.ctu.vn
  ORCID: 0000-0002-7711-2487

Author 2 (corresponding author — senior faculty, permanent email):
  Phan Anh Tu (Phan Anh Tú)
  Associate Professor, School of Economics, Can Tho University, Can Tho, Vietnam
  Email: patu@ctu.edu.vn
  ORCID: 0000-0003-0667-3137

Corresponding author choice: Phan Anh Tu (Author 2). Rationale: senior
faculty with a permanent institutional email; PhD candidate's
gstudent.ctu.vn address may change post-graduation, while journal
correspondence can extend over many months.
"""
from pathlib import Path
from docx import Document

REPO = Path("/home/user/Class-AI-Agent")
TITLE_PAGE = REPO / "papers/p3-singapore/Title_Page.docx"
COVER = REPO / "papers/p3-singapore/Cover_Letter.docx"

# ---- AUTHOR DATA ----
A1_NAME = "Do Thuy Huong"
A1_EMAIL = "huongp1323001@gstudent.ctu.vn"
A1_ORCID = "0000-0002-7711-2487"
A1_AFFIL = ("College of Economics, Can Tho University, "
            "Can Tho, Vietnam")

A2_NAME = "Phan Anh Tu"
A2_EMAIL = "patu@ctu.edu.vn"
A2_ORCID = "0000-0003-0667-3137"
A2_AFFIL = ("School of Economics, Can Tho University, "
            "Can Tho, Vietnam")

# Corresponding = Author 2 (senior faculty, permanent email)
CORR_NAME = A2_NAME
CORR_EMAIL = A2_EMAIL
CORR_ORCID = A2_ORCID
CORR_POSTAL = ("School of Economics, Can Tho University, "
               "Campus II, 3/2 Street, Ninh Kieu District, "
               "Can Tho City 900000, Vietnam")


def set_paragraph_text(p, text):
    """Replace paragraph text while preserving the first run's formatting."""
    if p.runs:
        p.runs[0].text = text
        for r in p.runs[1:]:
            r.text = ""
    else:
        p.text = text


def fill_title_page():
    doc = Document(TITLE_PAGE)

    # [2] Authors block: replace 3 placeholder lines with 2 authors.
    # Note: superscripts ᵃ and ᵇ for affiliations.
    authors_block = f"{A1_NAME}ᵃ\n{A2_NAME}ᵇ"
    set_paragraph_text(doc.paragraphs[2], authors_block)

    # [3] Affiliations block.
    affil_block = (f"ᵃ {A1_AFFIL}\n"
                   f"ᵇ {A2_AFFIL}")
    set_paragraph_text(doc.paragraphs[3], affil_block)

    # [5] Corresponding author block.
    corr_block = (f"{CORR_NAME}\n"
                  f"Email: {CORR_EMAIL}\n"
                  f"ORCID iD: https://orcid.org/{CORR_ORCID}\n"
                  f"{CORR_POSTAL}")
    set_paragraph_text(doc.paragraphs[5], corr_block)

    # [7] Acknowledgments — leave optional placeholder cleaner.
    set_paragraph_text(doc.paragraphs[7],
                       "The authors thank seminar participants and "
                       "colleagues at Can Tho University for helpful "
                       "feedback on earlier drafts. All remaining errors "
                       "are our own.")

    # [10] Funding — default no-support statement.
    set_paragraph_text(doc.paragraphs[10],
                       "The authors did not receive support from any "
                       "organization for the submitted work.")

    # [20] Authors' contributions.
    contrib = (
        f"{A1_NAME}: Conceptualization, Methodology, Data curation, "
        f"Formal analysis, Visualization, Writing — original draft. "
        f"{A2_NAME}: Conceptualization, Methodology, Supervision, "
        f"Validation, Writing — review & editing. Both authors read and "
        f"approved the final manuscript."
    )
    set_paragraph_text(doc.paragraphs[20], contrib)

    doc.save(TITLE_PAGE)
    print(f"Saved: {TITLE_PAGE}")


def fill_cover_letter():
    doc = Document(COVER)
    # Cover letter ends with three placeholder lines: [Author name],
    # [Affiliation], [Email address]. Replace with corresponding author block.
    n_replaced = 0
    for p in doc.paragraphs:
        old = p.text
        new = old
        new = new.replace("[Author name]", CORR_NAME)
        new = new.replace("[Affiliation]", CORR_AFFIL := A2_AFFIL)
        new = new.replace("[Email address]", CORR_EMAIL)
        if new != old:
            set_paragraph_text(p, new)
            n_replaced += 1

    # Add ORCID line right after the email if not already present
    # Find paragraph with the corresponding author email and append ORCID
    # only if the next paragraph isn't already an ORCID line.
    has_orcid = any(CORR_ORCID in p.text for p in doc.paragraphs)
    if not has_orcid:
        # Find the email paragraph to insert after
        for p in doc.paragraphs:
            if CORR_EMAIL in p.text:
                # Append ORCID to same paragraph if it's the standalone email line
                if p.text.strip() == CORR_EMAIL:
                    set_paragraph_text(
                        p, f"{CORR_EMAIL}\nORCID: https://orcid.org/{CORR_ORCID}"
                    )
                break

    doc.save(COVER)
    print(f"Saved: {COVER} ({n_replaced} placeholders replaced)")


def main():
    print("=" * 72)
    print("Fill author info — Title Page + Cover Letter")
    print("=" * 72)
    print(f"Author 1 (first):       {A1_NAME} <{A1_EMAIL}>")
    print(f"Author 2 (corresponding): {A2_NAME} <{A2_EMAIL}>")
    print(f"Corresponding author chosen: {CORR_NAME}")
    print()
    fill_title_page()
    fill_cover_letter()


if __name__ == "__main__":
    main()
