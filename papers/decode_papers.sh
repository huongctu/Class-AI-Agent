#!/bin/bash
# decode_papers.sh — Decode 4 papers (LATEST GitHub versions) from base64 chunks to .docx
# v2: Uses authoritative versions from source branches (not local /tmp)
# Usage: bash decode_papers.sh [output_dir]

set -e
OUT="${1:-papers_decoded}"
mkdir -p "$OUT"
cd "$OUT"

BASE="https://raw.githubusercontent.com/huongctu/Class-AI-Agent/refs/heads/claude/asia-internationalization-performance-2cYgO"

echo "=== P3 Singapore (Manuscript_Blinded_MIR_2_revised — LATEST từ claude/p3-r3-revision, 1.18 MB) ==="
for i in 00 01; do
  curl -sLO "$BASE/papers/p3-singapore/manuscript/Manuscript_Blinded_MIR_2_revised.docx.b64.part$i"
done
cat Manuscript_Blinded_MIR_2_revised.docx.b64.part00 Manuscript_Blinded_MIR_2_revised.docx.b64.part01 | base64 -d > Manuscript_Blinded_MIR_2_revised.docx
rm Manuscript_Blinded_MIR_2_revised.docx.b64.part0*
echo "  ✓ Manuscript_Blinded_MIR_2_revised.docx ($(wc -c < Manuscript_Blinded_MIR_2_revised.docx) bytes)"

echo "=== P4 Vietnam BLINDED (manuscript_blinded — LATEST từ claude/update-p4-draft-W6UKL, 2.0 MB) ==="
for i in 00 01 02 03; do
  curl -sLO "$BASE/papers/p4-vietnam/manuscript/manuscript_blinded.docx.b64.part$i"
done
cat manuscript_blinded.docx.b64.part00 manuscript_blinded.docx.b64.part01 manuscript_blinded.docx.b64.part02 manuscript_blinded.docx.b64.part03 | base64 -d > manuscript_blinded.docx
rm manuscript_blinded.docx.b64.part0*
echo "  ✓ manuscript_blinded.docx ($(wc -c < manuscript_blinded.docx) bytes)"

echo "=== P4 Vietnam FULL (manuscript_full_with_authors — LATEST, 2.0 MB) ==="
for i in 00 01 02 03; do
  curl -sLO "$BASE/papers/p4-vietnam/manuscript/manuscript_full_with_authors.docx.b64.part$i"
done
cat manuscript_full_with_authors.docx.b64.part00 manuscript_full_with_authors.docx.b64.part01 manuscript_full_with_authors.docx.b64.part02 manuscript_full_with_authors.docx.b64.part03 | base64 -d > manuscript_full_with_authors.docx
rm manuscript_full_with_authors.docx.b64.part0*
echo "  ✓ manuscript_full_with_authors.docx ($(wc -c < manuscript_full_with_authors.docx) bytes)"

echo "=== P5 China (manuscript_v1_8_blinded — fresh compile từ 6 markdown parts, 45 KB) ==="
curl -sLO "$BASE/papers/p5-china/manuscript/manuscript_v1_8_blinded.docx.b64"
base64 -d manuscript_v1_8_blinded.docx.b64 > manuscript_v1_8_blinded.docx
rm manuscript_v1_8_blinded.docx.b64
echo "  ✓ manuscript_v1_8_blinded.docx ($(wc -c < manuscript_v1_8_blinded.docx) bytes)"

echo "=== Luận án đề xuất 5 chương (compiled từ files 21+22A+22B+22C+22D, 75 KB) ==="
curl -sLO "$BASE/dist/luan_an_5_chuong_v1.docx.b64"
base64 -d luan_an_5_chuong_v1.docx.b64 > luan_an_5_chuong_v1.docx
rm luan_an_5_chuong_v1.docx.b64
echo "  ✓ luan_an_5_chuong_v1.docx ($(wc -c < luan_an_5_chuong_v1.docx) bytes)"

echo ""
echo "Done — 5 files ready in: $OUT/"
ls -la *.docx
