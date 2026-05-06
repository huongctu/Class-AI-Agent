#!/usr/bin/env python3
"""
Generate figures for CĐ1 v3.1 from WBES raw .dta files.

Dependencies: pandas, matplotlib, openpyxl
Usage: python3 generate_figures.py
Output: 3 SVG + 3 PNG in current directory.

Requires raw .dta files in working directory:
  - Mongolia-2009-full-data.dta (or similar from WBES Mongolia 2009)
  - Mongolia-2013-full-data.dta
  - Mongolia-2019-full-data.dta
  - Mongolia-2025-full-data.dta
  - Kiribati-2025-full-data.dta

Download from: https://www.enterprisesurveys.org/en/data/exploreeconomies

NCS: Đỗ Thùy Hương — HD: TS. Nguyễn Minh Cảnh — 06/05/2026
"""
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def compute_country_year_stats(dta_path, year):
    """Compute key WBES indicators for one country-year .dta file."""
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
        'fsts_mean': fsts.mean(),
        'exporter_pct': (fsts > 0).mean() * 100,
        'fdi10_pct': (fdi >= 10).sum() / len(fdi) * 100 if len(fdi) > 0 else np.nan,
        'rd_pct': (rd == 1).sum() / len(rd) * 100,
        'web_pct': (web == 1).sum() / len(web) * 100,
        'iso_pct': (iso == 1).sum() / len(iso) * 100,
        'sd_log': log_prod.std(),
    }


def fig_mongolia_evolution(df_mng, output_basename='fig_5_6_mongolia_evolution'):
    """4-panel Mongolia evolution 2009–2025."""
    fig, axes = plt.subplots(2, 2, figsize=(11, 8))
    fig.suptitle('Hình 5.6.1 — Mongolia: Evolution 2009–2025 (4 đợt khảo sát WBES)',
                 fontsize=14, fontweight='bold')
    # Panel A — FSTS
    ax = axes[0, 0]
    ax.plot(df_mng['year'], df_mng['fsts_mean'], 'o-', color='#1f77b4', lw=2, ms=10, label='FSTS trung bình (%)')
    ax.plot(df_mng['year'], df_mng['exporter_pct'], 's-', color='#ff7f0e', lw=2, ms=10, label='Tỷ lệ DN xuất khẩu (%)')
    ax.set_title('Quốc tế hóa: ĐÌNH TRỆ (resource curse pattern)')
    ax.legend(fontsize=9); ax.grid(alpha=0.3); ax.set_xticks(df_mng['year'])
    # Panel B — FDI
    ax = axes[0, 1]
    ax.plot(df_mng['year'], df_mng['fdi10_pct'], 'D-', color='#d62728', lw=2.5, ms=12)
    ax.fill_between(df_mng['year'], df_mng['fdi10_pct'], alpha=0.2, color='#d62728')
    ax.set_title('FDI ≥10%: GIẢM 7,2% → 3,2% (lời nguyền tài nguyên)')
    ax.grid(alpha=0.3); ax.set_xticks(df_mng['year']); ax.set_ylim(0, 8)
    # Panel C — Tech adoption
    ax = axes[1, 0]
    ax.plot(df_mng['year'], df_mng['web_pct'], '^-', color='#2ca02c', lw=2.5, ms=12, label='Website (%)')
    ax.plot(df_mng['year'], df_mng['iso_pct'], 'v-', color='#9467bd', lw=2, ms=10, label='ISO (%)')
    ax.plot(df_mng['year'], df_mng['rd_pct'], '*-', color='#8c564b', lw=2, ms=12, label='R&D (%)')
    ax.set_title('Năng lực CN + số: WEBSITE TĂNG (digital leapfrog)')
    ax.legend(fontsize=9); ax.grid(alpha=0.3); ax.set_xticks(df_mng['year'])
    # Panel D — sd log
    ax = axes[1, 1]
    ax.bar(df_mng['year'], df_mng['sd_log'], color='#17becf', edgecolor='black', width=2.5)
    ax.set_title('Phân tán năng suất nội bộ')
    ax.set_xticks(df_mng['year']); ax.grid(alpha=0.3, axis='y')
    for i, v in enumerate(df_mng['sd_log']):
        ax.text(df_mng['year'].iloc[i], v + 0.03, f'{v:.2f}', ha='center', fontsize=9)
    plt.tight_layout()
    plt.savefig(f'{output_basename}.png', dpi=120, bbox_inches='tight')
    plt.savefig(f'{output_basename}.svg', bbox_inches='tight')
    plt.close()


