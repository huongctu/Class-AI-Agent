"""
P7_capstone_47countries_analysis.py
=====================================
P7 capstone: M0-M7 regression suite across available WBES economies.

Data accepted (auto-detected):
  (A) /tmp/wbes/pool.csv          — full 47-country pool from wbes/02_harmonize.py
  (B) data/analysis/pooled_wbes_6waves.csv — existing 6-wave pool (SGP/VNM/CHN)

Column mapping from pooled_wbes_6waves.csv:
  ln_labor_prod  → lnLP (log labor productivity)
  export_pct     → FSTS × 100  (rescale to [0,1])
  quality_cert   → b8 (ISO cert)
  foreign_tech   → e6/h7 (foreign-licensed tech)
  website        → c22b (DAI primary)
  ln_empl        → log_emp
  firm_age       → firm_age
  foreign_own    → fdi proxy (≥10% → fdi10 dummy)
  TCI_thin/full  → pre-built TCI composites
  DAI_thin/rich  → pre-built DAI composites

Spec (thesis §3.3-§3.4):
  FSTS_c  = FSTS - wave_mean_FSTS   (mean-centred within country×year)
  lnLP    winsorised 1%/99% within country×year
  TCI_z   = z-std(TCI_thin) within wave  [primary, cross-wave]
  DAI_z   = z-std(DAI_thin) within wave  [primary, cross-wave]
  Controls: log_emp, firm_age, fdi10
  FEs:      country dummies, year dummies, sector dummies (if available)
  SE:       HC1 robust

Models M0-M7 (thesis Table 3.2):
  M0  controls + FE
  M1  M0 + FSTS_c
  M2  M1 + FSTS_c^2
  M3  M2 + FSTS_c^3           (H1 cubic S-curve)
  M4  M3 + TCI_z + FSTS×TCI  (H2 TCI moderation)
  M5  M3 + DAI_z + FSTS×DAI  (H3 DAI moderation)
  M6  M3 + TCI_z + DAI_z     (joint direct, no moderation)
  M7  M3 + TCI mod + DAI mod  (FULL)

Outputs: data/analysis/p7/
  p7_descriptives.csv
  p7_m0m7_full.csv
  p7_m0m7_by_country.csv
  p7_m0m7_by_period.csv
  p7_lm_tests.csv
  p7_paternoster.csv
  p7_grand_table.csv

Author : Đỗ Thùy Hương | PGS.TS. Phan Anh Tú
"""
from __future__ import annotations
import warnings
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats as scipy_stats

warnings.filterwarnings("ignore")
np.random.seed(20260427)

# ==============================================================
# PATHS
# ==============================================================
POOL_47  = Path("/tmp/wbes/pool.csv")
POOL_6W  = Path("data/analysis/pooled_wbes_6waves.csv")
OUT_DIR  = Path("data/analysis/p7")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ==============================================================
# ICRV REGIME MAPPING  (thesis §3.3.6)
# ==============================================================
ICRV = {
    # Regime 1 — Advanced innovation-driven
    "SGP": "R1_Adv_Innovation", "HKG": "R1_Adv_Innovation",
    "KOR": "R1_Adv_Innovation", "TWN": "R1_Adv_Innovation",
    "ISR": "R1_Adv_Innovation", "CYP": "R1_Adv_Innovation",
    # Regime 1' — Advanced resource-driven
    "SAU": "R1p_Adv_Resource", "QAT": "R1p_Adv_Resource",
    "KWT": "R1p_Adv_Resource", "BHR": "R1p_Adv_Resource",
    "BRN": "R1p_Adv_Resource",
    # Regime 2 — Upper-middle
    "CHN": "R2_Upper_Middle", "MYS": "R2_Upper_Middle",
    "THA": "R2_Upper_Middle", "KAZ": "R2_Upper_Middle",
    "ARM": "R2_Upper_Middle", "GEO": "R2_Upper_Middle",
    # Regime 3 — Emerging
    "IND": "R3_Emerging", "IDN": "R3_Emerging", "PHL": "R3_Emerging",
    "VNM": "R3_Emerging", "LKA": "R3_Emerging", "JOR": "R3_Emerging",
    "MNG": "R3_Emerging",
    # Regime 4 — Frontier
    "BGD": "R4_Frontier", "PAK": "R4_Frontier", "LAO": "R4_Frontier",
    "KHM": "R4_Frontier", "MMR": "R4_Frontier", "NPL": "R4_Frontier",
    "BTN": "R4_Frontier", "MDV": "R4_Frontier", "UZB": "R4_Frontier",
    "TJK": "R4_Frontier", "KGZ": "R4_Frontier", "TKM": "R4_Frontier",
    "AFG": "R4_Frontier", "TLS": "R4_Frontier", "IRQ": "R4_Frontier",
    "LBN": "R4_Frontier", "YEM": "R4_Frontier",
    # Regime 5 — SIDS Pacific
    "FJI": "R5_SIDS", "PNG": "R5_SIDS", "SLB": "R5_SIDS",
    "TON": "R5_SIDS", "VUT": "R5_SIDS", "WSM": "R5_SIDS",
}

