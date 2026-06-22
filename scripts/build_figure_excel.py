"""Export each figure's underlying data + a native Excel chart + the rendered
PNG into an .xlsx workbook. One workbook per figure (Figure 2a, 2b, 2c, 2d, 3)
plus a Figure 1 workbook that documents the conceptual model and embeds the
diagram. Outputs go under p4_vietnam/output/figures_excel/.

Run from repo root:
    python3 scripts/build_figure_excel.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.api as sm

from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
from openpyxl.chart.trendline import Trendline
from openpyxl.drawing.image import Image as XLImage
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from p4_vietnam_analysis import build_pooled, build_wave  # type: ignore
from p4_render_figures import fit_inverted_u, predict_curve  # type: ignore

ROOT = Path("/home/user/Class-AI-Agent/p4_vietnam")
FIG_DIR = ROOT / "output" / "figures"
OUT_DIR = ROOT / "output" / "figures_excel"
OUT_DIR.mkdir(parents=True, exist_ok=True)

GRID_N = 100

HEADER_FONT = Font(bold=True, color="FFFFFF")
HEADER_FILL = PatternFill("solid", fgColor="1F4E78")
NOTE_FONT = Font(italic=True, size=9, color="555555")
TITLE_FONT = Font(bold=True, size=12)


def write_header(ws, row, headers):
    for i, h in enumerate(headers, start=1):
        c = ws.cell(row=row, column=i, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[row].height = 22


def autosize(ws, max_col):
    for col in range(1, max_col + 1):
        letter = get_column_letter(col)
        max_len = 8
        for cell in ws[letter]:
            if cell.value is None:
                continue
            length = len(str(cell.value))
            if length > max_len:
                max_len = length
        ws.column_dimensions[letter].width = min(max_len + 2, 38)


def add_image(ws, png_path: Path, anchor: str = "A2"):
    if not png_path.exists():
        return
    img = XLImage(str(png_path))
    target_w = 760
    scale = target_w / img.width if img.width else 1
    img.width = target_w
    img.height = int(img.height * scale)
    ws.add_image(img, anchor)


# ---------------------------------------------------------------------------
# Figure 2a / 2b / 2c / 2d -- inverted-U curves per wave + pooled
# ---------------------------------------------------------------------------
def export_figure_2(waves, pooled):
    sub_panels = [
        ("2a", "Vietnam 2009",   waves[2009], False),
        ("2b", "Vietnam 2015",   waves[2015], False),
        ("2c", "Vietnam 2023",   waves[2023], False),
        ("2d", "Pooled Vietnam (2009/2015/2023)", pooled, True),
    ]

    for tag, label, df, with_wave_fe in sub_panels:
        fit, names = fit_inverted_u(df, with_wave_fe=with_wave_fe)
        f_max = min(1.0, df["FSTS"].max())
        grid = np.linspace(0, f_max, GRID_N)
        yhat, se = predict_curve(fit, names, df, grid)
        lower = yhat - 1.96 * se
        upper = yhat + 1.96 * se

        b1 = fit.params[names.index("FSTSc")]
        b2 = fit.params[names.index("FSTSc2")]
        tp_pct = (-b1 / (2 * b2) + df["FSTS"].mean()) * 100 if b2 < 0 else None

        wb = Workbook()

        # ---- README sheet -------------------------------------------------
        ws = wb.active
        ws.title = "README"
        ws["A1"] = f"Figure {tag}. Predicted ln(labour productivity) by FSTS"
        ws["A1"].font = TITLE_FONT
        ws["A2"] = f"Sample: {label}  (N = {len(df):,})"
        ws["A2"].font = Font(italic=True)
        ws["A4"] = "Specification"
        ws["A4"].font = Font(bold=True)
        ws["A5"] = ("M2: lnLP = b0 + b1*FSTSc + b2*FSTSc^2 + lnEmp + FirmAge "
                    "+ ForeignOwned + sector FE" + (" + wave FE" if with_wave_fe else "")
                    + ".  OLS with HC1 robust standard errors.")
        ws["A6"] = "Controls held at within-sample means; sector and wave fixed effects at modal value."
        ws["A8"] = "Coefficients"
        ws["A8"].font = Font(bold=True)
        ws["A9"] = "FSTSc"
        ws["B9"] = float(b1)
        ws["A10"] = "FSTSc^2"
        ws["B10"] = float(b2)
        if tp_pct is not None:
            ws["A12"] = "Implied turning point (raw FSTS, %)"
            ws["B12"] = round(tp_pct, 2)
        ws["A14"] = "Sheets"
        ws["A14"].font = Font(bold=True)
        ws["A15"] = "Data       — FSTS grid (%), predicted lnLP, 95% CI lower/upper"
        ws["A16"] = "Chart      — native Excel line chart of the predicted curve"
        ws["A17"] = "Image      — rendered PNG (sanity check)"
        ws["A19"] = ("Source: World Bank Enterprise Surveys "
                     "(https://www.enterprisesurveys.org); authors' calculations.")
        ws["A19"].font = NOTE_FONT
        ws.column_dimensions["A"].width = 60
        ws.column_dimensions["B"].width = 18

        # ---- Data sheet ---------------------------------------------------
        ws = wb.create_sheet("Data")
        write_header(ws, 1,
                     ["FSTS (%)", "Predicted lnLP", "Lower 95% CI", "Upper 95% CI"])
        for i, (f, y, lo, hi) in enumerate(zip(grid * 100, yhat, lower, upper),
                                            start=2):
            ws.cell(row=i, column=1, value=float(f))
            ws.cell(row=i, column=2, value=float(y))
            ws.cell(row=i, column=3, value=float(lo))
            ws.cell(row=i, column=4, value=float(hi))
        for col_letter in ("A", "B", "C", "D"):
            for cell in ws[col_letter][1:]:
                cell.number_format = "0.0000"
        autosize(ws, 4)

        # ---- Chart sheet --------------------------------------------------
        chart_ws = wb.create_sheet("Chart")
        chart = LineChart()
        chart.title = f"Figure {tag}. Predicted ln(LP) across FSTS — {label}"
        chart.x_axis.title = "Direct-export intensity, FSTS (%)"
        chart.y_axis.title = "Predicted ln(labour productivity)"
        chart.height = 11
        chart.width = 22
        chart.legend.position = "b"

        data_rows = GRID_N + 1
        x_ref = Reference(wb["Data"], min_col=1, min_row=2,
                          max_row=data_rows)
        y_pred = Reference(wb["Data"], min_col=2, min_row=1,
                           max_row=data_rows)
        y_lo = Reference(wb["Data"], min_col=3, min_row=1,
                         max_row=data_rows)
        y_hi = Reference(wb["Data"], min_col=4, min_row=1,
                         max_row=data_rows)
        chart.add_data(y_pred, titles_from_data=True)
        chart.add_data(y_lo, titles_from_data=True)
        chart.add_data(y_hi, titles_from_data=True)
        chart.set_categories(x_ref)
        for s in chart.series:
            s.smooth = True
        chart_ws.add_chart(chart, "B2")
        if tp_pct is not None:
            chart_ws["B30"] = (f"Turning point ≈ {tp_pct:.1f}% (vertical reference; "
                               f"compare visually against the curve maximum)")
            chart_ws["B30"].font = NOTE_FONT

        # ---- Image sheet --------------------------------------------------
        img_ws = wb.create_sheet("Image")
        img_ws["A1"] = f"Figure {tag} — rendered PNG"
        img_ws["A1"].font = TITLE_FONT
        add_image(img_ws, FIG_DIR / f"figure_{tag}.png", anchor="A3")

        out = OUT_DIR / f"figure_{tag}.xlsx"
        wb.save(str(out))
        print(f"  wrote {out}")


# ---------------------------------------------------------------------------
# Figure 3 -- moderator marginals (DAI low/high; TCI low/high)
# ---------------------------------------------------------------------------
def export_figure_3(pooled):
    df = pooled.copy()
    df["FSTSc_DAIz"] = df["FSTSc"] * df["DAI_z"]
    df["FSTSc2_DAIz"] = df["FSTSc2"] * df["DAI_z"]

    parts = [np.ones((len(df), 1))]
    names = ["const"]
    for v in ["FSTSc", "FSTSc2", "TCI_z", "DAI_z", "FSTSc_DAIz", "FSTSc2_DAIz",
              "lnEmp", "FirmAge", "ForeignOwned"]:
        parts.append(df[v].to_numpy().reshape(-1, 1))
        names.append(v)
    sec = pd.get_dummies(df["sector1"].astype(int), prefix="sector1",
                         drop_first=True, dtype=float)
    parts.append(sec.to_numpy())
    names.extend(sec.columns.tolist())
    wf = pd.get_dummies(df["wave"].astype(int), prefix="wave",
                        drop_first=True, dtype=float)
    parts.append(wf.to_numpy())
    names.extend(wf.columns.tolist())
    X = np.hstack(parts)
    fit = sm.OLS(df["lnLP"].to_numpy(), X).fit(cov_type="HC1")

    f_max = min(1.0, df["FSTS"].max())
    grid = np.linspace(0, f_max, GRID_N)
    fmean = df["FSTS"].mean()
    fsts_c = grid - fmean
    fsts_c2 = fsts_c ** 2

    means = {v: df[v].mean() for v in ["lnEmp", "FirmAge", "ForeignOwned",
                                        "TCI_z", "DAI_z"]}
    sector_mode = int(df["sector1"].mode().iloc[0])
    wave_mode = int(df["wave"].mode().iloc[0])

    def x_row(f_c, f_c2, dai_z, tci_z):
        x = np.zeros(len(names))
        x[names.index("const")] = 1.0
        x[names.index("FSTSc")] = f_c
        x[names.index("FSTSc2")] = f_c2
        x[names.index("TCI_z")] = tci_z
        x[names.index("DAI_z")] = dai_z
        x[names.index("FSTSc_DAIz")] = f_c * dai_z
        x[names.index("FSTSc2_DAIz")] = f_c2 * dai_z
        x[names.index("lnEmp")] = means["lnEmp"]
        x[names.index("FirmAge")] = means["FirmAge"]
        x[names.index("ForeignOwned")] = means["ForeignOwned"]
        for n in names:
            if n.startswith("sector1_") and int(n.split("_")[1]) == sector_mode:
                x[names.index(n)] = 1.0
            if n.startswith("wave_") and int(n.split("_")[1]) == wave_mode:
                x[names.index(n)] = 1.0
        return x

    p25_dai, p75_dai = df["DAI_z"].quantile([0.25, 0.75])
    p25_tci, p75_tci = df["TCI_z"].quantile([0.25, 0.75])

    yhat_low_dai = np.array([float(x_row(fc, fc2, p25_dai, means["TCI_z"]) @ fit.params)
                             for fc, fc2 in zip(fsts_c, fsts_c2)])
    yhat_high_dai = np.array([float(x_row(fc, fc2, p75_dai, means["TCI_z"]) @ fit.params)
                              for fc, fc2 in zip(fsts_c, fsts_c2)])
    yhat_low_tci = np.array([float(x_row(fc, fc2, means["DAI_z"], p25_tci) @ fit.params)
                             for fc, fc2 in zip(fsts_c, fsts_c2)])
    yhat_high_tci = np.array([float(x_row(fc, fc2, means["DAI_z"], p75_tci) @ fit.params)
                              for fc, fc2 in zip(fsts_c, fsts_c2)])

    wb = Workbook()

    ws = wb.active
    ws.title = "README"
    ws["A1"] = "Figure 3. Marginal-effect view of capability and digital moderators"
    ws["A1"].font = TITLE_FONT
    ws["A2"] = f"Sample: pooled Vietnam 2009/2015/2023 (N = {len(df):,})"
    ws["A2"].font = Font(italic=True)
    ws["A4"] = "Specification"
    ws["A4"].font = Font(bold=True)
    ws["A5"] = ("Pooled M8: lnLP = b0 + b1*FSTSc + b2*FSTSc^2 + b3*TCI_z + b4*DAI_z "
                "+ b5*FSTSc*DAI_z + b6*FSTSc^2*DAI_z + lnEmp + FirmAge + ForeignOwned "
                "+ sector FE + wave FE.  OLS with HC1 robust standard errors.")
    ws["A6"] = ("Controls held at sample means; sector and wave fixed effects at modal "
                "value. Moderator quantiles taken from the pooled sample.")
    ws["A8"] = "DAI_z quantiles"
    ws["A8"].font = Font(bold=True)
    ws["A9"] = "p25 (Low)"
    ws["B9"] = float(p25_dai)
    ws["A10"] = "p75 (High)"
    ws["B10"] = float(p75_dai)
    ws["A12"] = "TCI_z quantiles"
    ws["A12"].font = Font(bold=True)
    ws["A13"] = "p25 (Low)"
    ws["B13"] = float(p25_tci)
    ws["A14"] = "p75 (High)"
    ws["B14"] = float(p75_tci)
    ws["A16"] = "Sheets"
    ws["A16"].font = Font(bold=True)
    ws["A17"] = "Data 3a    — FSTS grid, predicted lnLP at low / high DAI_z (TCI_z held at mean)"
    ws["A18"] = "Chart 3a   — native Excel line chart of Panel 3a"
    ws["A19"] = "Data 3b    — FSTS grid, predicted lnLP at low / high TCI_z (DAI_z held at mean)"
    ws["A20"] = "Chart 3b   — native Excel line chart of Panel 3b"
    ws["A21"] = "Image      — rendered PNG of Figure 3 (sanity check)"
    ws["A23"] = ("Source: World Bank Enterprise Surveys "
                 "(https://www.enterprisesurveys.org); authors' calculations on "
                 "Vietnam 2009/2015/2023 pooled.")
    ws["A23"].font = NOTE_FONT
    ws.column_dimensions["A"].width = 70
    ws.column_dimensions["B"].width = 18

    # Panel 3a -------------------------------------------------------------
    ws = wb.create_sheet("Data 3a")
    write_header(ws, 1, ["FSTS (%)",
                         f"Low DAI_z (p25 = {p25_dai:.2f})",
                         f"High DAI_z (p75 = {p75_dai:.2f})"])
    for i, (f, y_lo, y_hi) in enumerate(zip(grid * 100, yhat_low_dai,
                                             yhat_high_dai), start=2):
        ws.cell(row=i, column=1, value=float(f))
        ws.cell(row=i, column=2, value=float(y_lo))
        ws.cell(row=i, column=3, value=float(y_hi))
    for col_letter in ("A", "B", "C"):
        for cell in ws[col_letter][1:]:
            cell.number_format = "0.0000"
    autosize(ws, 3)

    chart_ws = wb.create_sheet("Chart 3a")
    chart = LineChart()
    chart.title = "Figure 3a. Predicted ln(LP) by FSTS at low / high DAI_z"
    chart.x_axis.title = "Direct-export intensity, FSTS (%)"
    chart.y_axis.title = "Predicted ln(labour productivity)"
    chart.height = 11
    chart.width = 22
    chart.legend.position = "b"
    data_rows = GRID_N + 1
    x_ref = Reference(wb["Data 3a"], min_col=1, min_row=2, max_row=data_rows)
    y_lo_ref = Reference(wb["Data 3a"], min_col=2, min_row=1, max_row=data_rows)
    y_hi_ref = Reference(wb["Data 3a"], min_col=3, min_row=1, max_row=data_rows)
    chart.add_data(y_lo_ref, titles_from_data=True)
    chart.add_data(y_hi_ref, titles_from_data=True)
    chart.set_categories(x_ref)
    for s in chart.series:
        s.smooth = True
    chart_ws.add_chart(chart, "B2")

    # Panel 3b -------------------------------------------------------------
    ws = wb.create_sheet("Data 3b")
    write_header(ws, 1, ["FSTS (%)",
                         f"Low TCI_z (p25 = {p25_tci:.2f})",
                         f"High TCI_z (p75 = {p75_tci:.2f})"])
    for i, (f, y_lo, y_hi) in enumerate(zip(grid * 100, yhat_low_tci,
                                             yhat_high_tci), start=2):
        ws.cell(row=i, column=1, value=float(f))
        ws.cell(row=i, column=2, value=float(y_lo))
        ws.cell(row=i, column=3, value=float(y_hi))
    for col_letter in ("A", "B", "C"):
        for cell in ws[col_letter][1:]:
            cell.number_format = "0.0000"
    autosize(ws, 3)

    chart_ws = wb.create_sheet("Chart 3b")
    chart = LineChart()
    chart.title = "Figure 3b. Predicted ln(LP) by FSTS at low / high TCI_z"
    chart.x_axis.title = "Direct-export intensity, FSTS (%)"
    chart.y_axis.title = "Predicted ln(labour productivity)"
    chart.height = 11
    chart.width = 22
    chart.legend.position = "b"
    x_ref = Reference(wb["Data 3b"], min_col=1, min_row=2, max_row=data_rows)
    y_lo_ref = Reference(wb["Data 3b"], min_col=2, min_row=1, max_row=data_rows)
    y_hi_ref = Reference(wb["Data 3b"], min_col=3, min_row=1, max_row=data_rows)
    chart.add_data(y_lo_ref, titles_from_data=True)
    chart.add_data(y_hi_ref, titles_from_data=True)
    chart.set_categories(x_ref)
    for s in chart.series:
        s.smooth = True
    chart_ws.add_chart(chart, "B2")

    img_ws = wb.create_sheet("Image")
    img_ws["A1"] = "Figure 3 — rendered PNG (combined Panels 3a + 3b)"
    img_ws["A1"].font = TITLE_FONT
    add_image(img_ws, FIG_DIR / "figure_3_moderator_marginals.png", anchor="A3")

    out = OUT_DIR / "figure_3_moderator_marginals.xlsx"
    wb.save(str(out))
    print(f"  wrote {out}")


# ---------------------------------------------------------------------------
# Figure 1 -- conceptual model (no tabular data; embed PNG + describe links)
# ---------------------------------------------------------------------------
def export_figure_1():
    wb = Workbook()
    ws = wb.active
    ws.title = "README"
    ws["A1"] = "Figure 1. Conceptual model"
    ws["A1"].font = TITLE_FONT
    ws["A3"] = ("Figure 1 is a conceptual diagram (not a chart with tabular "
                "data). It depicts the relationships among the independent "
                "variable, the dependent variable, the two moderators, the "
                "control set, and the four hypotheses tested in the paper.")
    ws["A3"].alignment = Alignment(wrap_text=True, vertical="top")
    ws.row_dimensions[3].height = 60
    ws.column_dimensions["A"].width = 100

    ws["A5"] = "Hypotheses summarised in the diagram"
    ws["A5"].font = Font(bold=True)
    rows = [
        ("H1", "Internationalisation (FSTS_c, FSTS_c²) ⇒ Firm performance (lnLP) — nonlinear (inverted-U)"),
        ("H2", "Foreign-technology / standards capability (TCI_z) ⇒ Firm performance — direct positive"),
        ("H3", "Website-based digital presence (DAI_z) ⇒ Firm performance — direct positive on average"),
        ("H4 (exploratory)", "DAI_z moderates the FSTS-curve; concentrated in the 2023 wave"),
    ]
    write_header(ws, 6, ["Hypothesis", "Path"])
    for i, (h, p) in enumerate(rows, start=7):
        ws.cell(row=i, column=1, value=h)
        ws.cell(row=i, column=2, value=p)
        ws.cell(row=i, column=2).alignment = Alignment(wrap_text=True)
        ws.row_dimensions[i].height = 30
    ws.column_dimensions["B"].width = 110

    ws["A12"] = "Controls (top dashed box in the diagram)"
    ws["A12"].font = Font(bold=True)
    ws["A13"] = ("lnEmp (firm size); FirmAge; ForeignOwned (b2b > 0); "
                 "Sector FE (a4b/a4a 1-digit ISIC); Wave FE (in pooled).")

    ws["A15"] = ("Source: World Bank Enterprise Surveys "
                 "(https://www.enterprisesurveys.org); authors' construction.")
    ws["A15"].font = NOTE_FONT

    img_ws = wb.create_sheet("Diagram")
    img_ws["A1"] = "Figure 1 — rendered conceptual model (PNG)"
    img_ws["A1"].font = TITLE_FONT
    add_image(img_ws, FIG_DIR / "figure_1_conceptual_model.png", anchor="A3")

    out = OUT_DIR / "figure_1_conceptual_model.xlsx"
    wb.save(str(out))
    print(f"  wrote {out}")


def main():
    waves = {y: build_wave(y) for y in (2009, 2015, 2023)}
    pooled = build_pooled(waves)
    export_figure_1()
    export_figure_2(waves, pooled)
    export_figure_3(pooled)
    print(f"All Excel workbooks under {OUT_DIR}")


if __name__ == "__main__":
    main()
