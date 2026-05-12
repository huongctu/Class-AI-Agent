# P3 Singapore — Replication

Tái tạo manuscript và figures cho **P3 Singapore (MIR R3)**.

## Prerequisites

```bash
pip install python-docx==1.2.0 matplotlib pillow
```

WBES Singapore 2023 raw data — see [`data_source.md`](data_source.md) cho mapping.

## Steps

### Step 1: Apply 11 text patches to R3 manuscript

```bash
cd papers/p3-singapore/manuscript/
python3 ../replication/fix_r3_post_revision.py
```

Input: `Manuscript_Blinded_MIR_2_revised.docx` (R3 reference)
Output: `Manuscript_R3_FIXED.docx` (with 11 text patches: Avenyo DOI + hypothesis renumbering H3/H4 → H2/H3)

Verification:
- 0 instances of "H4" (legacy)
- 0 instances of old DOI `s41287-020-00328-2`
- New DOI `s41287-021-00364-6` present
- New title "Evidence from African firms" present

### Step 2: Regenerate Figure 1 conceptual model

```bash
cd papers/p3-singapore/figures/source/
python3 regenerate_fig1.py
```

Output: `fig1_FIXED.png` (2062×1404 RGBA, 254 KB)

Figure 1 has these label fixes vs R3 original:
- TCI × FSTS box: KHÔNG còn nhãn "H2" (đã demote)
- DAI × FSTS box: "H4: ..." → "H3: ..."
- Bottom legend: "H1: TCI ...; H3: DAI ..." → "H1: TCI ...; H2: DAI ..."

### Step 3: Embed Figure 1 vào DOCX

```python
import zipfile, shutil, os, tempfile

src = 'manuscript/Manuscript_R3_FIXED.docx'
dst = 'manuscript/manuscript_R3_FIGFIXED.docx'
shutil.copy(src, dst)

tmp = tempfile.mkdtemp()
with zipfile.ZipFile(src, 'r') as z:
    z.extractall(tmp)

# image3.png in word/media/ corresponds to Figure 1
shutil.copy('figures/source/fig1_FIXED.png',
            os.path.join(tmp, 'word', 'media', 'image3.png'))

os.remove(dst)
with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(tmp):
        for f in files:
            full = os.path.join(root, f)
            z.write(full, os.path.relpath(full, tmp))
```

Output: `manuscript_R3_FIGFIXED.docx` — **đây là file submit MIR**

## Verification

```bash
# Open in Word và verify:
# 1. Title contains "A Firm-Level Study of Singapore"
# 2. §2.3.3 có "Hypothesis 2 (H2)" (không phải H3)
# 3. §2.3.4 có "Hypothesis 3 (H3)" (không phải H4)
# 4. References list chứa "Avenyo, E. K., ... 10.1057/s41287-021-00364-6"
# 5. Figure 1 caption box hiển thị "H3: DAI × FSTS"
```

## Cross-link

- Branch gốc (full git history): [`claude/p3-r3-revision`](https://github.com/huongctu/Class-AI-Agent/tree/claude/p3-r3-revision)
- Audit report: [`../audit/R3_Post_Revision_Audit.md`](../audit/R3_Post_Revision_Audit.md)
- Pre-revision package: [`../audit/P3_Revision_Package.md`](../audit/P3_Revision_Package.md)
