"""
03_describe.py
Compute all descriptive tables for Chuyên đề 1 Chapters 4–6 from pool.csv.

Outputs (CSV) saved to /tmp/wbes/output/:
- Bang_4_1_Dispersion.csv: within-country productivity dispersion by regime
- Bang_4_3_Growth.csv: employment growth, FSTS, exporter share by regime
- Bang_4_4_Innovation.csv: R&D, ISO, website, innovation by regime
- Bang_4_5_Structure.csv: SME, exporter, FDI by regime
- Bang_4_6_Period_Delta.csv: Δ percentage points 2018-2024 vs 2007-2012
- Bang_5_1_Four_archetypes.csv: SGP, VNM, CHN, EmAsia composite
- Bang_6_1_Correlation.csv: bivariate correlations with log labor productivity
- Phu_luc_A_Coverage.csv: country-year coverage of pool

Usage:
    python3 02_harmonize.py  # first
    python3 03_describe.py

Author: Đỗ Thùy Hương — CD1 pipeline.
"""
import pandas as pd, numpy as np
from pathlib import Path
pd.set_option("display.float_format", "{:.3f}".format)

OUT = Path("/tmp/wbes/output"); OUT.mkdir(parents=True, exist_ok=True)
ORDER = ["Advanced","Upper-middle","Emerging","Frontier","SIDS"]

pool = pd.read_csv("/tmp/wbes/pool.csv", low_memory=False)
print(f"Loaded pool: {len(pool):,} rows × {pool.shape[1]} cols")

# Within-country winsorize log labor productivity
def winsor(s, lo=0.01, hi=0.99):
    if s.notna().sum() < 20: return s
    a, b = s.quantile([lo, hi]); return s.clip(a, b)
pool["log_lp_w"] = pool.groupby(["country_iso3","year_survey"])["log_labor_prod"].transform(winsor)

# === BẢNG 4.1: Productivity dispersion (per-country, regime-averaged) ===
def cy_dispersion(g):
    s = g.dropna()
    if len(s) < 30: return None
    p10, p25, p75, p90 = s.quantile([.10,.25,.75,.90])
    return pd.Series({"sd_log": s.std(),
                      "p90_p10_ratio": np.exp(p90 - p10),
                      "p75_p25_ratio": np.exp(p75 - p25),
                      "n_firms": len(s)})

cy = pool.groupby(["country_iso3","year_survey"])["log_lp_w"].apply(cy_dispersion).unstack()
cy = cy.reset_index().merge(
    pool[["country_iso3","icrv_regime"]].drop_duplicates(),
    on="country_iso3", how="left")

def wavg(g, col, w="n_firms"):
    g = g.dropna(subset=[col, w])
    if g[w].sum() == 0: return np.nan
    return (g[col] * g[w]).sum() / g[w].sum()

tbl41 = cy.groupby("icrv_regime").apply(lambda g: pd.Series({
    "n_country_years": len(g.dropna(subset=["sd_log"])),
    "n_firms": g["n_firms"].sum(),
    "sd_log_w": wavg(g, "sd_log"),
    "p90_p10_w": wavg(g, "p90_p10_ratio"),
    "p75_p25_w": wavg(g, "p75_p25_ratio"),
})).reindex(ORDER)
print("\n=== BẢNG 4.1: Productivity dispersion ===")
print(tbl41.round(2))
tbl41.to_csv(OUT / "Bang_4_1_Dispersion.csv")

# === BẢNG 4.3: Growth, FSTS, exporter ===
tbl43 = pool.groupby("icrv_regime").agg(
    empl_growth_pa=("empl_growth_3y","mean"),
    fsts_mean=("fsts_pct","mean"),
    fsts_median=("fsts_pct","median"),
    exporter_share=("exporter","mean"),
).reindex(ORDER)
tbl43["exporter_share"] *= 100
print("\n=== BẢNG 4.3: Growth + Internationalization ===")
print(tbl43.round(2))
tbl43.to_csv(OUT / "Bang_4_3_Growth.csv")

# === BẢNG 4.4: Innovation ===
tbl44 = (pool.groupby("icrv_regime")[["innov_product","innov_process","rd_active","iso_cert","website"]]
         .mean() * 100).reindex(ORDER)
print("\n=== BẢNG 4.4: Innovation (% of firms) ===")
print(tbl44.round(1))
tbl44.to_csv(OUT / "Bang_4_4_Innovation.csv")

# === BẢNG 4.5: Structure ===
tbl45 = (pool.groupby("icrv_regime")[["is_sme","exporter","fdi10"]]
         .mean() * 100).reindex(ORDER)
