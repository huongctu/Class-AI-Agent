# Manuscript v1.3 — Assembled Files

Manuscript was split into 6 markdown parts to fit GitHub push size limits. To assemble into a single document:

```bash
cd p5-china/apjm/
cat manuscript_v1_3_part1_frontmatter_intro.md \
    manuscript_v1_3_part2_theory.md \
    manuscript_v1_3_part3_data_methods.md \
    manuscript_v1_3_part4_results.md \
    manuscript_v1_3_part5_discussion.md \
    manuscript_v1_3_part6_limits_refs.md \
    > manuscript_v1_3.md
```

Or convert to .docx via pandoc:

```bash
pandoc manuscript_v1_3_part1_frontmatter_intro.md \
       manuscript_v1_3_part2_theory.md \
       manuscript_v1_3_part3_data_methods.md \
       manuscript_v1_3_part4_results.md \
       manuscript_v1_3_part5_discussion.md \
       manuscript_v1_3_part6_limits_refs.md \
       -o manuscript_v1_3.docx
```

## Parts

| Part | Content | Sections |
|---|---|---|
| 1 | Title, abstract, keywords, introduction | Front matter + §1 |
| 2 | Theory & 4 hypotheses + conceptual model | §2 |
| 3 | Data & methods | §3 |
| 4 | Results | §4 |
| 5 | Discussion + managerial + policy | §5 |
| 6 | Limitations + acknowledgements + references | §6 + back matter |

## Verification (run after assembly)

```bash
# Should return exactly 2 lines (intentional retentions: data clarification + sample-frame drift)
grep -ni 'manufactur' manuscript_v1_3.md

# Should return 19
grep -c 'Chinese private firms' manuscript_v1_3.md
```

## Changelog

See `CHANGELOG_v1_2_to_v1_3.md` for full diff log: 27 sentence-level edits + 2 paragraph insertions renaming "Chinese manufacturing SMEs" → "Chinese private firms" plus side updates (2024 -8 refusal code, replication note, replication pointer).

## Key replicated numbers (from `results/summary.md`)

- M2 turning point 2012: **49.37 %** (manuscript: 49.4 %)
- M2 turning point 2024: **47.19 %** (manuscript: 47.6 %)
- M2 turning point pooled: **48.78 %** (manuscript: 48.9 %)
- Paternoster FSTS: p = **0.412** (stable ✓)
- Paternoster FSTS²: p = **0.545** (stable ✓)
