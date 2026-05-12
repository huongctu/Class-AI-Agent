#!/usr/bin/env python3
"""
check-consistency.py — Kiểm tra nhất quán số liệu cốt lõi xuyên manuscripts + thesis.

Chạy từ thư mục gốc repo:
    python3 scripts/check-consistency.py
    python3 scripts/check-consistency.py --fix-report   # xuất báo cáo markdown
    python3 scripts/check-consistency.py --file manuscripts/p3_vietnam_en_clean.md
"""

import re
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import Optional

# ─── Canonical figures ────────────────────────────────────────────────────────
CANONICAL = {
    # CĐ1 / CĐ2 pool
    "pool_firms":          {"values": ["101.185", "101,185"], "wrong": ["101.035", "101,035", "101.135", "101,135"], "label": "Pool firms (CĐ1/CĐ2)"},
    "pool_economies":      {"values": ["47 nền kinh tế", "47 economies", "47 economies"], "wrong": ["48 nền", "46 nền"], "label": "47 economies"},
    "pool_country_year":   {"values": ["108 cặp", "108 country-year"], "wrong": ["107 cặp", "109 cặp"], "label": "108 country-year pairs"},
    "pool_waves":          {"values": ["14 mốc", "14 survey waves", "14 đợt"], "wrong": ["13 mốc", "15 mốc"], "label": "14 survey waves"},
    # ICRV groups — must sum to 47
    "icrv_sum_check":      {"values": ["5+5+6+7+17+7"], "wrong": [], "label": "ICRV sum 5+5+6+7+17+7=47"},
    # P3 Vietnam
    "p3_n":                {"values": ["N=2,958", "N = 2,958", "2,958 firm", "2.958 doanh"], "wrong": ["N=2958", "N=2.858", "N=2,968"], "label": "P3 N=2,958"},
    "p3_tp":               {"values": ["39.*46.*%", "39–46%", "39-46%"], "wrong": [], "label": "P3 turning points 39–46% FSTS"},
    "p3_lm":               {"values": ["p.*\\.013", "p<.013", "p = .013", "p<0.013"], "wrong": [], "label": "P3 Lind-Mehlum p<.013"},
    # P4 Singapore
    "p4_n":                {"values": ["N = 623", "N=623", "623 firm"], "wrong": ["N=632", "N=613"], "label": "P4 N=623"},
    "p4_n_m8":             {"values": ["N = 617", "N=617", "617"], "wrong": ["N=671", "N=716"], "label": "P4 M8 N=617"},
    "p4_tp":               {"values": ["88\\.6", "88.6%"], "wrong": ["86.8", "88.9"], "label": "P4 turning point ~88.6%"},
    "p4_lm":               {"values": ["p.*\\.303", "p = .303", "p=.303"], "wrong": [], "label": "P4 Lind-Mehlum p=.303"},
    # P5 China
    "p5_n_2012":           {"values": ["2,610", "2.610", "N.*2,610"], "wrong": ["2,601", "2,160"], "label": "P5 N=2,610 (2012)"},
    "p5_n_2024":           {"values": ["1,934", "1.934"], "wrong": ["1,943", "1,394"], "label": "P5 N=1,934 (2024)"},
    "p5_n_pooled":         {"values": ["4,544", "4.544"], "wrong": ["4,454", "4,445"], "label": "P5 N=4,544 (pooled)"},
    "p5_tp_2012":          {"values": ["49\\.4", "49.4%"], "wrong": ["49.6", "47.4"], "label": "P5 TP=49.4% (2012)"},
    "p5_tp_2024":          {"values": ["47\\.2", "47.2%"], "wrong": ["47.4", "72.4"], "label": "P5 TP=47.2% (2024)"},
    "p5_tp_pooled":        {"values": ["48\\.8", "48.8%"], "wrong": ["48.6", "84.8"], "label": "P5 TP=48.8% (pooled)"},
    "p5_paternoster_fsts": {"values": ["z.*\\.82", "p.*\\.412", "z = .82", "z=.82"], "wrong": [], "label": "P5 Paternoster FSTS z=.82 p=.412"},
    "p5_paternoster_fsts2":{"values": ["z.*\\.61", "p.*\\.545", "z = .61", "z=.61"], "wrong": [], "label": "P5 Paternoster FSTS² z=.61 p=.545"},
    # P6 meta-analysis
    "p6_k":                {"values": ["k.*=.*113", "k=113", "k = 113"], "wrong": ["k=112", "k=114"], "label": "P6 k=113 studies"},
    "p6_r":                {"values": ["r.*=.*0\\.07", "r = 0.07", "r=0.07"], "wrong": ["r=0.7", "r = 0.7"], "label": "P6 r=0.07"},
    "p6_i2":               {"values": ["87\\.92", "I².*87\\.92", "I2.*87\\.92"], "wrong": ["87.29", "97.82"], "label": "P6 I²=87.92%"},
    # Theoretical constructs — naming consistency
    "dai_name":            {"values": ["DAI_z", "DAI"], "wrong": ["TCI_thin"], "label": "DAI construct name (not TCI_thin)"},
}