tbl45.columns = ["SME (<100 LĐ)","Exporter (>0%)","FDI ≥10%"]
print("\n=== BẢNG 4.5: Structure (%) ===")
print(tbl45.round(1))
tbl45.to_csv(OUT / "Bang_4_5_Structure.csv")

# === BẢNG 4.6: Period delta ===
pool["period"] = pd.cut(pool["year_survey"], bins=[2006,2012,2017,2025],
                        labels=["2007-2012","2013-2017","2018-2024"])
metrics = ["website","exporter","fdi10","rd_active","iso_cert","innov_product"]
period_means = pool.groupby(["icrv_regime","period"], observed=False)[metrics].mean().mul(100).unstack(level=1)
period_means = period_means.reindex(ORDER)
deltas = pd.DataFrame(index=ORDER)
for k in metrics:
    p1 = period_means[(k, "2007-2012")]
    p3 = period_means[(k, "2018-2024")]
    deltas[f"Δ {k}"] = p3 - p1
print("\n=== BẢNG 4.6: Δ pp 2018-2024 vs 2007-2012 ===")
print(deltas.round(1))
deltas.to_csv(OUT / "Bang_4_6_Period_Delta.csv")

# === BẢNG 5.1: Four archetypes ===
focus = ["SGP","VNM","CHN"]
rows = []
for c in focus:
    sub = pool[pool["country_iso3"]==c]
    rows.append({
        "label": c, "n_firms": len(sub),
        "country_years": sub["year_survey"].nunique(),
        "fsts_mean": sub["fsts_pct"].mean(),
        "exporter_pct": sub["exporter"].mean()*100,
        "rd_active_pct": sub["rd_active"].mean()*100,
        "innov_product_pct": sub["innov_product"].mean()*100,
        "website_pct": sub["website"].mean()*100,
        "iso_cert_pct": sub["iso_cert"].mean()*100,
        "fdi10_pct": sub["fdi10"].mean()*100,
        "sme_pct": sub["is_sme"].mean()*100,
        "log_prod_sd": sub["log_lp_w"].std(),
        "p90_p10": np.exp(sub["log_lp_w"].quantile(0.9) - sub["log_lp_w"].quantile(0.1)),
    })
em = pool[pool["country_iso3"].isin(["IDN","PHL","IND","BGD"])]
rows.append({
    "label":"EmAsia(IDN+PHL+IND+BGD)", "n_firms":len(em),
    "country_years": em.groupby(["country_iso3","year_survey"]).ngroups,
    "fsts_mean": em["fsts_pct"].mean(),
    "exporter_pct": em["exporter"].mean()*100,
    "rd_active_pct": em["rd_active"].mean()*100,
    "innov_product_pct": em["innov_product"].mean()*100,
    "website_pct": em["website"].mean()*100,
    "iso_cert_pct": em["iso_cert"].mean()*100,
    "fdi10_pct": em["fdi10"].mean()*100,
    "sme_pct": em["is_sme"].mean()*100,
    "log_prod_sd": em["log_lp_w"].std(),
    "p90_p10": np.exp(em["log_lp_w"].quantile(0.9) - em["log_lp_w"].quantile(0.1)),
})
tbl51 = pd.DataFrame(rows).set_index("label")
print("\n=== BẢNG 5.1: Four archetypes ===")
print(tbl51.round(2))
tbl51.to_csv(OUT / "Bang_5_1_Four_archetypes.csv")

# === BẢNG 6.1: Correlations ===
corr_vars = ["log_employees","age","fdi10","fsts_pct","TCI","DAI"]
rows = []
for r in ORDER:
    sub = pool[pool["icrv_regime"]==r]
    row = {"icrv_regime": r, "n": len(sub)}
    for v in corr_vars:
        valid = sub[["log_lp_w", v]].dropna()
        row[v] = valid["log_lp_w"].corr(valid[v]) if len(valid) >= 30 else np.nan
    rows.append(row)
tbl61 = pd.DataFrame(rows).set_index("icrv_regime")
print("\n=== BẢNG 6.1: Pearson correlations with log labor productivity ===")
print(tbl61.round(3))
tbl61.to_csv(OUT / "Bang_6_1_Correlation.csv")

# === Phụ lục A: country-year coverage ===
cov = (pool.groupby(["icrv_regime","country_iso3"])
       .agg(years=("year_survey", lambda x: ",".join(map(str, sorted(set(x))))),
            n_firms=("country_iso3","count"))
       .reset_index().sort_values(["icrv_regime","country_iso3"]))
cov.to_csv(OUT / "Phu_luc_A_Coverage.csv", index=False)
print("\n=== Phụ lục A: country-year coverage saved ===")

print(f"\nAll tables saved to {OUT}/")
