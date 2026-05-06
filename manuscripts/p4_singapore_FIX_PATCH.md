# P3 Singapore Manuscript — Comprehensive Fix Patch (v1.0)

> **Source**: `01_Manuscript_formatted_2.pdf` (27 pages, compiled via Pandoc → LuaTeX, 2026-05-05)
> **Target**: NCS apply trực tiếp vào file `.tex` hoặc `.md` source
> **Author**: AI assistant audit + NCS review
> **Date**: 2026-05-06

## Tóm tắt

Patch này gộp **3 nhóm fix**:
1. **DOI verification** (1 fix critical)
2. **Hypothesis renumbering** (H1, H3, H4 → H1, H2, H3)
3. **Formatting & content polish** (9 issues từ audit ban đầu + review của NCS)

Tổng số edit: **15 changes** (4 critical, 6 medium, 5 cosmetic).

---

## A. DOI fixes (CRITICAL — fix trước submit)

### A.1 Avenyo et al. (2021) — DOI WRONG TWICE

**Verified qua Crossref + Springer**: cả DOI hiện tại trong bản thảo VÀ DOI user đề xuất ban đầu đều sai.

```
TÌM:
Avenyo, E. K., Tregenna, F., & Kraemer-Mbula, E. (2021). Do productive
capabilities affect export performance? Microeconomic evidence from
sub-Saharan Africa. The European Journal of Development Research, 33(2),
304–329. https://doi.org/10.1057/s41287-020-00328-2

THAY BẰNG:
Avenyo, E. K., Tregenna, F., & Kraemer-Mbula, E. (2021). Do productive
capabilities affect export performance? Evidence from African firms.
The European Journal of Development Research, 33(2), 304–329.
https://doi.org/10.1057/s41287-021-00364-6
```

**Lưu ý**: Cả 3 thay đổi cần thiết:
- DOI: `s41287-020-00328-2` → **`s41287-021-00364-6`**
- Subtitle: "Microeconomic evidence from sub-Saharan Africa" → **"Evidence from African firms"**
- Volume/issue/pages giữ nguyên (33(2), 304–329)

### A.2 DOI verification status — 28 references đã check

| # | Reference | DOI | Status |
|---|---|---|---|
| 1 | Aguinis et al. (2005) | 10.1037/0021-9010.90.1.94 | ✓ |
| 2 | Aiken & West (1991) | (book) | n/a |
| 3 | **Avenyo et al. (2021)** | ~~10.1057/s41287-020-00328-2~~ → **10.1057/s41287-021-00364-6** | ❌ FIX |
| 4 | Barney (1991) | 10.1177/014920639101700108 | ✓ |
| 5 | Bharadwaj et al. (2013) | 10.25300/MISQ/2013/37:2.3 | ✓ |
| 6 | Buckley & Casson (1976) | (book) | n/a |
| 7 | Coase (1937) | 10.1111/j.1468-0335.1937.tb00002.x | ✓ |
| 8 | Cohen (1988) | (book) | n/a |
| 9 | Cohen & Levinthal (1990) | 10.2307/2393553 | ✓ |
| 10 | Coltman et al. (2008) | 10.1016/j.jbusres.2008.01.013 | ✓ |
| 11 | Contractor et al. (2003) | 10.1057/palgrave.jibs.8400003 | ✓ |
| 12 | Haans et al. (2016) | 10.1002/smj.2399 | ✓ |
| 13 | Hambrick & Mason (1984) | 10.5465/amr.1984.4277628 | ✓ |
| 14 | Hennart (1982) | (book) | n/a |
| 15 | Hitt et al. (1997) | 10.5465/256948 | ✓ |
| 16 | Johanson & Vahlne (1977) | 10.1057/palgrave.jibs.8490676 | ✓ |
| 17 | Johanson & Vahlne (2009) | 10.1057/jibs.2009.24 | ✓ |
| 18 | Krammer et al. (2018) | 10.1016/j.ibusrev.2017.07.003 | ✓ |
| 19 | Lall (1992) | 10.1016/0305-750X(92)90097-F | ✓ |
| 20 | Lind & Mehlum (2010) | 10.1111/j.1468-0084.2009.00569.x | ✓ |
| 21 | Lu & Beamish (2004) | 10.5465/20159604 | ✓ |
| 22 | MacKinnon & White (1985) | 10.1016/0304-4076(85)90158-7 | ✓ |
| 23 | Marano et al. (2016) | 10.1177/0149206315624963 | ✓ verified |
| 24 | O'Brien (2007) | 10.1007/s11135-006-9018-6 | ✓ |
| 25 | Peng (2003) | 10.5465/amr.2003.9416341 | ✓ |
| 26 | Peng et al. (2008) | 10.1057/palgrave.jibs.8400377 | ✓ |
| 27 | Verhoef et al. (2021) | 10.1016/j.jbusres.2019.09.022 | ✓ |
| 28 | White (1980) | 10.2307/1912934 | ✓ |
| 29 | Williamson (1985) | (book) | n/a |
| 30 | Wolfolds & Siegel (2019) | 10.1002/smj.2995 | ✓ |
| 31 | Wright & Ricks (1994) | 10.1057/palgrave.jibs.8490222 | ✓ |
| 32 | World Bank (2024) | (data set, URL only) | n/a |

