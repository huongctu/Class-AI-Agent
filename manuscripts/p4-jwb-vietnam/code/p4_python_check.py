#!/usr/bin/env python3
"""
p4_python_check.py
==================
Second-source verification pipeline for P4 (Vietnam I-P) paper.

Reproduces in Python the full analytic workflow described in §3.2 and §3.3
of the manuscript, so that all coefficients can be cross-checked against the
primary Stata implementation. The two implementations should agree to within
small numerical rounding (typically <1e-3); persistent disagreement signals
a specification ambiguity that requires resolution before submission.

PRINCIPLES (must match Stata do-file)
-------------------------------------
1. Listwise deletion is applied ONCE on the full focal set:
   d2, l1, d3c, b8, e6, c22b, b5, b2b, a4b. Same sample is then used for
   baseline AND every robustness specification.
2. Composites are computed BEFORE z-standardization:
       TCI_thin = mean(b8, e6)
       DAI_core = c22b (own-website presence only; e6 reserved for TCI to
                       avoid construct contamination flagged by reviewer)
   Then z-standardized WITHIN-WAVE (not pooled).
3. Controls: lnemp = ln(l1), firmage = survey_year - b5,
   foreign_owned = (b2b > 0). Manager experience excluded (multicollinearity).
4. Sector FE: a4b 2-digit by default for robustness; broad-sector for baseline.

OUTPUTS
-------
- p4_python_check.md  -- markdown report with seven blocks, ready to paste
- p4_python_baseline.csv -- analytic dataset (for Stata comparison)
- p4_python_results.csv -- coefficient table, all specifications

USAGE
-----
    pip install pandas pyreadstat statsmodels scipy numpy
    python p4_python_check.py \\
        --files Vietnam-2009.dta Vietnam-2015.dta Vietnam-2023.dta \\
        --outdir ./check_output
"""

from __future__ import annotations

import argparse
import sys
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

try:
    import pyreadstat
except ImportError:
    sys.exit("pyreadstat is required. Install: pip install pyreadstat")

try:
    import statsmodels.api as sm
    from scipy import stats
except ImportError:
    sys.exit("statsmodels and scipy required. Install: pip install statsmodels scipy")

warnings.filterwarnings("ignore", category=FutureWarning)


# -----------------------------------------------------------------------------
# Configuration -- single source of truth for variable names and survey years
# -----------------------------------------------------------------------------

FOCAL_VARS = ["d2", "l1", "d3c", "b8", "e6", "c22b", "b5", "b2b"]
SECTOR_CANDIDATES = ["a4b", "a4a"]  # listwise on whichever exists in the wave
WAVE_YEARS = {"2009": 2009, "2015": 2015, "2023": 2023}
PAPER_TABLE2 = {
    # wave: (N, TCI_z, DAI_z) per Table 2 of v4.3
    "2009": (993,  0.317, 0.251),
    "2015": (964,  0.047, 0.022),
    "2023": (1014, 0.180, 0.176),
}

# Variables that may exist only in some waves
INNOVATION_VARS = ["h1", "h8"]                    # 2015, 2023 only
EPAYMENT_VARS = ["k33", "k38"]                    # 2023 only (per em's verification)


# -----------------------------------------------------------------------------
# Section 1: Loading and listwise deletion
# -----------------------------------------------------------------------------

def detect_wave(path: Path, df: pd.DataFrame) -> str:
    """Return wave label '2009' / '2015' / '2023' from filename or data."""
    for yr in WAVE_YEARS:
        if yr in path.name:
            return yr
    for cand in ("a14", "year", "wave"):
        if cand in df.columns:
            try:
                vals = df[cand].dropna().astype(int).unique()
                if len(vals) == 1:
                    return str(int(vals[0]))
            except Exception:
                pass
    raise ValueError(f"Cannot detect wave from {path.name}")


def load_wave(path: Path) -> tuple[str, pd.DataFrame]:
    """Load .dta, detect wave, apply listwise deletion on focal vars.
    Falls back through encodings (utf-8 -> latin1 -> cp1252)."""
    df = None
    last_err = None
    for enc in (None, "latin1", "cp1252"):
        try:
            kwargs = {"apply_value_formats": False}
            if enc is not None:
                kwargs["encoding"] = enc
            df, _meta = pyreadstat.read_dta(str(path), **kwargs)
            break
        except Exception as e:
            last_err = e
    if df is None:
        raise last_err
    wave = detect_wave(path, df)

    # Defensive: not every file is guaranteed to have a4b under that exact name.
    # Try fallbacks before listwise.
    for var in FOCAL_VARS:
        if var not in df.columns:
            print(f"  [warn] focal variable '{var}' missing in wave {wave}")

    df["wave"] = wave
    df["survey_year"] = WAVE_YEARS[wave]
    return wave, df


