"""
R3 Phase 0 — Diagnose the TCI standardization variant used in manuscript.

Canonical run reproduces FSTS²×DAI and AdjR² but produces TCI=0.153 vs
manuscript Table 2 M8 reporting TCI=0.153 (matched), and Table 3 baseline
reporting TCI=0.187 (mismatched). The manuscript's other Table 3 rows
also show TCI consistently *higher* than canonical by 0.02–0.05.

This is consistent with the Table 3 baseline row being a stale value
imported from a *different* TCI standardization variant. Test variants:

  V1 (canonical):   z-score each component, average, then re-z-score.
  V2 (simple-avg):  average raw 0/1 indicators, then z-score the average.
  V3 (no-restandardize): z-score each component, average — leave as-is
                         (no second z-score, sd ≠ 1).
  V4 (sum-not-mean): sum of z-scored components (not average), then z-score.

For each variant, fit the canonical M8 (TCI_full + DAI_rich) and report
TCI coefficient. The variant whose TCI≈0.187 explains the manuscript's
Table 3 baseline row.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.formula.api as smf

REPO = Path(__file__).resolve().parents[2]
DTA = REPO / "data" / "raw" / "Singapore2023fulldata.dta"


def load():
    df, _ = pyreadstat.read_dta(str(DTA))
    for col in ["b2b", "d2", "l1", "b5", "d3c", "a4a", "a4b_v4"]:
        df[col] = df[col].where(df[col] >= 0, np.nan)
    for col in ["b8", "e6", "h1", "h8"]:
        df[col + "_yn"] = (df[col] == 1).astype(int)
    df["c22b_yn"] = (df["c22b"] == 1).astype(int)
    df["dai_drop"] = (df["k33"] < 0) & (df["k38"] < 0)
    k33_med = df.loc[df["k33"] >= 0, "k33"].median()
    k38_med = df.loc[df["k38"] >= 0, "k38"].median()
    df["k33_imp"] = df["k33"].where(df["k33"] >= 0, k33_med)
    df["k38_imp"] = df["k38"].where(df["k38"] >= 0, k38_med)
    df.loc[df["dai_drop"], ["k33_imp", "k38_imp"]] = np.nan
    df["lp"] = df["d2"] / df["l1"]
    df["ln_lp"] = np.log(df["lp"])
    lo, hi = df["ln_lp"].quantile([0.01, 0.99])
    df["ln_lp"] = df["ln_lp"].clip(lo, hi)
    df["fsts"] = df["d3c"] / 100.0
    df["fsts_c"] = df["fsts"] - df["fsts"].mean()
    df["fsts_c2"] = df["fsts_c"] ** 2
    df["ln_empl"] = np.log(df["l1"])
    df["firm_age"] = 2023 - df["b5"]
    df["foreign"] = (df["b2b"].fillna(0) >= 10).astype(int)

    def bucket(nace):
        if pd.isna(nace):
            return np.nan
        n = int(nace)
        if 10 <= n <= 33:
            return "manufacturing"
        if 41 <= n <= 43:
            return "construction"
        return "retail_services"

    df["broad_sector"] = df["a4b_v4"].apply(bucket)
    return df


def make_dai_rich(df):
    df = df.copy()
    parts = ["c22b_yn", "k33_imp", "k38_imp"]
    for c in parts:
        mu, sd = df[c].mean(), df[c].std()
        df[c + "_z"] = (df[c] - mu) / sd
    raw = df[[c + "_z" for c in parts]].sum(axis=1, skipna=False) / len(parts)
    df["DAI"] = (raw - raw.mean()) / raw.std()
    return df


def tci_v1_canonical(df):
    df = df.copy()
    parts = ["b8_yn", "e6_yn", "h1_yn", "h8_yn"]
    for c in parts:
        mu, sd = df[c].mean(), df[c].std()
        df[c + "_z"] = (df[c] - mu) / sd
    raw = df[[c + "_z" for c in parts]].sum(axis=1) / len(parts)
    df["TCI"] = (raw - raw.mean()) / raw.std()
    return df


def tci_v2_simple_avg(df):
    df = df.copy()
    parts = ["b8_yn", "e6_yn", "h1_yn", "h8_yn"]
    raw = df[parts].sum(axis=1) / len(parts)
    df["TCI"] = (raw - raw.mean()) / raw.std()
    return df


def tci_v3_no_restandardize(df):
    df = df.copy()
    parts = ["b8_yn", "e6_yn", "h1_yn", "h8_yn"]
    for c in parts:
        mu, sd = df[c].mean(), df[c].std()
        df[c + "_z"] = (df[c] - mu) / sd
    df["TCI"] = df[[c + "_z" for c in parts]].sum(axis=1) / len(parts)
    return df


def tci_v4_sum_z(df):
    df = df.copy()
    parts = ["b8_yn", "e6_yn", "h1_yn", "h8_yn"]
    for c in parts:
        mu, sd = df[c].mean(), df[c].std()
        df[c + "_z"] = (df[c] - mu) / sd
    raw = df[[c + "_z" for c in parts]].sum(axis=1)
    df["TCI"] = (raw - raw.mean()) / raw.std()
    return df


def fit(df, mask=None):
    df = df.copy()
    df["fsts_c_DAI"] = df["fsts_c"] * df["DAI"]
    df["fsts_c2_DAI"] = df["fsts_c2"] * df["DAI"]
    core = ["ln_lp", "fsts_c", "fsts_c2", "TCI", "DAI",
            "fsts_c_DAI", "fsts_c2_DAI",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    m = df[core].notna().all(axis=1)
    if mask is not None:
        m &= mask
    formula = (
        "ln_lp ~ fsts_c + fsts_c2 + TCI + DAI"
        " + fsts_c_DAI + fsts_c2_DAI"
        " + ln_empl + firm_age + foreign + C(broad_sector)"
    )
    model = smf.ols(formula, data=df[m]).fit(cov_type="HC1")
    return {
        "n": int(m.sum()),
        "TCI": float(model.params["TCI"]),
        "DAI": float(model.params["DAI"]),
        "fsts_c2_DAI": float(model.params["fsts_c2_DAI"]),
        "adj_rsq": float(model.rsquared_adj),
        "TCI_sd": float(df.loc[m, "TCI"].std()),
    }


def main():
    print("=" * 75)
    print("R3 Phase 0 — Test which TCI variant matches manuscript Table 3 baseline")
    print(f"  Manuscript Table 3 baseline: TCI = 0.187")
    print(f"  Manuscript Table 2 M8:       TCI = 0.153 (matched by V1)")
    print("=" * 75)

    df = load()

    variants = {
        "V1_canonical_z_avg_z":  tci_v1_canonical,
        "V2_simple_avg_then_z":  tci_v2_simple_avg,
        "V3_z_avg_no_restand":   tci_v3_no_restandardize,
        "V4_sum_z_then_z":       tci_v4_sum_z,
    }

    print(f"\n{'Variant':<28}{'N':>5}{'TCI_β':>10}{'TCI_SD':>10}"
          f"{'FSTS²×DAI':>12}{'AdjR²':>8}")
    print("-" * 75)
    results = {}
    for name, builder in variants.items():
        d = builder(df)
        d = make_dai_rich(d)
        r = fit(d)
        results[name] = r
        print(f"{name:<28}{r['n']:>5}{r['TCI']:>+10.4f}"
              f"{r['TCI_sd']:>10.4f}{r['fsts_c2_DAI']:>+12.4f}"
              f"{r['adj_rsq']:>8.4f}")

    print(f"\n{'TARGET (Table 3 baseline)':<28}{'617':>5}{'+0.187':>10}"
          f"{'?':>10}{'+2.972':>12}{'0.192':>8}")

    # Find best match on TCI alone
    best = min(variants, key=lambda v: abs(results[v]["TCI"] - 0.187))
    print(f"\n→ TCI=0.187 best matches: {best} (TCI={results[best]['TCI']:.4f})")
    print(f"   But its FSTS²×DAI = {results[best]['fsts_c2_DAI']:.4f} "
          f"(Table 3 reports 2.972 — distance {abs(results[best]['fsts_c2_DAI']-2.972):.3f})")
    if abs(results[best]["fsts_c2_DAI"] - 2.972) > 0.10:
        print("\n   → Even the best TCI variant does NOT reproduce Table 3 baseline's")
        print("     joint pattern (TCI=0.187, FSTS²×DAI=2.972, AdjR²=0.192).")
        print("     Most likely: Table 3 baseline is a stale row from an earlier")
        print("     manuscript draft and should be replaced with the canonical M8")
        print("     numbers (TCI=0.153, FSTS²×DAI=3.119, AdjR²=0.196).")


if __name__ == "__main__":
    main()