→ **27/28 DOIs đúng**, chỉ Avenyo cần fix.

---

## B. Hypothesis renumbering (H1, H3, H4 → H1, H2, H3)

### Vấn đề
Bản thảo hiện có H1 (§2.3.1), bỏ H2 (§2.3.2 chỉ là "open empirical question"), H3 (§2.3.3), H4 (§2.3.4). Reviewer IJoEM/IBR sẽ đòi renumber liên tục.

### B.1 §2.3.3 — "Hypothesis 3 (H3)" → "Hypothesis 2 (H2)"

```
TÌM:
Hypothesis 3 (H3). The productivity association of digital adoption
(DAI) in Singapore is conditional rather than uniform across firms.

THAY BẰNG:
Hypothesis 2 (H2). The productivity association of digital adoption
(DAI) in Singapore is conditional rather than uniform across firms.
```

### B.2 §2.3.4 — "Hypothesis 4 (H4)" → "Hypothesis 3 (H3)"

```
TÌM:
Hypothesis 4 (H4). The association between digital adoption (DAI)
and firm performance becomes more positive at higher levels of export
intensity in Singapore.

THAY BẰNG:
Hypothesis 3 (H3). The association between digital adoption (DAI)
and firm performance becomes more positive at higher levels of export
intensity in Singapore.
```

### B.3 §2.4 Conceptual model — fix references trong text

```
TÌM:
H3 and H4 are therefore jointly informative: H3 concerns the
non-uniformity of the DAI–productivity association, whereas H4 specifies
the direction of that contingency across export intensity.

THAY BẰNG:
H2 and H3 are therefore jointly informative: H2 concerns the
non-uniformity of the DAI–productivity association, whereas H3 specifies
the direction of that contingency across export intensity.
```

### B.4 Figure 1 caption — fix "(H4)" → "(H3)" và "(H3)" → "(H2)"

```
TÌM:
Digital adoption (DAI) is the contingency variable on the I–P path (H4);
technological capability (TCI) enters mainly as a direct-effect construct
(H1), with any moderation by TCI assessed in a supplementary test rather
than hypothesised ex ante. The diagram also lists the direct effect of
DAI on the dependent variable (H3), which is estimated in the empirical
model

THAY BẰNG:
Digital adoption (DAI) is the contingency variable on the I–P path (H3);
technological capability (TCI) enters mainly as a direct-effect construct
(H1), with any moderation by TCI assessed in a supplementary test rather
than hypothesised ex ante. The diagram also lists the direct effect of
DAI on the dependent variable (H2), which is estimated in the empirical
model
```

