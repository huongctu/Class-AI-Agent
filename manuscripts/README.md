# Bản thảo bài báo công bố quốc tế (manuscripts)

Thư mục này chứa các bản thảo bài báo công bố quốc tế của NCS Đỗ Thùy Hương, là nguồn dữ liệu/bằng chứng nội bộ cho luận án tiến sĩ. Theo Quyết định 4769/QĐ-ĐHCT ngày 15/10/2024 của Hiệu trưởng Trường Đại học Cần Thơ, tên luận án chính thức là **"Quốc tế hóa và hiệu quả hoạt động kinh doanh của các doanh nghiệp ở Châu Á"**, do PGS.TS. Phan Anh Tú hướng dẫn.

> **Lưu ý**: Thư mục `manuscripts/` lưu **bản tiếng Việt học thuật** dùng làm bằng chứng nội bộ cho luận án (Chương 4). Bộ hồ sơ submission đầy đủ (manuscript tiếng Anh + figures + tables + replication scripts + audit reports) cho 3 bản thảo đang chuẩn bị (**P3 Singapore — MIR**, **P4 Vietnam — IJoEM**, **P5 China — APJM**) được lưu tại [`../papers/`](../papers/) — xem [`papers/README.md`](../papers/README.md) để có overview.

## Cấu trúc thư mục

| File | Nội dung | Ngôn ngữ |
|---|---|---|
| [`QD_legal_reference.md`](QD_legal_reference.md) | Tham chiếu pháp lý chính thức (QĐ 4768 giao chuyên đề + QĐ 4769 điều chỉnh tên LATS) | VI |
| [`p3_vietnam_vi.md`](p3_vietnam_vi.md) | **Vietnam manuscript — bản tiếng Việt học thuật** (3 đợt 2009/2015/2023, n=2.958) | VI |
| [`p4_singapore_vi.md`](p4_singapore_vi.md) | **Singapore manuscript — bản tiếng Việt học thuật** (đợt 2023, n=623) | VI |
| `p3_vietnam_en_clean.md` | Vietnam manuscript — bản tiếng Anh đã chuẩn hóa (commit kế tiếp) | EN |
| `p4_singapore_en_clean.md` | Singapore manuscript — bản tiếng Anh đã chuẩn hóa (commit kế tiếp) | EN |

## Quan hệ với luận án

- **P3 Vietnam manuscript** → đi vào **Chương 4 Mục 4.2** (bằng chứng country-level cho transitional economy với TCI vs DAI; phát hiện stage-contingent digital value 2009→2015→2023). Submission package đầy đủ (v5.9 IJoEM, 27 edits) tại [`../papers/p4-vietnam/`](../papers/p4-vietnam/).
- **P4 Singapore manuscript** → đi vào **Chương 4 Mục 4.2** (bằng chứng country-level ASEAN benchmark cho digitally advanced economy; phát hiện DAI as conditional scaling resource). Submission package đầy đủ (R3 MIR, 12 patches + Figure 1 regen) tại [`../papers/p3-singapore/`](../papers/p3-singapore/).
- **P5 China manuscript** → đi vào **Chương 4 Mục 4.3** (bằng chứng temporal heterogeneity 2012↔2024; cross-tier comparison). Submission package đầy đủ (v1.8 APJM, 42/42 references verified) tại [`../papers/p5-china/`](../papers/p5-china/).

## Lưu ý về tên file

File gốc do NCS upload: `manuscript_blinded_3.docx` (= **Vietnam paper**) và `01_Manuscript_4.docx` (= **Singapore paper**). Tên file không khớp với numbering theo plan luận án: P3 = Singapore (theo plan), P4 = Vietnam (theo plan). Để minh bạch, thư mục này gọi chúng theo **nội dung quốc gia thực tế**: `p3_vietnam_*.md` và `p4_singapore_*.md`.

## Quy chuẩn học thuật

- Bản tiếng Việt: theo chuẩn học thuật APA 7th, ngôn ngữ học thuật (không khẩu ngữ), trình bày 5–7 mục chính (Tóm tắt, Giới thiệu, Cơ sở lý thuyết, Phương pháp, Kết quả, Thảo luận, Kết luận).
- Bản tiếng Anh: standardized academic English, fix grammar/style minor, giữ nguyên cấu trúc và bằng chứng thực nghiệm.
- Trích dẫn: tất cả các tham chiếu giữ nguyên format APA 7th theo bản gốc.
