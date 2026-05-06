"""
P5 China — Three-way moderation test: DOI × Year2024 × Tech.

H3 dynamic moderation hypothesis (per dissertation-architecture v1.4):
    Tech-conditioned shift over time = β₉, β₁₀ ≠ 0 in:

    lnLP = β₀ + β₁·DOI + β₂·DOI² + β₃·Year2024
         + β₄·DOI×Year2024 + β₅·DOI²×Year2024
         + β₆·Tech + β₇·DOI×Tech + β₈·DOI²×Tech
         + β₉·DOI×Year2024×Tech + β₁₀·DOI²×Year2024×Tech
         + γ·Controls + ε

Joint F-tests:
    F1: (β₄, β₅) = 0 → cross-wave shape difference (H2 shift)
    F2: (β₇, β₈) = 0 → Tech moderates curvature (H3 cross-sectional)
    F3: (β₉, β₁₀) = 0 → Tech-conditioned dynamic moderation (H3 dynamic)

Verified results (Python on full WBES private-firm frame, sample_full N = 3,559):
    F1: F(2, 3558) = 2.236, p = 0.107  → FAIL TO REJECT (no shift detected)
    F2: F(2, 3558) = 3.256, p = 0.039  → marginal pooled support but individual coefs NS
    F3: F(2, 3558) = 0.274, p = 0.760  → NO support for dynamic moderation

Usage:
    export D2012=/path/to/China2012fullESN2700data.dta
    export D2024=/path/to/China2024fulldata.dta
    python3 three_way_moderation.py
"""
import os
import pyreadstat
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
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

    df['lnLP'] = np.where((df['d2'] > 0) & (df['l1'] > 0),
                          np.log(df['d2'] / df['l1']), np.nan)
    df['DOI'] = df['d3c'] / 100
    df['DOIsq'] = df['DOI'] ** 2
    df['lnEmp'] = np.where(df['l1'] > 0, np.log(df['l1']), np.nan)
    df['firmage'] = np.where((df['b5'] > 1900) & (df['b5'] <= year),
                             year - df['b5'], np.nan)
    df['foreigndummy'] = np.where(df['b2b'].notna(), (df['b2b'] > 0).astype(float), np.nan)

    for v in ['e6', 'b8', 'h_new', 'h_rd', 'c22b']:
        df[f'z_{v}'] = zstd(df[v])
    tci = df[['z_e6', 'z_b8', 'z_h_new', 'z_h_rd']]
    df['Tech'] = tci.mean(axis=1).where(tci.notna().sum(axis=1) >= 3)

    df['wave2024'] = 1 if year == 2024 else 0
    df['sample_full'] = df[['lnLP', 'DOI', 'DOIsq', 'lnEmp', 'firmage',
                             'foreigndummy', 'Tech']].notna().all(axis=1)
    return df


def run_three_way(pooled, cluster='idstd'):
    """Run full pooled 3-way interaction spec on sample_full."""
    d = pooled[pooled['sample_full']].copy()
    d['DOI_w24']        = d['DOI']    * d['wave2024']
    d['DOIsq_w24']      = d['DOIsq']  * d['wave2024']
    d['DOI_Tech']       = d['DOI']    * d['Tech']
    d['DOIsq_Tech']     = d['DOIsq']  * d['Tech']
    d['DOI_w24_Tech']   = d['DOI']    * d['wave2024'] * d['Tech']
    d['DOIsq_w24_Tech'] = d['DOIsq']  * d['wave2024'] * d['Tech']

    formula = ('lnLP ~ DOI + DOIsq + wave2024 '
               '+ DOI_w24 + DOIsq_w24 '
               '+ Tech + DOI_Tech + DOIsq_Tech '
               '+ DOI_w24_Tech + DOIsq_w24_Tech '
               '+ lnEmp + firmage + foreigndummy')
    m = smf.ols(formula, data=d).fit(
        cov_type='cluster', cov_kwds={'groups': d[cluster].astype(int)})
    return m, d


