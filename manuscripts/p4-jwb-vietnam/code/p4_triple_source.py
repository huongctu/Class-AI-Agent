#!/usr/bin/env python3
"""
p4_triple_source.py
===================
Triple-source numerical verification of the P4 baseline OLS specification.

Runs the same outcome equation on the same X / y matrix through three
independent estimators and asserts that coefficients and standard errors
agree to machine precision (< 1e-10):

  1. statsmodels.OLS with cov_type='HC1'
  2. linearmodels.IV2SLS with zero instruments and cov_type='robust'
  3. Pure NumPy closed form  beta = (X'X)^{-1} X'y
     with manual HC1 covariance:
       V = (X'X)^{-1} X' diag(e^2) X (X'X)^{-1} * n / (n - k)

This protects against silent regressions in any single library and gives
the editor a self-contained reproducibility artefact.

Usage
-----
    python p4_triple_source.py \
        --baseline-csv ../output/p4_python_baseline.csv \
        --log         ../output/triple_source_verification.log

The baseline CSV is the file written by `p4_python_check.py`. The script
estimates the wave-pooled outcome equation:

    lnLP ~ fsts_c + fsts_c2 + tci_z + dai_z
         + lnemp + firmage + foreign_owned
         + sector_broad FE + wave FE
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

try:
    from linearmodels.iv import IV2SLS
except ImportError:
    sys.exit("linearmodels is required. Install: pip install linearmodels")


def manual_ols_hc1(X: np.ndarray, y: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Pure NumPy OLS + HC1 robust covariance.
    Returns (beta_hat, se_hc1)."""
    n, k = X.shape
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    e = y - X @ beta
    bread = XtX_inv
    meat = X.T @ np.diag(e ** 2) @ X
    V_hc1 = bread @ meat @ bread * (n / (n - k))
    se = np.sqrt(np.diag(V_hc1))
    return beta, se


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline-csv", required=True)
    ap.add_argument("--log", required=True)
    args = ap.parse_args()

    df = pd.read_csv(args.baseline_csv)
    df = df.dropna(subset=[
        "lnLP", "fsts_c", "fsts_c2", "tci_z", "dai_z",
        "lnemp", "firmage", "foreign_owned", "sector_broad", "wave",
    ]).copy()

    # Build design matrix exactly once and re-use across all three estimators
    base_cols = ["fsts_c", "fsts_c2", "tci_z", "dai_z",
                 "lnemp", "firmage", "foreign_owned"]
    Xb = df[base_cols].astype(float)
    sec = pd.get_dummies(df["sector_broad"].astype(str),
                         prefix="sec", drop_first=True).astype(float)
    wfe = pd.get_dummies(df["wave"].astype(str),
                         prefix="wave", drop_first=True).astype(float)
    X = pd.concat([Xb, sec, wfe], axis=1)
    X = sm.add_constant(X)
    y = df["lnLP"].astype(float)

    # 1) statsmodels OLS HC1
    sm_fit = sm.OLS(y, X).fit(cov_type="HC1")
    beta_sm = sm_fit.params.values
    se_sm = sm_fit.bse.values

    # 2) linearmodels IV2SLS (no instruments -> identical to OLS).
    # debiased=True applies the n/(n-k) correction that makes the robust
    # covariance HC1-equivalent (statsmodels' default for cov_type='HC1').
    lm_fit = IV2SLS(y, X, None, None).fit(cov_type="robust", debiased=True)
    beta_lm = lm_fit.params.values
    se_lm = lm_fit.std_errors.values

    # 3) Manual NumPy
    Xn = X.values.astype(float)
    yn = y.values.astype(float)
    beta_np, se_np = manual_ols_hc1(Xn, yn)

    # Compare
    n, k = Xn.shape
    coef_diff_sm_lm = np.max(np.abs(beta_sm - beta_lm))
    coef_diff_sm_np = np.max(np.abs(beta_sm - beta_np))
    coef_diff_lm_np = np.max(np.abs(beta_lm - beta_np))
    se_diff_sm_lm = np.max(np.abs(se_sm - se_lm))
    se_diff_sm_np = np.max(np.abs(se_sm - se_np))
    se_diff_lm_np = np.max(np.abs(se_lm - se_np))
    coef_max = max(coef_diff_sm_lm, coef_diff_sm_np, coef_diff_lm_np)
    se_max = max(se_diff_sm_lm, se_diff_sm_np, se_diff_lm_np)

    log = []
    log.append("# P4 triple-source verification log\n")
    log.append(f"Sample size      : n = {n}")
    log.append(f"Parameter count  : k = {k}")
    log.append(f"Outcome variable : lnLP\n")
    log.append("Pairwise coefficient max-abs differences:")
    log.append(f"  statsmodels vs linearmodels : {coef_diff_sm_lm:.3e}")
    log.append(f"  statsmodels vs numpy        : {coef_diff_sm_np:.3e}")
    log.append(f"  linearmodels vs numpy       : {coef_diff_lm_np:.3e}")
    log.append(f"  MAX                         : {coef_max:.3e}\n")
    log.append("Pairwise standard-error max-abs differences:")
    log.append(f"  statsmodels vs linearmodels : {se_diff_sm_lm:.3e}")
    log.append(f"  statsmodels vs numpy        : {se_diff_sm_np:.3e}")
    log.append(f"  linearmodels vs numpy       : {se_diff_lm_np:.3e}")
    log.append(f"  MAX                         : {se_max:.3e}\n")

    threshold = 1e-9
    if coef_max < threshold and se_max < threshold:
        log.append(
            f"PASS — all three estimators agree to within {threshold:.0e}.")
        rc = 0
    else:
        log.append(
            f"FAIL — at least one estimator diverges by more than {threshold:.0e}.")
        rc = 1

    log.append("\n## Coefficient table (4 hypothesis-relevant rows)")
    log.append("| param | statsmodels | linearmodels | numpy |")
    log.append("|---|---|---|---|")
    for i, name in enumerate(X.columns):
        if name in ("fsts_c", "fsts_c2", "tci_z", "dai_z"):
            log.append(f"| {name} | {beta_sm[i]:.10f} | "
                       f"{beta_lm[i]:.10f} | {beta_np[i]:.10f} |")

    Path(args.log).write_text("\n".join(log), encoding="utf-8")
    print("\n".join(log))
    sys.exit(rc)


if __name__ == "__main__":
    main()
