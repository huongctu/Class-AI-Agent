"""
wbes/02_harmonize.py
====================
Harmonize raw WBES .dta files for all 47 economies → /tmp/wbes/pool.csv

Usage
-----
  python wbes/02_harmonize.py [--raw-dir RAW_DIR] [--out OUT]

Arguments
---------
  --raw-dir   Directory containing per-country subdirectories of .dta files.
              Default: raw/
              Structure expected:
                raw/VNM/VNM_2009_wbes.dta
                raw/VNM/VNM_2015_wbes.dta
                raw/CHN/CHN_2012_wbes.dta
                ...
  --out       Output CSV path. Default: /tmp/wbes/pool.csv

Falls back to data/analysis/pooled_wbes_6waves.csv (already harmonised,
3 countries) if no .dta files are found under --raw-dir.

Author: Đỗ Thùy Hương | thesis 2026
"""
from __future__ import annotations

import argparse
import logging
import math
import re
import sys
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd

# ── import catalogue ──────────────────────────────────────────────────────────
sys.path.insert(0, str(Path(__file__).parent))
from config_wbes import (
    COUNTRY_WAVES, ICRV,
    VAR_MAP_PRIMARY, VAR_MAP_OVERRIDES, SECTOR_LABELS,
)

logging.basicConfig(
    format="%(levelname)s | %(message)s",
    level=logging.INFO,
)
log = logging.getLogger("harmonize")

# ── constants ─────────────────────────────────────────────────────────────────
SURVEY_YEAR_RE = re.compile(r"_(\d{4})_")


# ── helpers ───────────────────────────────────────────────────────────────────

def _detect_year(path: Path) -> Optional[int]:
    """Extract survey year from filename."""
    m = SURVEY_YEAR_RE.search(path.name)
    return int(m.group(1)) if m else None


def _find_dta(raw_dir: Path, iso3: str, year: int) -> Optional[Path]:
    """Locate any .dta file for (iso3, year) under raw_dir/iso3/."""
    country_dir = raw_dir / iso3
    if not country_dir.exists():
        return None
    for p in country_dir.glob("*.dta"):
        y = _detect_year(p)
        if y == year:
            return p
        # some files are named without year — fall through
    # fuzzy: any .dta in directory if only one file for iso3
    dtas = list(country_dir.glob("*.dta"))
    if len(dtas) == 1:
        return dtas[0]
    return None


def _build_var_map(year: int) -> dict[str, str]:
    vmap = dict(VAR_MAP_PRIMARY)
    overrides = VAR_MAP_OVERRIDES.get(year, {})
    vmap.update(overrides)
    return vmap


def _read_dta(path: Path, var_map: dict[str, str]) -> pd.DataFrame:
    """Read one WBES .dta, rename to harmonised columns, return raw slice."""
    log.info(f"  Reading {path.name} …")
    try:
        df = pd.read_stata(str(path), convert_categoricals=False)
    except Exception:
        df = pd.read_stata(str(path), convert_categoricals=True)

    # lower-case all column names for safe matching
    df.columns = [c.lower().strip() for c in df.columns]

    rename = {}
    for raw, harm in var_map.items():
        raw_l = raw.lower()
        if raw_l in df.columns and harm not in rename.values():
            rename[raw_l] = harm

    df = df.rename(columns=rename)
    keep = [c for c in var_map.values() if c in df.columns]
    # always keep firm_id if present
    for cand in ["idstd", "id_std", "firmid", "id"]:
        if cand in df.columns and "firm_id" not in df.columns:
            df["firm_id"] = df[cand]
            keep.append("firm_id")
    df = df[[c for c in keep if c in df.columns]].copy()
    return df


