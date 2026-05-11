#!/usr/bin/env python3
"""
merge_wbes_dta.py — Gộp và chuẩn hóa file .dta WBES từ 47 quốc gia.

Xử lý 3 thế hệ schema WBES:
  - PICS3      (2009–2013): schema gốc
  - Standardized (2014–2018): schema chuẩn hóa
  - BREADY/BEE  (2019–2025): schema hiện đại

Chạy:
  python3 scripts/merge_wbes_dta.py --dir data/wbes_raw/ --out data/wbes_pooled.csv
  python3 scripts/merge_wbes_dta.py --demo   # chạy demo với synthetic data
"""

import re
import sys
import argparse
import warnings
from pathlib import Path
from dataclasses import dataclass, field

import numpy as np
import pandas as pd

try:
    import pyreadstat
    DTA_AVAILABLE = True
except ImportError:
    DTA_AVAILABLE = False
    warnings.warn("pyreadstat không có — chỉ hỗ trợ demo mode")

# ─── Schema harmonization map ────────────────────────────────────────────────
# Mỗi key là tên biến chuẩn (canonical); value là danh sách alias theo schema
VARMAP = {
    # --- Dependent variable ---
    "ln_lp":        ["ln_lp", "lnlp"],                         # computed
    "annual_sales": ["d2", "d2a", "annual_sales_lcu"],          # sales LCU
    "employees_perm": ["l1", "employees_perm", "perm_emp"],     # permanent staff

    # --- Internationalization ---
    "fsts":         ["d3c", "d3b", "fsts_pct"],                # % sales exported / 100
    "exporter":     ["d3", "exporter_bin"],                    # binary

    # --- TCI components ---
    "iso_cert":     ["b8", "b8a", "iso_certified"],
    "rd_dummy":     ["h8", "h7a", "do_rd"],
    "innov_product":["h1", "h2a", "new_product"],
    "foreign_tech": ["e6", "e6a", "uses_foreign_tech"],

    # --- DAI components ---
    "website":      ["c22b", "d4a", "has_website"],
    "epay_b2b":     ["k33", "k22a", "epayment_b2b"],
    "epay_b2c":     ["k38", "k29b", "epayment_b2c"],

    # --- Manager characteristics ---
    "exp_manager":  ["b5", "b5a", "manager_exp_years"],
    "educ_manager": ["b7", "b7a", "manager_educ_level"],
    "gender_manager":["b6a", "b6", "female_manager"],

    # --- Controls ---
    "firm_age":     ["b5", "year_established", "firm_age_years"],  # computed from estab year
    "size_cat":     ["a6a", "a6b", "size_category"],
    "foreign_own":  ["b2b", "b3b", "foreign_ownership_pct"],
    "sector":       ["a4b", "a4a", "sector_isic"],
    "country":      ["country", "countrycode", "country_iso3"],
    "year":         ["year", "survey_year", "wbes_year"],
}

# ICRV 5-regime mapping (WGI Rule of Law thresholds: +0.80 / -0.50)
ICRV_MAP = {
    # I — Advanced (WGI > +0.80)
    "SGP": "I_Advanced", "HKG": "I_Advanced", "KOR": "I_Advanced",
    "TWN": "I_Advanced", "ISR": "I_Advanced",
    # II — Upper-middle (0 ≤ WGI ≤ +0.80)
    "SAU": "II_UpperMiddle", "QAT": "II_UpperMiddle", "KWT": "II_UpperMiddle",
    "BHR": "II_UpperMiddle", "BRN": "II_UpperMiddle",
    "CHN": "II_UpperMiddle", "MYS": "II_UpperMiddle", "THA": "II_UpperMiddle",
    "KAZ": "II_UpperMiddle", "ARM": "II_UpperMiddle", "GEO": "II_UpperMiddle",
    # III — Emerging (-0.50 < WGI < 0)
    "VNM": "III_Emerging", "IDN": "III_Emerging", "PHL": "III_Emerging",
    "IND": "III_Emerging", "LKA": "III_Emerging", "JOR": "III_Emerging",
    "MNG": "III_Emerging",
    # IV — Frontier (WGI < -0.50)
    "BGD": "IV_Frontier", "PAK": "IV_Frontier", "LAO": "IV_Frontier",
    "KHM": "IV_Frontier", "MMR": "IV_Frontier", "NPL": "IV_Frontier",
    "BTN": "IV_Frontier", "MDV": "IV_Frontier", "UZB": "IV_Frontier",
    "TJK": "IV_Frontier", "KGZ": "IV_Frontier", "TKM": "IV_Frontier",
    "AFG": "IV_Frontier", "TLS": "IV_Frontier", "IRQ": "IV_Frontier",
    "LBN": "IV_Frontier", "YEM": "IV_Frontier",
    # V — SIDS Pacific
    "FJI": "V_SIDS", "PNG": "V_SIDS", "SLB": "V_SIDS",
    "TON": "V_SIDS", "VUT": "V_SIDS", "WSM": "V_SIDS", "KIR": "V_SIDS",
}


