"""
merge_macro_with_pool.py
================================================================================
Merge macro indicators (from fetch_macro_indicators.py output) with WBES firm-level
pool to create enhanced pool for CD2 modeling.

Input:
    wbes/macro/macro_indicators_wide.csv  (country-year × indicators)
    /tmp/wbes/pool.csv                     (firm-level WBES pool, n≈101K)

Output:
    /tmp/wbes/pool_with_macro.csv          (firm-level + macro merged)

Usage (run locally after fetch_macro_indicators.py):
    python3 wbes/merge_macro_with_pool.py

Author: Đỗ Thùy Hương — CD2 macro pipeline.
"""
import pandas as pd
from pathlib import Path

POOL_PATH = Path("/tmp/wbes/pool.csv")
MACRO_PATH = Path("wbes/macro/macro_indicators_wide.csv")
OUT_PATH = Path("/tmp/wbes/pool_with_macro.csv")

print("Loading pool...")
pool = pd.read_csv(POOL_PATH, low_memory=False)
print(f"  Pool: {len(pool):,} firms × {pool.shape[1]} cols")
print(f"  Country-years: {pool.groupby(['country_iso3','year_survey']).ngroups}")

print("\nLoading macro indicators...")
if not MACRO_PATH.exists():
    raise FileNotFoundError(f"{MACRO_PATH} not found. Run fetch_macro_indicators.py first.")
macro = pd.read_csv(MACRO_PATH)
macro.columns = [c.lower() if c not in ["country_iso3","year"] else c for c in macro.columns]
print(f"  Macro: {len(macro):,} country-year rows × {macro.shape[1]} indicators")

# Check missing country-years in macro
pool_cy = set(pool[["country_iso3","year_survey"]].drop_duplicates().apply(tuple, axis=1))
macro_cy = set(macro[["country_iso3","year"]].apply(tuple, axis=1))
missing = pool_cy - macro_cy
if missing:
    print(f"\n  WARN: {len(missing)} country-year pairs missing in macro:")
    for cy in sorted(missing)[:10]:
        print(f"    {cy}")

# Merge: pool's year_survey ↔ macro's year
print("\nMerging...")
merged = pool.merge(macro, left_on=["country_iso3","year_survey"],
                    right_on=["country_iso3","year"], how="left")
merged = merged.drop(columns=["year"], errors="ignore")
print(f"  Merged: {len(merged):,} rows × {merged.shape[1]} cols")
print(f"  Coverage of macro: {merged['rl.est'].notna().mean()*100:.1f}% rows have WGI Rule of Law")
print(f"  Coverage GDP/capita: {merged['ny.gdp.pcap.pp.kd'].notna().mean()*100:.1f}%")

# Add ICRV regime sub-grouping (innovation vs resource Advanced)
print("\nAdding ICRV sub-regime...")
INNOVATION_ADVANCED = ["SGP","HKG","KOR","TWN","ISR","CYP"]
RESOURCE_ADVANCED   = ["SAU","QAT","KWT","BHR","BRN"]
merged["icrv_subregime"] = merged["icrv_regime"]
merged.loc[merged["country_iso3"].isin(INNOVATION_ADVANCED), "icrv_subregime"] = "Advanced-innovation"
merged.loc[merged["country_iso3"].isin(RESOURCE_ADVANCED),   "icrv_subregime"] = "Advanced-resource"
print("  ICRV sub-regime distribution:")
print(merged["icrv_subregime"].value_counts().to_string())

# Save
merged.to_csv(OUT_PATH, index=False)
print(f"\nSaved enhanced pool: {OUT_PATH}")
print(f"Size: {OUT_PATH.stat().st_size / 1e6:.1f} MB")
