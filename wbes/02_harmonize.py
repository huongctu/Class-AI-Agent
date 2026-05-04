"""
02_harmonize.py
Read 85 WBES .dta files (across 3 schema generations 2007-2025), harmonize to
common variable set, build pool.csv with one row per firm.

Variables extracted (canonical names):
- country_iso3, year_survey, icrv_regime
- sales (d2/d2x/n3), employees (l1/l11a/l10)
- fsts_pct = d3b + d3c (indirect + direct exports as % of sales)
- exporter dummy = (fsts_pct > 0)
- age = year_survey - b5
- fdi10 dummy = (b2b >= 10)
- innov_product (h1), innov_process (h2), rd_active (h8), iso_cert (b8), website (c22b)
- TCI = mean(rd_active, iso_cert)  [will add machinery in v3]
- DAI = website  [will add e-commerce, ERP, cloud from 2018+ schema in v3]
- is_sme = (employees < 100)
- log_labor_prod, log_employees
- empl_growth_3y from l1 vs l2

Encoding: tries default → latin1 → cp1252 → utf-8 progressively.

Usage:
    python3 01_inventory.py  # first
    python3 02_harmonize.py

Author: Đỗ Thùy Hương — CD1 pipeline.
"""
import pyreadstat, pandas as pd, numpy as np, json, warnings
from pathlib import Path
warnings.filterwarnings("ignore")

COUNTRY_CANON = {
    "afghanistan":"AFG","armenia":"ARM","bahrain":"BHR","bangladesh":"BGD",
    "bhutan":"BTN","bruneidarussalam":"BRN","cambodia":"KHM","cambodiainformal":"KHM",
    "china":"CHN","cyprus":"CYP","georgia":"GEO","hongkongsarchina":"HKG",
    "india":"IND","indonesia":"IDN","iraq":"IRQ","israel":"ISR","jordan":"JOR",
    "kazakhstan":"KAZ","korearepublic":"KOR","kyrgyzrepublic":"KGZ",
    "laoinformal":"LAO","laopdr":"LAO","laos":"LAO","malaysia":"MYS",
    "mongolia":"MNG","nepal":"NPL","pakistan":"PAK","philippines":"PHL",
    "republic_of_cyprus":"CYP","singapore":"SGP","srilanka":"LKA",
    "taiwanchina":"TWN","tajikistan":"TJK","thailand":"THA","timorleste":"TLS",
    "turkmenistan":"TKM","uzbekistan":"UZB","vanuatu":"VUT","vietnam":"VNM",
}

ICRV = {
    "SGP":"Advanced","KOR":"Advanced","HKG":"Advanced","TWN":"Advanced",
    "ISR":"Advanced","BHR":"Advanced","BRN":"Advanced","CYP":"Advanced",
    "CHN":"Upper-middle","MYS":"Upper-middle","THA":"Upper-middle",
    "KAZ":"Upper-middle","ARM":"Upper-middle","GEO":"Upper-middle",
    "VNM":"Emerging","IDN":"Emerging","PHL":"Emerging","IND":"Emerging",
    "LKA":"Emerging","JOR":"Emerging","MNG":"Emerging",
    "BGD":"Frontier","PAK":"Frontier","LAO":"Frontier","KHM":"Frontier",
    "NPL":"Frontier","BTN":"Frontier","UZB":"Frontier","TJK":"Frontier",
    "KGZ":"Frontier","TKM":"Frontier","AFG":"Frontier","TLS":"Frontier","IRQ":"Frontier",
    "VUT":"SIDS","FJI":"SIDS","WSM":"SIDS","TON":"SIDS","SLB":"SIDS","PNG":"SIDS",
}

# WBES missing-by-design codes
MISSING_CODES = {-9, -8, -7, -6, -5, -4, -3, -2, -1}

def num(x):
    if pd.isna(x): return np.nan
    try:
        v = float(x)
        return np.nan if v in MISSING_CODES else v
    except: return np.nan

def safe_col(df, candidates):
    for c in candidates:
        if c in df.columns: return df[c].apply(num)
    return pd.Series([np.nan]*len(df))

def safe_dummy(df, candidates):
    """WBES dummy: 1=yes, 2=no. Return 0/1 with NaN for missing."""
    for c in candidates:
        if c in df.columns:
            v = df[c].apply(num)
            return (v == 1).astype(float).where(~v.isna())
    return pd.Series([np.nan]*len(df))

