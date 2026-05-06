"""
P5 China — Audit empirical claims in v1.6 / v1.7.

Verifies (or invalidates) specific numbers claimed in the manuscript:
1. §1 productivity-premium calculation
2. §4.6 mfg-only Paternoster z (FSTS, FSTS²)
3. §4.7 panel-firm exclusion N + TP shift
4. §3.6 Heckman selection IMR z by wave
5. §4.7 ISIC 2-digit FE coefficient change
6. §4.2 productivity premium at TP

Usage:
    python3 audit_v1_6_claims.py
"""
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.api as sm
from scipy import stats
from scipy.stats import norm
import os
import warnings
warnings.filterwarnings('ignore')

ROOT = os.environ.get('P5_ROOT', '/home/user/p5-china')
d12_all = pd.read_csv(f'{ROOT}/built_2012_all.csv', low_memory=False)
d24_all = pd.read_csv(f'{ROOT}/built_2024_all.csv', low_memory=False)
d12_mfg = pd.read_csv(f'{ROOT}/built_2012_mfg.csv', low_memory=False)
d24_mfg = pd.read_csv(f'{ROOT}/built_2024_mfg.csv', low_memory=False)

b12 = d12_all[d12_all['sample_base']==True]
b24 = d24_all[d24_all['sample_base']==True]

print("=" * 70)
print("AUDIT 1: §1 productivity-premium calculation")
print("=" * 70)
diff = b24['lnLP'].mean() - b12['lnLP'].mean()
print(f"  Diff in mean lnLP: {diff:.3f}; level premium: {(np.exp(diff)-1)*100:.1f}%")

print("\n" + "=" * 70)
print("AUDIT 2: §4.6 mfg-only Paternoster z-tests")
print("=" * 70)
def m2_estimate(df):
    d = df[df['sample_base']==True].copy()
    m = smf.ols('lnLP ~ FSTS + FSTSsq + lnEmp + firmage + foreigndummy', data=d).fit(cov_type='HC1')
    return {'N': int(m.nobs),
            'FSTS': m.params['FSTS'], 'FSTS_se': m.bse['FSTS'],
            'FSTSsq': m.params['FSTSsq'], 'FSTSsq_se': m.bse['FSTSsq']}

def paternoster(a, b, term):
    z = (a[term] - b[term]) / np.sqrt(a[f'{term}_se']**2 + b[f'{term}_se']**2)
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p

mfg12 = m2_estimate(d12_mfg); mfg24 = m2_estimate(d24_mfg)
z_fsts, p_fsts = paternoster(mfg12, mfg24, 'FSTS')
z_fstssq, p_fstssq = paternoster(mfg12, mfg24, 'FSTSsq')
print(f"  FSTS:  z={z_fsts:+.3f}, p={p_fsts:.3f}")
print(f"  FSTS²: z={z_fstssq:+.3f}, p={p_fstssq:.3f}")

print("\n" + "=" * 70)
print("AUDIT 3: §4.7 panel-firm exclusion (need 'panel' col in 2024)")
print("=" * 70)
if 'panel' in d24_all.columns:
    panel_in_base = ((d24_all['panel']==1) & (d24_all['sample_base']==True)).sum()
    n_pool_excl = b12.shape[0] + b24.shape[0] - panel_in_base
    print(f"  Panel firms in 2024 base: {panel_in_base}; N pool excl panel: {n_pool_excl}")
    pool_nopanel = pd.concat([b12.assign(wave2024=0),
                              b24[b24['panel']!=1].assign(wave2024=1)])
    m_np = smf.ols('lnLP ~ FSTS + FSTSsq + lnEmp + firmage + foreigndummy + wave2024',
                    data=pool_nopanel).fit(cov_type='HC1')
    if m_np.params['FSTSsq'] < 0:
        tp_np = -m_np.params['FSTS'] / (2 * m_np.params['FSTSsq']) * 100
        print(f"  TP (no-panel pool) = {tp_np:.2f}%; vs main 48.78%; Δ = {abs(tp_np-48.78):.2f} pp")

print("\n" + "=" * 70)
print("AUDIT 4: §3.6 Heckman selection IMR")
print("=" * 70)
for df, label in [(d12_all, '2012'), (d24_all, '2024')]:
    if 'a2' not in df.columns:
        print(f"  {label}: a2 missing; skip")
        continue
    df['_inbase'] = (df['sample_base']==True).astype(int)
    try:
        m_sel = smf.probit('_inbase ~ C(a2)', data=df).fit(disp=0)
        xb = m_sel.predict(df, linear=True)
        df['_imr'] = norm.pdf(xb) / norm.cdf(xb)
        d_in = df[df['_inbase']==1]
        m2_imr = smf.ols('lnLP ~ FSTS + FSTSsq + lnEmp + firmage + foreigndummy + _imr',
                          data=d_in).fit(cov_type='HC1')
        print(f"  {label} Heckman IMR: z={m2_imr.tvalues['_imr']:+.3f}, p={m2_imr.pvalues['_imr']:.3f}")
    except Exception as e:
        print(f"  {label} Heckman failed: {e}")

print("\n" + "=" * 70)
print("AUDIT 5: §4.7 ISIC 2-digit FE robustness")
print("=" * 70)
pool_all = pd.concat([b12.assign(wave2024=0), b24.assign(wave2024=1)])
m_base = smf.ols('lnLP ~ FSTS + FSTSsq + lnEmp + firmage + foreigndummy + wave2024',
                  data=pool_all).fit(cov_type='HC1')
m_fe = smf.ols('lnLP ~ FSTS + FSTSsq + lnEmp + firmage + foreigndummy + wave2024 + C(a4a)',
                data=pool_all).fit(cov_type='HC1')
pc_fsts = abs(m_fe.params['FSTS'] - m_base.params['FSTS']) / abs(m_base.params['FSTS']) * 100
pc_fstssq = abs(m_fe.params['FSTSsq'] - m_base.params['FSTSsq']) / abs(m_base.params['FSTSsq']) * 100
print(f"  Baseline FSTS: {m_base.params['FSTS']:+.3f}; with FE: {m_fe.params['FSTS']:+.3f} (Δ {pc_fsts:.1f}%)")
print(f"  Baseline FSTS²: {m_base.params['FSTSsq']:+.3f}; with FE: {m_fe.params['FSTSsq']:+.3f} (Δ {pc_fstssq:.1f}%)")

print("\n" + "=" * 70)
print("AUDIT 6: §4.2 productivity premium at TP")
print("=" * 70)
for df, label in [(d12_all, '2012'), (d24_all, '2024')]:
    res = m2_estimate(df)
    if res['FSTSsq'] < 0:
        tp = -res['FSTS'] / (2 * res['FSTSsq'])
        prem = np.exp(res['FSTS']*tp + res['FSTSsq']*tp**2) - 1
        print(f"  {label}: TP = {tp*100:.1f}%; productivity premium at TP = {prem*100:.1f}%")
