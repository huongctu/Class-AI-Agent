#!/usr/bin/env python3
"""
academic_language_check.py — Chuẩn hóa ngôn ngữ học thuật tiếng Anh trong manuscripts.

Kiểm tra:
  1. Hedging & academic register (quá informal, quá absolute claims)
  2. Passive/active voice balance
  3. First-person trong blind review sections
  4. Hedge words thiếu khi trình bày kết quả uncertain
  5. Informal contractions và colloquialisms
  6. Consistency trong verb tense (IMRaD conventions)
  7. Overuse of intensifiers (very, quite, really)
  8. Weak/vague academic phrases

Chạy:
  python3 scripts/academic_language_check.py --file manuscripts/p3_vietnam_en_clean.md
  python3 scripts/academic_language_check.py --file manuscripts/p3_vietnam_en_clean.md --suggest
"""

import re
import sys
import argparse
from pathlib import Path
from dataclasses import dataclass


# ─── Rule patterns ────────────────────────────────────────────────────────────
@dataclass
class LangRule:
    name: str
    pattern: str
    message: str
    suggestion: str
    severity: str       # "error" | "warning" | "info"
    ignore_sections: list  # skip in these section types


RULES: list[LangRule] = [
    # 1. Absolute claim without hedge
    LangRule(
        name="absolute_claim",
        pattern=r"\b(proves?|shows? that|demonstrates? that|confirms? that)\b",
        message="Absolute claim — academic writing requires hedging",
        suggestion="→ 'suggests that' / 'provides evidence that' / 'indicates that'",
        severity="warning",
        ignore_sections=["abstract", "conclusion"],
    ),
    # 2. Informal contractions
    LangRule(
        name="contraction",
        pattern=r"\b(don't|doesn't|can't|won't|isn't|aren't|wasn't|weren't|hasn't|haven't|it's|that's|we're|they're|there's)\b",
        message="Informal contraction in academic text",
        suggestion="→ expand: 'do not', 'cannot', 'it is'",
        severity="error",
        ignore_sections=[],
    ),
    # 3. Informal colloquials
    LangRule(
        name="colloquial",
        pattern=r"\b(a lot of|lots of|big|huge|tons of|kind of|sort of|a bit|pretty much|basically|you know|like,)\b",
        message="Colloquial expression",
        suggestion="→ 'a considerable number of' / 'substantially' / 'relatively'",
        severity="warning",
        ignore_sections=[],
    ),
    # 4. First-person in hypothesis/theory sections
    LangRule(
        name="first_person_theory",
        pattern=r"\b(I argue|I suggest|I propose|I believe|I think|I claim)\b",
        message="First-person singular in academic argument — use author(s) or passive",
        suggestion="→ 'This study argues' / 'The present study proposes' / passive voice",
        severity="warning",
        ignore_sections=["acknowledgements"],
    ),
    # 5. Overused intensifiers
    LangRule(
        name="intensifier",
        pattern=r"\b(very (important|significant|interesting|relevant|clear|strong)|really (important|shows|demonstrates)|quite (clear|obvious|evident))\b",
        message="Vague intensifier weakens academic precision",
        suggestion="→ use precise quantifiers or delete: 'significantly', 'substantially', 'notably'",
        severity="info",
        ignore_sections=[],
    ),
    # 6. Weak reference phrases
    LangRule(
        name="weak_reference",
        pattern=r"\b(some researchers|some studies|certain scholars|many people think)\b",
        message="Vague reference without citation",
        suggestion="→ cite specific author(s): 'Hitt et al. (1997) demonstrate...'",
        severity="warning",
        ignore_sections=[],
    ),
    # 7. Passive overuse in Results (should vary)
    LangRule(
        name="stacked_passive",
        pattern=r"(was found|were found|is shown|are shown|was observed|were observed|was noted|were noted).{0,30}(was found|were found|is shown|are shown)",
        message="Stacked passives — vary sentence structure",
        suggestion="→ alternate: 'Table 2 shows...' / 'The results indicate...'",
        severity="info",
        ignore_sections=[],
    ),
    # 8. Tense inconsistency markers (past in Methods is fine; present in Discussion)
    LangRule(
        name="future_in_results",
        pattern=r"\b(will be|will show|will demonstrate|will confirm|will indicate)\b",
        message="Future tense in Results/Discussion — use past or present",
        suggestion="→ 'was found' (past in results) / 'suggests' (present in discussion)",
        severity="warning",
        ignore_sections=["introduction", "methodology"],
    ),
    # 9. Redundant phrases
    LangRule(
        name="redundancy",
        pattern=r"\b(in order to|due to the fact that|at this point in time|in the event that|for the purpose of|with regard to the fact that)\b",
        message="Wordy/redundant phrase",
        suggestion="→ 'to' / 'because' / 'now' / 'if' / 'for' / 'regarding'",
        severity="info",
        ignore_sections=[],
    ),
    # 10. Overclaiming generalizability
    LangRule(
        name="overgeneralize",
        pattern=r"\b(all firms|all companies|every company|universally applicable|always true|never false)\b",
        message="Overgeneralization — scope claim too broad",
        suggestion="→ 'firms in our sample' / 'in the contexts examined' / 'for most firms'",
        severity="warning",
        ignore_sections=[],
    ),
    # 11. Confused hedges (double negative or awkward)
    LangRule(
        name="not_insignificant",
        pattern=r"\b(not insignificant|not unimportant|not uncommon|not unusual)\b",
        message="Double-negative hedge — imprecise",
        suggestion="→ 'significant' / 'important' / 'common' / 'notable'",
        severity="info",
        ignore_sections=[],
    ),
    # ── Author-voice rules (Đỗ Thúy Hương — PhD elevation) ──────────────────
    # 12. Direct hypothesis without conditional framing
    LangRule(
        name="unconditional_hypothesis",
        pattern=r"\bH\d[a-z]?[:\s].{0,60}(has a|have a|is|are) (positive|negative|significant) (impact|effect|influence|relationship)\b",
        message="Hypothesis lacks conditional framing — PhD register requires: 'under [condition], [mechanism] predicts...'",
        suggestion="→ 'H1: Under [condition], [mechanism] generates [expected direction] because [pathway]'",
        severity="warning",
        ignore_sections=["references", "appendix"],
    ),
    # 13. "Supports H1/H2/H3" without mechanism explanation
    LangRule(
        name="bare_hypothesis_support",
        pattern=r"\b(supports?|confirms?|validates?)\s+H\d[a-z]?\b",
        message="'Supports H[n]' without mechanism — state the coefficient and theoretical pathway",
        suggestion="→ 'β = [value] (p = [p]), consistent with H[n]: [mechanism explanation]'",
        severity="warning",
        ignore_sections=["abstract", "conclusion", "references"],
    ),
    # 14. Single-mechanism claims ("X helps Y") without pathway
    LangRule(
        name="single_mechanism_vague",
        pattern=r"\b(helps?|enables?|allows?|lets?)\s+(firms?|companies|businesses|managers?|organizations?)\s+(to\s+)?(overcome|improve|enhance|achieve|increase|reduce)\b",
        message="Single-mechanism claim without theoretical pathway — name the mechanism and cite it",
        suggestion="→ 'reduces [specific cost] through [pathway] (Author, Year)' not 'helps firms improve'",
        severity="warning",
        ignore_sections=["introduction", "references", "appendix"],
    ),
    # 15. Limitation as afterthought bullet without remedy
    LangRule(
        name="limitation_no_remedy",
        pattern=r"^\s*[-*]\s*(1\.|2\.|3\.|first,?|second,?|third,?|one limitation|a limitation|the (main|key|primary|major) limitation)",
        message="Limitation bullet without inferential bound + remedy — integrate as prose with methodological solution",
        suggestion="→ 'First, [what cannot be concluded] because [source]. Future work using [method] would resolve [specific ambiguity]'",
        severity="info",
        ignore_sections=["references", "appendix"],
    ),
    # 16. "More research is needed" without specification
    LangRule(
        name="vague_future_research",
        pattern=r"\b(more research (is|are) needed|future (studies|research|work) (should|could|might|may|would) (examine|investigate|explore|consider|look at))\b",
        message="Vague future-research call — specify mechanism, method, and ambiguity to be resolved",
        suggestion="→ 'Future work using [method] would resolve [ambiguity] by [mechanism of resolution]'",
        severity="warning",
        ignore_sections=["references"],
    ),
    # 17. "Contrasts with [X]" without context-specific reconciliation
    LangRule(
        name="unreconciled_contrast",
        pattern=r"\b(contrasts? with|differs? from|inconsistent with|contradicts?)\s+[A-ZÀÁÂÃÈÉÊÌÍÒÓÔÕÙÚÝĐ][a-zàáâãèéêìíòóôõùúýđ]+.{0,40}\(\d{4}\)",
        message="Contrast with prior work not reconciled — explain the divergence via boundary condition or context difference",
        suggestion="→ 'The divergence from [Author, Year] is interpretable: [context difference] shifts [mechanism], predicting [different outcome]'",
        severity="info",
        ignore_sections=["references", "appendix"],
    ),
    # ── Transparency rules (Aguinis et al., 2019; Meyer et al., 2017) ─────────
    # 18. Bare "significant" without "statistically" (Meyer et al., 2017)
    LangRule(
        name="bare_significant",
        pattern=r"(?<!\bstatistically\s)\b(is|are|was|were|becomes?|remained?)\s+significant\b(?!\s+in\s+the\s+sense)",
        message="'Significant' without 'statistically' — use 'statistically significant' per Meyer et al. (2017)",
        suggestion="→ 'statistically significant (p = [exact value])' — never 'significant', 'highly significant', 'marginally significant'",
        severity="warning",
        ignore_sections=["references", "appendix"],
    ),
    # 19. "Marginally/almost/nearly/highly significant" — anti-pattern (Meyer et al., 2017)
    LangRule(
        name="qualified_significant",
        pattern=r"\b(marginally|almost|nearly|borderline|quasi|highly|weakly)\s+(statistically\s+)?significant\b",
        message="'[Qualifier] significant' is not a valid statistical category (Meyer et al., 2017)",
        suggestion="→ Report exact p-value: 'p = 0.07' not 'marginally significant'; 'p = 0.001' not 'highly significant'",
        severity="error",
        ignore_sections=["references", "appendix"],
    ),
    # 20. Asterisk-based significance reporting (Aguinis et al., 2019; Meyer et al., 2017)
    LangRule(
        name="asterisk_significance",
        pattern=r"[*†]{1,3}\s*p\s*[<≤]\s*[0-9.]+|p\s*[<≤]\s*[0-9.]+\s*[*†]{1,3}|\bsignificant at the\s+(0\.\d+|[0-9]+%)\s+level",
        message="Asterisk/cutoff-based p-reporting — use exact p-values (Aguinis et al., 2019; Meyer et al., 2017)",
        suggestion="→ Replace '***p < .001' with 'p = [exact value, e.g., p = .003]'",
        severity="warning",
        ignore_sections=["references", "appendix"],
    ),
]

