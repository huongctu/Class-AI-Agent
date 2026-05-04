#!/usr/bin/env bash
# P5 China v1.5 — one-shot manuscript .docx builder
#
# Generates manuscript_v1_5.docx with all 4 figures embedded inline.
# Outputs: manuscript_v1_5.docx (~770 KB) ready for journal upload.
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

echo "[3/4] Assembling 6 manuscript parts + injecting figure references..."
cat \
    manuscript_v1_5_part1_frontmatter_intro.md \
    manuscript_v1_5_part2_theory.md \
    manuscript_v1_4_part3_data_methods.md \
    manuscript_v1_4_part4_results.md \
    manuscript_v1_5_part5_discussion.md \
    manuscript_v1_5_part6_limits_refs.md \
    > manuscript_v1_5_complete.md

python3 - <<'PY'
import re
with open('manuscript_v1_5_complete.md') as f: t = f.read()
for pat, rep in [
    (r'(> \*\*Figure 1\.\*\*)', r'![Figure 1: Conceptual model](figures/figure1_v1_4.png)\n\n\1'),
    (r'(> \*\*Figure 2\.\*\*)', r'![Figure 2: Threshold forest plot](figures/figure2_threshold_forest.png)\n\n\1'),
    (r'(> \*\*Figure 3\.\*\*)', r'![Figure 3: Predicted curves](figures/figure3_predicted_curves.png)\n\n\1'),
    (r'(> \*\*Figure 4\.\*\*)', r'![Figure 4: Level-shift bars](figures/figure4_level_shift_bars.png)\n\n\1'),
]:
    t = re.sub(pat, rep, t, count=1)
with open('manuscript_v1_5_with_figures.md','w') as f: f.write(t)
print('      saved manuscript_v1_5_with_figures.md')
PY

echo "[4/4] Converting to .docx via pandoc..."
if command -v pandoc &>/dev/null; then
  pandoc manuscript_v1_5_with_figures.md \
    --resource-path=. \
    -o manuscript_v1_5.docx
  echo ""
  echo "✅ BUILD COMPLETE: manuscript_v1_5.docx ($(du -h manuscript_v1_5.docx | cut -f1))"
  echo "   Ready to upload to APJM (or alternative target — see SUBMISSION_TARGETS.md)"
else
  echo "      [ERROR] pandoc not installed. Install via:"
  echo "        macOS:    brew install pandoc"
  echo "        Ubuntu:   apt install pandoc"
  echo "        Windows:  https://pandoc.org/installing.html"
  exit 1
fi
