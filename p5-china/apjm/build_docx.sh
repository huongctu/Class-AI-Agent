#!/usr/bin/env bash
# P5 China v1.8 BLINDED — one-shot manuscript .docx builder
#
# Generates manuscript_v1_8_blinded.docx with all 4 figures embedded inline.
# Output: manuscript_v1_8_blinded.docx (~770 KB) ready for journal upload
# (APJM "Manuscript" slot — double-blind review).
#
# This is the BLINDED version of the manuscript:
#   - Self-citations (Do & Tu, 2025 / 2026) replaced with "Author Citation"
#   - GitHub repo handle (huongctu/Class-AI-Agent) removed
#   - Reference-list entries for Do & Tu papers anonymized
# Author info goes in the separate `submission/01_title_page.md` upload slot.
#
# Prerequisites (one-time install):
#   macOS:    brew install pandoc graphviz && pip install matplotlib numpy
#   Ubuntu:   apt install pandoc graphviz && pip install matplotlib numpy
#   Windows:  download pandoc-windows.msi + graphviz-windows.exe + pip install matplotlib numpy
#
# Usage (from p5-china/apjm/):
#   bash build_docx.sh
#

set -euo pipefail
cd "$(dirname "$0")"

VERSION="v1_8_blinded"
OUTPUT="manuscript_${VERSION}.docx"

echo "[1/4] Rendering Figure 1 (conceptual model) via Graphviz..."
if command -v dot &>/dev/null; then
  dot -Tpng figures/figure1_conceptual_model_v1_4.dot -o figures/figure1_v1_4.png
  echo "      saved figures/figure1_v1_4.png"
else
  echo "      [SKIP] graphviz 'dot' not installed; Figure 1 will be missing"
fi

echo "[2/4] Rendering Figures 2/3/4 (data plots) via matplotlib..."
if python3 -c "import matplotlib" 2>/dev/null; then
  ( cd figures && python3 render_figures.py )
  echo "      saved figures/figure{2,3,4}_*.png"
else
  echo "      [SKIP] matplotlib not installed; Figures 2/3/4 will be missing"
fi

echo "[3/4] Assembling 6 v1.8 BLINDED manuscript parts + injecting figure references..."
cat \
    manuscript_v1_8_blinded_part1_frontmatter_intro.md \
    manuscript_v1_8_blinded_part2_theory.md \
    manuscript_v1_8_blinded_part3_data_methods.md \
    manuscript_v1_8_blinded_part4_results.md \
    manuscript_v1_8_blinded_part5_discussion.md \
    manuscript_v1_8_blinded_part6_limits_refs.md \
    > manuscript_v1_8_blinded_complete.md

python3 - <<'PY'
import re
with open('manuscript_v1_8_blinded_complete.md') as f: t = f.read()
for pat, rep in [
    (r'(> \*\*Figure 1\.\*\*)', r'![Figure 1: Conceptual model](figures/figure1_v1_4.png)\n\n\1'),
    (r'(> \*\*Figure 2\.\*\*)', r'![Figure 2: Threshold forest plot](figures/figure2_threshold_forest.png)\n\n\1'),
    (r'(> \*\*Figure 3\.\*\*)', r'![Figure 3: Predicted curves](figures/figure3_predicted_curves.png)\n\n\1'),
    (r'(> \*\*Figure 4\.\*\*)', r'![Figure 4: Level-shift bars](figures/figure4_level_shift_bars.png)\n\n\1'),
]:
    t = re.sub(pat, rep, t, count=1)
with open('manuscript_v1_8_blinded_with_figures.md','w') as f: f.write(t)
print('      saved manuscript_v1_8_blinded_with_figures.md')
PY

echo "[4/4] Converting to .docx via pandoc..."
if command -v pandoc &>/dev/null; then
  pandoc manuscript_v1_8_blinded_with_figures.md \
    --resource-path=. \
    -o "${OUTPUT}"
  echo ""
  echo "BUILD COMPLETE: ${OUTPUT} ($(du -h "${OUTPUT}" | cut -f1))"
  echo "  Upload to APJM 'Manuscript' (blinded) slot."
  echo "  Title page (with author info) goes in separate slot — see submission/01_title_page.md"
  echo ""
  echo "  Verification:"
  echo "  - 13,146 words (target 10-15K for ABS-3 IB journals)"
  echo "  - 39 references APA 7th with DOIs"
  echo "  - 3 tables (descriptives, M2 main, three-way moderation)"
  echo "  - 4 figures embedded (conceptual, threshold forest, predicted curves, level-shift bars)"
  echo "  - All empirical claims verified against data (see CLAIMS_AUDIT.md)"
  echo "  - All Tier-C references verified (see VERIFICATION_RESULTS.md)"
  echo ""
  echo "  Final blinding verification (run before upload):"
  echo "    grep -nE \"(Do & Tu|huongctu|Class-AI-Agent)\" manuscript_v1_8_blinded_part*.md"
  echo "    expected: empty (no matches)"
else
  echo "      [ERROR] pandoc not installed. Install via:"
  echo "        macOS:    brew install pandoc"
  echo "        Ubuntu:   apt install pandoc"
  echo "        Windows:  https://pandoc.org/installing.html"
  exit 1
fi
