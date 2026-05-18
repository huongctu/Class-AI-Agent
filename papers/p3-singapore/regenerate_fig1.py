"""
Regenerate Figure 1 (Conceptual model) for P3 Singapore R3 manuscript
with corrected hypothesis numbering.

Original numbering (in image3.png inside Manuscript_Blinded_MIR_2_revised.docx):
  - H2: TCI x FSTS (open empirical question)  <- TCI moderation arrow
  - H4: DAI x FSTS (stronger at high FSTS)    <- DAI moderation arrow
  - Bottom: "H1: TCI ...; H3: DAI ..."

Corrected (consecutive H1, H2, H3 after R3 H2-demotion):
  - TCI x FSTS (open empirical question)      <- no H number; demoted in R3
  - H3: DAI x FSTS (stronger at high FSTS)    <- was H4
  - Bottom: "H1: TCI ...; H2: DAI ..."        <- H3 was renumbered to H2

Usage:
    pip install matplotlib pillow
    python3 regenerate_fig1.py
    # Output: fig1_FIXED.png

Then replace word/media/image3.png inside the .docx zip:
    import zipfile, shutil, os, tempfile
    src = "Manuscript_Blinded_MIR_2_revised.docx"
    dst = "Manuscript_R3_FIGFIXED.docx"
    shutil.copy(src, dst)
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(src, 'r') as z: z.extractall(tmp)
    shutil.copy('fig1_FIXED.png', os.path.join(tmp, 'word', 'media', 'image3.png'))
    os.remove(dst)
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(tmp):
            for f in files:
                z.write(os.path.join(root, f), os.path.relpath(os.path.join(root, f), tmp))
"""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Match the original aspect ratio (2077x1426)
fig, ax = plt.subplots(figsize=(13.85, 9.5), dpi=150)
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.axis('off')

# Color palette matching original
COLOR_TCI_FILL = '#D6E8F5'
COLOR_TCI_EDGE = '#5B9BD5'
COLOR_DAI_FILL = '#FCE4D6'
COLOR_DAI_EDGE = '#ED7D31'
COLOR_IV_FILL = '#E7E6E6'
COLOR_IV_EDGE = '#7F7F7F'
COLOR_DV_FILL = '#E2EFD9'
COLOR_DV_EDGE = '#548235'
COLOR_CTL_FILL = '#FFF2CC'
COLOR_CTL_EDGE = '#BF8F00'
COLOR_TEXT = '#1F1F1F'

# Title
fig.text(0.5, 0.965, 'Figure 1. Conceptual model',
         ha='center', fontsize=14, fontweight='bold')
fig.text(0.5, 0.945,
         'Internationalization -> Firm Performance, moderated by technological capability and digital adoption',
         ha='center', fontsize=10, color='#3F3F3F')

# Legend top right (Direct vs Moderation)
fig.text(0.95, 0.965, '--- Direct association', ha='right', fontsize=9, color='#1F1F1F')
fig.text(0.95, 0.945, '- - - Moderation association', ha='right', fontsize=9, color='#1F1F1F')

# === MODERATORS section (top) ===
fig.text(0.06, 0.905, 'MODERATORS', fontsize=10, fontweight='bold', color='#7030A0')

# TCI box (top left)
tci_box = FancyBboxPatch((10, 75), 30, 12,
                         boxstyle='round,pad=0.5,rounding_size=2',
                         linewidth=2.5, edgecolor=COLOR_TCI_EDGE,
                         facecolor=COLOR_TCI_FILL)
ax.add_patch(tci_box)
ax.text(25, 84, 'Technological Capability (TCI)', ha='center', va='center',
        fontsize=11.5, fontweight='bold', color=COLOR_TEXT)
ax.text(25, 78.5, 'Lall 1992; Cohen & Levinthal 1990',
        ha='center', va='center', fontsize=9, style='italic', color='#5F5F5F')

# DAI box (top right)
dai_box = FancyBboxPatch((60, 75), 30, 12,
                         boxstyle='round,pad=0.5,rounding_size=2',
                         linewidth=2.5, edgecolor=COLOR_DAI_EDGE,
                         facecolor=COLOR_DAI_FILL)