# ─── IMRaD tense conventions ──────────────────────────────────────────────────
SECTION_TENSE = {
    "abstract":     "mixed — past for methods/results, present for implications",
    "introduction": "present for claims, present perfect for lit review",
    "methodology":  "past tense throughout",
    "results":      "past tense for findings; present for tables/figures",
    "discussion":   "present tense for interpretation",
    "conclusion":   "present tense",
}

# ─── Hedge word checker ───────────────────────────────────────────────────────
RESULT_CLAIM_PATTERNS = [
    r"\b(supports? H[1-9]|confirms? the hypothesis|validates? the model)\b",
    r"\b(β[₁₂₃]?|beta|coefficient).*?(is|are|was|were) (positive|negative|significant)\b",
    r"\b(turning point|inflection point) (is|was) (at|approximately|around)\b",
]

HEDGE_WORDS = [
    "suggests", "indicates", "appears", "seems", "may", "might", "could",
    "partially", "tentatively", "provides evidence", "consistent with",
    "in line with", "arguably", "as hypothesized"
]


def detect_section(line: str) -> str | None:
    """Return section type from markdown heading."""
    m = re.match(r'^#{1,3}\s+\d*\.?\s*(.*)', line.strip())
    if not m:
        return None
    title = m.group(1).lower()
    for sec in ["abstract", "introduction", "methodology", "method",
                "results", "discussion", "conclusion", "acknowledgement",
                "references", "appendix"]:
        if sec in title:
            return sec
    return None


