# Figure 1 — P5 China Conceptual Model

Two source formats provided. Pick whichever your toolchain supports.

## Variable taxonomy (matches manuscript v1.3 §2.5)

| Role | Variable | Operationalization | Hypothesis | Render style |
|---|---|---|---|---|
| **Dependent variable (DV)** | `lnLP` | ln(d2 / l1) | — | outcome box (gray fill, thick border) |
| **Independent variable (IV)** | `FSTS`, `FSTS²` | d3c/100 and its square | H1 | solid box, solid arrow |
| **Moderator** | Working-capital condition | `k7`, `k8/k82`, `k3a`, `k3bc`, `k3f`, `k30` (+ 2012-only `k1c`, `k2c`) | **H3** | **dashed box**, **dashed arrow** |
| **Level-shifter (additional predictor)** | `TCIfull` | z-mean(e6, b8, h1/CNo1, h8/CNo3) | H4a | solid box, solid arrow |
| **Level-shifter (additional predictor)** | `DAIcore` | z(c22b own-website) | H4b | solid box, solid arrow |
| **Controls** | `lnEmp`, `firmage`, `foreigndummy`, sector (`a4a`) strata, `wave2024` (pooled only) | various | — | solid box, thin gray arrow |
| **Cross-wave annotation** | H2 stability link | Paternoster (1998) z-test on (FSTS, FSTS²) | H2 | note shape, **dotted double-headed link** |

**Key clarification for reviewers.** Working-capital is the **only true moderator** in the model (interacts with FSTS² to test H3). TCI and DAI are additional predictors / level-shifters — they enter the regression as direct effects on lnLP, NOT as moderators of the curvature. This is a deliberate architectural choice (see manuscript §2.4) prioritizing threshold stability and reflecting WBES measurement constraints (lower-tier digital indicators only).

## Files

| File | Format | Use |
|---|---|---|
| `figure1_conceptual_model.mmd` | Mermaid | GitHub renders inline; quick previews |
| `figure1_conceptual_model.dot` | Graphviz DOT | Higher-quality publication output |

## Rendering

### Mermaid → PNG / SVG

```bash
# Install mermaid-cli
npm install -g @mermaid-js/mermaid-cli

# Render PNG
mmdc -i figure1_conceptual_model.mmd -o figure1.png -w 1600 -H 900 -b white

# Render SVG (better for Word embedding)
mmdc -i figure1_conceptual_model.mmd -o figure1.svg -b white

# Render PDF
mmdc -i figure1_conceptual_model.mmd -o figure1.pdf
```

Or paste the `.mmd` content into https://mermaid.live for instant preview.

### Graphviz → PNG / SVG / PDF

```bash
# Install Graphviz
brew install graphviz       # macOS
apt install graphviz        # Ubuntu / Debian

# Render
dot -Tpng figure1_conceptual_model.dot -o figure1.png
dot -Tsvg figure1_conceptual_model.dot -o figure1.svg
dot -Tpdf figure1_conceptual_model.dot -o figure1.pdf
```

Or paste the `.dot` content into https://dreampuf.github.io/GraphvizOnline for browser-based render.

### Embedding into the Word manuscript

1. Render to SVG (preferred) or 600-dpi PNG.
2. Insert at the Figure 1 placeholder in the manuscript (after §2.5 caption).
3. Verify legend visibility, font size ≥ 10pt, no truncated labels.
4. Re-export the assembled `manuscript_v1_3.docx` from pandoc; or paste the rendered figure manually if working in Word native.

## Visual semantics (as described in caption P036)

- **Boxes** = firm-level constructs.
- **Dashed box** (Working-Capital Condition) = exploratory, secondary role; not the manuscript's central mechanism.
- **Solid arrows** = the four directional hypotheses (H1, H4a, H4b plus thin control arrow).
- **Dashed arrow** (Working-Capital → ln LP) = exploratory H3 post-threshold conditioning.
- **Dotted double-headed link** (Export Intensity ↔ H2 annotation) = cross-wave stability evaluation, not a directional causal claim.
- **Outcome box** (ln LP) = filled gray with thick border to anchor the rightmost endpoint.

## ASCII fallback (for plain-text contexts)

```
                                   ┌──────────────────────┐
                                   ┆ Working-Capital      ┆   (dashed box →
                                   ┆ Condition (H3)       ┆    exploratory)
                                   ┆ • Liquidity          ┆
                                   ┆ • Financing          ┆
                                   ┆ • A2F obstacle       ┆
                                   └────────┬─────────────┘
                                            ╎ dashed arrow
                                            ╎ (H3 moderation)
                                            ▼
  ┌─────────────────────┐                        ┌──────────────────┐
  │ Export Intensity   │ ═H1 inverted-U═══════▶ │  Firm Performance │
  │  FSTS, FSTS²       │                        │   ln(LP)          │
  └────┬───────────────┘                        │   (DV)            │
       ┗ dotted ↔ H2                            │                   │
         (cross-wave stability)                  │                   │
  ┌─────────────────────┐                        │                   │
  │ Technological      │ ═H4a level shift═════▶ │                   │
  │ Capability TCI     │                        │                   │
  └─────────────────────┘                        │                   │
  ┌─────────────────────┐                        │                   │
  │ Digital Adoption   │ ═H4b level shift═════▶ │                   │
  │ DAI (c22b)         │                        │                   │
  └─────────────────────┘                        │                   │
  ┌─────────────────────┐                        │                   │
  │ Controls           │ ───────────────────▶ │                   │
  │ lnEmp, firmage,    │                        │                   │
  │ foreign, sector    │                        │                   │
  └─────────────────────┘                        └──────────────────┘
```
