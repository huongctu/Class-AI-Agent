#!/bin/bash
# decode_papers.sh — Decode 3 papers from base64 chunks to .docx files
# Usage: bash decode_papers.sh [output_dir]
# Output: 3 .docx files ready to print/submit

set -e
OUT="${1:-papers_decoded}"
mkdir -p "$OUT"
cd "$OUT"

BASE="https://raw.githubusercontent.com/huongctu/Class-AI-Agent/refs/heads/claude/asia-internationalization-performance-2cYgO"

echo "=== P3 Singapore (R3 FIGFIXED, 1.1 MB) ==="
curl -sLO "$BASE/papers/p3-singapore/manuscript/Manuscript_R3_FIGFIXED.docx.b64.part00"
curl -sLO "$BASE/papers/p3-singapore/manuscript/Manuscript_R3_FIGFIXED.docx.b64.part01"
cat Manuscript_R3_FIGFIXED.docx.b64.part00 Manuscript_R3_FIGFIXED.docx.b64.part01 | base64 -d > Manuscript_R3_FIGFIXED.docx
rm Manuscript_R3_FIGFIXED.docx.b64.part0*
echo "  ✓ Manuscript_R3_FIGFIXED.docx ($(wc -c < Manuscript_R3_FIGFIXED.docx) bytes)"

echo "=== P4 Vietnam (v5.9 FIXED, 2.0 MB) ==="
for i in 00 01 02 03; do
  curl -sLO "$BASE/papers/p4-vietnam/manuscript/manuscript_v5_9_FIXED.docx.b64.part$i"
done
cat manuscript_v5_9_FIXED.docx.b64.part00 manuscript_v5_9_FIXED.docx.b64.part01 manuscript_v5_9_FIXED.docx.b64.part02 manuscript_v5_9_FIXED.docx.b64.part03 | base64 -d > manuscript_v5_9_FIXED.docx
rm manuscript_v5_9_FIXED.docx.b64.part0*
echo "  ✓ manuscript_v5_9_FIXED.docx ($(wc -c < manuscript_v5_9_FIXED.docx) bytes)"

echo "=== P5 China (v1.8 blinded, 45 KB) ==="
curl -sLO "$BASE/papers/p5-china/manuscript/manuscript_v1_8_blinded.docx.b64"
base64 -d manuscript_v1_8_blinded.docx.b64 > manuscript_v1_8_blinded.docx
rm manuscript_v1_8_blinded.docx.b64
echo "  ✓ manuscript_v1_8_blinded.docx ($(wc -c < manuscript_v1_8_blinded.docx) bytes)"

echo ""
echo "Done — 3 papers ready in: $OUT/"
ls -la *.docx
