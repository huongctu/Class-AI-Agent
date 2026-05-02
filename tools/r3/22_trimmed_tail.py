"""
R3 Phase 2 — Trimmed-tail re-estimation of canonical M8.

Reviewer #4 demanded: "trimmed-tail or leave-one-out re-estimation" so
readers can determine whether the DAI moderation result is driven by a
handful of high-intensity exporters in the sparse upper tail.

Re-fit canonical M8 after dropping firms above each of these FSTS cutoffs:
  drop FSTS > 95  (drops top ~1%)
  drop FSTS > 90  (drops top ~1%)
  drop FSTS > 80  (drops top ~3%)
  drop FSTS > 70  (drops top ~3%)
  drop FSTS > 50  (drops top ~5%)

For each cutoff, report:
  - N retained
  - Coefficient and p for fsts_c2, fsts_c_DAI, fsts_c2_DAI
  - Joint F-test for DAI moderation
  - Adjusted R²

If the DAI moderation evaporates by FSTS-cutoff 70, the contribution
claim relies on a thin tail. If it survives at cutoff 80 or below, the
claim is robust to the empirical-leverage concern.

Outputs:
  outputs/r3/tables/T_trimmed_tail.tex
  outputs/r3/audit/trimmed_tail.json
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


def load_clean():
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


def fit_with_cutoff(df, cutoff_pct=None):
    """Fit M8 after dropping firms with fsts > cutoff_pct/100. Re-center
    fsts within the retained sample so the polynomial is anchored on the
    retained distribution."""
    if cutoff_pct is None:
        sub = df.copy()
        label = "Full"
    else:
        sub = df[df["fsts"] <= cutoff_pct / 100].copy()
        label = f"≤{cutoff_pct}%"
    sub["fsts_c"] = sub["fsts"] - sub["fsts"].mean()
    sub["fsts_c2"] = sub["fsts_c"] ** 2
    sub["fsts_c_DAI"] = sub["fsts_c"] * sub["DAI"]
    sub["fsts_c2_DAI"] = sub["fsts_c2"] * sub["DAI"]
    core = ["ln_lp", "fsts_c", "fsts_c2", "TCI", "DAI",
            "fsts_c_DAI", "fsts_c2_DAI",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    mask = sub[core].notna().all(axis=1)
    formula = (
        "ln_lp ~ fsts_c + fsts_c2 + TCI + DAI"
        " + fsts_c_DAI + fsts_c2_DAI"
        " + ln_empl + firm_age + foreign + C(broad_sector)"
    )
    model = smf.ols(formula, data=sub[mask]).fit(cov_type="HC1")
    fwald = model.f_test("fsts_c_DAI = 0, fsts_c2_DAI = 0")
    return {
        "label": label,
        "n": int(mask.sum()),
        "TCI": float(model.params["TCI"]),
        "TCI_p": float(model.pvalues["TCI"]),
        "fsts_c2": float(model.params["fsts_c2"]),
        "fsts_c2_p": float(model.pvalues["fsts_c2"]),
        "fsts_c_DAI": float(model.params["fsts_c_DAI"]),
        "fsts_c_DAI_p": float(model.pvalues["fsts_c_DAI"]),
        "fsts_c2_DAI": float(model.params["fsts_c2_DAI"]),
        "fsts_c2_DAI_p": float(model.pvalues["fsts_c2_DAI"]),
        "joint_F": float(fwald.fvalue),
        "joint_p": float(fwald.pvalue),
        "adj_rsq": float(model.rsquared_adj),
    }


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
    print("R3 Phase 2 — Trimmed-tail re-estimation")
    print("=" * 72)

    df = load_clean()
    cutoffs = [None, 95, 90, 80, 70, 50]
    results = [fit_with_cutoff(df, c) for c in cutoffs]

    print(f"\n{'Cutoff':<10}{'N':>6}{'TCI':>11}{'FSTS²':>13}"
          f"{'FSTS×DAI':>13}{'FSTS²×DAI':>13}{'JointF (p)':>15}"
          f"{'AdjR²':>9}")
    print("-" * 95)
    for r in results:
        cell = lambda b, p: f"{b:+.3f}{stars(p)}"
        print(f"{r['label']:<10}{r['n']:>6}"
              f"{cell(r['TCI'], r['TCI_p']):>11}"
              f"{cell(r['fsts_c2'], r['fsts_c2_p']):>13}"
              f"{cell(r['fsts_c_DAI'], r['fsts_c_DAI_p']):>13}"
              f"{cell(r['fsts_c2_DAI'], r['fsts_c2_DAI_p']):>13}"
              f"{r['joint_F']:>5.2f} ({r['joint_p']:.3f}) "
              f"{r['adj_rsq']:>9.3f}")

    out_json = AUDIT_DIR / "trimmed_tail.json"
    out_json.write_text(json.dumps(results, indent=2))
    print(f"\nWrote: {out_json}")

    # LaTeX table
    tex = []
    tex.append("\\begin{table}[ht]")
    tex.append("\\centering")
    tex.append("\\caption{Trimmed-tail re-estimation of canonical M8. "
               "Drop firms above each FSTS cutoff and re-fit, "
               "re-centering FSTS within the retained sample. HC1 SE.}")
    tex.append("\\label{tab:trimmed_tail}")
    tex.append("\\begin{tabular}{lrrrrrrr}")
    tex.append("\\toprule")
    tex.append("Cutoff & N & TCI & FSTS$^2$ & FSTS$\\times$DAI "
               "& FSTS$^2\\times$DAI & Joint F (p) & Adj.\\,R$^2$ \\\\")
    tex.append("\\midrule")
    for r in results:
        tex.append(
            f"{r['label']} & {r['n']} & "
            f"{r['TCI']:+.3f}{stars(r['TCI_p'])} & "
            f"{r['fsts_c2']:+.3f}{stars(r['fsts_c2_p'])} & "
            f"{r['fsts_c_DAI']:+.3f}{stars(r['fsts_c_DAI_p'])} & "
            f"{r['fsts_c2_DAI']:+.3f}{stars(r['fsts_c2_DAI_p'])} & "
            f"{r['joint_F']:.2f} ({r['joint_p']:.3f}) & "
            f"{r['adj_rsq']:.3f} \\\\"
        )
    tex.append("\\bottomrule")
    tex.append("\\end{tabular}")
    tex.append("\\par\\smallskip")
    tex.append("\\footnotesize Note: $\\dagger\\,p<.10$, $*\\,p<.05$, "
               "$**\\,p<.01$, $***\\,p<.001$.")
    tex.append("\\end{table}")
    tex_path = TABLES_DIR / "T_trimmed_tail.tex"
    tex_path.write_text("\n".join(tex))
    print(f"Wrote: {tex_path}")

    # Verdict
    print("\n" + "=" * 72)
    print("Verdict on right-tail-leverage concern:")
    print("=" * 72)
    full = results[0]
    cut70 = next(r for r in results if r["label"] == "≤70%")
    cut50 = next(r for r in results if r["label"] == "≤50%")
    print(f"  Full sample:    FSTS²×DAI = {full['fsts_c2_DAI']:+.3f}, "
          f"joint F p = {full['joint_p']:.3f}")
    print(f"  Drop FSTS>70:   FSTS²×DAI = {cut70['fsts_c2_DAI']:+.3f}, "
          f"joint F p = {cut70['joint_p']:.3f}")
    print(f"  Drop FSTS>50:   FSTS²×DAI = {cut50['fsts_c2_DAI']:+.3f}, "
          f"joint F p = {cut50['joint_p']:.3f}")
    if cut70["joint_p"] < 0.10 and cut50["joint_p"] < 0.10:
        print("\n  → DAI moderation survives at FSTS≤70 and FSTS≤50.")
        print("    The result is NOT driven by a handful of upper-tail firms.")
    elif cut70["joint_p"] < 0.10:
        print("\n  → DAI moderation survives FSTS≤70 but evaporates at FSTS≤50.")
        print("    Caveat: contribution depends on the FSTS 50–70 segment.")
    else:
        print("\n  → DAI moderation evaporates at FSTS≤70.")
        print("    The contribution claim must be reframed: the moderation")
        print("    pattern is concentrated in the upper tail and cannot be")
        print("    cleanly identified on the bulk of the distribution.")


if __name__ == "__main__":
    main()