REGIME_ORDER = [
    "R1_Adv_Innovation", "R1p_Adv_Resource",
    "R2_Upper_Middle", "R3_Emerging",
    "R4_Frontier", "R5_SIDS",
]


def assign_period(year: int) -> str:
    if year <= 2013:
        return "P1_2009_2013"
    elif year <= 2018:
        return "P2_2014_2018"
    else:
        return "P3_2019_2025"


# ==============================================================
# DATA LOADING
# ==============================================================
def load_data() -> pd.DataFrame:
    if POOL_47.exists():
        print(f"[INFO] Loading full pool: {POOL_47}")
        df = pd.read_csv(POOL_47)
        return _norm_pool47(df)
    if POOL_6W.exists():
        print(f"[INFO] Loading 6-wave pool: {POOL_6W}")
        df = pd.read_csv(POOL_6W)
        return _norm_6wave(df)
    raise FileNotFoundError(f"No data found at {POOL_47} or {POOL_6W}")


def _norm_pool47(df: pd.DataFrame) -> pd.DataFrame:
    rn = {
        "country_iso3": "country", "year_survey": "year",
        "log_labor_prod": "lnlp_raw", "log_employees": "log_emp",
        "ln_labor_prod": "lnlp_raw", "ln_empl": "log_emp",
        "fsts_pct": "fsts_pct", "export_pct": "fsts_pct",
        "rd_active": "h8",
        "iso_cert": "quality_cert", "website": "website",
        "sector_code": "sector",
    }
    df = df.rename(columns={k: v for k, v in rn.items() if k in df.columns})
    df["fsts"] = pd.to_numeric(df["fsts_pct"], errors="coerce").clip(0, 100) / 100.0
    for col in ["e6", "h7", "foreign_tech"]:
        if col in df.columns:
            df["foreign_tech"] = df[col]
            break
    if "fdi10" not in df.columns:
        # try b2b (raw WBES) then foreign_own (pre-harmonised)
        fo_raw = pd.to_numeric(
            df.get("b2b", df.get("foreign_own", pd.Series(dtype=float))),
            errors="coerce",
        )
        df["fdi10"] = (fo_raw >= 10).astype(float).where(fo_raw.notna())
    # Build TCI_thin and DAI_thin if not present
    if "TCI_thin" not in df.columns:
        items = df[["quality_cert", "foreign_tech"]].apply(pd.to_numeric, errors="coerce")
        df["TCI_thin"] = items.mean(axis=1, skipna=True).where(items.notna().sum(axis=1) >= 1)
    if "DAI_thin" not in df.columns:
        df["DAI_thin"] = pd.to_numeric(df.get("website", pd.Series(dtype=float)), errors="coerce")
    return df


