"""Bilingual UI strings (default English)."""

STRINGS = {
    "en": {
        "app_title": "Ellipsoid Projection Bound",
        "app_subtitle": "How 2D observations constrain 3D intrinsic shape",
        "lang_label": "Language",
        "lang_en": "English",
        "lang_zh": "中文",
        "home_welcome": "Welcome",
        "home_body": (
            "For a triaxial ellipsoid with semi-axes $a \\ge b \\ge c > 0$, the **projected** "
            "axis ratio $q_{\\mathrm{proj}} = b_{\\mathrm{proj}}/a_{\\mathrm{proj}}$ satisfies "
            "$q_{\\mathrm{proj}} \\ge c/a$ for **every** projection direction.\n\n"
            "**Consequence:** if you observe $q_{\\mathrm{proj}} = q$, then the intrinsic "
            "$c/a$ must lie in $[0, q]$. All models with $c/a > q$ are geometrically forbidden.\n\n"
            "Use the sidebar to navigate:\n"
            "- **Constraint Explorer** — parameter-space allowed/forbidden regions\n"
            "- **Projection Sweep** — how $q_{\\mathrm{proj}}$ varies with viewing angle\n"
            "- **Mathematical Proof** — step-by-step derivation"
        ),
        "page_constraint_title": "Constraint Explorer",
        "constraint_one_liner": (
            "**Main result:** measuring a 2D axis ratio $q_{\\mathrm{obs}}$ means the intrinsic "
            "$c/a$ cannot exceed $q_{\\mathrm{obs}}$ — projection only makes shapes look rounder, never flatter."
        ),
        "constraint_how_to": (
            "**Task 1 — Pick a shape.** Click a preset (e.g. Oblate) or set $b/a$ and $c/a$ manually, "
            "then click **Update**. The blue dot in the top-left plot is your candidate model. "
            "Rotate the 3D ellipsoid (top-right) to build intuition for what the shape looks like.\n\n"
            "**Task 2 — Set an observation.** Move the $q_{\\mathrm{obs}}$ slider and click **Update**. "
            "The red dashed line in the parameter-space plot divides allowed (green) from forbidden (red). "
            "Is your blue dot above or below the line? Check the **Status** metric at the bottom.\n\n"
            "**Task 3 — Search for the flattest view.** Sweep azimuth and elevation, then click **Update**. "
            "Watch the 2D projection (bottom-right) change. Can you find the angle that produces the "
            "smallest $q_{\\mathrm{proj}}$? Compare it with $c/a$ in the metrics. In the bottom-left "
            "heatmap, the **red contour** marks $q_{\\mathrm{proj}} = c/a$. If the **white contour** "
            "($q_{\\mathrm{proj}} = q_{\\mathrm{obs}}$) also appears, some viewing angles produce a "
            "projection matching your observation."
        ),
        "constraint_panel_a": (
            "**Parameter space** — Each point is a possible intrinsic shape $(b/a,\\; c/a)$. "
            "The red dashed line is your observation $q_{\\mathrm{obs}}$. "
            "Shapes **below** the line are allowed; **above** are ruled out."
        ),
        "constraint_panel_b": (
            "**Projection map** — For the blue-dot shape, this shows how flat it looks from every viewing angle. "
            "Darker = flatter. The red contour is the minimum $q_{\\mathrm{proj}} = c/a$; "
            "the white contour marks $q_{\\mathrm{proj}} = q_{\\mathrm{obs}}$."
        ),
        "constraint_panel_c": (
            "**3D ellipsoid** — The actual shape at the blue dot ($a=1$). "
            "The red arrow is your current line of sight."
        ),
        "constraint_panel_d": (
            "**2D projection** — What you would see along that line of sight. "
            "Check that $q_{\\mathrm{proj}} \\ge c/a$ always holds."
        ),
        "constraint_focus": "Focus here first →",
        "page_sweep_title": "Projection Sweep",
        "sweep_one_liner": (
            "**Main point:** for a fixed 3D shape, $q_{\\mathrm{proj}}$ changes with viewing angle "
            "but **never drops below** $c/a$ — rotation only makes the silhouette rounder, not flatter."
        ),
        "sweep_how_to": (
            "**Task 1 — Verify the bound.** Pick any shape and click **Update**. "
            "In the 1D sweep, confirm every curve stays above the red $c/a$ line. "
            "In the histogram, check that no bin appears to the left of the red dashed line.\n\n"
            "**Task 2 — How likely is a flat view?** Set $q_{\\mathrm{obs}}$ to your observed value "
            "and click **Update**. The green dotted line in the histogram shows where your observation "
            "sits in the distribution. If $q_{\\mathrm{obs}}$ is near $c/a$, only a narrow set of "
            "viewing angles can produce it; if $q_{\\mathrm{obs}}$ is much larger, most viewing angles "
            "would produce a value at least that round."
        ),
        "sweep_panel_heatmap": (
            "**All-sky map** — color is $q_{\\mathrm{proj}}$ at each (azimuth, elevation). "
            "Darker regions are the flattest views; the global minimum equals $c/a$."
        ),
        "sweep_panel_hist": (
            "**Distribution** — how often each $q_{\\mathrm{proj}}$ occurs on a coarse viewing grid. "
            "Red dashed: theoretical minimum $c/a$. Green dotted: your $q_{\\mathrm{obs}}$ (if set)."
        ),
        "sweep_panel_1d": (
            "**Elevation scan** — at fixed azimuth, $q_{\\mathrm{proj}}$ vs elevation. "
            "Every curve should lie on or above the red $c/a$ bound."
        ),
        "page_proof_title": "Mathematical Proof",
        "sidebar_params": "Parameters",
        "param_q_obs": "Observed 2D axis ratio $q_{\\mathrm{obs}}$",
        "param_p": "Intrinsic $b/a$",
        "param_q": "Intrinsic $c/a$",
        "param_azim": "Azimuth (°)",
        "param_elev": "Elevation (°)",
        "btn_update": "Update",
        "hint_update": "Adjust sliders, then click **Update**.",
        "preset_oblate": "Oblate",
        "preset_prolate": "Prolate",
        "preset_sphere": "Sphere",
        "preset_triaxial": "Triaxial",
        "metric_c_over_a": "Intrinsic $c/a$",
        "metric_q_proj": "Current $q_{\\mathrm{proj}}$",
        "metric_q_min": "Min $q_{\\mathrm{proj}}$",
        "metric_q_obs": "Observed $q_{\\mathrm{obs}}$",
        "status_allowed": "Allowed",
        "status_forbidden": "Forbidden",
        "metric_status": "Status",
        "panel_param_space": "Parameter space $(b/a,\\; c/a)$",
        "panel_heatmap": "$q_{\\mathrm{proj}}$ vs viewing angle",
        "panel_3d": "3D ellipsoid",
        "panel_2d": "2D projection",
        "allowed_label": "Allowed (c/a \u2264 q_obs)",
        "forbidden_label": "Forbidden (c/a > q_obs)",
        "expander_sweep_1d": "1D sweep ($q_{\\mathrm{proj}}$ vs elevation)",
        "expander_hist": "$q_{\\mathrm{proj}}$ distribution over viewing directions",
        "der_intro": (
            "Self-contained derivation that the projected axis ratio is bounded below by $c/a$, "
            "via the Poincaré (Cauchy interlacing) theorem on the ellipsoid shape tensor."
        ),
        "sec1_title": "1. Shape tensor",
        "sec1_body": "A triaxial ellipsoid aligned with the coordinate axes has shape tensor $\\mathbf{S} = \\mathrm{diag}(a^2, b^2, c^2)$ with $a \\ge b \\ge c > 0$.",
        "sec1_wlog_note": (
            "**WLOG** (*without loss of generality*) means we may rescale all axes by the same factor "
            "and set $a=1$. Only **axis ratios** $b/a$ and $c/a$ matter for $q_{\\mathrm{proj}}$; "
            "the absolute size of the ellipsoid does not change the proof."
        ),
        "sec1_shape_defs": (
            "**Shape classes** (with $a \\ge b \\ge c$):\n\n"
            "- **Sphere**: $a = b = c$ ($b/a = c/a = 1$)\n"
            "- **Oblate spheroid**: $a = b > c$ ($b/a = 1$, $0 < c/a < 1$) — disk-like\n"
            "- **Prolate spheroid**: $a > b = c$ ($b/a = c/a < 1$) — cigar-like\n"
            "- **Triaxial ellipsoid**: $a > b > c$ ($b/a$ and $c/a$ all distinct) — the general case"
        ),
        "sec2_title": "2. Orthogonal projection",
        "sec2_body": "Project onto the plane perpendicular to the unit viewing direction $\\mathbf{n}$. The projected $2\\times2$ tensor has eigenvalues $\\mu_1 = a_{\\mathrm{proj}}^2 \\ge \\mu_2 = b_{\\mathrm{proj}}^2$.",
        "sec3_title": "3. Cauchy interlacing",
        "sec3_body": "Eigenvalues of the projected tensor interlace with those of $\\mathbf{S}$:",
        "sec4_title": "4. Two bounds",
        "sec4_body": "Taking square roots:",
        "sec5_title": "5. Main inequality",
        "sec5_body": "Dividing the two bounds:",
        "sec6_title": "6. Observational consequence",
        "sec6_body": (
            "Measuring $q_{\\mathrm{proj}} = q$ rules out every intrinsic shape with $c/a > q$. "
            "In the $(b/a, c/a)$ plane, feasible shapes satisfy $0 < c/a \\le b/a \\le 1$ and "
            "$c/a \\le q_{\\mathrm{obs}}$."
        ),
        "sec7_title": "7. Geometric interpretation",
        "sec7_body": (
            "Projection onto a plane can only make an ellipsoid appear **rounder**, never **flatter**, "
            "than it intrinsically is. The minimum projected axis ratio equals $c/a$, achieved when "
            "the viewing direction aligns with the intermediate principal axis."
        ),
        "sec8_title": "8. Analytical formula",
        "sec8_body": (
            "With $a=1$ and viewing direction $\\mathbf{n}=(n_1,n_2,n_3)$, the projected eigenvalues "
            "satisfy a quadratic whose coefficients are:"
        ),
    },
    "zh": {
        "app_title": "椭球投影轴比上界",
        "app_subtitle": "二维观测如何约束三维内禀形状",
        "lang_label": "语言",
        "lang_en": "English",
        "lang_zh": "中文",
        "home_welcome": "欢迎",
        "home_body": (
            "对半轴满足 $a \\ge b \\ge c > 0$ 的三轴椭球，**投影**轴比 "
            "$q_{\\mathrm{proj}} = b_{\\mathrm{proj}}/a_{\\mathrm{proj}}$ 对**任意**投影方向均有 "
            "$q_{\\mathrm{proj}} \\ge c/a$。\n\n"
            "**推论：**若观测到 $q_{\\mathrm{proj}} = q$，则内禀 $c/a$ 只能落在 $[0, q]$；"
            "所有 $c/a > q$ 的三维模型在几何上**不可能**。\n\n"
            "请通过侧边栏切换页面：\n"
            "- **Constraint Explorer / 约束探索** — 参数空间允许/禁止区域\n"
            "- **Projection Sweep / 投影扫描** — $q_{\\mathrm{proj}}$ 随视角变化\n"
            "- **Mathematical Proof / 数学证明** — 分步推导"
        ),
        "page_constraint_title": "约束探索",
        "constraint_one_liner": (
            "**主要结论：**若二维观测轴比为 $q_{\\mathrm{obs}}$，则内禀 $c/a$ 不可能超过 $q_{\\mathrm{obs}}$——"
            "投影只会让形状看起来更圆，绝不会更扁。"
        ),
        "constraint_how_to": (
            "**任务 1 — 选一个形状。** 点击预设（如扁椭球）或手动设 $b/a$、$c/a$，再点 **更新**。"
            "左上图蓝点是候选模型。旋转右上图三维椭球，建立形状直觉。\n\n"
            "**任务 2 — 设一个观测。** 拖动 $q_{\\mathrm{obs}}$ 滑块并点 **更新**。"
            "参数空间图中红色虚线划分允许（绿）与禁止（红）区域。蓝点在线上方还是下方？看底部 **状态**。\n\n"
            "**任务 3 — 找最扁的视角。** 扫描方位角与仰角后点 **更新**。"
            "观察右下二维投影变化。能否找到使 $q_{\\mathrm{proj}}$ 最小的角度？与指标中的 $c/a$ 比较。"
            "左下热力图中 **红色等高线** 为 $q_{\\mathrm{proj}} = c/a$；若出现 **白色等高线**"
            "（$q_{\\mathrm{proj}} = q_{\\mathrm{obs}}$），说明存在视角使投影与观测一致。"
        ),
        "constraint_panel_a": (
            "**参数空间** — 每一点代表一个可能的内禀形状 $(b/a,\\; c/a)$。"
            "红色虚线是观测 $q_{\\mathrm{obs}}$。线**下方**允许，**上方**排除。"
        ),
        "constraint_panel_b": (
            "**投影图** — 对蓝点形状，显示各视角下的投影扁率。"
            "颜色越深越扁。红色等高线 = 最小 $q_{\\mathrm{proj}} = c/a$；"
            "白色等高线 = $q_{\\mathrm{proj}} = q_{\\mathrm{obs}}$。"
        ),
        "constraint_panel_c": (
            "**三维椭球** — 蓝点对应的真实形状（$a=1$）。红色箭头为当前视线。"
        ),
        "constraint_panel_d": (
            "**二维投影** — 沿该视线的观测椭圆。验证恒有 $q_{\\mathrm{proj}} \\ge c/a$。"
        ),
        "constraint_focus": "建议先看这里 →",
        "page_sweep_title": "投影扫描",
        "sweep_one_liner": (
            "**要点：**固定一个三维形状后，$q_{\\mathrm{proj}}$ 随视角变化，"
            "但**绝不会低于** $c/a$——旋转只会让轮廓更圆，不会更扁。"
        ),
        "sweep_how_to": (
            "**任务 1 — 验证下界。** 任选形状并点 **更新**。"
            "在一维扫描中确认每条曲线都在红色 $c/a$ 线上方；"
            "在直方图中确认没有柱子落在红色虚线左侧。\n\n"
            "**任务 2 — 扁的视角有多「难得」？** 设定 $q_{\\mathrm{obs}}$ 并点 **更新**。"
            "直方图中绿色点线标出观测值在分布中的位置。"
            "若 $q_{\\mathrm{obs}}$ 接近 $c/a$，只有少数视角能恰好那么扁；"
            "若 $q_{\\mathrm{obs}}$ 大得多，大多数视角都会至少那么圆。"
        ),
        "sweep_panel_heatmap": (
            "**全天球图** — 颜色为各 (方位角, 仰角) 下的 $q_{\\mathrm{proj}}$。"
            "越深越扁；全局最小值等于 $c/a$。"
        ),
        "sweep_panel_hist": (
            "**分布** — 在粗视角网格上 $q_{\\mathrm{proj}}$ 的出现频率。"
            "红色虚线：理论最小值 $c/a$。绿色点线：你设定的 $q_{\\mathrm{obs}}$（若有）。"
        ),
        "sweep_panel_1d": (
            "**仰角扫描** — 固定方位角时 $q_{\\mathrm{proj}}$ 随仰角变化。"
            "每条曲线都应在红色 $c/a$ 下界之上。"
        ),
        "page_proof_title": "数学证明",
        "sidebar_params": "参数",
        "param_q_obs": "观测二维轴比 $q_{\\mathrm{obs}}$",
        "param_p": "内禀 $b/a$",
        "param_q": "内禀 $c/a$",
        "param_azim": "方位角 (°)",
        "param_elev": "仰角 (°)",
        "btn_update": "更新",
        "hint_update": "调整滑块后，点击 **更新**。",
        "preset_oblate": "扁椭球",
        "preset_prolate": "长椭球",
        "preset_sphere": "球体",
        "preset_triaxial": "三轴",
        "metric_c_over_a": "内禀 $c/a$",
        "metric_q_proj": "当前 $q_{\\mathrm{proj}}$",
        "metric_q_min": "最小 $q_{\\mathrm{proj}}$",
        "metric_q_obs": "观测 $q_{\\mathrm{obs}}$",
        "status_allowed": "允许",
        "status_forbidden": "禁止",
        "metric_status": "状态",
        "panel_param_space": "参数空间 $(b/a,\\; c/a)$",
        "panel_heatmap": "$q_{\\mathrm{proj}}$ 随视角",
        "panel_3d": "三维椭球",
        "panel_2d": "二维投影",
        "allowed_label": "允许 (c/a \u2264 q_obs)",
        "forbidden_label": "禁止 (c/a > q_obs)",
        "expander_sweep_1d": "一维扫描（$q_{\\mathrm{proj}}$ vs 仰角）",
        "expander_hist": "视角均匀分布下 $q_{\\mathrm{proj}}$ 的分布",
        "der_intro": "基于形状张量的 Poincaré（Cauchy 交错）定理，证明投影轴比以 $c/a$ 为下界。",
        "sec1_title": "1. 形状张量",
        "sec1_body": "与坐标轴对齐的三轴椭球，形状张量 $\\mathbf{S} = \\mathrm{diag}(a^2, b^2, c^2)$，$a \\ge b \\ge c > 0$。",
        "sec1_wlog_note": (
            "**WLOG**（*without loss of generality*，**不失一般性**）表示可将三条半轴同乘一个常数，"
            "从而设 $a=1$。证明只依赖**轴比** $b/a$、$c/a$，与椭球的绝对尺度无关。"
        ),
        "sec1_shape_defs": (
            "**形状分类**（$a \\ge b \\ge c$）：\n\n"
            "- **球体**：$a = b = c$（$b/a = c/a = 1$）\n"
            "- **扁椭球**：$a = b > c$（$b/a = 1$，$0 < c/a < 1$）— 盘状\n"
            "- **长椭球**：$a > b = c$（$b/a = c/a < 1$）— 雪茄状\n"
            "- **三轴椭球**：$a > b > c$（$b/a$ 与 $c/a$ 互不相同）— 一般情形"
        ),
        "sec2_title": "2. 正交投影",
        "sec2_body": "沿单位视线 $\\mathbf{n}$ 正交投影到平面，得到 $2\\times2$ 投影张量，特征值 $\\mu_1 = a_{\\mathrm{proj}}^2 \\ge \\mu_2 = b_{\\mathrm{proj}}^2$。",
        "sec3_title": "3. Cauchy 交错",
        "sec3_body": "投影张量特征值与 $\\mathbf{S}$ 的特征值交错：",
        "sec4_title": "4. 两个界",
        "sec4_body": "开方得：",
        "sec5_title": "5. 主不等式",
        "sec5_body": "两式相除：",
        "sec6_title": "6. 观测推论",
        "sec6_body": (
            "测得 $q_{\\mathrm{proj}} = q$ 可排除所有 $c/a > q$ 的内禀形状。"
            "在 $(b/a, c/a)$ 平面上，可行域为 $0 < c/a \\le b/a \\le 1$ 且 $c/a \\le q_{\\mathrm{obs}}$。"
        ),
        "sec7_title": "7. 几何解释",
        "sec7_body": (
            "投影到平面只会让椭球看起来**更圆**，绝不会比内禀形状**更扁**。"
            "投影轴比的最小值等于 $c/a$，在视线与中间主轴对齐时达到。"
        ),
        "sec8_title": "8. 解析公式",
        "sec8_body": (
            "设 $a=1$，视线 $\\mathbf{n}=(n_1,n_2,n_3)$，投影特征值满足一个二次方程，系数为："
        ),
    },
}


def t(key: str, lang: str = "en") -> str:
    return STRINGS.get(lang, STRINGS["en"]).get(key, key)
