# Khung luận án — Internationalization and Firm Performance in Asian Countries

## Thông tin chung

- **Tên đề tài (VI)**: Quốc tế hóa và hiệu quả hoạt động kinh doanh của doanh nghiệp ở các quốc gia châu Á
- **Tên đề tài (EN)**: Internationalization and Firm Performance in Asian Countries
- **Nghiên cứu sinh**: Đỗ Thùy Hương (Mã NCS: P1323001)
- **Người hướng dẫn khoa học**: PGS.TS. Phan Anh Tú
- **Đơn vị đào tạo**: Trường Kinh tế, Đại học Cần Thơ
- **Loại hình**: Luận án tích lũy (cumulative thesis), 5 chương
- **Ngôn ngữ luận án**: Tiếng Việt; các bản thảo bài báo công bố quốc tế viết bằng tiếng Anh

## Mục đích thư mục `/thesis/`

Thư mục này lưu **tài liệu khung umbrella** của luận án — gồm dàn ý chương, định vị các paper thành phần và danh mục công trình có liên quan. Code phân tích Stata và bản thảo manuscript được lưu trên các nhánh chuyên biệt khác trong cùng repo (xem bảng dưới).

## Nội dung thư mục

| File | Mô tả |
|---|---|
| `README.md` | Bản đồ thư mục, status các paper, tham chiếu các nhánh chứa code/manuscript |
| `thesis_outline_vi.md` | Dàn ý chi tiết 5 chương luận án theo chuẩn CTU |
| `research_program_framing.md` | Định vị P3–P7, lập luận có citation APA 7th, song ngữ VI/EN |
| `related_publications_vi.md` | Danh mục 4 công trình đã công bố và đoạn chuẩn cho Chương 1 |

## Bản đồ các nhánh chứa code/manuscript

| Paper | Nhánh chứa | Đường dẫn |
|---|---|---|
| P3 — Singapore (analysis) | `claude/verify-stata-results-So3mf` | `scripts/P3_MIR_Singapore_Analysis.do` |
| P4 — Vietnam (manuscript) | `claude/fix-integrity-update-scope-d7rUx` | `manuscripts/p4-jwb-vietnam/` |
| P4 — Vietnam (analysis) | `claude/verify-stata-results-So3mf` | `scripts/P4_JWB_Vietnam_Analysis.do` |
| P5 — China (analysis) | `claude/verify-stata-results-So3mf` | `scripts/P5_APJM_China_Analysis.do` |
| P6 — Meta-analysis update | (tài liệu nội bộ ngoài repo) | `build_final_database.py`, `search_queries.json`, `study_database.json` |
| P7 — 25 quốc gia châu Á | (đang thiết kế) | chưa có |
| Dữ liệu pooled WBES | `main` | `data/analysis/pooled_wbes_6waves.csv` |

## Status 4 công trình có liên quan đã công bố

| # | Công trình | Năm | Loại | Ghi chú |
|---|---|---|---|---|
| 1 | *Internationalization and firm performance: A meta-analysis review* — Kỷ yếu ICBEF 2025, Vol. 2, tr. 469–489, NXB Đại học Cần Thơ, ISBN | 2025 | Conference proceedings (international) | Bài kỷ yếu nền; P6 trong luận án là bản cập nhật và mở rộng |
| 2 | *Unveiling the impact of Chinese manufacturing SMEs' internationalization on performance* — Journal of Finance and Accounting Research | 2026 | Journal article | Bài Trung Quốc, bằng chứng cơ chế phi tuyến |
| 3 | *Firm performance heterogeneity in emerging Asia* — Vietnam Economic & Financial Review | 2026 | Journal article | Bài Emerging Asia, 17 nền kinh tế, vai trò công nghệ |
| 4 | *Internationalization and firm performance of firms in India: The role of top management* — IntechOpen | 2025 | Book chapter (open access) | Bài Ấn Độ, vai trò top manager experience và gender |

## Status 5 paper trong luận án

| Paper | Bối cảnh | Câu khóa identity | Trạng thái |
|---|---|---|---|
| **P3** | Singapore — ASEAN benchmark economy | Vai trò bổ trợ của DAI trong small open economy | Bản thảo đã hoàn thiện |
| **P4** | Việt Nam — transitional economy | Technological capability và digital adoption vận hành khác nhau | Bản thảo đã hoàn thiện |
| **P5** | Trung Quốc — large emerging economy (target APJM) | Cấu trúc inverted-U có ổn định? Digital là level shifter | Đang phân tích dữ liệu, chưa viết manuscript |
| **P6** | Meta-analysis update 1982–2026 | Vì sao literature dị biệt cao, moderator nào quan trọng | Bản cập nhật và mở rộng từ bài ICBEF 2025; đang hoàn thiện cho luận án |
| **P7** | 25 quốc gia châu Á — capstone | Digital contingencies có khái quát xuyên quốc gia? | Đang thiết kế; có tùy chọn moderator phụ về top manager gender/experience |

## Phạm vi dữ liệu thực nghiệm

Luận án bao quát các nền kinh tế châu Á có dữ liệu phù hợp tại thời điểm triển khai. Nhật Bản hiện chưa có dữ liệu thực nghiệm trong khuôn khổ luận án nên không thuộc empirical scope, mặc dù literature về Nhật Bản (Lu & Beamish, 2001, 2004; Likitwongkajon & Vithessonthi, 2020) vẫn được sử dụng trong phần tổng quan tài liệu của P6.

## Quy ước branch

- `main`: nhánh chính, chứa dữ liệu pooled WBES.
- `claude/asia-internationalization-performance-2cYgO`: nhánh chứa khung umbrella luận án (thư mục này).
- `claude/<feature>-<id>`: nhánh chuyên biệt cho từng paper hoặc nhiệm vụ phụ trợ.

## Tham khảo

Các citation APA 7th cho từng lập luận khoa học được liệt kê đầy đủ trong `research_program_framing.md`.
