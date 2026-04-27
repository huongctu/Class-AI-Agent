"""
analyze-ip-regression.py
=========================
Reproducible analysis pipeline for the I-P relationship across 6 country-waves.

Inputs:  data/analysis/pooled_wbes_6waves.csv (built by build-pooled-dataset.py)
Outputs:
    data/analysis/results-p3-singapore.csv
    data/analysis/results-p4-vietnam.csv
    data/analysis/results-p5-china.csv
    data/analysis/results-grand-comparison.csv

Specifications (verified from session):
    Controls:    ln_empl, firm_age, foreign_dummy
                 (manager_exp DROPPED - VIF inflated to 5.85-6.11 with ln_empl)
    Robust SE:   HC1
    FSTS scale:  0-1 proportion (NOT 0-100 percentage)
    TCI_thin:    mean(foreign_tech, quality_cert)         - for P4 cross-wave (VNM 2009 lacks h1/h8)
    TCI_full:    mean(foreign_tech, product_innov, rd_spending, quality_cert)  - for P3, P5
    DAI_thin:    mean(website, foreign_tech)              - cross-wave consistent
    DAI_rich:    mean(website, epayment_pct/100, epay_supp_pct/100)  - B-READY only
    Sample:      Listwise deletion within each model; no winsorization

Author: Do Thuy Huong
"""
from __future__ import annotations
from pathlib import Path
from typing import Optional, List, Dict

import numpy as np
import pandas as pd
import statsmodels.api as sm

# =====================================================================
# CONFIG
# =====================================================================
INPUT_CSV = Path("data/analysis/pooled_wbes_6waves.csv")
OUT_DIR = Path("data/analysis")
OUT_DIR.mkdir(parents=True, exist_ok=True)

CONTROLS = ["ln_empl", "firm_age", "foreign_dummy"]
ROBUST_SE = "HC1"

np.random.seed(20260427)


# =====================================================================
# COMPOSITE CONSTRUCTION
# =====================================================================
def build_tci_thin(df: pd.DataFrame) -> pd.Series:
    """TCI thin: mean of foreign_tech + quality_cert (cross-wave incl. VNM 2009)."""
    items = df[["foreign_tech", "quality_cert"]]
    n_valid = items.notna().sum(axis=1)
    return items.mean(axis=1).where(n_valid >= 1)


def build_tci_full(df: pd.DataFrame) -> pd.Series:
    """TCI full: mean of all 4 Lall items (requires h1, h8 - not for VNM 2009)."""
    items = df[["foreign_tech", "product_innov", "rd_spending", "quality_cert"]]
    n_valid = items.notna().sum(axis=1)
    return items.mean(axis=1).where(n_valid >= 3)  # require >=3 of 4 items


def build_dai_thin(df: pd.DataFrame) -> pd.Series:
    """DAI thin: mean of website + foreign_tech (cross-wave consistent)."""
    items = df[["website", "foreign_tech"]]
    n_valid = items.notna().sum(axis=1)
    return items.mean(axis=1).where(n_valid >= 1)


def build_dai_rich(df: pd.DataFrame) -> pd.Series:
    """DAI rich: mean of website + epayment_pct/100 + epay_supp_pct/100 (B-READY only)."""
    df_temp = pd.DataFrame({
        "website": df["website"],
        "epay_norm": df["epayment_pct"] / 100.0,
        "epay_supp_norm": df["epay_supp_pct"] / 100.0,
    })
    n_valid = df_temp.notna().sum(axis=1)
    return df_temp.mean(axis=1).where(n_valid >= 2)


def standardize(s: pd.Series) -> pd.Series:
    """Z-standardize a series within its non-NA values."""
    valid = s.dropna()
    if len(valid) == 0 or valid.std() == 0:
        return s * np.nan
    return (s - valid.mean()) / valid.std()


# =====================================================================
# REGRESSION HELPERS
# =====================================================================
def fit_ols(y: pd.Series, X: pd.DataFrame):
    """OLS with HC1 robust SE; auto-add constant; cast to float."""
    Xc = sm.add_constant(X.astype(float))
    return sm.OLS(y.astype(float), Xc, missing="drop").fit(cov_type=ROBUST_SE)


