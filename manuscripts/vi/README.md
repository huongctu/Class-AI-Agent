# Bản dịch tiếng Việt 3 bản thảo bài báo (P3, P4, P5)

> **Mục đích**: Cung cấp bản dịch tiếng Việt học thuật cho 3 manuscripts P3 Vietnam (APJM), P4 Singapore (MIR), P5 China (IJoEM) phục vụ:
> 1. Bổ sung dossier nộp Hội đồng CTU đánh giá luận án
> 2. Cho phép thành viên Hội đồng đọc trực tiếp tiếng Việt mà không phải dịch lại
> 3. Tạo bản gốc tham chiếu nội bộ cho NCS Đỗ Thùy Hương và HD TS. Nguyễn Minh Cảnh
>
> **NCS**: Đỗ Thùy Hương · P1323001 · Quản trị kinh doanh (9340101)
> **HD**: TS. Nguyễn Minh Cảnh · Trường Kinh tế, Trường Đại học Cần Thơ
> **Phiên bản**: 12/05/2026

## Bản dịch trong thư mục này

| File | Bản gốc EN | Tạp chí mục tiêu | Sample |
|---|---|---|---|
| `p3_vietnam_vi_v12.md` | `manuscripts/p3_vietnam_en_clean.md` (v12 Phase 9) | *Asia Pacific Journal of Management* (APJM) | N=2.958 (3 wave WBES Việt Nam 2009/2015/2023) |
| `p4_singapore_vi_v8.md` | `manuscripts/p4_singapore_en_clean.md` (v8 Phase 9) | *Management International Review* (MIR) | N=623/617 (WBES Singapore 2023) |
| `p5_china_vi_v9.md` | `manuscripts/p5_china_en_clean.md` (v2.0 Phase 9) | *International Journal of Emerging Markets* (IJoEM) | N=4.559 (2 wave WBES Trung Quốc 2012+2024) |

## Phương pháp dịch

Áp dụng 5 convention chuẩn từ `thesis/09b_vn_term_glossary.md` (v1.2 — 68 thuật ngữ chính thức):

1. **Thuật ngữ tiếng Anh lần đầu**: Format "tiếng Việt (English term)" — vd: "phân tán hiệu quả (productivity dispersion)".
2. **Acronym**: Giữ nguyên tiếng Anh (TCI, DAI, FSTS, ICRV, WBES, OLS, HC1, IV, 2SLS, PSM) — lần đầu giải thích đầy đủ "Năng lực số (Digital Adoption Index — DAI)".
3. **Câu**: Tối đa 35 từ/câu. Câu liệt kê 4+ phần tử ngắt thành câu mở + câu liệt kê.
4. **Đoạn văn**: 3-5 câu, mở bằng câu chủ đề (topic sentence).
5. **Voice & tone**: Tránh "tôi/chúng tôi" — dùng "nghiên cứu này", "bài báo này". Tránh khẩu ngữ. Hedge cẩn trọng.

## Phạm vi giữ nguyên (KHÔNG dịch)

- **References list**: Giữ nguyên APA 7 tiếng Anh (chuẩn quốc tế cho submission)
- **Số liệu thập phân**: Giữ EN format `0.07`, `2,958`, `β = 0.179`, `p < .001` — đảm bảo nhất quán với bản EN tableq
- **Acronym**: TCI, DAI, FSTS, ICRV, WBES giữ nguyên (sau lần đầu giải thích)
- **Statistical symbols**: β, p, F, R², SE giữ nguyên
- **Citation in-text**: format APA 7 — "Lu và Beamish (2004)" hoặc "(Marano et al., 2016)"

## Tài liệu tham chiếu

- `thesis/09b_vn_term_glossary.md` — Bảng thuật ngữ Anh-Việt 68 mục × 7 nhóm
- `thesis/09_academic_writing_standards_vi.md` — 5 conventions + anti-patterns + 12-điểm checklist
- `writing_guides/00_author_voice_guide.md` — 12 patterns MSc → PhD elevation

## Trạng thái submission tổng hợp

| Paper | EN canonical | VI version (folder này) | Status submission |
|---|---|---|---|
| P3 Vietnam | v12 Phase 9 ✅ canonical | v12 Phase 10 dịch xong (12/05/2026) | Ready for APJM submission |
| P4 Singapore | v8 Phase 9 ✅ canonical | v8 Phase 10 dịch xong (12/05/2026) | Ready for MIR submission |
| P5 China | v2.0 Phase 9 ✅ canonical | v9 Phase 10 dịch xong (12/05/2026) | Ready for IJoEM submission |

## Hạn chế của bản dịch

- Bản dịch tiếng Việt KHÔNG thay thế bản tiếng Anh trong submission tới tạp chí quốc tế. Bản VI là internal reference cho Hội đồng CTU.
- Mọi thay đổi nội dung khoa học (số liệu, hypothesis, results) chỉ được áp dụng cho bản EN. Bản VI cần re-sync khi bản EN có revision đáng kể.
- Bảng dữ liệu giữ nguyên format EN — chỉ caption + headers Việt hóa.

## Sync với bản EN

Khi bản EN có revision mới:
```bash
# So sánh phiên bản VI vs EN canonical
diff -u manuscripts/p3_vietnam_en_clean.md manuscripts/vi/p3_vietnam_vi_v12.md
# Rerun translation pipeline nếu cần
```
