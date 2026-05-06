"""
P5 China — full M0..M8 + Paternoster z-test on 'all' (full private) frame.

Usage:
    export D2012=/path/to/China2012fullESN2700data.dta
    export D2024=/path/to/China2024fulldata.dta
    python3 full_models.py

Verified results vs manuscript v1.2:
    M2 turning point 2012  : 49.37 %  (v1.2: 49.4 %)
    M2 turning point 2024  : 47.19 %  (v1.2: 47.6 %)
    M2 turning point pooled: 48.78 %  (v1.2: 48.9 %)
    Paternoster z FSTS     : p = 0.412  (fail to reject equality → stable)
    Paternoster z FSTSsq   : p = 0.545  (fail to reject equality → stable)
"""
import os
import pyreadstat
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

D2012 = os.environ.get('D2012', 'China2012fullESN2700data.dta')
D2024 = os.environ.get('D2024', 'China2024fulldata.dta')


def yes_no_bin(s):
    s = pd.to_numeric(s, errors='coerce')
    return s.map({1: 1.0, 2: 0.0})


def zstd(s):
    s = pd.to_numeric(s, errors='coerce')
    return (s - s.mean()) / s.std()


def build(df, year, codes):
    df = df.copy()
    for v in ['d2', 'd3c', 'l1', 'b5', 'b2b']:
        df[v] = pd.to_numeric(df[v], errors='coerce')
        df.loc[df[v].isin(codes), v] = np.nan

    if year == 2012:
        bins = {'e6': 'e6', 'b8': 'b8', 'h_new': 'CNo1', 'h_rd': 'CNo3', 'c22b': 'c22b'}
    else:
        bins = {'e6': 'e6', 'b8': 'b8', 'h_new': 'h1', 'h_rd': 'h8', 'c22b': 'c22b'}
    for new, src in bins.items():
        df[new] = yes_no_bin(df[src]) if src in df.columns else np.nan

    df['lnLP'] = np.where((df['d2'] > 0) & (df['l1'] > 0), np.log(df['d2'] / df['l1']), np.nan)
    df['FSTS'] = df['d3c'] / 100
    df['FSTSsq'] = df['FSTS'] ** 2
    df['lnEmp'] = np.where(df['l1'] > 0, np.log(df['l1']), np.nan)
    df['firmage'] = np.where((df['b5'] > 1900) & (df['b5'] <= year), year - df['b5'], np.nan)
    df['foreigndummy'] = np.where(df['b2b'].notna(), (df['b2b'] > 0).astype(float), np.nan)

    for v in ['e6', 'b8', 'h_new', 'h_rd', 'c22b']:
        df[f'z_{v}'] = zstd(df[v])
    tci = df[['z_e6', 'z_b8', 'z_h_new', 'z_h_rd']]
    df['TCIfull'] = tci.mean(axis=1).where(tci.notna().sum(axis=1) >= 3)
    dai = df[['z_c22b', 'z_e6']]
    df['DAIthin'] = dai.mean(axis=1).where(dai.notna().sum(axis=1) >= 1)

    df['sample_base'] = df[['lnLP', 'FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy']].notna().all(axis=1)
    df['sample_dai'] = df['sample_base'] & df['DAIthin'].notna()
    df['sample_tci'] = df['sample_base'] & df['TCIfull'].notna()
    df['sample_full'] = df['sample_tci'] & df['DAIthin'].notna()
    df['wave2024'] = 1 if year == 2024 else 0
    return df


def fit(formula, d, cluster=None):
    m = smf.ols(formula, data=d)
    if cluster is None:
        return m.fit(cov_type='HC1')
    return m.fit(cov_type='cluster', cov_kwds={'groups': d[cluster].astype(int)})


def turning_point(model):
    b1, b2 = model.params['FSTS'], model.params['FSTSsq']
    if b2 >= 0:
        return None, None, None, None
    tp = -b1 / (2 * b2)
    g = pd.Series(0.0, index=model.params.index)
    g['FSTS'] = -1 / (2 * b2)
    g['FSTSsq'] = b1 / (2 * b2 ** 2)
    se = np.sqrt(g.values @ model.cov_params().values @ g.values)
    return tp, se, tp - 1.96 * se, tp + 1.96 * se


def paternoster(m1, m2, var):
    b1, se1 = m1.params[var], m1.bse[var]
    b2, se2 = m2.params[var], m2.bse[var]
    z = (b1 - b2) / np.sqrt(se1 ** 2 + se2 ** 2)
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return b1, se1, b2, se2, z, p