def read_dta_safe(path):
    """Try encodings progressively."""
    for enc in [None, "latin1", "cp1252", "utf-8"]:
        try:
            kw = {} if enc is None else {"encoding": enc}
            df, meta = pyreadstat.read_dta(path, **kw)
            return df, meta
        except Exception:
            continue
    return None, None

def main():
    with open("/tmp/wbes/manifest.json") as fh:
        manifest = json.load(fh)
    records = []
    errors = []
    ok = 0
    for entry in manifest:
        cnt_raw = entry["country"].lower().rstrip("_").rstrip("-")
        iso = COUNTRY_CANON.get(cnt_raw)
        if not iso:
            errors.append(("unknown_country", cnt_raw)); continue
        year = int(entry["year"])
        path = entry["path"]
        df, meta = read_dta_safe(path)
        if df is None or len(df) < 50:
            errors.append(("read_fail_or_too_small", Path(path).name)); continue
        try:
            sales = safe_col(df, ["d2","d2x","n3"])
            employees = safe_col(df, ["l1","l11a","l10"])
            # CORRECT FSTS = d3b (indirect) + d3c (direct exports)
            d3b = safe_col(df, ["d3b"]).fillna(0)
            d3c = safe_col(df, ["d3c"]).fillna(0)
            fsts = (d3b + d3c).clip(0, 100)
            fsts_na = safe_col(df, ["d3b"]).isna() & safe_col(df, ["d3c"]).isna()
            fsts = fsts.where(~fsts_na)

            b5 = safe_col(df, ["b5"]); age = (year - b5).where(b5 > 1900)
            b2b = safe_col(df, ["b2b"])
            fdi10 = (b2b >= 10).astype(float).where(~b2b.isna())
            h1 = safe_dummy(df, ["h1"]); h2 = safe_dummy(df, ["h2"])
            h8 = safe_dummy(df, ["h8"]); b8 = safe_dummy(df, ["b8"])
            c22b = safe_dummy(df, ["c22b"])
            a6a = safe_col(df, ["a6a"])
            sector = (df["stratificationsectorcode"] if "stratificationsectorcode" in df.columns
                      else (df["stra_sector"] if "stra_sector" in df.columns
                            else pd.Series([np.nan]*len(df))))
            l2 = safe_col(df, ["l2"])

            rec = pd.DataFrame({
                "country_iso3": iso, "year_survey": year,
                "icrv_regime": ICRV.get(iso, "Other"),
                "sales": sales, "employees": employees,
                "fsts_pct": fsts,
                "exporter": (fsts > 0).astype(float).where(~fsts.isna()),
                "age": age, "fdi10": fdi10,
                "innov_product": h1, "innov_process": h2,
                "rd_active": h8, "iso_cert": b8, "website": c22b,
                "sector_code": sector, "size_strat": a6a,
                "empl_3y_ago": l2,
            })
            rec["labor_prod"] = rec["sales"] / rec["employees"]
            rec["log_labor_prod"] = np.log(rec["labor_prod"].where(rec["labor_prod"] > 0))
            rec["log_employees"] = np.log(rec["employees"].where(rec["employees"] > 0))
            rec["empl_growth_3y"] = ((rec["employees"]/rec["empl_3y_ago"])**(1/3) - 1) * 100
            rec["empl_growth_3y"] = rec["empl_growth_3y"].where(
                (rec["employees"] > 0) & (rec["empl_3y_ago"] > 0) &
                (rec["empl_growth_3y"].abs() < 100))
            rec["is_sme"] = (rec["employees"] < 100).astype(float).where(~rec["employees"].isna())
            rec["TCI"] = rec[["rd_active","iso_cert"]].mean(axis=1)
            rec["DAI"] = rec[["website"]].mean(axis=1)
            records.append(rec); ok += 1
        except Exception as e:
            errors.append(("processing", f"{Path(path).name}: {e}"))

    pool = pd.concat(records, ignore_index=True)
    out = Path("/tmp/wbes/pool.csv")
    pool.to_csv(out, index=False)

    print(f"OK files: {ok} / {len(manifest)}")
    print(f"Pool: {len(pool):,} rows")
    print(f"Distinct country-year units: {pool.groupby(['country_iso3','year_survey']).ngroups}")
    print(f"Distinct countries (ISO3): {pool['country_iso3'].nunique()}")
    print(f"\nICRV regime distribution:")
    print(pool["icrv_regime"].value_counts().to_string())
    print(f"\nErrors: {len(errors)}")
    return pool, errors

if __name__ == "__main__":
    main()
