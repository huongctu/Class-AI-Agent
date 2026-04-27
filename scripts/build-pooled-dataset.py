"""
build-pooled-dataset.py
========================
Build pooled WBES dataset for I-P analysis across 6 country-waves.

Input: Raw .dta files for SGP 2023, VNM 2009/2015/2023, CHN 2012/2024
Output: data/analysis/pooled_wbes_6waves.csv

Variable harmonization rules:
- WBES missing codes (-9, -8, -7, -6, -99) -> NaN
- Binary recoding: 1=Yes -> 1, 2=No -> 0
- China 2012 legacy item names: CNo1->h1, CNo3->h8 (R&D spending), CNh7->e6
- Vietnam 2015 h8 special handling: continuous R&D spend -> binary indicator
- Foreign tech: harmonize h7 (pre-2017) -> e6 (post-2017)

Author: Do Thuy Huong
Supervisor: PGS.TS. Phan Anh Tu
"""
from __future__ import annotations
import os
from pathlib import Path
from typing import Dict, Optional

import numpy as np
import pandas as pd

# =====================================================================
# CONFIG - EDIT THESE PATHS TO YOUR LOCAL DATA LOCATIONS
# =====================================================================
DATA_DIR = Path("data/raw")  # adjust to your local path
OUTPUT_PATH = Path("data/analysis/pooled_wbes_6waves.csv")

# Map (country, year) -> relative path to .dta file
DTA_FILES: Dict[tuple, str] = {
    ("SGP", 2023): "Singapore-2023-full-data.dta",
    ("VNM", 2009): "Vietnam-2009-full-data.dta",
    ("VNM", 2015): "Vietnam-2015-full-data.dta",
    ("VNM", 2023): "Vietnam-2023-full-data.dta",
    ("CHN", 2012): "China-2012-full-data.dta",
    ("CHN", 2024): "China-2024-full-data.dta",
}

WBES_MISSING_CODES = [-9, -8, -7, -6, -99, -66, -77, -88]


# =====================================================================
# UTILITY FUNCTIONS
# =====================================================================
def clean_missing(series: pd.Series, codes: list = WBES_MISSING_CODES) -> pd.Series:
    if pd.api.types.is_numeric_dtype(series):
        return series.replace(codes, np.nan)
    return series


def yes_no_binary(series: pd.Series) -> pd.Series:
    """WBES Yes/No (1/2) -> binary (1/0). Other values -> NaN."""
    s = clean_missing(series)
    out = pd.Series(np.nan, index=s.index)
    out[s == 1] = 1.0
    out[s == 2] = 0.0
    return out


def percentage_to_proportion(series: pd.Series) -> pd.Series:
    s = clean_missing(series)
    return s / 100.0


def safe_get(df: pd.DataFrame, col: str) -> pd.Series:
    if col in df.columns:
        return df[col]
    return pd.Series(np.nan, index=df.index)


