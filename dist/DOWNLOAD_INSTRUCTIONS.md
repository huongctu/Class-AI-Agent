# HƯỚNG DẪN TẢI XUỐNG DOSSIER

## Cách nhanh nhất — Download từng MD từ GitHub UI

NCS truy cập vào branch `claude/asia-internationalization-performance-2cYgO` tại:

https://github.com/huongctu/Class-AI-Agent/tree/claude/asia-internationalization-performance-2cYgO

### Download trực tiếp từng file (chỉ cần trong trình duyệt)

1. Mở URL trên trong trình duyệt
2. Vào folder `thesis/` hoặc `manuscripts/`
3. Click vào file `.md` muốn tải
4. Click nút **Raw**
5. Right-click → **Save As** → luưu về máy

### Download toàn bộ branch dưới dạng zip

Tại URL trên, click nút xanh **Code** → **Download ZIP**. Zip này bao gồm toàn bộ source MD + scripts (~600KB).

## Cách đầy đủ — Build DOCX từ source

Xem hướng dẫn chi tiết ở [`templates/README.md`](../templates/README.md) và [`00_README.md`](00_README.md).

Tóm tắt 5 bước:

```bash
# 1. Clone repo (hoặc giải nén zip download từ GitHub)
git clone -b claude/asia-internationalization-performance-2cYgO https://github.com/huongctu/Class-AI-Agent.git
cd Class-AI-Agent

# 2. Cài Pandoc + python-docx
#    Pandoc: https://pandoc.org/installing.html
pip install python-docx

# 3. Tạo pandoc default reference
pandoc -o /tmp/pandoc_default.docx --print-default-data-file reference.docx

# 4. Build CTU template
python3 templates/build_ctu_reference.py /tmp/pandoc_default.docx templates/

# 5. Convert MD → DOCX (xuất vào dist/)
bash templates/build_dist.sh
```

Kết quả:
- `dist/luan_an/` — 5 file DOCX luận án
- `dist/chuyen_de_1/`, `dist/chuyen_de_2/` — file DOCX 2 chuyên đề
- `dist/manuscripts/` — manuscripts P3, P4 + results 4 công trình
- Tổng 27 file DOCX (~1.2 MB)

## Phương án đơn giản nhất — Yêu cầu Claude Code

Nếu không tiện cài Pandoc, NCS có thể yêu cầu Claude Code support trong phiên session tiếp theo:

> "Hãy push 2 CTU template DOCX (binary, ~10KB mỗi) vào `templates/` qua chunked base64. Sau đó cho NCS hướng dẫn decode 1 lần."

Claude sẽ encode 2 file template binary (10KB mỗi) thành base64 và chia ~14 chunks, push từng chunk. NCS sau đó chạy 1 lệnh decode để có template binary, sau đó chạy `bash templates/build_dist.sh` để có toàn bộ 27 DOCX.

Hoặc, nếu ưu tiên tốc độ: NCS có thể mở từng MD trong Microsoft Word và set format CTU manual (Page Setup + Font + Paragraph) — mất ~30 phút cho toàn bộ dossier.
