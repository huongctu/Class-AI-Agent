#!/usr/bin/env python3
"""Hierarchical OLS regression suite for P3/P4/P5 dissertation papers.

Runs M1-M8 models for each paper, computes Lind-Mehlum U-tests,
marginal effects, VIF, and exports results to CSV.
"""

import os
import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.stats.diagnostic import het_breuschpagan
from scipy import stats
import warnings

warnings.filterwarnings('ignore')

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'analysis', 'pooled_wbes_6waves.csv')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'analysis')

CONTROLS = ['ln_empl', 'firm_age', 'foreign_dummy']


def ols_run(y, X, label, show=True):
    Xc = sm.add_constant(X)
    m = sm.OLS(y, Xc, missing='drop').fit(cov_type='HC1')
    if show:
        print(f'\n{"="*78}')
        print(f'  {label}')
        print(f'  N={int(m.nobs)}, R2={m.rsquared:.4f}, AdjR2={m.rsquared_adj:.4f}, F={m.fvalue:.3f}')
        print(f'{"="*78}')
        print(f'  {"Variable":<28} {"B":>10} {"SE":>10} {"t":>8} {"p":>8}')
        print(f'  {"-"*66}')
        for v in m.params.index:
            c, se, t, p = m.params[v], m.bse[v], m.tvalues[v], m.pvalues[v]
            sig = '***' if p < .001 else '**' if p < .01 else '*' if p < .05 else '+' if p < .1 else ''
            vn = 'Constant' if v == 'const' else v
            print(f'  {vn:<28} {c:>10.4f} {se:>10.4f} {t:>8.3f} {p:>8.4f} {sig}')
    return m


def lind_mehlum(mod, fsts_data, b1='FSTS', b2='FSTS2', label=''):
    beta1, beta2 = mod.params[b1], mod.params[b2]
    se1, se2 = mod.bse[b1], mod.bse[b2]
    cov = mod.cov_params()
    c12 = cov.loc[b1, b2]
    tp = -beta1 / (2 * beta2)

    g1, g2 = -1 / (2 * beta2), beta1 / (2 * beta2**2)
    se_tp = np.sqrt(g1**2 * se1**2 + g2**2 * se2**2 + 2 * g1 * g2 * c12)

    fmin = fsts_data.min()
    fmax = fsts_data.max()

    sl_lo = beta1 + 2 * beta2 * fmin
    se_sl_lo = np.sqrt(se1**2 + 4 * fmin**2 * se2**2 + 4 * fmin * c12)
    t_lo = sl_lo / se_sl_lo
    p_lo = 1 - stats.t.cdf(t_lo, mod.df_resid) if sl_lo > 0 else stats.t.cdf(t_lo, mod.df_resid)

    sl_hi = beta1 + 2 * beta2 * fmax
    se_sl_hi = np.sqrt(se1**2 + 4 * fmax**2 * se2**2 + 4 * fmax * c12)
    t_hi = sl_hi / se_sl_hi
    p_hi = stats.t.cdf(t_hi, mod.df_resid) if sl_hi < 0 else 1 - stats.t.cdf(t_hi, mod.df_resid)

    overall_p = max(p_lo, p_hi)
    status = 'CONFIRMED' if overall_p < .05 else 'MARGINAL' if overall_p < .1 else 'NOT_CONFIRMED'

    print(f'  {label}: TP={tp * 100:.1f}% [CI:{(tp - 1.96 * se_tp) * 100:.0f}%,{(tp + 1.96 * se_tp) * 100:.0f}%]'
          f'  LM_p={overall_p:.4f} {status}')
    return {'tp': tp, 'tp_pct': tp * 100, 'lm_p': overall_p, 'status': status,
            'se_tp': se_tp, 'ci_lo': (tp - 1.96 * se_tp) * 100, 'ci_hi': (tp + 1.96 * se_tp) * 100}


def marginal_effects(mod, dai_var, fsts_vals=None):
    if fsts_vals is None:
        fsts_vals = [0, .05, .10, .15, .20, .30, .50, .70, 1.0]

    fsts_x = f'FSTS_x_{dai_var}'
    fsts2_x = f'FSTS2_x_{dai_var}'

    if fsts_x not in mod.params.index:
        return []

    bd = mod.params[dai_var]
    bfd = mod.params[fsts_x]
    bf2d = mod.params[fsts2_x]
    cov = mod.cov_params()
    vnames = [dai_var, fsts_x, fsts2_x]

    results = []
    for x in fsts_vals:
        me = bd + bfd * x + bf2d * x**2
        g = np.array([1, x, x**2])
        vc = np.array([[cov.loc[a, b] for b in vnames] for a in vnames])
        se_me = np.sqrt(g @ vc @ g)
        t_me = me / se_me
        p_me = 2 * (1 - stats.t.cdf(abs(t_me), mod.df_resid))
        results.append({'fsts_pct': x * 100, 'me': me, 'se': se_me, 't': t_me, 'p': p_me})
    return results


