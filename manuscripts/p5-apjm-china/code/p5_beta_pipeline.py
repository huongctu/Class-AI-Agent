#!/usr/bin/env python3
"""
p5_beta_pipeline.py
===================
P5 Option β V2 execution pipeline.

Plan B1 (cross-wave clean) per anh's choice:
  - Block A (Liquidity Access): k7 overdraft, k8/k82 line of credit
  - Block C (Financing Structure): k3a internal, k3bc bank, k3f trade
  - Block D (Access Obstacle): k30 Likert
  - Block B (Receivables Exposure: k1c, k2c) reported as 2012-only robustness

Spec discipline (matches em P4 and P5 do-file conventions):
  - Treat WBES `-9` as missing
  - Listwise on focal vars (d2, l1, d3c, b8, e6, c22b)
  - TCI_full = mean(b8, e6, h1, h8) require >=3 of 4 items
  - DAI_thin = mean(c22b, e6) require >=1 of 2 items
  - Z-standardize within wave
  - OLS with HC1 robust SE
  - Interactions: focal is FSTS_sq × WC

Outputs:
  ../output/p5_beta_results.csv  -- long-format coefficient table
  ../output/p5_beta_run.log      -- stdout log
"""

from __future__ import annotations
import sys, os
from pathlib import Path
import numpy as np
import pandas as pd
import statsmodels.api as sm

try:
    import pyreadstat
except ImportError:
    sys.exit("pyreadstat is required.")

PATHS = {
    2012: "/root/.claude/uploads/dc8321ff-3a71-4dcf-a64c-b978cd7a489b/0918305d-China2012fullESN2700data.dta",
    2024: "/root/.claude/uploads/dc8321ff-3a71-4dcf-a64c-b978cd7a489b/56768710-China2024fulldata.dta",
}
OUTDIR = Path(__file__).resolve().parent.parent / "output"
OUTDIR.mkdir(parents=True, exist_ok=True)

LOG_LINES: list[str] = []

def log(msg: str = "") -> None:
    print(msg)
    LOG_LINES.append(str(msg))


def read_dta_with_fallback(path: str) -> pd.DataFrame:
    last_err = None
    for enc in (None, "latin1", "cp1252"):
        try:
            kwargs = {"apply_value_formats": False}
            if enc is not None:
                kwargs["encoding"] = enc
            df, _meta = pyreadstat.read_dta(path, **kwargs)
            return df
        except Exception as e:
            last_err = e
    raise last_err


