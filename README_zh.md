# ellipsoid-projection-bound

**交互式可视化：证明三轴椭球的投影轴比是真实轴比的严格下界。**

> English: [README.md](README.md)

---

## 核心结论

半轴满足 $a \ge b \ge c > 0$ 时，**投影轴比** $q_\text{proj} = b_\text{proj}/a_\text{proj}$ 对**任意**投影方向均有 $q_\text{proj} \ge c/a$。

若观测到 $q_\text{proj} = q$，则内禀 $c/a$ 只能落在 $[0, q]$；所有 $c/a > q$ 的三维模型在几何上**不可能**。

---

## 快速开始

```bash
pip install -r requirements.txt
streamlit run app.py
```

默认地址：`http://localhost:8501`

---

## 页面说明

| 页面 | 功能 |
|------|------|
| **首页** | 定理陈述与导航 |
| **Constraint Explorer / 约束探索** | 给定观测 $q_\text{obs}$，$(b/a, c/a)$ 允许/禁止区域 |
| **Projection Sweep / 投影扫描** | $q_\text{proj}$ 热力图、分布、一维扫描 |
| **Mathematical Proof / 数学证明** | 分步 LaTeX 推导 |

---

## 文件结构

```
ellipsoid-projection-bound/
├── app.py
├── pages/
│   ├── 1_Constraint_Explorer.py
│   ├── 2_Projection_Sweep.py
│   └── 3_Mathematical_Proof.py
├── src/
│   ├── projection.py
│   ├── viz.py
│   └── ...
├── docs/
│   └── MATH_PROOF.md    # 完整数学证明
├── requirements.txt
└── .streamlit/config.toml
```

---

## 依赖

`streamlit`、`numpy`、`plotly`

---

## 许可证

MIT
