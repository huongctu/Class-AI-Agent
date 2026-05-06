#!/bin/bash
# P5 China — Bootstrap script to fetch full submission package from source branch
#
# Usage (after cloning thesis branch):
#   cd papers/p5-china/
#   bash bootstrap.sh
#
# Downloads từ claude/p5-china-sample-outline-1KXp4 branch:
# - 6 manuscript markdown parts (parts 1-6)
# - build_docx.sh + manuscript_v1_8_blinded.docx (compiled)
# - 6 submission markdown files
# - 4 audit reports (CITATION_AUDIT, CLAIMS_AUDIT, VERIFICATION_RESULTS, SUBMISSION_TARGETS)
# - 4 figure PNGs (figure1-4)
# - 5 figure source files (.dot, .mmd, .py, READMEs)

set -euo pipefail
cd "$(dirname "$0")"

BASE="https://raw.githubusercontent.com/huongctu/Class-AI-Agent/claude/p5-china-sample-outline-1KXp4/p5-china/apjm"

mkdir -p manuscript/parts submission audit figures figures/source replication

echo "[1/5] Downloading 6 manuscript markdown parts..."
for i in 1 2 3 4 5 6; do
  case $i in
    1) name='frontmatter_intro' ;;
    2) name='theory' ;;
    3) name='data_methods' ;;
    4) name='results' ;;
    5) name='discussion' ;;
    6) name='limits_refs' ;;
  esac
  curl -fsSL -o "manuscript/parts/manuscript_v1_8_blinded_part${i}_${name}.md" \
    "${BASE}/manuscript_v1_8_blinded_part${i}_${name}.md"
  echo "  ✓ part${i}_${name}.md"
done

echo "[2/5] Downloading build script + compiled manuscript..."
curl -fsSL -o manuscript/build_docx.sh "${BASE}/build_docx.sh"
chmod +x manuscript/build_docx.sh
curl -fsSL -o manuscript/manuscript_v1_8_blinded.docx "${BASE}/manuscript_v1_8_blinded.docx" || echo "  (may not be on source branch — run build_docx.sh to regenerate)"

echo "[3/5] Downloading 6 submission markdown files..."
for f in 00_SUBMISSION_CHECKLIST 01_title_page 02_cover_letter 03_declarations 04_blinding_check 05_suggested_reviewers; do
  curl -fsSL -o "submission/${f}.md" "${BASE}/submission/${f}.md"
  echo "  ✓ ${f}.md"
done

echo "[4/5] Downloading 4 audit reports..."
curl -fsSL -o audit/CITATION_AUDIT.md "${BASE}/CITATION_AUDIT.md"
curl -fsSL -o audit/CLAIMS_AUDIT.md "${BASE}/CLAIMS_AUDIT.md"
curl -fsSL -o audit/VERIFICATION_RESULTS.md "${BASE}/VERIFICATION_RESULTS.md"
curl -fsSL -o audit/SUBMISSION_TARGETS.md "${BASE}/SUBMISSION_TARGETS.md"

echo "[5/5] Downloading figures + sources..."
for f in figure1_v1_4 figure2_threshold_forest figure3_predicted_curves figure4_level_shift_bars; do
  curl -fsSL -o "figures/${f}.png" "${BASE}/figures/${f}.png" || true
done
# Source files
for f in figure1_conceptual_model_v1_4.dot figure1_conceptual_model_v1_4.mmd render_figures.py README.md RENDER_FIGURES_README.md; do
  curl -fsSL -o "figures/source/${f}" "${BASE}/figures/${f}" || true
done

echo ""
echo "✓ Bootstrap complete."
echo ""
echo "Next steps:"
echo "  1. Build manuscript:    cd manuscript/ && bash build_docx.sh"
echo "     (requires: pandoc, graphviz, matplotlib, numpy, pillow)"
echo "  2. Verify final docx:   ls -lh manuscript/manuscript_v1_8_blinded.docx (target ~768 KB)"
echo "  3. Check blinding:      grep -nE '(Do & Tu|huongctu|Class-AI-Agent)' manuscript/parts/*.md"
echo "     (expected: empty)"
echo ""
echo "For APJM upload, use:"
echo "  - manuscript/manuscript_v1_8_blinded.docx → APJM 'Manuscript' (blinded) slot"
echo "  - submission/01_title_page.md → APJM 'Title Page' (with author info) slot"
echo "  - submission/02_cover_letter.md → APJM 'Cover Letter' slot"
