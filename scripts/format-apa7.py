#!/usr/bin/env python3
"""
format-apa7.py — Kiểm tra chéo citations inline vs danh mục references APA7.

Chạy:
    python3 scripts/format-apa7.py                          # kiểm tra tất cả
    python3 scripts/format-apa7.py --paper manuscripts/p3_vietnam_en_clean.md
    python3 scripts/format-apa7.py --refs thesis/04_references_apa7.md
    python3 scripts/format-apa7.py --orphans                # chỉ liệt kê refs thừa
"""

import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict

# ─── Config ──────────────────────────────────────────────────────────────────
DEFAULT_REFS_FILE = "thesis/04_references_apa7.md"

MANUSCRIPT_PATTERNS = [
    "p3/p3_vietnam_en_clean.md",
    "p4/p4_singapore_en_clean.md",
    "p5/versions/apjm/manuscript_v1_8_blinded_part1_frontmatter_intro.md",
    "p5/versions/apjm/manuscript_v1_8_blinded_part2_theory.md",
    "p5/versions/apjm/manuscript_v1_8_blinded_part3_data_methods.md",
    "p5/versions/apjm/manuscript_v1_8_blinded_part4_results.md",
    "chuyen_de/cd1/14_cd1_part1_intro_theory_vi.md",
    "chuyen_de/cd1/15_cd1_part2_findings_vi.md",
    "chuyen_de/cd1/16_cd1_part3_cases_conclusion_vi.md",
    "chuyen_de/cd2/17_cd2_part1_intro_theory_vi.md",
    "chuyen_de/cd2/18_cd2_part2_review_framework_hypotheses_vi.md",
    "chuyen_de/cd2/19_cd2_part3_models_data_conclusion_vi.md",
    "p6/21_p6_meta_vi.md",
]

# Regex: (Author, Year) hoặc Author (Year) hoặc Author et al. (Year)
# Bắt được: (Đỗ & Phan, 2026), (World Bank, 2025), (Lu & Beamish, 2004), etc.
INLINE_CITE_RE = re.compile(
    r'\('
    r'([A-ZÀ-Ỵa-zà-ỵÐđ][A-ZÀ-Ỵa-zà-ỵÐđ\s\-,\.&]+?)'  # author(s)
    r',\s*'
    r'(\d{4}[a-z]?)'                                       # year
    r'(?:,\s*(?:p\.|pp\.)?\s*[\d\-]+)?'                   # optional page
    r'\)'
)

# Regex để parse author + year từ reference list entries
# APA7: Author, A., & Co, B. (Year). Title...  — include & in character class
REF_ENTRY_RE = re.compile(
    r'^([A-ZÀ-Ỵa-zà-ỵÐđ][A-Za-zÀ-Ỵà-ỵÐđ\s\-,\.&]+?)\.\s*\((\d{4}[a-z]?)(?:,\s*[A-Za-z]+)?\)'
)

# Known abbreviation/alias mappings (inline key → how they appear in refs)
ALIASES = {
    # Map abbreviation → how the entry appears in the reference list.
    # Keep same token so normalize_author produces the matching first word.
    "World Bank": "World Bank",
    "ADB": "ADB",
    "UNCTAD": "UNCTAD",
    "IMF": "IMF",
    "WTO": "WTO",
    "CIEM": "CIEM",
    "IFC": "IFC",
    "WIPO": "WIPO",
    "OECD": "OECD",
}


def extract_inline_citations(text: str) -> list[tuple[str, str]]:
    """Returns list of (author_raw, year) tuples from inline citations."""
    results = []
    for m in INLINE_CITE_RE.finditer(text):
        author = m.group(1).strip().rstrip(",")
        year = m.group(2).strip()
        results.append((author, year))
    return results


def normalize_author(raw: str) -> str:
    """Normalize author string for matching."""
    raw = raw.strip()
    # et al. → keep first author only
    raw = re.sub(r'\s+et al\.?', '', raw, flags=re.IGNORECASE)
    # Remove initials like "A., B."
    raw = re.sub(r',?\s+[A-Z]\.\s*(?:&\s*)?', ' ', raw)
    # Remove " & " and "and"
    raw = re.sub(r'\s*&\s*|\s+and\s+', ' ', raw)
    return raw.strip().lower()


