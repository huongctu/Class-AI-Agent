# P5 China — Tables

P5 manuscript embeds 3 tables inline trong markdown source (`manuscript/parts/`):

| Table | Section | Source markdown | Content |
|---|---|---|---|
| Table 1 | §3.5 (Data) | `parts/manuscript_v1_8_blinded_part3_data_methods.md` | Descriptive statistics for analytic samples (2012, 2024, pooled) |
| Table 2 | §4.2 (Results) | `parts/manuscript_v1_8_blinded_part4_results.md` | M2 main inverted-U specification (3 columns × 4 panels) |
| Table 3 | §4.4 (Three-way moderation) | `parts/manuscript_v1_8_blinded_part4_results.md` | Capability × wave × FSTS interactions |

## How to extract tables to CSV

Nếu cần tables dạng CSV để re-analysis hoặc replicate paper figures:

```bash
# Option 1: Pandoc convert manuscript to docx, then use pandoc/python-docx to extract
cd manuscript/
bash build_docx.sh
python3 - <<'EOF'
from docx import Document
import csv
doc = Document('manuscript_v1_8_blinded.docx')
for i, table in enumerate(doc.tables):
    with open(f'../tables/table_{i+1}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in table.rows:
            writer.writerow([cell.text for cell in row.cells])
print('Tables exported')
EOF
```

```bash
# Option 2: Direct copy from underlying replication scripts
# (P5 build pipeline runs Stata + Python for estimates, then injects into markdown)
# See repo root for `tools/` directory with replication scripts.
```

## Reproducibility

All table values trace to a canonical estimation pipeline đã được verified với:
- 42/42 references audited (Tier A/B/C/D — see `../audit/CITATION_AUDIT.md`)
- All empirical claims verified against raw WBES `.dta` (see `../audit/CLAIMS_AUDIT.md`)
- Per-reference verification table (see `../audit/VERIFICATION_RESULTS.md`)
