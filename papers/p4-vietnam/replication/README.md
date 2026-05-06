# P4 Vietnam — Replication

Tái tạo manuscript và figures cho **P4 Vietnam (IJoEM v5.9)**.

## Prerequisites

```bash
pip install python-docx==1.2.0
```

WBES Vietnam 2009 + 2015 + 2023 raw data — see [`data_source.md`](data_source.md).

## Steps

### Step 1: Get binary submission files

```bash
cd papers/p4-vietnam/
bash bootstrap.sh
```

Tải về từ branch gốc `claude/update-p4-draft-W6UKL`:
- `manuscript/manuscript_blinded_FIXED.docx` (v5.8 + 7 prior fixes)
- `manuscript/manuscript_full_with_authors_FIXED.docx`
- `submission/cover_letter_ijoem.docx`
- `submission/response_letter_round2.docx`
- `figures/*.png` và `*.pdf` (7 figures)
- `figures/source/*.xlsx` (6 Excel files — figures_excel)

### Step 2: Apply 20 reviewer-driven v5.9 edits

```bash
python3 replication/apply_v59_edits.py
```

Input: `manuscript/manuscript_blinded_FIXED.docx`
Output: `manuscript/manuscript_v5_9_blinded.docx` (final v5.9)

20 edits:
- Abstract (4 blocks): tighter framing, drop technical overload, add dual-margin reading
- §2.1 H1: dual-margin participation+intensity framing
- §2.4 H4: tightened to wave-specific exploratory framing
- §4.3 hypothesis tests: H1 "qualified support"; H4 "limited exploratory support"
- §5.1 (2 paragraphs): "foundational digital adoption" replaces "digital capability" for DAI_z referent
- §5.2 (3 paragraphs): PSM/2SLS evidence sharpens TCI vs DAI distinction
- §5.3 (3 paragraphs): 2015 dip reframed as institutional plausibility
- §6 Limitations: limit2 Tier-1 proxy framing; limit4 grammar fix + cross-wave evenness reframing
- §7 Conclusion (2 paragraphs): dual-margin + TCI robust / DAI wave-sensitive

Verification:
- 0 occurrences of "H1 is strongly supported" (legacy)
- 0 occurrences of "operates through two distinct margins" (legacy)
- New phrases: "qualified support", "foundational digital adoption", etc.

### Step 3: Apply same edits to with-authors version

```bash
sed 's|manuscript_blinded_FIXED|manuscript_full_with_authors_FIXED|g; s|manuscript_v5_9_blinded|manuscript_v5_9_full_with_authors|g' replication/apply_v59_edits.py > replication/apply_v59_edits_full.py
python3 replication/apply_v59_edits_full.py
```

Output: `manuscript/manuscript_v5_9_full_with_authors.docx`

### Step 4: Reproduce figures (optional)

Xem `figures/source/*.xlsx` — mỗi Excel chứa:
- Sheet "Data" — raw data của figure
- Sheet "Chart" — native Excel chart
- Sheet "Image" — embedded PNG export

Để tạo lại: mở XLSX trong Excel, chỉnh data nếu cần, export Chart sang PNG.

## Cross-link

- Branch gốc (full git history): [`claude/update-p4-draft-W6UKL`](https://github.com/huongctu/Class-AI-Agent/tree/claude/update-p4-draft-W6UKL)
- v5.9 commits: [`fix(p4-v5.8)` 7 patches](https://github.com/huongctu/Class-AI-Agent/commit/c16908b8) + [`fix(p4-v5.9)` 20 edits](https://github.com/huongctu/Class-AI-Agent/commit/47e06b5b)
