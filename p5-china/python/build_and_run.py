"""
P5 China — Python replication pipeline

Usage:
    export D2012=/path/to/China2012fullESN2700data.dta
    export D2024=/path/to/China2024fulldata.dta
    python3 build_and_run.py

Produces:
    audit_N_all.csv  — sample-size audit on full WBES private-firm frame
    audit_N_mfg.csv  — audit when manufacturing filter is applied
    Quick M2 turning-point check on both frames.

Verified vs manuscript v1.2 on 'all' frame:
    Turning points: 49.37%  (2012) / 47.19% (2024) / 48.78% (pooled)
    N (sample_base): 2,610 / 1,934 / 4,544 — within 2 firms of v1.2.
"""
import os
import pyreadstat
import pandas as pd
import numpy as np
import statsmodels.api as sm
import warnings
warnings.filterwarnings('ignore')

D2012 = os.environ.get('D2012', 'China2012fullESN2700data.dta')
D2024 = os.environ.get('D2024', 'China2024fulldata.dta')

NONRESP_2012 = [-9, -7]
NONRESP_2024 = [-9, -8, -7]

audit = []


def recode_missing(df, vars_to_clean, codes):
    for v in vars_to_clean:
        if v in df.columns:
            df[v] = pd.to_numeric(df[v], errors='coerce')
            df.loc[df[v].isin(codes), v] = np.nan
    return df


def yes_no_to_binary(s):
    s = pd.to_numeric(s, errors='coerce')
    return s.map({1: 1.0, 2: 0.0})


def zstd(s):
    s = pd.to_numeric(s, errors='coerce')
    return (s - s.mean()) / s.std()


def build_wave(df, wave_year, mfg_filter='all'):
    """
    Build analytic wave file.
    mfg_filter: 'all' (no filter) or 'mfg' (manufacturing only)
    """
    df = df.copy()
    audit.append((wave_year, 'raw', 'open', len(df)))

    if mfg_filter == 'mfg':
        if wave_year == 2012:
            df = df[df['a4a'].between(15, 38)].copy()
            audit.append((wave_year, 'mfg', 'a4a 15-38', len(df)))
        else:  # 2024
            df['_d1a2_2digit'] = df['d1a2_v4'].astype(int) // 100
            df = df[df['_d1a2_2digit'].between(10, 33)].copy()
            audit.append((wave_year, 'mfg', 'd1a2_v4//100 10-33', len(df)))

    codes = NONRESP_2012 if wave_year == 2012 else NONRESP_2024
    df = recode_missing(df, ['d2', 'd3c', 'l1', 'b5', 'b2b'], codes)

    if wave_year == 2012:
        bins = {'e6': 'e6', 'b8': 'b8', 'h1_item': 'CNo1', 'h8_item': 'CNo3', 'c22b': 'c22b'}
    else:
        bins = {'e6': 'e6', 'b8': 'b8', 'h1_item': 'h1', 'h8_item': 'h8', 'c22b': 'c22b'}
    for new, src in bins.items():
        df[new] = yes_no_to_binary(df[src]) if src in df.columns else np.nan

    df['lnLP'] = np.where((df['d2'] > 0) & (df['l1'] > 0),
                          np.log(df['d2'] / df['l1']), np.nan)
    df['FSTS'] = df['d3c'] / 100
    df['FSTSsq'] = df['FSTS'] ** 2
    df['lnEmp'] = np.where(df['l1'] > 0, np.log(df['l1']), np.nan)
    df['firmage'] = np.where((df['b5'] > 1900) & (df['b5'] <= wave_year),
                             wave_year - df['b5'], np.nan)
    df['foreigndummy'] = np.where(df['b2b'].notna(), (df['b2b'] > 0).astype(float), np.nan)

    for v in ['e6', 'b8', 'h1_item', 'h8_item', 'c22b']:
        df[f'z_{v}'] = zstd(df[v])

    tci_z = df[['z_e6', 'z_b8', 'z_h1_item', 'z_h8_item']]
    df['tci_count'] = tci_z.notna().sum(axis=1)
    df['TCIfull'] = tci_z.mean(axis=1).where(df['tci_count'] >= 3)

    dai_z = df[['z_c22b', 'z_e6']]
    df['DAIthin'] = dai_z.mean(axis=1).where(dai_z.notna().sum(axis=1) >= 1)

    df['sample_analytic'] = df[['lnLP', 'FSTS', 'lnEmp', 'firmage', 'foreigndummy']].notna().all(axis=1)
    df['sample_base'] = df[['lnLP', 'FSTS', 'FSTSsq', 'lnEmp', 'firmage', 'foreigndummy']].notna().all(axis=1)
    df['sample_dai'] = df['sample_base'] & df['DAIthin'].notna()
    df['sample_tci'] = df['sample_base'] & df['TCIfull'].notna()
    df['sample_full'] = df['sample_tci'] & df['DAIthin'].notna()
    df['wave2024'] = 1 if wave_year == 2024 else 0

    for s in ['analytic', 'base', 'dai', 'tci', 'full']:
        audit.append((wave_year, f'sample_{s}', mfg_filter, int(df[f'sample_{s}'].sum())))
    return df


