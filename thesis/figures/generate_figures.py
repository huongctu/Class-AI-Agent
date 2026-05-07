#!/usr/bin/env python3
"""
Generate figures v2 for CĐ1 v3.1c — 5 figures from WBES + simulated parameters.

Dependencies: pandas, matplotlib, numpy, openpyxl
Usage: python3 generate_figures.py
Output: 5 figures (PNG + SVG each).

Requires raw .dta files cho Hình 5.6.1:
  Mongolia-2009/2013/2019/2025-full-data.dta
Download: https://www.enterprisesurveys.org/en/data/exploreeconomies

NCS: Đỗ Thùy Hương — HD: TS. Nguyễn Minh Cảnh — 06/05/2026 v2.0
"""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def compute_country_year_stats(dta_path, year):
    df = pd.read_stata(dta_path, convert_categoricals=False)
    fsts = df.get('d3b', pd.Series(dtype=float)).fillna(0) + df.get('d3c', pd.Series(dtype=float)).fillna(0)
    fsts = fsts[(fsts >= 0) & (fsts <= 100)]
    fdi = df.get('b2b', pd.Series(dtype=float)).dropna()
    rd = df.get('h5', pd.Series(dtype=float))
    web = df.get('c22b', pd.Series(dtype=float))
    iso = df.get('b8', pd.Series(dtype=float))
    sales = df.get('d2', pd.Series(dtype=float))
    emp = df.get('l1', pd.Series(dtype=float))
    valid = (sales > 0) & (emp > 0)
    log_prod = np.log(sales[valid] / emp[valid])
    return {
        'year': year, 'n': len(df),
        'fsts_mean': fsts.mean(), 'exporter_pct': (fsts > 0).mean() * 100,
        'fdi10_pct': (fdi >= 10).sum() / len(fdi) * 100 if len(fdi) > 0 else np.nan,
        'rd_pct': (rd == 1).sum() / len(rd) * 100,
        'web_pct': (web == 1).sum() / len(web) * 100,
        'iso_pct': (iso == 1).sum() / len(iso) * 100,
        'sd_log': log_prod.std(),
    }


def fig_4_1_pool_composition(out='fig_4_1_pool_composition'):
    sub = ['Emerging', 'Frontier', 'Upper-mid', 'Advanced', 'SIDS']
    n = [47803, 28678, 16693, 6640, 1371]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    total = sum(n); pcts = [v / total * 100 for v in n]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.barh(sub, n, color=colors, edgecolor='black')
    for i, (v, pct) in enumerate(zip(n, pcts)):
        ax.text(v + 500, i, f'{v:,} ({pct:.1f}%)', va='center', fontsize=9, fontweight='bold')
    ax.set_title('Hình 4.1.1 — Pool 101.185 doanh nghiệp · 47 nước · 108 QG×năm · v3.1', fontsize=10, fontweight='bold')
    ax.set_xlim(0, 55000); ax.grid(alpha=0.3, axis='x')
    plt.tight_layout(); plt.savefig(f'{out}.png', dpi=120, bbox_inches='tight'); plt.savefig(f'{out}.svg', bbox_inches='tight'); plt.close()


def fig_4_2_productivity_density(out='fig_4_2_productivity_density'):
    """NEW v2: Phân phối năng suất theo 6 phân nhóm con (kernel density approximation)."""
    fig, ax = plt.subplots(figsize=(9, 5))
    sub_regimes = [
        ('Advanced innovation', 0, 1.03, '#1f77b4'),
        ('Advanced resource', 0.5, 0.49, '#d62728'),
        ('Upper-middle', -0.3, 1.29, '#2ca02c'),
        ('Emerging', -0.6, 1.24, '#ff7f0e'),
        ('Frontier', -1.2, 1.36, '#8c564b'),
        ('SIDS Pacific', -0.9, 1.32, '#9467bd'),
    ]
    x = np.linspace(-5, 5, 300)
    for label, mean, sd, color in sub_regimes:
        y = np.exp(-(x - mean)**2 / (2 * sd**2)) / (sd * np.sqrt(2 * np.pi))
        ax.plot(x, y, label=f'{label} (sd={sd:.2f})', color=color, lw=2)
        ax.fill_between(x, y, alpha=0.15, color=color)
    ax.set_xlabel('Log năng suất lao động (chuẩn hóa)')
    ax.set_ylabel('Mật độ xác suất')
    ax.set_title('Hình 4.2 — Phân phối năng suất theo 6 phân nhóm con (kernel density, n=101.185)\nMinh họa từ tham số sd log; chi tiết Bảng 4.1', fontsize=11, fontweight='bold')
    ax.legend(loc='upper left', fontsize=9); ax.grid(alpha=0.3)
    plt.tight_layout(); plt.savefig(f'{out}.png', dpi=120, bbox_inches='tight'); plt.savefig(f'{out}.svg', bbox_inches='tight'); plt.close()