def apply_listwise(dfs: dict[str, pd.DataFrame]) -> dict[str, pd.DataFrame]:
    """Apply listwise deletion on focal vars + first available sector code,
    ONCE per wave. WBES uses a4b (2-digit ISIC) in 2009/2015 and a4a (1-digit)
    in 2023; either is sufficient for sector FE."""
    out = {}
    for wave, df in dfs.items():
        sector_present = next((s for s in SECTOR_CANDIDATES if s in df.columns), None)
        cols_present = [v for v in FOCAL_VARS if v in df.columns]
        if sector_present:
            cols_present = cols_present + [sector_present]
        before = len(df)
        # WBES uses -9 to encode "don't know" / "refused" — treat as missing
        clean = df.replace(-9, pd.NA).dropna(subset=cols_present).copy()
        out[wave] = clean
        print(f"  Wave {wave}: {before} -> {len(clean)} after listwise on {cols_present}")
    return out


# -----------------------------------------------------------------------------
# Section 2: Variable construction
# -----------------------------------------------------------------------------

def build_variables(df: pd.DataFrame, wave: str) -> pd.DataFrame:
    """Construct all analysis variables per §3.2 specification."""
    df = df.copy()

    # Coerce numeric vars after the listwise NA replacement (object dtype after
    # replace(-9, NA) requires explicit cast).
    for v in ("d2", "l1", "d3c", "b8", "e6", "c22b", "b5", "b2b"):
        if v in df.columns:
            df[v] = pd.to_numeric(df[v], errors="coerce")
    df = df.dropna(subset=[v for v in ("d2", "l1", "d3c", "b5", "b2b")
                            if v in df.columns]).copy()
    # Drop non-positive sales/employees (cannot take log).
    df = df[(df["d2"] > 0) & (df["l1"] > 0)].copy()

    # Productivity (lnLP = ln(d2 / l1))
    df["lnLP"] = np.log(df["d2"].astype(float) / df["l1"].astype(float))

    # Export intensity, mean-centred within-wave then squared
    df["fsts"] = df["d3c"] / 100.0  # rescale to [0,1]
    df["fsts_c"] = df["fsts"] - df["fsts"].mean()
    df["fsts_c2"] = df["fsts_c"] ** 2

    # Composite TCI_thin and DAI_core (BEFORE z-standardization)
    # b8 and c22b are typically 1/2 (Yes/No) in WBES; convert to binary 0/1
    for v in ["b8", "e6", "c22b"]:
        if v in df.columns:
            # WBES convention: 1 = Yes, 2 = No; remap to 1/0
            df[v + "_dum"] = (df[v] == 1).astype(int)

    df["tci_thin"] = (df["b8_dum"] + df["e6_dum"]) / 2.0
    # DAI_core = c22b only. e6 is excluded to keep TCI/DAI orthogonal: e6
    # (foreign-licensed technology) is a Lall (1992) capability proxy, not a
    # Bharadwaj (2013)/Verhoef (2021) digital-presence proxy. Cf. §2.2 / §3.2.
    df["dai_core"] = df["c22b_dum"].astype(float)

    # Controls
    df["lnemp"] = np.log(df["l1"])
    df["firmage"] = df["survey_year"] - df["b5"]
    df["foreign_owned"] = (df["b2b"] > 0).astype(int)

    # Sector: 2-digit ISIC from a4b; broad sector by collapsing first digit.
    # The 2023 Vietnam release ships with a4a only (industry sampling sector,
    # 1-digit broad codes 1-7); fall back when a4b is absent.
    sector_src = "a4b" if "a4b" in df.columns else (
        "a4a" if "a4a" in df.columns else None)
    if sector_src is not None:
        df["sector_2d"] = df[sector_src].astype(str).str.zfill(2).str[:2]
        df["sector_broad"] = df[sector_src].astype(str).str[:1]
    return df


