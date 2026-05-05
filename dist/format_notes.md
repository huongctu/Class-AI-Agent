# Quy chuẩn format áp dụng cho dossier luận án

## 1. Format CTU cho luận án và 2 chuyên đề

Tham chiếu: Quy định hình thức luận án tiến sĩ, Trường Kinh tế, Đại học Cần Thơ.

| Thông số | Giá trị |
|---|---|
| Khổ giấy | A4 (21cm × 29.7cm), portrait |
| Lề trái | 3 cm |
| Lề phải | 2 cm |
| Lề trên | 2 cm |
| Lề dưới | 2 cm |
| Font chính | Times New Roman |
| Cỡ chữ thân | 13 pt |
| Cỡ chữ Heading 1 | 16 pt, bold |
| Cỡ chữ Heading 2 | 14 pt, bold |
| Cỡ chữ Heading 3 | 13 pt, bold |
| Màu chữ | Đen (#000000) |
| Căn lề | Justify (canh đều) |
| Line spacing | 1.5 |
| Đánh số trang | Cuối trang, giữa |
| Đánh số mục | Tối đa 3 cấp (1.1, 1.1.1) |
| Số bảng/hình | Theo chương (Bảng 4.1, Hình 4.1) |
| Trích dẫn | APA 7th |

## 2. Format bài báo tiếng Anh (P3, P4)

Tham chiếu: Submission guidelines của các tạp chí International Business mainstream (JIBS, GSJ, IBR, JBR, JWB).

| Thông số | Giá trị |
|---|---|
| Khổ giấy | A4 |
| Lề | 2.5 cm tất cả các cạnh |
| Font | Times New Roman 12 pt |
| Màu chữ | Đen |
| Căn lề | Justify |
| Line spacing | 1.15 |
| Trích dẫn | APA 7th (in-text + reference list) |

## 3. Quy ước citation APA 7th

### In-text citation

- 1 tác giả: `(Barney, 1991)` hoặc `Barney (1991)`
- 2 tác giả: `(Johanson & Vahlne, 2009)` hoặc `Johanson và Vahlne (2009)` (VI)
- 3+ tác giả: `(Marano et al., 2016)` ngay từ trích đầu tiên
- Nhiều nguồn cùng ngoặc: alphabet `(Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016)`
- Tiếng Việt: tên tác giả dạng "Đỗ và Phan (2026 — VEFR)" để phân biệt giữa nhiều công trình cùng năm

### Reference list

- Sắp xếp alphabet theo họ tác giả đầu tiên
- 2 tác giả: dùng "&" giữa hai tên
- 3-20 tác giả: liệt kê đầy đủ, dùng "&" trước tên cuối
- 21+ tác giả: liệt kê 19 đầu, "...", và tác giả cuối
- Mỗi entry có DOI khi có sẵn (định dạng `https://doi.org/...`)
- Italic cho tên tạp chí và tên sách
- Volume in italic, issue in normal: `*Journal of International Business Studies, 50*(8), 1372–1387`

## 4. Quy ước trang bìa CTU (cho luận án và CĐ)

```
BỘ GIÁO DỤC VÀ ĐÀO TẠO
TRƯỜNG ĐẠI HỌC CẦN THƠ
TRƯỜNG KINH TẾ

─────────────

ĐỖ THÙY HƯƠNG

[LOẠI TÀI LIỆU]
[VD: LUẬN ÁN TIẾN SĨ / CHUYÊN ĐỀ TIẾN SĨ SỐ 1]

[TÊN ĐỀ TÀI THEO QĐ CHÍNH THỨC]

Ngành: Quản trị kinh doanh
Mã ngành: 9340101
Mã nghiên cứu sinh: P1323001

NGƯỜI HƯỚNG DẪN KHOA HỌC
[TÊN HD]

Cần Thơ, năm [năm bảo vệ]
```

## 5. Lưu ý khi chỉnh sửa DOCX trực tiếp

- DOCX trong dossier này được build qua Pandoc + python-docx với CTU style template
- Khi mở trong Word, các style đã được set sẵn (Normal, Heading 1, Heading 2, ...)
- Để giữ tính nhất quán, khi thêm nội dung mới, **dùng Style menu** thay vì format bằng tay
- Để áp dụng style cho đoạn mới: chọn đoạn → Home → Styles → chọn "Normal" hoặc "Heading 1/2/3"
- Tránh dùng *Bold/Italic* trực tiếp ngoài context của citation/emphasis

## 6. Chuyển đổi giữa các format

```bash
# DOCX → PDF (cần libreoffice)
libreoffice --headless --convert-to pdf "file.docx"

# MD → DOCX với template CTU
pandoc -f gfm -t docx \
  --reference-doc=templates/ctu_thesis_reference.docx \
  "input.md" -o "output.docx"

# DOCX → PDF qua Word (manual): File → Save As → PDF
```

## 7. Trạng thái build

- **Pandoc version yêu cầu**: 3.x+
- **python-docx**: 1.0+
- **CTU template**: `ctu_thesis_reference.docx` (lề 3-2-2-2, TNR 13pt, justify, 1.5 spacing, đen)
- **Paper template**: `ctu_paper_reference.docx` (lề 2.5cm, TNR 12pt, justify, 1.15 spacing, đen)
- **Tổng số DOCX dự kiến**: 27 file
- **Tổng dung lượng**: ~1.2 MB

## 8. Phạm vi build

### Đã build (trong dossier này)
- 5 file plan luận án (Ch.0-4, references)
- CĐ1: 1 outline + 3 phần nội dung (file 12, 14, 15, 16)
- CĐ2: 1 outline + 3 phần nội dung (file 13, 17, 18, 19)
- Manuscripts: P3 Vietnam (VI cô đọng + EN clean), P4 Singapore (VI cô đọng + EN clean)
- Results 4 công trình: P1, P2, P_India, P_Meta
- Tham chiếu: QĐ 4768/4769, published works index, TLTQ, review report

### Không build (NCS chưa yêu cầu hoặc chưa có)
- **P5 China 2012-2024**: NCS đã upload nhưng "chưa kiểm tra kết quả" — sẽ build sau khi review
- **P8 Pacific SIDS**: bản thảo REVISED v2 — chưa convert
- **Bản full word-by-word VI cho P3, P4**: dossier hiện chứa bản cô đọng; bản full sẽ commit và build riêng
- **PDF**: NCS có thể tự convert qua Word/LibreOffice
- **Bản nộp chính thức**: chưa có trang bìa CTU đầy đủ, lời cam đoan, mục lục Word — NCS bổ sung khi xuất bản chính thức