def _derive_variables(df: pd.DataFrame, iso3: str, year: int) -> pd.DataFrame:
    df = df.copy()

    # ── labor productivity ────────────────────────────────────────────────────
    sales = pd.to_numeric(df.get("total_sales_raw", pd.Series(dtype=float)),
                          errors="coerce")
    empl = pd.to_numeric(df.get("employees", pd.Series(dtype=float)),
                         errors="coerce")
    lp = sales / empl.replace(0, np.nan)
    df["ln_labor_prod"] = np.log(lp.clip(lower=1e-6)).where(
        (lp > 0) & lp.notna() & (empl > 0)
    )
    df["ln_empl"] = np.log(empl.replace(0, np.nan)).where(empl > 0)

    # ── FSTS: export_pct already 0-100 (WBES a14b is 0-100) ─────────────────
    ep = pd.to_numeric(df.get("export_pct", pd.Series(dtype=float)), errors="coerce")
    df["export_pct"] = ep.clip(0, 100)
    df["exporter"] = (ep > 0).astype(float).where(ep.notna())

    # ── firm age ──────────────────────────────────────────────────────────────
    yr_est = pd.to_numeric(df.get("yr_established", pd.Series(dtype=float)),
                           errors="coerce")
    df["firm_age"] = (year - yr_est).clip(0, 150).where(yr_est.notna())
    df.drop(columns=["yr_established"], errors="ignore", inplace=True)

    # ── foreign ownership ─────────────────────────────────────────────────────
    fo = pd.to_numeric(df.get("foreign_own", pd.Series(dtype=float)), errors="coerce")
    df["foreign_own"] = fo.clip(0, 100)

    # ── binary indicators → 0/1 (may be coded as 1=yes/2=no in old WBES) ────
    for col in ["quality_cert", "foreign_tech", "website",
                "product_innov", "process_innov", "rd_spending"]:
        if col not in df.columns:
            continue
        s = pd.to_numeric(df[col], errors="coerce")
        # WBES sometimes: 1=yes, 2=no  → recode
        if s.dropna().isin([1, 2]).all() and (s == 2).any():
            df[col] = (s == 1).astype(float).where(s.notna())
        else:
            df[col] = s.clip(0, 1)

    # ── TCI composite ─────────────────────────────────────────────────────────
    tci_items = df[["quality_cert", "foreign_tech"]].apply(
        pd.to_numeric, errors="coerce"
    )
    valid_n = tci_items.notna().sum(axis=1)
    df["TCI_thin"] = tci_items.mean(axis=1, skipna=True).where(valid_n >= 1)

    extra = [c for c in ["product_innov", "process_innov", "rd_spending"]
             if c in df.columns]
    if extra:
        full_items = pd.concat([tci_items, df[extra].apply(pd.to_numeric, errors="coerce")], axis=1)
        valid_full = full_items.notna().sum(axis=1)
        df["TCI_full"] = full_items.mean(axis=1, skipna=True).where(valid_full >= 2)
    else:
        df["TCI_full"] = df["TCI_thin"]

    # ── DAI composites ────────────────────────────────────────────────────────
    df["DAI_thin"] = pd.to_numeric(df.get("website", pd.Series(dtype=float)),
                                   errors="coerce").clip(0, 1)
    epay = pd.to_numeric(df.get("epayment_pct", pd.Series(dtype=float)), errors="coerce")
    epay_s = pd.to_numeric(df.get("epay_supp_pct", pd.Series(dtype=float)), errors="coerce")
    dai_items = pd.concat([df["DAI_thin"], (epay / 100).clip(0, 1),
                           (epay_s / 100).clip(0, 1)], axis=1)
    valid_dai = dai_items.notna().sum(axis=1)
    df["DAI_rich"] = dai_items.mean(axis=1, skipna=True).where(valid_dai >= 1)

    # ── sector ────────────────────────────────────────────────────────────────
    if "sector_isic4" in df.columns:
        s2d = pd.to_numeric(df["sector_isic4"], errors="coerce") // 10 * 10
        df["sector"] = s2d.map(SECTOR_LABELS).fillna("Other")
    else:
        df["sector"] = "Unknown"

    # ── identifiers ──────────────────────────────────────────────────────────
    df["country"] = iso3
    df["year"] = year
    df["dataset"] = f"{iso3}_{year}"

    return df


_HARMONISED_COLS = [
    "dataset", "country", "year",
    "website", "foreign_tech", "product_innov", "process_innov",
    "rd_spending", "quality_cert",
    "epayment_pct", "epay_supp_pct",
    "total_sales_raw", "employees",
    "ln_labor_prod", "ln_empl",
    "export_pct", "exporter",
    "firm_age", "manager_exp", "foreign_own",
    "TCI_thin", "TCI_full", "DAI_thin", "DAI_rich",
    "sector",
]


