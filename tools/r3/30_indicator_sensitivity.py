"""
R3 Phase 3 — Indicator sensitivity for TCI and DAI.

Reviewer concern #2: r(TCI, DAI) = 0.31 leaves room for theoretical
fungibility. DAI may be capturing general formalization or transaction
intensity; TCI may be capturing export readiness or external connectedness.
Need (a) drop-one-item stability, (b) item-swap falsification, (c)
multicollinearity / redundancy diagnostics — appropriate to **formative**
composites (since TCI and DAI are z-standardized formative indices, not
reflective constructs that would warrant CFA / AVE / HTMT).

This script runs three test families:

  3A. Drop-one-item stability:
      - TCI = 4 items: drop each → 4 alt TCIs → re-fit M8.
      - DAI = 3 items: drop each → 3 alt DAIs → re-fit M8.
      Track: TCI β, FSTS²×DAI β, joint F (DAI moderation), Adj R².

  3B. Item-swap falsification:
      - SWAP1: move c22b (website) from DAI to TCI.
      - SWAP2: move h1 (foreign tech license) from TCI to DAI.
      - SWAP3: move e6 (R&D) from TCI to DAI.
      If the moderation pattern survives random reassignment, the
      separation is fragile (constructs are fungible).

  3C. Multicollinearity diagnostics:
      - Pairwise correlation matrix of all 7 items.
      - VIF for each regressor in M8 (using the canonical TCI/DAI).

Outputs:
  outputs/r3/audit/indicator_sensitivity.json
  outputs/r3/tables/T_drop_one.tex
  outputs/r3/tables/T_item_swap.tex
  outputs/r3/tables/T_VIF_corr.tex
  outputs/r3/figures/Indicator_corr_heatmap.png
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

REPO = Path(__file__).resolve().parents[2]
DTA = REPO / "data" / "raw" / "Singapore2023fulldata.dta"
AUDIT_DIR = REPO / "outputs" / "r3" / "audit"
TABLES_DIR = REPO / "outputs" / "r3" / "tables"
FIG_DIR = REPO / "outputs" / "r3" / "figures"
for d in (AUDIT_DIR, TABLES_DIR, FIG_DIR):
    d.mkdir(parents=True, exist_ok=True)

TCI_PARTS = ["b8_yn", "e6_yn", "h1_yn", "h8_yn"]
DAI_PARTS = ["c22b_yn", "k33_imp", "k38_imp"]
ITEM_LABELS = {
    "b8_yn":   "TCI: ISO certification",
    "e6_yn":   "TCI: R&D spending",
    "h1_yn":   "TCI: foreign tech license",
    "h8_yn":   "TCI: in-house product/process innov.",
    "c22b_yn": "DAI: firm has website",
    "k33_imp": "DAI: e-payment to suppliers (%)",
    "k38_imp": "DAI: e-sales to customers (%)",
}


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
    return df


def composite(df, parts, name):
    df = df.copy()
    zs = []
    for c in parts:
        mu, sd = df[c].mean(), df[c].std()
        zcol = c + "_z_for_" + name
        df[zcol] = (df[c] - mu) / sd
        zs.append(zcol)
    raw = df[zs].sum(axis=1, skipna=False) / len(parts)
    df[name] = (raw - raw.mean()) / raw.std()
    return df


def fit_m8(df, tci_col="TCI", dai_col="DAI"):
    df = df.copy()
    df["TCI"] = df[tci_col]
    df["DAI"] = df[dai_col]
    df["fsts_c_DAI"] = df["fsts_c"] * df["DAI"]
    df["fsts_c2_DAI"] = df["fsts_c2"] * df["DAI"]
    core = ["ln_lp", "fsts_c", "fsts_c2", "TCI", "DAI",
            "fsts_c_DAI", "fsts_c2_DAI",
            "ln_empl", "firm_age", "foreign", "broad_sector"]
    mask = df[core].notna().all(axis=1)
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
        "DAI": float(m.params["DAI"]),
        "DAI_p": float(m.pvalues["DAI"]),
        "fsts_c2_DAI": float(m.params["fsts_c2_DAI"]),
        "fsts_c2_DAI_p": float(m.pvalues["fsts_c2_DAI"]),
        "joint_F": float(fwald.fvalue),
        "joint_p": float(fwald.pvalue),
        "adj_rsq": float(m.rsquared_adj),
    }


def stars(p):
    if p < 0.001: return "***"
    if p < 0.01:  return "**"
    if p < 0.05:  return "*"
    if p < 0.10:  return "†"
    return ""


def task_3a_drop_one(df):
    """Drop-one-item stability."""
    print("\n" + "=" * 72)
    print("3A. Drop-one-item stability")
    print("=" * 72)
    rows = []
    df_canon = composite(composite(df, TCI_PARTS, "TCI"), DAI_PARTS, "DAI")
    rows.append(("Canonical (all items)", fit_m8(df_canon)))

    for drop in TCI_PARTS:
        keep = [p for p in TCI_PARTS if p != drop]
        d2 = composite(df, keep, "TCI")
        d2 = composite(d2, DAI_PARTS, "DAI")
        rows.append((f"TCI drop {ITEM_LABELS[drop]}", fit_m8(d2)))

    for drop in DAI_PARTS:
        keep = [p for p in DAI_PARTS if p != drop]
        d2 = composite(df, TCI_PARTS, "TCI")
        d2 = composite(d2, keep, "DAI")
        rows.append((f"DAI drop {ITEM_LABELS[drop]}", fit_m8(d2)))

    print(f"\n{'Spec':<46}{'N':>5}{'TCI':>11}{'FSTS²×DAI':>13}"
          f"{'Joint F (p)':>15}{'AdjR²':>9}")
    print("-" * 100)
    for label, r in rows:
        print(f"{label:<46}{r['n']:>5}"
              f"{r['TCI']:>+8.3f}{stars(r['TCI_p']):<3}"
              f"{r['fsts_c2_DAI']:>+10.3f}{stars(r['fsts_c2_DAI_p']):<3}"
              f"{r['joint_F']:>5.2f} ({r['joint_p']:.3f})  "
              f"{r['adj_rsq']:>8.3f}")
    return rows


def task_3b_swap(df):
    """Item-swap falsification."""
    print("\n" + "=" * 72)
    print("3B. Item-swap falsification")
    print("=" * 72)

    swaps = [
        ("SWAP1: move c22b (website) → TCI",
         TCI_PARTS + ["c22b_yn"], [p for p in DAI_PARTS if p != "c22b_yn"]),
        ("SWAP2: move h1 (foreign tech) → DAI",
         [p for p in TCI_PARTS if p != "h1_yn"], DAI_PARTS + ["h1_yn"]),
        ("SWAP3: move e6 (R&D) → DAI",
         [p for p in TCI_PARTS if p != "e6_yn"], DAI_PARTS + ["e6_yn"]),
    ]
    rows = []
    df_canon = composite(composite(df, TCI_PARTS, "TCI"), DAI_PARTS, "DAI")
    rows.append(("Canonical (correct assignment)", fit_m8(df_canon)))
    for label, t_parts, d_parts in swaps:
        d2 = composite(df, t_parts, "TCI")
        d2 = composite(d2, d_parts, "DAI")
        rows.append((label, fit_m8(d2)))

    print(f"\n{'Spec':<42}{'N':>5}{'TCI':>11}{'DAI':>11}"
          f"{'FSTS²×DAI':>13}{'Joint F (p)':>15}")
    print("-" * 100)
    for label, r in rows:
        print(f"{label:<42}{r['n']:>5}"
              f"{r['TCI']:>+8.3f}{stars(r['TCI_p']):<3}"
              f"{r['DAI']:>+8.3f}{stars(r['DAI_p']):<3}"
              f"{r['fsts_c2_DAI']:>+10.3f}{stars(r['fsts_c2_DAI_p']):<3}"
              f"{r['joint_F']:>5.2f} ({r['joint_p']:.3f})")
    return rows


def task_3c_corr_vif(df):
    """Indicator correlation matrix + VIF on M8 regressors."""
    print("\n" + "=" * 72)
    print("3C. Indicator correlation matrix + VIF")
    print("=" * 72)

    # Need a subset where all items are present
    all_items = TCI_PARTS + DAI_PARTS
    sub = df[all_items].dropna()
    print(f"\nN with all 7 items present: {len(sub)}")

    corr = sub.corr()
    print("\nPairwise correlation matrix (Pearson):")
    label_short = {k: k for k in all_items}
    print(corr.round(3).to_string())

    # Heatmap
    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(corr.values, cmap="RdBu_r", vmin=-1, vmax=1, aspect="equal")
    labels = [ITEM_LABELS[c] for c in all_items]
    ax.set_xticks(range(len(all_items)))
    ax.set_xticklabels(labels, rotation=40, ha="right", fontsize=9)
    ax.set_yticks(range(len(all_items)))
    ax.set_yticklabels(labels, fontsize=9)
    for i in range(len(all_items)):
        for j in range(len(all_items)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
                    ha="center", va="center", fontsize=8,
                    color="white" if abs(corr.iloc[i, j]) > 0.5 else "black")
    fig.colorbar(im, ax=ax, fraction=0.045, pad=0.04)
    ax.set_title("Pairwise correlations of TCI and DAI items")
    fig.tight_layout()
    out_fig = FIG_DIR / "Indicator_corr_heatmap.png"
    fig.savefig(out_fig, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\nWrote: {out_fig}")

    # Cross-construct mean correlations
    tci_dai_corrs = []
    for t in TCI_PARTS:
        for d in DAI_PARTS:
            tci_dai_corrs.append(corr.loc[t, d])
    print(f"\nMean cross-construct TCI×DAI item correlation: "
          f"{np.mean(tci_dai_corrs):.3f}")
    print(f"Max abs cross-construct correlation: "
          f"{np.max(np.abs(tci_dai_corrs)):.3f}")

    # VIF
    df_canon = composite(composite(df, TCI_PARTS, "TCI"), DAI_PARTS, "DAI")
    df_canon["fsts_c_DAI"] = df_canon["fsts_c"] * df_canon["DAI"]
    df_canon["fsts_c2_DAI"] = df_canon["fsts_c2"] * df_canon["DAI"]
    regressors = ["fsts_c", "fsts_c2", "TCI", "DAI",
                  "fsts_c_DAI", "fsts_c2_DAI",
                  "ln_empl", "firm_age", "foreign"]
    vif_sub = df_canon[regressors].dropna()
    vifs = {}
    arr = vif_sub.values
    for i, name in enumerate(regressors):
        vifs[name] = float(variance_inflation_factor(arr, i))
    print("\nVIF on M8 regressors (excl. sector dummies):")
    for k, v in vifs.items():
        flag = " ⚠" if v > 10 else ""
        print(f"  {k:<14}{v:>8.2f}{flag}")

    return {
        "n_with_all_items": int(len(sub)),
        "corr_matrix": corr.round(4).to_dict(),
        "mean_cross_construct_corr": float(np.mean(tci_dai_corrs)),
        "max_cross_construct_corr": float(np.max(np.abs(tci_dai_corrs))),
        "vifs": vifs,
    }


def write_tex_drop_one(rows):
    tex = ["\\begin{table}[ht]", "\\centering",
           "\\caption{Drop-one-item stability of canonical M8.}",
           "\\label{tab:drop_one}",
           "\\begin{tabular}{lrrrrr}", "\\toprule",
           "Spec & N & TCI & FSTS$^2\\times$DAI & Joint F (p) & Adj.\\,R$^2$ \\\\",
           "\\midrule"]
    for label, r in rows:
        tex.append(
            f"{label} & {r['n']} & "
            f"{r['TCI']:+.3f}{stars(r['TCI_p'])} & "
            f"{r['fsts_c2_DAI']:+.3f}{stars(r['fsts_c2_DAI_p'])} & "
            f"{r['joint_F']:.2f} ({r['joint_p']:.3f}) & "
            f"{r['adj_rsq']:.3f} \\\\"
        )
    tex += ["\\bottomrule", "\\end{tabular}",
            "\\par\\smallskip",
            "\\footnotesize Note: $\\dagger\\,p<.10$, $*\\,p<.05$, "
            "$**\\,p<.01$, $***\\,p<.001$.",
            "\\end{table}"]
    (TABLES_DIR / "T_drop_one.tex").write_text("\n".join(tex))


def write_tex_swap(rows):
    tex = ["\\begin{table}[ht]", "\\centering",
           "\\caption{Item-swap falsification: re-assign indicators "
           "between TCI and DAI.}",
           "\\label{tab:item_swap}",
           "\\begin{tabular}{lrrrrr}", "\\toprule",
           "Spec & N & TCI & DAI & FSTS$^2\\times$DAI & Joint F (p) \\\\",
           "\\midrule"]
    for label, r in rows:
        tex.append(
            f"{label} & {r['n']} & "
            f"{r['TCI']:+.3f}{stars(r['TCI_p'])} & "
            f"{r['DAI']:+.3f}{stars(r['DAI_p'])} & "
            f"{r['fsts_c2_DAI']:+.3f}{stars(r['fsts_c2_DAI_p'])} & "
            f"{r['joint_F']:.2f} ({r['joint_p']:.3f}) \\\\"
        )
    tex += ["\\bottomrule", "\\end{tabular}",
            "\\par\\smallskip",
            "\\footnotesize Note: SWAP rows test whether moderation "
            "pattern survives reassigning indicators between constructs. "
            "Significant joint F surviving SWAP implies the constructs "
            "are interchangeable (fungibility); a null swap result "
            "supports correct assignment.",
            "\\end{table}"]
    (TABLES_DIR / "T_item_swap.tex").write_text("\n".join(tex))


def write_tex_vif(payload):
    tex = ["\\begin{table}[ht]", "\\centering",
           "\\caption{VIF on M8 regressors (excluding sector dummies).}",
           "\\label{tab:vif}",
           "\\begin{tabular}{lr}", "\\toprule",
           "Regressor & VIF \\\\", "\\midrule"]
    for k, v in payload["vifs"].items():
        flag = "$^{\\ddagger}$" if v > 10 else ""
        tex.append(f"{k} & {v:.2f}{flag} \\\\")
    tex += ["\\bottomrule", "\\end{tabular}",
            "\\par\\smallskip",
            "\\footnotesize $^{\\ddagger}$ VIF $>$ 10 indicates "
            "concerning multicollinearity. "
            f"Mean cross-construct (TCI item $\\times$ DAI item) Pearson "
            f"correlation: {payload['mean_cross_construct_corr']:.3f}; "
            f"max: {payload['max_cross_construct_corr']:.3f}.",
            "\\end{table}"]
    (TABLES_DIR / "T_VIF_corr.tex").write_text("\n".join(tex))


def main():
    print("=" * 72)
    print("R3 Phase 3 — Indicator sensitivity (formative-construct logic)")
    print("=" * 72)
    df = load_frame()

    rows_3a = task_3a_drop_one(df)
    rows_3b = task_3b_swap(df)
    info_3c = task_3c_corr_vif(df)

    payload = {
        "drop_one": [{"label": l, **r} for l, r in rows_3a],
        "swap": [{"label": l, **r} for l, r in rows_3b],
        "corr_vif": info_3c,
    }
    out = AUDIT_DIR / "indicator_sensitivity.json"
    out.write_text(json.dumps(payload, indent=2))
    print(f"\nWrote: {out}")

    write_tex_drop_one(rows_3a)
    write_tex_swap(rows_3b)
    write_tex_vif(info_3c)
    print(f"Wrote: {TABLES_DIR / 'T_drop_one.tex'}")
    print(f"Wrote: {TABLES_DIR / 'T_item_swap.tex'}")
    print(f"Wrote: {TABLES_DIR / 'T_VIF_corr.tex'}")


if __name__ == "__main__":
    main()