def fig_sids_comparison(output_basename='fig_5_7_sids_comparison'):
    """3-way comparison: Kiribati vs Fiji vs Singapore."""
    indicators = ['FSTS (%)', 'FDI ≥10% (%)', 'R&D (%)', 'ISO (%)', 'Website (%)', 'sd log năng suất']
    kir = [1.0, 0.7, 14.0, 1.3, 18.7, 1.48]
    fji = [12.5, 9.9, 18.8, 16.5, 74.8, 1.09]
    sgp = [7.1, 31.5, 7.5, 23.3, 66.1, 1.03]
    fig, ax = plt.subplots(figsize=(12, 7))
    x = np.arange(len(indicators)); w = 0.27
    ax.bar(x - w, kir, w, label='Kiribati 2025 (isolated)', color='#d62728', edgecolor='black')
    ax.bar(x, fji, w, label='Fiji 2025 (high-digital)', color='#2ca02c', edgecolor='black')
    ax.bar(x + w, sgp, w, label='Singapore 2023 (Advanced)', color='#1f77b4', edgecolor='black')
    ax.set_title('Hình 5.7.1 — Dị biệt nội bộ SIDS Thái Bình Dương: Kiribati vs Fiji vs Singapore',
                 fontsize=12, fontweight='bold')
    ax.set_xticks(x); ax.set_xticklabels(indicators, rotation=15, ha='right')
    ax.legend(fontsize=10); ax.grid(alpha=0.3, axis='y')
    plt.tight_layout()
    plt.savefig(f'{output_basename}.png', dpi=120, bbox_inches='tight')
    plt.savefig(f'{output_basename}.svg', bbox_inches='tight')
    plt.close()


def fig_pool_composition(output_basename='fig_4_1_pool_composition'):
    """Bar chart pool composition by sub-regime (101.185 firms)."""
    sub_regimes = ['Emerging', 'Frontier', 'Upper-middle', 'Advanced', 'SIDS Thái Bình Dương']
    n_firms = [47803, 28678, 16693, 6640, 1371]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    total = sum(n_firms); pcts = [n / total * 100 for n in n_firms]
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.barh(sub_regimes, n_firms, color=colors, edgecolor='black')
    for i, (n, pct) in enumerate(zip(n_firms, pcts)):
        ax.text(n + 500, i, f'{n:,} ({pct:.1f}%)', va='center', fontsize=10, fontweight='bold')
    ax.set_xlabel('Số doanh nghiệp')
    ax.set_title('Hình 4.1.1 — Phân bố nhóm dữ liệu CĐ1 (n=101.185 · 47 nước · 108 QG×năm · 2009–2025) v3.1',
                 fontsize=12, fontweight='bold')
    ax.set_xlim(0, 55000); ax.grid(alpha=0.3, axis='x')
    plt.tight_layout()
    plt.savefig(f'{output_basename}.png', dpi=120, bbox_inches='tight')
    plt.savefig(f'{output_basename}.svg', bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    # Mongolia panel from 4 .dta files
    mng_data = []
    for year, path in [(2009, 'Mongolia-2009-full-data.dta'),
                       (2013, 'Mongolia-2013-full-data.dta'),
                       (2019, 'Mongolia-2019-full-data.dta'),
                       (2025, 'Mongolia-2025-full-data.dta')]:
        try:
            mng_data.append(compute_country_year_stats(path, year))
        except FileNotFoundError:
            print(f'WARNING: {path} not found — fall back to cached mongolia_panel.csv')
    if mng_data:
        df_mng = pd.DataFrame(mng_data)
        df_mng.to_csv('mongolia_panel.csv', index=False)
    else:
        df_mng = pd.read_csv('mongolia_panel.csv')
    fig_mongolia_evolution(df_mng)
    fig_sids_comparison()
    fig_pool_composition()
    print('Generated 3 figures (PNG + SVG) — see thesis/figures/')
