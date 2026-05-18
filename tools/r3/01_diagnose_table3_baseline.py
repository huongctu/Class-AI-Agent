"""
R3 Phase 0 — Diagnose D1 (Table 3 baseline row mismatch).

Reviewer flagged that Manuscript Table 3 baseline row reports:
    TCI = 0.187, FSTS² × DAI = 2.972, Adj R² = 0.192

while Manuscript Table 2 M8 (same N=617) reports:
    TCI = 0.153, FSTS² × DAI = 3.119, Adj R² = 0.196

Canonical M8 from raw .dta (00_canonical_m8.py) reproduces Table 2 M8
exactly. So Table 3 baseline must reflect a slightly different spec.

This script tests candidate specs that might explain the baseline row,
ranked by plausibility:

  C1. M8 with DAI_thin (drop k38 from DAI; only c22b + k33).
  C2. M8 with TCI_thin (drop one of b8/e6/h1/h8 from TCI).
  C3. M8 estimated on the smaller "core" sample (N=617 minus extra drops).
  C4. M8 with HC3 instead of HC1.
  C5. M8 with Newey-West (lag=0).
  C6. M8 without negative-code → NaN treatment for one continuous control.

Best-fit candidate is the one whose (TCI, FSTS²×DAI, Adj R²) triple is
closest to (0.187, 2.972, 0.192).
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

TARGET = {"TCI": 0.187, "fsts_c2_DAI": 2.972, "adj_rsq": 0.192}


def base_frame():
    """Replicate exact build from 00_canonical_m8.py."""
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
    df.loc[df["dai_drop"], ["k33_imp", "k38_imp", "c22b_yn"]] = np.nan

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


def make_composite(df: pd.DataFrame, parts: list[str], name: str) -> pd.DataFrame:
    df = df.copy()
    cols_z = []
    for c in parts:
        mu, sd = df[c].mean(), df[c].std()
        zcol = c + "_z_" + name
        df[zcol] = (df[c] - mu) / sd
        cols_z.append(zcol)
    raw = df[cols_z].sum(axis=1, skipna=False) / len(parts)
    df[name] = (raw - raw.mean()) / raw.std()
    return df


def fit_m8(df: pd.DataFrame, tci_col="TCI", dai_col="DAI",
           cov_type="HC1") -> dict:
    df = df.copy()
    df["TCI"] = df[tci_col]
    df["DAI"] = df[dai_col]
    df["fsts_c_DAI"] = df["fsts_c"] * df["DAI"]
    df["fsts_c2_DAI"] = df["fsts_c2"] * df["DAI"]
    core = ["ln_lp", "fsts_c", "fsts_c2", "TCI", "DAI",
            "fsts_c_DAI", "fsts_c2_DAI",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    mask = df[core].notna().all(axis=1)
    formula = (
        "ln_lp ~ fsts_c + fsts_c2 + TCI + DAI"
        " + fsts_c_DAI + fsts_c2_DAI"
        " + ln_empl + firm_age + foreign + C(broad_sector)"
    )
    m = smf.ols(formula, data=df[mask]).fit(cov_type=cov_type)
    return {
        "n": int(mask.sum()),
        "TCI": float(m.params.get("TCI", np.nan)),
        "DAI": float(m.params.get("DAI", np.nan)),
        "fsts_c": float(m.params.get("fsts_c", np.nan)),
        "fsts_c2": float(m.params.get("fsts_c2", np.nan)),
        "fsts_c_DAI": float(m.params.get("fsts_c_DAI", np.nan)),
        "fsts_c2_DAI": float(m.params.get("fsts_c2_DAI", np.nan)),
        "rsq": float(m.rsquared),
        "adj_rsq": float(m.rsquared_adj),
    }


def distance(result: dict) -> float:
    """L1 distance from target on the 3 reviewer-flagged numbers."""
    d = 0.0
    for k in ("TCI", "fsts_c2_DAI", "adj_rsq"):
        d += abs(result[k] - TARGET[k])
    return d


def main():
    print("=" * 75)
    print("R3 Phase 0 — D1 root-cause diagnosis")
    print(f"  Target (Table 3 baseline): TCI={TARGET['TCI']}, "
          f"FSTS²×DAI={TARGET['fsts_c2_DAI']}, Adj R²={TARGET['adj_rsq']}")
    print("=" * 75)

    df = base_frame()

    # Candidate specs
    specs = {}

    # Build TCI variants
    df = make_composite(df, ["b8_yn", "e6_yn", "h1_yn", "h8_yn"], "TCI_full")
    df = make_composite(df, ["b8_yn", "e6_yn", "h1_yn"], "TCI_thin_drop_h8")
    df = make_composite(df, ["b8_yn", "e6_yn", "h8_yn"], "TCI_thin_drop_h1")
    df = make_composite(df, ["b8_yn", "h1_yn", "h8_yn"], "TCI_thin_drop_e6")
    df = make_composite(df, ["e6_yn", "h1_yn", "h8_yn"], "TCI_thin_drop_b8")

    # Build DAI variants
    df = make_composite(df, ["c22b_yn", "k33_imp", "k38_imp"], "DAI_rich")
    df = make_composite(df, ["c22b_yn", "k33_imp"], "DAI_thin_drop_k38")
    df = make_composite(df, ["c22b_yn", "k38_imp"], "DAI_thin_drop_k33")
    df = make_composite(df, ["k33_imp", "k38_imp"], "DAI_thin_drop_c22b")

    # ---- Candidate set ----
    print("\nFitting candidate specs...")

    specs["C0_canonical (Table 2 M8)"] = fit_m8(df, "TCI_full", "DAI_rich")
    specs["C1a_DAI_thin_drop_k38"] = fit_m8(df, "TCI_full", "DAI_thin_drop_k38")
    specs["C1b_DAI_thin_drop_k33"] = fit_m8(df, "TCI_full", "DAI_thin_drop_k33")
    specs["C1c_DAI_thin_drop_c22b"] = fit_m8(df, "TCI_full", "DAI_thin_drop_c22b")
    specs["C2a_TCI_thin_drop_h8"] = fit_m8(df, "TCI_thin_drop_h8", "DAI_rich")
    specs["C2b_TCI_thin_drop_h1"] = fit_m8(df, "TCI_thin_drop_h1", "DAI_rich")
    specs["C2c_TCI_thin_drop_e6"] = fit_m8(df, "TCI_thin_drop_e6", "DAI_rich")
    specs["C2d_TCI_thin_drop_b8"] = fit_m8(df, "TCI_thin_drop_b8", "DAI_rich")
    specs["C4_HC3_SE"] = fit_m8(df, "TCI_full", "DAI_rich", cov_type="HC3")
    specs["C5_HC0_SE"] = fit_m8(df, "TCI_full", "DAI_rich", cov_type="HC0")

    # Print results table
    print(f"\n{'Candidate':<32}{'N':>5}{'TCI':>9}{'FSTS²×DAI':>12}{'AdjR²':>8}{'L1 dist':>10}")
    print("-" * 75)
    ranked = sorted(specs.items(), key=lambda kv: distance(kv[1]))
    for name, r in ranked:
        d = distance(r)
        print(f"{name:<32}{r['n']:>5}{r['TCI']:>9.4f}"
              f"{r['fsts_c2_DAI']:>12.4f}{r['adj_rsq']:>8.4f}{d:>10.4f}")

    print(f"\nTarget                          {'-':>5}"
          f"{TARGET['TCI']:>9.4f}{TARGET['fsts_c2_DAI']:>12.4f}"
          f"{TARGET['adj_rsq']:>8.4f}")

    # Best candidate
    best_name, best_result = ranked[0]
    best_dist = distance(best_result)
    print(f"\nBest match: {best_name} (L1 distance = {best_dist:.4f})")

    # Save full diagnosis
    out_path = OUT_DIR / "D1_diagnosis.json"
    out_path.write_text(json.dumps({
        "target": TARGET,
        "candidates": specs,
        "best": {"name": best_name, "result": best_result, "l1": best_dist},
    }, indent=2))
    print(f"\nWrote: {out_path}")

    # Verdict
    print("\n" + "=" * 75)
    if best_dist < 0.020:
        print(f"VERDICT: Table 3 baseline matches '{best_name}'.")
        print("  → Action: clarify the Table 3 note to specify this exact spec,")
        print("    OR re-run with the canonical M8 spec to make the row identical")
        print("    to Table 2 M8 (recommended for clarity).")
    elif best_dist < 0.050:
        print(f"VERDICT: '{best_name}' is the closest match but not exact.")
        print("  → Action: replace Table 3 baseline row with canonical M8 numbers")
        print("    (TCI=0.153, FSTS²×DAI=3.119, Adj R²=0.196). The reported")
        print("    values likely reflect a stale or hand-edited cell.")
    else:
        print("VERDICT: No candidate spec reproduces the Table 3 baseline numbers.")
        print("  → Action: the baseline row is most likely a transcription error.")
        print("    Replace with canonical M8 numbers (TCI=0.153, FSTS²×DAI=3.119,")
        print("    Adj R²=0.196) so all robustness specs in Table 3 reference the")
        print("    same baseline as Table 2 M8.")
    print("=" * 75)


if __name__ == "__main__":
    main()