def compute_vif(X_df):
    Xc = sm.add_constant(X_df.dropna())
    vifs = {}
    for i, col in enumerate(Xc.columns):
        if col != 'const':
            vifs[col] = variance_inflation_factor(Xc.values, i)
    return vifs


def extract_model_row(mod, label):
    row = {'model': label, 'n': int(mod.nobs), 'r2': mod.rsquared, 'adj_r2': mod.rsquared_adj, 'f': mod.fvalue}
    for v in mod.params.index:
        if v == 'const':
            continue
        row[f'{v}_b'] = mod.params[v]
        row[f'{v}_se'] = mod.bse[v]
        row[f'{v}_p'] = mod.pvalues[v]
    return row


def run_paper(sample, tci_var, dai_var, controls_list, label_prefix, paper_label):
    print(f'\n\n{"#"*78}')
    print(f'  {paper_label}')
    print(f'  N={len(sample)}, TCI={tci_var}, DAI={dai_var}')
    print(f'{"#"*78}')

    for idx in [tci_var, dai_var]:
        sample[f'FSTS_x_{idx}'] = sample['FSTS'] * sample[idx]
        sample[f'FSTS2_x_{idx}'] = sample['FSTS2'] * sample[idx]

    dep = 'ln_labor_prod'
    rows = []

    m1 = ols_run(sample[dep], sample[controls_list], f'{label_prefix}-M1: Controls')
    rows.append(extract_model_row(m1, 'M1'))

    m2 = ols_run(sample[dep], sample[controls_list + ['FSTS', 'FSTS2']], f'{label_prefix}-M2: Inverted-U')
    rows.append(extract_model_row(m2, 'M2'))

    m3 = ols_run(sample[dep], sample[controls_list + ['FSTS', 'FSTS2', tci_var]], f'{label_prefix}-M3: +TCI')
    rows.append(extract_model_row(m3, 'M3'))

    m4 = ols_run(sample[dep], sample[controls_list + ['FSTS', 'FSTS2', tci_var,
                  f'FSTS_x_{tci_var}', f'FSTS2_x_{tci_var}']], f'{label_prefix}-M4: +TCI mod')
    rows.append(extract_model_row(m4, 'M4'))

    m5 = ols_run(sample[dep], sample[controls_list + ['FSTS', 'FSTS2', dai_var]], f'{label_prefix}-M5: +DAI')
    rows.append(extract_model_row(m5, 'M5'))

    m6 = ols_run(sample[dep], sample[controls_list + ['FSTS', 'FSTS2', dai_var,
                  f'FSTS_x_{dai_var}', f'FSTS2_x_{dai_var}']], f'{label_prefix}-M6: +DAI mod')
    rows.append(extract_model_row(m6, 'M6'))

    m7 = ols_run(sample[dep], sample[controls_list + ['FSTS', 'FSTS2', tci_var, dai_var]],
                 f'{label_prefix}-M7: TCI+DAI')
    rows.append(extract_model_row(m7, 'M7'))

    m8 = ols_run(sample[dep], sample[controls_list + ['FSTS', 'FSTS2', tci_var, dai_var,
                  f'FSTS_x_{tci_var}', f'FSTS2_x_{tci_var}',
                  f'FSTS_x_{dai_var}', f'FSTS2_x_{dai_var}']], f'{label_prefix}-M8: Full')
    rows.append(extract_model_row(m8, 'M8'))

    print(f'\n  Lind-Mehlum U-tests:')
    lm2 = lind_mehlum(m2, sample['FSTS'].dropna(), label='M2')
    lm7 = lind_mehlum(m7, sample['FSTS'].dropna(), label='M7')

    me = marginal_effects(m8, dai_var)
    if me:
        print(f'\n  DAI marginal effects (M8):')
        print(f'  {"FSTS%":>6} {"ME":>10} {"SE":>10} {"t":>8} {"p":>8}')
        for r in me:
            sig = '***' if r['p'] < .001 else '**' if r['p'] < .01 else '*' if r['p'] < .05 else '+' if r['p'] < .1 else ''
            print(f'  {r["fsts_pct"]:>5.0f}% {r["me"]:>10.4f} {r["se"]:>10.4f} {r["t"]:>8.3f} {r["p"]:>8.4f} {sig}')

    vifs = compute_vif(sample[controls_list + ['FSTS', 'FSTS2', tci_var, dai_var]])
    print(f'\n  VIF (M7):')
    for v, val in vifs.items():
        flag = ' !!' if val > 5 else ''
        print(f'    {v:<25} {val:>6.2f}{flag}')

    return pd.DataFrame(rows), {'lm_m2': lm2, 'lm_m7': lm7}


