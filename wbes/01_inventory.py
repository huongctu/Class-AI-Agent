"""
01_inventory.py
Build inventory of WBES .dta files: deduplicate by country-year, identify usable files.

Output: /tmp/wbes/manifest.json with one entry per (country, year) pointing
to the largest .dta file for that pair.

Usage:
    python3 01_inventory.py

Author: Đỗ Thùy Hương — CD1 pipeline.
"""
import os, re, json
from pathlib import Path

UPLOAD_DIR = Path("/root/.claude/uploads/884e7349-32ee-4b8d-a668-1a18a10aaa6b")
files = sorted(UPLOAD_DIR.glob("*.dta"))
print(f"Total .dta files: {len(files)}")

pattern = re.compile(r"^[a-f0-9]+-(.+?)(\d{4}).*\.dta$", re.IGNORECASE)
inventory = {}
unparsed = []
for f in files:
    m = pattern.match(f.name)
    if not m:
        unparsed.append(f.name); continue
    country = m.group(1).rstrip("_").rstrip("-")
    year = m.group(2)
    key = (country, year)
    sz = f.stat().st_size
    if key not in inventory or sz > inventory[key]["size"]:
        inventory[key] = {"path": str(f), "size": sz,
                          "country": country, "year": year}

print(f"Unique country-year units: {len(inventory)}")
print(f"Unparsed files: {len(unparsed)}")

manifest = sorted(inventory.values(), key=lambda x: (x["country"], x["year"]))
out = Path("/tmp/wbes/manifest.json")
out.parent.mkdir(parents=True, exist_ok=True)
with open(out, "w") as fh:
    json.dump(manifest, fh, indent=2)
print(f"Saved {out} with {len(manifest)} entries")

from collections import defaultdict
years_by_country = defaultdict(list)
for v in manifest:
    years_by_country[v["country"]].append(v["year"])
print(f"\nDistinct countries: {len(years_by_country)}")
for c in sorted(years_by_country.keys()):
    print(f"  {c:35s} {sorted(set(years_by_country[c]))}")