ax.add_patch(dai_box)
ax.text(75, 84, 'Digital Adoption (DAI)', ha='center', va='center',
        fontsize=11.5, fontweight='bold', color=COLOR_TEXT)
ax.text(75, 78.5, 'Bharadwaj et al. 2013; Verhoef et al. 2021',
        ha='center', va='center', fontsize=9, style='italic', color='#5F5F5F')

# === Hypothesis labels on moderator arrows ===
# CHANGE: TCI moderation no longer numbered (was H2, demoted in R3)
tci_arrow_label = FancyBboxPatch((14, 64), 22, 6,
                                  boxstyle='round,pad=0.3',
                                  linewidth=1.5, edgecolor=COLOR_TCI_EDGE,
                                  facecolor='white')
ax.add_patch(tci_arrow_label)
ax.text(25, 68, 'TCI x FSTS', ha='center', va='center',
        fontsize=10, fontweight='bold', color=COLOR_TCI_EDGE)
ax.text(25, 65, '(open empirical question)', ha='center', va='center',
        fontsize=8.5, style='italic', color='#5F5F5F')

# CHANGE: H4 -> H3 for DAI moderation
dai_arrow_label = FancyBboxPatch((64, 64), 22, 6,
                                  boxstyle='round,pad=0.3',
                                  linewidth=1.5, edgecolor=COLOR_DAI_EDGE,
                                  facecolor='white')
ax.add_patch(dai_arrow_label)
ax.text(75, 68, 'H3: DAI x FSTS', ha='center', va='center',
        fontsize=10, fontweight='bold', color=COLOR_DAI_EDGE)
ax.text(75, 65, '(stronger at high FSTS)', ha='center', va='center',
        fontsize=8.5, style='italic', color='#5F5F5F')

# === Independent Variable box (left) ===
fig.text(0.06, 0.555, 'INDEPENDENT VARIABLE', fontsize=10, fontweight='bold', color='#1F1F1F')

iv_box = FancyBboxPatch((6, 40), 35, 12.5,
                        boxstyle='round,pad=0.5,rounding_size=2',
                        linewidth=2.5, edgecolor=COLOR_IV_EDGE,
                        facecolor=COLOR_IV_FILL)
ax.add_patch(iv_box)
ax.text(23.5, 49, 'Internationalization', ha='center', va='center',
        fontsize=12.5, fontweight='bold', color=COLOR_TEXT)
ax.text(23.5, 45, 'FSTS = foreign sales / total sales', ha='center', va='center',
        fontsize=9, style='italic', color='#5F5F5F')
ax.text(23.5, 42.5, '(linear and quadratic terms)', ha='center', va='center',
        fontsize=8.5, style='italic', color='#5F5F5F')

# === Dependent Variable box (right) ===
fig.text(0.595, 0.555, 'DEPENDENT VARIABLE', fontsize=10, fontweight='bold', color='#1F1F1F')

dv_box = FancyBboxPatch((59, 40), 32, 12.5,
                        boxstyle='round,pad=0.5,rounding_size=2',
                        linewidth=2.5, edgecolor=COLOR_DV_EDGE,
                        facecolor=COLOR_DV_FILL)
ax.add_patch(dv_box)
ax.text(75, 49, 'Firm Performance', ha='center', va='center',
        fontsize=12.5, fontweight='bold', color=COLOR_TEXT)
ax.text(75, 45, 'ln(labour productivity)', ha='center', va='center',
        fontsize=9, style='italic', color='#5F5F5F')

# === H_IP arrow (IV -> DV) with inverted-U label ===
arrow_iv_dv = FancyArrowPatch((41, 46.5), (59, 46.5),
                               arrowstyle='->', mutation_scale=22,
                               linewidth=2.2, color='#3F3F3F')
ax.add_patch(arrow_iv_dv)

hip_label = FancyBboxPatch((42, 49), 16, 5.5,
                           boxstyle='round,pad=0.2',
                           linewidth=1, edgecolor='#3F3F3F',
                           facecolor='white')
