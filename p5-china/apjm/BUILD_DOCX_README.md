# P5 China v1.5 — How to Build the Submission .docx

Three options, ranked by ease.

## Option 1 — One-shot script (recommended)

If you have **pandoc**, **graphviz**, and **python3 + matplotlib** installed:

```bash
cd p5-china/apjm/
bash build_docx.sh
```

Produces `manuscript_v1_5.docx` (~770 KB) with all 4 figures embedded.

### Install prerequisites (one-time)

| OS | Command |
|---|---|
| macOS | `brew install pandoc graphviz && pip install matplotlib numpy` |
| Ubuntu / Debian | `apt install pandoc graphviz && pip install matplotlib numpy` |
| Windows | Download `pandoc-windows.msi` from https://pandoc.org/installing.html and `graphviz-windows.exe` from https://graphviz.org/download/, then `pip install matplotlib numpy` |

## Option 2 — Online pandoc (no install)

Fastest path with zero installation:

1. Open https://pandoc.org/try in a browser.
2. Set **From** = Markdown, **To** = docx.
3. Open `manuscript_v1_5_complete.md` from this repo (raw view), copy all content, paste into the textarea.
4. Click **Convert** → download the .docx.
5. **Note:** figures will not auto-embed via the online tool. After downloading, open in Word and insert figures 1–4 manually at the figure caption placeholders (PNG files in `figures/`).

Rendered figure PNG files for manual insertion:
- `figures/figure1_v1_4.png` (conceptual model)
- `figures/figure2_threshold_forest.png`
- `figures/figure3_predicted_curves.png`
- `figures/figure4_level_shift_bars.png`

## Option 3 — Manual Word assembly

If you prefer working entirely in Word:

1. Open Word → New blank document.
2. For each of the 6 manuscript parts, open the `.md` file in a text editor, copy the content, paste into Word.
3. Word will preserve most markdown formatting; clean up the headings and bullet lists.
4. Insert the 4 figures at the figure caption placeholders.
5. Save as `manuscript_v1_5.docx`.

This is the slowest but most reliable when you need fine-grained control over Word formatting (e.g., for a journal-specific template).

## Verification

The assembled `manuscript_v1_5_complete.md` should be ~70 KB and contain:
- 6 numbered sections (Abstract through References)
- 39 references in alphabetical APA 7th order with DOIs
- 4 figure caption blocks (`> **Figure N.** ...`)
- 16+ instances of "Chinese private firms"
- Exactly 8 mentions of `manufactur*` (all intentional: literature/frame references and the §4.6 mfg-only robustness check)

Verify with:

```bash
grep -c "^## " manuscript_v1_5_complete.md           # should be 9 (incl. subsections)
grep -c "https://doi.org" manuscript_v1_5_complete.md  # should be 36+
grep -ni "manufactur" manuscript_v1_5_complete.md      # should be 8 lines
```

## Where the source files live

All v1.5 source files in `p5-china/apjm/`:

| File | Size | Notes |
|---|---|---|
| `manuscript_v1_5_part1_frontmatter_intro.md` | ~10 KB | Title, abstract, intro |
| `manuscript_v1_5_part2_theory.md` | ~12 KB | Theory + 4 hypotheses |
| `manuscript_v1_4_part3_data_methods.md` | ~12 KB | Data + methods (reused unchanged) |
| `manuscript_v1_4_part4_results.md` | ~14 KB | Results (reused unchanged) |
| `manuscript_v1_5_part5_discussion.md` | ~9 KB | Discussion (durability framing) |
| `manuscript_v1_5_part6_limits_refs.md` | ~16 KB | 6 limitations + 39 refs |
| `figures/figure1_conceptual_model_v1_4.dot` | <2 KB | Graphviz source for Figure 1 |
| `figures/figure1_conceptual_model_v1_4.mmd` | <2 KB | Mermaid alternative |
| `figures/render_figures.py` | ~9 KB | Builds Figures 2/3/4 from verified data |
| `build_docx.sh` | ~3 KB | One-shot builder (this directory) |
| `SUBMISSION_TARGETS.md` | ~6 KB | 14 alternative journals + fit rationale |
| `CHANGELOG_v1_4_to_v1_5.md` | ~5 KB | Diff log v1.4 → v1.5 |

## After building

1. Open `manuscript_v1_5.docx` in Word; verify figures render correctly at the right places.
2. Add author/affiliation page (kept separate from blinded manuscript per most journals' rules).
3. Optionally re-export to PDF for preview (`pandoc ... -o manuscript_v1_5.pdf`).
4. Cross-check word count vs target journal guidelines (`SUBMISSION_TARGETS.md` lists per-journal limits).
5. Upload to journal editorial system.