@dataclass
class HarmonizeLog:
    country: str
    year: int
    schema: str
    n_raw: int
    n_clean: int
    missing_vars: list = field(default_factory=list)


def detect_schema(cols: list[str]) -> str:
    """Detect WBES schema generation from column names."""
    cols_lower = {c.lower() for c in cols}
    if "k33" in cols_lower or "k38" in cols_lower:
        return "BREADY_BEE"
    if "c22b" in cols_lower or "h8" in cols_lower:
        return "Standardized"
    return "PICS3"


def find_col(df: pd.DataFrame, aliases: list[str]) -> str | None:
    """Find first matching alias in DataFrame columns (case-insensitive)."""
    cols_lower = {c.lower(): c for c in df.columns}
    for alias in aliases:
        if alias.lower() in cols_lower:
            return cols_lower[alias.lower()]
    return None


def harmonize_one(df: pd.DataFrame, country: str, year: int) -> tuple[pd.DataFrame, HarmonizeLog]:
    schema   = detect_schema(list(df.columns))
    n_raw    = len(df)
    missing  = []
    out      = pd.DataFrame()

    for canonical, aliases in VARMAP.items():
        col = find_col(df, aliases)
        if col:
            out[canonical] = pd.to_numeric(df[col], errors="coerce")
        else:
            out[canonical] = np.nan
            missing.append(canonical)

    # Derived variables
    # FSTS: convert from percentage (0–100) to proportion (0–1)
    if "fsts" in out.columns and out["fsts"].max(skipna=True) > 1.5:
        out["fsts"] = out["fsts"] / 100.0
    out["fsts"] = out["fsts"].clip(0, 1)

    # ln(LP) = ln(annual_sales / employees_perm)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        out["ln_lp"] = np.log(
            out["annual_sales"].clip(lower=1) / out["employees_perm"].clip(lower=1)
        )

    # TCI composite (z-score of ≥3 valid components)
    tci_items = ["iso_cert", "rd_dummy", "innov_product", "foreign_tech"]
    tci_avail = [c for c in tci_items if out[c].notna().sum() > 0]
    if len(tci_avail) >= 3:
        tci_raw = out[tci_avail].mean(axis=1, skipna=True)
        out["tci_z"] = (tci_raw - tci_raw.mean()) / tci_raw.std()
    else:
        out["tci_z"] = np.nan

    # DAI composite
    dai_items_t1 = ["website"]
    dai_items_t2 = ["epay_b2b", "epay_b2c"]
    dai_t1 = out[dai_items_t1].mean(axis=1, skipna=True)
    if schema == "BREADY_BEE":
        dai_t2 = out[dai_items_t2].mean(axis=1, skipna=True)
        dai_raw = (dai_t1 + dai_t2) / 2
    else:
        dai_raw = dai_t1
    out["dai_z"] = (dai_raw - dai_raw.mean()) / (dai_raw.std() + 1e-9)

    # Foreign ownership binary (≥10%)
    out["foreign_own_bin"] = (out["foreign_own"] >= 10).astype(float)

    # Country / year / schema metadata
    out["country_iso3"] = country
    out["survey_year"]  = year
    out["schema"]       = schema
    out["icrv_regime"]  = ICRV_MAP.get(country, "Unknown")

    # Drop observations with no DV or IV
    mask = out["ln_lp"].notna() & out["fsts"].notna()
    out  = out[mask].copy()

    log = HarmonizeLog(country=country, year=year, schema=schema,
                       n_raw=n_raw, n_clean=len(out), missing_vars=missing)
    return out, log