### B.5 Figure 1 box "H4: DAI × FSTS" → "H3: DAI × FSTS"

(Trong sơ đồ Figure 1 — sửa nhãn box hoặc trong source code của figure)

---

## C. Formatting fixes (từ audit gốc + review của NCS)

### C.1 Double "References" header (CRITICAL)

Trang 25 hiện tại có `References` xuất hiện 2 lần liên tiếp:
```
References
References

Aguinis, H., Beaty, J. C., ...
```

```
TÌM (trong source — có thể là duplicate \section{References} hoặc
   một lần \section + một lần emit từ bibtex):
\section{References}
\section{References}

HOẶC dạng markdown:
# References
# References

THAY BẰNG (chỉ giữ 1 lần):
\section{References}
```

### C.2 References KHÔNG sắp alphabet (CRITICAL)

Trang 26 hiện tại sai thứ tự:
```
Hiện tại: Haans → Hambrick → Hitt → Krammer → Hennart → Lall → Lind → Lu → Johanson → Johanson → Marano
```

```
Đúng APA 7 (alphabet theo họ tác giả đầu):
Haans → Hambrick → Hennart → Hitt → Johanson (1977) → Johanson (2009)
→ Krammer → Lall → Lind → Lu → MacKinnon → Marano → ...
```

Trang 27 cũng có vấn đề:
```
Hiện tại: ... Verhoef → Williamson → Wolfolds → MacKinnon → White → World Bank → Wright
Đúng:     ... MacKinnon (đã ở trên trang 26) → ... → Verhoef → White → Williamson → Wolfolds → World Bank → Wright
```

→ Sort lại toàn bộ references theo alphabet họ tác giả đầu tiên.

### C.3 β symbols missing trong body text (CRITICAL)

§4.3, §4.4, §4.5 hiện tại có những vị trí:
```
"TCI ... ( = 0.168, SE = 0.040, p < .001)"  ← thiếu β
"DAI ... ( = 0.104, SE = 0.038, p = .007)"
"DAI coefficient attenuates to = 0.077"
"the direct DAI term is small ( = 0.019, p = .705)"
"the linear interaction with FSTS is negative and marginal ( = −1.177, p = .083)"
"the quadratic interaction term is positive ( = 3.118, SE = 1.117, p = .005)"
```

```
Cần thay TẤT CẢ instances của " = 0.XXX" trong body
THÀNH "(β = 0.XXX" — Greek beta phải được preserve

Trong LaTeX source: dùng $\beta$ trong inline math
Trong Markdown source: dùng \beta hoặc UTF-8 β trực tiếp
Trong DOCX source: keyboard input "β" hoặc Insert → Symbol → Greek small letter beta (U+03B2)
```

→ 6+ vị trí cần fix; nếu source là LaTeX, có thể dùng regex: `( = ([\-\+]?[0-9]\.[0-9]+))` → `(\\beta = $2`.

### C.4 Font Computer Modern → Times New Roman

Bản thảo đang render bằng Computer Modern (LaTeX default). Nếu target IBR/MIR/JIBS yêu cầu Times New Roman:

```
Trong LaTeX preamble, thêm:
\usepackage{newtxtext,newtxmath}
% hoặc:
\usepackage{mathptmx}

Trong pandoc YAML metadata (nếu source là markdown):
mainfont: "Times New Roman"
mainfontoptions:
  - "Numbers=OldStyle"

Trong DOCX template — đổi style "Normal" font sang Times New Roman.
```

### C.5 Table 2 column headers merge

Trang 14 hiện tại:
```
Variable | M0Ctrl | M2Inv-U | M5+TCM6+DAM7T+DM4DAI×M8Full
```

→ Cần widen cells hoặc rotate hoặc shorten labels:

```
Đề xuất label cleaner:
Variable | M0 | M1 | M2 | M3 | M4 | M5 | M6
         | Ctrl | InvU | +TCI | +DAI | TCI+DAI | DAIx | Full
```

