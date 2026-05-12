"""
fetch_macro_indicators.py
================================================================================
Fetch macro indicators (WGI Rule of Law, WDI GDP per capita PPP, FDI inflows %GDP)
from World Bank Data360 API for 47 Asian + Pacific countries × years 2009-2025.

Output: wbes/macro/macro_indicators_long.csv (long format)
        wbes/macro/macro_indicators_wide.csv (wide format, country-year)

Usage (run locally on a machine with internet):
    pip install requests pandas
    python3 wbes/fetch_macro_indicators.py

Then merge with pool:
    python3 wbes/merge_macro_with_pool.py

Author: Đỗ Thùy Hương — CD2 macro pipeline.
"""
import requests
import pandas as pd
import time
from pathlib import Path

ISO_CODES = ["AFG","ARM","BGD","BHR","BRN","BTN","CHN","CYP","FJI","GEO","HKG","IDN",
             "IND","IRQ","ISR","JOR","KAZ","KGZ","KHM","KOR","KWT","LAO","LBN","LKA",
             "MDV","MMR","MNG","MYS","NPL","PAK","PHL","PNG","QAT","SAU","SGP","SLB",
             "THA","TJK","TKM","TLS","TON","TWN","UZB","VNM","VUT","WSM","YEM"]

INDICATORS = {
    # WGI (Worldwide Governance Indicators) - z-scores from -2.5 to 2.5
    "RL.EST":           ("WB_WGI", "WGI Rule of Law"),
    "GE.EST":           ("WB_WGI", "WGI Government Effectiveness"),
    "RQ.EST":           ("WB_WGI", "WGI Regulatory Quality"),
    "CC.EST":           ("WB_WGI", "WGI Control of Corruption"),
    # WDI macro economic
    "NY.GDP.PCAP.PP.KD":   ("WB_WDI", "GDP per capita PPP (constant 2017 USD)"),
    "NY.GDP.MKTP.KD.ZG":   ("WB_WDI", "GDP growth (%)"),
    "BX.KLT.DINV.WD.GD.ZS":("WB_WDI", "FDI net inflows (% of GDP)"),
    "NE.EXP.GNFS.ZS":      ("WB_WDI", "Exports of goods and services (% of GDP)"),
    "FP.CPI.TOTL.ZG":      ("WB_WDI", "Inflation, consumer prices (annual %)"),
    # ITU Digital Hub
    "IT.NET.USER.ZS":      ("WB_WDI", "Internet users (% of population)"),
}

def fetch_wb_legacy(indicator, country, year_from=2009, year_to=2025):
    """Use World Bank legacy Open API."""
    url = (f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"
           f"?date={year_from}:{year_to}&format=json&per_page=200")
    try:
        r = requests.get(url, timeout=15, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        data = r.json()
        if len(data) > 1 and data[1]:
            return data[1]
    except Exception as e:
        print(f"    ERROR {indicator}/{country}: {e}")
    return []

def fetch_data360(indicator, database_id, year_from=2009, year_to=2025):
    """Use Data360 API (https://data360api.worldbank.org)."""
    url = "https://data360api.worldbank.org/data360/data"
    rows = []
    for skip in range(0, 10000, 1000):
        params = {
            "DATABASE_ID": database_id,
            "INDICATOR": f"{database_id}_{indicator.replace('.', '_')}",
            "timePeriodFrom": str(year_from),
            "timePeriodTo": str(year_to),
            "skip": str(skip),
        }
        try:
            r = requests.get(url, params=params, timeout=30,
                            headers={"User-Agent": "Mozilla/5.0"})
            r.raise_for_status()
            data = r.json()
            batch = data.get("value", [])
            count = data.get("count", 0)
            rows.extend(batch)
            if len(batch) < 1000 or skip + 1000 >= count:
                break
            time.sleep(0.5)
        except Exception as e:
            print(f"    ERROR {indicator} skip={skip}: {e}")
            break
    return rows

def main():
    out_dir = Path("wbes/macro")
    out_dir.mkdir(parents=True, exist_ok=True)
    all_rows = []

    print("Fetching from World Bank legacy API (preferred):")
    for indicator, (db, label) in INDICATORS.items():
        print(f"\n[{indicator}] {label}")
        for iso in ISO_CODES:
            obs = fetch_wb_legacy(indicator, iso)
            for o in obs:
                if o.get("value") is not None:
                    all_rows.append({
                        "country_iso3": iso,
                        "year": int(o["date"]),
                        "indicator": indicator,
                        "value": float(o["value"]),
                        "label": label,
                    })
            time.sleep(0.1)
        print(f"  Cumulative rows: {len(all_rows)}")

    if not all_rows:
        print("\nLegacy API failed; trying Data360...")
        for indicator, (db, label) in INDICATORS.items():
            obs = fetch_data360(indicator, db)
            for r in obs:
                if r.get("REF_AREA") in ISO_CODES and r.get("OBS_VALUE") is not None:
                    all_rows.append({
                        "country_iso3": r["REF_AREA"],
                        "year": int(r["TIME_PERIOD"]),
                        "indicator": indicator,
                        "value": float(r["OBS_VALUE"]),
                        "label": label,
                    })

    if all_rows:
        df = pd.DataFrame(all_rows)
        df.to_csv(out_dir / "macro_indicators_long.csv", index=False)
        # Wide format
        wide = df.pivot_table(index=["country_iso3","year"],
                              columns="indicator", values="value", aggfunc="first")
        wide.reset_index().to_csv(out_dir / "macro_indicators_wide.csv", index=False)
        print(f"\nSaved {len(df)} long rows → macro_indicators_long.csv")
        print(f"Saved {len(wide)} country-year pairs → macro_indicators_wide.csv")
        print(f"\nIndicators fetched: {df['indicator'].nunique()}")
        print(f"Countries: {df['country_iso3'].nunique()}")
        print(f"Years: {df['year'].min()}–{df['year'].max()}")
    else:
        print("\nERROR: Could not fetch any data. Check internet connection or API endpoints.")

if __name__ == "__main__":
    main()