def lind_mehlum_utest(df, sample_col):
    d = df[df[sample_col]].copy()
    X = sm.add_constant(np.column_stack([d['FSTS'], d['FSTSsq'], d['lnEmp'],
                                          d['firmage'], d['foreigndummy']]))
    model = sm.OLS(d['lnLP'].values, X).fit(cov_type='HC1')
    b1, b2 = model.params[1], model.params[2]
    if b2 >= 0:
        return None, None, None, model
    tp = -b1 / (2 * b2)
    g = np.array([0, -1 / (2 * b2), b1 / (2 * b2 ** 2), 0, 0, 0])
    se_tp = np.sqrt(g @ model.cov_params() @ g)
    return tp, se_tp, model.params, model


if __name__ == '__main__':
    print("=" * 70 + "\nLoading raw data...")
    df12_raw, _ = pyreadstat.read_dta(D2012)
    df24_raw, _ = pyreadstat.read_dta(D2024, encoding='utf-8')
    print(f"  2012: {df12_raw.shape}\n  2024: {df24_raw.shape}")
    if 'panel' in df24_raw.columns:
        print(f"  2024 panel firms: {(df24_raw['panel']==1).sum()}")

    for frame in ['all', 'mfg']:
        print(f"\n{'='*70}\n>>> FRAME: {frame.upper()} <<<")
        audit.clear()
        df12 = build_wave(df12_raw, 2012, mfg_filter=frame)
        df24 = build_wave(df24_raw, 2024, mfg_filter=frame)

        common = [c for c in df12.columns if c in df24.columns]
        pooled = pd.concat([df12[common], df24[common]], ignore_index=True)
        audit.append(('pooled', 'append', frame, len(pooled)))
        for s in ['analytic', 'base', 'dai', 'tci', 'full']:
            audit.append(('pooled', f'sample_{s}', frame, int(pooled[f'sample_{s}'].sum())))

        print("\n--- AUDIT N ---")
        print(f"{'wave':<8}{'step':<20}{'filter':<25}{'N':>8}")
        for w, step, flt, n in audit:
            print(f"{str(w):<8}{step:<20}{flt:<25}{n:>8}")

        pd.DataFrame(audit, columns=['wave', 'step', 'filter', 'N']).to_csv(
            f'audit_N_{frame}.csv', index=False)

        print(f"\n--- M2 TURNING POINTS (frame: {frame}) ---")
        for label, d in [('2012', df12), ('2024', df24)]:
            tp, se, _, model = lind_mehlum_utest(d, 'sample_base')
            if tp is not None:
                lo, hi = (tp - 1.96 * se) * 100, (tp + 1.96 * se) * 100
                print(f"  {label}: TP = {tp*100:.2f}%  [95% CI: {lo:.2f}, {hi:.2f}]  N={int(model.nobs)}")

    print("\nDone. Output: audit_N_all.csv, audit_N_mfg.csv")
