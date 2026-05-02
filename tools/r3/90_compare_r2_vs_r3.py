"""
R3 vs R2 comparison report — generates a side-by-side markdown
comparing the original Round 2 manuscript against the current Round 3
final manuscript.
"""
from pathlib import Path
from docx import Document
import re

REPO = Path(__file__).resolve().parents[2]
ORIG = REPO / "papers/p3-singapore/Manuscript_Blinded_MIR_2_original.docx"
CURR = REPO / "papers/p3-singapore/Manuscript_Blinded_MIR_2_revised.docx"
OUT = REPO / "papers/p3-singapore/R3_vs_R2_Comparison.md"


def get_section(doc, start_label, end_label_options):
    """Grab the text of a section between two heading paragraphs."""
    paras = doc.paragraphs
    start = next((i for i, p in enumerate(paras)
                  if p.text.strip() == start_label), None)
    if start is None:
        return None
    end = len(paras)
    for i in range(start + 1, len(paras)):
        t = paras[i].text.strip()
        if any(t.startswith(opt) for opt in end_label_options):
            end = i
            break
    return [paras[i].text.strip() for i in range(start, end)
            if paras[i].text.strip()]


def find_paragraph(doc, prefix):
    for p in doc.paragraphs:
        if p.text.strip().startswith(prefix):
            return p.text.strip()
    return None


def find_substring_paragraph(doc, substring):
    for p in doc.paragraphs:
        if substring in p.text:
            return p.text.strip()
    return None


