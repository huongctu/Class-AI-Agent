"""
R3 Phase 0 — Audit ALL six rows of Manuscript Table 3 (robustness checks).

Manuscript Table 3 currently reports (TCI, FSTS²×DAI, Joint F (p), AdjR², N):
  R1 Baseline (TCI_full + DAI_rich):     617   0.187***   2.972*   3.28 (.039)   0.192
  R2 R1: DAI_thin (website c22b only):   623   0.211***   1.563    0.95 (.388)   0.184
  R3 R2: TCI_thin (e6 + b8):             617   0.171***   2.749*   2.97 (.052)   0.188
  R4 R3: Excl micro-firms (<10 empl):    464   0.218***   3.535*   4.64 (.010)   0.226
  R5 R4: SMEs only (≤200 empl):          595   0.180***   3.483**  3.81 (.023)   0.197
  R6 R5: Exporters only (FSTS > 0):       84   0.143      1.308    3.18 (.048)   0.140

This script re-estimates each spec from raw data, so we can:
  1. Confirm canonical baseline matches Table 2 M8.
  2. Detect any other transcription errors (mismatches in R2–R6).
  3. Output a corrected Table 3 in plain text + LaTeX for the manuscript.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.formula.api as smf

REPO = Path(__file__).resolve().parents[2]
DTA = REPO / "data" / "raw" / "Singapore2023fulldata.dta"
OUT_DIR = REPO / "outputs" / "r3" / "audit"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def base_frame():
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
    # Only propagate dai_drop missingness to k33_imp / k38_imp, NOT to c22b_yn:
    # c22b ("does the firm have a website") is answered independently of
    # the k33/k38 questions, so DAI_thin (c22b-only) keeps the full sample.
    df.loc[df["dai_drop"], ["k33_imp", "k38_imp"]] = np.nan

    df["lp"] = df["d2"] / df["l1"]
    df["ln_lp"] = np.log(df["lp"])
    lo, hi = df["ln_lp"].quantile([0.01, 0.99])
    df["ln_lp"] = df["ln_lp"].clip(lo, hi)

    df["fsts"] = df["d3c"] / 100.0
    df["fsts_c"] = df["fsts"] - df["fsts"].mean()
    df["fsts_c2"] = df["fsts_c"] ** 2

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

    # Composites: full TCI (4 binary) and rich DAI (3 indicators).
    def composite(parts: list[str], colname: str):
        zs = []
        for c in parts:
            mu, sd = df[c].mean(), df[c].std()
            df[c + "_z_" + colname] = (df[c] - mu) / sd
            zs.append(c + "_z_" + colname)
        raw = df[zs].sum(axis=1, skipna=False) / len(parts)
        df[colname] = (raw - raw.mean()) / raw.std()

    composite(["b8_yn", "e6_yn", "h1_yn", "h8_yn"], "TCI_full")
    composite(["c22b_yn", "k33_imp", "k38_imp"], "DAI_rich")
    # R2 in Table 3: DAI_thin = "website c22b only" → solo c22b z-scored.
    df["DAI_thin_c22b_only"] = (
        (df["c22b_yn"] - df["c22b_yn"].mean()) / df["c22b_yn"].std()
    )
    # R3 in Table 3: TCI_thin = "e6 + b8" only.
    composite(["e6_yn", "b8_yn"], "TCI_thin_e6_b8")
    return df


def fit_m8(df, tci="TCI_full", dai="DAI_rich", subset_mask=None):
    df = df.copy()
    df["TCI"] = df[tci]
    df["DAI"] = df[dai]
    df["fsts_c_DAI"] = df["fsts_c"] * df["DAI"]
    df["fsts_c2_DAI"] = df["fsts_c2"] * df["DAI"]
    core = ["ln_lp", "fsts_c", "fsts_c2", "TCI", "DAI",
            "fsts_c_DAI", "fsts_c2_DAI",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    mask = df[core].notna().all(axis=1)
    if subset_mask is not None:
        mask &= subset_mask
    formula = (
        "ln_lp ~ fsts_c + fsts_c2 + TCI + DAI"
        " + fsts_c_DAI + fsts_c2_DAI"
        " + ln_empl + firm_age + foreign + C(broad_sector)"
    )
    m = smf.ols(formula, data=df[mask]).fit(cov_type="HC1")
    fwald = m.f_test("fsts_c_DAI = 0, fsts_c2_DAI = 0")
    return {
        "n": int(mask.sum()),
        "TCI": float(m.params["TCI"]),
        "TCI_p": float(m.pvalues["TCI"]),
        "fsts_c2_DAI": float(m.params["fsts_c2_DAI"]),
        "fsts_c2_DAI_p": float(m.pvalues["fsts_c2_DAI"]),
        "joint_F": float(fwald.fvalue),
        "joint_p": float(fwald.pvalue),
        "adj_rsq": float(m.rsquared_adj),
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


def fmt_row(label, r):
    tci_str = f"{r['TCI']:+.3f}{stars(r['TCI_p'])}"
    fst_str = f"{r['fsts_c2_DAI']:+.3f}{stars(r['fsts_c2_DAI_p'])}"
    f_str = f"{r['joint_F']:.2f} ({r['joint_p']:.3f})"
    return (label, str(r["n"]), tci_str, fst_str, f_str,
            f"{r['adj_rsq']:.3f}")


def main():
    print("=" * 95)
    print("R3 Phase 0 — Re-estimate ALL six rows of Table 3")
    print("=" * 95)

    df = base_frame()

    rows_canon = {}

    # R1 Baseline: TCI_full + DAI_rich (M8 canonical).
    rows_canon["R1_baseline"] = fit_m8(df, "TCI_full", "DAI_rich")

    # R2 DAI_thin (website c22b only): drop k33, k38 → use only c22b_yn.
    # Note: with only c22b, DAI_thin_c22b_only is defined for ALL 623 firms
    # (since c22b binary has no -9 codes that would exclude). So sample = 623.
    rows_canon["R2_DAI_thin"] = fit_m8(df, "TCI_full", "DAI_thin_c22b_only")

    # R3 TCI_thin (e6 + b8 only).
    rows_canon["R3_TCI_thin"] = fit_m8(df, "TCI_thin_e6_b8", "DAI_rich")

    # R4 Exclude micro-firms (<10 empl).
    rows_canon["R4_excl_micro"] = fit_m8(df, "TCI_full", "DAI_rich",
                                         subset_mask=(df["l1"] >= 10))

    # R5 SMEs only (≤200 empl).
    rows_canon["R5_SMEs"] = fit_m8(df, "TCI_full", "DAI_rich",
                                   subset_mask=(df["l1"] <= 200))

    # R6 Exporters only (FSTS > 0).
    rows_canon["R6_exporters"] = fit_m8(df, "TCI_full", "DAI_rich",
                                        subset_mask=(df["fsts"] > 0))

    # Manuscript values for comparison
    manuscript = {
        "R1_baseline":   {"label": "Baseline (TCI_full + DAI_rich)",
                          "n": 617, "TCI": 0.187, "fsts_c2_DAI": 2.972,
                          "joint_F": 3.28, "joint_p": 0.039, "adj_rsq": 0.192},
        "R2_DAI_thin":   {"label": "R1: DAI_thin (website c22b only)",
                          "n": 623, "TCI": 0.211, "fsts_c2_DAI": 1.563,
                          "joint_F": 0.95, "joint_p": 0.388, "adj_rsq": 0.184},
        "R3_TCI_thin":   {"label": "R2: TCI_thin (e6 + b8)",
                          "n": 617, "TCI": 0.171, "fsts_c2_DAI": 2.749,
                          "joint_F": 2.97, "joint_p": 0.052, "adj_rsq": 0.188},
        "R4_excl_micro": {"label": "R3: Excl micro-firms (<10 empl)",
                          "n": 464, "TCI": 0.218, "fsts_c2_DAI": 3.535,
                          "joint_F": 4.64, "joint_p": 0.010, "adj_rsq": 0.226},
        "R5_SMEs":       {"label": "R4: SMEs only (≤200 empl)",
                          "n": 595, "TCI": 0.180, "fsts_c2_DAI": 3.483,
                          "joint_F": 3.81, "joint_p": 0.023, "adj_rsq": 0.197},
        "R6_exporters":  {"label": "R5: Exporters only (FSTS > 0)",
                          "n": 84, "TCI": 0.143, "fsts_c2_DAI": 1.308,
                          "joint_F": 3.18, "joint_p": 0.048, "adj_rsq": 0.140},
    }

    # Compare side-by-side
    print(f"\n{'Row':<14}{'N(can/man)':<14}{'TCI(can/man)':<22}"
          f"{'FSTS²×DAI(can/man)':<28}{'AdjR²(can/man)':<20}")
    print("-" * 95)
    diffs = {}
    for key in rows_canon:
        c = rows_canon[key]
        m = manuscript[key]
        n_match = "✓" if c["n"] == m["n"] else "✗"
        tci_dist = abs(c["TCI"] - m["TCI"])
        fst_dist = abs(c["fsts_c2_DAI"] - m["fsts_c2_DAI"])
        adj_dist = abs(c["adj_rsq"] - m["adj_rsq"])
        tci_match = "✓" if tci_dist < 0.005 else "✗"
        fst_match = "✓" if fst_dist < 0.020 else "✗"
        adj_match = "✓" if adj_dist < 0.005 else "✗"
        print(f"{key:<14}"
              f"{c['n']:>4}/{m['n']:<4} {n_match:<5}"
              f"{c['TCI']:>+7.3f}/{m['TCI']:<+7.3f} {tci_match:<3}"
              f"{c['fsts_c2_DAI']:>+8.3f}/{m['fsts_c2_DAI']:<+7.3f} {fst_match:<6}"
              f"{c['adj_rsq']:>6.3f}/{m['adj_rsq']:<6.3f} {adj_match}")
        diffs[key] = {
            "n_match": c["n"] == m["n"],
            "tci_dist": tci_dist,
            "fst_dist": fst_dist,
            "adj_dist": adj_dist,
        }

    # ---- Output corrected table ----
    print("\n" + "=" * 95)
    print("CORRECTED TABLE 3 (canonical, ready to paste into manuscript)")
    print("=" * 95)
    header = ["Specification", "N", "TCI β_z", "FSTS² × DAI",
              "Joint F (p)", "Adj. R²"]
    print(" | ".join(f"{h:<32}" if i == 0 else f"{h:>14}"
                     for i, h in enumerate(header)))
    print("-" * 110)
    labels = [
        ("R1_baseline",   "Baseline (TCI_full + DAI_rich)"),
        ("R2_DAI_thin",   "R1: DAI_thin (website c22b only)"),
        ("R3_TCI_thin",   "R2: TCI_thin (e6 + b8)"),
        ("R4_excl_micro", "R3: Excl micro-firms (<10 empl)"),
        ("R5_SMEs",       "R4: SMEs only (≤200 empl)"),
        ("R6_exporters",  "R5: Exporters only (FSTS > 0)"),
    ]
    corrected_rows = []
    for key, label in labels:
        row = fmt_row(label, rows_canon[key])
        corrected_rows.append(row)
        print(" | ".join(f"{v:<32}" if i == 0 else f"{v:>14}"
                         for i, v in enumerate(row)))

    # Save outputs
    audit_payload = {
        "canonical": rows_canon,
        "manuscript_reported": manuscript,
        "diffs": diffs,
        "corrected_table": corrected_rows,
    }
    audit_json = OUT_DIR / "table3_audit.json"
    audit_json.write_text(json.dumps(audit_payload, indent=2))
    print(f"\nWrote: {audit_json}")

    # Verdict summary
    print("\n" + "=" * 95)
    print("VERDICT — which manuscript rows must be corrected:")
    print("=" * 95)
    threshold_tci = 0.005
    threshold_fst = 0.020
    threshold_adj = 0.005
    n_bad = 0
    for key, d in diffs.items():
        bad = (not d["n_match"]
               or d["tci_dist"] >= threshold_tci
               or d["fst_dist"] >= threshold_fst
               or d["adj_dist"] >= threshold_adj)
        if bad:
            n_bad += 1
            issues = []
            if not d["n_match"]:
                issues.append(f"N mismatch")
            if d["tci_dist"] >= threshold_tci:
                issues.append(f"TCI off by {d['tci_dist']:.3f}")
            if d["fst_dist"] >= threshold_fst:
                issues.append(f"FSTS²×DAI off by {d['fst_dist']:.3f}")
            if d["adj_dist"] >= threshold_adj:
                issues.append(f"AdjR² off by {d['adj_dist']:.3f}")
            print(f"  ✗ {key}: {'; '.join(issues)}")
        else:
            print(f"  ✓ {key}: matches within tolerance")
    print(f"\n→ Manuscript rows requiring correction: {n_bad} of 6")


if __name__ == "__main__":
    main()