def check_result_hedging(line: str, line_no: int) -> list[dict]:
    issues = []
    for pat in RESULT_CLAIM_PATTERNS:
        if re.search(pat, line, re.IGNORECASE):
            line_lower = line.lower()
            has_hedge = any(h in line_lower for h in HEDGE_WORDS)
            if not has_hedge:
                issues.append({
                    "line_no": line_no,
                    "rule": "missing_hedge",
                    "severity": "warning",
                    "message": "Result claim without hedge word",
                    "suggestion": "→ Add hedge: 'suggests', 'indicates', 'is consistent with', 'as hypothesized'",
                    "line": line.strip()[:100],
                })
    return issues


@dataclass
class Issue:
    line_no: int
    rule: str
    severity: str
    message: str
    suggestion: str
    line: str


def scan_file(path: Path, suggest: bool = False) -> list[Issue]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    issues = []
    current_section = "body"

    for i, line in enumerate(lines, 1):
        # Track current section
        sec = detect_section(line)
        if sec:
            current_section = sec
            continue

        # Skip code blocks, tables, reference entries
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("|") or \
           stripped.startswith("http") or re.match(r'^[A-ZÀ-Ỵ][a-z]+.*\(\d{4}\)', stripped):
            continue

        # Apply rules
        for rule in RULES:
            if current_section in rule.ignore_sections:
                continue
            if re.search(rule.pattern, line, re.IGNORECASE):
                issues.append(Issue(
                    line_no=i,
                    rule=rule.name,
                    severity=rule.severity,
                    message=rule.message,
                    suggestion=rule.suggestion if suggest else "",
                    line=stripped[:100],
                ))

        # Hedge check for result claims
        for h_issue in check_result_hedging(line, i):
            issues.append(Issue(
                line_no=h_issue["line_no"],
                rule=h_issue["rule"],
                severity=h_issue["severity"],
                message=h_issue["message"],
                suggestion=h_issue["suggestion"] if suggest else "",
                line=h_issue["line"],
            ))

    return issues


