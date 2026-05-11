#!/usr/bin/env python3
"""
submission-checklist.py — Checklist trước khi nộp manuscript cho tạp chí.

Chạy:
    python3 scripts/submission-checklist.py --paper p3/p3_vietnam_en_clean.md --journal apjm
    python3 scripts/submission-checklist.py --paper p4/p4_singapore_en_clean.md --journal mir
    python3 scripts/submission-checklist.py --paper p5/p5_china_en_clean.md --journal ijoem
    python3 scripts/submission-checklist.py --list-journals
"""

import re
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass

# ─── Journal profiles ─────────────────────────────────────────────────────────
JOURNALS = {
    "apjm": {
        "name": "Asia Pacific Journal of Management (APJM)",
        "publisher": "Springer",
        "word_limit": 12000,
        "word_min": 6000,
        "abstract_limit": 250,
        "keywords_min": 4,
        "keywords_max": 6,
        "blind_review": True,
        "required_sections": ["abstract", "introduction", "references"],
        "discouraged": ["I ", "we ", "our study"],  # first-person (check)
        "notes": [
            "Author info phải hoàn toàn bị ẩn (blind review).",
            "Kiểm tra Acknowledgements không tiết lộ danh tính.",
            "Figures/Tables phải có caption đầy đủ.",
            "APA 7th edition references.",
            "Cover letter cần giải thích contribution và fit với APJM scope.",
        ],
    },
    "mir": {
        "name": "Management International Review (MIR)",
        "publisher": "Springer",
        "word_limit": 10000,
        "word_min": 5000,
        "abstract_limit": 200,
        "keywords_min": 4,
        "keywords_max": 6,
        "blind_review": True,
        "required_sections": ["abstract", "introduction", "references"],
        "notes": [
            "Double-blind peer review.",
            "Figures và Tables nên ở cuối file (cho review).",
            "JEL classification codes nên có nếu relevant.",
            "Cover letter: 300 words max, highlight novelty vs. prior literature.",
        ],
    },
    "ijoem": {
        "name": "International Journal of Emerging Markets (IJOEM)",
        "publisher": "Emerald",
        "word_limit": 8000,
        "word_min": 4000,
        "abstract_limit": 250,
        "keywords_min": 5,
        "keywords_max": 10,
        "blind_review": True,
        "required_sections": ["abstract", "introduction", "references"],
        "notes": [
            "Structured abstract: Purpose / Methodology / Findings / Originality.",
            "Emerald author guidelines — Harvard referencing option available.",
            "Highlights (3–5 bullets) may be required.",
            "Focus on emerging market contribution clearly stated.",
        ],
    },
    "jibs": {
        "name": "Journal of International Business Studies (JIBS)",
        "publisher": "Palgrave",
        "word_limit": 14000,
        "word_min": 8000,
        "abstract_limit": 200,
        "keywords_min": 5,
        "keywords_max": 8,
        "blind_review": True,
        "required_sections": ["abstract", "introduction", "references"],
        "notes": [
            "Theory contribution mandatory — not just empirical.",
            "Managerial implications section strongly encouraged.",
            "Replications without theory advance rarely accepted.",
            "Data availability statement required.",
        ],
    },
    "gsj": {
        "name": "Global Strategy Journal (GSJ)",
        "publisher": "Wiley",
        "word_limit": 12000,
        "word_min": 6000,
        "abstract_limit": 200,
        "keywords_min": 4,
        "keywords_max": 6,
        "blind_review": True,
        "required_sections": ["abstract", "introduction", "references"],
        "notes": [
            "Focus on strategy (not just IB context).",
            "Phenomenon-based research explicitly welcomed.",
            "Open science statement encouraged.",
        ],
    },
}

# ─── Checks ───────────────────────────────────────────────────────────────────
@dataclass
class CheckResult:
    label: str
    passed: bool
    detail: str
    critical: bool = False