def fig_5_1_seven_scenes(out='fig_5_1_seven_scenes'):
    """NEW v2: Định vị 7 tiểu cảnh trên trục Phân tán × FDI."""
    fig, ax = plt.subplots(figsize=(11, 7))
    scenes = [
        ('Singapore', 1.03, 31.5, '#1f77b4', 'o'),
        ('Việt Nam', 1.38, 11.4, '#ff7f0e', 's'),
        ('Trung Quốc', 1.20, 6.0, '#2ca02c', 'D'),
        ('Em Asia', 2.18, 4.4, '#9467bd', '^'),
        ('Mongolia', 1.16, 4.7, '#8c564b', 'v'),
        ('SIDS Pacific', 1.32, 23.5, '#e377c2', '*'),
        ('Saudi+Qatar+Kuwait', 0.49, 11.5, '#d62728', 'P'),
    ]
    sizes_n = [623, 3077, 4889, 42278, 1905, 1371, 1632]
    for i, (name, sd, fdi, color, marker) in enumerate(scenes):
        ax.scatter(sd, fdi, s=np.sqrt(sizes_n[i]) * 8, c=color, marker=marker,
                   edgecolors='black', linewidth=1.5, alpha=0.85, label=f'{name} (n={sizes_n[i]:,})')
        ax.annotate(name, (sd, fdi), xytext=(8, 5), textcoords='offset points', fontsize=10, fontweight='bold')
    ax.set_xlabel('Phân tán năng suất (sd log) →', fontsize=11)
    ax.set_ylabel('Tỷ lệ FDI ≥10% (%) →', fontsize=11)
    ax.set_title('Hình 5.1 — Định vị 7 tiểu cảnh điển hình trên hệ trục Phân tán × FDI', fontsize=12, fontweight='bold')
    ax.grid(alpha=0.3); ax.set_xlim(0.2, 2.4); ax.set_ylim(-2, 35)
    ax.axhspan(20, 35, alpha=0.05, color='blue')
    ax.text(0.3, 32, 'Vùng FDI cao (>20%)', fontsize=9, color='blue', fontweight='bold')
    ax.axvspan(1.5, 2.4, alpha=0.05, color='red')
    ax.text(2.0, 28, 'Vùng phân tán cao (>1,5)', fontsize=9, color='red', fontweight='bold', ha='center')
    plt.tight_layout(); plt.savefig(f'{out}.png', dpi=120, bbox_inches='tight'); plt.savefig(f'{out}.svg', bbox_inches='tight'); plt.close()


