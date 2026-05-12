#!/usr/bin/env python3
"""Inventory, dedupe, classify, and copy Asian WBES .dta files into canonical structure."""
import hashlib
import re
import shutil
import sys
from collections import defaultdict
from pathlib import Path
import csv

ALL_DTA = Path("/tmp/all_dta.txt").read_text().strip().splitlines()

# UN M.49 Asia regions + WB "East Asia & Pacific" extension
ASIA_REGIONS = {
    "East Asia": {"China", "HongKongSARChina", "Japan", "Korea", "KoreaRepublic",
                  "Mongolia", "TaiwanChina", "DPRK"},
    "Southeast Asia": {"BruneiDarussalam", "Cambodia", "CambodiaInformal", "Indonesia",
                      "LaoPDR", "LaoInformal", "Laos", "Malaysia", "Myanmar",
                      "Philippines", "Singapore", "Thailand", "TimorLeste", "Vietnam", "VietNam"},
    "South Asia": {"Afghanistan", "Bangladesh", "Bhutan", "India", "Iran",
                  "Maldives", "Nepal", "Pakistan", "SriLanka"},
    "Central Asia": {"Kazakhstan", "KyrgyzRepublic", "Kyrgyzrepublic",
                    "Tajikistan", "Turkmenistan", "Uzbekistan"},
    "West Asia": {"Armenia", "Azerbaijan", "Bahrain", "Cyprus", "Republic_of_Cyprus",
                 "Georgia", "Iraq", "Israel", "Jordan", "Kuwait", "Lebanon",
                 "Oman", "Palestine", "Qatar", "Saudi-Arabia", "Syria", "Turkey",
                 "UAE", "Yemen"},
    "Pacific": {"Fiji", "Samoa", "Kiribati", "Tonga", "Solomon-Islands",
                "PapuaNewGuinea", "Papua-New-Guinea", "Vanuatu", "Tuvalu",
                "Palau", "Nauru", "MarshallIslands", "Micronesia"},
}
NOT_ASIA = set()  # Pacific now included per World Bank EAP regional grouping

# Country name canonicalization
NAME_MAP = {
    "VietNam": "Vietnam",
    "HongKongSARChina": "HongKong",
    "TaiwanChina": "Taiwan",
    "KoreaRepublic": "Korea",
    "BruneiDarussalam": "Brunei",
    "LaoPDR": "Laos", "Laos": "Laos", "LaoInformal": "Laos",
    "Kyrgyzrepublic": "KyrgyzRepublic",
    "Republic_of_Cyprus": "Cyprus",
    "CambodiaInformal": "Cambodia",
    "Saudi-Arabia": "SaudiArabia",
    "TimorLeste": "TimorLeste",
    "Papua-New-Guinea": "PapuaNewGuinea",
    "Solomon-Islands": "SolomonIslands",
    "PapuaNewGuinea": "PapuaNewGuinea",
}

ALL_COUNTRIES = set()
for r in ASIA_REGIONS.values():
    ALL_COUNTRIES.update(r)

def parse_filename(path: str):
    """Extract country, year, wave_tag from filename."""
    fname = Path(path).name
    # Strip UUID prefix: '0f95fc42-Armenia2024fulldata.dta' -> 'Armenia2024fulldata.dta'
    stem = re.sub(r'^[0-9a-f]{8}-', '', fname)
    stem = stem.replace('.dta', '')

    # Multi-country panel files
    if '_' in stem and re.search(r'\d{4}_\d{4}', stem):
        m = re.match(r'^([A-Za-z\-]+)_(\d{4}(?:_\d{4})+)', stem)
        if m:
            return m.group(1), m.group(2).replace('_', '-'), 'panel'

    # Standard: Country YYYY fulldata / full-data
    # Handle 'Lebanon-COVID follow up 2020-full data' style with non-standard
    m = re.match(r'^([A-Za-z][A-Za-z\-]*?)[\s\-]*?(\d{4})[\s\-]?(.*)$', stem)
    if m:
        country = m.group(1).strip('-').strip()
        year = m.group(2)
        suffix = m.group(3).strip('-').strip().replace(' ', '')
        return country, year, suffix or 'fulldata'

    return None, None, None

# Classify
inventory = []
by_country_year = defaultdict(list)

for p in ALL_DTA:
    country, year, tag = parse_filename(p)
    if country is None:
        continue
    country_canon = NAME_MAP.get(country, country)
    # Determine region
    region = None
    for r, members in ASIA_REGIONS.items():
        if country in members or country_canon in members:
            region = r
            break
    if region is None:
        if country in NOT_ASIA or country_canon in NOT_ASIA:
            continue  # Pacific - skip
        # Skip unknown
        continue
    size = Path(p).stat().st_size
    h = hashlib.md5(Path(p).read_bytes()).hexdigest()[:8]
    inventory.append({
        "src": p, "country": country_canon, "year": year, "tag": tag,
        "region": region, "size": size, "md5_8": h
    })
    by_country_year[(country_canon, year, tag)].append((size, p, h))

# Dedupe: keep largest file (most data) per (country, year, tag)
chosen = {}
for key, files in by_country_year.items():
    files.sort(key=lambda x: -x[0])  # largest first
    chosen[key] = files[0]

print(f"Total .dta scanned: {len(ALL_DTA)}")
print(f"Asia-classified files: {len(inventory)}")
print(f"Deduplicated unique country-year-tag: {len(chosen)}")

# Build target tree
target_root = Path("/home/user/Class-AI-Agent/data/asia")
raw_root = target_root / "raw"
raw_root.mkdir(parents=True, exist_ok=True)

manifest_rows = []
for (country, year, tag), (size, src, h) in sorted(chosen.items()):
    country_dir = raw_root / country
    country_dir.mkdir(exist_ok=True)
    # canonical name
    if tag == 'fulldata':
        fname = f"{country}_{year}.dta"
    elif tag == 'panel':
        fname = f"{country}_panel_{year}.dta"
    else:
        fname = f"{country}_{year}_{tag}.dta"
    dst = country_dir / fname
    shutil.copy2(src, dst)
    # find region
    region = next((r for r, m in ASIA_REGIONS.items()
                  if country in m or any(NAME_MAP.get(x, x) == country for x in m)), "Unknown")
    manifest_rows.append({
        "region": region,
        "country": country,
        "year": year,
        "tag": tag,
        "filename": fname,
        "rel_path": str(dst.relative_to(target_root)),
        "size_bytes": size,
        "size_mb": round(size / 1024 / 1024, 2),
        "md5_8": h,
    })

# Write manifest CSV
manifest_path = target_root / "manifest.csv"
with open(manifest_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=manifest_rows[0].keys())
    writer.writeheader()
    writer.writerows(manifest_rows)

print(f"\nManifest: {manifest_path}")
print(f"Total files copied: {len(manifest_rows)}")
print(f"Total size: {sum(r['size_bytes'] for r in manifest_rows) / 1024 / 1024:.1f} MB")

# Summary by region/country
from collections import Counter
print("\nBy region:")
region_count = Counter(r['region'] for r in manifest_rows)
for r, c in sorted(region_count.items()):
    print(f"  {r}: {c} files")

print("\nBy country:")
country_count = Counter(r['country'] for r in manifest_rows)
for c, cnt in sorted(country_count.items()):
    print(f"  {c}: {cnt}")
