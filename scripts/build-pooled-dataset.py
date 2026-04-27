#!/usr/bin/env python3
"""Build pooled WBES dataset from raw .dta files for P3/P4/P5 analysis."""

import sys
import os
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings('ignore')

DTA_FILES = {
    'VNM_2009': 'Vietnam2009fulldata.dta',
    'VNM_2015': 'Vietnam2015fulldata.dta',
    'VNM_2023': 'VietNam2023fulldata.dta',
    'CHN_2012': 'China2012fullESN2700data.dta',
    'CHN_2024': 'China2024fulldata.dta',
    'SGP_2023': 'Singapore2023fulldata.dta',
}

OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'analysis', 'pooled_wbes_6waves.csv')


def clean_binary(series):
    s = pd.to_numeric(series, errors='coerce').copy()
    s[s.isin([-9, -7, -99])] = np.nan
    out = pd.Series(np.nan, index=s.index, dtype=float)
    out[s == 1] = 1.0
    out[s == 2] = 0.0
    return out


def clean_continuous(series):
    s = pd.to_numeric(series, errors='coerce').copy()
    s[s.isin([-9, -7, -99])] = np.nan
    s[s < 0] = np.nan
    return s


def find_dta(filename, search_dirs):
    for d in search_dirs:
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if f.endswith(filename) or filename in f:
                return os.path.join(d, f)
    return None


def process_wave(name, raw):
    n = len(raw)
    country = name.split('_')[0]
    year = name.split('_')[1]

    df = pd.DataFrame(index=range(n))
    df['dataset'] = name
    df['country'] = country
    df['year'] = year

    df['website'] = clean_binary(raw['c22b']).values if 'c22b' in raw.columns else np.nan
    df['foreign_tech'] = clean_binary(raw['e6']).values if 'e6' in raw.columns else np.nan

    if 'h1' in raw.columns:
        df['product_innov'] = clean_binary(raw['h1']).values
    elif 'CNo1' in raw.columns:
        df['product_innov'] = clean_binary(raw['CNo1']).values
    else:
        df['product_innov'] = np.nan

    df['process_innov'] = clean_binary(raw['h5']).values if 'h5' in raw.columns else np.nan

    if name == 'VNM_2015':
        h8 = pd.to_numeric(raw['h8'], errors='coerce')
        h8[h8.isin([-9, -7, -99])] = np.nan
        h8[h8 < 0] = np.nan
        rd_vals = np.full(n, np.nan)
        rd_vals[~h8.isna().values] = np.where(h8.dropna().values > 0, 1.0, 0.0)
        df['rd_spending'] = rd_vals
    elif 'h8' in raw.columns:
        df['rd_spending'] = clean_binary(raw['h8']).values
    elif 'CNo3' in raw.columns:
        df['rd_spending'] = clean_binary(raw['CNo3']).values
    else:
        df['rd_spending'] = np.nan

    df['quality_cert'] = clean_binary(raw['b8']).values if 'b8' in raw.columns else np.nan
    df['epayment_pct'] = clean_continuous(raw['k33']).values if 'k33' in raw.columns else np.nan
    df['epay_supp_pct'] = clean_continuous(raw['k38']).values if 'k38' in raw.columns else np.nan

    sales = clean_continuous(raw['d2']) if 'd2' in raw.columns else pd.Series(np.nan, index=range(n))
    empl = clean_continuous(raw['l1']) if 'l1' in raw.columns else pd.Series(np.nan, index=range(n))
    df['total_sales'] = sales.values
    df['employees'] = empl.values

    sales_v = sales.values.astype(float)
    empl_v = empl.values.astype(float)
    with np.errstate(divide='ignore', invalid='ignore'):
        lp = np.where(
            (empl_v > 0) & (sales_v > 0) & np.isfinite(empl_v) & np.isfinite(sales_v),
            sales_v / empl_v, np.nan,
        )
        df['ln_labor_prod'] = np.where(np.isfinite(lp) & (lp > 0), np.log(lp), np.nan)
        df['ln_empl'] = np.where((empl_v > 0) & np.isfinite(empl_v), np.log(empl_v), np.nan)

    if 'd3a' in raw.columns:
        dom = clean_continuous(raw['d3a']).values.astype(float)
        exp_pct = 100.0 - dom
        exp_pct[np.isnan(dom)] = np.nan
        exp_pct[exp_pct < 0] = np.nan
        df['export_pct'] = exp_pct
        df['exporter'] = np.where(np.isnan(exp_pct), np.nan, np.where(exp_pct > 0, 1.0, 0.0))
    else:
        df['export_pct'] = np.nan
        df['exporter'] = np.nan

    df['firm_age'] = clean_continuous(raw['a7']).values if 'a7' in raw.columns else np.nan
    df['manager_exp'] = clean_continuous(raw['a6a']).values if 'a6a' in raw.columns else np.nan
    df['foreign_own'] = clean_continuous(raw['b2b']).values if 'b2b' in raw.columns else np.nan

    return df


def build_indices(pooled):
    pooled['TCI_thin'] = pooled[['foreign_tech', 'quality_cert']].mean(axis=1)
    pooled['TCI_full'] = pooled[['foreign_tech', 'product_innov', 'rd_spending', 'quality_cert']].mean(axis=1)
    pooled['DAI_thin'] = pooled[['website', 'foreign_tech']].mean(axis=1)

    tmp = pd.DataFrame({
        'w': pooled['website'].values,
        'e': (pooled['epayment_pct'] / 100).values,
        's': (pooled['epay_supp_pct'] / 100).values,
    })
    pooled['DAI_rich'] = tmp.mean(axis=1).values
    return pooled


def main():
    search_dirs = [
        '/root/.claude/uploads/ee8cf557-3187-40cd-a8f8-78b91d84d086/',
        '/root/.claude/uploads/ce7c31e1-991b-4902-9cc8-e11349ab817c/',
        '/root/.claude/uploads/099f45cf-eefb-48d3-ab08-2bc6562f7dca/',
    ]

    if len(sys.argv) > 1:
        search_dirs = [sys.argv[1]]

    all_rows = []
    for name, filename in DTA_FILES.items():
        path = find_dta(filename, search_dirs)
        if path is None:
            print(f'  SKIP {name}: {filename} not found')
            continue

        raw = pd.read_stata(path, convert_categoricals=False).reset_index(drop=True)
        df = process_wave(name, raw)
        all_rows.append(df)
        print(f'  {name}: {len(df)} rows from {os.path.basename(path)}')

    if not all_rows:
        print('ERROR: No .dta files found. Pass directory as argument.')
        sys.exit(1)

    pooled = pd.concat(all_rows, ignore_index=True)
    pooled = build_indices(pooled)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    pooled.to_csv(OUTPUT_PATH, index=False)
    print(f'\nSaved {len(pooled)} rows to {OUTPUT_PATH}')
    print(pooled['dataset'].value_counts().to_string())


if __name__ == '__main__':
    main()