# Files to check (relative to repo root)
DEFAULT_PATTERNS = [
    "p3/*.md",
    "p4/*.md",
    "p5/*.md",
    "p5/versions/apjm/*.md",
    "p6/*.md",
    "chuyen_de/cd1/*.md",
    "chuyen_de/cd2/*.md",
    "thesis/*.md",
    "writing_guides/*.md",
]

@dataclass
class Finding:
    file: str
    line_no: int
    line: str
    key: str
    kind: str  # "wrong_value" | "possible_inconsistency"
    detail: str

def _skip_line(line: str) -> bool:
    """Return True for lines where false positives are expected."""
    s = line.strip()
    # DOI / URL lines
    if re.search(r'https?://doi\.org|https?://|doi\.org', s):
        return True
    # Historical version notes (e.g., "cập nhật từ 101.035")
    if re.search(r'cập nhật từ|updated from|formerly|previous version', s, re.IGNORECASE):
        return True
    # Robustness spec row labels (e.g., "| R2: TCI_thin |")
    if re.match(r'\|\s*R\d+:', s):
        return True
    return False


def scan_file(path: Path) -> list[Finding]:
    findings = []
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  [SKIP] Cannot read {path}: {e}")
        return findings

    lines = text.splitlines()
    for key, rule in CANONICAL.items():
        for i, line in enumerate(lines, 1):
            if _skip_line(line):
                continue
            # Check for explicitly wrong values (literal string match, not regex)
            for wrong in rule.get("wrong", []):
                if re.search(re.escape(wrong), line, re.IGNORECASE):
                    findings.append(Finding(
                        file=str(path),
                        line_no=i,
                        line=line.strip()[:120],
                        key=key,
                        kind="wrong_value",
                        detail=f"Found wrong value matching '{wrong}' — expected: {rule['label']}",
                    ))
    return findings


def run_checks(root: Path, files: Optional[list[Path]] = None) -> tuple[list[Finding], int]:
    if files is None:
        files = []
        for pat in DEFAULT_PATTERNS:
            files.extend(root.glob(pat))

    all_findings = []
    checked = 0
    for f in sorted(set(files)):
        if not f.is_file():
            continue
        checked += 1
        found = scan_file(f)
        all_findings.extend(found)
    return all_findings, checked


def main():
    parser = argparse.ArgumentParser(description="Kiểm tra nhất quán số liệu cốt lõi")
    parser.add_argument("--file", help="Chỉ kiểm tra file cụ thể này")
    parser.add_argument("--fix-report", action="store_true", help="Xuất báo cáo markdown")
    parser.add_argument("--root", default=".", help="Thư mục gốc repo (mặc định: .)")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    target_files = [Path(args.file)] if args.file else None
    findings, checked = run_checks(root, target_files)

    print(f"\n{'='*65}")
    print(f"  check-consistency.py — Báo cáo nhất quán số liệu")
    print(f"{'='*65}")
    print(f"  Kiểm tra: {checked} file(s)")
    print(f"  Phát hiện: {len(findings)} vấn đề")
    print(f"{'='*65}\n")

    if not findings:
        print("  ✅  Không phát hiện số liệu không nhất quán.\n")
        sys.exit(0)

    # Group by file
    by_file: dict[str, list[Finding]] = {}
    for f in findings:
        by_file.setdefault(f.file, []).append(f)

    for filepath, flist in sorted(by_file.items()):
        rel = Path(filepath).relative_to(root) if root in Path(filepath).parents else filepath
        print(f"  📄  {rel}")
        for f in flist:
            icon = "❌" if f.kind == "wrong_value" else "⚠️ "
            print(f"      {icon} Dòng {f.line_no:4d}: {f.detail}")
            print(f"           → {f.line[:100]}")
        print()

    if args.fix_report:
        report_path = root / "scripts" / "consistency-report.md"
        lines = ["# Báo cáo nhất quán số liệu\n", f"Kiểm tra: {checked} file(s) — {len(findings)} vấn đề\n\n"]
        for filepath, flist in sorted(by_file.items()):
            rel = Path(filepath).relative_to(root) if root in Path(filepath).parents else filepath
            lines.append(f"## `{rel}`\n\n")
            for f in flist:
                lines.append(f"- **Dòng {f.line_no}**: {f.detail}\n")
                lines.append(f"  ```\n  {f.line[:120]}\n  ```\n")
            lines.append("\n")
        report_path.write_text("".join(lines), encoding="utf-8")
        print(f"  📋  Báo cáo đã lưu: {report_path}\n")

    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
