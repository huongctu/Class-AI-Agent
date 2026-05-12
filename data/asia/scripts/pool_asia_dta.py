#!/usr/bin/env python3
"""Read each .dta, enrich manifest with n_obs/n_vars, attempt pooled file with core WBES variables."""
import csv
import json
from pathlib import Path
import pyreadstat
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

ROOT = Path("/home/user/Class-AI-Agent/data/asia")
RAW = ROOT / "raw"
POOLED_DIR = ROOT / "pooled"
POOLED_DIR.mkdir(exist_ok=True)

# Load manifest
manifest = list(csv.DictReader(open(ROOT / "manifest.csv")))

# WBES core variables that appear consistently across waves
# (source: Enterprise Surveys Indicator Descriptions, World Bank)
CORE_VARS = {
    # Identifiers
    "idstd": "Standard firm ID",
    "id": "Firm ID",
    "country": "Country (3-digit ISO)",
    "year": "Survey year",
    "a0": "Country (code)",
    "a1": "Country name",
    "a2": "City/region",
    "a3a": "Region code",
    "a3b": "Region name",
    "a4a": "Size strata",
    "a4b": "Industry strata",
    "a6a": "ISIC sector",
    "a6b": "Screener sector",
    # Firm characteristics
    "b1": "Legal status",
    "b2a": "Sector",
    "b2b": "Sector detail",
    "b3": "Year of operation",
    "b4": "Female ownership share",
    "b5": "Year est",
    "b6a": "Foreign ownership %",
    "b7": "Top manager experience (years)",
    # Sales / performance
    "d2": "Total annual sales",
    "d1a3": "Sales 3 years ago",
    "n3": "Total sales last fiscal year",
    "n2a": "Sales 3y ago",
    # Employment
    "l1": "Full-time permanent workers",
    "l2": "Full-time temporary workers",
    "l4a": "Full-time perm workers 3y ago",
    # Exports
    "d3a": "% direct exports",
    "d3b": "% indirect exports",
    "d3c": "% domestic sales",
    "d10": "Established for indirect exports",
    # Innovation
    "h1": "New product/service introduced",
    "h5": "R&D spending",
    # Finance
    "k3a": "Working capital financed internally %",
    "k3bc": "Working capital from banks %",
    # Weight
    "wstrict": "Strict weight",
    "wmedian": "Median weight",
    "weight": "Sample weight",
}

# Step 1: Enrich manifest with schema info
print("Step 1: Reading each .dta to extract schema...")
enriched_rows = []
schema_per_file = {}

def read_dta_robust(path):
    """Read .dta with encoding fallbacks."""
    for enc in (None, "latin1", "cp1252", "utf-8"):
        try:
            kw = {"apply_value_formats": False}
            if enc:
                kw["encoding"] = enc
            return pyreadstat.read_dta(str(path), **kw)
        except Exception as e:
            last = e
    raise last

for i, row in enumerate(manifest, 1):
    fpath = ROOT / row["rel_path"]
    try:
        df, meta = read_dta_robust(fpath)
        n_obs = len(df)
        n_vars = len(df.columns)
        var_names = list(df.columns)
        core_hits = [v for v in CORE_VARS if v in var_names]
        schema_per_file[row["filename"]] = {
            "country": row["country"], "year": row["year"],
            "n_obs": n_obs, "n_vars": n_vars,
            "vars": var_names[:50],  # truncate to 50 first for readability
            "all_vars_count": n_vars,
            "core_vars_present": core_hits,
        }
        enriched_rows.append({**row, "n_obs": n_obs, "n_vars": n_vars,
                             "core_vars": len(core_hits)})
        if i % 20 == 0:
            print(f"  {i}/{len(manifest)} done")
    except Exception as e:
        print(f"  ERROR reading {fpath.name}: {e}")
        enriched_rows.append({**row, "n_obs": -1, "n_vars": -1, "core_vars": 0})

# Write enriched manifest
manifest_path = ROOT / "manifest.csv"
with open(manifest_path, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=enriched_rows[0].keys())
    w.writeheader()
    w.writerows(enriched_rows)

# Write schema JSON
with open(ROOT / "schema.json", "w") as f:
    json.dump(schema_per_file, f, indent=2, default=str)

total_obs = sum(r["n_obs"] for r in enriched_rows if r["n_obs"] > 0)
print(f"\nTotal observations across all files: {total_obs:,}")

# Step 2: Build core-variable pooled file
print("\nStep 2: Pooling on core WBES variables...")
dfs = []
for row in enriched_rows:
    if row["n_obs"] < 0:
        continue
    fpath = ROOT / row["rel_path"]
    try:
        df, _ = read_dta_robust(fpath)
        # Keep only core vars that exist; cast to string for cross-file consistency
        keep = [v for v in CORE_VARS if v in df.columns]
        sub = df[keep].copy() if keep else pd.DataFrame()
        # Add metadata columns (no leading underscore — Stata-safe)
        sub.insert(0, "src_country", row["country"])
        sub.insert(1, "src_year", row["year"])
        sub.insert(2, "src_region", row["region"])
        sub.insert(3, "src_file", row["filename"])
        dfs.append(sub)
    except Exception as e:
        print(f"  skip {fpath.name}: {e}")

pooled = pd.concat(dfs, ignore_index=True, sort=False)
print(f"Pooled shape: {pooled.shape}")
print(f"Pooled columns: {list(pooled.columns)[:20]}...")

# Cast object columns to string for .dta safety
for col in pooled.columns:
    if pooled[col].dtype == "object":
        pooled[col] = pooled[col].astype(str).replace("nan", "")

# Save as .dta (core only) and .csv (everything)
pool_dta = POOLED_DIR / "asia_pooled_core.dta"
pool_csv = POOLED_DIR / "asia_pooled_core.csv"
try:
    pyreadstat.write_dta(pooled, str(pool_dta), file_label="Pooled WBES Asia (core variables)")
    print(f"Wrote {pool_dta} ({pool_dta.stat().st_size / 1024 / 1024:.1f} MB)")
except Exception as e:
    print(f"  .dta write failed: {e}")

pooled.to_csv(pool_csv, index=False)
print(f"Wrote {pool_csv} ({pool_csv.stat().st_size / 1024 / 1024:.1f} MB)")

# Coverage summary
print("\nCore variable coverage:")
for v in CORE_VARS:
    if v in pooled.columns:
        non_null = pooled[v].notna().sum() if pooled[v].dtype != "object" else (pooled[v] != "").sum()
        print(f"  {v}: {non_null:,} / {len(pooled):,} ({100*non_null/len(pooled):.1f}%)")
