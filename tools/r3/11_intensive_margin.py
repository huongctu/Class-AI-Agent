"""
R3 Phase 1 — Stage 2: Intensive margin (OLS on exporter subsample).

Within the exporter subsample (FSTS > 0, N=84 after controls), re-estimate
M2 / M5 / M8 to test how productivity moves with the *intensive* margin
of FSTS — addressing reviewer concern #3 directly.

Specifications:
  M2': ln_lp ~ fsts_c + fsts_c2 + controls
  M5': add TCI
  M8': add DAI + DAI×FSTS + DAI×FSTS²

FSTS centering is recomputed *within the exporter subsample* (mean of
exporter FSTS only) so the polynomial is anchored on the intensive
distribution rather than on the full-sample mean (which is dominated
by the 82% domestic firms with FSTS=0).

Outputs:
  outputs/r3/audit/intensive_margin.json   (3 model specs)
  outputs/r3/tables/T_intensive.tex        (revised Table 2-equivalent)
  outputs/r3/audit/intensive_margin.txt    (statsmodels summaries)
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.formula.api as smf

REPO = Path(__file__).resolve().parents[2]
DTA = REPO / "data" / "raw" / "Singapore2023fulldata.dta"
AUDIT_DIR = REPO / "outputs" / "r3" / "audit"
TABLES_DIR = REPO / "outputs" / "r3" / "tables"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)
TABLES_DIR.mkdir(parents=True, exist_ok=True)


def load_frame():
    df, _ = pyreadstat.read_dta(str(DTA))
    for col in ["b2b", "d2", "l1", "b5", "d3c", "a4a", "a4b_v4"]:
        df[col] = df[col].where(df[col] >= 0, np.nan)
    for col in ["b8", "e6", "h1", "h8"]:
        df[col + "_yn"] = (df[col] == 1).astype(int)
    df["c22b_yn"] = (df["c22b"] == 1).astype(int)
    df["dai_drop"] = (df["k33"] < 0) & (df["k38"] < 0)
    k33_med = df.loc[df["k33"] >= 0, "k33"].median()
    k38_med = df.loc[df["k38"] >= 0, "k38"].median()
    df["k33_imp"] = df["k33"].where(df["k33"] >= 0, k33_med)
    df["k38_imp"] = df["k38"].where(df["k38"] >= 0, k38_med)
    df.loc[df["dai_drop"], ["k33_imp", "k38_imp"]] = np.nan

    df["lp"] = df["d2"] / df["l1"]
    df["ln_lp"] = np.log(df["lp"])
    lo, hi = df["ln_lp"].quantile([0.01, 0.99])
    df["ln_lp"] = df["ln_lp"].clip(lo, hi)

    df["fsts"] = df["d3c"] / 100.0
    df["ln_empl"] = np.log(df["l1"])
    df["firm_age"] = 2023 - df["b5"]
    df["foreign"] = (df["b2b"].fillna(0) >= 10).astype(int)

    def bucket(nace):
        if pd.isna(nace):
            return np.nan
        n = int(nace)
        if 10 <= n <= 33:
            return "manufacturing"
        if 41 <= n <= 43:
            return "construction"
        return "retail_services"

    df["broad_sector"] = df["a4b_v4"].apply(bucket)

    def composite(parts, name):
        zs = []
        for c in parts:
            mu, sd = df[c].mean(), df[c].std()
            zcol = c + "_z_" + name
            df[zcol] = (df[c] - mu) / sd
            zs.append(zcol)
        raw = df[zs].sum(axis=1, skipna=False) / len(parts)
        df[name] = (raw - raw.mean()) / raw.std()

    composite(["b8_yn", "e6_yn", "h1_yn", "h8_yn"], "TCI")
    composite(["c22b_yn", "k33_imp", "k38_imp"], "DAI")
    return df


def stars(p):
    if p < 0.001:
        return "***"
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    if p < 0.10:
        return "†"
    return ""


def fit_specs(df_int):
    """Fit M2', M5', M8' on the exporter subsample with within-subsample centering."""
    fsts_mean_int = df_int["fsts"].mean()
    df_int = df_int.copy()
    df_int["fsts_c"] = df_int["fsts"] - fsts_mean_int
    df_int["fsts_c2"] = df_int["fsts_c"] ** 2
    df_int["fsts_c_DAI"] = df_int["fsts_c"] * df_int["DAI"]
    df_int["fsts_c2_DAI"] = df_int["fsts_c2"] * df_int["DAI"]

    ctrl = "ln_empl + firm_age + foreign + C(broad_sector)"
    spec_m2 = f"ln_lp ~ fsts_c + fsts_c2 + {ctrl}"
    spec_m5 = f"ln_lp ~ fsts_c + fsts_c2 + TCI + {ctrl}"
    spec_m8 = (f"ln_lp ~ fsts_c + fsts_c2 + TCI + DAI"
               f" + fsts_c_DAI + fsts_c2_DAI + {ctrl}")

    m2 = smf.ols(spec_m2, data=df_int).fit(cov_type="HC1")
    m5 = smf.ols(spec_m5, data=df_int).fit(cov_type="HC1")
    m8 = smf.ols(spec_m8, data=df_int).fit(cov_type="HC1")
    return {"M2": m2, "M5": m5, "M8": m8}, fsts_mean_int