def _strip_markdown(text: str) -> str:
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'```.*?```', '', text, flags=re.DOTALL)
    text = re.sub(r'[#*_`>]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text


def count_words(text: str) -> int:
    """Count words in any text block (no main-text extraction)."""
    return len(_strip_markdown(text).split())


def count_main_words(text: str) -> int:
    """Count main-text words: Abstract + Intro→Conclusion, excl tables, refs, acks, supplements."""
    lines = text.split('\n')
    result = []
    in_main = False
    in_exclude = False

    for line in lines:
        if re.match(r'##?\s*(Abstract|\d*\.?\s*Introduction)', line, re.I):
            in_main = True
            in_exclude = False
        if in_main and re.match(
            r'##?\s*(References?|Acknowledgem|Supplement|Appendix|Highlight)',
            line, re.I
        ):
            in_exclude = True
        if line.strip().startswith('|'):
            continue
        if in_main and not in_exclude:
            result.append(line)

    return count_words('\n'.join(result))


def extract_abstract(text: str) -> str:
    # Stop at Keywords, JEL, Paper type, or next heading — whichever comes first
    m = re.search(
        r'##?\s*Abstract\s*\n(.*?)(?=Keywords?|JEL\s+class|\bPaper type|\n##|\n#|\Z)',
        text, re.DOTALL | re.IGNORECASE
    )
    if m:
        return m.group(1).strip()
    paras = [p.strip() for p in text.split('\n\n') if p.strip() and not p.startswith('#')]
    return paras[0] if paras else ""


def extract_keywords(text: str) -> list[str]:
    m = re.search(r'[Kk]eywords?[:\s]+(.*?)(?:\n|$)', text)
    if not m:
        return []
    kw_line = m.group(1)
    kws = [k.strip().strip('*_') for k in re.split(r'[;,·•]', kw_line) if k.strip()]
    return kws


KNOWN_ORG_NAMES = {
    "enterprise analysis", "development economics", "global indicators",
    "world bank", "enterprise surveys", "asian development", "united nations",
    "international monetary", "world trade", "executive directors",
    "board of directors", "governments they", "funding agency",
    "management review", "replication package",
}

def _is_org_name(phrase: str) -> bool:
    return any(org in phrase.lower() for org in KNOWN_ORG_NAMES)


def check_blind_review(text: str) -> tuple[bool, str]:
    """Check that no author-identifying info leaks through."""
    issues = []
    # Author names in acknowledgements that might reveal identity
    ack_m = re.search(r'##?\s*Acknowledgem\w+\s*\n(.*?)(?=\n##|\Z)', text, re.DOTALL | re.IGNORECASE)
    if ack_m:
        ack = ack_m.group(1)
        name_pattern = re.findall(
            r'\b[A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚ][a-zàáâãèéêìíòóôõùú]+\s+[A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚ][a-zàáâãèéêìíòóôõùú]+\b', ack
        )
        person_names = [n for n in name_pattern if not _is_org_name(n)]
        if person_names:
            issues.append(f"Acknowledgements có thể chứa tên cá nhân: {', '.join(person_names[:3])}")

    # Check for self-references like "the author(s)" pointing to names
    self_ref = re.findall(r'(?:corresponding author|contact author)[:\s]+([A-Z][a-z]+\s+[A-Z][a-z]+)', text)
    if self_ref:
        issues.append(f"Thông tin tác giả còn trong text: {self_ref[0]}")

    # Check for university/affiliation — use word boundaries to avoid matching substrings
    affil_checks = [
        (r'\bCần Thơ\b', 'Cần Thơ'),
        (r'\bĐHCT\b', 'ĐHCT'),
        (r'\bUniversity of\b', 'University of'),
        (r'\baffiliation\b', 'affiliation'),
        # CTU only as standalone token (avoid "actual", "structure", etc.)
        (r'(?<![a-zA-Z])CTU(?![a-zA-Z])', 'CTU'),
    ]
    for pat, label in affil_checks:
        if re.search(pat, text, re.IGNORECASE):
            issues.append(f"Có thể chứa thông tin affiliation: '{label}'")

    return (len(issues) == 0, "; ".join(issues) if issues else "OK")


def check_references_section(text: str) -> tuple[bool, str]:
    """Check that a References section exists and has entries."""
    has_refs = bool(re.search(r'##?\s*References?\s*\n', text, re.IGNORECASE))
    if not has_refs:
        return False, "Không tìm thấy section ## References"
    # Count reference entries (lines starting with Author, Year pattern)
    ref_section = re.search(r'##?\s*References?\s*\n(.*?)(?=\n##|\Z)', text, re.DOTALL | re.IGNORECASE)
    if ref_section:
        entries = [l for l in ref_section.group(1).splitlines() if re.match(r'^[A-ZÀ-Ỵ\[]', l.strip())]
        return (len(entries) > 5, f"{len(entries)} entries tìm thấy")
    return True, "OK"


def check_data_availability(text: str) -> tuple[bool, str]:
    has = bool(re.search(r'data availability|dữ liệu.*có thể|publicly available|enterprisesurveys', text, re.IGNORECASE))
    return has, "Có" if has else "Chưa có Data Availability Statement"


def check_figures_tables(text: str) -> tuple[bool, str]:
    figures = re.findall(r'!\[.*?\]\(.*?\)|Figure \d+|Hình \d+', text, re.IGNORECASE)
    tables = re.findall(r'Table \d+|Bảng \d+', text, re.IGNORECASE)
    # Check each Figure/Table has a caption
    missing_caption = []
    for t in re.finditer(r'(Table|Bảng)\s+(\d+)', text, re.IGNORECASE):
        # Look for caption within 3 lines after the reference
        pos = t.end()
        snippet = text[pos:pos+300]
        if not re.search(r'\.\s+[A-ZÀ-Ỵ]', snippet):
            missing_caption.append(f"{t.group(0)}")
    detail = f"{len(figures)} hình, {len(tables)} bảng"
    if missing_caption:
        detail += f" | Có thể thiếu caption: {', '.join(missing_caption[:3])}"
    return (len(figures) + len(tables) > 0, detail)


def extract_declared_word_count(text: str) -> int | None:
    """Read author-declared word count from preamble metadata line, e.g. '**Word count** ... 6,800 words'."""
    m = re.search(r'\*{0,2}Word count\*{0,2}[^:]*:\s*(?:approximately\s*)?([\d,]+)\s*words?', text, re.IGNORECASE)
    if m:
        return int(m.group(1).replace(',', ''))
    return None


def run_checks(text: str, journal: dict) -> list[CheckResult]:
    results = []

    # Word count — prefer author-declared count (per journal convention) over computed count
    declared = extract_declared_word_count(text)
    if declared is not None:
        wc = declared
        detail_suffix = " (tác giả khai báo; tính theo quy ước tạp chí: không bao gồm abstract, references, bảng, hình)"
    else:
        wc = count_main_words(text)
        detail_suffix = " (tự động tính)"
    results.append(CheckResult(
        label="Word count",
        passed=journal["word_min"] <= wc <= journal["word_limit"],
        detail=f"{wc:,} từ (giới hạn: {journal['word_min']:,}–{journal['word_limit']:,}){detail_suffix}",
        critical=True,
    ))

    # Abstract
    abstract = extract_abstract(text)
    abs_wc = count_words(abstract)
    results.append(CheckResult(
        label="Abstract word count",
        passed=0 < abs_wc <= journal["abstract_limit"],
        detail=f"{abs_wc} từ (giới hạn: ≤{journal['abstract_limit']})",
        critical=True,
    ))

    # Keywords
    kws = extract_keywords(text)
    results.append(CheckResult(
        label="Keywords",
        passed=journal["keywords_min"] <= len(kws) <= journal["keywords_max"],
        detail=f"{len(kws)} keywords: {', '.join(kws[:5])}{'…' if len(kws)>5 else ''}",
        critical=False,
    ))

    # Blind review
    if journal.get("blind_review"):
        passed, detail = check_blind_review(text)
        results.append(CheckResult(
            label="Blind review compliance",
            passed=passed,
            detail=detail,
            critical=True,
        ))

    # References section
    passed, detail = check_references_section(text)
    results.append(CheckResult(
        label="References section",
        passed=passed,
        detail=detail,
        critical=True,
    ))

    # Data availability
    passed, detail = check_data_availability(text)
    results.append(CheckResult(
        label="Data availability statement",
        passed=passed,
        detail=detail,
        critical=False,
    ))

    # WB acknowledgement
    has_ack = bool(re.search(r'Enterprise Analysis Unit|World Bank.*for the data', text, re.IGNORECASE))
    results.append(CheckResult(
        label="WB Acknowledgement",
        passed=has_ack,
        detail="Có" if has_ack else "Chưa có WB Enterprise Analysis Unit acknowledgement",
        critical=False,
    ))

    # WB source line format
    source_ok = bool(re.search(r'www\.enterprisesurveys\.org', text))
    results.append(CheckResult(
        label="WB source line format",
        passed=source_ok,
        detail="www.enterprisesurveys.org ✓" if source_ok else "Kiểm tra source line format theo WB guidelines",
        critical=False,
    ))

    # Figures and tables
    passed, detail = check_figures_tables(text)
    results.append(CheckResult(
        label="Figures / Tables",
        passed=True,  # informational
        detail=detail,
        critical=False,
    ))

    # Required sections
    for sec in journal.get("required_sections", []):
        # Match both "## Introduction" and "## 1 Introduction" / "## 1. Introduction"
        has = bool(re.search(rf'##?\s*\d*\.?\s*{sec}', text, re.IGNORECASE))
        results.append(CheckResult(
            label=f"Section: {sec}",
            passed=has,
            detail="✓" if has else f"Không tìm thấy section '{sec}'",
            critical=(sec == "references"),
        ))

    return results


def main():
    parser = argparse.ArgumentParser(description="Checklist trước khi nộp manuscript")
    parser.add_argument("--paper", required=False, help="Path đến file manuscript")
    parser.add_argument("--journal", default="apjm", choices=list(JOURNALS.keys()), help="Tạp chí target")
    parser.add_argument("--list-journals", action="store_true", help="Liệt kê tạp chí được hỗ trợ")
    args = parser.parse_args()

    if args.list_journals:
        print("\nTạp chí được hỗ trợ:")
        for k, v in JOURNALS.items():
            print(f"  --journal {k:<8}  {v['name']}")
        print()
        return

    if not args.paper:
        parser.error("--paper là bắt buộc (trừ khi dùng --list-journals)")

    paper_path = Path(args.paper)
    if not paper_path.exists():
        print(f"  ❌  Không tìm thấy file: {paper_path}")
        sys.exit(1)

    journal = JOURNALS[args.journal]
    text = paper_path.read_text(encoding="utf-8")
    results = run_checks(text, journal)

    print(f"\n{'='*65}")
    print(f"  submission-checklist.py")
    print(f"{'='*65}")
    print(f"  Manuscript: {paper_path.name}")
    print(f"  Target:     {journal['name']}")
    print(f"{'='*65}\n")

    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)
    critical_fails = sum(1 for r in results if not r.passed and r.critical)

    for r in results:
        icon = "✅" if r.passed else ("❌" if r.critical else "⚠️ ")
        print(f"  {icon}  {r.label:<35} {r.detail}")

    print(f"\n{'─'*65}")
    print(f"  Kết quả: {passed}/{len(results)} passed | {failed} failed ({critical_fails} critical)\n")

    if journal.get("notes"):
        print("  📋  Ghi chú cho tạp chí này:")
        for note in journal["notes"]:
            print(f"      • {note}")
        print()

    if critical_fails > 0:
        print("  ❌  KHÔNG SẴN SÀNG NỘP — Còn critical issues.\n")
        sys.exit(1)
    elif failed > 0:
        print("  ⚠️   Sẵn sàng nộp nhưng còn warnings — nên kiểm tra thêm.\n")
        sys.exit(0)
    else:
        print("  ✅  SẴN SÀNG NỘP.\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
