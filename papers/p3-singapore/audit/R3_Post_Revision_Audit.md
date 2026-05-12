# P3 Singapore R3 — Post-Revision Audit Report

> **Date**: 2026-05-06
> **Source**: `Manuscript_Blinded_MIR_2_revised.docx` (R3 final, on branch `claude/p3-r3-revision`)
> **Output**: `Manuscript_R3_FIGFIXED.docx` (after applying ALL patches including Figure 1)

## Summary

R3 đã giải quyết hầu hết các phản biện reviewer. Audit hậu-R3 phát hiện **3 nhóm vấn đề còn sót** (12 changes total):

1. **Avenyo et al. (2021) DOI sai** — kế thừa từ R2, chưa được fix trong R3
2. **Hypothesis numbering có gap** — H1, H3, H4 (H2 đã được demote thành "open empirical question" theo phản hồi reviewer)
3. **Figure 1 chứa nhãn cũ** — embedded PNG vẫn hiển thị "H4: DAI × FSTS" và "H3: DAI direct" (sau khi renumber phải là H3 và H2)

Đã apply tất cả 12 fixes vào `Manuscript_R3_FIGFIXED.docx`. Verify clean: 0 H4 references trong text body, Figure 1 đã regenerate.

## Phát hiện chính

### 1. Avenyo (2021) DOI verified qua Crossref + Springer

```
Bản R2 + R3 (cả hai đều sai): 10.1057/s41287-020-00328-2  ❌
DOI thực:                       10.1057/s41287-021-00364-6  ✓
Title thực:                     "Evidence from African firms"
Title trong bản thảo:           "Microeconomic evidence from sub-Saharan Africa" ❌
```

DOI cũ KHÔNG resolve trên doi.org (404). Title cũ là paraphrase của abstract, không phải title thực.

### 2. Hypothesis numbering rationale

Trong R3, NCS đã (rất đúng) demote TCI moderation từ H2 sang "open empirical question". Tuy nhiên numbering còn lại có gap:

```
R3 hiện tại:
  H1 (§2.3.1)   ✓ TCI direct
  [H2 demoted to open empirical question — không có nhãn "Hypothesis 2"]
  H3 (§2.3.3)   DAI conditional
  H4 (§2.3.4)   DAI moderation by FSTS

R3 fixed (consecutive numbering):
  H1 (§2.3.1)   ✓ TCI direct
  [open empirical question — text giữ nguyên, không có nhãn]
  H2 (§2.3.3)   DAI conditional         ← was H3
  H3 (§2.3.4)   DAI moderation by FSTS  ← was H4
```

### 3. Figure 1 đã regenerate (NEW — 2026-05-06)

**Vấn đề**: Sơ đồ Figure 1 trong R3 docx (file `image3.png` trong `word/media/`) chứa các nhãn cũ:
- "H2: TCI × FSTS (open empirical question)" — TCI moderation arrow
- "H4: DAI × FSTS (stronger at high FSTS)" — DAI moderation arrow
- Bottom legend: "H1: TCI ...; H3: DAI ..." — DAI direct effect

Patch script trước (`fix_r3_post_revision.py`) chỉ fix CAPTION text bên dưới figure. Nhãn TRONG image (embedded PNG) cần regenerate riêng.

**Giải pháp**: Sử dụng `regenerate_fig1.py` (matplotlib) để tạo lại Figure 1 với:
- TCI moderation arrow: chỉ "TCI × FSTS (open empirical question)" — KHÔNG còn nhãn H2 (vì đã demote)
- DAI moderation arrow: "H3: DAI × FSTS (stronger at high FSTS)" — was H4
- Bottom legend: "H1: TCI...; H2: DAI...; conditional on FSTS" — was H3
- Thiết kế giữ nguyên: 4 boxes (Moderators × 2, IV, DV), 4 controls, scope footer
- Aspect ratio 2062×1404 (xấp xỉ original 2077×1426)

**Cách reproduce**:
```bash
pip install matplotlib pillow python-docx
python3 regenerate_fig1.py  # outputs fig1_FIXED.png
# then replace word/media/image3.png inside .docx zip
```

