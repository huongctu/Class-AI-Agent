"""
P5 China — Render Figures 2, 3, 4 from verified replication results.

Inputs (verified Python replication, full WBES private-firm frame):
    Figure 2  forest plot of M2 turning points + 95% CIs
    Figure 3  predicted ln(LP) curves overlay 2012 vs 2024 with bands + safe zone
    Figure 4  TCI / DAI level-shift bars by wave with 95% CI

Outputs:
    figure2_threshold_forest.{png,svg}
    figure3_predicted_curves.{png,svg}
    figure4_level_shift_bars.{png,svg}
"""
import os
import numpy as np
import matplotlib.pyplot as plt

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 1.0,
})

# ============================================================
# Verified M2 replicated coefficients (full WBES private frame)
# Source: results/M2_table.csv + results/results_coefs.csv
# ============================================================
m2 = {
    '2012':   {'intercept': 12.7925, 'FSTS':  2.0654, 'FSTSsq': -2.0919,
               'lnEmp': -0.1023, 'firmage': 0.0076, 'foreign': 0.1120,
               'FSTS_se': 0.3790, 'FSTSsq_se': 0.4345, 'N': 2610,
               'mean_lnEmp': 4.31, 'mean_firmage': 13.5, 'mean_foreign': 0.06},
    '2024':   {'intercept': 12.3760, 'FSTS':  1.4980, 'FSTSsq': -1.5873,
               'lnEmp':  0.1180, 'firmage': 0.0124, 'foreign': 0.2566,
               'FSTS_se': 0.5783, 'FSTSsq_se': 0.7117, 'N': 1934,
               'mean_lnEmp': 4.18, 'mean_firmage': 17.8, 'mean_foreign': 0.04},
    'Pooled': {'intercept': 12.2955, 'FSTS':  1.7843, 'FSTSsq': -1.8289,
               'lnEmp':  0.0047, 'firmage': 0.0118, 'foreign': 0.2172,
               'FSTS_se': 0.3195, 'FSTSsq_se': 0.3753, 'N': 4544,
               'mean_lnEmp': 4.25, 'mean_firmage': 15.5, 'mean_foreign': 0.05},
}

turning = {
    '2012':   {'tp': 0.4937, 'ci_lo': 0.4317, 'ci_hi': 0.5557, 'N': 2610},
    '2024':   {'tp': 0.4719, 'ci_lo': 0.3446, 'ci_hi': 0.5992, 'N': 1934},
    'Pooled': {'tp': 0.4878, 'ci_lo': 0.4265, 'ci_hi': 0.5491, 'N': 4544},
}

paternoster = {
    'FSTS':   {'z': 0.821, 'p': 0.412},
    'FSTSsq': {'z': -0.605, 'p': 0.545},
}

levels = {
    'TCI': {
        '2012':   {'b': 0.2757, 'se': 0.0431},
        '2024':   {'b': 0.4258, 'se': 0.0466},
        'Pooled': {'b': 0.3608, 'se': 0.0321},
    },
    'DAI': {
        '2012':   {'b': 0.0772, 'se': 0.0273},
        '2024':   {'b': 0.1876, 'se': 0.0443},
        'Pooled': {'b': 0.1150, 'se': 0.0236},
    },
}


def figure2():
    fig, ax = plt.subplots(figsize=(9.0, 5.0))
    waves = ['2012', '2024', 'Pooled']
    colors = ['#1f77b4', '#d62728', '#444444']
    y_pos = [4, 3, 2]

    for y, w, c in zip(y_pos, waves, colors):
        d = turning[w]
        ax.errorbar(d['tp']*100, y,
                    xerr=[[d['tp']*100 - d['ci_lo']*100],
                          [d['ci_hi']*100 - d['tp']*100]],
                    fmt='o', color=c, markersize=10, capsize=6,
                    linewidth=2.0, elinewidth=1.6)
        ax.text(d['tp']*100 + 0.4, y + 0.20,
                f"{d['tp']*100:.1f}%", fontsize=10, color=c, fontweight='bold')

    ax.axvspan(30, 60, color='#4daf4a', alpha=0.10, zorder=0)
    ax.text(45, 4.55, 'Safe operating zone (30–60 %)',
            ha='center', fontsize=9, color='#2d6d2d', style='italic')

    ax.set_yticks(y_pos)
    ax.set_yticklabels([f"{w}\n(N = {turning[w]['N']:,})" for w in waves])
    ax.set_xlabel('Optimal export-intensity threshold (% of total sales)', fontsize=11)
    ax.set_xlim(20, 70)
    ax.set_ylim(0.3, 4.9)
    ax.grid(axis='x', alpha=0.25, linestyle='--', linewidth=0.6)

    paternoster_text = (
        f"Paternoster cross-wave equality (2012 vs 2024):\n"
        f"  FSTS:  z = {paternoster['FSTS']['z']:+.2f},  p = {paternoster['FSTS']['p']:.3f}\n"
        f"  FSTS²: z = {paternoster['FSTSsq']['z']:+.2f},  p = {paternoster['FSTSsq']['p']:.3f}\n"
        f"  Joint F(2, 3558) = 2.24, p = .107 → equality NOT rejected\n"
        f"  → unexpected stability finding (predicted shift not detected)"
    )
    ax.text(0.5, -0.32, paternoster_text, ha='center', va='top',
            transform=ax.transAxes, fontsize=8.8,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#f5f5f5', edgecolor='#888'))

    ax.set_title('Figure 2. Optimal export-intensity threshold across waves\n'
                 '(M2 inverted-U turning point with delta-method 95 % CI)',
                 fontsize=11, pad=10)
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig(os.path.join(OUT_DIR, 'figure2_threshold_forest.png'), dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, 'figure2_threshold_forest.svg'), bbox_inches='tight')
    plt.close()
    print('[OK] Figure 2 saved')


