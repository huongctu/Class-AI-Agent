# P5 China — APJM Submission Outline + Replication Pipeline

## Context

Mục tiêu: chạy lại sạch model P5 (China 2012 + 2024 WBES, manuscript v1.2) và chuẩn bị submission cho *Asia Pacific Journal of Management (APJM)*. Manuscript v1.2 đã chốt analytic samples 2,619 (2012) / 1,940 (2024) / 4,559 (pooled), nhưng RA cần re-construct từ raw để (a) verify N theo từng tầng lọc, (b) re-run M0–M8 với sample flags rõ ràng, (c) khóa methods section trước khi blind manuscript.

### Verification từ implementation reports (đã đọc)

1. **ISIC version mismatch giữa hai wave.** China 2012 `a4a` dùng **ISIC Rev 3.1** (manufacturing = 15–37, có thêm 38 = Other Manufacturing residual). China 2024 `a4a` dùng **stratum code 1–14** (1–9 = manufacturing strata). 2024 cũng có `d1a2_v4` = 4-digit ISIC Rev 4. Hai codeframe không tương đương → phải xử lý sector filter riêng từng wave; chỉ aggregate manufacturing là so sánh được cross-wave.
2. **Recommended industry variable cho 2024.** WBES 2024 implementation report ghi rõ: "Users are generally advised to use industry categories based on the realized information in `d1a2_v4`" (4-digit ISIC Rev 4 từ phỏng vấn), không dùng `a4a` (từ frame).
3. **State-owned exclusion (2012).** File `China2012fullESN2700data.dta` chứa 2,700 private firms, đã loại 148 state-owned (lưu riêng). Nhưng dataset vẫn bao gồm services, retail, IT, construction → cần manufacturing filter nếu muốn mfg-only.
4. **Panel observations (2024).** 2,189 = 1,972 fresh + 217 panel (panel firms cũng trong 2012). Pooled regression vi phạm independence nếu không xử lý.
5. **Nonresponse codes khác nhau.** 2012: `-9` (don't know/refuse combined), `-7` (n/a). 2024: `-9` (DK), `-8` (refuse), `-7` (n/a) — phải recode cả ba sang missing cho 2024.

### Quyết định phương pháp đã chốt

| Fork | Lựa chọn | Implementation |
|---|---|---|
| Sample frame | **Full private** (no mfg filter) | Match v1.2 reported N |
| Mfg filter 2024 (if applied) | `d1a2_v4//100 ∈ [10,33]` | WBES recommended |
| Panel SE pooled | Cluster theo `idstd` | `vce(cluster idstd)` cho mọi pooled regression |
| Mfg scope 2012 (if applied) | `a4a` 15–38 (giữ Other Mfg) | `keep if a4a >= 15 & a4a <= 38` |

## Recommended approach — see do/ and python/ for implementations.

## Critical files

- Raw 2012: `China2012fullESN2700data.dta` (2,700 private mfg+services firms)
- Raw 2024: `China2024fulldata.dta` (2,189 firms, 1,972 fresh + 217 panel)
- `manuscript_p5_v1_2.docx` — verify exact `firmage` formula và filter v1.2 dùng
- `BREADY_2024_Questionnaire.pdf` — verify `b5` definition cho 2024 và TCI/DAI item codes
- `China_ES_Manufacturing_English_FINAL.pdf` — 2012 questionnaire reference

## Verification plan

1. **Audit N table.** RA chạy `01_build_2012.do` và `02_build_2024.do`; file `audit/audit_N_checklist.csv` phải khớp expected ±10 firms ở mọi tầng.
2. **Replication sanity.** Re-run M2 trên `sample_base` 2012 và 2024; turning point trong khoảng [48 %, 51 %] (2012) và [46 %, 49 %] (2024).
3. **Cross-wave equality test.** Paternoster z trên FSTS và FSTSsq giữa 2012 và 2024 phải fail to reject (p > 0.10) — central claim của paper.
4. **Pooled clustered SE.** `vce(cluster idstd)` trên 4,544 obs; ~4,342 unique idstd clusters.
5. **APJM dry-run.** Title + abstract + cover letter qua 2 internal reviewers (chị + 1 colleague) trước upload.

## Open items RA cần check khi mở v1.2

1. `firmage` công thức v1.2 hiện dùng (`year - b5`?) — sync với plan.
2. `foreigndummy` threshold v1.2 dùng (b2b > 0% hay b2b ≥ 10%?) — sync.
3. TCI/DAI items 2024 mapping — `e6`, `b8`, `h1`, `h8` có đổi tên trong BREADY 2024 không.
4. State-ownership 2012: nếu v1.2 strict private thresholds (e.g., loại firms với b2c > 10% state), thêm filter trong `01_build_2012.do`.