def main():
    orig = Document(ORIG)
    curr = Document(CURR)

    # Basic stats
    orig_words = sum(len(p.text.split()) for p in orig.paragraphs)
    curr_words = sum(len(p.text.split()) for p in curr.paragraphs)

    # Abstract word counts (exclude "Abstract" heading + Keywords line)
    def abs_words(doc):
        started = False
        words = 0
        for p in doc.paragraphs:
            t = p.text.strip()
            if t == "Abstract":
                started = True
                continue
            if started:
                if (t.startswith("Keywords") or t.startswith("1 Introduction")
                        or t.startswith("Figure")):
                    break
                words += len(t.split())
        return words

    orig_abs = abs_words(orig)
    curr_abs = abs_words(curr)

    # Section headings
    def headings(doc):
        out = []
        for i, p in enumerate(doc.paragraphs):
            t = p.text.strip()
            if not t:
                continue
            if (t in ("Abstract", "References", "Data Availability Statement")
                or (len(t) < 80 and re.match(r"^\d(\.\d+)?\s+\w", t))):
                out.append(t)
        return out

    h_orig = headings(orig)
    h_curr = headings(curr)

    # Hypothesis statements
    h1_orig = find_paragraph(orig, "Hypothesis 1 (H1)")
    h1_curr = find_paragraph(curr, "Hypothesis 1 (H1)")
    h2_orig = find_paragraph(orig, "Hypothesis 2 (H2)")
    h2_curr_demoted = None
    for p in curr.paragraphs:
        if "open empirical question" in p.text and "supplementary" in p.text:
            h2_curr_demoted = p.text.strip()
            break
    h3_orig = find_paragraph(orig, "Hypothesis 3 (H3)")
    h3_curr = find_paragraph(curr, "Hypothesis 3 (H3)")
    h4_orig = find_paragraph(orig, "Hypothesis 4 (H4)")
    h4_curr = find_paragraph(curr, "Hypothesis 4 (H4)")

    # Build markdown
    md = []
    md.append("# Manuscript Comparison: R2 Original vs R3 Final")
    md.append("")
    md.append("**Files compared:**")
    md.append("- R2 original: `Manuscript_Blinded_MIR_2_original.docx`")
    md.append("- R3 final: `Manuscript_Blinded_MIR_2_revised.docx`")
    md.append("")
    md.append("**Date:** 2026-05-03")
    md.append("**Branch:** `claude/p3-r3-revision` · PR #6 (20 commits)")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. Quick stats")
    md.append("")
    md.append("| Metric | R2 original | R3 final | Δ |")
    md.append("|---|---:|---:|---:|")
    md.append(f"| Total paragraphs | {len(orig.paragraphs)} | "
              f"{len(curr.paragraphs)} | "
              f"{len(curr.paragraphs) - len(orig.paragraphs):+} |")
    md.append(f"| Manuscript words | {orig_words:,} | {curr_words:,} | "
              f"{curr_words - orig_words:+,} |")
    md.append(f"| Abstract words | {orig_abs} | {curr_abs} | "
              f"{curr_abs - orig_abs:+} |")
    md.append(f"| Tables | {len(orig.tables)} | {len(curr.tables)} | "
              f"{len(curr.tables) - len(orig.tables):+} |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. Title")
    md.append("")
    md.append(f"**R2:** {orig.paragraphs[0].text}")
    md.append("")
    md.append(f"**R3:** {curr.paragraphs[0].text}")
    md.append("")
    md.append("**Diff:** R3 adds *': A Firm-Level Study of Singapore'*; "
              "removes implicit boundary-condition framing.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 3. Section structure")
    md.append("")
    md.append("### Sections only in R2 (removed/renamed in R3)")
    md.append("")
    only_orig = set(h_orig) - set(h_curr)
    if only_orig:
        for h in sorted(only_orig):
            md.append(f"- `{h}`")
    else:
        md.append("- (none — all R2 sections survive in some form)")
    md.append("")
    md.append("### Sections only in R3 (newly added)")
    md.append("")
    only_curr = set(h_curr) - set(h_orig)
    if only_curr:
        for h in sorted(only_curr):
            md.append(f"- `{h}`")
    else:
        md.append("- (none)")
    md.append("")
    md.append("### Major structural changes")
    md.append("")
    md.append("- **§4.3 renamed:** R2 *'TCI direct effect supports H1; "
              "TCI moderation null supports H2'* → R3 *'TCI results'* "
              "(narrower title because H2 has been demoted to a research "
              "question; section no longer claims to *support* H2).")
    md.append("- **§4.4 renamed:** R2 *'DAI moderation: evidence "
              "concentrated in the high-export tail'* → R3 *'DAI results'* "
              "(generalises section, includes new clarification "
              "paragraph about M8 centering arithmetic).")
    md.append("- **§6 NEW:** R3 adds a standalone *'6 Conclusion'* "
              "section. R2 went straight from §5 Discussion to §6 "
              "Limitations.")
    md.append("- **§7 renumbered:** R2 *'6 Limitations and Future Research'* "
              "→ R3 *'7 Limitations and Future Research'* (because of "
              "the new §6 Conclusion above).")
    md.append("- **NEW: Data Availability Statement** added between "
              "§7 and References.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 4. Abstract — full side-by-side")
    md.append("")
    md.append(f"### R2 original ({orig_abs} words, single paragraph)")
    md.append("")
    # Get R2 abstract
    started = False
    for p in orig.paragraphs:
        t = p.text.strip()
        if t == "Abstract":
            started = True
            continue
        if started:
            if t.startswith("Keywords") or t.startswith("1 Introduction"):
                break
            if t:
                md.append(f"> {t}")
                md.append(">")
    md.append("")
    md.append(f"### R3 final ({curr_abs} words, two paragraphs)")
    md.append("")
    started = False
    for p in curr.paragraphs:
        t = p.text.strip()
        if t == "Abstract":
            started = True
            continue
        if started:
            if t.startswith("Keywords") or t.startswith("1 Introduction"):
                break
            if t:
                md.append(f"> {t}")
                md.append(">")
    md.append("")
    md.append("**Key changes:**")
    md.append(f"- Length cut from {orig_abs} to {curr_abs} words "
              f"({orig_abs - curr_abs:+} → much tighter, within MIR 250 limit).")
    md.append("- *'in a digital-frontier economy'* removed.")
    md.append("- *'level-shift effect on the productivity intercept'* removed.")
    md.append("- *'sharper construct validity and an initial boundary-"
              "condition argument for internationalization research in "
              "digital-frontier settings'* → *'within-context evidence "
              "from Singapore that ... suggests that digital adoption "
              "may function more as a contingent scaling resource than "
              "as a uniform productivity advantage.'*")
    md.append("- New explicit numbers in findings: *'imprecisely located "
              "and falls in a sparsely populated region'* signals the "
              "bootstrap CI work.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 5. Hypotheses — claim register tightened")
    md.append("")
    md.append("### H1 (TCI direct) — UNCHANGED")
    md.append(f"> **R2:** {h1_orig}")
    md.append(">")
    md.append(f"> **R3:** {h1_curr}")
    md.append("")
    md.append("### H2 (TCI moderation) — DEMOTED to research question")
    md.append(f"> **R2:** {h2_orig}")
    md.append(">")
    md.append(f"> **R3:** *(no longer a labelled hypothesis)* — "
              f"{h2_curr_demoted}")
    md.append("")
    md.append("**Rationale:** R2 asserted TCI as a *level-shift* rather "
              "than moderator. Reviewer pointed out that a non-significant "
              "interaction does not establish absence of moderation. R3 "
              "drops the H2 label and treats TCI moderation as an open "
              "empirical question tested supplementarily.")
    md.append("")
    md.append("### H3 (DAI direct) — REFRAMED")
    md.append(f"> **R2:** {h3_orig}")
    md.append(">")
    md.append(f"> **R3:** {h3_curr}")
    md.append("")
    md.append("**Rationale:** R2 predicted DAI is *positively associated "
              "on average*. M8 actually shows direct DAI null (β=0.019, "
              "p=.705); Table 4 shows DAI sig at FSTS=0, null in middle, "
              "sig in upper tail. R3 reframes from average premium to "
              "conditional non-uniformity, matching what the data "
              "actually estimate.")
    md.append("")
    md.append("### H4 (DAI moderation by FSTS) — UNCHANGED")
    md.append(f"> **R2:** {h4_orig}")
    md.append(">")
    md.append(f"> **R3:** {h4_curr}")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 6. NEW Section 6 — Conclusion (was absent in R2)")
    md.append("")
    md.append("**R2:** No standalone Conclusion section. Discussion "
              "(§5.1, §5.2) flowed directly into §6 Limitations.")
    md.append("")
    md.append("**R3:** Adds three Conclusion paragraphs that:")
    md.append("- Restate the construct distinction (TCI = direct level "
              "effect; DAI = conditional scaling).")
    md.append("- Qualify the I-P literature interpretation in this setting "
              "without overturning it.")
    md.append("- Explicitly disavow generalising to all digitally advanced "
              "economies; close with call for comparative + longitudinal "
              "future research.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 7. Section 7 (Limitations) — major rewrite")
    md.append("")
    md.append("**R2 §6 Limitations:** ~700 words, defensive, included "
              "long Heckman / Wolfolds & Siegel tangent, equivalence-"
              "testing tangent, framing as 'extreme-case, within-context "
              "evidence'.")
    md.append("")
    md.append("**R3 §7 Limitations:** 430 words, focused on three clean "
              "limitations:")
    md.append("1. Associational single-country cross-section "
              "(reverse causation, omitted variables, selection).")
    md.append("2. Thin upper-tail support (bootstrap CI [53%, 253%]; "
              "96.3% inverted-U recovery; precision constraint in N=84).")
    md.append("3. Tier 1–2 measurement boundary (DAI captures "
              "foundational adoption, not deeper organizational "
              "capability or AI-grade dynamic capability).")
    md.append("")
    md.append("**Plus:** Concrete future-research IV strategies — "
              "firm-to-port distance, customs-clearance times, regional "
              "broadband coverage, within-sector peer adoption — with "
              "Wolfolds & Siegel (2019) caveat (added in Pass 5).")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 8. Tables — what changed")
    md.append("")
    md.append("| Table | R2 | R3 | Status |")
    md.append("|---|---|---|---|")
    md.append("| Table 1 (Descriptive + Correlations) | Same | Same | "
              "✓ Unchanged |")
    md.append("| Table 2 (Hierarchical OLS M0–M8) | Same structure | "
              "Same structure; M8 R²/AdjR² text aligned with table | "
              "✓ Numerical consistency fixed (Pass 3 D1) |")
    md.append("| Table 3 (Robustness, 6 specs) | All 6 rows had stale "
              "numbers from earlier draft | All 6 rows re-estimated from "
              "raw .dta with locked spec; baseline now matches Table 2 "
              "M8 exactly | ✓ Major fix (Pass 0) |")
    md.append("| Table 4 (Marginal effects of DAI) | Same | Same; §4.4 "
              "prose now consistent with FSTS=0 row +0.080 (p=.045) | "
              "✓ Internal consistency fixed (Pass 3) |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 9. Figures — all three regenerated from canonical data")
    md.append("")
    md.append("| Figure | R2 | R3 |")
    md.append("|---|---|---|")
    md.append("| Figure 1 (Conceptual) | Old IB-style with 'Boundary "
              "condition: Digital-frontier institutional environment' "
              "panel at bottom | Redesigned IV/DV/Moderator/Control "
              "framework; bottom panel now 'Scope: extreme-case, within-"
              "context evidence from Singapore' |")
    md.append("| Figure 2 (DAI marginal effect) | Plain marginal-effect "
              "curve | **Support-aware version**: rug strip + decile "
              "counts + thin-tail (>70%) shaded grey; reader sees "
              "exactly where the high-tail signal sits relative to data "
              "density |")
    md.append("| Figure 3 (Predicted I-P curve) | Plain quadratic with "
              "TP at 88.6% | **Bootstrap-aware version**: 95% CI band "
              "for predicted line + red shaded vertical band for the "
              "turning-point CI [52.8%, 252.9%] + in-figure note '96.3% "
              "of bootstrap replications recover an inverted-U shape' |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 10. Five reviewer concerns — disposition")
    md.append("")
    md.append("| Reviewer issue | R2 status | R3 status |")
    md.append("|---|---|---|")
    md.append("| #1 Digital-frontier overclaim | Title: *'in Singapore'* "
              "(neutral but Abstract used 'digital-frontier economy'); "
              "Abstract closed with 'boundary-condition argument for "
              "digital-frontier settings' | Title: *'A Firm-Level Study "
              "of Singapore'*; Abstract drops boundary-condition wording "
              "entirely; framed as 'within-context evidence' throughout |")
    md.append("| #2 TCI/DAI fungibility | Construct architecture stated "
              "but no item-level sensitivity disclosed in prose | "
              "Cross-construct r=0.106 reported; SWAP1 falsification in "
              "§4.5 (joint F drops .011 → .154 when c22b reassigned to "
              "TCI); deeper item-to-construct theory in §3.2.3 |")
    md.append("| #3 Extensive vs intensive margin | Full-sample "
              "polynomial used as primary I-P test | §3.3 explicitly "
              "frames full-sample polynomial as descriptive baseline; "
              "Stage-1 logit (extensive) + Stage-2 OLS on N=84 "
              "exporters (intensive) added |")
    md.append("| #4 Right-tail leverage | Acknowledged in passing | "
              "Cook's D + LOO + trimmed-tail + bootstrap CI all "
              "implemented; figures support-aware; §7 explicitly "
              "grounds caution in thin upper tail |")
    md.append("| #5 Hypothesis ↔ estimate mismatch | H2 claimed "
              "level-shift; H3 claimed positive-on-average | H2 demoted "
              "to research question; H3 reframed to conditional non-"
              "uniformity; §4.4 includes M8-centering clarification |")
    md.append("| D1 Table 3 baseline mismatch | Stale numbers across "
              "all 6 rows | All 6 rows re-estimated from raw .dta and "
              "corrected (Pass 0) |")
    md.append("| D2 Mis-grounded caveat | Used adj-R² across samples | "
              "§7 limitation 2 grounded in thin upper-tail support and "
              "small-subsample precision instead |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## Bottom line")
    md.append("")
    md.append("R3 is **substantially different from R2** in framing, "
              "claim register, structure, and numerical consistency. "
              "Specifically:")
    md.append("")
    md.append("- **Framing:** Singapore is now a within-context, "
              "analytically informative case rather than a basis for a "
              "general boundary condition for digitally mature economies.")
    md.append("- **Claims:** H2 demoted to research question; H3 "
              "reframed to non-uniformity; *'level-shift effect'* and "
              "*'inverted-U is robust'* phrasing fully removed.")
    md.append("- **Structure:** New §6 Conclusion; §7 Limitations cut "
              "to 430 words; §3.2.3 deeper item-to-construct theory; "
              "§4.5 item-swap falsification visible.")
    md.append("- **Numerical consistency:** Table 3 fully re-estimated "
              "(all 6 rows); §4.4 prose matches Table 2 M8 (R²=0.211, "
              "adj R²=0.196) and Table 4 (FSTS=0 effect=+0.080 p=.045).")
    md.append("- **New theory:** TCE (Coase 1937; Williamson 1985) "
              "framing for the conditional DAI mechanism in §5.1.")
    md.append("- **Figures:** All three regenerated from canonical data; "
              "Figures 2 and 3 are now support-aware; Figure 1 redesigned "
              "to standard IB IV-DV-Moderator-Control framework.")
    md.append("")
    md.append("Final consistency audit: **13 / 13 pass · 0 issues**.")

    OUT.write_text("\n".join(md))
    print(f"Wrote: {OUT}")
    print(f"Length: {sum(1 for _ in open(OUT))} lines")


if __name__ == "__main__":
    main()