def predict_lnLP(wave, fsts):
    p = m2[wave]
    return (p['intercept'] + p['FSTS']*fsts + p['FSTSsq']*fsts**2
            + p['lnEmp']*p['mean_lnEmp']
            + p['firmage']*p['mean_firmage']
            + p['foreign']*p['mean_foreign'])


def predict_lnLP_se(wave, fsts):
    p = m2[wave]
    var = (p['FSTS_se']**2)*fsts**2 + (p['FSTSsq_se']**2)*fsts**4
    return np.sqrt(var)


def figure3():
    fig, ax = plt.subplots(figsize=(9.0, 5.2))
    fsts_grid = np.linspace(0, 1, 200)

    for wave, color in [('2012', '#1f77b4'), ('2024', '#d62728')]:
        y = np.array([predict_lnLP(wave, x) for x in fsts_grid])
        se = np.array([predict_lnLP_se(wave, x) for x in fsts_grid])
        ax.plot(fsts_grid*100, y, '-', color=color, linewidth=2.2,
                label=f"{wave}  (TP = {turning[wave]['tp']*100:.1f} %, N = {turning[wave]['N']:,})")
        ax.fill_between(fsts_grid*100, y - 1.96*se, y + 1.96*se, color=color, alpha=0.15)
        ax.axvline(turning[wave]['tp']*100, color=color, linestyle=':', linewidth=1.5, alpha=0.7)

    ax.axvspan(30, 60, color='#4daf4a', alpha=0.10, zorder=0)
    ax.text(45, ax.get_ylim()[1] - 0.05, 'Safe operating zone (30–60 %)',
            ha='center', va='top', fontsize=9.5, color='#2d6d2d', style='italic',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='white',
                      edgecolor='#4daf4a', alpha=0.85))

    ax.set_xlabel('Export intensity FSTS (% of total sales)', fontsize=11)
    ax.set_ylabel('Predicted ln(LP) — log labour productivity', fontsize=11)
    ax.set_xlim(0, 100)
    ax.legend(loc='lower center', frameon=True, fontsize=10, framealpha=0.9)
    ax.grid(alpha=0.25, linestyle='--', linewidth=0.6)
    ax.set_title('Figure 3. Predicted ln(LP) across export intensity, 2012 vs 2024\n'
                 '(M2 fits at within-wave control means; shaded = 95 % CI of predicted mean)',
                 fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, 'figure3_predicted_curves.png'), dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, 'figure3_predicted_curves.svg'), bbox_inches='tight')
    plt.close()
    print('[OK] Figure 3 saved')


def figure4():
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    waves = ['2012', '2024', 'Pooled']
    x = np.arange(len(waves))
    w = 0.35

    tci_b  = [levels['TCI'][wv]['b']  for wv in waves]
    tci_se = [levels['TCI'][wv]['se'] for wv in waves]
    dai_b  = [levels['DAI'][wv]['b']  for wv in waves]
    dai_se = [levels['DAI'][wv]['se'] for wv in waves]

    bars1 = ax.bar(x - w/2, tci_b, w, yerr=[1.96*s for s in tci_se], capsize=4,
                   color='#377eb8', label='TCI_full (tech capability)',
                   edgecolor='black', linewidth=0.8)
    bars2 = ax.bar(x + w/2, dai_b, w, yerr=[1.96*s for s in dai_se], capsize=4,
                   color='#ff7f00', label='DAI (digital adoption — c22b + e6 thin)',
                   edgecolor='black', linewidth=0.8)

    for bar, b in zip(bars1, tci_b):
        ax.text(bar.get_x() + bar.get_width()/2, b + 0.018,
                f"{b:+.3f}", ha='center', fontsize=9, fontweight='bold', color='#193d66')
    for bar, b in zip(bars2, dai_b):
        ax.text(bar.get_x() + bar.get_width()/2, b + 0.018,
                f"{b:+.3f}", ha='center', fontsize=9, fontweight='bold', color='#a04500')

    ax.axhline(0, color='black', linewidth=0.7)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{wv}\n(N = {turning[wv]['N']:,})" for wv in waves])
    ax.set_ylabel('β (within-wave z-standardised level shift)', fontsize=11)
    ax.set_ylim(-0.05, 0.55)
    ax.legend(loc='upper left', frameon=True, fontsize=9.5)
    ax.grid(axis='y', alpha=0.25, linestyle='--', linewidth=0.6)
    ax.text(0.99, 0.05,
            'Paternoster cross-wave on TCI: z = −2.55, p = .011 → strengthening 2012 → 2024',
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=8.5, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#f5f5f5', edgecolor='#888'))
    ax.set_title('Figure 4. Level-shift coefficients TCI and DAI by wave\n'
                 '(direct effects from M5 / M6, OLS-HC1; pooled clustered on idstd)',
                 fontsize=11, pad=10)
    plt.tight_layout()
    plt.savefig(os.path.join(OUT_DIR, 'figure4_level_shift_bars.png'), dpi=300, bbox_inches='tight')
    plt.savefig(os.path.join(OUT_DIR, 'figure4_level_shift_bars.svg'), bbox_inches='tight')
    plt.close()
    print('[OK] Figure 4 saved')


if __name__ == '__main__':
    figure2()
    figure3()
    figure4()
    print(f'\nAll figures saved to {OUT_DIR}')