def fig_5_6_mongolia_evolution(df_mng, out='fig_5_6_mongolia_evolution'):
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    fig.suptitle('Hình 5.6.1 — Mongolia: Evolution 2009–2025 (4 đợt WBES)', fontsize=14, fontweight='bold')
    ax = axes[0, 0]
    ax.plot(df_mng['year'], df_mng['fsts_mean'], 'o-', lw=2, ms=10, label='FSTS (%)')
    ax.plot(df_mng['year'], df_mng['exporter_pct'], 's-', lw=2, ms=10, label='Doanh nghiệp xuất khẩu (%)')
    ax.set_title('Quốc tế hóa đình trệ (resource curse)'); ax.legend(fontsize=9); ax.grid(alpha=0.3); ax.set_xticks(df_mng['year'])
    ax = axes[0, 1]
    ax.plot(df_mng['year'], df_mng['fdi10_pct'], 'D-', color='#d62728', lw=2.5, ms=12)
    ax.fill_between(df_mng['year'], df_mng['fdi10_pct'], alpha=0.2, color='#d62728')
    ax.set_title('FDI ≥10%: 7,2→3,2% (lời nguyền tài nguyên)'); ax.grid(alpha=0.3); ax.set_xticks(df_mng['year']); ax.set_ylim(0, 8)
    ax = axes[1, 0]
    ax.plot(df_mng['year'], df_mng['web_pct'], '^-', color='#2ca02c', lw=2.5, ms=12, label='Website (%)')
    ax.plot(df_mng['year'], df_mng['iso_pct'], 'v-', color='#9467bd', lw=2, ms=10, label='ISO (%)')
    ax.plot(df_mng['year'], df_mng['rd_pct'], '*-', color='#8c564b', lw=2, ms=12, label='R&D (%)')
    ax.set_title('Năng lực CN + số: WEBSITE TĂNG (digital leapfrog)'); ax.legend(fontsize=9); ax.grid(alpha=0.3); ax.set_xticks(df_mng['year'])
    ax = axes[1, 1]
    ax.bar(df_mng['year'], df_mng['sd_log'], color='#17becf', edgecolor='black', width=2.5)
    ax.set_title('Phân tán sd_log năng suất nội bộ'); ax.set_xticks(df_mng['year']); ax.grid(alpha=0.3, axis='y')
    for i, v in enumerate(df_mng['sd_log']):
        ax.text(df_mng['year'].iloc[i], v + 0.03, f'{v:.2f}', ha='center', fontsize=9)
    plt.tight_layout(); plt.savefig(f'{out}.png', dpi=120, bbox_inches='tight'); plt.savefig(f'{out}.svg', bbox_inches='tight'); plt.close()


def fig_5_7_sids_comparison(out='fig_5_7_sids_comparison'):
    indicators = ['FSTS (%)', 'FDI ≥10% (%)', 'R&D (%)', 'ISO (%)', 'Website (%)', 'sd log']
    kir = [1.0, 0.7, 14.0, 1.3, 18.7, 1.48]
    fji = [12.5, 9.9, 18.8, 16.5, 74.8, 1.09]
    sgp = [7.1, 31.5, 7.5, 23.3, 66.1, 1.03]
    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(indicators)); w = 0.27
    ax.bar(x - w, kir, w, label='Kiribati 2025 (isolated)', color='#d62728', edgecolor='black')
    ax.bar(x, fji, w, label='Fiji 2025 (high-digital)', color='#2ca02c', edgecolor='black')
    ax.bar(x + w, sgp, w, label='Singapore 2023 (Advanced)', color='#1f77b4', edgecolor='black')
    ax.set_title('Hình 5.7.1 — Dị biệt nội bộ SIDS Thái Bình Dương: Kiribati vs Fiji vs Singapore', fontsize=12, fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels(indicators, rotation=15, ha='right')
    ax.legend(loc='upper right', fontsize=10); ax.grid(alpha=0.3, axis='y')
    plt.tight_layout(); plt.savefig(f'{out}.png', dpi=120, bbox_inches='tight'); plt.savefig(f'{out}.svg', bbox_inches='tight'); plt.close()


if __name__ == '__main__':
    # Mongolia panel (cần raw .dta)
    mng_data = []
    for year, path in [(2009, 'Mongolia-2009-full-data.dta'),
                       (2013, 'Mongolia-2013-full-data.dta'),
                       (2019, 'Mongolia-2019-full-data.dta'),
                       (2025, 'Mongolia-2025-full-data.dta')]:
        try:
            mng_data.append(compute_country_year_stats(path, year))
        except FileNotFoundError:
            print(f'WARNING: {path} not found — fallback to mongolia_panel.csv')
    if mng_data:
        df_mng = pd.DataFrame(mng_data); df_mng.to_csv('mongolia_panel.csv', index=False)
    else:
        df_mng = pd.read_csv('mongolia_panel.csv')
    fig_4_1_pool_composition()
    fig_4_2_productivity_density()
    fig_5_1_seven_scenes()
    fig_5_6_mongolia_evolution(df_mng)
    fig_5_7_sids_comparison()
    print('Generated 5 figures (PNG + SVG) in current directory.')