def load_dta_dir(dta_dir: Path) -> pd.DataFrame:
    """Load and harmonize all .dta files from a directory."""
    dta_files = sorted(dta_dir.glob("*.dta"))
    if not dta_files:
        print(f"  ❌  Không tìm thấy file .dta trong {dta_dir}")
        sys.exit(1)

    frames, logs = [], []
    for f in dta_files:
        # Expect filename pattern: VNM_2015.dta or vietnam_2015.dta
        stem = f.stem.upper()
        parts = re.split(r"[_\-\s]", stem)
        country = parts[0][:3]
        year_matches = [p for p in parts if re.match(r"20\d{2}|199\d", p)]
        year = int(year_matches[0]) if year_matches else 0

        print(f"  Loading {f.name} ({country} {year})...", end=" ")
        try:
            df, meta = pyreadstat.read_dta(str(f))
            df_clean, log = harmonize_one(df, country, year)
            frames.append(df_clean)
            logs.append(log)
            print(f"n={log.n_raw} → {log.n_clean} [{log.schema}]")
        except Exception as e:
            print(f"ERROR: {e}")

    if not frames:
        print("  ❌  Không load được file nào.")
        sys.exit(1)

    pooled = pd.concat(frames, ignore_index=True)

    print(f"\n  ✅  Pool: {len(pooled):,} doanh nghiệp | "
          f"{pooled['country_iso3'].nunique()} quốc gia | "
          f"{pooled['survey_year'].nunique()} năm khảo sát")

    # Summary log
    print("\n  Bảng tóm tắt harmonization:")
    print(f"  {'Country':8} {'Year':6} {'Schema':15} {'Raw':>7} {'Clean':>7} {'Loss%':>7}")
    print(f"  {'─'*55}")
    for lg in logs:
        loss = 100 * (1 - lg.n_clean / max(lg.n_raw, 1))
        print(f"  {lg.country:8} {lg.year:6} {lg.schema:15} {lg.n_raw:7,} {lg.n_clean:7,} {loss:6.1f}%")

    return pooled


def make_demo_data(n_countries: int = 10, seed: int = 42) -> pd.DataFrame:
    """Generate synthetic WBES-like data for demo."""
    np.random.seed(seed)
    countries = list(ICRV_MAP.keys())[:n_countries]
    frames = []
    for c in countries:
        for year in [2015, 2019, 2023]:
            n = np.random.randint(80, 400)
            df = pd.DataFrame({
                "country_iso3": c,
                "survey_year":  year,
                "schema":       "Standardized" if year < 2019 else "BREADY_BEE",
                "icrv_regime":  ICRV_MAP.get(c, "Unknown"),
                "fsts":         np.random.beta(0.7, 5, n).clip(0, 1),
                "ln_lp":        np.random.normal(11.5, 1.2, n),
                "tci_z":        np.random.normal(0, 1, n),
                "dai_z":        np.random.normal(0, 1, n),
                "exp_manager":  np.random.randint(0, 35, n).astype(float),
                "foreign_own_bin": (np.random.rand(n) > 0.8).astype(float),
            })
            frames.append(df)
    return pd.concat(frames, ignore_index=True)


def print_summary(df: pd.DataFrame):
    print(f"\n{'='*65}")
    print("  WBES Pooled Dataset — Summary Statistics")
    print(f"{'='*65}")
    print(f"  N total:         {len(df):>10,}")
    print(f"  Countries:       {df['country_iso3'].nunique():>10,}")
    print(f"  Survey years:    {df['survey_year'].nunique():>10,}")
    print(f"  FSTS > 0:        {(df['fsts'] > 0).sum():>10,}  ({100*(df['fsts']>0).mean():.1f}%)")
    print(f"  Mean FSTS:       {df['fsts'].mean():>10.3f}")
    print(f"  Mean ln(LP):     {df['ln_lp'].mean():>10.3f}")

    print(f"\n  ICRV Regime breakdown:")
    regime_counts = df["icrv_regime"].value_counts()
    for regime, cnt in regime_counts.items():
        bar = "█" * max(1, int(30 * cnt / len(df)))
        print(f"    {regime:<20} {cnt:>7,}  {bar}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Gộp file .dta WBES từ 47 quốc gia")
    parser.add_argument("--dir",  default="data/wbes_raw/", help="Thư mục chứa file .dta")
    parser.add_argument("--out",  default="data/wbes_pooled.csv", help="Output CSV")
    parser.add_argument("--demo", action="store_true", help="Chạy demo với synthetic data")
    args = parser.parse_args()

    print("\nWBES Data Harmonization Pipeline")
    print("─" * 65)

    if args.demo:
        print("  [DEMO MODE] Tạo synthetic WBES data...")
        df = make_demo_data(n_countries=10)
        print_summary(df)
        print("  Để dùng với real data: python3 scripts/merge_wbes_dta.py --dir data/wbes_raw/\n")
        return

    if not DTA_AVAILABLE:
        print("  ❌  pyreadstat chưa cài. Chạy: pip install pyreadstat")
        sys.exit(1)

    dta_dir = Path(args.dir)
    if not dta_dir.exists():
        print(f"  ❌  Thư mục không tồn tại: {dta_dir}")
        print("      Tạo thư mục và đặt các file .dta vào đó:")
        print("      mkdir -p data/wbes_raw/")
        print("      # Đặt VNM_2015.dta, VNM_2023.dta, CHN_2012.dta ... vào data/wbes_raw/")
        sys.exit(1)

    df = load_dta_dir(dta_dir)
    print_summary(df)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out_path, index=False, encoding="utf-8")
    print(f"  💾  Đã lưu: {out_path}  ({len(df):,} dòng × {len(df.columns)} cột)\n")


if __name__ == "__main__":
    main()
