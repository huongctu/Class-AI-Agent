#!/usr/bin/env python3
"""
inspect_wbes_vn.py
==================
Inspect WBES Vietnam .dta files for variables relevant to P4 manuscript.

Reports for each wave (2009, 2015, 2023):
  - Whether each focal WBES item is present (by name and by label match)
  - Variable label, type, missing %, value range / categories
  - Patterns matched for e-payment items (k33*, k38*, *pay*, *ecom*)
  - Region variable candidates (a2, stratificationregioncode, region*)
  - Sector variable detail (a4a, a4b, ISIC depth)

Output: a single Markdown file (wbes_vn_inspection.md) with one section per
wave plus a cross-wave summary table. Output is suitable for pasting into
the response letter or supplementary materials.

Usage
-----
    pip install pandas pyreadstat
    python inspect_wbes_vn.py \
        --files Vietnam-2009-full-data.dta \
                Vietnam-2015-full-data.dta \
                Vietnam-2023-full-data.dta \
        --out wbes_vn_inspection.md

If the WBES public files use different filenames, pass them in any order;
the script tags each wave from the file metadata or from the filename.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

import pandas as pd

try:
    import pyreadstat
except ImportError:
    sys.exit("pyreadstat is required. Install with: pip install pyreadstat")


# -----------------------------------------------------------------------------
# Configuration: focal items to probe
# -----------------------------------------------------------------------------

FOCAL_ITEMS = {
    # Productivity / scale
    "d2":   "Total annual sales (productivity numerator)",
    "l1":   "Permanent full-time employees (productivity denominator)",
    "d3c":  "Direct exports as % of total sales (FSTS)",
    # TCI thin items
    "b8":   "Internationally recognized quality certification",
    "e6":   "Foreign-licensed technology",
    # TCI full items (wave 2015 / 2023 only)
    "h1":   "R&D expenditure",
    "h8":   "Introduced new/significantly improved product",
    # DAI thin items
    "c22b": "Communication via website / own e-mail",
    # Region / strata candidates
    "a2":   "Sampling region (within country)",
    "stratificationregioncode": "Derived sampling region code",
    # Sector items
    "a4a":  "Industry sector (ISIC code)",
    "a4b":  "Industry sector (alternate ISIC code)",
    # Firm-level controls
    "b5":   "Year of establishment (for firm age)",
    "b2b":  "Foreign ownership share",
}

# Patterns to match country-suffixed e-payment items
EPAYMENT_PATTERNS = [
    r"^k33(?:_[A-Z]{2,3})?$",   # k33, k33_VN, k33_BR, etc.
    r"^k38(?:_[A-Z]{2,3})?$",
    r".*pay.*",                  # any var containing "pay"
    r".*ecom.*",                 # e-commerce
    r".*epay.*",
    r".*online.*sale.*",
]
EPAY_RE = [re.compile(p, re.IGNORECASE) for p in EPAYMENT_PATTERNS]


# -----------------------------------------------------------------------------
# Reading
# -----------------------------------------------------------------------------

def read_dta(path: Path) -> tuple[pd.DataFrame, "pyreadstat._readstat_parser.metadata_container"]:
    """Read a Stata .dta file with full metadata. Falls back through common
    encodings (utf-8 default -> latin1 -> cp1252) for non-UTF saves."""
    last_err = None
    for enc in (None, "latin1", "cp1252"):
        try:
            kwargs = {"apply_value_formats": False}
            if enc is not None:
                kwargs["encoding"] = enc
            df, meta = pyreadstat.read_dta(str(path), **kwargs)
            return df, meta
        except Exception as e:
            last_err = e
    raise last_err


def detect_wave(meta, path: Path, df: pd.DataFrame) -> str:
    """Try to identify the survey wave from filename or content."""
    name = path.name
    for yr in ("2009", "2015", "2023"):
        if yr in name:
            return yr
    # Fall back to value of `a14` (interview year) or similar
    for cand in ("a14", "year", "wave"):
        if cand in df.columns:
            try:
                vals = df[cand].dropna().astype(int).unique()
                if len(vals) >= 1:
                    return str(int(vals[0]))
            except Exception:
                pass
    return "unknown"


# -----------------------------------------------------------------------------
# Probing
# -----------------------------------------------------------------------------

def variable_summary(df: pd.DataFrame, meta, varname: str) -> dict:
    """Return a small dict summarising a single variable."""
    info = {"present": varname in df.columns}
    if not info["present"]:
        return info
    s = df[varname]
    info["label"] = meta.column_labels[meta.column_names.index(varname)] \
        if varname in meta.column_names else ""
    info["dtype"] = str(s.dtype)
    info["n_total"] = int(len(s))
    info["n_missing"] = int(s.isna().sum())
    info["pct_missing"] = round(100 * info["n_missing"] / info["n_total"], 1) if info["n_total"] else 0.0
    if pd.api.types.is_numeric_dtype(s):
        nonna = s.dropna()
        if len(nonna):
            info["min"] = float(nonna.min())
            info["max"] = float(nonna.max())
            info["unique"] = int(nonna.nunique())
        else:
            info["min"] = info["max"] = info["unique"] = None
    else:
        info["unique"] = int(s.dropna().nunique())
    return info


def find_epayment_vars(df: pd.DataFrame) -> list[str]:
    """Return all variables matching e-payment patterns."""
    hits = []
    for col in df.columns:
        if any(p.match(col) for p in EPAY_RE):
            hits.append(col)
    return sorted(hits)


def find_region_vars(df: pd.DataFrame) -> list[str]:
    """Return candidate region/strata variables."""
    pats = [r"^a2$", r"^region.*$", r".*stratification.*region.*", r".*region.*code.*"]
    rx = [re.compile(p, re.IGNORECASE) for p in pats]
    return sorted({c for c in df.columns if any(p.match(c) for p in rx)})


# -----------------------------------------------------------------------------
# Markdown rendering
# -----------------------------------------------------------------------------

def render_wave_section(wave: str, path: Path, df: pd.DataFrame, meta) -> str:
    out = []
    out.append(f"## Wave {wave} — `{path.name}`\n")
    out.append(f"Rows: **{len(df):,}**  |  Columns: **{len(df.columns):,}**\n")

    # Focal items table
    out.append("\n### Focal items\n")
    out.append("| Item | Present | Label | Type | n missing | % missing | Range / unique |")
    out.append("|---|---|---|---|---|---|---|")
    for var, desc in FOCAL_ITEMS.items():
        s = variable_summary(df, meta, var)
        if not s["present"]:
            out.append(f"| `{var}` | ❌ | _{desc}_ |  |  |  |  |")
            continue
        rng = ""
        if "min" in s and s["min"] is not None:
            rng = f"{s['min']:g} – {s['max']:g} ({s['unique']} unique)"
        elif "unique" in s:
            rng = f"{s['unique']} unique"
        label = (s["label"] or "")[:60]
        out.append(f"| `{var}` | ✓ | {label} | {s['dtype']} | {s['n_missing']:,} | {s['pct_missing']}% | {rng} |")

    # E-payment patterns
    out.append("\n### E-payment items (pattern match)\n")
    epay = find_epayment_vars(df)
    if not epay:
        out.append("_No variables matched k33*, k38*, *pay*, *ecom*, *epay*, *online*sale*._")
    else:
        out.append("| Variable | Label | Missing % |")
        out.append("|---|---|---|")
        for v in epay:
            s = variable_summary(df, meta, v)
            label = (s.get("label") or "")[:80]
            out.append(f"| `{v}` | {label} | {s.get('pct_missing', 0)}% |")

    # Region variable candidates
    out.append("\n### Region / sampling-strata candidates\n")
    regs = find_region_vars(df)
    if not regs:
        out.append("_No region variable candidates found. Check codebook for the country-specific name._")
    else:
        out.append("| Variable | Label | Unique values | Missing % |")
        out.append("|---|---|---|---|")
        for v in regs:
            s = variable_summary(df, meta, v)
            label = (s.get("label") or "")[:80]
            out.append(f"| `{v}` | {label} | {s.get('unique', '?')} | {s.get('pct_missing', 0)}% |")

    return "\n".join(out) + "\n"


def render_summary(wave_results: dict[str, dict]) -> str:
    """Cross-wave summary table for the response letter."""
    out = []
    out.append("\n## Cross-wave summary — focal-item availability\n")
    waves = sorted(wave_results.keys())
    header = "| Item | Description | " + " | ".join(waves) + " |"
    align = "|---|---|" + "---|" * len(waves)
    out.append(header)
    out.append(align)
    for var, desc in FOCAL_ITEMS.items():
        cells = []
        for w in waves:
            cells.append("✓" if wave_results[w].get(var, False) else "—")
        out.append(f"| `{var}` | {desc[:50]} | " + " | ".join(cells) + " |")
    return "\n".join(out) + "\n"


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--files", nargs="+", required=True,
                    help="Path(s) to WBES Vietnam .dta file(s)")
    ap.add_argument("--out", default="wbes_vn_inspection.md",
                    help="Output Markdown file (default: wbes_vn_inspection.md)")
    args = ap.parse_args()

    sections = ["# WBES Vietnam — variable inspection report\n"]
    sections.append(f"_Generated for P4 manuscript revision._\n")
    sections.append(f"_Files inspected: {len(args.files)}_\n")

    wave_results: dict[str, dict] = {}

    for f in args.files:
        path = Path(f)
        if not path.exists():
            print(f"[warn] file not found: {path}", file=sys.stderr)
            continue
        print(f"[info] reading {path.name} ...", file=sys.stderr)
        try:
            df, meta = read_dta(path)
        except Exception as e:
            print(f"[error] failed to read {path}: {e}", file=sys.stderr)
            continue
        wave = detect_wave(meta, path, df)
        sections.append(render_wave_section(wave, path, df, meta))
        wave_results[wave] = {v: (v in df.columns) for v in FOCAL_ITEMS}

    if wave_results:
        sections.append(render_summary(wave_results))

    Path(args.out).write_text("\n".join(sections), encoding="utf-8")
    print(f"[ok] wrote {args.out}")


if __name__ == "__main__":
    main()