# =====================================================================
# WAVE-SPECIFIC HARMONIZATION
# =====================================================================
def harmonize_wave(df_raw: pd.DataFrame, country: str, year: int) -> pd.DataFrame:
    df = df_raw.copy()
    out = pd.DataFrame(index=df.index)
    out["country"] = country
    out["year"] = year

    out["firm_id"] = df.get("idstd", pd.Series(range(len(df)), index=df.index))

    # Outcome
    out["sales"] = clean_missing(safe_get(df, "d2"))
    out["employees"] = clean_missing(safe_get(df, "l1"))
    with np.errstate(divide="ignore", invalid="ignore"):
        lp = out["sales"] / out["employees"]
        out["ln_lp"] = np.where(lp > 0, np.log(lp), np.nan)

    # Core IV
    out["fsts"] = percentage_to_proportion(safe_get(df, "d3c"))
    out["fsts_sq"] = out["fsts"] ** 2

    # TCI items
    if country == "CHN" and year == 2012:
        out["foreign_tech"] = yes_no_binary(safe_get(df, "CNh7").fillna(safe_get(df, "h7")))
    elif year < 2017:
        out["foreign_tech"] = yes_no_binary(safe_get(df, "h7"))
    else:
        out["foreign_tech"] = yes_no_binary(safe_get(df, "e6"))

    if country == "CHN" and year == 2012:
        out["product_innov"] = yes_no_binary(
            safe_get(df, "h1").fillna(safe_get(df, "CNo1"))
        )
    elif country == "VNM" and year == 2009:
        out["product_innov"] = np.nan
    else:
        out["product_innov"] = yes_no_binary(safe_get(df, "h1"))

    if country == "CHN" and year == 2012:
        out["rd_spending"] = yes_no_binary(
            safe_get(df, "h8").fillna(safe_get(df, "CNo3"))
        )
    elif country == "VNM" and year == 2009:
        out["rd_spending"] = np.nan
    elif country == "VNM" and year == 2015:
        h8_raw = clean_missing(safe_get(df, "h8"))
        if pd.api.types.is_numeric_dtype(h8_raw) and h8_raw.max() and h8_raw.max() > 1:
            out["rd_spending"] = (h8_raw > 0).astype(float)
        else:
            out["rd_spending"] = yes_no_binary(h8_raw)
    else:
        out["rd_spending"] = yes_no_binary(safe_get(df, "h8"))

    out["quality_cert"] = yes_no_binary(safe_get(df, "b8"))

    # DAI items
    out["website"] = yes_no_binary(safe_get(df, "c22b"))

    if (country, year) in [("SGP", 2023), ("VNM", 2023), ("CHN", 2024)]:
        out["epayment_pct"] = clean_missing(safe_get(df, "k33"))
        out["epay_supp_pct"] = clean_missing(safe_get(df, "k38"))
    else:
        out["epayment_pct"] = np.nan
        out["epay_supp_pct"] = np.nan

    # Controls
    with np.errstate(divide="ignore", invalid="ignore"):
        out["ln_empl"] = np.where(out["employees"] > 0, np.log(out["employees"]), np.nan)

    b5 = clean_missing(safe_get(df, "b5"))
    if b5.notna().any():
        out["firm_age"] = year - b5
        out.loc[out["firm_age"] < 0, "firm_age"] = np.nan
        out.loc[out["firm_age"] > 200, "firm_age"] = np.nan
    else:
        out["firm_age"] = np.nan

    b2b = clean_missing(safe_get(df, "b2b"))
    out["foreign_dummy"] = (b2b > 0).astype("Int64").where(b2b.notna(), pd.NA).astype(float)

    out["manager_exp"] = clean_missing(safe_get(df, "b6"))

    if "a4b_v4" in df.columns:
        out["sector"] = clean_missing(df["a4b_v4"])
    else:
        out["sector"] = clean_missing(safe_get(df, "a4b"))

    out["female_kdm"] = yes_no_binary(safe_get(df, "b7a"))

    if "k7" in df.columns:
        out["credit_access"] = yes_no_binary(df["k7"])
    elif "k8" in df.columns:
        out["credit_access"] = yes_no_binary(df["k8"])
    else:
        out["credit_access"] = np.nan

    return out


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    pooled = []

    for (country, year), filename in DTA_FILES.items():
        full_path = DATA_DIR / filename
        if not full_path.exists():
            print(f"[WARN] Missing file: {full_path} - skipping ({country} {year})")
            continue

        print(f"[INFO] Reading {country} {year}: {full_path}")
        try:
            df_raw = pd.read_stata(full_path, convert_categoricals=False)
        except Exception as e:
            print(f"[ERROR] Failed to read {full_path}: {e}")
            continue

        print(f"        Raw N = {len(df_raw)}")
        df_harm = harmonize_wave(df_raw, country, year)
        print(f"        Harmonized N = {len(df_harm)}")
        pooled.append(df_harm)

    if not pooled:
        print("[ERROR] No data loaded. Edit DATA_DIR and re-run.")
        return

    df_pooled = pd.concat(pooled, ignore_index=True)
    print(f"\n[INFO] Pooled N = {len(df_pooled)}")
    print(df_pooled.groupby(["country", "year"]).size().to_string())

    df_pooled.to_csv(OUTPUT_PATH, index=False)
    print(f"\n[INFO] Saved pooled dataset -> {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
