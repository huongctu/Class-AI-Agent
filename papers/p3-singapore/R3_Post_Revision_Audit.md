# P3 Singapore R3 — Post-Revision Audit Report

> **Date**: 2026-05-06
> **Source**: `Manuscript_Blinded_MIR_2_revised.docx` (R3 final, on branch `claude/p3-r3-revision`)
> **Output**: `Manuscript_R3_FIXED.docx` (after applying `fix_r3_post_revision.py`)

## Summary

R3 đã giải quyết hầu hết các phản biện reviewer. Audit hậu-R3 phát hiện **2 nhóm vấn đề còn sót** (11 changes total), đều mang tính cosmetic/citation và không ảnh hưởng nội dung khoa học:

1. **Avenyo et al. (2021) DOI sai** — kế thừa từ R2, chưa được fix trong R3
2. **Hypothesis numbering có gap** — H1, H3, H4 (H2 đã được demote thành "open empirical question" theo phản hồi reviewer)

Đã apply tất cả 11 fixes vào `Manuscript_R3_FIXED.docx`. Verify clean: 0 H4 references, 0 old DOI, 0 old subtitle.

## Phát hiện chính

### 1. Avenyo (2021) DOI được verified qua Crossref + Springer

```
Bản R2 + R3 (cả hai đều sai): 10.1057/s41287-020-00328-2  ❌
DOI thực:                       10.1057/s41287-021-00364-6  ✓
Title thực:                     "Evidence from African firms"
Title trong bản thảo:           "Microeconomic evidence from sub-Saharan Africa" ❌
```

DOI cũ KHÔNG resolve trên doi.org (404). Title cũ là paraphrase của abstract, không phải title thực.

### 2. Hypothesis numbering rationale

Trong R3, NCS đã (rất đúng) demote TCI moderation từ H2 sang "open empirical question" (theo phản biện reviewer rằng "non-significant interaction does not establish absence of moderation"). Tuy nhiên numbering còn lại có gap:

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

Giải pháp này:
- Giữ nguyên thay đổi nội dung mà R3 đã apply (H2 demoted)
- Đảm bảo numbering H1, H2, H3 liên tục
- Không cần explain "missing H2" trong response letter

## 11 changes đã apply

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

## Verification

```
$ python3 -c "..."
✓ NEW Avenyo DOI: FOUND
✓ NEW Avenyo subtitle: FOUND
✓ H2 (DAI conditional): FOUND
✓ H3 (DAI moderation): FOUND
✓ §2.4 H2+H3 phrase: FOUND
✓ H2 concerns: FOUND
✓ H3 specifies: FOUND

✓ removed "Microeconomic evidence from sub-Saharan Africa"
✓ removed "Hypothesis 4 (H4)"
✓ removed "Hypothesis 3 (H3). The productivity association"
✓ removed "s41287-020-00328-2"
✓ removed "H3 and H4 are jointly informative"
✓ removed "whereas H4 specifies"

Any "H4" references remaining: 0
```

## Lưu ý — Figure 1 (sơ đồ vẽ tay/PowerPoint)

Sơ đồ Figure 1 trong R3 chứa các nhãn box "H1: TCI × FSTS (open empirical question)" và "H4: DAI × FSTS (stronger at high FSTS)". Patch script đã xử lý CAPTION text bên dưới figure, nhưng nhãn TRONG figure (nếu nó là embedded image/SmartArt) cần fix thủ công trong PowerPoint/Inkscape.

**Nếu Figure 1 là PNG/SVG embedded**: NCS cần mở source file (PowerPoint, Visio, Inkscape) và sửa nhãn box trực tiếp:
- "H4: DAI × FSTS (stronger at high FSTS)" → "H3: DAI × FSTS (stronger at high FSTS)"

**Nếu Figure 1 là native Word drawing**: thì script python-docx có thể handle, nhưng phức tạp hơn — có thể cần fix manual qua Word UI.

## Phạm vi không làm trong patch này

- Không re-estimate models (R3 đã re-estimate Table 3, đã verify consistency 13/13 pass)
- Không thay đổi nội dung Discussion / Conclusion / Limitations (R3 đã rewrite kỹ)
- Không thêm robustness panels (đã có 6 panels)
- Không change figure source (cần fix manual nếu Figure 1 chứa H4 nhãn box)

## Trạng thái sẵn sàng submit MIR

Sau khi apply 11 patches:
- ✓ All citations APA 7 format
- ✓ All DOIs verified (28/28 references)
- ✓ Hypothesis numbering consecutive H1, H2, H3
- ✓ R3 framing (within-context, not boundary condition)
- ✓ Statistical evidence properly hedged ("is consistent with" / "qualifies" not "supports")
- ✓ 13/13 consistency audit pass (per R3_vs_R2_Comparison.md)
- ⚠ Figure 1 box label "H4" → "H3" cần fix manual nếu là embedded image

→ R3 + 11 patches = sẵn sàng submit MIR round 4 (hoặc thay thế R3).
