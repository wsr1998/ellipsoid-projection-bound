# ellipsoid-projection-bound

**Interactive visualization proving that the projected axis ratio is a strict upper bound on the intrinsic axis ratio of a triaxial ellipsoid.**

> 中文文档请见 [README_zh.md](README_zh.md)

---

## Key Result

For a triaxial ellipsoid with semi-axes $a \ge b \ge c > 0$, the **projected (observed) axis ratio** $q_\text{proj} \equiv b_\text{proj}/a_\text{proj}$ satisfies

$$
q_\text{proj} \;\ge\; \frac{c}{a}
$$

for **any** projection direction. Equivalently, projection onto a plane can only make an ellipsoid appear *rounder*, never *flatter*, than it intrinsically is.

This tool lets you explore this theorem interactively: drag the sliders to change the ellipsoid shape and viewing angle, and verify that the projected axis ratio never falls below the intrinsic $c/a$.

---

## Mathematical Background

The proof rests on the **Poincaré (Cauchy interlacing) theorem**. The ellipsoid is described by a symmetric positive-definite shape tensor **S** with eigenvalues $\lambda_1 = a^2 \ge \lambda_2 = b^2 \ge \lambda_3 = c^2$. An orthogonal projection onto any plane produces a $2\times 2$ projected shape tensor whose eigenvalues $\mu_1 = a_\text{proj}^2$, $\mu_2 = b_\text{proj}^2$ interlace with those of **S**:

$$
a^2 \;\ge\; a_\text{proj}^2 \;\ge\; b^2 \;\ge\; b_\text{proj}^2 \;\ge\; c^2
$$

Taking square roots yields two bounds:

1. $a_\text{proj} \le a$ — projection cannot enlarge the longest axis.  
2. $b_\text{proj} \ge c$ — projection cannot shrink below the shortest intrinsic axis.

Dividing gives $q_\text{proj} = b_\text{proj}/a_\text{proj} \ge c/a$.

**Practical consequence:** measuring a projected flattening $q_\text{proj}$ rules out all intrinsic shapes rounder than the observation — any model with $c/a > q_\text{proj}$ is geometrically prohibited.

---

## Demo

![screenshot](docs/screenshot.png)

The app shows:

- **Top row** — four 3-D ellipsoid views (XY, XZ, YZ planes + your custom angle).  
- **Bottom row** — the corresponding 2-D projections with computed axis ratios.  
- **Sidebar metrics** — intrinsic 3-D ratios $b/a$, $c/a$, $c/b$ and the custom-view projected ratio.

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/ellipsoid-projection-bound.git
cd ellipsoid-projection-bound

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

The app opens at `http://localhost:8501` by default.

---

## Usage

| Control | Description |
|---------|-------------|
| **a / b / c sliders** | Set the three semi-axis lengths ($a \ge$ recommended) |
| **Azimuth** | Horizontal rotation of the custom viewing direction (0°–360°) |
| **Elevation** | Vertical tilt of the custom viewing direction (−90°–90°) |
| **Quick Presets** | Load common shapes (oblate spheroid, prolate ellipsoid, sphere) |

### Exploring the bound

1. Set any ellipsoid shape, e.g. $a=3,\; b=2,\; c=1$ ($c/a = 0.333$).  
2. Sweep the azimuth and elevation across all angles.  
3. Observe that the **Custom Projection Ratio** in the bottom-right never drops below $0.333$.

---

## File Structure

```
ellipsoid-projection-bound/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # English documentation (this file)
├── README_zh.md              # Chinese documentation
└── docs/
    └── MATH_PROOF.md         # Self-contained mathematical proof
```

---

## Dependencies

| Package | Purpose |
|---------|---------|
| `numpy` | Numerical computation (projection, eigenvalue decomposition) |
| `matplotlib` | Rendering 3-D and 2-D plots |
| `streamlit` | Interactive web interface |

---

## Citation

If this visualization accompanies a publication, please cite the relevant paper where this geometric proof appears. The core inequality follows from:

> Bellman, R. (1997). *Introduction to Matrix Analysis* (2nd ed.). SIAM.

---

## License

MIT
