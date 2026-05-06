# P4 Vietnam v5.9 Changelog (v5.8 → v5.9)

> 27 total edits across 2 phases. All applied to both `manuscript_blinded.docx` and `manuscript_full_with_authors.docx`.

## Phase 1: 7 metadata + structural fixes (`fix_p4_v58.py`)

| # | Section | Change |
|---|---|---|
| 1 | Header metadata | `Tables: 2 (Table 1 desc; Table 2 main pattern). Figures: 2` → `Tables: 4 (Table 1 desc §4.0; Table 2 directional §4.4; Table 3 robustness §4.5; Table 4 turning points §4.5). Figures: 3 (Figure 1 conceptual; Figure 2 with 4 panels predicted I-P curves; Figure 3 moderation slices)` |
| 2 | §4.4 | `Table 1 summarises the directional` → `Table 2 summarises the directional` (fix duplicate "Table 1" label since descriptives is also Table 1) |
| 3 | §4.5 | `Table LM reports the implied turning points` → `Table 4 reports the implied turning points` (rename ad-hoc Table LM to consecutive Table 4) |
| 4 | Supplementary materials | `tables/table_lind_mehlum.csv (Table LM source)` → `(Table 4 source)` |
| 5 | §2.1 (Theory) | `transitional economy such as Vietnam` → `transitional economy such as Vietnam (Cuervo-Cazurra, 2012)` (add cite for previously uncited reference) |
| 6 | §2.4 (Stage-contingent digital value) | `In early phases of internationalisation, digital tools may create...` → `Drawing on the dynamic-capability lifecycle perspective (Helfat & Peteraf, 2003), we argue that in early phases of internationalisation, digital tools may create...` (add cite for previously uncited reference) |
| 7 | Title | append `— Three-Wave Evidence from Vietnam` for discoverability |

## Phase 2: 20 reviewer-driven clean-copy edits (`apply_v59_edits.py`)

### Abstract (4 blocks)

| # | Block | Change |
|---|---|---|
| 8 | Purpose | Tighter framing; explicit "foundational digital adoption" framing for DAI |
| 9 | Design/methodology/approach | Drop Heckman/control-function/Paternoster details (move to body); compact phrasing |
| 10 | Findings | Explicit dual-margin reading; quantitative TP range (39–46%) |
| 11 | Originality/value | Foreground "context-sensitive and wave-specific" not "uniformly stable" |

### §2.1 H1 + §2.4 H4

| # | Section | Change |
|---|---|---|
| 12 | §2.1 H1 | Rewritten to participation-and-intensity structure framing (drop "operates through two distinct margins" overclaim); H1a participation + H1b intensity preserved with "weaker, diminishing, or non-significant" wording |
| 13 | §2.4 H4 | Tightened to "wave-specific" not "stage-contingent"; explicit "strongest within-sample detectability anticipated in 2023" |

### §4.3 Interpretation (2 paragraphs)

| # | Paragraph | Change |
|---|---|---|
| 14 | H1+H2+H3 | "qualified support" not "strongly supported"; explicit participation-margin caveat; concentrate on transition rather than within-exporter curvature |
| 15 | H4 | "limited exploratory support"; pooled wave × focal interaction does not detect cross-wave separability |

### §5 Discussion (8 paragraphs)

| # | Section | Change |
|---|---|---|
| 16 | §5.1 para 1 | "foundational digital adoption" replaces "digital capability" for DAI_z referent |
| 17 | §5.1 para 2 | Lifecycle interpretation explicit |
| 18 | §5.2 para 1 | TCI robust under PSM and 2SLS; DAI attenuates to null under IV |
| 19 | §5.2 para 2 | DAI_rich extension reinforces construct interpretation |
| 20 | §5.2 para 3 | Closing take-away: identification-robust vs context-sensitive |
| 21 | §5.3 para 1 | 2015 dip = wave-specific compression of foundational digital-adoption channel |
| 22 | §5.3 para 2 | Institutional plausibility caveat: "should not be treated as a formally identified explanation" |
| 23 | §5.3 para 3 | Wave-specific heterogeneity consistent with stage contingency |

### §6 Limitations (2 paragraphs)

| # | Limitation | Change |
|---|---|---|
| 24 | limit2 | Tier-1-style proxy framing for DAI_z |
| 25 | limit4 | Grammar fix (was "although the Paternoster..." missing main clause) + cross-wave evenness reframing |

### §7 Conclusion (2 paragraphs)

| # | Paragraph | Change |
|---|---|---|
| 26 | p1 | Dual-margin + non-monotonic framing; "driven primarily by participation-and-intensity structure" |
| 27 | p2 | TCI robust, DAI wave-sensitive, pooled averages conceal heterogeneity |

## Skip rationale (per NCS instruction "chỉ lấy file FINAL")

Không push các file phiên bản cũ:
- `manuscript_blinded.docx` (v5.8 trước fix) — reference only on source branch
- `manuscript_full_with_authors.docx` (v5.8 trước fix) — reference only on source branch
- `response_letter_to_reviewer.docx` (round 1) — historical, only round 2 needed for resubmission
- `figure_2_main_results.png` (legacy combined) — superseded by figure_2a-d split

## Verification

```python
# Verify all 20 v5.9 edits applied (text-level):
grep -c 'H1 receives qualified support' manuscript_v5_9_blinded.docx  # = 1
grep -c 'foundational digital adoption' manuscript_v5_9_blinded.docx  # >= 8
grep -c 'operates through two distinct margins' manuscript_v5_9_blinded.docx  # = 0
grep -c 'H1 is strongly supported' manuscript_v5_9_blinded.docx  # = 0
```

All 27 edits verified clean on both blinded + full_with_authors versions.