def harmonise_one(raw_dir: Path, iso3: str, year: int) -> Optional[pd.DataFrame]:
    """Return harmonised DataFrame for one (iso3, year) wave, or None."""
    path = _find_dta(raw_dir, iso3, year)
    if path is None:
        log.warning(f"  {iso3} {year}: .dta not found under {raw_dir / iso3}/")
        return None

    var_map = _build_var_map(year)
    try:
        df = _read_dta(path, var_map)
    except Exception as exc:
        log.error(f"  {iso3} {year}: read error — {exc}")
        return None

    if df.empty:
        log.warning(f"  {iso3} {year}: empty after variable selection")
        return None

    df = _derive_variables(df, iso3, year)

    # keep only harmonised columns that exist
    cols = [c for c in _HARMONISED_COLS if c in df.columns]
    return df[cols]


def harmonise_all(raw_dir: Path) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    total_waves = sum(len(yrs) for yrs in COUNTRY_WAVES.values())
    done = skipped = 0

    for iso3, years in COUNTRY_WAVES.items():
        if not years:
            log.info(f"[SKIP] {iso3}: no WBES rounds listed")
            skipped += 1
            continue
        log.info(f"[{iso3}] {len(years)} wave(s): {years}")
        for year in years:
            df = harmonise_one(raw_dir, iso3, year)
            if df is not None and not df.empty:
                frames.append(df)
                done += 1
            else:
                skipped += 1

    log.info(f"\nLoaded {done}/{total_waves} waves ({skipped} skipped/missing).")
    if not frames:
        raise RuntimeError(
            "No data loaded. Check --raw-dir contains subdirectories "
            "with .dta files, e.g.  raw/VNM/VNM_2009_wbes.dta"
        )
    pool = pd.concat(frames, ignore_index=True)
    log.info(f"Pool: {len(pool):,} rows × {pool.shape[1]} cols, "
             f"{pool['country'].nunique()} countries.")
    return pool


def _fallback_6wave(path_6w: Path) -> pd.DataFrame:
    """Load the pre-harmonised 6-wave file (SGP/VNM/CHN only)."""
    log.info(f"[FALLBACK] Using {path_6w}")
    df = pd.read_csv(path_6w)
    if "sector" not in df.columns:
        df["sector"] = "Unknown"
    return df


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Harmonise WBES → pool.csv")
    parser.add_argument("--raw-dir", default="raw",
                        help="Root directory of raw .dta files (default: raw/)")
    parser.add_argument("--out", default="/tmp/wbes/pool.csv",
                        help="Output CSV path (default: /tmp/wbes/pool.csv)")
    parser.add_argument("--fallback", default="data/analysis/pooled_wbes_6waves.csv",
                        help="Fallback CSV if no .dta files found")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    # Check if any .dta files exist
    has_dta = raw_dir.exists() and any(raw_dir.rglob("*.dta"))

    if has_dta:
        log.info(f"Found .dta files under {raw_dir}. Running full harmonisation.")
        pool = harmonise_all(raw_dir)
    else:
        fallback = Path(args.fallback)
        if fallback.exists():
            log.warning(f"No .dta files found under {raw_dir}.")
            log.warning("Using fallback 6-wave pool (VNM/CHN/SGP only).")
            log.warning("To run all 47 countries: place WBES .dta files under raw/<ISO3>/")
            pool = _fallback_6wave(fallback)
        else:
            log.error(
                f"No .dta files found under {raw_dir} "
                f"and fallback {fallback} does not exist."
            )
            log.error(
                "\nTo obtain WBES data:\n"
                "  1. Go to https://microdata.worldbank.org/index.php/catalog/enterprise_surveys\n"
                "  2. Filter by country and download the Stata (.dta) files\n"
                "  3. Place under raw/<ISO3>/<ISO3>_<year>_wbes.dta\n"
                "  4. Re-run:  python wbes/02_harmonize.py\n"
            )
            sys.exit(1)

    pool.to_csv(out_path, index=False)
    log.info(f"\n✓ Pool saved → {out_path}  ({len(pool):,} rows)")

    # Summary statistics
    log.info("\n── Country coverage ──────────────────────────────────────────")
    summary = (
        pool.groupby("country")
        .agg(n=("country", "count"), years=("year", lambda x: sorted(x.unique())))
        .reset_index()
    )
    for _, row in summary.iterrows():
        regime = ICRV.get(row["country"], "?")
        log.info(f"  {row['country']:5s}  n={row['n']:6,}  {row['years']}  [{regime}]")

    log.info(f"\nTotal: {len(pool):,} firm-wave observations, "
             f"{pool['country'].nunique()} countries")


if __name__ == "__main__":
    main()
