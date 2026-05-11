#!/bin/bash
# build_docx.sh — Chuyển markdown CĐ2 sang Word .docx theo format CTU QĐ 1799/SH
# Mirror cd1/build_docx.sh — pipeline pandoc → apply CTU format
set -e
cd "$(dirname "$0")/../.."

SRC="thesis/cd2/00_cd2_complete_vi.md"
OUT="thesis/cd2/00_cd2_complete_vi.docx"

echo "→ [1/2] Pandoc convert: $SRC → $OUT"
pandoc "$SRC" \
    --from markdown+pipe_tables+raw_html \
    --to docx \
    --toc \
    --toc-depth=3 \
    -o "$OUT" 2>&1 | grep -v "Could not fetch resource figures" || true

echo "→ [2/2] Apply CTU format (TNR 13pt | 1.2 spacing | margins L:3cm Others:2cm)"
python3 scripts/apply_ctu_format.py "$OUT"

echo ""
echo "✓ Hoàn tất. Mở $OUT trong Word/LibreOffice."
echo ""
echo "Bước trong Word trước khi nộp:"
echo "  1. F9 (Update field) để refresh mục lục"
echo "  2. Kiểm tra danh mục bảng + hình + từ viết tắt"
echo "  3. Insert hình minh họa từ thesis/figures/ vào đúng vị trí"
echo "  4. Save As .docx final"
