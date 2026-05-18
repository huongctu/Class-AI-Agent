"""
R3 Phase 2 — Bootstrap CI for the turning point of FSTS in M2 and M8.

The manuscript reports turning point ≈ 82.4% (from M2). Reviewer #4
notes this point lies in the thinnest portion of empirical support
(only ~3% of firms have FSTS > 70%), so a single point estimate is
inadequate. Quantify uncertainty with cluster-bootstrap CI.

Method:
  - 5,000 bootstrap reps with replacement (firm-level, no clusters)
  - For each rep, refit M2 and compute turning point: -β1 / (2 β2)
  - Report 95% percentile CI for the turning point on the FSTS scale (%)

Outputs:
  outputs/r3/audit/bootstrap_tp.json
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
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

N_REPS = 5000
SEED = 20260502


def load_clean():
    df, _ = pyreadstat.read_dta(str(DTA))
    for col in ["b2b", "d2", "l1", "b5", "d3c", "a4a", "a4b_v4"]:
        df[col] = df[col].where(df[col] >= 0, np.nan)
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
    core = ["ln_lp", "fsts", "ln_empl", "firm_age", "foreign", "broad_sector"]
    return df[df[core].notna().all(axis=1)].copy()


def fit_m2(df):
    df = df.copy()
    fsts_mean = df["fsts"].mean()
    df["fsts_c"] = df["fsts"] - fsts_mean
    df["fsts_c2"] = df["fsts_c"] ** 2
    formula = ("ln_lp ~ fsts_c + fsts_c2 + ln_empl + firm_age + foreign"
               " + C(broad_sector)")
    m = smf.ols(formula, data=df).fit()
    b1 = m.params["fsts_c"]
    b2 = m.params["fsts_c2"]
    if abs(b2) < 1e-9:
        return None, fsts_mean, b1, b2
    tp_centered = -b1 / (2 * b2)
    tp_pct = (tp_centered + fsts_mean) * 100
    return tp_pct, fsts_mean, b1, b2


def main():
    print("=" * 72)
    print("R3 Phase 2 — Bootstrap CI for turning point (M2)")
    print(f"  Reps: {N_REPS}, seed: {SEED}")
    print("=" * 72)

    df = load_clean().reset_index(drop=True)
    n = len(df)
    print(f"\nClean sample: N = {n}")

    tp_full, fsts_mean, b1, b2 = fit_m2(df)
    print(f"Full-sample M2: β1 = {b1:+.3f}, β2 = {b2:+.3f}, "
          f"turning point = {tp_full:.2f}%")

    rng = np.random.default_rng(SEED)
    tps = []
    valid = 0
    inverted_u_count = 0
    for r in range(N_REPS):
        idx = rng.choice(n, size=n, replace=True)
        sub = df.iloc[idx]
        try:
            tp, _, b1_b, b2_b = fit_m2(sub)
            if tp is None or not np.isfinite(tp):
                continue
            tps.append(tp)
            valid += 1
            if b2_b < 0 and b1_b > 0:
                inverted_u_count += 1
        except Exception:
            continue
        if (r + 1) % 1000 == 0:
            print(f"  rep {r+1}/{N_REPS} complete")

    tps = np.array(tps)
    print(f"\n{valid}/{N_REPS} reps yielded a finite turning point")
    print(f"Inverted-U shape (β1>0 & β2<0) in {inverted_u_count}/{N_REPS} reps "
          f"({inverted_u_count/N_REPS*100:.1f}%)")

    # Filter out absurd values (way outside any meaningful FSTS range)
    tp_finite = tps[(tps > -200) & (tps < 500)]
    print(f"After clipping to [-200, 500]: {len(tp_finite)} reps")

    pct = np.percentile(tp_finite, [2.5, 25, 50, 75, 97.5])
    pct_in_range = (((tp_finite >= 0) & (tp_finite <= 100)).mean()) * 100

    print(f"\nBootstrap distribution of turning point (%):")
    print(f"  2.5%   = {pct[0]:>8.2f}")
    print(f"  25%    = {pct[1]:>8.2f}")
    print(f"  Median = {pct[2]:>8.2f}")
    print(f"  75%    = {pct[3]:>8.2f}")
    print(f"  97.5%  = {pct[4]:>8.2f}")
    print(f"  → 95% percentile CI: [{pct[0]:.1f}, {pct[4]:.1f}]")
    print(f"  → % of bootstrap reps with TP in [0, 100]: "
          f"{pct_in_range:.1f}%")

    summary = {
        "n_reps": N_REPS,
        "n_valid": int(valid),
        "n_after_clip": int(len(tp_finite)),
        "full_sample_tp_pct": float(tp_full),
        "boot_ci_95": [float(pct[0]), float(pct[4])],
        "boot_iqr": [float(pct[1]), float(pct[3])],
        "boot_median": float(pct[2]),
        "pct_inverted_U_shape": float(inverted_u_count / N_REPS * 100),
        "pct_TP_in_0_100_range": float(pct_in_range),
    }
    out = AUDIT_DIR / "bootstrap_tp.json"
    out.write_text(json.dumps(summary, indent=2))
    print(f"\nWrote: {out}")

    # Verdict
    print("\n" + "=" * 72)
    print("Verdict: how informative is the turning-point estimate?")
    print("=" * 72)
    width = pct[4] - pct[0]
    if width < 30:
        print(f"  CI width = {width:.0f} pp — turning point is reasonably "
              f"well-identified.")
    elif width < 80:
        print(f"  CI width = {width:.0f} pp — turning point is only loosely "
              f"identified; treat 82.4% as indicative, not precise.")
    else:
        print(f"  CI width = {width:.0f} pp — turning point is weakly "
              f"identified. The reported 82.4% should be reframed as a")
        print(f"  descriptive observation; the curvature is not precisely")
        print(f"  pinned down by these data.")


if __name__ == "__main__":
    main()