def extract_results(model, model_name: str, sample_label: str) -> pd.DataFrame:
    """Tidy regression output for CSV writing."""
    rows = []
    for var in model.params.index:
        rows.append({
            "sample": sample_label,
            "model": model_name,
            "variable": var,
            "coef": model.params[var],
            "se": model.bse[var],
            "t": model.tvalues[var],
            "p_value": model.pvalues[var],
            "ci_lo_95": model.conf_int().loc[var, 0],
            "ci_hi_95": model.conf_int().loc[var, 1],
        })
    rows.append({
        "sample": sample_label, "model": model_name, "variable": "_FIT_",
        "coef": np.nan, "se": np.nan, "t": np.nan, "p_value": np.nan,
        "ci_lo_95": np.nan, "ci_hi_95": np.nan,
    })
    df = pd.DataFrame(rows)
    df["n_obs"] = int(model.nobs)
    df["r_squared"] = float(model.rsquared)
    df["adj_r_squared"] = float(model.rsquared_adj)
    df["aic"] = float(model.aic)
    df["bic"] = float(model.bic)
    return df


def lind_mehlum_test(model, fsts_var: str = "fsts", fsts_sq_var: str = "fsts_sq",
                      x_min: float = 0.0, x_max: float = 1.0) -> dict:
    """
    Lind-Mehlum (2010) U-test for inverted-U.
    Returns slopes at x_min and x_max, with one-sided p-values and joint p.
    """
    if fsts_var not in model.params.index or fsts_sq_var not in model.params.index:
        return {"p_lm": np.nan, "slope_lo": np.nan, "slope_hi": np.nan,
                "p_lo_one": np.nan, "p_hi_one": np.nan, "tp": np.nan}

    b1 = model.params[fsts_var]
    b2 = model.params[fsts_sq_var]
    cov = model.cov_params()
    var_b1 = cov.loc[fsts_var, fsts_var]
    var_b2 = cov.loc[fsts_sq_var, fsts_sq_var]
    cov_b12 = cov.loc[fsts_var, fsts_sq_var]

    slope_lo = b1 + 2 * b2 * x_min
    slope_hi = b1 + 2 * b2 * x_max
    var_slope_lo = var_b1 + 4 * x_min ** 2 * var_b2 + 4 * x_min * cov_b12
    var_slope_hi = var_b1 + 4 * x_max ** 2 * var_b2 + 4 * x_max * cov_b12

    from scipy import stats as scipy_stats
    se_lo = np.sqrt(max(var_slope_lo, 0))
    se_hi = np.sqrt(max(var_slope_hi, 0))
    t_lo = slope_lo / se_lo if se_lo > 0 else np.nan
    t_hi = slope_hi / se_hi if se_hi > 0 else np.nan

    # Inverted-U: slope_lo > 0 (positive at low end), slope_hi < 0 (negative at high end)
    p_lo_one = 1 - scipy_stats.norm.cdf(t_lo)  # slope_lo > 0
    p_hi_one = scipy_stats.norm.cdf(t_hi)      # slope_hi < 0
    p_lm = max(p_lo_one, p_hi_one)

    tp = -b1 / (2 * b2) if abs(b2) > 1e-12 else np.nan

    return {
        "p_lm": float(p_lm),
        "slope_lo": float(slope_lo),
        "slope_hi": float(slope_hi),
        "p_lo_one": float(p_lo_one),
        "p_hi_one": float(p_hi_one),
        "tp": float(tp),
    }


def cohen_f2(model_full, model_reduced) -> float:
    """Cohen's f2 = (R2_full - R2_reduced) / (1 - R2_full)."""
    r2_f, r2_r = model_full.rsquared, model_reduced.rsquared
    if r2_f >= 1.0:
        return np.nan
    return (r2_f - r2_r) / (1.0 - r2_f)