def run_all(df, label, cluster=None):
    print(f"\n{'=' * 60}\n{label}\n{'=' * 60}")
    base = df[df['sample_base']].copy()
    tci = df[df['sample_tci']].copy()
    dai = df[df['sample_dai']].copy()
    full = df[df['sample_full']].copy()

    ctrl = 'lnEmp + firmage + foreigndummy'
    suffix = ' + wave2024' if 'wave2024' in df.columns and df['wave2024'].nunique() > 1 else ''
    ctrl_full = ctrl + suffix

    out = {}
    out['M0'] = fit(f'lnLP ~ {ctrl_full}', base, cluster)
    out['M1'] = fit(f'lnLP ~ FSTS + {ctrl_full}', base, cluster)
    out['M2'] = fit(f'lnLP ~ FSTS + FSTSsq + {ctrl_full}', base, cluster)
    out['M3'] = fit(f'lnLP ~ FSTS + FSTSsq + TCIfull + {ctrl_full}', tci, cluster)
    out['M4'] = fit(f'lnLP ~ FSTS + FSTSsq + DAIthin + {ctrl_full}', dai, cluster)
    out['M5'] = fit(f'lnLP ~ TCIfull + {ctrl_full}', tci, cluster)
    out['M6'] = fit(f'lnLP ~ DAIthin + {ctrl_full}', dai, cluster)
    out['M7'] = fit(f'lnLP ~ TCIfull + DAIthin + {ctrl_full}', full, cluster)
    out['M8'] = fit(f'lnLP ~ FSTS + FSTSsq + TCIfull + DAIthin + {ctrl_full}', full, cluster)

    tp, se, lo, hi = turning_point(out['M2'])
    if tp is not None:
        print(f"  M2 turning point: {tp*100:.2f}% [95% CI {lo*100:.2f}, {hi*100:.2f}]  N={int(out['M2'].nobs)}")

    rows = []
    for name, m in out.items():
        for var in ['FSTS', 'FSTSsq', 'TCIfull', 'DAIthin']:
            if var in m.params.index:
                rows.append({'model': name, 'var': var,
                             'coef': m.params[var], 'se': m.bse[var],
                             'p': m.pvalues[var], 'N': int(m.nobs)})
    return out, pd.DataFrame(rows)


if __name__ == '__main__':
    df12_raw, _ = pyreadstat.read_dta(D2012)
    df24_raw, _ = pyreadstat.read_dta(D2024, encoding='utf-8')

    df12 = build(df12_raw, 2012, [-9, -7])
    df24 = build(df24_raw, 2024, [-9, -8, -7])

    df12['idstd'] = df12_raw['idstd'] if 'idstd' in df12_raw.columns else range(len(df12))
    df24['idstd'] = df24_raw['idstd'] if 'idstd' in df24_raw.columns else range(len(df12), len(df12) + len(df24))

    common = ['idstd', 'lnLP', 'FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy',
              'TCIfull', 'DAIthin', 'sample_base', 'sample_dai', 'sample_tci',
              'sample_full', 'wave2024']
    pooled = pd.concat([df12[common], df24[common]], ignore_index=True)
    print(f"Pooled total = {len(pooled)};  panel firms duplicated idstd: "
          f"{pooled['idstd'].duplicated(keep=False).sum() // 2}")

    m12, c12 = run_all(df12, '2012')
    m24, c24 = run_all(df24, '2024')
    mp, cp = run_all(pooled, 'POOLED (cluster idstd)', cluster='idstd')

    c12['wave'] = '2012'; c24['wave'] = '2024'; cp['wave'] = 'pooled'
    pd.concat([c12, c24, cp], ignore_index=True).to_csv('results_coefs.csv', index=False)

    print("\n" + "=" * 60 + "\nPATERNOSTER Z-TEST — cross-wave (2012 vs 2024) on M2\n" + "=" * 60)
    for v in ['FSTS', 'FSTSsq']:
        b1, se1, b2, se2, z, p = paternoster(m12['M2'], m24['M2'], v)
        verdict = 'stable' if p > 0.10 else 'rejected'
        print(f"  {v}: b12={b1:+.3f}({se1:.3f})  b24={b2:+.3f}({se2:.3f})  z={z:+.3f}  p={p:.3f}  ==> {verdict}")

    print("\n" + "=" * 60 + "\nM2 TURNING POINTS — three samples\n" + "=" * 60)
    for label, m in [('2012', m12['M2']), ('2024', m24['M2']), ('Pooled', mp['M2'])]:
        tp, se, lo, hi = turning_point(m)
        if tp is not None:
            print(f"  {label:>7}: {tp*100:6.2f}%   95% CI [{lo*100:6.2f}, {hi*100:6.2f}]   N={int(m.nobs)}")

    m2_table = pd.DataFrame({
        '2012': [f"{m12['M2'].params[v]:+.4f} ({m12['M2'].bse[v]:.4f})" if v in m12['M2'].params.index else '-'
                 for v in ['Intercept', 'FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy']],
        '2024': [f"{m24['M2'].params[v]:+.4f} ({m24['M2'].bse[v]:.4f})" if v in m24['M2'].params.index else '-'
                 for v in ['Intercept', 'FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy']],
        'Pooled': [f"{mp['M2'].params[v]:+.4f} ({mp['M2'].bse[v]:.4f})" if v in mp['M2'].params.index else '-'
                   for v in ['Intercept', 'FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy']],
    }, index=['Intercept', 'FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy'])
    print("\n" + m2_table.to_string())
    m2_table.to_csv('M2_table.csv')
    print("\nDone. Outputs: results_coefs.csv, M2_table.csv")