def report_F(model, terms, label):
    R = np.zeros((len(terms), len(model.params)))
    name_to_idx = {n: i for i, n in enumerate(model.params.index)}
    for i, t in enumerate(terms):
        if t not in name_to_idx:
            return None, None
        R[i, name_to_idx[t]] = 1
    test = model.f_test(R)
    fval = float(test.fvalue) if np.isscalar(test.fvalue) else float(np.atleast_1d(test.fvalue).flatten()[0])
    pval = float(test.pvalue)
    print(f"\n  {label}")
    print(f"     F({int(test.df_num)}, {int(test.df_denom)}) = {fval:.3f},  p = {pval:.4f}")
    return fval, pval


def main():
    df12_raw, _ = pyreadstat.read_dta(D2012)
    df24_raw, _ = pyreadstat.read_dta(D2024, encoding='utf-8')
    df12 = build(df12_raw, 2012, [-9, -7])
    df24 = build(df24_raw, 2024, [-9, -8, -7])
    df12['idstd'] = df12_raw['idstd']
    df24['idstd'] = df24_raw['idstd']

    common = ['idstd', 'lnLP', 'DOI', 'DOIsq', 'wave2024', 'Tech',
              'lnEmp', 'firmage', 'foreigndummy', 'sample_full']
    pooled = pd.concat([df12[common], df24[common]], ignore_index=True)

    print("=" * 70)
    print("THREE-WAY MODERATION TEST (H3 dynamic)")
    print("=" * 70)
    print(f"Pooled sample_full N = {pooled['sample_full'].sum()}")

    model, d = run_three_way(pooled)

    focal = ['DOI', 'DOIsq', 'wave2024', 'DOI_w24', 'DOIsq_w24',
             'Tech', 'DOI_Tech', 'DOIsq_Tech',
             'DOI_w24_Tech', 'DOIsq_w24_Tech']
    print("\n--- Focal interaction coefficients ---")
    for t in focal:
        if t in model.params.index:
            b = model.params[t]; se = model.bse[t]; p = model.pvalues[t]
            sig = '***' if p < .01 else '**' if p < .05 else '*' if p < .10 else ''
            print(f"  {t:<22}  β = {b:+.4f}  (SE = {se:.4f})  p = {p:.4f}  {sig}")

    print("\n--- Joint F-tests ---")
    f1, p1 = report_F(model, ['DOI_w24', 'DOIsq_w24'],
                      'F1: H2 cross-wave shape shift')
    f2, p2 = report_F(model, ['DOI_Tech', 'DOIsq_Tech'],
                      'F2: H3 cross-sectional Tech moderation')
    f3, p3 = report_F(model, ['DOI_w24_Tech', 'DOIsq_w24_Tech'],
                      'F3: H3 dynamic Tech×wave moderation')

    print("\n=== VERDICT ===")
    print(f"  H2 (predicted shift):              p = {p1:.3f}  "
          f"{'REJECT' if p1 < .05 else 'FAIL TO REJECT — stability finding'}")
    print(f"  H3 cross-sectional Tech mod:        p = {p2:.3f}  "
          f"{'SUPPORT' if p2 < .05 else 'NO support'}")
    print(f"  H3 dynamic Tech×wave moderation:    p = {p3:.3f}  "
          f"{'SUPPORT' if p3 < .05 else 'NO support'}")

    rows = []
    for t in focal:
        if t in model.params.index:
            rows.append({'term': t, 'coef': model.params[t],
                         'se': model.bse[t], 'p': model.pvalues[t],
                         'N': int(model.nobs)})
    rows.append({'term': 'F1_shift',  'coef': np.nan, 'se': np.nan, 'p': p1, 'N': int(model.nobs)})
    rows.append({'term': 'F2_modX',   'coef': np.nan, 'se': np.nan, 'p': p2, 'N': int(model.nobs)})
    rows.append({'term': 'F3_modDyn', 'coef': np.nan, 'se': np.nan, 'p': p3, 'N': int(model.nobs)})
    pd.DataFrame(rows).to_csv('three_way_moderation.csv', index=False)
    print("\nSaved: three_way_moderation.csv")


if __name__ == '__main__':
    main()
