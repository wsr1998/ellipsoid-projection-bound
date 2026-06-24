# ellipsoid-projection-bound

**交互式可视化工具：证明三轴椭球的投影轴比是真实轴比的严格上界。**

> English documentation: [README.md](README.md)

---

## 核心结论

对于半轴满足 $a \ge b \ge c > 0$ 的三轴椭球，**投影（观测）轴比** $q_\text{proj} \equiv b_\text{proj}/a_\text{proj}$ 对**任意**投影方向均满足

$$
q_\text{proj} \;\ge\; \frac{c}{a}
$$

换句话说：将椭球投影到平面上，只会让它看起来*更圆*，永远不会比真实形状*更扁*。

本工具让你交互式地探索这一定理：拖动滑块改变椭球形状和观察角度，随时验证投影轴比始终不低于真实 $c/a$。

---

## 数学背景

证明的核心是 **Poincaré（Cauchy 交错）定理**。椭球用对称正定形状张量 **S** 表示，其特征值为 $\lambda_1 = a^2 \ge \lambda_2 = b^2 \ge \lambda_3 = c^2$。将椭球正交投影到任意平面，得到的 $2\times2$ 投影形状张量的特征值 $\mu_1 = a_\text{proj}^2$，$\mu_2 = b_\text{proj}^2$ 与全矩阵特征值交错排列：

$$
a^2 \;\ge\; a_\text{proj}^2 \;\ge\; b^2 \;\ge\; b_\text{proj}^2 \;\ge\; c^2
$$

取平方根得到两个不等式：

1. $a_\text{proj} \le a$ — 投影不能使最长轴变大；
2. $b_\text{proj} \ge c$ — 投影不能使最短轴变小。

两式相除即得 $q_\text{proj} = b_\text{proj}/a_\text{proj} \ge c/a$。

**实际意义：** 观测到的投影扁率 $q_\text{proj}$ 排除了所有比观测值"更圆"的真实形状——所有满足 $c/a > q_\text{proj}$ 的模型在几何上均被禁止。

---

## 演示截图

![screenshot](docs/screenshot.png)

应用界面包含：

- **上排** — 四个三维椭球视图（XY、XZ、YZ 平面 + 自定义角度）；
- **下排** — 对应的二维投影图，显示计算所得的投影轴比；
- **侧边栏指标** — 真实三维轴比 $b/a$、$c/a$、$c/b$ 以及自定义视角的投影轴比。

---

## 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/<your-username>/ellipsoid-projection-bound.git
cd ellipsoid-projection-bound

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动应用
streamlit run app.py
```

应用默认在 `http://localhost:8501` 打开。

---

## 使用方法

| 控件 | 说明 |
|------|------|
| **a / b / c 滑块** | 设置三条半轴长度（建议保持 $a \ge b \ge c$） |
| **方位角** | 自定义观察方向的水平旋转角度（0°–360°） |
| **仰角** | 自定义观察方向的垂直倾斜角度（−90°–90°） |
| **快速预设** | 加载常见形状（扁球体、长椭球、球体） |

### 验证上界

1. 设置任意椭球，例如 $a=3,\; b=2,\; c=1$（$c/a = 0.333$）；
2. 扫描所有方位角和仰角；
3. 观察右下角**自定义投影轴比**始终不低于 $0.333$。

---

## 文件结构

```
ellipsoid-projection-bound/
├── app.py                    # 主 Streamlit 应用
├── requirements.txt          # Python 依赖
├── README.md                 # 英文文档
├── README_zh.md              # 中文文档（本文件）
└── docs/
    └── MATH_PROOF.md         # 完整数学证明
```

---

## 依赖库

| 包 | 用途 |
|----|------|
| `numpy` | 数值计算（投影、特征值分解） |
| `matplotlib` | 三维与二维绘图 |
| `streamlit` | 交互式 Web 界面 |

---

## 引用

若本可视化工具配合论文使用，请引用该几何证明所在的文献。核心不等式来自：

> Bellman, R. (1997). *Introduction to Matrix Analysis* (2nd ed.). SIAM.

---

## 许可证

MIT