ax.add_patch(hip_label)
ax.text(50, 53, 'H_IP: inverted-U', ha='center', va='center',
        fontsize=9, fontweight='bold', color='#3F3F3F')
ax.text(50, 50.5, '(descriptive, full sample)', ha='center', va='center',
        fontsize=8, style='italic', color='#5F5F5F')

# === Moderator dashed arrows (TCI -> path; DAI -> path) ===
arrow_tci = FancyArrowPatch((25, 75), (38, 53),
                             arrowstyle='->', mutation_scale=18,
                             linewidth=1.8, color=COLOR_TCI_EDGE,
                             linestyle='dashed')
ax.add_patch(arrow_tci)

arrow_dai = FancyArrowPatch((75, 75), (62, 53),
                             arrowstyle='->', mutation_scale=18,
                             linewidth=1.8, color=COLOR_DAI_EDGE,
                             linestyle='dashed')
ax.add_patch(arrow_dai)

# === Controls section (bottom) ===
fig.text(0.06, 0.305, 'CONTROLS', fontsize=10, fontweight='bold', color='#BF8F00')

control_labels = [
    ('Firm size', 'ln(employees)'),
    ('Firm age', '2023 - founded'),
    ('Foreign-owned', '>=10% foreign equity'),
    ('Sector FE', 'manufacturing /\nretail / construction'),
]
ctl_x_starts = [6, 27, 49, 73]
ctl_widths = [18, 18, 20, 20]
for (label, sub), x, w in zip(control_labels, ctl_x_starts, ctl_widths):
    box = FancyBboxPatch((x, 18), w, 9,
                         boxstyle='round,pad=0.4,rounding_size=2',
                         linewidth=2, edgecolor=COLOR_CTL_EDGE,
                         facecolor=COLOR_CTL_FILL)
    ax.add_patch(box)
    ax.text(x + w/2, 24, label, ha='center', va='center',
            fontsize=10.5, fontweight='bold', color=COLOR_TEXT)
    ax.text(x + w/2, 20.5, sub, ha='center', va='center',
            fontsize=8.5, style='italic', color='#5F5F5F')

arrow_ctl = FancyArrowPatch((83, 27), (76, 40),
                             arrowstyle='->', mutation_scale=14,
                             linewidth=1.5, color='#BF8F00')
ax.add_patch(arrow_ctl)

# === Bottom note: direct effects ===
note_box = FancyBboxPatch((4, 9), 92, 5,
                          boxstyle='round,pad=0.3',
                          linewidth=1, edgecolor='#7F7F7F',
                          facecolor='#F5F5F5')
ax.add_patch(note_box)
ax.text(50, 12.5, 'Direct effects of moderators on the DV (also estimated, not drawn as arrows for clarity):',
        ha='center', va='center', fontsize=9, fontweight='bold', color=COLOR_TEXT)
# CHANGE: H3 -> H2 for DAI direct effect (was H3)
ax.text(50, 10.2,
        'H1: TCI -> ln(labour productivity), positive direct effect.   '
        'H2: DAI -> ln(labour productivity), conditional on FSTS.',
        ha='center', va='center', fontsize=9, color=COLOR_TEXT)

# === Scope footer ===
scope_box = FancyBboxPatch((4, 2), 92, 5,
                           boxstyle='round,pad=0.3',
                           linewidth=1, edgecolor='#7F7F7F',
                           facecolor='white', linestyle='dashed')
ax.add_patch(scope_box)
ax.text(50, 5,
        'Scope: extreme-case, within-context evidence from Singapore',
        ha='center', va='center', fontsize=10, fontweight='bold', color=COLOR_TEXT)
ax.text(50, 2.8,
        'WBES 2023, N = 623 (full) / 617 (DAI sample); FSTS = 0 in 82.2% of firms; FSTS > 70% in 3.2% of firms - see Section 7.',
        ha='center', va='center', fontsize=8.5, style='italic', color='#5F5F5F')

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig('fig1_FIXED.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

from PIL import Image
img = Image.open('fig1_FIXED.png')
print('Generated Figure 1 (FIXED):')
print(f'  Size: {img.size}')
print(f'  Mode: {img.mode}')
print('  File: fig1_FIXED.png')