def coerce_numeric(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    for c in cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df


def replace_missing_codes(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Replace WBES non-response codes -9 / -7 with NaN for the given columns."""
    for c in cols:
        if c in df.columns:
            df[c] = df[c].where(~df[c].isin([-9, -7]))
    return df


def build_wave(year: int, raw: pd.DataFrame) -> pd.DataFrame:
    log(f"\n--- Building wave {year} ---")
    df = raw.copy()
    df["wave"] = year

    # Focal columns to coerce + clean.
    # Note: CHN 2012 uses CNo1 (innovation) and CNo3 (R&D spending) instead of
    # standard h1 / h8. CHN 2024 uses standard h1 / h8.
    focal = ["d2", "l1", "d3c", "b8", "e6", "c22b", "b5", "b2b",
             "k7", "k30", "k3a", "k3bc", "k3e", "k3f", "k3hd",
             "k1c", "k2c", "a4a", "a4b", "a2"]
    if year == 2012:
        focal += ["k8", "CNo1", "CNo3"]
    elif year == 2024:
        focal += ["k82", "h1", "h8"]

    df = coerce_numeric(df, focal)
    df = replace_missing_codes(df, focal)

    # Harmonize innovation/R&D items across waves: CHN 2012 → h1 = CNo1, h8 = CNo3
    if year == 2012:
        df["h1"] = df.get("CNo1", pd.Series(np.nan, index=df.index))
        df["h8"] = df.get("CNo3", pd.Series(np.nan, index=df.index))

    # Drop firms missing the absolute essentials for the threshold core
    essentials = ["d2", "l1", "d3c"]
    before = len(df)
    df = df.dropna(subset=essentials).copy()
    df = df[(df["d2"] > 0) & (df["l1"] > 0)]
    log(f"  After essentials drop ({essentials} > 0): {len(df)} of {before}")

    # Outcome + threshold core
    df["lnLP"] = np.log(df["d2"].astype(float) / df["l1"].astype(float))
    df["FSTS"] = df["d3c"].astype(float) / 100.0
    df["FSTS_sq"] = df["FSTS"] ** 2
    df["lnemp"] = np.log(df["l1"].astype(float))
    df["firm_age"] = year - df["b5"]
    df["foreign_dummy"] = (df["b2b"].fillna(0) >= 10).astype(int)

    # TCI_full = mean(b8 + e6 + h1 + h8) require >=3 non-missing
    tci_items = ["b8", "e6", "h1", "h8"]
    for v in tci_items:
        if v in df.columns:
            # WBES coding: 1 = yes, 2 = no -> 1 / 0
            df[f"{v}_d"] = (df[v] == 1).astype("float")
            # Items with NaN remain NaN (so rownonmiss is correct)
            df.loc[df[v].isna(), f"{v}_d"] = np.nan
    tci_dum_cols = [f"{v}_d" for v in tci_items if f"{v}_d" in df.columns]
    df["tci_n_valid"] = df[tci_dum_cols].notna().sum(axis=1)
    df["TCI_full"] = df[tci_dum_cols].mean(axis=1, skipna=True)
    df.loc[df["tci_n_valid"] < 3, "TCI_full"] = np.nan

    # DAI_thin = mean(c22b, e6) require >=1
    dai_items = ["c22b", "e6"]
    dai_dum_cols = [f"{v}_d" for v in dai_items if f"{v}_d" in df.columns]
    df["dai_n_valid"] = df[dai_dum_cols].notna().sum(axis=1)
    df["DAI_thin"] = df[dai_dum_cols].mean(axis=1, skipna=True)
    df.loc[df["dai_n_valid"] < 1, "DAI_thin"] = np.nan

    # Working-capital variables per Plan B1
    # Block A: Liquidity Access (binary 1 = yes)
    if "k7" in df.columns:
        df["overdraft"] = (df["k7"] == 1).astype("float")
        df.loc[df["k7"].isna(), "overdraft"] = np.nan
    # Line of credit harmonized binary
    line_src = "k8" if year == 2012 else "k82"
    if line_src in df.columns:
        if year == 2012:
            df["line_credit"] = (df[line_src] == 1).astype("float")
        else:
            # k82 in 2024 is 1-4; treat 1 (yes/active) and 2 (yes/approved-not-active) as access
            df["line_credit"] = df[line_src].isin([1, 2]).astype("float")
        df.loc[df[line_src].isna(), "line_credit"] = np.nan

    # Block C: Financing Structure (% shares)
    for v in ("k3a", "k3bc", "k3f"):
        if v in df.columns:
            # Validate percentage range (0-100)
            df.loc[(df[v] < 0) | (df[v] > 100), v] = np.nan

    # Block D: Access obstacle (Likert; higher = more obstacle)
    # k30 has -7 / -9 as missing already cleared. Range 0-4 expected.
    if "k30" in df.columns:
        df.loc[(df["k30"] < 0) | (df["k30"] > 4), "k30"] = np.nan

    # Block B (2012-only robustness): k1c, k2c percentages
    for v in ("k1c", "k2c"):
        if v in df.columns:
            df.loc[(df[v] < 0) | (df[v] > 100), v] = np.nan

    # Within-wave z-standardize the WC variables we will use
    def zscore(s):
        return (s - s.mean()) / s.std(ddof=1)

    for v in ["overdraft", "line_credit", "k3a", "k3bc", "k3f", "k30", "k1c", "k2c"]:
        if v in df.columns:
            df[f"{v}_z"] = zscore(df[v])

    # Liquidity Access Index: mean of overdraft_z and line_credit_z (where available)
    la_components = [c for c in ("overdraft_z", "line_credit_z") if c in df.columns]
    if la_components:
        df["LA_idx"] = df[la_components].mean(axis=1, skipna=True)
        df["LA_idx_z"] = zscore(df["LA_idx"])

    log(f"  Final wave {year}: {len(df)} rows; "
        f"TCI_full n={df['TCI_full'].notna().sum()}; "
        f"DAI_thin n={df['DAI_thin'].notna().sum()}; "
        f"overdraft n={df['overdraft'].notna().sum() if 'overdraft' in df else 0}; "
        f"line_credit n={df['line_credit'].notna().sum() if 'line_credit' in df else 0}; "
        f"k3a n={df['k3a'].notna().sum() if 'k3a' in df else 0}; "
        f"k30 n={df['k30'].notna().sum() if 'k30' in df else 0}")
    return df


def fit_ols(df: pd.DataFrame, y: str, rhs: list[str]) -> sm.regression.linear_model.RegressionResults | None:
    """Fit OLS-HC1 on `df` for given outcome `y` and right-hand-side `rhs`.
    Drops rows with missing in any rhs variable."""
    cols = [y] + rhs
    sub = df.dropna(subset=cols).copy()
    if len(sub) < 30:
        return None
    X = sub[rhs].astype(float).copy()
    X = sm.add_constant(X)
    return sm.OLS(sub[y].astype(float), X).fit(cov_type="HC1")


def extract_row(model, sample_label: str, model_label: str) -> list[dict]:
    if model is None:
        return [{"sample": sample_label, "model": model_label, "variable": "FAIL",
                 "beta": np.nan, "se": np.nan, "p": np.nan, "n": 0, "r2": np.nan}]
    rows = []
    for v in model.params.index:
        rows.append({
            "sample": sample_label,
            "model": model_label,
            "variable": v,
            "beta": float(model.params[v]),
            "se": float(model.bse[v]),
            "p": float(model.pvalues[v]),
            "n": int(model.nobs),
            "r2": float(model.rsquared),
        })
    return rows


def lind_mehlum(model) -> tuple[float, float]:
    """Lind-Mehlum U-test p-value + turning point in raw FSTS."""
    if model is None or "FSTS" not in model.params.index or "FSTS_sq" not in model.params.index:
        return np.nan, np.nan
    b1 = model.params["FSTS"]
    b2 = model.params["FSTS_sq"]
    se1 = model.bse["FSTS"]
    se2 = model.bse["FSTS_sq"]
    cov = model.cov_params().loc["FSTS", "FSTS_sq"]
    # Test on the [0, 1] support
    slope_lo = b1 + 2 * b2 * 0
    slope_hi = b1 + 2 * b2 * 1
    var_lo = se1 ** 2
    var_hi = se1 ** 2 + 4 * se2 ** 2 + 4 * cov
    from scipy import stats
    t_lo = slope_lo / max(np.sqrt(var_lo), 1e-12)
    t_hi = slope_hi / max(np.sqrt(var_hi), 1e-12)
    p_lo = 1 - stats.norm.cdf(t_lo)
    p_hi = stats.norm.cdf(t_hi)
    p_lm = max(p_lo, p_hi)
    tp_pct = (-b1 / (2 * b2)) * 100 if b2 != 0 else np.nan
    return p_lm, tp_pct


def paternoster_z(b_a: float, se_a: float, b_b: float, se_b: float) -> tuple[float, float]:
    from scipy import stats
    if any(np.isnan(x) for x in (b_a, se_a, b_b, se_b)):
        return np.nan, np.nan
    z = (b_a - b_b) / np.sqrt(se_a ** 2 + se_b ** 2)
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    return z, p


def main():
    log("=" * 70)
    log("P5 Option β V2 — Plan B1 execution")
    log("=" * 70)

    waves = {}
    for year, p in PATHS.items():
        log(f"\n[load] {year}: {p}")
        raw = read_dta_with_fallback(p)
        log(f"  raw rows={len(raw)} cols={len(raw.columns)}")
        waves[year] = build_wave(year, raw)

    # Pool with wave indicator (use original indices; data already has wave column)
    pool = pd.concat(waves.values(), ignore_index=False, sort=False)
    pool["wave_2024"] = (pool["wave"] == 2024).astype(int)
    log(f"\n[pool] total rows={len(pool)}")

    # Pooled z-standardize TCI / DAI / financing-structure for pooled models
    def zscore(s):
        return (s - s.mean()) / s.std(ddof=1)
    for v in ["TCI_full", "DAI_thin", "overdraft", "line_credit",
              "k3a", "k3bc", "k3f", "k30", "LA_idx"]:
        if v in pool.columns:
            pool[f"{v}_zp"] = zscore(pool[v])

    # Within-wave z stays via the per-wave _z columns built in build_wave
    # We rely on per-wave models using *_z and pooled models using *_zp

    rows = []
    paternoster_rows = []

    # ======================================================================
    # M0 — Threshold core (replicate)
    # ======================================================================
    log("\n" + "=" * 70)
    log("M0 — Threshold core (FSTS + FSTS² + controls)")
    log("=" * 70)
    for label, sub in [("CHN_2012", waves[2012]),
                       ("CHN_2024", waves[2024]),
                       ("CHN_pooled", pool)]:
        rhs = ["FSTS", "FSTS_sq", "lnemp", "firm_age", "foreign_dummy"]
        if label == "CHN_pooled":
            rhs = rhs + ["wave_2024"]
        m = fit_ols(sub, "lnLP", rhs)
        if m is None:
            log(f"  {label}: FAIL (n<30)")
            continue
        rows.extend(extract_row(m, label, "M0_baseline"))
        p_lm, tp = lind_mehlum(m)
        log(f"  {label}: n={int(m.nobs)} TP={tp:.2f}% LM_p={p_lm:.4f}  "
            f"FSTS β={m.params['FSTS']:+.3f} (p={m.pvalues['FSTS']:.4f}); "
            f"FSTS² β={m.params['FSTS_sq']:+.3f} (p={m.pvalues['FSTS_sq']:.4f})")

    # ======================================================================
    # Add direct TCI / DAI as positive level shifters
    # ======================================================================
    log("\n" + "=" * 70)
    log("Threshold core + TCI + DAI direct (P5 baseline structure)")
    log("=" * 70)
    for label, sub, tci_col, dai_col in [
        ("CHN_2012", waves[2012], "TCI_full_z", "DAI_thin_z"),
        ("CHN_2024", waves[2024], "TCI_full_z", "DAI_thin_z"),
        ("CHN_pooled", pool, "TCI_full_zp", "DAI_thin_zp"),
    ]:
        # Within-wave z columns; for pooled we already created _zp
        # For 2012/2024 individual waves, the *_z used above were built per-wave
        # by build_wave; but build_wave only zscored WC variables. Let's z TCI/DAI per wave too.
        sub = sub.copy()
        if tci_col not in sub.columns:
            sub[tci_col] = (sub["TCI_full"] - sub["TCI_full"].mean()) / sub["TCI_full"].std(ddof=1)
        if dai_col not in sub.columns:
            sub[dai_col] = (sub["DAI_thin"] - sub["DAI_thin"].mean()) / sub["DAI_thin"].std(ddof=1)

        rhs = ["FSTS", "FSTS_sq", tci_col, dai_col, "lnemp", "firm_age", "foreign_dummy"]
        if label == "CHN_pooled":
            rhs += ["wave_2024"]
        m = fit_ols(sub, "lnLP", rhs)
        if m is None:
            log(f"  {label}: FAIL")
            continue
        rows.extend(extract_row(m, label, "M0p_TCI_DAI_direct"))
        log(f"  {label}: n={int(m.nobs)} TCI β={m.params[tci_col]:+.3f} (p={m.pvalues[tci_col]:.4f}); "
            f"DAI β={m.params[dai_col]:+.3f} (p={m.pvalues[dai_col]:.4f})")

    # ======================================================================
    # M1 — Item-level WC × FSTS² interactions
    # M3 — Block-level WC × FSTS² interactions
    # M4 — Composite WC stress index
    # ======================================================================
    # WC variables to test (cross-wave): overdraft, line_credit, LA_idx, k3a, k3bc, k3f, k30
    wc_blocks = {
        "overdraft":   ("Block A — Liquidity Access (item)",   "z",  "+"),  # higher = access
        "line_credit": ("Block A — Liquidity Access (item)",   "z",  "+"),
        "LA_idx":      ("Block A — Liquidity Access (block)",  "z",  "+"),
        "k3a":         ("Block C — Financing (internal)",      "raw", "-"),  # higher = self-financing dependence
        "k3bc":        ("Block C — Financing (bank)",          "raw", "+"),  # higher = external buffer
        "k3f":         ("Block C — Financing (trade credit)",  "raw", "+/-"),
        "k30":         ("Block D — Access obstacle (Likert)",  "raw", "-"),  # higher = more obstacle = more stress
    }

    log("\n" + "=" * 70)
    log("M1/M3 — WC × FSTS² interactions (item + block)")
    log("Spec note: TCI/DAI dropped from WC interaction models so 2012 runs.")
    log("Joint WC + Digital diagnostic reported separately below.")
    log("=" * 70)
    log(f"{'sample':12s} {'wc':12s} {'block':45s} {'β_inter':>10s} {'p':>8s} {'n':>5s}")

    for sample_label, sub, suffix in [
        ("CHN_2012", waves[2012], "_z"),
        ("CHN_2024", waves[2024], "_z"),
        ("CHN_pooled", pool, "_zp"),
    ]:
        sub = sub.copy()
        for wc, (block_label, scale_pref, exp_sign) in wc_blocks.items():
            wc_col = f"{wc}{suffix}" if scale_pref == "z" else wc
            if wc_col not in sub.columns:
                continue
            sub[f"FSTS_x_{wc}"] = sub["FSTS"] * sub[wc_col]
            sub[f"FSTSsq_x_{wc}"] = sub["FSTS_sq"] * sub[wc_col]

            rhs = ["FSTS", "FSTS_sq",
                   wc_col, f"FSTSsq_x_{wc}",
                   "lnemp", "firm_age", "foreign_dummy"]
            if sample_label == "CHN_pooled":
                rhs += ["wave_2024"]

            m = fit_ols(sub, "lnLP", rhs)
            if m is None:
                continue
            model_label = f"M1_{wc}_FSTSsq" if wc != "LA_idx" else f"M3_{wc}_FSTSsq"
            rows.extend(extract_row(m, sample_label, model_label))

            inter_var = f"FSTSsq_x_{wc}"
            b_inter = m.params.get(inter_var, np.nan)
            p_inter = m.pvalues.get(inter_var, np.nan)
            log(f"{sample_label:12s} {wc:12s} {block_label:45s} {b_inter:+10.3f} {p_inter:8.4f} {int(m.nobs):5d}")

    # ======================================================================
    # M4 — Composite wc_stress_index (cross-wave, Block A + Block C + Block D)
    # ======================================================================
    log("\n" + "=" * 70)
    log("M4 — Composite WC stress index (higher = more stress)")
    log("=" * 70)
    # Build wc_stress_index per wave: -LA_idx_z + k3a_z(internal=stress) + k30_z(obstacle=stress) - k3bc_z(bank=relief)
    for sample_label, sub, suffix in [
        ("CHN_2012", waves[2012], "_z"),
        ("CHN_2024", waves[2024], "_z"),
        ("CHN_pooled", pool, "_zp"),
    ]:
        sub = sub.copy()
        # Ensure z columns exist
        for v in ["LA_idx", "k3a", "k3bc", "k30"]:
            if f"{v}{suffix}" not in sub.columns and v in sub.columns:
                sub[f"{v}{suffix}"] = (sub[v] - sub[v].mean()) / sub[v].std(ddof=1)
        components = []
        if f"LA_idx{suffix}" in sub.columns:
            components.append(-sub[f"LA_idx{suffix}"])
        if f"k3a{suffix}" in sub.columns:
            components.append(sub[f"k3a{suffix}"])
        if f"k3bc{suffix}" in sub.columns:
            components.append(-sub[f"k3bc{suffix}"])
        if f"k30{suffix}" in sub.columns:
            components.append(sub[f"k30{suffix}"])
        if not components:
            continue
        sub["wc_stress_index"] = pd.concat(components, axis=1).mean(axis=1, skipna=True)
        sub["wc_stress_index_z"] = (sub["wc_stress_index"] - sub["wc_stress_index"].mean()) / sub["wc_stress_index"].std(ddof=1)
        sub["FSTSsq_x_wcstress"] = sub["FSTS_sq"] * sub["wc_stress_index_z"]

        rhs = ["FSTS", "FSTS_sq",
               "wc_stress_index_z", "FSTSsq_x_wcstress",
               "lnemp", "firm_age", "foreign_dummy"]
        if sample_label == "CHN_pooled":
            rhs += ["wave_2024"]
        m = fit_ols(sub, "lnLP", rhs)
        if m is None:
            continue
        rows.extend(extract_row(m, sample_label, "M4_wc_stress_FSTSsq"))
        b = m.params.get("FSTSsq_x_wcstress", np.nan)
        p = m.pvalues.get("FSTSsq_x_wcstress", np.nan)
        log(f"  {sample_label}: wc_stress_index × FSTS² β={b:+.3f} (p={p:.4f}) n={int(m.nobs)}")

    # ======================================================================
    # Block B (2012-only robustness): k1c (purchases-on-credit), k2c (sales-on-credit)
    # ======================================================================
    log("\n" + "=" * 70)
    log("Block B (2012-only robustness): k1c / k2c × FSTS²")
    log("=" * 70)
    sub12 = waves[2012].copy()
    for wc in ["k1c", "k2c"]:
        wc_col = f"{wc}_z"
        if wc_col not in sub12.columns:
            continue
        sub12[f"FSTSsq_x_{wc}"] = sub12["FSTS_sq"] * sub12[wc_col]
        rhs = ["FSTS", "FSTS_sq",
               wc_col, f"FSTSsq_x_{wc}",
               "lnemp", "firm_age", "foreign_dummy"]
        m = fit_ols(sub12, "lnLP", rhs)
        if m is None:
            continue
        rows.extend(extract_row(m, "CHN_2012_only", f"M1_{wc}_FSTSsq_2012only"))
        b = m.params.get(f"FSTSsq_x_{wc}", np.nan)
        p = m.pvalues.get(f"FSTSsq_x_{wc}", np.nan)
        log(f"  {wc} × FSTS² β={b:+.3f} (p={p:.4f}) n={int(m.nobs)}")

    # ======================================================================
    # Paternoster cross-wave z-tests on TCI / DAI / FSTS / FSTS²
    # ======================================================================
    log("\n" + "=" * 70)
    log("Paternoster cross-wave z-tests")
    log("=" * 70)
    # Use the M0p_TCI_DAI_direct model's coefficients
    df_rows = pd.DataFrame(rows)
    pat_rows = []
    for spec in ["M0p_TCI_DAI_direct"]:
        for var, var_2024 in [("TCI_full_z", "TCI_full_z"),
                                ("DAI_thin_z", "DAI_thin_z"),
                                ("FSTS", "FSTS"),
                                ("FSTS_sq", "FSTS_sq")]:
            r12 = df_rows[(df_rows.sample == "CHN_2012") &
                          (df_rows.model == spec) &
                          (df_rows.variable == var)]
            r24 = df_rows[(df_rows.sample == "CHN_2024") &
                          (df_rows.model == spec) &
                          (df_rows.variable == var_2024)]
            if r12.empty or r24.empty:
                continue
            b12, se12 = float(r12.beta.iloc[0]), float(r12.se.iloc[0])
            b24, se24 = float(r24.beta.iloc[0]), float(r24.se.iloc[0])
            z, p = paternoster_z(b12, se12, b24, se24)
            pat_rows.append({"variable": var, "b_2012": b12, "se_2012": se12,
                              "b_2024": b24, "se_2024": se24, "z": z, "p": p})
            log(f"  {var:12s}  b12={b12:+.3f}  b24={b24:+.3f}  z={z:+.2f}  p={p:.4f}")

    # ======================================================================
    # Persist outputs
    # ======================================================================
    df_rows = pd.DataFrame(rows)
    df_rows.to_csv(OUTDIR / "p5_beta_results.csv", index=False)
    pd.DataFrame(pat_rows).to_csv(OUTDIR / "p5_beta_paternoster.csv", index=False)
    log(f"\n[done] wrote {OUTDIR/'p5_beta_results.csv'} ({len(df_rows)} rows)")
    log(f"[done] wrote {OUTDIR/'p5_beta_paternoster.csv'} ({len(pat_rows)} rows)")

    (OUTDIR / "p5_beta_run.log").write_text("\n".join(LOG_LINES), encoding="utf-8")
    log(f"[done] wrote {OUTDIR/'p5_beta_run.log'}")


if __name__ == "__main__":
    main()