def paternoster_z(b1: float, se1: float, b2: float, se2: float) -> dict:
    """
    Paternoster, Brame, Mazerolle and Piquero (1998) z-test
    for difference in regression coefficients across independent samples.
        z = (b1 - b2) / sqrt(se1^2 + se2^2)
    """
    if any(pd.isna([b1, se1, b2, se2])):
        return {"z": np.nan, "p_two_sided": np.nan, "diff": np.nan}
    diff = b1 - b2
    se_diff = np.sqrt(se1 ** 2 + se2 ** 2)
    z = diff / se_diff if se_diff > 0 else np.nan
    from scipy import stats as scipy_stats
    p = 2 * (1 - scipy_stats.norm.cdf(abs(z))) if not np.isnan(z) else np.nan
    return {"z": float(z), "p_two_sided": float(p), "diff": float(diff)}


# =====================================================================
# MODEL SUITE - applied to each (sub)sample
# =====================================================================
def run_model_suite(df: pd.DataFrame, label: str, tci_var: str = "tci_full",
                     dai_var: str = "dai_thin", wave_dummies: List[str] = None,
                     verbose: bool = True) -> Dict:
    """Run M0 -> M8 specifications for one (sub)sample."""
    df = df.copy()

    # standardize TCI and DAI within sample
    df[f"{tci_var}_z"] = standardize(df[tci_var])
    df[f"{dai_var}_z"] = standardize(df[dai_var])

    # interaction terms
    df[f"fsts_x_{tci_var}"] = df["fsts"] * df[f"{tci_var}_z"]
    df[f"fsts_sq_x_{tci_var}"] = df["fsts_sq"] * df[f"{tci_var}_z"]
    df[f"fsts_x_{dai_var}"] = df["fsts"] * df[f"{dai_var}_z"]
    df[f"fsts_sq_x_{dai_var}"] = df["fsts_sq"] * df[f"{dai_var}_z"]

    wave_dummies = wave_dummies or []
    models: Dict = {}
    y = df["ln_lp"]

    # M0: controls only
    X = df[CONTROLS + wave_dummies]
    models["M0_controls"] = fit_ols(y, X)

    # M1: + FSTS linear
    X = df[["fsts"] + CONTROLS + wave_dummies]
    models["M1_linear"] = fit_ols(y, X)

    # M2: + FSTS^2 (inverted-U baseline)
    X = df[["fsts", "fsts_sq"] + CONTROLS + wave_dummies]
    models["M2_invU"] = fit_ols(y, X)

    # M3: + TCI direct + moderation
    X = df[["fsts", "fsts_sq", f"{tci_var}_z",
            f"fsts_x_{tci_var}", f"fsts_sq_x_{tci_var}"] + CONTROLS + wave_dummies]
    models["M3_TCI"] = fit_ols(y, X)

    # M4: + DAI direct + moderation
    X = df[["fsts", "fsts_sq", f"{dai_var}_z",
            f"fsts_x_{dai_var}", f"fsts_sq_x_{dai_var}"] + CONTROLS + wave_dummies]
    models["M4_DAI"] = fit_ols(y, X)

    # M5: TCI direct only
    X = df[["fsts", "fsts_sq", f"{tci_var}_z"] + CONTROLS + wave_dummies]
    models["M5_TCI_direct"] = fit_ols(y, X)

    # M6: DAI direct only
    X = df[["fsts", "fsts_sq", f"{dai_var}_z"] + CONTROLS + wave_dummies]
    models["M6_DAI_direct"] = fit_ols(y, X)

    # M7: TCI + DAI both direct (no moderation)
    X = df[["fsts", "fsts_sq", f"{tci_var}_z", f"{dai_var}_z"] + CONTROLS + wave_dummies]
    models["M7_both_direct"] = fit_ols(y, X)

    # M8: FULL - TCI + DAI direct + DAI moderation
    X = df[["fsts", "fsts_sq",
            f"{tci_var}_z",
            f"{dai_var}_z", f"fsts_x_{dai_var}", f"fsts_sq_x_{dai_var}"] + CONTROLS + wave_dummies]
    models["M8_full"] = fit_ols(y, X)

    if verbose:
        print(f"\n--- {label} ---")
        m2 = models["M2_invU"]
        lm = lind_mehlum_test(m2)
        print(f"  M2 inverted-U: TP = {lm['tp']*100:.1f}%, LM p = {lm['p_lm']:.3f}")
        m3 = models["M3_TCI"]
        if f"{tci_var}_z" in m3.params.index:
            print(f"  M3 TCI direct: beta = {m3.params[f'{tci_var}_z']:+.3f} "
                  f"(p = {m3.pvalues[f'{tci_var}_z']:.3f})")
        m6 = models["M6_DAI_direct"]
        if f"{dai_var}_z" in m6.params.index:
            print(f"  M6 DAI direct: beta = {m6.params[f'{dai_var}_z']:+.3f} "
                  f"(p = {m6.pvalues[f'{dai_var}_z']:.3f})")
        m4 = models["M4_DAI"]
        if f"fsts_x_{dai_var}" in m4.params.index:
            print(f"  M4 DAI mod FSTSxDAI: beta = {m4.params[f'fsts_x_{dai_var}']:+.3f} "
                  f"(p = {m4.pvalues[f'fsts_x_{dai_var}']:.3f})")
        if f"fsts_sq_x_{dai_var}" in m4.params.index:
            print(f"        DAI mod FSTS^2xDAI: beta = {m4.params[f'fsts_sq_x_{dai_var}']:+.3f} "
                  f"(p = {m4.pvalues[f'fsts_sq_x_{dai_var}']:.3f})")

    return models