def main():
    pooled = pd.read_csv(DATA_PATH)
    pooled['FSTS'] = pooled['export_pct'] / 100
    pooled['FSTS2'] = pooled['FSTS'] ** 2
    pooled['foreign_dummy'] = np.where(
        pooled['foreign_own'].isna(), np.nan,
        np.where(pooled['foreign_own'] > 0, 1.0, 0.0),
    )

    # ── P3 SINGAPORE ──
    sgp = pooled[pooled['dataset'] == 'SGP_2023'].copy()
    sgp = sgp.dropna(subset=['ln_labor_prod', 'FSTS', 'ln_empl', 'firm_age']).copy()
    p3_df, p3_lm = run_paper(sgp, 'TCI_full', 'DAI_rich', CONTROLS, 'SGP', 'P3 SINGAPORE (N=623)')

    # ── P5 CHINA POOLED ──
    chn = pooled[pooled['country'] == 'CHN'].copy()
    chn['wave_2024'] = (chn['year'] == '2024').astype(float)
    chn = chn.dropna(subset=['ln_labor_prod', 'FSTS', 'ln_empl', 'firm_age']).copy()
    p5_df, p5_lm = run_paper(chn, 'TCI_full', 'DAI_thin', CONTROLS + ['wave_2024'],
                              'CHN', 'P5 CHINA POOLED (2012+2024)')

    # P5 by-wave
    for wave in ['CHN_2012', 'CHN_2024']:
        sub = pooled[pooled['dataset'] == wave].copy()
        sub['FSTS'] = sub['export_pct'] / 100
        sub['FSTS2'] = sub['FSTS'] ** 2
        sub['foreign_dummy'] = np.where(sub['foreign_own'].isna(), np.nan,
                                         np.where(sub['foreign_own'] > 0, 1.0, 0.0))
        sub = sub.dropna(subset=['ln_labor_prod', 'FSTS', 'ln_empl', 'firm_age']).copy()
        run_paper(sub, 'TCI_full', 'DAI_thin', CONTROLS, wave, f'P5 {wave}')

    # ── P4 VIETNAM POOLED ──
    vnm = pooled[pooled['country'] == 'VNM'].copy()
    vnm['wave_2015'] = (vnm['year'] == '2015').astype(float)
    vnm['wave_2023'] = (vnm['year'] == '2023').astype(float)
    vnm = vnm.dropna(subset=['ln_labor_prod', 'FSTS', 'ln_empl', 'firm_age']).copy()
    p4_df, p4_lm = run_paper(vnm, 'TCI_thin', 'DAI_thin', CONTROLS + ['wave_2015', 'wave_2023'],
                              'VNM', 'P4 VIETNAM POOLED (2009+2015+2023)')

    # P4 by-wave
    for wave in ['VNM_2009', 'VNM_2015', 'VNM_2023']:
        sub = pooled[pooled['dataset'] == wave].copy()
        sub['FSTS'] = sub['export_pct'] / 100
        sub['FSTS2'] = sub['FSTS'] ** 2
        sub['foreign_dummy'] = np.where(sub['foreign_own'].isna(), np.nan,
                                         np.where(sub['foreign_own'] > 0, 1.0, 0.0))
        sub = sub.dropna(subset=['ln_labor_prod', 'FSTS', 'ln_empl', 'firm_age']).copy()
        run_paper(sub, 'TCI_thin', 'DAI_thin', CONTROLS, wave, f'P4 {wave}')

    # ── SAVE RESULTS ──
    p3_df.to_csv(os.path.join(OUTPUT_DIR, 'results-p3-singapore.csv'), index=False)
    p5_df.to_csv(os.path.join(OUTPUT_DIR, 'results-p5-china.csv'), index=False)
    p4_df.to_csv(os.path.join(OUTPUT_DIR, 'results-p4-vietnam.csv'), index=False)
    print(f'\n\nResults saved to {OUTPUT_DIR}/')

    # ── GRAND SUMMARY ──
    print(f'\n{"="*90}')
    print('  GRAND SUMMARY — 3 PAPERS')
    print(f'{"="*90}')
    print(f'  {"":>20} {"SGP23":>10} {"CHN12":>10} {"CHN24":>10} {"VNM09":>10} {"VNM15":>10} {"VNM23":>10}')
    print(f'  {"-"*80}')

    summaries = {
        'SGP23': {'tp': p3_lm['lm_m2']['tp_pct'], 'lm': p3_lm['lm_m2']['lm_p']},
        'CHN_pooled': {'tp': p5_lm['lm_m2']['tp_pct'], 'lm': p5_lm['lm_m2']['lm_p']},
        'VNM_pooled': {'tp': p4_lm['lm_m2']['tp_pct'], 'lm': p4_lm['lm_m2']['lm_p']},
    }

    for key, val in summaries.items():
        print(f'  {key:<20} TP={val["tp"]:.1f}%  LM_p={val["lm"]:.4f}')


if __name__ == '__main__':
    main()