def zstd_within_wave(df_pool: pd.DataFrame, varname: str) -> pd.Series:
    """Z-standardize a variable within each wave separately."""
    return df_pool.groupby("wave")[varname].transform(
        lambda x: (x - x.mean()) / x.std(ddof=1)
    )


# -----------------------------------------------------------------------------
# Section 3: Baseline OLS with HC1 robust SE
# -----------------------------------------------------------------------------

def run_ols(df: pd.DataFrame, sector_var: str = "sector_broad",
            extra: list[str] | None = None, include_wave_fe: bool = False
            ) -> sm.regression.linear_model.RegressionResultsWrapper:
    """Estimate OLS-HC1 productivity model on `df`."""
    extra = extra or []
    base = ["fsts_c", "fsts_c2", "tci_z", "dai_z",
            "lnemp", "firmage", "foreign_owned"]
    cols = base + extra

    X = df[cols].copy()
    # Sector dummies
    if sector_var in df.columns and df[sector_var].nunique() > 1:
        sec = pd.get_dummies(df[sector_var], prefix="sec", drop_first=True)
        X = pd.concat([X, sec], axis=1)
    if include_wave_fe and df["wave"].nunique() > 1:
        wfe = pd.get_dummies(df["wave"], prefix="wave", drop_first=True)
        X = pd.concat([X, wfe], axis=1)

    X = sm.add_constant(X.astype(float))
    y = df["lnLP"].astype(float)
    model = sm.OLS(y, X, missing="drop").fit(cov_type="HC1")
    return model


def lind_mehlum_test(model, x_var: str = "fsts_c",
                     x_min: float = -0.5, x_max: float = 1.0) -> dict:
    """Lind-Mehlum (2010) U-test for inverted-U relationship.

    Tests the joint hypothesis:
        H0: slope at x_min <= 0 OR slope at x_max >= 0
        H1: slope at x_min > 0 AND slope at x_max < 0  (inverted-U)
    """
    b1 = model.params.get(x_var, np.nan)
    b2 = model.params.get(x_var + "2", np.nan)
    se_b1 = model.bse.get(x_var, np.nan)
    se_b2 = model.bse.get(x_var + "2", np.nan)
    cov_b1b2 = model.cov_params().loc[x_var, x_var + "2"] if (
        x_var in model.params.index and x_var + "2" in model.params.index) else np.nan

    slope_lo = b1 + 2 * b2 * x_min
    slope_hi = b1 + 2 * b2 * x_max
    var_lo = se_b1 ** 2 + (2 * x_min) ** 2 * se_b2 ** 2 + 2 * (2 * x_min) * cov_b1b2
    var_hi = se_b1 ** 2 + (2 * x_max) ** 2 * se_b2 ** 2 + 2 * (2 * x_max) * cov_b1b2

    t_lo = slope_lo / np.sqrt(max(var_lo, 1e-12))
    t_hi = slope_hi / np.sqrt(max(var_hi, 1e-12))

    # Test: max-of-two-sided test, cf. Lind & Mehlum 2010 eq. (4)
    p_lo = 1 - stats.norm.cdf(t_lo)        # P(slope at min <= 0)
    p_hi = stats.norm.cdf(t_hi)            # P(slope at max >= 0)
    p_value = max(p_lo, p_hi)

    turning_point = -b1 / (2 * b2) if b2 != 0 else np.nan
    return {"slope_lo": slope_lo, "slope_hi": slope_hi,
            "p_lo": p_lo, "p_hi": p_hi, "p_value": p_value,
            "turning_point_pct": (turning_point + np.nan) * 100
            if np.isnan(turning_point) else (turning_point + 0) * 100}


# -----------------------------------------------------------------------------
# Section 4: Heckman 2-step
# -----------------------------------------------------------------------------