# =====================================================================
# PER-PAPER ANALYSIS PIPELINES
# =====================================================================
def analyze_p3_singapore(df: pd.DataFrame) -> pd.DataFrame:
    """P3: Singapore 2023 - TCI_full, DAI_rich primary, DAI_thin robustness."""
    print("\n" + "=" * 70)
    print("P3 SINGAPORE 2023")
    print("=" * 70)
    sgp = df[(df["country"] == "SGP") & (df["year"] == 2023)].copy()
    sgp["tci_full"] = build_tci_full(sgp)
    sgp["tci_thin"] = build_tci_thin(sgp)
    sgp["dai_thin"] = build_dai_thin(sgp)
    sgp["dai_rich"] = build_dai_rich(sgp)

    all_results = []

    models_rich = run_model_suite(sgp, "Singapore 2023 / TCI_full + DAI_rich",
                                    tci_var="tci_full", dai_var="dai_rich")
    for mn, mod in models_rich.items():
        all_results.append(extract_results(mod, mn, "SGP_2023_DAIrich"))

    models_thin = run_model_suite(sgp, "Singapore 2023 / TCI_full + DAI_thin (robustness)",
                                    tci_var="tci_full", dai_var="dai_thin")
    for mn, mod in models_thin.items():
        all_results.append(extract_results(mod, mn, "SGP_2023_DAIthin"))

    return pd.concat(all_results, ignore_index=True)


def analyze_p4_vietnam(df: pd.DataFrame) -> pd.DataFrame:
    """P4: Vietnam 2009/2015/2023 - TCI_thin (cross-wave) + DAI_thin (cross-wave)."""
    print("\n" + "=" * 70)
    print("P4 VIETNAM 2009 / 2015 / 2023")
    print("=" * 70)
    vnm = df[df["country"] == "VNM"].copy()
    if len(vnm) == 0:
        return pd.DataFrame()
    vnm["tci_thin"] = build_tci_thin(vnm)
    vnm["tci_full"] = build_tci_full(vnm)
    vnm["dai_thin"] = build_dai_thin(vnm)
    vnm["dai_rich"] = build_dai_rich(vnm)

    all_results = []

    for yr in [2009, 2015, 2023]:
        sub = vnm[vnm["year"] == yr].copy()
        if len(sub) == 0:
            continue
        models = run_model_suite(sub, f"Vietnam {yr} / TCI_thin + DAI_thin",
                                  tci_var="tci_thin", dai_var="dai_thin")
        for mn, mod in models.items():
            all_results.append(extract_results(mod, mn, f"VNM_{yr}_thin"))

    if vnm["year"].nunique() >= 2:
        vnm_pooled = vnm.copy()
        vnm_pooled["wave_2015"] = (vnm_pooled["year"] == 2015).astype(int)
        vnm_pooled["wave_2023"] = (vnm_pooled["year"] == 2023).astype(int)
        models_pooled = run_model_suite(vnm_pooled, "Vietnam pooled 3 waves",
                                          tci_var="tci_thin", dai_var="dai_thin",
                                          wave_dummies=["wave_2015", "wave_2023"])
        for mn, mod in models_pooled.items():
            all_results.append(extract_results(mod, mn, "VNM_pooled"))

    if not all_results:
        return pd.DataFrame()
    return pd.concat(all_results, ignore_index=True)