def main():
    parser = argparse.ArgumentParser(description="Kiểm tra ngôn ngữ học thuật tiếng Anh")
    parser.add_argument("--file", required=True, help="File manuscript .md cần kiểm tra")
    parser.add_argument("--suggest", action="store_true", help="Hiển thị đề xuất sửa lỗi")
    parser.add_argument("--min-severity", default="info",
                        choices=["info", "warning", "error"], help="Mức tối thiểu hiển thị")
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"  ❌  File không tồn tại: {path}")
        sys.exit(1)

    severity_rank = {"info": 0, "warning": 1, "error": 2}
    min_rank      = severity_rank[args.min_severity]

    issues = scan_file(path, suggest=args.suggest)
    issues = [iss for iss in issues if severity_rank[iss.severity] >= min_rank]

    # Count by severity
    n_err  = sum(1 for i in issues if i.severity == "error")
    n_warn = sum(1 for i in issues if i.severity == "warning")
    n_info = sum(1 for i in issues if i.severity == "info")

    print(f"\n{'='*65}")
    print(f"  academic_language_check.py")
    print(f"{'='*65}")
    print(f"  File:     {path.name}")
    print(f"  Issues:   {n_err} errors | {n_warn} warnings | {n_info} info")
    print(f"{'='*65}\n")

    if not issues:
        print("  ✅  Không phát hiện vấn đề ngôn ngữ học thuật.\n")
        sys.exit(0)

    icon_map = {"error": "❌", "warning": "⚠️ ", "info": "ℹ️ "}

    # Group by rule category
    by_rule: dict[str, list[Issue]] = {}
    for iss in issues:
        by_rule.setdefault(iss.rule, []).append(iss)

    for rule_name, rule_issues in sorted(by_rule.items()):
        first = rule_issues[0]
        print(f"  {icon_map[first.severity]} [{first.rule}] — {first.message}")
        if args.suggest and first.suggestion:
            print(f"      {first.suggestion}")
        for iss in rule_issues[:3]:
            print(f"      Dòng {iss.line_no:4d}: {iss.line[:90]}")
        if len(rule_issues) > 3:
            print(f"      ... và {len(rule_issues)-3} trường hợp khác")
        print()

    # IMRaD tense guide
    print(f"  📝  Quy tắc thì động từ theo IMRaD:")
    for sec, guide in SECTION_TENSE.items():
        print(f"      {sec:<15} {guide}")
    print()

    sys.exit(1 if n_err > 0 else 0)


if __name__ == "__main__":
    main()