def heckman_twostep(df: pd.DataFrame, sector_var: str = "sector_broad"
                    ) -> dict:
    """Manual Heckman 2-step with sampling-region exclusion restriction."""
    df = df.copy()
    df["exporter"] = (df["fsts"] > 0).astype(int)

    # Selection equation: probit on full sample
    sel_cols = ["lnemp", "firmage", "foreign_owned"]
    Z = df[sel_cols].copy()
    if "a2" in df.columns:
        region = pd.get_dummies(df["a2"], prefix="reg", drop_first=True)
        Z = pd.concat([Z, region], axis=1)
    elif "stratificationregioncode" in df.columns:
        region = pd.get_dummies(df["stratificationregioncode"],
                                prefix="reg", drop_first=True)
        Z = pd.concat([Z, region], axis=1)
    if sector_var in df.columns:
        sec = pd.get_dummies(df[sector_var], prefix="sec", drop_first=True)
        Z = pd.concat([Z, sec], axis=1)

    Z = sm.add_constant(Z.astype(float))
    try:
        probit = sm.Probit(df["exporter"].astype(int), Z, missing="drop").fit(
            disp=0, maxiter=200)
    except Exception as exc:
        return {"converged": False, "error": str(exc)}

    # Inverse Mills Ratio
    xb = probit.predict(Z, linear=True)
    df["imr"] = stats.norm.pdf(xb) / stats.norm.cdf(xb)

    # Outcome equation on EXPORTERS only, with IMR as additional regressor
    sub = df[df["exporter"] == 1].copy()
    if len(sub) < 30:
        return {"converged": False, "error": "n_exporters < 30"}

    out_cols = ["fsts_c", "fsts_c2", "tci_z", "dai_z",
                "lnemp", "firmage", "foreign_owned", "imr"]
    X_out = sub[out_cols].copy()
    if sector_var in sub.columns and sub[sector_var].nunique() > 1:
        sec = pd.get_dummies(sub[sector_var], prefix="sec", drop_first=True)
        X_out = pd.concat([X_out, sec], axis=1)
    X_out = sm.add_constant(X_out.astype(float))
    y_out = sub["lnLP"].astype(float)
    out = sm.OLS(y_out, X_out, missing="drop").fit(cov_type="HC1")

    return {"converged": True,
            "lambda": out.params["imr"], "se_lambda": out.bse["imr"],
            "p_lambda": out.pvalues["imr"], "n_exporters": len(sub),
            "outcome_model": out}


# -----------------------------------------------------------------------------
# Section 5: Control Function
# -----------------------------------------------------------------------------

def control_function(df: pd.DataFrame, sector_var: str = "sector_broad"
                     ) -> dict:
    """Control function: probit selection -> generalized residual -> OLS."""
    df = df.copy()
    df["exporter"] = (df["fsts"] > 0).astype(int)

    sel_cols = ["lnemp", "firmage", "foreign_owned"]
    Z = df[sel_cols].copy()
    region_var = "a2" if "a2" in df.columns else (
        "stratificationregioncode" if "stratificationregioncode" in df.columns
        else None)
    if region_var:
        Z = pd.concat([Z, pd.get_dummies(df[region_var], prefix="reg",
                                         drop_first=True)], axis=1)
    if sector_var in df.columns:
        Z = pd.concat([Z, pd.get_dummies(df[sector_var], prefix="sec",
                                         drop_first=True)], axis=1)
    Z = sm.add_constant(Z.astype(float))

    try:
        probit = sm.Probit(df["exporter"].astype(int), Z, missing="drop").fit(
            disp=0, maxiter=200)
    except Exception as exc:
        return {"converged": False, "error": str(exc)}

    xb = probit.predict(Z, linear=True)
    Phi = stats.norm.cdf(xb)
    phi = stats.norm.pdf(xb)
    # Generalized residual (Wooldridge 2010, eq. 17.32)
    df["gr"] = df["exporter"] * (phi / np.maximum(Phi, 1e-10)) - \
               (1 - df["exporter"]) * (phi / np.maximum(1 - Phi, 1e-10))

    # Outcome OLS on FULL sample with GR as control
    out_model = run_ols(df, sector_var=sector_var, extra=["gr"])
    return {"converged": True,
            "gr_coef": out_model.params["gr"],
            "se_gr": out_model.bse["gr"],
            "p_gr": out_model.pvalues["gr"],
            "outcome_model": out_model,
            "n": int(out_model.nobs)}


# -----------------------------------------------------------------------------
# Section 6: Robustness pipeline
# -----------------------------------------------------------------------------

def robustness_2digit_isic(df: pd.DataFrame) -> sm.regression.linear_model.RegressionResultsWrapper:
    return run_ols(df, sector_var="sector_2d")


def robustness_micro_excl(df: pd.DataFrame) -> sm.regression.linear_model.RegressionResultsWrapper:
    sub = df[df["l1"] >= 10].copy()
    return run_ols(sub, sector_var="sector_broad")