def analyze_p5_china(df: pd.DataFrame) -> pd.DataFrame:
    """P5: China 2012/2024 - TCI_full + DAI_thin (cross-wave) + DAI_rich (2024)."""
    print("\n" + "=" * 70)
    print("P5 CHINA 2012 / 2024")
    print("=" * 70)
    chn = df[df["country"] == "CHN"].copy()
    if len(chn) == 0:
        return pd.DataFrame()
    chn["tci_full"] = build_tci_full(chn)
    chn["dai_thin"] = build_dai_thin(chn)
    chn["dai_rich"] = build_dai_rich(chn)

    all_results = []

    for yr in [2012, 2024]:
        sub = chn[chn["year"] == yr].copy()
        if len(sub) == 0:
            continue
        models_thin = run_model_suite(sub, f"China {yr} / TCI_full + DAI_thin",
                                        tci_var="tci_full", dai_var="dai_thin")
        for mn, mod in models_thin.items():
            all_results.append(extract_results(mod, mn, f"CHN_{yr}_thin"))

        if yr == 2024 and sub["dai_rich"].notna().sum() > 50:
            models_rich = run_model_suite(sub, f"China {yr} / TCI_full + DAI_rich",
                                            tci_var="tci_full", dai_var="dai_rich")
            for mn, mod in models_rich.items():
                all_results.append(extract_results(mod, mn, f"CHN_{yr}_rich"))

    if chn["year"].nunique() >= 2:
        chn_pooled = chn.copy()
        chn_pooled["wave_2024"] = (chn_pooled["year"] == 2024).astype(int)
        models_pooled = run_model_suite(chn_pooled, "China pooled 2 waves",
                                          tci_var="tci_full", dai_var="dai_thin",
                                          wave_dummies=["wave_2024"])
        for mn, mod in models_pooled.items():
            all_results.append(extract_results(mod, mn, "CHN_pooled"))

    if not all_results:
        return pd.DataFrame()
    return pd.concat(all_results, ignore_index=True)


