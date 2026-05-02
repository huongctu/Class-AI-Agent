"""P4 Vietnam analysis pipeline (Python equivalent of the Stata blueprint).

Loads the three Vietnam WBES waves, builds harmonised analytic files, runs the
M0–M8 nested OLS sequence per wave and pooled with HC1 robust standard errors,
applies a Lind–Mehlum-style turning-point check, and emits the manuscript-
facing CSV outputs.

Run from repo root:
    python3 scripts/p4_vietnam_analysis.py

Outputs land under /home/user/Class-AI-Agent/p4_vietnam/output/.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat
import statsmodels.api as sm
from scipy import stats

ROOT = Path("/home/user/Class-AI-Agent/p4_vietnam")
OUT_TABLES = ROOT / "output" / "tables"
OUT_TABLES.mkdir(parents=True, exist_ok=True)
OUT_LOGS = ROOT / "output" / "logs"
OUT_LOGS.mkdir(parents=True, exist_ok=True)

RAW = {
    2009: "/root/.claude/uploads/baf64a94-2e13-4dbf-8dcc-22587a547e56/360621d3-Vietnam2009fulldata.dta",
    2015: "/root/.claude/uploads/baf64a94-2e13-4dbf-8dcc-22587a547e56/17205265-Vietnam2015fulldata.dta",
    2023: "/root/.claude/uploads/baf64a94-2e13-4dbf-8dcc-22587a547e56/e2b1dd4a-VietNam2023fulldata.dta",
}


def read_dta(path: str) -> pd.DataFrame:
    try:
        df, _ = pyreadstat.read_dta(path)
    except Exception:
        df, _ = pyreadstat.read_dta(path, encoding="latin1")
    return df


def to_numeric(s: pd.Series) -> pd.Series:
    return pd.to_numeric(s, errors="coerce")


def clean_missing(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    """Convert WBES non-response codes (-9 don't know, -6 not applicable) to NaN."""
    for c in cols:
        if c in df.columns:
            df[c] = to_numeric(df[c])
            df.loc[df[c].isin([-9, -6, -7, -8]), c] = np.nan
    return df


def recode_yesno(s: pd.Series) -> pd.Series:
    """WBES 1/2 → 1/0 binary."""
    return s.map({1: 1, 2: 0})


def first_digit(x: float) -> float:
    if pd.isna(x):
        return np.nan
    s = str(int(x))
    return float(s[0])


def build_wave(year: int) -> pd.DataFrame:
    df = read_dta(RAW[year])
    df["wave"] = year
    df = clean_missing(
        df,
        ["d2", "l1", "d3c", "b8", "e6", "c22b", "b2b", "b5", "a2",
         "a4a", "a4b", "h1", "h8", "k33", "k38"],
    )
    df["lnLP"] = np.log(df["d2"] / df["l1"])
    df["lnEmp"] = np.log(df["l1"])
    df["FirmAge"] = year - df["b5"]
    df["ForeignOwned"] = (df["b2b"] > 0).astype(float)
    df.loc[df["b2b"].isna(), "ForeignOwned"] = np.nan
    df["FSTS"] = df["d3c"] / 100.0
    df["export_any"] = (df["FSTS"] > 0).astype(float)
    df.loc[df["FSTS"].isna(), "export_any"] = np.nan

    df["b8_r"] = recode_yesno(df["b8"])
    df["e6_r"] = recode_yesno(df["e6"])
    df["c22b_r"] = recode_yesno(df["c22b"])
    df["TCI_thin"] = df[["b8_r", "e6_r"]].mean(axis=1)
    df["DAI_thin"] = df["c22b_r"]

    if year in (2015, 2023):
        df["h1_r"] = recode_yesno(df["h1"])
        if year == 2023:
            df["h8_r"] = recode_yesno(df["h8"])
        else:
            df["h8_r"] = (df["h8"] > 0).astype(float)
            df.loc[df["h8"].isna(), "h8_r"] = np.nan
        df["TCI_full"] = df[["b8_r", "e6_r", "h1_r", "h8_r"]].mean(axis=1)

    if year == 2023:
        df["k33b"] = (df["k33"] > 0).astype(float)
        df.loc[df["k33"].isna(), "k33b"] = np.nan
        df["k38b"] = (df["k38"] > 0).astype(float)
        df.loc[df["k38"].isna(), "k38b"] = np.nan
        df["k33c"] = df["k33"] / 100.0
        df["k38c"] = df["k38"] / 100.0
        df["DAI_rich_cont"] = df[["c22b_r", "k33c", "k38c"]].mean(axis=1)
        df["DAI_rich_bin"] = df[["c22b_r", "k33b", "k38b"]].mean(axis=1)

    if "a4b" in df.columns and year in (2009, 2015):
        df["sector1"] = df["a4b"].apply(first_digit)
    else:
        df["sector1"] = df["a4a"].apply(first_digit)

    focal = ["lnLP", "lnEmp", "FirmAge", "ForeignOwned", "FSTS", "TCI_thin", "DAI_thin", "sector1"]
    df = df.dropna(subset=focal).copy()

    fmean = df["FSTS"].mean()
    df["FSTSc"] = df["FSTS"] - fmean
    df["FSTSc2"] = df["FSTSc"] ** 2

    df["TCI_z"] = (df["TCI_thin"] - df["TCI_thin"].mean()) / df["TCI_thin"].std(ddof=1)
    df["DAI_z"] = (df["DAI_thin"] - df["DAI_thin"].mean()) / df["DAI_thin"].std(ddof=1)

    if "TCI_full" in df.columns:
        sub = df.dropna(subset=["TCI_full"])
        if len(sub) > 1:
            mu, sd = sub["TCI_full"].mean(), sub["TCI_full"].std(ddof=1)
            df["TCI_full_z"] = (df["TCI_full"] - mu) / sd

    if "DAI_rich_cont" in df.columns:
        for col in ["DAI_rich_cont", "DAI_rich_bin"]:
            sub = df.dropna(subset=[col])
            if len(sub) > 1:
                mu, sd = sub[col].mean(), sub[col].std(ddof=1)
                df[f"{col}_z"] = (df[col] - mu) / sd

    return df


def build_pooled(waves: dict[int, pd.DataFrame]) -> pd.DataFrame:
    pooled = pd.concat(waves.values(), ignore_index=True, sort=False)
    pooled["FSTSc"] = pooled.groupby("wave")["FSTS"].transform(lambda s: s - s.mean())
    pooled["FSTSc2"] = pooled["FSTSc"] ** 2
    pooled["TCI_z"] = pooled.groupby("wave")["TCI_thin"].transform(
        lambda s: (s - s.mean()) / s.std(ddof=1)
    )
    pooled["DAI_z"] = pooled.groupby("wave")["DAI_thin"].transform(
        lambda s: (s - s.mean()) / s.std(ddof=1)
    )
    return pooled


def design_matrix(df: pd.DataFrame, terms: list[str], extra_dummies: list[str] | None = None) -> tuple[np.ndarray, list[str]]:
    """Return (X, names) with intercept and one-hot for categorical sector / wave."""
    parts = []
    names = ["const"]
    parts.append(np.ones((len(df), 1)))
    for t in terms:
        parts.append(df[t].to_numpy().reshape(-1, 1))
        names.append(t)
    if extra_dummies:
        for cat in extra_dummies:
            d = pd.get_dummies(df[cat].astype(int), prefix=cat, drop_first=True, dtype=float)
            parts.append(d.to_numpy())
            names.extend(d.columns.tolist())
    X = np.hstack(parts)
    return X, names


def fit_ols_hc1(df: pd.DataFrame, terms: list[str], dummies: list[str]) -> dict:
    X, names = design_matrix(df, terms, dummies)
    y = df["lnLP"].to_numpy()
    model = sm.OLS(y, X)
    fit = model.fit(cov_type="HC1")
    return {
        "names": names,
        "b": fit.params,
        "se": fit.bse,
        "p": fit.pvalues,
        "vcov": fit.cov_params(),
        "n": int(fit.nobs),
        "r2": float(fit.rsquared),
        "fit": fit,
    }


def joint_test(fit_dict: dict, terms_to_test: list[str]) -> tuple[float, float]:
    """Wald F-test on a subset of coefficients (with HC1 covariance)."""
    names = fit_dict["names"]
    b = np.asarray(fit_dict["b"])
    V = np.asarray(fit_dict["vcov"])
    R = np.zeros((len(terms_to_test), len(names)))
    for i, t in enumerate(terms_to_test):
        R[i, names.index(t)] = 1.0
    Rb = R @ b
    RVR = R @ V @ R.T
    try:
        wald = float(Rb.T @ np.linalg.solve(RVR, Rb))
    except np.linalg.LinAlgError:
        return (np.nan, np.nan)
    df1 = len(terms_to_test)
    df2 = fit_dict["n"] - len(names)
    F = wald / df1
    p = 1 - stats.f.cdf(F, df1, df2)
    return float(F), float(p)


def turning_point(fit_dict: dict, fsts_mean: float) -> dict:
    names = fit_dict["names"]
    b = np.asarray(fit_dict["b"])
    V = np.asarray(fit_dict["vcov"])
    i1, i2 = names.index("FSTSc"), names.index("FSTSc2")
    b1, b2 = b[i1], b[i2]
    if b2 == 0:
        return {"tp_centred": np.nan, "tp_lo": np.nan, "tp_hi": np.nan, "tp_raw": np.nan}
    tp_c = -b1 / (2 * b2)
    grad = np.array([-1 / (2 * b2), b1 / (2 * b2 ** 2)])
    cov = V[np.ix_([i1, i2], [i1, i2])]
    var_tp = float(grad @ cov @ grad.T)
    se_tp = float(np.sqrt(max(var_tp, 0.0)))
    return {
        "tp_centred": float(tp_c),
        "tp_se": se_tp,
        "tp_lo": float(tp_c - 1.96 * se_tp),
        "tp_hi": float(tp_c + 1.96 * se_tp),
        "tp_raw": float(tp_c + fsts_mean),
        "tp_raw_lo": float(tp_c + fsts_mean - 1.96 * se_tp),
        "tp_raw_hi": float(tp_c + fsts_mean + 1.96 * se_tp),
    }


def lind_mehlum_p(fit_dict: dict, fsts_min: float, fsts_max: float) -> float:
    """Sasabuchi-style one-sided test for an inverted-U over [fsts_min, fsts_max].
    Reports the maximum of the two endpoint p-values (Lind & Mehlum 2010 §3)."""
    names = fit_dict["names"]
    b = np.asarray(fit_dict["b"])
    V = np.asarray(fit_dict["vcov"])
    i1, i2 = names.index("FSTSc"), names.index("FSTSc2")

    def slope_at(x):
        s = b[i1] + 2 * b[i2] * x
        g = np.zeros(len(b))
        g[i1] = 1.0
        g[i2] = 2 * x
        var = float(g @ V @ g.T)
        return s, np.sqrt(max(var, 0.0))

    s_lo, se_lo = slope_at(fsts_min)
    s_hi, se_hi = slope_at(fsts_max)
    t_lo = s_lo / se_lo if se_lo > 0 else np.inf
    t_hi = s_hi / se_hi if se_hi > 0 else -np.inf
    p_lo = 1 - stats.norm.cdf(t_lo)
    p_hi = stats.norm.cdf(t_hi)
    return float(max(p_lo, p_hi))


def run_models(df: pd.DataFrame, label: str, dummies: list[str]) -> dict:
    """Run M0–M8 + LM tests and capture all needed quantities for a sample."""
    out: dict = {"label": label, "n": len(df)}
    base = ["lnEmp", "FirmAge", "ForeignOwned"]

    M0 = fit_ols_hc1(df, base, dummies)
    out["M0"] = M0

    M1 = fit_ols_hc1(df, ["FSTSc"] + base, dummies)
    out["M1"] = M1

    M2 = fit_ols_hc1(df, ["FSTSc", "FSTSc2"] + base, dummies)
    out["M2"] = M2
    fsts_mean = df["FSTS"].mean()
    out["TP"] = turning_point(M2, fsts_mean)
    out["LM_p"] = lind_mehlum_p(M2, df["FSTSc"].min(), df["FSTSc"].max())
    out["FSTS_min"] = float(df["FSTS"].min())
    out["FSTS_max"] = float(df["FSTS"].max())

    df3 = df.copy()
    df3["FSTSc_TCIz"] = df3["FSTSc"] * df3["TCI_z"]
    df3["FSTSc2_TCIz"] = df3["FSTSc2"] * df3["TCI_z"]
    M3 = fit_ols_hc1(df3, ["FSTSc", "FSTSc2", "TCI_z", "FSTSc_TCIz", "FSTSc2_TCIz"] + base, dummies)
    F, p = joint_test(M3, ["FSTSc_TCIz", "FSTSc2_TCIz"])
    out["M3"] = M3
    out["M3_jointF"] = F
    out["M3_jointp"] = p

    df4 = df.copy()
    df4["FSTSc_DAIz"] = df4["FSTSc"] * df4["DAI_z"]
    df4["FSTSc2_DAIz"] = df4["FSTSc2"] * df4["DAI_z"]
    M4 = fit_ols_hc1(df4, ["FSTSc", "FSTSc2", "DAI_z", "FSTSc_DAIz", "FSTSc2_DAIz"] + base, dummies)
    F, p = joint_test(M4, ["FSTSc_DAIz", "FSTSc2_DAIz"])
    out["M4"] = M4
    out["M4_jointF"] = F
    out["M4_jointp"] = p

    out["M5"] = fit_ols_hc1(df, ["FSTSc", "FSTSc2", "TCI_z"] + base, dummies)
    out["M6"] = fit_ols_hc1(df, ["FSTSc", "FSTSc2", "DAI_z"] + base, dummies)
    out["M7"] = fit_ols_hc1(df, ["FSTSc", "FSTSc2", "TCI_z", "DAI_z"] + base, dummies)

    df8 = df.copy()
    df8["FSTSc_DAIz"] = df8["FSTSc"] * df8["DAI_z"]
    df8["FSTSc2_DAIz"] = df8["FSTSc2"] * df8["DAI_z"]
    M8 = fit_ols_hc1(df8, ["FSTSc", "FSTSc2", "TCI_z", "DAI_z", "FSTSc_DAIz", "FSTSc2_DAIz"] + base, dummies)
    F, p = joint_test(M8, ["FSTSc_DAIz", "FSTSc2_DAIz"])
    out["M8"] = M8
    out["M8_jointF"] = F
    out["M8_jointp"] = p

    return out


def emit_long_coef_csv(per_sample_results: dict, path: Path) -> None:
    rows = []
    keep_terms = {
        "FSTSc", "FSTSc2", "TCI_z", "DAI_z",
        "FSTSc_TCIz", "FSTSc2_TCIz", "FSTSc_DAIz", "FSTSc2_DAIz",
        "lnEmp", "FirmAge", "ForeignOwned",
    }
    for sample, res in per_sample_results.items():
        for model_name in ["M0", "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8"]:
            fit = res.get(model_name)
            if fit is None:
                continue
            for j, term in enumerate(fit["names"]):
                if term not in keep_terms:
                    continue
                b = float(fit["b"][j])
                se = float(fit["se"][j])
                p = float(fit["p"][j])
                rows.append({
                    "sample": sample,
                    "model": model_name,
                    "term": term,
                    "b": round(b, 4),
                    "se": round(se, 4),
                    "p": round(p, 4),
                    "ci_lo": round(b - 1.96 * se, 4),
                    "ci_hi": round(b + 1.96 * se, 4),
                    "n": fit["n"],
                    "r2": round(fit["r2"], 4),
                })
    pd.DataFrame(rows).to_csv(path, index=False)


def emit_joint_F(per_sample_results: dict, path: Path) -> None:
    rows = []
    for sample, res in per_sample_results.items():
        for model_name, test_label in [("M3", "H2"), ("M4", "P1"), ("M8", "P1_full")]:
            F = res.get(f"{model_name}_jointF")
            p = res.get(f"{model_name}_jointp")
            if F is None:
                continue
            rows.append({
                "sample": sample,
                "model": model_name,
                "test": test_label,
                "F": round(float(F), 4),
                "p": round(float(p), 4),
            })
    pd.DataFrame(rows).to_csv(path, index=False)


def emit_lm(per_sample_results: dict, path: Path) -> None:
    rows = []
    for sample, res in per_sample_results.items():
        tp = res["TP"]
        rows.append({
            "sample": sample,
            "tp_raw": round(tp["tp_raw"], 4),
            "tp_raw_lo": round(tp["tp_raw_lo"], 4),
            "tp_raw_hi": round(tp["tp_raw_hi"], 4),
            "lm_p": round(res["LM_p"], 4),
            "fsts_min": round(res["FSTS_min"], 4),
            "fsts_max": round(res["FSTS_max"], 4),
            "n": res["n"],
        })
    pd.DataFrame(rows).to_csv(path, index=False)


def emit_descriptives(waves: dict[int, pd.DataFrame], pooled: pd.DataFrame, path: Path) -> None:
    rows = []
    for label, df in [("VNM2009", waves[2009]), ("VNM2015", waves[2015]),
                      ("VNM2023", waves[2023]), ("VNMpooled", pooled)]:
        rows.append({
            "sample": label,
            "N": len(df),
            "lnLP_mean": round(df["lnLP"].mean(), 3),
            "lnLP_sd": round(df["lnLP"].std(ddof=1), 3),
            "FSTS_mean": round(df["FSTS"].mean(), 3),
            "FSTS_sd": round(df["FSTS"].std(ddof=1), 3),
            "exp_any_share": round(df["export_any"].mean(), 3),
            "TCI_thin_mean": round(df["TCI_thin"].mean(), 3),
            "TCI_thin_sd": round(df["TCI_thin"].std(ddof=1), 3),
            "DAI_thin_mean": round(df["DAI_thin"].mean(), 3),
            "DAI_thin_sd": round(df["DAI_thin"].std(ddof=1), 3),
            "lnEmp_mean": round(df["lnEmp"].mean(), 3),
            "lnEmp_sd": round(df["lnEmp"].std(ddof=1), 3),
            "FirmAge_mean": round(df["FirmAge"].mean(), 1),
            "FirmAge_sd": round(df["FirmAge"].std(ddof=1), 1),
            "ForeignOwned_share": round(df["ForeignOwned"].mean(), 3),
        })
    pd.DataFrame(rows).to_csv(path, index=False)


def fit_with(df: pd.DataFrame, focal: list[str], dummies: list[str]) -> dict:
    fit = fit_ols_hc1(df, focal, dummies)
    return fit


def heckman_two_step(df: pd.DataFrame, focal: list[str], dummies: list[str],
                     selection_extra: str = "a2") -> dict:
    """Manual Heckman two-step with WBES sampling region as exclusion restriction.

    Selection probit: export_any ~ lnEmp + FirmAge + ForeignOwned + sector1 + a2
    Outcome (selected sample, FSTS > 0): focal terms + IMR.

    Returns dict with both the IMR-augmented OLS and the control-function
    variant (generalised residual), plus the selection probit summary.
    """
    sub = df.dropna(subset=["export_any", "lnEmp", "FirmAge", "ForeignOwned",
                            "sector1", selection_extra]).copy()

    parts = [np.ones((len(sub), 1)),
             sub["lnEmp"].to_numpy().reshape(-1, 1),
             sub["FirmAge"].to_numpy().reshape(-1, 1),
             sub["ForeignOwned"].to_numpy().reshape(-1, 1)]
    sec = pd.get_dummies(sub["sector1"].astype(int), prefix="sector1",
                         drop_first=True, dtype=float).reset_index(drop=True)
    parts.append(sec.to_numpy())
    a2 = pd.get_dummies(sub[selection_extra].astype(int), prefix=selection_extra,
                        drop_first=True, dtype=float).reset_index(drop=True)
    parts.append(a2.to_numpy())
    if "wave" in dummies:
        wf = pd.get_dummies(sub["wave"].astype(int), prefix="wave",
                            drop_first=True, dtype=float).reset_index(drop=True)
        parts.append(wf.to_numpy())
    Z = np.hstack(parts)

    try:
        probit = sm.Probit(sub["export_any"].to_numpy(), Z).fit(disp=False)
    except Exception:  # singular sector cell or perfect prediction
        return {"status": "selection_probit_failed"}

    xb = Z @ probit.params
    phi = stats.norm.pdf(xb)
    Phi = stats.norm.cdf(xb)
    Phi = np.clip(Phi, 1e-9, 1 - 1e-9)
    sub["imr"] = phi / Phi
    sub["gres"] = (sub["export_any"].to_numpy() * (phi / Phi)
                   - (1 - sub["export_any"].to_numpy()) * (phi / (1 - Phi)))

    selected = sub[sub["export_any"] == 1].copy()
    if len(selected) < 30:
        return {"status": "too_few_exporters"}
    fit_imr = fit_ols_hc1(selected, focal + ["imr"], dummies)
    fit_cf = fit_ols_hc1(sub, focal + ["gres"], dummies)

    return {
        "status": "ok",
        "n_total": len(sub),
        "n_selected": len(selected),
        "imr_b": float(fit_imr["b"][fit_imr["names"].index("imr")]),
        "imr_se": float(fit_imr["se"][fit_imr["names"].index("imr")]),
        "imr_p": float(fit_imr["p"][fit_imr["names"].index("imr")]),
        "gres_b": float(fit_cf["b"][fit_cf["names"].index("gres")]),
        "gres_se": float(fit_cf["se"][fit_cf["names"].index("gres")]),
        "gres_p": float(fit_cf["p"][fit_cf["names"].index("gres")]),
        "fit_imr": fit_imr,
        "fit_cf": fit_cf,
    }


def emit_selection_csv(per_sample_results: dict, path: Path) -> None:
    rows = []
    for sample, res in per_sample_results.items():
        h = res.get("Heckman")
        if h is None or h.get("status") != "ok":
            continue
        rows.append({
            "sample": sample,
            "n_total": h["n_total"],
            "n_selected": h["n_selected"],
            "imr_b": round(h["imr_b"], 4),
            "imr_se": round(h["imr_se"], 4),
            "imr_p": round(h["imr_p"], 4),
            "gres_b": round(h["gres_b"], 4),
            "gres_se": round(h["gres_se"], 4),
            "gres_p": round(h["gres_p"], 4),
        })
    pd.DataFrame(rows).to_csv(path, index=False)


def emit_paternoster_csv(per_sample_results: dict, path: Path) -> None:
    """Pairwise Paternoster (1998) z-tests on focal M7/M8 coefficients."""
    pairs = [("VNM2009", "VNM2015"), ("VNM2009", "VNM2023"), ("VNM2015", "VNM2023")]
    targets = [
        ("M7", "FSTSc"), ("M7", "FSTSc2"), ("M7", "TCI_z"), ("M7", "DAI_z"),
        ("M8", "FSTSc_DAIz"), ("M8", "FSTSc2_DAIz"),
    ]
    rows = []
    for a, b in pairs:
        for model, term in targets:
            ra = per_sample_results.get(a, {}).get(model)
            rb = per_sample_results.get(b, {}).get(model)
            if ra is None or rb is None:
                continue
            if term not in ra["names"] or term not in rb["names"]:
                continue
            ja, jb = ra["names"].index(term), rb["names"].index(term)
            b_a = float(ra["b"][ja])
            se_a = float(ra["se"][ja])
            b_b = float(rb["b"][jb])
            se_b = float(rb["se"][jb])
            z = (b_a - b_b) / np.sqrt(se_a**2 + se_b**2)
            p = 2 * (1 - stats.norm.cdf(abs(z)))
            rows.append({
                "model": model,
                "term": term,
                "pair": f"{a}_vs_{b}",
                "b_a": round(b_a, 4),
                "se_a": round(se_a, 4),
                "b_b": round(b_b, 4),
                "se_b": round(se_b, 4),
                "z": round(float(z), 4),
                "p": round(float(p), 4),
            })
    pd.DataFrame(rows).to_csv(path, index=False)


def extract_focal(fit: dict, terms: list[str], panel: str, sample: str) -> list[dict]:
    rows = []
    for t in terms:
        if t not in fit["names"]:
            continue
        j = fit["names"].index(t)
        b = float(fit["b"][j])
        se = float(fit["se"][j])
        rows.append({
            "panel": panel,
            "sample": sample,
            "term": t,
            "b": round(b, 4),
            "se": round(se, 4),
            "p": round(float(fit["p"][j]), 4),
            "n": fit["n"],
        })
    return rows


def run_robustness(waves: dict[int, pd.DataFrame], pooled: pd.DataFrame) -> list[dict]:
    rows: list[dict] = []
    base = ["lnEmp", "FirmAge", "ForeignOwned"]

    for y in (2015, 2023):
        df = waves[y].dropna(subset=["TCI_full_z"]).copy()
        df["FSTSc_TCIfull"] = df["FSTSc"] * df["TCI_full_z"]
        df["FSTSc2_TCIfull"] = df["FSTSc2"] * df["TCI_full_z"]
        fit_direct = fit_with(df, ["FSTSc", "FSTSc2", "TCI_full_z", "DAI_z"] + base, ["sector1"])
        rows.extend(extract_focal(
            fit_direct,
            ["FSTSc", "FSTSc2", "TCI_full_z", "DAI_z"],
            "TCI_full_direct",
            f"VNM{y}",
        ))
        fit_mod = fit_with(
            df,
            ["FSTSc", "FSTSc2", "TCI_full_z", "FSTSc_TCIfull", "FSTSc2_TCIfull"] + base,
            ["sector1"],
        )
        F, p = joint_test(fit_mod, ["FSTSc_TCIfull", "FSTSc2_TCIfull"])
        rows.extend(extract_focal(
            fit_mod,
            ["FSTSc", "FSTSc2", "TCI_full_z", "FSTSc_TCIfull", "FSTSc2_TCIfull"],
            "TCI_full_moderation",
            f"VNM{y}",
        ))
        rows.append({
            "panel": "TCI_full_moderation",
            "sample": f"VNM{y}",
            "term": "joint_F_TCI_full_interactions",
            "b": round(float(F), 4),
            "se": np.nan,
            "p": round(float(p), 4),
            "n": fit_mod["n"],
        })

    df23 = waves[2023]
    for spec, label in [("DAI_rich_cont_z", "DAI_rich_cont"), ("DAI_rich_bin_z", "DAI_rich_bin")]:
        sub = df23.dropna(subset=[spec]).copy()
        sub[f"FSTSc_{label}"] = sub["FSTSc"] * sub[spec]
        sub[f"FSTSc2_{label}"] = sub["FSTSc2"] * sub[spec]
        fit_full = fit_with(
            sub,
            ["FSTSc", "FSTSc2", "TCI_z", spec, f"FSTSc_{label}", f"FSTSc2_{label}"] + base,
            ["sector1"],
        )
        F, p = joint_test(fit_full, [f"FSTSc_{label}", f"FSTSc2_{label}"])
        rows.extend(extract_focal(
            fit_full,
            ["FSTSc", "FSTSc2", "TCI_z", spec, f"FSTSc_{label}", f"FSTSc2_{label}"],
            f"DAI_rich_2023_{label}",
            "VNM2023",
        ))
        rows.append({
            "panel": f"DAI_rich_2023_{label}",
            "sample": "VNM2023",
            "term": "joint_F_DAI_rich_interactions",
            "b": round(float(F), 4),
            "se": np.nan,
            "p": round(float(p), 4),
            "n": fit_full["n"],
        })

    common = df23.dropna(subset=["DAI_rich_cont_z"]).copy()
    common["FSTSc_DAIz"] = common["FSTSc"] * common["DAI_z"]
    common["FSTSc2_DAIz"] = common["FSTSc2"] * common["DAI_z"]
    fit_common = fit_with(
        common,
        ["FSTSc", "FSTSc2", "TCI_z", "DAI_z", "FSTSc_DAIz", "FSTSc2_DAIz"] + base,
        ["sector1"],
    )
    F, p = joint_test(fit_common, ["FSTSc_DAIz", "FSTSc2_DAIz"])
    rows.extend(extract_focal(
        fit_common,
        ["FSTSc", "FSTSc2", "TCI_z", "DAI_z", "FSTSc_DAIz", "FSTSc2_DAIz"],
        "DAI_thin_on_rich_sample_2023",
        "VNM2023",
    ))
    rows.append({
        "panel": "DAI_thin_on_rich_sample_2023",
        "sample": "VNM2023",
        "term": "joint_F_DAI_thin_interactions",
        "b": round(float(F), 4),
        "se": np.nan,
        "p": round(float(p), 4),
        "n": fit_common["n"],
    })

    macro = pooled[np.exp(pooled["lnEmp"]) >= 10].copy()
    macro["FSTSc_DAIz"] = macro["FSTSc"] * macro["DAI_z"]
    macro["FSTSc2_DAIz"] = macro["FSTSc2"] * macro["DAI_z"]
    fit_macro = fit_with(
        macro,
        ["FSTSc", "FSTSc2", "TCI_z", "DAI_z", "FSTSc_DAIz", "FSTSc2_DAIz"] + base,
        ["sector1", "wave"],
    )
    F, p = joint_test(fit_macro, ["FSTSc_DAIz", "FSTSc2_DAIz"])
    rows.extend(extract_focal(
        fit_macro,
        ["FSTSc", "FSTSc2", "TCI_z", "DAI_z", "FSTSc_DAIz", "FSTSc2_DAIz"],
        "micro_excluded_pooled",
        "VNMpooled_l1ge10",
    ))
    rows.append({
        "panel": "micro_excluded_pooled",
        "sample": "VNMpooled_l1ge10",
        "term": "joint_F_DAI_interactions",
        "b": round(float(F), 4),
        "se": np.nan,
        "p": round(float(p), 4),
        "n": fit_macro["n"],
    })

    return rows


def run_sector_split(pooled: pd.DataFrame) -> list[dict]:
    """Estimate the M2 / M7 / M8 specifications separately on manufacturing
    (sector1 in {1, 2, 3} — ISIC 15-37) and non-manufacturing (sector1 in
    {4, 5, 6, 7} — utilities, construction, wholesale/retail, transport,
    finance and other services). Both subsets retain wave fixed effects.
    Reports the focal coefficients plus the joint F-tests for TCI and DAI
    moderation so reviewers can compare the two sub-samples directly.
    """
    rows: list[dict] = []
    base = ["lnEmp", "FirmAge", "ForeignOwned"]

    splits = {
        "manufacturing": pooled[pooled["sector1"].isin([1, 2, 3])].copy(),
        "non_manufacturing": pooled[pooled["sector1"].isin([4, 5, 6, 7])].copy(),
    }

    for label, df in splits.items():
        n = len(df)
        for v in ["FSTSc_TCIz", "FSTSc2_TCIz", "FSTSc_DAIz", "FSTSc2_DAIz"]:
            df[v] = df["FSTSc"] * df["TCI_z"] if "TCIz" in v else df["FSTSc"] * df["DAI_z"]
        df["FSTSc_TCIz"]  = df["FSTSc"]  * df["TCI_z"]
        df["FSTSc2_TCIz"] = df["FSTSc2"] * df["TCI_z"]
        df["FSTSc_DAIz"]  = df["FSTSc"]  * df["DAI_z"]
        df["FSTSc2_DAIz"] = df["FSTSc2"] * df["DAI_z"]

        # M2 inverted-U
        m2 = fit_ols_hc1(df, ["FSTSc", "FSTSc2"] + base, ["sector1", "wave"])
        rows.extend(extract_focal(m2, ["FSTSc", "FSTSc2"], f"sector_split_{label}", "M2"))

        # M7 dual direct
        m7 = fit_ols_hc1(df, ["FSTSc", "FSTSc2", "TCI_z", "DAI_z"] + base,
                         ["sector1", "wave"])
        rows.extend(extract_focal(m7, ["FSTSc", "FSTSc2", "TCI_z", "DAI_z"],
                                  f"sector_split_{label}", "M7"))

        # M8 with DAI interactions
        m8 = fit_ols_hc1(
            df,
            ["FSTSc", "FSTSc2", "TCI_z", "DAI_z", "FSTSc_DAIz", "FSTSc2_DAIz"] + base,
            ["sector1", "wave"],
        )
        F_dai, p_dai = joint_test(m8, ["FSTSc_DAIz", "FSTSc2_DAIz"])
        rows.extend(extract_focal(
            m8,
            ["FSTSc", "FSTSc2", "TCI_z", "DAI_z", "FSTSc_DAIz", "FSTSc2_DAIz"],
            f"sector_split_{label}", "M8",
        ))
        rows.append({
            "panel": f"sector_split_{label}",
            "sample": "VNMpooled",
            "term": "joint_F_DAI_interactions_M8",
            "b": round(float(F_dai), 4), "se": np.nan,
            "p": round(float(p_dai), 4), "n": n,
        })

        # Optional: TCI moderation joint F
        m3 = fit_ols_hc1(
            df,
            ["FSTSc", "FSTSc2", "TCI_z", "FSTSc_TCIz", "FSTSc2_TCIz"] + base,
            ["sector1", "wave"],
        )
        F_tci, p_tci = joint_test(m3, ["FSTSc_TCIz", "FSTSc2_TCIz"])
        rows.append({
            "panel": f"sector_split_{label}",
            "sample": "VNMpooled",
            "term": "joint_F_TCI_interactions_M3",
            "b": round(float(F_tci), 4), "se": np.nan,
            "p": round(float(p_tci), 4), "n": n,
        })
        rows.append({
            "panel": f"sector_split_{label}",
            "sample": "VNMpooled",
            "term": "N",
            "b": float(n), "se": np.nan, "p": np.nan, "n": n,
        })

    return rows


def main() -> None:
    waves = {y: build_wave(y) for y in (2009, 2015, 2023)}
    for y, df in waves.items():
        print(f"VNM{y}: N = {len(df)}")
    pooled = build_pooled(waves)
    print(f"VNMpooled: N = {len(pooled)}")

    sector_dummies = ["sector1"]

    results = {}
    for y, df in waves.items():
        results[f"VNM{y}"] = run_models(df, f"VNM{y}", dummies=sector_dummies)
    results["VNMpooled"] = run_models(pooled, "VNMpooled", dummies=["sector1", "wave"])

    base = ["lnEmp", "FirmAge", "ForeignOwned"]
    focal_for_heckman = ["FSTSc", "FSTSc2", "TCI_z", "DAI_z"] + base
    for y, df in waves.items():
        results[f"VNM{y}"]["Heckman"] = heckman_two_step(df, focal_for_heckman, ["sector1"])
    results["VNMpooled"]["Heckman"] = heckman_two_step(
        pooled, focal_for_heckman, ["sector1", "wave"]
    )

    emit_long_coef_csv(results, OUT_TABLES / "coefs_main_models.csv")
    emit_joint_F(results, OUT_TABLES / "joint_tests_main_models.csv")
    emit_lm(results, OUT_TABLES / "table_lind_mehlum.csv")
    emit_descriptives(waves, pooled, OUT_TABLES / "table_1_descriptives.csv")
    emit_selection_csv(results, OUT_TABLES / "selection_checks.csv")
    emit_paternoster_csv(results, OUT_TABLES / "table_paternoster.csv")

    rob = run_robustness(waves, pooled)
    rob.extend(run_sector_split(pooled))
    pd.DataFrame(rob).to_csv(OUT_TABLES / "table_3_robustness.csv", index=False)
    print(f"\nrobustness panels written: {len(rob)} rows")

    summary = {
        "samples": {k: r["n"] for k, r in results.items()},
        "tp_raw_centred": {k: r["TP"]["tp_raw"] for k, r in results.items()},
        "lm_p": {k: r["LM_p"] for k, r in results.items()},
        "M3_jointp_TCI_moderation": {k: r.get("M3_jointp") for k, r in results.items()},
        "M4_jointp_DAI_moderation": {k: r.get("M4_jointp") for k, r in results.items()},
        "M8_jointp_DAI_moderation_full": {k: r.get("M8_jointp") for k, r in results.items()},
    }
    print("\n=== summary ===")
    print(json.dumps(summary, indent=2, default=float))

    (OUT_LOGS / "analysis_summary.json").write_text(json.dumps(summary, indent=2, default=float))


if __name__ == "__main__":
    main()