def robustness_tci_full(df: pd.DataFrame, wave: str
                        ) -> sm.regression.linear_model.RegressionResultsWrapper | None:
    """TCI_full = mean(b8, e6, h1, h8) for waves with h1/h8 available."""
    if not all(v in df.columns for v in INNOVATION_VARS):
        return None
    df = df.copy()
    for v in INNOVATION_VARS:
        df[v + "_dum"] = (df[v] == 1).astype(int)
    df["tci_full"] = (df["b8_dum"] + df["e6_dum"] +
                      df["h1_dum"] + df["h8_dum"]) / 4.0
    df["tci_z"] = zstd_within_wave(df, "tci_full")  # overwrite tci_z
    n_valid = df["tci_full"].notna().sum()
    if n_valid < 200:
        print(f"    [skip] TCI_full: n_valid={n_valid} < 200 in wave {wave}")
        return None
    return run_ols(df, sector_var="sector_broad")


def robustness_dai_rich(df: pd.DataFrame, mode: str = "continuous"
                        ) -> sm.regression.linear_model.RegressionResultsWrapper | None:
    """DAI_rich for 2023: c22b, k33, k38 (continuous % or binary).

    e6 (foreign-licensed tech) excluded to avoid construct contamination
    with TCI (which retains e6 as a Lall 1992 capability proxy).
    """
    if not all(v in df.columns for v in EPAYMENT_VARS):
        return None
    df = df.copy()
    if mode == "continuous":
        # k33, k38 are typically % already; rescale to [0,1]
        df["k33_use"] = df["k33"] / 100.0
        df["k38_use"] = df["k38"] / 100.0
    else:  # binary
        df["k33_use"] = (df["k33"] > 0).astype(float)
        df["k38_use"] = (df["k38"] > 0).astype(float)

    df["dai_rich"] = (df["c22b_dum"] + df["k33_use"] + df["k38_use"]) / 3.0
    df["dai_z"] = zstd_within_wave(df, "dai_rich")  # overwrite dai_z
    return run_ols(df, sector_var="sector_broad")


def coef_delta(model_new, model_base, vars_=("fsts_c", "fsts_c2",
                                             "tci_z", "dai_z")) -> dict:
    """Compute % change in coefficient between two models."""
    out = {}
    for v in vars_:
        if v in model_new.params.index and v in model_base.params.index:
            b_new = model_new.params[v]
            b_base = model_base.params[v]
            if abs(b_base) < 1e-6:
                out[v] = float("nan")
            else:
                out[v] = 100.0 * (b_new - b_base) / abs(b_base)
        else:
            out[v] = float("nan")
    return out


# -----------------------------------------------------------------------------
# Markdown report assembly
# -----------------------------------------------------------------------------

def fmt(x, decimals=3):
    if x is None or (isinstance(x, float) and np.isnan(x)):
        return "—"
    return f"{x:.{decimals}f}"


