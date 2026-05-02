"""
R3 Phase 1 — Extensive-margin model: who becomes an exporter?

Addresses reviewer concern #3: "82% of firms have FSTS=0; quadratic OLS
estimated on the full sample is anchored by the domestic-vs-exporter
split, not by movement along the continuous FSTS range."

Two-part / hurdle architecture:
  Stage 1 (this script): Logit Pr(exporter=1 | TCI, DAI, controls)
  Stage 2 (11_intensive_margin.py): OLS on exporter subsample (FSTS > 0)

Specification:
  exporter ~ TCI + DAI + ln_empl + firm_age + foreign + C(broad_sector)

Outputs:
  outputs/r3/audit/extensive_margin.json   (params, AME, fit)
  outputs/r3/tables/T_extensive.tex        (Table 4 in revised manuscript)
  outputs/r3/audit/extensive_margin.txt    (statsmodels summary)
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

    df["fsts"] = df["d3c"] / 100.0
    df["exporter"] = (df["fsts"] > 0).astype(int)

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

    # Composites
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


def fit_logit(df):
    core = ["exporter", "TCI", "DAI", "ln_empl", "firm_age",
            "foreign", "broad_sector"]
    mask = df[core].notna().all(axis=1)
    formula = ("exporter ~ TCI + DAI + ln_empl + firm_age + foreign"
               " + C(broad_sector)")
    model = smf.logit(formula, data=df[mask]).fit(disp=False)
    n = int(mask.sum())
    n_exp = int(df.loc[mask, "exporter"].sum())
    return model, n, n_exp


def average_marginal_effects(model, df_clean):
    """Compute AME for each predictor. For Logit, dy/dx = phi(Xb) * beta."""
    Xb = model.fittedvalues
    p = 1 / (1 + np.exp(-Xb))
    weight = (p * (1 - p)).mean()
    ame = {}
    for term, beta in model.params.items():
        if term in ("Intercept",):
            continue
        ame[term] = float(beta * weight)
    return ame, float(weight)


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


def main():
    print("=" * 72)
    print("R3 Phase 1 — Stage 1: Extensive margin (Logit)")
    print("=" * 72)

    df = load_frame()
    print(f"\nFull sample: N = {len(df)}")
    print(f"Exporters (FSTS > 0): {df['exporter'].sum()} "
          f"({df['exporter'].mean()*100:.1f}%)")

    # Subsample after non-NA filter
    core = ["exporter", "TCI", "DAI", "ln_empl", "firm_age",
            "foreign", "broad_sector"]
    mask = df[core].notna().all(axis=1)
    n_clean = int(mask.sum())
    n_exp_clean = int(df.loc[mask, "exporter"].sum())
    print(f"After core-control filter: N = {n_clean}, "
          f"exporters = {n_exp_clean}")

    print("\n[1] Logit: exporter ~ TCI + DAI + controls + sector FE\n")
    model, n, n_exp = fit_logit(df)
    print(model.summary().as_text())

    # AME
    df_clean = df[mask].copy()
    ame, weight = average_marginal_effects(model, df_clean)

    payload = {
        "n": n,
        "n_exporters": n_exp,
        "n_domestic": n - n_exp,
        "pseudo_rsq": float(model.prsquared),
        "llf": float(model.llf),
        "ll_null": float(model.llnull),
        "lr_chi2": float(2 * (model.llf - model.llnull)),
        "lr_p": float(model.llr_pvalue),
        "params": {k: float(v) for k, v in model.params.items()},
        "bse": {k: float(v) for k, v in model.bse.items()},
        "pvalues": {k: float(v) for k, v in model.pvalues.items()},
        "odds_ratios": {k: float(np.exp(v)) for k, v in model.params.items()},
        "ame": ame,
        "ame_weight_phi": weight,
    }

    json_path = AUDIT_DIR / "extensive_margin.json"
    json_path.write_text(json.dumps(payload, indent=2))
    txt_path = AUDIT_DIR / "extensive_margin.txt"
    txt_path.write_text(model.summary().as_text())
    print(f"\nWrote: {json_path}")
    print(f"Wrote: {txt_path}")

    # ---- Build LaTeX-ish table ----
    print("\n" + "=" * 72)
    print("Table — Extensive margin (Stage 1, Logit)")
    print("=" * 72)
    rows = []
    label_map = {
        "TCI": "TCI (z)",
        "DAI": "DAI (z)",
        "ln_empl": "Firm size (ln)",
        "firm_age": "Firm age",
        "foreign": "Foreign-owned",
        "C(broad_sector)[T.manufacturing]": "Sector: manufacturing",
        "C(broad_sector)[T.retail_services]": "Sector: retail/services",
        "C(broad_sector)[T.construction]": "Sector: construction",
    }
    print(f"{'Variable':<28}{'β (logit)':>14}{'OR':>10}{'AME':>10}{'p':>10}")
    print("-" * 72)
    for term in label_map:
        if term not in model.params:
            continue
        beta = model.params[term]
        se = model.bse[term]
        p = model.pvalues[term]
        odds = np.exp(beta)
        a = ame.get(term, np.nan)
        sig = stars(p)
        rows.append({
            "label": label_map[term],
            "beta": beta, "se": se, "p": p, "or": odds, "ame": a,
        })
        print(f"{label_map[term]:<28}"
              f"{beta:>+9.3f}{sig:<5}"
              f"{odds:>10.3f}"
              f"{a:>+10.4f}"
              f"{p:>10.4f}")
    print("-" * 72)
    print(f"{'N':<28}{n:>14}")
    print(f"{'Exporters / Domestic':<28}{n_exp:>4} / {n - n_exp}")
    print(f"{'Pseudo R²':<28}{payload['pseudo_rsq']:>14.4f}")
    print(f"{'LR chi²':<28}{payload['lr_chi2']:>14.4f}")
    print(f"{'LR p-value':<28}{payload['lr_p']:>14.4f}")

    # LaTeX table
    tex = []
    tex.append("\\begin{table}[ht]")
    tex.append("\\centering")
    tex.append("\\caption{Extensive margin: probability of being an exporter "
               "(Logit, Stage 1 of two-part design)}")
    tex.append("\\label{tab:extensive}")
    tex.append("\\begin{tabular}{lrrrr}")
    tex.append("\\toprule")
    tex.append("Variable & $\\beta$ & OR & AME & $p$ \\\\")
    tex.append("\\midrule")
    for r in rows:
        tex.append(
            f"{r['label']} & "
            f"{r['beta']:+.3f}{stars(r['p'])} & "
            f"{r['or']:.3f} & "
            f"{r['ame']:+.4f} & "
            f"{r['p']:.3f} \\\\"
        )
    tex.append("\\midrule")
    tex.append(f"N & \\multicolumn{{4}}{{r}}{{{n} ({n_exp} exporters / "
               f"{n - n_exp} domestic)}} \\\\")
    tex.append(f"Pseudo $R^2$ & \\multicolumn{{4}}{{r}}"
               f"{{{payload['pseudo_rsq']:.4f}}} \\\\")
    tex.append(f"LR $\\chi^2$ ($p$) & \\multicolumn{{4}}{{r}}"
               f"{{{payload['lr_chi2']:.2f} ({payload['lr_p']:.3f})}} \\\\")
    tex.append("\\bottomrule")
    tex.append("\\end{tabular}")
    tex.append("\\par\\smallskip")
    tex.append("\\footnotesize Note: Sector fixed effects included. "
               "$\\dagger\\,p<.10$, $*\\,p<.05$, $**\\,p<.01$, "
               "$***\\,p<.001$.")
    tex.append("\\end{table}")
    tex_path = TABLES_DIR / "T_extensive.tex"
    tex_path.write_text("\n".join(tex))
    print(f"\nWrote: {tex_path}")


if __name__ == "__main__":
    main()