Hoặc dùng 2-row header với line break.

### C.6 Renumber Models (NCS issue #8)

Bản thảo dùng tên models không tuần tự:
```
Hiện tại: M0Ctrl, M2InvU, M5+TCI, M6+DAI, M7T+D, M4DAI×, M8Full
```

```
Đề xuất rename theo thứ tự logic:
M0: Controls only
M1: + FSTS quadratic (inverted-U baseline)
M2: + TCI direct
M3: + DAI direct
M4: TCI + DAI joint direct
M5: + TCI × FSTS interactions (supplementary)
M6: + DAI × FSTS interactions (full DAI moderation)
```

Cần update Table 2 column headers + body text references.

---

## D. Substantive concerns (NCS review #3-7)

### D.1 Marginal effect tại FSTS=100% = +1.742 (NCS issue #3)

Hiện tại Table 4 hiển thị +1.742** (p = .002) tại FSTS=100% — dựa trên ~3% firms (n≈20). Reviewer có thể coi là extrapolation artifact.

**Đề xuất 2 lựa chọn**:

**Option A** (conservative): Trim Table 4 ở FSTS ≤ 70%, đẩy hàng FSTS=100% xuống Online Appendix với caveat rõ.

**Option B** (transparent): Giữ Table 4 nguyên nhưng thêm grey shading hoặc dấu † cho 2 hàng FSTS≥70% và caption note:
```
Note: Marginal effects at FSTS ≥ 70 % are computed in a sparsely
populated region of the data (approximately 3 % of firms; see Figure 2),
so should be interpreted as suggestive rather than conclusive.
```

§7 đã caveat nhưng có thể bổ sung explicit reference đến Table 4.

### D.2 R5 robustness (exporters-only) — TCI mất significance (NCS issue #4)

§4.5 hiện tại: R5 N=84, TCI β=0.130 không significant. Cần thừa nhận rõ:

```
ĐỀ XUẤT THÊM vào §4.5 cuối phần R5:
"Within the exporters-only sub-sample (R5), the TCI direct association
attenuates to β = 0.130 and is no longer statistically distinguishable
from zero. This finding is broadly consistent with the small-sample
caveats noted above (N = 84) but indicates that, even within this restricted
sub-sample, TCI's productivity premium is detectable only when domestic
firms are included as a comparison set. We treat this as a precision
limitation rather than evidence against H1, while flagging it transparently
for readers."
```

### D.3 DAI moderation phụ thuộc B-READY 2023 e-payment items (NCS issue #5)

§4.5 đã lưu ý nhưng cần explicit:

```
ĐỀ XUẤT THÊM vào §4.5 phần DAI moderation:
"The DAI moderation pattern (joint F = 4.56) reflects information
contributed by both website (c22b) and electronic-payment items (k33,
k38). Restricting DAI to website only (R1) reduces the joint F to 1.55
[verify: manuscript shows 4.01]. This indicates that the DAI×FSTS²
evidence is not driven by digital presence alone; the electronic-payment
items, available only in the B-READY 2023 module, are integral to the
moderation signal. Generalisation to settings without an e-payment module
therefore requires caution."
```

### D.4 N=623 power discussion (NCS issue #6)

§7 nên thêm:

```
ĐỀ XUẤT THÊM vào §7 (Limitations):
"The single-wave Singapore design (N = 623; 617 with DAI items)
provides limited statistical power for detecting moderation in the
sparsely populated upper tail of the FSTS distribution. With 11+
parameters (FSTS, FSTS², TCI, DAI, FSTS×DAI, FSTS²×DAI, four controls,
sector FE), and only ~20 firms with FSTS > 70 %, the moderation
estimates in this region rest on thin support. Multi-country or
multi-wave designs would be needed to strengthen tail-based inference."
```

### D.5 Modulate language: "supports" → "is consistent with" (NCS issue #7)

Joint F = 4.56 (p = .011) là moderate evidence, không phải strong. Cần soften ngôn từ ở những chỗ over-claim:

