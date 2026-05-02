"""
R3 Phase 0 — Canonical M8 estimation from raw WBES Singapore 2023 .dta.

LOCKED SPECIFICATION (single source of truth for all R3 work).
Replicates the spec used to generate Manuscript MIR Round 2 results.

Sample construction (yields N=617 for the DAI/M8 sample):
  Continuous vars (b2b, d2, l1, b5, d3c, a4a, a4b_v4): negative WBES codes
    (-9 / -7 / -8) → NaN.
  TCI binary components (b8, e6, h1, h8): yes=1 if value==1, else 0
    (treats refusals/don't-know as "no", per H2 conservative reading).
  DAI binary (c22b): same yes-coding as TCI.
  DAI continuous (k33, k38): drop firms missing BOTH (6 firms → N=617);
    impute single-missing with sample median.

Composite construction:
  TCI (z-standardized formative composite over 4 binary indicators):
    components = {b8_yn, e6_yn, h1_yn, h8_yn}.
    Each z-scored, averaged, then re-z-scored.
  DAI (z-standardized formative composite over 3 indicators):
    components = {c22b_yn, k33_imp, k38_imp}.
    Each z-scored, averaged, then re-z-scored.

Productivity:
  ln_lp = ln(d2 / l1), winsorized at 1% and 99%.

FSTS:
  fsts   = d3c / 100                  (export share, 0–1 scale)
  fsts_c = fsts - mean(fsts)          (mean-centered)
  fsts_c2 = fsts_c ** 2

Controls:
  ln_empl  = ln(l1)
  firm_age = 2023 - b5
  foreign  = 1 if b2b ≥ 10 (≥10% foreign ownership), else 0
  broad_sector ∈ {manufacturing, retail_services, construction} from a4b_v4 NACE.

Model M8 (locked):
  ln_lp ~ fsts_c + fsts_c2 + TCI + DAI + fsts_c_DAI + fsts_c2_DAI
        + ln_empl + firm_age + foreign + C(broad_sector)
  HC1 robust SE.

Outputs:
  outputs/r3/audit/m8_canonical.json   (params, SE, p-values, fit)
  outputs/r3/audit/m8_canonical.csv    (one row per coefficient)
  outputs/r3/audit/m8_canonical.txt    (statsmodels summary)
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.formula.api as smf

REPO = Path(__file__).resolve().parents[2]
DTA = REPO / "data" / "raw" / "Singapore2023fulldata.dta"
OUT_DIR = REPO / "outputs" / "r3" / "audit"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def build_analysis_frame() -> pd.DataFrame:
    df, _ = pyreadstat.read_dta(str(DTA))

    # 1. Negative WBES codes → NaN for continuous variables.
    for col in ["b2b", "d2", "l1", "b5", "d3c", "a4a", "a4b_v4"]:
        df[col] = df[col].where(df[col] >= 0, np.nan)

    # 2. TCI binary components: yes=1, else 0 (incl. refusals).
    for col in ["b8", "e6", "h1", "h8"]:
        df[col + "_yn"] = (df[col] == 1).astype(int)

    # 3. DAI binary (c22b): same coding.
    df["c22b_yn"] = (df["c22b"] == 1).astype(int)

    # 4. DAI continuous (k33, k38): drop firms missing both; impute single-missing.
    df["dai_drop"] = (df["k33"] < 0) & (df["k38"] < 0)
    k33_med = df.loc[df["k33"] >= 0, "k33"].median()
    k38_med = df.loc[df["k38"] >= 0, "k38"].median()
    df["k33_imp"] = df["k33"].where(df["k33"] >= 0, k33_med)
    df["k38_imp"] = df["k38"].where(df["k38"] >= 0, k38_med)
    df.loc[df["dai_drop"], ["k33_imp", "k38_imp", "c22b_yn"]] = np.nan

    # 5. Productivity (winsorized 1/99).
    df["lp"] = df["d2"] / df["l1"]
    df["ln_lp"] = np.log(df["lp"])
    lo, hi = df["ln_lp"].quantile([0.01, 0.99])
    df["ln_lp"] = df["ln_lp"].clip(lo, hi)

    # 6. FSTS (mean-centered, squared).
    df["fsts"] = df["d3c"] / 100.0
    fsts_mean = df["fsts"].mean()
    df["fsts_c"] = df["fsts"] - fsts_mean
    df["fsts_c2"] = df["fsts_c"] ** 2

    # 7. TCI composite.
    tci_parts = ["b8_yn", "e6_yn", "h1_yn", "h8_yn"]
    for c in tci_parts:
        mu, sd = df[c].mean(), df[c].std()
        df[c + "_z"] = (df[c] - mu) / sd
    df["tci_raw"] = df[[c + "_z" for c in tci_parts]].sum(axis=1) / 4
    df["TCI"] = (df["tci_raw"] - df["tci_raw"].mean()) / df["tci_raw"].std()

    # 8. DAI composite.
    dai_parts = ["c22b_yn", "k33_imp", "k38_imp"]
    for c in dai_parts:
        mu, sd = df[c].mean(), df[c].std()
        df[c + "_z"] = (df[c] - mu) / sd
    df["dai_raw"] = df[[c + "_z" for c in dai_parts]].sum(axis=1, skipna=False) / 3
    df["DAI"] = (df["dai_raw"] - df["dai_raw"].mean()) / df["dai_raw"].std()

    # 9. Controls.
    df["ln_empl"] = np.log(df["l1"])
    df["firm_age"] = 2023 - df["b5"]
    df["foreign"] = (df["b2b"].fillna(0) >= 10).astype(int)

    # 10. Broad sector (NACE → 3 buckets).
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

    # 11. Interactions for moderation models.
    df["fsts_c_DAI"] = df["fsts_c"] * df["DAI"]
    df["fsts_c2_DAI"] = df["fsts_c2"] * df["DAI"]
    df["fsts_c_TCI"] = df["fsts_c"] * df["TCI"]
    df["fsts_c2_TCI"] = df["fsts_c2"] * df["TCI"]

    df.attrs["fsts_mean"] = float(fsts_mean)
    return df


def fit_m8(df: pd.DataFrame):
    core = ["ln_lp", "fsts_c", "fsts_c2", "TCI", "DAI",
            "fsts_c_DAI", "fsts_c2_DAI",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    mask = df[core].notna().all(axis=1)
    formula = (
        "ln_lp ~ fsts_c + fsts_c2 + TCI + DAI"
        " + fsts_c_DAI + fsts_c2_DAI"
        " + ln_empl + firm_age + foreign + C(broad_sector)"
    )
    model = smf.ols(formula, data=df[mask]).fit(cov_type="HC1")
    return model, formula, int(mask.sum())


def serialize(model, formula, n, label):
    return {
        "label": label,
        "formula": formula,
        "n": n,
        "rsquared": float(model.rsquared),
        "rsquared_adj": float(model.rsquared_adj),
        "fvalue": float(model.fvalue),
        "f_pvalue": float(model.f_pvalue),
        "aic": float(model.aic),
        "bic": float(model.bic),
        "params": {k: float(v) for k, v in model.params.items()},
        "bse": {k: float(v) for k, v in model.bse.items()},
        "tvalues": {k: float(v) for k, v in model.tvalues.items()},
        "pvalues": {k: float(v) for k, v in model.pvalues.items()},
        "ci_lower": {k: float(v) for k, v in model.conf_int()[0].items()},
        "ci_upper": {k: float(v) for k, v in model.conf_int()[1].items()},
    }


def to_one_row(payload):
    rows = []
    for term, beta in payload["params"].items():
        rows.append({
            "term": term,
            "beta": beta,
            "se": payload["bse"][term],
            "t": payload["tvalues"][term],
            "p": payload["pvalues"][term],
            "ci_lo": payload["ci_lower"][term],
            "ci_hi": payload["ci_upper"][term],
        })
    out = pd.DataFrame(rows)
    out["n"] = payload["n"]
    out["adj_rsq"] = payload["rsquared_adj"]
    return out


def main():
    print("=" * 72)
    print("R3 Phase 0 — Canonical M8 from raw WBES Singapore 2023")
    print("=" * 72)

    df = build_analysis_frame()
    print(f"\nRaw firms loaded: {len(df)}")
    print(f"FSTS mean (centering offset): {df.attrs['fsts_mean']:.4f}")

    m8, formula, n = fit_m8(df)
    print(f"M8 sample: N = {n} (target: 617)")

    payload = serialize(m8, formula, n, "M8_canonical")

    (OUT_DIR / "m8_canonical.json").write_text(json.dumps(payload, indent=2))
    to_one_row(payload).to_csv(OUT_DIR / "m8_canonical.csv", index=False)
    (OUT_DIR / "m8_canonical.txt").write_text(str(m8.summary()))
    print(f"\nWrote: {OUT_DIR / 'm8_canonical.json'}")
    print(f"Wrote: {OUT_DIR / 'm8_canonical.csv'}")
    print(f"Wrote: {OUT_DIR / 'm8_canonical.txt'}")

    print("\nKey coefficients (the 4 numbers reviewer flagged in D1):")
    print(f"{'Term':<22}{'beta':>10}{'SE':>9}{'p':>9}")
    print("-" * 50)
    for term in ["TCI", "DAI", "fsts_c", "fsts_c2",
                 "fsts_c_DAI", "fsts_c2_DAI",
                 "ln_empl", "firm_age", "foreign"]:
        if term in payload["params"]:
            b = payload["params"][term]
            s = payload["bse"][term]
            p = payload["pvalues"][term]
            print(f"{term:<22}{b:>10.4f}{s:>9.4f}{p:>9.4f}")

    print(f"\nN = {payload['n']}, R² = {payload['rsquared']:.4f}, "
          f"Adj R² = {payload['rsquared_adj']:.4f}")

    # Reviewer-flagged comparison
    print("\n" + "=" * 72)
    print("D1 reconciliation against Manuscript Table 2 / Table 3 baseline")
    print("=" * 72)
    tci = payload["params"]["TCI"]
    fsts2_dai = payload["params"]["fsts_c2_DAI"]
    adj = payload["rsquared_adj"]
    print(f"  Source                            TCI   FSTS²×DAI  Adj R²")
    print(f"  Canonical (this run, N={payload['n']})   {tci:>6.3f}   {fsts2_dai:>7.3f}   {adj:>6.3f}")
    print(f"  Manuscript Table 2 M8             0.153    3.119   0.196")
    print(f"  Manuscript Table 3 baseline       0.187    2.972   0.192")
    print()
    print("If 'Canonical' matches Table 2 M8 → Table 3 baseline row is the")
    print("mismatch and must be corrected (or its note clarified). If")
    print("'Canonical' matches neither, deeper diagnosis required (see")
    print("01_diagnose_table3_baseline.py).")


if __name__ == "__main__":
    main()