def parse_reference_list(refs_text: str) -> dict[str, list[str]]:
    """
    Returns dict: normalized_first_author → list of years found.
    """
    result = defaultdict(list)
    for line in refs_text.splitlines():
        line = line.strip()
        if not line or line.startswith('#') or line.startswith('>') or line.startswith('---'):
            continue
        # Strip markdown bold markers (**...**) before matching
        line = re.sub(r'^\*+', '', line).strip()
        m = REF_ENTRY_RE.match(line)
        if m:
            author_raw = m.group(1).strip()
            year = m.group(2).strip()
            # Take first surname only (before first comma)
            first_surname = author_raw.split(',')[0].strip().lower()
            result[first_surname].append(year)
    return result


def check_citation_in_refs(
    author: str, year: str, ref_index: dict[str, list[str]]
) -> bool:
    """Try to match an inline citation against the reference index."""
    # Check alias expansion first
    expanded = author
    for abbrev, full in ALIASES.items():
        if abbrev.lower() in author.lower():
            expanded = full

    # Get first word of author (first surname)
    first_word = normalize_author(expanded).split()[0] if normalize_author(expanded).split() else ""

    if not first_word:
        return True  # Can't check, skip

    for ref_key in ref_index:
        if first_word in ref_key or ref_key in first_word:
            if year in ref_index[ref_key]:
                return True
    return False


def run(root: Path, manuscript_files: list[Path], refs_file: Path, show_orphans: bool):
    if not refs_file.exists():
        print(f"  ❌  Không tìm thấy file references: {refs_file}")
        sys.exit(1)

    refs_text = refs_file.read_text(encoding="utf-8")
    ref_index = parse_reference_list(refs_text)

    print(f"\n{'='*65}")
    print(f"  format-apa7.py — Kiểm tra cross-reference citations")
    print(f"{'='*65}")
    print(f"  References file: {refs_file.relative_to(root)}")
    print(f"  Entries trong refs: {sum(len(v) for v in ref_index.values())}")
    print(f"  Manuscripts: {len(manuscript_files)} file(s)\n")

    missing_total = 0
    all_inline: dict[str, set[tuple[str, str]]] = defaultdict(set)

    for mf in sorted(manuscript_files):
        if not mf.exists():
            continue
        text = mf.read_text(encoding="utf-8")
        citations = extract_inline_citations(text)
        file_missing = []

        for author, year in citations:
            all_inline[str(mf)].add((author, year))
            if not check_citation_in_refs(author, year, ref_index):
                file_missing.append((author, year))

        if file_missing:
            missing_total += len(file_missing)
            rel = mf.relative_to(root)
            print(f"  📄  {rel}")
            seen = set()
            for author, year in sorted(set(file_missing)):
                key = f"{author} ({year})"
                if key not in seen:
                    seen.add(key)
                    print(f"      ⚠️   Citation trong text KHÔNG CÓ trong refs: ({author}, {year})")
            print()

    if missing_total == 0:
        print("  ✅  Tất cả citations inline đều có entry trong references.\n")
    else:
        print(f"  ❌  Tổng: {missing_total} citation(s) không tìm thấy trong references.\n")

    # Orphan check: refs in file but never cited
    if show_orphans:
        print(f"\n{'─'*65}")
        print("  Refs trong danh mục nhưng chưa được cite (có thể bỏ):")
        cited_authors = set()
        for citations in all_inline.values():
            for author, year in citations:
                first = normalize_author(author).split()[0] if normalize_author(author).split() else ""
                cited_authors.add(first)

        orphans = []
        for ref_key, years in sorted(ref_index.items()):
            if ref_key not in cited_authors and not any(c in ref_key for c in cited_authors):
                for yr in years:
                    orphans.append(f"{ref_key} ({yr})")
        if orphans:
            for o in orphans[:20]:  # cap at 20 to avoid noise
                print(f"      • {o}")
            if len(orphans) > 20:
                print(f"      … và {len(orphans)-20} nữa")
        else:
            print("      (Không có refs thừa — tốt!)")
        print()

    return missing_total


def main():
    parser = argparse.ArgumentParser(description="Kiểm tra chéo citations APA7")
    parser.add_argument("--paper", help="Kiểm tra file manuscript cụ thể")
    parser.add_argument("--refs", help="File danh mục references (mặc định: thesis/04_references_apa7.md)")
    parser.add_argument("--orphans", action="store_true", help="Liệt kê refs thừa (có trong danh mục nhưng chưa cite)")
    parser.add_argument("--root", default=".", help="Thư mục gốc repo")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    refs_file = root / (args.refs or DEFAULT_REFS_FILE)

    if args.paper:
        files = [Path(args.paper).resolve()]
    else:
        files = [root / p for p in MANUSCRIPT_PATTERNS]

    missing = run(root, files, refs_file, args.orphans)
    sys.exit(1 if missing > 0 else 0)


if __name__ == "__main__":
    main()
