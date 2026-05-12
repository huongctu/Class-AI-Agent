# P5 China — Replication

Tái tạo manuscript và figures cho **P5 China (APJM v1.8)**.

## Prerequisites

```bash
# Required
pip install matplotlib numpy pillow python-docx==1.2.0

# Required for Figure 1 (Graphviz conceptual model)
# macOS:    brew install pandoc graphviz
# Ubuntu:   apt install pandoc graphviz
# Windows:  download pandoc-windows.msi + graphviz-windows.exe
```

WBES China 2012 + 2024 raw data — see [`data_source.md`](data_source.md).

## Steps

### Step 1: Bootstrap submission package

```bash
cd papers/p5-china/
bash bootstrap.sh
```

Tải 6 manuscript parts + build script + 6 submission docs + 4 audit reports + figures.

### Step 2: Build manuscript

```bash
cd manuscript/
bash build_docx.sh
```

Quy trình:
1. Render Figure 1 từ Graphviz `.dot` source (figure1_v1_4.png)
2. Render Figures 2/3/4 từ matplotlib (`render_figures.py`)
3. Cộng 6 markdown parts → `manuscript_v1_8_blinded_complete.md`
4. Inject figure references → `manuscript_v1_8_blinded_with_figures.md`
5. Pandoc convert → `manuscript_v1_8_blinded.docx` (~768 KB)

Verification:
- Word count: 13,146 (target 10-15K cho ABS-3 IB journals)
- 39 references APA 7th, all DOIs verified
- 3 tables (descriptives, M2 main, three-way moderation)
- 4 figures embedded

### Step 3: Final blinding check

```bash
cd manuscript/
grep -nE '(Do & Tu|huongctu|Class-AI-Agent)' parts/*.md
# Expected: empty
```

### Step 4: Submit to APJM

Xem `submission/00_SUBMISSION_CHECKLIST.md` for portal upload mapping.

## Patches applied since v1.8 build

- **v1.8.1 (2026-05-06)**: Avenyo (2021) DOI fix `s41287-020-00269-w` → `s41287-021-00364-6` + title "Microeconomic evidence from sub-Saharan Africa" → "Evidence from African firms" (verified Crossref + Springer). See [`audit/CITATION_AUDIT.md`](../audit/CITATION_AUDIT.md) for full audit log (42/42 references verified across Tier A/B/C/D).

## Cross-link

- Branch gốc (full git history): [`claude/p5-china-sample-outline-1KXp4`](https://github.com/huongctu/Class-AI-Agent/tree/claude/p5-china-sample-outline-1KXp4)
- v1.8.1 Avenyo fix commit: [`a14ca97`](https://github.com/huongctu/Class-AI-Agent/commit/a14ca978)
- Tier B audit close commit: [`ffae888`](https://github.com/huongctu/Class-AI-Agent/commit/ffae8884)