# =====================================================================
# GRAND COMPARISON TABLE
# =====================================================================
def build_grand_comparison(df: pd.DataFrame) -> pd.DataFrame:
    """Cross-paper grand comparison: TP, LM p, TCI/DAI direct, TCI/DAI mod for each wave."""
    print("\n" + "=" * 70)
    print("GRAND COMPARISON TABLE (cross-paper)")
    print("=" * 70)

    rows = []
    waves = [
        ("SGP", 2023, "tci_full", "dai_rich"),
        ("CHN", 2012, "tci_full", "dai_thin"),
        ("CHN", 2024, "tci_full", "dai_thin"),
        ("VNM", 2009, "tci_thin", "dai_thin"),
        ("VNM", 2015, "tci_thin", "dai_thin"),
        ("VNM", 2023, "tci_thin", "dai_thin"),
    ]

    for country, year, tci_var, dai_var in waves:
        sub = df[(df["country"] == country) & (df["year"] == year)].copy()
        if len(sub) == 0:
            print(f"  [skip] {country} {year}: no data")
            continue
        sub["tci_thin"] = build_tci_thin(sub)
        sub["tci_full"] = build_tci_full(sub)
        sub["dai_thin"] = build_dai_thin(sub)
        sub["dai_rich"] = build_dai_rich(sub)

        models = run_model_suite(sub, f"{country} {year}",
                                  tci_var=tci_var, dai_var=dai_var, verbose=False)
        m2 = models["M2_invU"]
        m3 = models["M3_TCI"]
        m4 = models["M4_DAI"]
        m6 = models["M6_DAI_direct"]
        lm = lind_mehlum_test(m2)

        rows.append({
            "country_year": f"{country}_{year}",
            "n_analytic": int(m2.nobs),
            "tp_pct": lm["tp"] * 100 if not np.isnan(lm["tp"]) else np.nan,
            "lm_p": lm["p_lm"],
            "tci_var_used": tci_var,
            "tci_direct_beta": m3.params.get(f"{tci_var}_z", np.nan),
            "tci_direct_p": m3.pvalues.get(f"{tci_var}_z", np.nan),
            "tci_fsts_mod_beta": m3.params.get(f"fsts_x_{tci_var}", np.nan),
            "tci_fsts_mod_p": m3.pvalues.get(f"fsts_x_{tci_var}", np.nan),
            "tci_fsts_sq_mod_beta": m3.params.get(f"fsts_sq_x_{tci_var}", np.nan),
            "tci_fsts_sq_mod_p": m3.pvalues.get(f"fsts_sq_x_{tci_var}", np.nan),
            "dai_var_used": dai_var,
            "dai_direct_beta": m6.params.get(f"{dai_var}_z", np.nan),
            "dai_direct_p": m6.pvalues.get(f"{dai_var}_z", np.nan),
            "dai_fsts_mod_beta": m4.params.get(f"fsts_x_{dai_var}", np.nan),
            "dai_fsts_mod_p": m4.pvalues.get(f"fsts_x_{dai_var}", np.nan),
            "dai_fsts_sq_mod_beta": m4.params.get(f"fsts_sq_x_{dai_var}", np.nan),
            "dai_fsts_sq_mod_p": m4.pvalues.get(f"fsts_sq_x_{dai_var}", np.nan),
        })

    return pd.DataFrame(rows)


# =====================================================================
# MAIN
# =====================================================================
def main() -> None:
    if not INPUT_CSV.exists():
        print(f"[ERROR] Pooled dataset not found: {INPUT_CSV}")
        print("        Run scripts/build-pooled-dataset.py first.")
        return

    print(f"[INFO] Loading {INPUT_CSV}")
    df = pd.read_csv(INPUT_CSV)
    print(f"[INFO] Pooled N = {len(df)}")
    print(f"[INFO] Per-wave breakdown:\n{df.groupby(['country', 'year']).size()}")

    # P3
    p3_results = analyze_p3_singapore(df)
    p3_path = OUT_DIR / "results-p3-singapore.csv"
    p3_results.to_csv(p3_path, index=False)
    print(f"\n[INFO] Saved -> {p3_path}  ({len(p3_results)} rows)")

    # P4
    p4_results = analyze_p4_vietnam(df)
    p4_path = OUT_DIR / "results-p4-vietnam.csv"
    p4_results.to_csv(p4_path, index=False)
    print(f"[INFO] Saved -> {p4_path}  ({len(p4_results)} rows)")

    # P5
    p5_results = analyze_p5_china(df)
    p5_path = OUT_DIR / "results-p5-china.csv"
    p5_results.to_csv(p5_path, index=False)
    print(f"[INFO] Saved -> {p5_path}  ({len(p5_results)} rows)")

    # Grand comparison
    grand = build_grand_comparison(df)
    grand_path = OUT_DIR / "results-grand-comparison.csv"
    grand.to_csv(grand_path, index=False)
    print(f"[INFO] Saved -> {grand_path}")
    print("\n=== GRAND COMPARISON ===")
    print(grand.to_string(index=False))


if __name__ == "__main__":
    main()
