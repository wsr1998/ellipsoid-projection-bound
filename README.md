# ellipsoid-projection-bound

**Interactive visualization proving that the projected axis ratio is a strict lower bound on the intrinsic axis ratio of a triaxial ellipsoid.**

> 中文文档请见 [README_zh.md](README_zh.md)

---

## Key Result

For a triaxial ellipsoid with semi-axes $a \ge b \ge c > 0$, the **projected (observed) axis ratio** $q_\text{proj} \equiv b_\text{proj}/a_\text{proj}$ satisfies

$$
q_\text{proj} \;\ge\; \frac{c}{a}
$$

for **any** projection direction. If you observe $q_\text{proj} = q$, then intrinsic $c/a$ must lie in $[0, q]$ — all models with $c/a > q$ are geometrically forbidden.

---

## Quick Start

```bash
git clone https://github.com/<your-username>/ellipsoid-projection-bound.git
cd ellipsoid-projection-bound
pip install -r requirements.txt
streamlit run app.py
```

Opens at `http://localhost:8501`.

---

## App Structure

| Page | Description |
|------|-------------|
| **Home** | Theorem statement and navigation |
| **Constraint Explorer** | $(b/a, c/a)$ allowed/forbidden regions given observed $q_\text{obs}$ |
| **Projection Sweep** | $q_\text{proj}$ heatmap, histogram, and 1D sweeps |
| **Mathematical Proof** | Step-by-step LaTeX derivation |

```
ellipsoid-projection-bound/
├── app.py
├── pages/
│   ├── 1_Constraint_Explorer.py
│   ├── 2_Projection_Sweep.py
│   └── 3_Mathematical_Proof.py
├── src/
│   ├── projection.py    # Exact shape-tensor projection
│   ├── viz.py           # Plotly figures
│   ├── ui.py, i18n.py
│   └── derivation.py, theory_content.py
├── docs/
│   └── MATH_PROOF.md    # Self-contained mathematical proof
├── requirements.txt
└── .streamlit/config.toml
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `streamlit` | Interactive web UI |
| `numpy` | Projection math |
| `plotly` | Interactive 3D/2D plots |

---

## License

MIT