def build_report(results: dict, outpath: Path):
    L = ["# P4 Python check — full re-estimation report\n"]
    L.append("Generated by `p4_python_check.py`. Cross-check against Stata.\n")

    # Block 1 — Baseline reproduction
    L.append("## Block 1. Baseline reproduction vs paper Table 2\n")
    L.append("| Wave | N (Python) | N (paper) | TCI_z (Py) | TCI_z (paper) | DAI_z (Py) | DAI_z (paper) |")
    L.append("|---|---|---|---|---|---|---|")
    for wave in ("2009", "2015", "2023"):
        if wave in results["baseline"]:
            m = results["baseline"][wave]
            n_paper, tci_paper, dai_paper = PAPER_TABLE2[wave]
            tci_py = m.params.get("tci_z", float("nan"))
            dai_py = m.params.get("dai_z", float("nan"))
            L.append(f"| {wave} | {int(m.nobs)} | {n_paper} | "
                     f"{fmt(tci_py)} | {tci_paper:.3f} | "
                     f"{fmt(dai_py)} | {dai_paper:.3f} |")
    if "pooled" in results["baseline"]:
        m = results["baseline"]["pooled"]
        L.append(f"| pooled | {int(m.nobs)} | 2,971 | "
                 f"{fmt(m.params.get('tci_z'))} | 0.176 | "
                 f"{fmt(m.params.get('dai_z'))} | 0.154 |")

    # Lind-Mehlum
    L.append("\n### Block 1b. Lind–Mehlum p-values\n")
    L.append("| Wave | TP (%) | LM p (Py) | LM p (paper) |")
    L.append("|---|---|---|---|")
    paper_lm = {"2009": 0.060, "2015": 0.017, "2023": 0.029, "pooled": 0.002}
    for wave in ("2009", "2015", "2023", "pooled"):
        if wave in results.get("lm", {}):
            lm = results["lm"][wave]
            L.append(f"| {wave} | {fmt(lm['turning_point_pct'], 1)} | "
                     f"{fmt(lm['p_value'])} | {paper_lm[wave]:.3f} |")

    # Block 2 — Heckman + CF
    L.append("\n## Block 2. Heckman 2-step and CF (cross-check)\n")
    L.append("| Wave | Heckman λ | p(λ) | n_exp | CF GR | p(GR) |")
    L.append("|---|---|---|---|---|---|")
    for wave in ("2009", "2015", "2023", "pooled"):
        h = results.get("heckman", {}).get(wave, {})
        c = results.get("cf", {}).get(wave, {})
        L.append(f"| {wave} | "
                 f"{fmt(h.get('lambda'))} | {fmt(h.get('p_lambda'))} | "
                 f"{h.get('n_exporters', '—')} | "
                 f"{fmt(c.get('gr_coef'))} | {fmt(c.get('p_gr'))} |")

    # Block 3 — 2-digit ISIC
    L.append("\n## Block 3. 2-digit ISIC sector FE (Δ% vs broad-sector baseline)\n")
    L.append("| Wave | ΔFSTS_c | ΔFSTS_c² | ΔTCI_z | ΔDAI_z |")
    L.append("|---|---|---|---|---|")
    for wave in ("2009", "2015", "2023", "pooled"):
        d = results.get("isic2d", {}).get(wave, {})
        L.append(f"| {wave} | "
                 f"{fmt(d.get('fsts_c'), 1)}% | {fmt(d.get('fsts_c2'), 1)}% | "
                 f"{fmt(d.get('tci_z'), 1)}% | {fmt(d.get('dai_z'), 1)}% |")

    # Block 4 — k33/k38 verification
    L.append("\n## Block 4. k33/k38 e-payment item verification\n")
    for wave, info in results.get("epay_check", {}).items():
        L.append(f"- **Wave {wave}:** {info}")

    # Block 5 — Micro-firm exclusion
    L.append("\n## Block 5. Micro-firm exclusion (l1 ≥ 10)\n")
    L.append("| Wave | N (subset) | ΔFSTS_c | ΔFSTS_c² | ΔTCI_z | ΔDAI_z |")
    L.append("|---|---|---|---|---|---|")
    for wave in ("2009", "2015", "2023", "pooled"):
        d = results.get("micro_excl", {}).get(wave, {})
        L.append(f"| {wave} | {d.get('n', '—')} | "
                 f"{fmt(d.get('fsts_c'), 1)}% | {fmt(d.get('fsts_c2'), 1)}% | "
                 f"{fmt(d.get('tci_z'), 1)}% | {fmt(d.get('dai_z'), 1)}% |")

    # Block 6 — TCI_full
    L.append("\n## Block 6. TCI_full robustness (h1/h8 added)\n")
    L.append("| Wave | n_valid | β TCI_full | Δ% vs TCI_thin |")
    L.append("|---|---|---|---|")
    for wave in ("2015", "2023"):
        d = results.get("tci_full", {}).get(wave, {})
        L.append(f"| {wave} | {d.get('n_valid', '—')} | "
                 f"{fmt(d.get('beta'))} | {fmt(d.get('delta_pct'), 1)}% |")

    # Block 7 — DAI_rich
    L.append("\n## Block 7. DAI_rich robustness (k33, k38 added; 2023 only)\n")
    L.append("| Spec | N | β DAI_rich | SE | p | vs paper claim 0.329, p=.028 |")
    L.append("|---|---|---|---|---|---|")
    for spec in ("continuous", "binary"):
        d = results.get("dai_rich", {}).get(spec, {})
        match = ""
        if d.get("beta") is not None and not np.isnan(d.get("beta", float("nan"))):
            if 0.30 < d["beta"] < 0.35 and d.get("p", 1) < 0.05:
                match = "✓ matches paper"
            else:
                match = "✗ does not match"
        L.append(f"| {spec} | {d.get('n', '—')} | "
                 f"{fmt(d.get('beta'))} | {fmt(d.get('se'))} | "
                 f"{fmt(d.get('p'))} | {match} |")

    L.append("\n---\n")
    L.append("## Interpretation guide\n")
    L.append("- **Block 1 baseline must agree with paper Table 2 to within ~0.01.** "
             "If gap > 0.05, listwise deletion or z-standardisation specification "
             "in Stata differs from this script; reconcile before trusting later blocks.")
    L.append("- **Block 2 Heckman/CF should match Stata twostep output.**")
    L.append("- **Block 3, 5: Δ% ranges feed directly into response letter mục 5.**")
    L.append("- **Block 7: if neither continuous nor binary k33/k38 reproduces "
             "paper's 0.329, paper claim must be revisited with co-authors.**")

    outpath.write_text("\n".join(L), encoding="utf-8")


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--files", nargs="+", required=True,
                    help="Paths to WBES Vietnam .dta files (any order)")
    ap.add_argument("--outdir", default="./check_output",
                    help="Output directory (default: ./check_output)")
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    # ----- Section 1: Load + listwise -----
    print("\n[1/6] Loading and applying listwise deletion ...")
    raw = {}
    for f in args.files:
        wave, df = load_wave(Path(f))
        raw[wave] = df
    clean = apply_listwise(raw)

    # ----- Section 2: Build variables -----
    print("\n[2/6] Building variables ...")
    built = {wave: build_variables(df, wave) for wave, df in clean.items()}
    # Preserve original wave index so robustness blocks can merge optional vars
    # (h1/h8/k33/k38) back onto the pooled frame without ambiguity.
    pool = pd.concat(built.values(), ignore_index=False)

    # Within-wave z-standardisation
    pool["tci_z"] = zstd_within_wave(pool, "tci_thin")
    pool["dai_z"] = zstd_within_wave(pool, "dai_core")

    # Save analytic dataset
    pool_out = pool[[c for c in pool.columns if c in
                     ["wave", "lnLP", "fsts", "fsts_c", "fsts_c2",
                      "tci_thin", "dai_core", "tci_z", "dai_z",
                      "lnemp", "firmage", "foreign_owned",
                      "sector_broad", "sector_2d"]]]
    pool_out.to_csv(outdir / "p4_python_baseline.csv", index=False)
    print(f"  Saved analytic dataset -> {outdir/'p4_python_baseline.csv'}")

    results: dict = {}

    # ----- Section 3: Baseline OLS + Lind-Mehlum -----
    print("\n[3/6] Baseline OLS-HC1 + Lind-Mehlum ...")
    results["baseline"] = {}
    results["lm"] = {}
    for wave in ("2009", "2015", "2023"):
        sub = pool[pool["wave"] == wave]
        if len(sub) < 100:
            continue
        m = run_ols(sub)
        results["baseline"][wave] = m
        results["lm"][wave] = lind_mehlum_test(m)
    m_pool = run_ols(pool, include_wave_fe=True)
    results["baseline"]["pooled"] = m_pool
    results["lm"]["pooled"] = lind_mehlum_test(m_pool)
    print("  Baseline coefficients (TCI_z, DAI_z) by wave:")
    for wave, m in results["baseline"].items():
        print(f"    {wave}: TCI_z = {m.params.get('tci_z'):.3f}, "
              f"DAI_z = {m.params.get('dai_z'):.3f}, N = {int(m.nobs)}")

    # ----- Section 4: Heckman -----
    print("\n[4/6] Heckman 2-step ...")
    results["heckman"] = {}
    for wave in ("2009", "2015", "2023"):
        sub = pool[pool["wave"] == wave]
        if len(sub) < 100:
            continue
        h = heckman_twostep(sub)
        results["heckman"][wave] = h
    results["heckman"]["pooled"] = heckman_twostep(pool)

    # ----- Section 5: CF -----
    print("\n[5/6] Control Function ...")
    results["cf"] = {}
    for wave in ("2009", "2015", "2023"):
        sub = pool[pool["wave"] == wave]
        if len(sub) < 100:
            continue
        results["cf"][wave] = control_function(sub)
    results["cf"]["pooled"] = control_function(pool)

    # ----- Section 6: Robustness -----
    print("\n[6/6] Robustness specifications ...")

    # 2-digit ISIC
    results["isic2d"] = {}
    for wave in ("2009", "2015", "2023"):
        sub = pool[pool["wave"] == wave]
        if len(sub) < 100:
            continue
        m_2d = robustness_2digit_isic(sub)
        results["isic2d"][wave] = coef_delta(m_2d, results["baseline"][wave])
    m_2d_pool = robustness_2digit_isic(pool)
    results["isic2d"]["pooled"] = coef_delta(m_2d_pool, m_pool)

    # k33/k38 verification
    results["epay_check"] = {}
    for wave, df in built.items():
        n_k33 = df["k33"].notna().sum() if "k33" in df.columns else 0
        n_k38 = df["k38"].notna().sum() if "k38" in df.columns else 0
        if n_k33 == 0 and n_k38 == 0:
            results["epay_check"][wave] = "k33 and k38 absent from this wave"
        else:
            r33 = (df["k33"].min(), df["k33"].max()) if n_k33 else (None, None)
            r38 = (df["k38"].min(), df["k38"].max()) if n_k38 else (None, None)
            results["epay_check"][wave] = (f"k33 n_valid={n_k33} range={r33}, "
                                           f"k38 n_valid={n_k38} range={r38}")

    # Micro-firm exclusion
    results["micro_excl"] = {}
    for wave in ("2009", "2015", "2023"):
        sub = pool[pool["wave"] == wave]
        if len(sub) < 100:
            continue
        m_micro = robustness_micro_excl(sub)
        d = coef_delta(m_micro, results["baseline"][wave])
        d["n"] = int(m_micro.nobs)
        results["micro_excl"][wave] = d
    m_micro_pool = robustness_micro_excl(pool)
    d_pool = coef_delta(m_micro_pool, m_pool)
    d_pool["n"] = int(m_micro_pool.nobs)
    results["micro_excl"]["pooled"] = d_pool

    # TCI_full — merge h1/h8 from `built` onto pool subset by intersecting index
    results["tci_full"] = {}
    for wave in ("2015", "2023"):
        sub = built.get(wave)
        if sub is None:
            continue
        sub_z = pool[pool["wave"] == wave].copy()
        common_idx = sub_z.index.intersection(sub.index)
        for v in INNOVATION_VARS:
            sub_z[v] = pd.NA
            if v in sub.columns:
                sub_z.loc[common_idx, v] = sub.loc[common_idx, v]
            sub_z[v] = pd.to_numeric(sub_z[v], errors="coerce")
        m_full = robustness_tci_full(sub_z, wave)
        if m_full is None:
            continue
        beta_full = m_full.params.get("tci_z", float("nan"))
        beta_thin = results["baseline"][wave].params.get("tci_z", float("nan"))
        delta = (100 * (beta_full - beta_thin) / abs(beta_thin)
                 if abs(beta_thin) > 1e-6 else float("nan"))
        n_valid = int(m_full.nobs)
        results["tci_full"][wave] = {"n_valid": n_valid, "beta": beta_full,
                                     "delta_pct": delta}

    # DAI_rich (2023 only, both specs)
    results["dai_rich"] = {}
    sub_2023 = pool[pool["wave"] == "2023"].copy()
    common_idx = sub_2023.index.intersection(built["2023"].index)
    for v in EPAYMENT_VARS:
        sub_2023[v] = pd.NA
        if v in built["2023"].columns:
            sub_2023.loc[common_idx, v] = built["2023"].loc[common_idx, v]
        sub_2023[v] = pd.to_numeric(sub_2023[v], errors="coerce")
    for spec in ("continuous", "binary"):
        m_rich = robustness_dai_rich(sub_2023, mode=spec)
        if m_rich is None:
            results["dai_rich"][spec] = {}
            continue
        results["dai_rich"][spec] = {
            "n": int(m_rich.nobs),
            "beta": m_rich.params.get("dai_z", float("nan")),
            "se": m_rich.bse.get("dai_z", float("nan")),
            "p": m_rich.pvalues.get("dai_z", float("nan"))}

    # ----- Build report -----
    build_report(results, outdir / "p4_python_check.md")
    print(f"\n[done] Report written to {outdir/'p4_python_check.md'}")
    print(f"       Analytic dataset to {outdir/'p4_python_baseline.csv'}")
    print("\nNext step: cross-check Block 1 baseline vs paper Table 2.")
    print("If TCI_z or DAI_z gaps > 0.05, debug listwise/z-std before trusting later blocks.")


if __name__ == "__main__":
    main()
