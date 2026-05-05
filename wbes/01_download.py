"""
wbes/01_download.py
===================
Helper to download WBES Stata files from the World Bank Microdata Library.

Usage
-----
  python wbes/01_download.py --list          # show all 47 surveys to download
  python wbes/01_download.py --check         # check which files are already present
  python wbes/01_download.py --download      # attempt bulk download (requires login token)

Manual download (recommended for thesis)
----------------------------------------
1. Go to  https://microdata.worldbank.org/index.php/catalog/enterprise_surveys
2. For each economy in the list below:
   a. Search by country name
   b. Open the most recent survey round
   c. Download → "Stata" (.dta) format
   d. Place the file in:  raw/<ISO3>/<ISO3>_<year>_wbes.dta
3. Run:  python wbes/02_harmonize.py

Note: World Bank WBES data is freely available but requires a (free) account
on the microdata portal for bulk downloads.

Author: Đỗ Thùy Hương | thesis 2026
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config_wbes import COUNTRY_WAVES, ICRV

# World Bank WBES microdata portal base
PORTAL_URL = "https://microdata.worldbank.org/index.php/catalog/enterprise_surveys"

# Country full names for the download checklist
COUNTRY_NAMES: dict[str, str] = {
    "SGP": "Singapore",        "HKG": "Hong Kong SAR, China",
    "KOR": "Korea, Rep.",      "TWN": "Taiwan, China",
    "ISR": "Israel",           "CYP": "Cyprus",
    "SAU": "Saudi Arabia",     "QAT": "Qatar",
    "KWT": "Kuwait",           "BHR": "Bahrain",
    "BRN": "Brunei Darussalam","CHN": "China",
    "MYS": "Malaysia",         "THA": "Thailand",
    "KAZ": "Kazakhstan",       "ARM": "Armenia",
    "GEO": "Georgia",          "IND": "India",
    "IDN": "Indonesia",        "PHL": "Philippines",
    "VNM": "Vietnam",          "LKA": "Sri Lanka",
    "JOR": "Jordan",           "MNG": "Mongolia",
    "BGD": "Bangladesh",       "PAK": "Pakistan",
    "LAO": "Lao PDR",          "KHM": "Cambodia",
    "MMR": "Myanmar",          "NPL": "Nepal",
    "BTN": "Bhutan",           "MDV": "Maldives",
    "UZB": "Uzbekistan",       "TJK": "Tajikistan",
    "KGZ": "Kyrgyz Republic",  "TKM": "Turkmenistan",
    "AFG": "Afghanistan",      "TLS": "Timor-Leste",
    "IRQ": "Iraq",             "LBN": "Lebanon",
    "YEM": "Yemen",            "FJI": "Fiji",
    "PNG": "Papua New Guinea", "SLB": "Solomon Islands",
    "TON": "Tonga",            "VUT": "Vanuatu",
    "WSM": "Samoa",
}


def list_surveys() -> None:
    """Print the full download checklist."""
    print("\n" + "="*72)
    print("WBES DOWNLOAD CHECKLIST — 47 economies")
    print(f"Portal: {PORTAL_URL}")
    print("="*72)
    print(f"{'ISO3':<6} {'Regime':<22} {'Years':<20} {'Country Name'}")
    print("-"*72)
    for iso3, years in COUNTRY_WAVES.items():
        regime = ICRV.get(iso3, "?")
        name   = COUNTRY_NAMES.get(iso3, iso3)
        yr_str = str(years) if years else "(no WBES rounds)"
        print(f"{iso3:<6} {regime:<22} {yr_str:<20} {name}")
    print("-"*72)
    total = sum(1 for yrs in COUNTRY_WAVES.values() if yrs)
    print(f"\nTotal: {len(COUNTRY_WAVES)} economies, "
          f"{total} with available WBES rounds.\n")
    print("Place downloaded files at:  raw/<ISO3>/<ISO3>_<year>_wbes.dta")
    print("Then run:                   python wbes/02_harmonize.py\n")


def check_files(raw_dir: Path) -> None:
    """Show which .dta files are present vs missing."""
    print(f"\nChecking {raw_dir.resolve()} …\n")
    found, missing = [], []
    for iso3, years in COUNTRY_WAVES.items():
        for year in years:
            country_dir = raw_dir / iso3
            candidates = list(country_dir.glob(f"*{year}*.dta")) if country_dir.exists() else []
            target = f"raw/{iso3}/{iso3}_{year}_wbes.dta"
            if candidates:
                found.append((iso3, year, str(candidates[0])))
            else:
                missing.append((iso3, year, target))

    print(f"✓  FOUND  ({len(found)} waves):")
    for iso3, year, path in found:
        print(f"   {iso3} {year}  →  {path}")

    print(f"\n✗  MISSING ({len(missing)} waves):")
    for iso3, year, target in missing:
        name = COUNTRY_NAMES.get(iso3, iso3)
        print(f"   {iso3} {year}  →  {target}   [{name}]")

    pct = 100 * len(found) / max(len(found) + len(missing), 1)
    print(f"\nCoverage: {len(found)}/{len(found)+len(missing)} waves ({pct:.0f}%)\n")


def download_attempt(raw_dir: Path) -> None:
    """
    Attempt programmatic download via World Bank Microdata API.

    The WBES microdata API does not support unauthenticated bulk downloads.
    This function prints curl commands the user can run after logging in.
    """
    print("\nWorld Bank WBES does not support anonymous bulk download.")
    print("Instead, use the curl commands below after logging in to:")
    print(f"  {PORTAL_URL}\n")
    print("Step 1: Log in and copy your session cookie (_ga, _shibsession, etc.)")
    print("Step 2: Run the curl commands (replace COOKIE with your session cookie):\n")

    for iso3, years in list(COUNTRY_WAVES.items())[:5]:  # show first 5 as example
        for year in years:
            target = raw_dir / iso3 / f"{iso3}_{year}_wbes.dta"
            name   = COUNTRY_NAMES.get(iso3, iso3)
            print(f"# {name} {year}")
            print(f"mkdir -p raw/{iso3}")
            print(f'curl -b "COOKIE" -L '
                  f'"https://microdata.worldbank.org/index.php/catalog/SURVEY_ID/export/dta" '
                  f'-o "raw/{iso3}/{iso3}_{year}_wbes.dta"\n')

    print("(Replace SURVEY_ID with the numeric ID from the portal URL for each survey.)")
    print("\nRecommended: download manually from the portal in ~30 min for all 47 economies.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="WBES download helper for 47-country thesis pool"
    )
    parser.add_argument("--list",     action="store_true", help="List all surveys")
    parser.add_argument("--check",    action="store_true", help="Check downloaded files")
    parser.add_argument("--download", action="store_true", help="Show download commands")
    parser.add_argument("--raw-dir",  default="raw",       help="Raw data directory")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)

    if args.list:
        list_surveys()
    elif args.check:
        check_files(raw_dir)
    elif args.download:
        download_attempt(raw_dir)
    else:
        list_surveys()
        check_files(raw_dir)


if __name__ == "__main__":
    main()
