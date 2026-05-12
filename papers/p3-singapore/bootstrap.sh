#!/bin/bash
# P3 Singapore — Bootstrap script to fetch binary files from source branch
#
# Usage (after cloning thesis branch):
#   cd papers/p3-singapore/
#   bash bootstrap.sh
#
# Downloads 5 binary submission files from claude/p3-r3-revision branch
# into manuscript/ + figures/ subfolders. Then optionally regenerates
# the FIGFIXED manuscript (with corrected hypothesis numbering) by
# running fix_r3_post_revision.py + regenerate_fig1.py.

set -euo pipefail
cd "$(dirname "$0")"

BASE="https://raw.githubusercontent.com/huongctu/Class-AI-Agent/claude/p3-r3-revision/papers/p3-singapore"

mkdir -p manuscript figures

echo "[1/5] Downloading R3 reference manuscript..."
curl -fsSL -o manuscript/Manuscript_Blinded_MIR_2_revised.docx "${BASE}/Manuscript_Blinded_MIR_2_revised.docx"

echo "[2/5] Downloading Cover Letter..."
curl -fsSL -o manuscript/Cover_Letter.docx "${BASE}/Cover_Letter.docx"

echo "[3/5] Downloading Title Page..."
curl -fsSL -o manuscript/Title_Page.docx "${BASE}/Title_Page.docx"

echo "[4/5] Downloading Figure 2 (DAI marginal effect)..."
curl -fsSL -o figures/figure2_dai_marginal.png "${BASE}/submission/figures/Figure2_DAI_Marginal_Effect.png"

echo "[5/5] Downloading Figure 3 (predicted I-P curve)..."
curl -fsSL -o figures/figure3_predicted_curve.png "${BASE}/submission/figures/Figure3_IP_Predicted_Curve.png"

echo ""
echo "Optional: regenerate FIGFIXED manuscript with corrected hypothesis numbering"
echo "  pip install python-docx==1.2.0 matplotlib pillow"
echo "  cd manuscript/"
echo "  python3 ../replication/fix_r3_post_revision.py"
echo "  cd ../figures/source/"
echo "  python3 regenerate_fig1.py"
echo "  # Then merge fig1_FIXED.png into Manuscript_R3_FIXED.docx → manuscript_R3_FIGFIXED.docx"
echo "  # See replication/README.md Step 3 for full procedure"
echo ""
echo "✓ Bootstrap complete. Files in manuscript/ + figures/"
echo ""
echo "Submission-ready files for MIR portal upload:"
echo "  - manuscript/manuscript_R3_FIGFIXED.docx (after running regen scripts)"
echo "  - manuscript/Cover_Letter.docx"
echo "  - manuscript/Title_Page.docx"
echo "  - figures/figure1_conceptual_model.png (= fig1_FIXED.png after regen)"
echo "  - figures/figure2_dai_marginal.png"
echo "  - figures/figure3_predicted_curve.png"