def serialize(model, name):
    return {
        "label": name,
        "n": int(model.nobs),
        "rsquared": float(model.rsquared),
        "rsquared_adj": float(model.rsquared_adj),
        "fvalue": float(model.fvalue),
        "f_pvalue": float(model.f_pvalue),
        "params": {k: float(v) for k, v in model.params.items()},
        "bse": {k: float(v) for k, v in model.bse.items()},
        "pvalues": {k: float(v) for k, v in model.pvalues.items()},
    }


def main():
    print("=" * 72)
    print("R3 Phase 1 — Stage 2: Intensive margin (OLS on exporters)")
    print("=" * 72)

    df = load_frame()
    core = ["ln_lp", "fsts", "TCI", "DAI",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    mask_core = df[core].notna().all(axis=1)
    mask_int = mask_core & (df["fsts"] > 0)
    df_int = df[mask_int].copy()

    print(f"\nFull sample (after core filter):  N = {mask_core.sum()}")
    print(f"Intensive sample (FSTS > 0):      N = {len(df_int)}")
    print(f"FSTS distribution within intensive sample:")
    print(f"  mean = {df_int['fsts'].mean():.3f}")
    for q in (.25, .5, .75, .9, .95, .99, 1.0):
        v = df_int["fsts"].quantile(q)
        print(f"  P{int(q*100):>3} = {v:.3f}")

    models, fsts_mean_int = fit_specs(df_int)

    payload = {
        "n_intensive": len(df_int),
        "fsts_mean_intensive": fsts_mean_int,
        "models": {k: serialize(m, k + "_intensive") for k, m in models.items()},
    }

    json_path = AUDIT_DIR / "intensive_margin.json"
    json_path.write_text(json.dumps(payload, indent=2))
    print(f"\nWrote: {json_path}")

    txt_path = AUDIT_DIR / "intensive_margin.txt"
    txt_path.write_text("\n\n".join(m.summary().as_text()
                                    for m in models.values()))
    print(f"Wrote: {txt_path}")

    # ---- Side-by-side comparison: full vs intensive ----
    print("\n" + "=" * 80)
    print("Intensive-margin OLS (FSTS > 0, N={})".format(len(df_int)))
    print("=" * 80)
    print(f"{'Variable':<22}{'M2 (intensive)':>16}{'M5 (intensive)':>16}"
          f"{'M8 (intensive)':>16}")
    print("-" * 80)

    var_labels = [
        ("FSTS",         "fsts_c"),
        ("FSTS²",        "fsts_c2"),
        ("TCI (z)",      "TCI"),
        ("DAI (z)",      "DAI"),
        ("FSTS × DAI",   "fsts_c_DAI"),
        ("FSTS² × DAI",  "fsts_c2_DAI"),
        ("Firm size (ln)", "ln_empl"),
        ("Firm age",       "firm_age"),
        ("Foreign-owned",  "foreign"),
    ]
    rows = []
    for label, term in var_labels:
        line = f"{label:<22}"
        row = {"label": label}
        for k in ("M2", "M5", "M8"):
            m = models[k]
            if term in m.params.index:
                b = m.params[term]
                p = m.pvalues[term]
                cell = f"{b:+.3f}{stars(p)}"
                row[k] = {"beta": float(b), "p": float(p)}
            else:
                cell = ""
                row[k] = None
            line += f"{cell:>16}"
        rows.append(row)
        print(line)

    print("-" * 80)
    print(f"{'N':<22}"
          + "".join(f"{int(models[k].nobs):>16}" for k in ("M2", "M5", "M8")))
    print(f"{'R²':<22}"
          + "".join(f"{models[k].rsquared:>16.4f}" for k in ("M2", "M5", "M8")))
    print(f"{'Adj. R²':<22}"
          + "".join(f"{models[k].rsquared_adj:>16.4f}" for k in ("M2", "M5", "M8")))

    # Joint F-test for DAI moderation in M8 intensive
    m8 = models["M8"]
    fwald = m8.f_test("fsts_c_DAI = 0, fsts_c2_DAI = 0")
    print(f"\nM8 intensive: joint F-test (DAI moderation) F = "
          f"{fwald.fvalue:.3f}, p = {fwald.pvalue:.4f}")

    # Lind-Mehlum on M2 intensive
    from scipy.stats import norm
    b1, b2 = m8.params["fsts_c"], m8.params["fsts_c2"]
    fsts_min = df_int["fsts"].min() - fsts_mean_int
    fsts_max = df_int["fsts"].max() - fsts_mean_int
    slope_min = b1 + 2 * b2 * fsts_min
    slope_max = b1 + 2 * b2 * fsts_max
    cov = m8.cov_params()
    var_min = (cov.loc["fsts_c", "fsts_c"]
               + 4 * fsts_min**2 * cov.loc["fsts_c2", "fsts_c2"]
               + 4 * fsts_min * cov.loc["fsts_c", "fsts_c2"])
    var_max = (cov.loc["fsts_c", "fsts_c"]
               + 4 * fsts_max**2 * cov.loc["fsts_c2", "fsts_c2"]
               + 4 * fsts_max * cov.loc["fsts_c", "fsts_c2"])
    t_min = slope_min / np.sqrt(var_min)
    t_max = slope_max / np.sqrt(var_max)
    p_lm = max(1 - norm.cdf(t_min), norm.cdf(t_max))
    print(f"\nLind-Mehlum U-test on M8 intensive (within exporters):")
    print(f"  Slope at FSTS_min: {slope_min:.3f}, t = {t_min:+.3f}")
    print(f"  Slope at FSTS_max: {slope_max:.3f}, t = {t_max:+.3f}")
    print(f"  Lind-Mehlum p     = {p_lm:.4f}")

    # Turning point (intensive)
    if abs(b2) > 1e-9:
        tp_centered = -b1 / (2 * b2)
        tp_pct = (tp_centered + fsts_mean_int) * 100
        print(f"  Turning point    = {tp_pct:.2f}% (FSTS scale)")

    # ---- LaTeX table ----
    tex = []
    tex.append("\\begin{table}[ht]")
    tex.append("\\centering")
    tex.append("\\caption{Intensive margin: ln(labor productivity) on the "
               f"exporter subsample (FSTS $>$ 0, $N={len(df_int)}$). "
               "HC1 robust SE.}")
    tex.append("\\label{tab:intensive}")
    tex.append("\\begin{tabular}{lrrr}")
    tex.append("\\toprule")
    tex.append(" & M2 (intensive) & M5 (intensive) & M8 (intensive) \\\\")
    tex.append("\\midrule")
    for r in rows:
        cells = []
        for k in ("M2", "M5", "M8"):
            v = r[k]
            if v is None:
                cells.append("")
            else:
                cells.append(f"{v['beta']:+.3f}{stars(v['p'])}")
        tex.append(f"{r['label']} & " + " & ".join(cells) + " \\\\")
    tex.append("\\midrule")
    tex.append(f"$N$ & "
               + " & ".join(str(int(models[k].nobs)) for k in ("M2", "M5", "M8"))
               + " \\\\")
    tex.append(f"$R^2$ & "
               + " & ".join(f"{models[k].rsquared:.3f}"
                            for k in ("M2", "M5", "M8")) + " \\\\")
    tex.append(f"Adj.\\,$R^2$ & "
               + " & ".join(f"{models[k].rsquared_adj:.3f}"
                            for k in ("M2", "M5", "M8")) + " \\\\")
    tex.append("\\bottomrule")
    tex.append("\\end{tabular}")
    tex.append("\\par\\smallskip")
    tex.append("\\footnotesize Note: FSTS centered at intensive-subsample mean. "
               "Sector fixed effects included. "
               "$\\dagger\\,p<.10$, $*\\,p<.05$, $**\\,p<.01$, $***\\,p<.001$.")
    tex.append("\\end{table}")
    tex_path = TABLES_DIR / "T_intensive.tex"
    tex_path.write_text("\n".join(tex))
    print(f"\nWrote: {tex_path}")


if __name__ == "__main__":
    main()