def _norm_6wave(df: pd.DataFrame) -> pd.DataFrame:
    """Map pooled_wbes_6waves.csv columns to internal names."""
    rn = {
        "ln_labor_prod": "lnlp_raw",
        "ln_empl":       "log_emp",
        "export_pct":    "fsts_pct",  # 0-100 scale
    }
    df = df.rename(columns={k: v for k, v in rn.items() if k in df.columns})
    # FSTS: rescale 0-100 → 0-1
    df["fsts"] = pd.to_numeric(df["fsts_pct"], errors="coerce").clip(0, 100) / 100.0
    # FDI dummy: foreign_own ≥ 10%
    if "fdi10" not in df.columns and "foreign_own" in df.columns:
        fo = pd.to_numeric(df["foreign_own"], errors="coerce")
        df["fdi10"] = (fo >= 10).astype(float).where(fo.notna())
    return df


# ==============================================================
# FEATURE ENGINEERING
# ==============================================================
def winsorize_group(s: pd.Series, lo=0.01, hi=0.99) -> pd.Series:
    valid = s.dropna()
    if len(valid) < 20:
        return s
    p_lo, p_hi = valid.quantile([lo, hi])
    return s.clip(p_lo, p_hi)


def z_std(s: pd.Series) -> pd.Series:
    valid = s.dropna()
    if len(valid) < 5 or valid.std() == 0:
        return pd.Series(np.nan, index=s.index)
    return (s - valid.mean()) / valid.std()


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Cast numeric
    for col in ["lnlp_raw", "fsts", "log_emp", "firm_age", "fdi10",
                "quality_cert", "foreign_tech", "website",
                "TCI_thin", "TCI_full", "DAI_thin", "DAI_rich"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # lnLP: winsorise within wave
    df["lnlp"] = (
        df.groupby(["country", "year"])["lnlp_raw"]
          .transform(lambda s: winsorize_group(s, 0.01, 0.99))
    )

    # FSTS: mean-centre within wave
    wave_mean = df.groupby(["country", "year"])["fsts"].transform("mean")
    df["fsts_c"]  = df["fsts"] - wave_mean
    df["fsts_c2"] = df["fsts_c"] ** 2
    df["fsts_c3"] = df["fsts_c"] ** 3

    # TCI_z: z-std(TCI_thin) within wave
    if "TCI_thin" in df.columns:
        df["tci_z"] = df.groupby(["country", "year"])["TCI_thin"].transform(z_std)
    else:
        items = df[["quality_cert", "foreign_tech"]].apply(pd.to_numeric, errors="coerce")
        tci_raw = items.mean(axis=1, skipna=True).where(items.notna().sum(axis=1) >= 1)
        df["tci_z"] = df.groupby(["country", "year"])[tci_raw.name if hasattr(tci_raw, "name") else "quality_cert"].transform(z_std)
        df["_tci_raw"] = tci_raw
        df["tci_z"] = df.groupby(["country", "year"])["_tci_raw"].transform(z_std)

    # TCI_full_z (robustness)
    if "TCI_full" in df.columns:
        df["tci_full_z"] = df.groupby(["country", "year"])["TCI_full"].transform(z_std)

    # DAI_z: z-std(DAI_thin) within wave
    if "DAI_thin" in df.columns:
        df["dai_z"] = df.groupby(["country", "year"])["DAI_thin"].transform(z_std)
    elif "website" in df.columns:
        df["dai_z"] = df.groupby(["country", "year"])["website"].transform(z_std)
    else:
        df["dai_z"] = np.nan

    # DAI_rich_z (robustness, 2023+ only)
    if "DAI_rich" in df.columns:
        df["dai_rich_z"] = df.groupby(["country", "year"])["DAI_rich"].transform(z_std)

    # ICRV regime
    df["icrv"] = df["country"].map(ICRV).fillna("R_Other")

    # Period
    df["period"] = df["year"].apply(assign_period)

    # firm_age guard
    if "firm_age" in df.columns:
        df["firm_age"] = df["firm_age"].clip(0, 200)

    # Interaction terms
    df["fsts_x_tci"]  = df["fsts_c"]  * df["tci_z"]
    df["fsts2_x_tci"] = df["fsts_c2"] * df["tci_z"]
    df["fsts_x_dai"]  = df["fsts_c"]  * df["dai_z"]
    df["fsts2_x_dai"] = df["fsts_c2"] * df["dai_z"]

    return df


def add_fe_dummies(
    df: pd.DataFrame,
    country: bool = True,
    year: bool = True,
    sector: bool = False,
) -> Tuple[pd.DataFrame, List[str]]:
    fe_cols: List[str] = []
    if country and df["country"].nunique() > 1:
        d = pd.get_dummies(df["country"], prefix="FE_c", drop_first=True, dtype=float)
        df = pd.concat([df, d], axis=1)
        fe_cols.extend(d.columns.tolist())
    if year and df["year"].nunique() > 1:
        d = pd.get_dummies(df["year"].astype(str), prefix="FE_y", drop_first=True, dtype=float)
        df = pd.concat([df, d], axis=1)
        fe_cols.extend(d.columns.tolist())
    if sector and "sector" in df.columns and df["sector"].nunique() > 1:
        s = df["sector"].fillna("Unknown").astype(str)
        d = pd.get_dummies(s, prefix="FE_s", drop_first=True, dtype=float)
        df = pd.concat([df, d], axis=1)
        fe_cols.extend(d.columns.tolist())
    return df, fe_cols


# ==============================================================
# REGRESSION ENGINE
# ==============================================================
CONTROLS = ["log_emp", "firm_age", "fdi10"]


def fit_ols(y: pd.Series, X: pd.DataFrame, cov_type: str = "HC1"):
    Xc = sm.add_constant(X.astype(float))
    return sm.OLS(y.astype(float), Xc, missing="drop").fit(cov_type=cov_type)


def extract_coefs(model, model_name: str, sample_lbl: str) -> pd.DataFrame:
    rows = []
    for var in model.params.index:
        if var.startswith(("FE_c", "FE_y", "FE_s")):
            continue
        p = model.pvalues[var]
        rows.append({
            "sample":  sample_lbl,
            "model":   model_name,
            "variable": var,
            "coef":    round(model.params[var], 4),
            "se":      round(model.bse[var], 4),
            "t":       round(model.tvalues[var], 3),
            "p":       round(p, 4),
            "stars":   "***" if p < 0.01 else "**" if p < 0.05 else "*" if p < 0.10 else "",
            "ci_lo":   round(model.conf_int().loc[var, 0], 4),
            "ci_hi":   round(model.conf_int().loc[var, 1], 4),
            "n":       int(model.nobs),
            "r2":      round(model.rsquared, 4),
            "adj_r2":  round(model.rsquared_adj, 4),
        })
    return pd.DataFrame(rows)


# ==============================================================
# STATISTICAL TESTS
# ==============================================================
def lm_cubic(model, b1="fsts_c", b2="fsts_c2", b3="fsts_c3") -> dict:
    """Lind-Mehlum extended: find TP1, TP2 from cubic; Wald p for β2=β3=0."""
    out = {"b1": np.nan, "b2": np.nan, "b3": np.nan,
           "tp1_pct": np.nan, "tp2_pct": np.nan,
           "disc": np.nan, "wald_p": np.nan}
    if not all(v in model.params.index for v in [b1, b2, b3]):
        return out
    _b1, _b2, _b3 = float(model.params[b1]), float(model.params[b2]), float(model.params[b3])
    out.update({"b1": round(_b1, 4), "b2": round(_b2, 4), "b3": round(_b3, 4)})
    disc = 4*_b2**2 - 12*_b3*_b1
    out["disc"] = round(disc, 6)
    if disc >= 0 and abs(_b3) > 1e-14:
        sq = np.sqrt(disc)
        out["tp1_pct"] = round((-2*_b2 - sq) / (6*_b3) * 100, 1)
        out["tp2_pct"] = round((-2*_b2 + sq) / (6*_b3) * 100, 1)
    try:
        idx = list(model.params.index)
        R = np.zeros((2, len(idx)))
        R[0, idx.index(b2)] = 1
        R[1, idx.index(b3)] = 1
        out["wald_p"] = round(float(model.f_test(R).pvalue), 4)
    except Exception:
        pass
    return out


def lm_quadratic(model, b1="fsts_c", b2="fsts_c2", x_min=0.0, x_max=1.0) -> dict:
    """Lind-Mehlum (2010) inverted-U test."""
    out = {"lm_p": np.nan, "tp_pct": np.nan}
    if b1 not in model.params.index or b2 not in model.params.index:
        return out
    _b1, _b2 = float(model.params[b1]), float(model.params[b2])
    cov = model.cov_params()
    v1, v2, c12 = float(cov.loc[b1, b1]), float(cov.loc[b2, b2]), float(cov.loc[b1, b2])
    sl_lo = _b1 + 2*_b2*x_min
    sl_hi = _b1 + 2*_b2*x_max
    se_lo = np.sqrt(max(v1 + 4*x_min**2*v2 + 4*x_min*c12, 0))
    se_hi = np.sqrt(max(v1 + 4*x_max**2*v2 + 4*x_max*c12, 0))
    t_lo = sl_lo / se_lo if se_lo > 0 else np.nan
    t_hi = sl_hi / se_hi if se_hi > 0 else np.nan
    p_lo = 1 - scipy_stats.norm.cdf(t_lo) if not np.isnan(t_lo) else np.nan
    p_hi = scipy_stats.norm.cdf(t_hi)     if not np.isnan(t_hi) else np.nan
    lm_p = max(p_lo, p_hi) if not any(np.isnan([p_lo, p_hi])) else np.nan
    tp = -_b1 / (2*_b2) if abs(_b2) > 1e-14 else np.nan
    out.update({"lm_p": round(lm_p, 4) if not np.isnan(lm_p) else np.nan,
                "tp_pct": round(tp*100, 1) if not np.isnan(tp) else np.nan})
    return out


def paternoster_z(b1, se1, b2, se2) -> dict:
    if any(pd.isna([b1, se1, b2, se2])):
        return {"z": np.nan, "p2": np.nan, "diff": np.nan}
    diff = b1 - b2
    se = np.sqrt(se1**2 + se2**2)
    z = diff / se if se > 0 else np.nan
    p = 2*(1 - scipy_stats.norm.cdf(abs(z))) if not np.isnan(z) else np.nan
    return {"z": round(z, 3), "p2": round(p, 4), "diff": round(diff, 4)}


# ==============================================================
# MODEL SUITE  M0-M7
# ==============================================================
def run_m0m7(
    df: pd.DataFrame, label: str, fe_cols: List[str], verbose: bool = True
) -> Dict:
    controls = [c for c in CONTROLS if c in df.columns]
    x_fe = [c for c in fe_cols if c in df.columns]
    y = df["lnlp"]

    def _X(*extra):
        cols = [c for c in extra if c in df.columns] + controls + x_fe
        return df[cols]

    n_tci = df["tci_z"].notna().sum() if "tci_z" in df.columns else 0
    n_dai = df["dai_z"].notna().sum() if "dai_z" in df.columns else 0
    MIN = 50

    models: Dict = {}
    models["M0_controls"]  = fit_ols(y, _X())
    models["M1_linear"]    = fit_ols(y, _X("fsts_c"))
    models["M2_quadratic"] = fit_ols(y, _X("fsts_c", "fsts_c2"))
    models["M3_cubic"]     = fit_ols(y, _X("fsts_c", "fsts_c2", "fsts_c3"))

    if n_tci >= MIN:
        models["M4_TCI"] = fit_ols(y, _X("fsts_c", "fsts_c2", "fsts_c3",
                                          "tci_z", "fsts_x_tci", "fsts2_x_tci"))
    if n_dai >= MIN:
        models["M5_DAI"] = fit_ols(y, _X("fsts_c", "fsts_c2", "fsts_c3",
                                          "dai_z", "fsts_x_dai", "fsts2_x_dai"))
    if n_tci >= MIN and n_dai >= MIN:
        models["M6_TCI_DAI"] = fit_ols(y, _X("fsts_c", "fsts_c2", "fsts_c3",
                                               "tci_z", "dai_z"))
        models["M7_full"] = fit_ols(y, _X("fsts_c", "fsts_c2", "fsts_c3",
                                           "tci_z", "fsts_x_tci", "fsts2_x_tci",
                                           "dai_z", "fsts_x_dai", "fsts2_x_dai"))
    if verbose:
        m3 = models.get("M3_cubic")
        if m3:
            lm = lm_cubic(m3)
            print(f"  [{label}] M3 n={int(m3.nobs):,}  "
                  f"β1={lm['b1']:+.3f} β2={lm['b2']:+.3f} β3={lm['b3']:+.3f}  "
                  f"TP1={lm['tp1_pct']}%  TP2={lm['tp2_pct']}%  Wald_p={lm['wald_p']}")
        for tag, mkey, vname in [
            ("M4 TCI", "M4_TCI", "tci_z"),
            ("M5 DAI", "M5_DAI", "dai_z"),
        ]:
            mod = models.get(mkey)
            if mod and vname in mod.params.index:
                print(f"  [{label}] {tag}: β={mod.params[vname]:+.3f} "
                      f"(p={mod.pvalues[vname]:.3f}){' ***' if mod.pvalues[vname]<0.01 else ' **' if mod.pvalues[vname]<0.05 else ' *' if mod.pvalues[vname]<0.10 else ''}")
    return models


# ==============================================================
# ANALYSIS PIPELINES
# ==============================================================
def analyze_full(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    print("\n" + "="*65)
    print(f"FULL POOL — {df['country'].nunique()} economies  n={len(df):,}  "
          f"years {df['year'].min()}–{df['year'].max()}")
    print("="*65)
    df_fe, fe_cols = add_fe_dummies(df)
    models = run_m0m7(df_fe, "Full", fe_cols, verbose=True)

    coef_rows, lm_rows = [], []
    for mn, mod in models.items():
        coef_rows.append(extract_coefs(mod, mn, "FULL"))
        lm = lm_cubic(mod)
        lm.update({"sample": "FULL", "model": mn, "n": int(mod.nobs)})
        lm_rows.append(lm)
        lm2 = lm_quadratic(mod)
        lm_rows[-1].update({"lm_p_quad": lm2["lm_p"], "tp_quad_pct": lm2["tp_pct"]})

    return pd.concat(coef_rows, ignore_index=True), pd.DataFrame(lm_rows)


def analyze_by_country(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Run M0-M7 per country (and pooled multi-wave where applicable)."""
    print("\n" + "="*65)
    print("BY COUNTRY / WAVE")
    print("="*65)
    coef_rows, lm_rows = [], []

    for country in sorted(df["country"].unique()):
        sub = df[df["country"] == country].copy()
        waves = sorted(sub["year"].unique())

        # Individual waves
        for yr in waves:
            sw = sub[sub["year"] == yr].copy()
            if len(sw) < 50:
                continue
            lbl = f"{country}_{yr}"
            print(f"\n  ---- {lbl}  (n={len(sw):,}) ----")
            sw_fe, fe_cols = add_fe_dummies(sw, country=False, year=False)
            models = run_m0m7(sw_fe, lbl, fe_cols, verbose=True)
            for mn, mod in models.items():
                coef_rows.append(extract_coefs(mod, mn, lbl))
                lm = lm_cubic(mod)
                lm.update({"sample": lbl, "model": mn, "n": int(mod.nobs)})
                lm_rows.append(lm)

        # Pooled across waves (if ≥2 waves)
        if len(waves) >= 2:
            lbl = f"{country}_pooled"
            print(f"\n  ---- {lbl}  (n={len(sub):,}) ----")
            sub_fe, fe_cols = add_fe_dummies(sub, country=False, year=True)
            models = run_m0m7(sub_fe, lbl, fe_cols, verbose=True)
            for mn, mod in models.items():
                coef_rows.append(extract_coefs(mod, mn, lbl))
                lm = lm_cubic(mod)
                lm.update({"sample": lbl, "model": mn, "n": int(mod.nobs)})
                lm_rows.append(lm)

    return (
        pd.concat(coef_rows, ignore_index=True) if coef_rows else pd.DataFrame(),
        pd.DataFrame(lm_rows),
    )


def analyze_by_period(df: pd.DataFrame) -> pd.DataFrame:
    print("\n" + "="*65)
    print("BY PERIOD")
    print("="*65)
    coef_rows = []
    for period in ["P1_2009_2013", "P2_2014_2018", "P3_2019_2025"]:
        sub = df[df["period"] == period].copy()
        if len(sub) < 50:
            print(f"  [SKIP] {period}: n={len(sub)}")
            continue
        print(f"\n  ---- {period}  (n={len(sub):,}) ----")
        sub_fe, fe_cols = add_fe_dummies(sub)
        models = run_m0m7(sub_fe, period, fe_cols, verbose=True)
        for mn, mod in models.items():
            coef_rows.append(extract_coefs(mod, mn, period))
    return pd.concat(coef_rows, ignore_index=True) if coef_rows else pd.DataFrame()


def build_grand_table(
    full_res: pd.DataFrame,
    country_res: pd.DataFrame,
    period_res: pd.DataFrame,
) -> pd.DataFrame:
    KEY_VARS   = ["fsts_c", "fsts_c2", "fsts_c3",
                  "tci_z", "fsts_x_tci", "fsts2_x_tci",
                  "dai_z", "fsts_x_dai", "fsts2_x_dai"]
    KEY_MODELS = ["M3_cubic", "M4_TCI", "M5_DAI", "M7_full"]

    rows = []
    for df_res in [full_res, country_res, period_res]:
        if df_res is None or len(df_res) == 0:
            continue
        for sample in df_res["sample"].unique():
            for model in KEY_MODELS:
                sub = df_res[(df_res["sample"] == sample) & (df_res["model"] == model)]
                if sub.empty:
                    continue
                n_obs = sub["n"].iloc[0]
                for var in KEY_VARS:
                    row = sub[sub["variable"] == var]
                    if row.empty:
                        continue
                    rows.append({
                        "sample": sample, "model": model, "variable": var,
                        "coef":  row["coef"].values[0],
                        "se":    row["se"].values[0],
                        "p":     row["p"].values[0],
                        "stars": row["stars"].values[0],
                        "n":     n_obs,
                    })
    return pd.DataFrame(rows)


def build_paternoster(country_res: pd.DataFrame) -> pd.DataFrame:
    """Cross-sample Paternoster z-tests for FSTS_c coefficient (M3)."""
    MODEL = "M3_cubic"
    VAR   = "fsts_c"
    samples = country_res["sample"].unique().tolist()
    rows = []
    for i, s1 in enumerate(samples):
        for s2 in samples[i+1:]:
            def _get(s):
                sub = country_res[
                    (country_res["sample"] == s) &
                    (country_res["model"] == MODEL) &
                    (country_res["variable"] == VAR)
                ]
                if sub.empty:
                    return np.nan, np.nan
                return sub["coef"].values[0], sub["se"].values[0]
            b1, se1 = _get(s1)
            b2, se2 = _get(s2)
            pz = paternoster_z(b1, se1, b2, se2)
            rows.append({"sample_a": s1, "sample_b": s2,
                         "coef_a": b1, "coef_b": b2, **pz})
    return pd.DataFrame(rows)


def build_descriptives(df: pd.DataFrame) -> pd.DataFrame:
    cols = ["lnlp", "fsts", "TCI_thin", "DAI_thin", "log_emp", "firm_age", "fdi10"]
    present = [c for c in cols if c in df.columns]
    rows = []
    for (country, year), sub in df.groupby(["country", "year"]):
        row = {"country": country, "year": int(year),
               "icrv": sub["icrv"].iloc[0], "n": len(sub)}
        for col in present:
            valid = sub[col].dropna()
            row[f"{col}_mean"]   = round(valid.mean(), 4) if len(valid) else np.nan
            row[f"{col}_sd"]     = round(valid.std(),  4) if len(valid) else np.nan
            row[f"{col}_median"] = round(valid.median(),4) if len(valid) else np.nan
        row["exporter_pct"] = round((sub["fsts"] > 0).mean() * 100, 1)
        rows.append(row)
    return pd.DataFrame(rows)


# ==============================================================
# MAIN
# ==============================================================
def main() -> None:
    print("[INFO] Loading data...")
    df_raw = load_data()
    print(f"[INFO] Raw rows : {len(df_raw):,}")
    print(f"[INFO] Countries: {sorted(df_raw['country'].unique())}")
    print(f"[INFO] Years    : {sorted(df_raw['year'].unique())}")

    print("\n[INFO] Building features...")
    df = build_features(df_raw)

    df = df.dropna(subset=["lnlp", "fsts_c"])
    print(f"[INFO] Analytic sample (lnlp + fsts_c): {len(df):,}")
    print(f"[INFO] ICRV:\n{df['icrv'].value_counts().to_string()}")
    print(f"[INFO] Period:\n{df['period'].value_counts().to_string()}")

    # ---- Descriptives ----
    desc = build_descriptives(df)
    desc.to_csv(OUT_DIR / "p7_descriptives.csv", index=False)
    print(f"\n[INFO] Descriptives -> {OUT_DIR}/p7_descriptives.csv")
    print(desc[["country", "year", "n", "lnlp_mean", "lnlp_sd",
                "fsts_mean", "exporter_pct"]].to_string(index=False))

    # ---- Full pool ----
    full_res, lm_full = analyze_full(df)
    full_res.to_csv(OUT_DIR / "p7_m0m7_full.csv", index=False)
    lm_full.to_csv(OUT_DIR / "p7_lm_full.csv", index=False)

    # ---- By country / wave ----
    country_res, lm_country = analyze_by_country(df)
    if len(country_res):
        country_res.to_csv(OUT_DIR / "p7_m0m7_by_country.csv", index=False)
        lm_country.to_csv(OUT_DIR / "p7_lm_by_country.csv", index=False)

    # ---- By period ----
    period_res = analyze_by_period(df)
    if len(period_res):
        period_res.to_csv(OUT_DIR / "p7_m0m7_by_period.csv", index=False)

    # ---- Grand table ----
    grand = build_grand_table(full_res, country_res, period_res)
    grand.to_csv(OUT_DIR / "p7_grand_table.csv", index=False)

    # ---- Paternoster ----
    if len(country_res):
        pat = build_paternoster(country_res)
        pat.to_csv(OUT_DIR / "p7_paternoster.csv", index=False)

    # ---- LM summary ----
    lm_all = pd.concat([lm_full, lm_country], ignore_index=True)
    lm_all.to_csv(OUT_DIR / "p7_lm_tests.csv", index=False)

    # ---- Print grand summary ----
    print("\n" + "="*65)
    print("GRAND TABLE: M3 cubic coefficients (FSTS_c, FSTS_c2, FSTS_c3)")
    print("="*65)
    if not grand.empty:
        m3 = grand[grand["model"] == "M3_cubic"][
            ["sample", "variable", "coef", "stars", "n"]
        ]
        for sample in m3["sample"].unique():
            sub = m3[m3["sample"] == sample]
            fsts_row  = sub[sub["variable"] == "fsts_c"]
            fsts2_row = sub[sub["variable"] == "fsts_c2"]
            fsts3_row = sub[sub["variable"] == "fsts_c3"]
            def _fmt(r):
                if r.empty: return "  n/a"
                return f"  {r['coef'].values[0]:+.3f}{r['stars'].values[0]}"
            n = sub["n"].values[0] if len(sub) else "?"
            print(f"  {sample:<25}  β1={_fmt(fsts_row)}  β2={_fmt(fsts2_row)}  β3={_fmt(fsts3_row)}  n={n:,}")

    print("\n" + "="*65)
    print("LIND-MEHLUM CUBIC (TP1 / TP2 / Wald p)  — M3")
    print("="*65)
    lm_m3 = lm_all[lm_all["model"] == "M3_cubic"][
        ["sample", "tp1_pct", "tp2_pct", "wald_p", "n"]
    ].dropna(subset=["wald_p"])
    print(lm_m3.to_string(index=False))

    print(f"\n[DONE] Outputs in {OUT_DIR}/")


if __name__ == "__main__":
    main()
