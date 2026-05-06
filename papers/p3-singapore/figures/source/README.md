# P3 Singapore — Figures Source

Scripts tạo lại 3 figures trong manuscript MIR R3.

## Figure 1 — Conceptual Model

**Source**: [`regenerate_fig1.py`](regenerate_fig1.py)

```bash
pip install matplotlib pillow
python3 regenerate_fig1.py
```

Output: `fig1_FIXED.png` (2062×1404 RGBA, 254 KB)

**Lịch sử vật cải**: Figure 1 gốc (image3.png trong R3 docx) có nhãn hypothesis cũ (H2 cho TCI moderation, H4 cho DAI moderation, H3 cho DAI direct). Sau khi R3 demote H2 và tiếp tục renumber H3→H2 và H4→H3, cần regenerate Figure 1 với nhãn mới:
- TCI × FSTS box: không còn nhãn số ("open empirical question")
- DAI × FSTS box: H3 (was H4)
- Bottom legend: H2 (was H3)

Matplotlib script tái tạo sơ đồ với color palette như bản Word/PowerPoint gốc.

## Figure 2 — DAI Marginal Effect

**Source**: KHÔNG có trong repo (regenerated externally during R3 process)

File: `figures/figure2_dai_marginal.png` — "support-aware version" với rug strip + decile counts + thin-tail (FSTS > 70%) shaded grey.

Để reproduce, cần marginal effects from Model M8 tại 9 mức FSTS (0%, 5%, 10%, 15%, 20%, 30%, 50%, 70%, 100%) plus delta-method SE — tham chiếu tables/coefs_main_models.csv (nếu có) hoặc reproduce từ manuscript Table 4.

## Figure 3 — Predicted I–P Curve

**Source**: KHÔNG có trong repo (regenerated externally during R3 process)

File: `figures/figure3_predicted_curve.png` — "bootstrap-aware version" với 95% CI band + red shaded vertical band cho turning-point CI [52.8%, 252.9%] + in-figure note "96.3% of bootstrap replications recover an inverted-U shape".

Để reproduce, cần bootstrap 5,000 cluster-bootstrap replications của M2 inverted-U specification, plus prediction intervals.

## Future regeneration

Nếu cần regenerate Figure 2 và Figure 3 — có thể viết thêm matplotlib script tương tự như `regenerate_fig1.py`. Inputs cần thiết:
- Figure 2: `outputs/r3/audit/m8_canonical.csv` (model M8 estimates) + `dai_marginal_effects.csv` (marginal effects tại 9 FSTS levels)
- Figure 3: `outputs/r3/audit/m2_bootstrap_5000.json` (bootstrap turning-point CI) + observed firm dispersion cho rug strip

Replication script gốc ở [`p3-r3-revision` branch tại `tools/r3/06_render_fig2_v2.py`, `tools/r3/07_render_fig3_v2.py`].