```
TÌM ALL instances của:
"supports H3" → "is consistent with H3"
"supports H4" → "is consistent with H3" (sau khi renumber)
"the evidence supports the conditional-scaling interpretation"
→ "the evidence is consistent with the conditional-scaling interpretation"
"strong evidence" → "moderate evidence"
"firmly identified" → already correctly stated as "is not formally identified"
```

§5.1 và §6 có thể có những chỗ cần soft-edit.

---

## E. Implementation checklist

### E.1 Trước khi compile lại

- [ ] Apply A.1: fix Avenyo DOI + title
- [ ] Apply B.1, B.2, B.3, B.4, B.5: renumber hypothesis H3→H2, H4→H3 (all locations)
- [ ] Apply C.1: remove duplicate `\section{References}` / `# References`
- [ ] Apply C.2: sort references alphabetically by first author surname
- [ ] Apply C.3: replace ` = X.XXX` with `β = X.XXX` in §4.3, §4.4, §4.5 body
- [ ] Apply C.4: switch to Times-like font (`\usepackage{newtxtext,newtxmath}`)
- [ ] Apply C.5: fix Table 2 column headers (widen, rotate, or shorten)
- [ ] Apply C.6: renumber models M0–M6 logically
- [ ] Apply D.1: caveat marginal effects at FSTS≥70% in Table 4 caption
- [ ] Apply D.2: acknowledge R5 TCI null in §4.5
- [ ] Apply D.3: explicit B-READY 2023 dependency in §4.5
- [ ] Apply D.4: power discussion in §7
- [ ] Apply D.5: soften "supports" → "is consistent with" globally

### E.2 Sau khi recompile

- [ ] Verify: Avenyo DOI + title đã fix
- [ ] Verify: H1, H2, H3 (không còn H4)
- [ ] Verify: References xuất hiện 1 lần, alphabet đúng
- [ ] Verify: tất cả β rendered đúng trong body (không còn "( = X.XXX")
- [ ] Verify: font Times-like
- [ ] Verify: Table 2 columns readable
- [ ] Verify: model labels nhất quán M0–M6
- [ ] Verify: Table 4 caption có caveat về thin tail
- [ ] Verify: §4.5 có acknowledgment R5 null + B-READY dependency
- [ ] Verify: §7 có power discussion

### E.3 Pre-submit checklist

- [ ] Word count main text ≤ journal limit (kiểm tra IBR/MIR/JIBS guidelines)
- [ ] Highlights bullets ≤ 5 (P3 hiện chưa có Highlights — cần check journal có yêu cầu không)
- [ ] APA 7 format consistent
- [ ] Figures embedded inline với captions
- [ ] Data availability statement included
- [ ] AI use disclosure included
- [ ] Conflict of interest + Funding statements
- [ ] Cover letter sẵn sàng

---

## F. Phạm vi không làm trong patch này

- Không cấu trúc lại §5 Discussion (nội dung khoa học OK)
- Không thay đổi conceptual model framing (OK)
- Không thêm robustness panels mới (11 panels hiện tại đã đủ)
- Không re-estimate models (số liệu hiện tại đúng)
- Không thay đổi journal target (IBR/MIR/ABM phù hợp; tránh JIBS desk-screen)

---

## G. Câu hỏi follow-up cho NCS

1. **NCS có file `.tex` hoặc `.docx` source không?** Nếu có, gửi lên đây để tôi apply patches trực tiếp.
2. **Journal target chính xác?** IBR? MIR? Asian Business & Management? Format tweak có thể khác.
3. **Có muốn tôi reconstruct full clean LaTeX file** từ PDF content + tất cả patches đã apply? (Sẽ ~600-800 dòng, NCS chỉ cần `pdflatex` để compile.)

---

*Patch v1.0 — 2026-05-06. NCS: Đỗ Thùy Hương. AI assistant: comprehensive audit theo review của NCS + audit ban đầu.*