## 12 changes đã apply

| # | Vùng | Trước → Sau |
|---|---|---|
| 1 | References (Avenyo) | DOI: `s41287-020-00328-2` → `s41287-021-00364-6` |
| 2 | References (Avenyo) | Subtitle: "Microeconomic evidence..." → "Evidence from African firms" |
| 3 | §2.3.3 | "Hypothesis 3 (H3)" → "Hypothesis 2 (H2)" (DAI conditional) |
| 4 | §2.3.4 | "Hypothesis 4 (H4)" → "Hypothesis 3 (H3)" (DAI moderation) |
| 5 | §2.4 (text) | "H3 and H4 are jointly informative" → "H2 and H3" |
| 6 | §2.4 (text) | "H3 concerns the non-uniformity" → "H2 concerns" |
| 7 | §2.4 (text) | "whereas H4 specifies the direction" → "whereas H3 specifies" |
| 8 | Figure 1 caption (para 45) | "(H4)" path → "(H3)" path |
| 9 | Figure 1 caption (para 45) | DAI direct "(H3)" → "(H2)" |
| 10 | Figure 1 caption (para 156) | "(H4)" path → "(H3)" path (duplicate caption) |
| 11 | Figure 1 caption (para 156) | DAI direct "(H3)" → "(H2)" (duplicate caption) |
| **12** | **Figure 1 image** (image3.png) | **Regenerated với matplotlib — H4 → H3 và H3 → H2 trong nhãn box** |

## Verification

```
=== TEXT FIXES (paragraph-level) ===
✓ NEW Avenyo DOI: FOUND
✓ NEW Avenyo subtitle: FOUND
✓ H2 (DAI conditional): FOUND
✓ H3 (DAI moderation): FOUND
✓ §2.4 H2+H3 phrase: FOUND
✓ H2 concerns: FOUND
✓ H3 specifies: FOUND

✓ removed "Microeconomic evidence from sub-Saharan Africa"
✓ removed "Hypothesis 4 (H4)"
✓ removed "s41287-020-00328-2"
✓ removed "H3 and H4 are jointly informative"

Any "H4" references remaining: 0

=== FIGURE 1 IMAGE ===
✓ image3.png replaced: 320,414 → 254,957 bytes
✓ New image: 2062×1404 RGBA (similar to original 2077×1426)
✓ Visual inspection: TCI moderation no longer shows H2; DAI moderation shows H3; bottom legend shows H1+H2
```

## Files trong commit này

| File | Mô tả | Vị trí |
|---|---|---|
| `fix_r3_post_revision.py` | Patch script cho text fixes (changes 1-11) | `papers/p3-singapore/replication/` |
| `regenerate_fig1.py` | Script tạo lại Figure 1 PNG (change 12) | `papers/p3-singapore/figures/source/` |
| `R3_Post_Revision_Audit.md` | Audit report (file này) | `papers/p3-singapore/audit/` |
| `Manuscript_R3_FIGFIXED.docx` | **Output cuối** với cả 12 fixes | `papers/p3-singapore/manuscript/` |

## Trạng thái sẵn sàng submit MIR

Sau khi apply 12 patches:
- ✓ All citations APA 7 format
- ✓ All DOIs verified (28/28 references; Avenyo fix bằng DOI thực)
- ✓ Hypothesis numbering consecutive H1, H2, H3 trong cả text VÀ Figure 1
- ✓ R3 framing (within-context, not boundary condition)
- ✓ Statistical evidence properly hedged
- ✓ 13/13 consistency audit pass (per R3_vs_R2_Comparison.md)
- ✓ Figure 1 image regenerated với numbering nhất quán

→ **R3 + 12 patches = sẵn sàng submit MIR round 4** (hoặc thay thế R3).

## Phạm vi không làm trong patch này

- Không re-estimate models (R3 đã re-estimate Table 3, đã verify consistency 13/13 pass)
- Không thay đổi nội dung Discussion / Conclusion / Limitations (R3 đã rewrite kỹ)
- Không thêm robustness panels (đã có 6 panels)
- Không thay đổi Figures 2 & 3 (already regenerated in R3)
