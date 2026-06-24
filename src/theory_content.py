"""LaTeX formula blocks for the derivation page."""

LATEX_SHAPE_TENSOR = r"\mathbf{S} = \mathrm{diag}(a^2,\; b^2,\; c^2), \qquad \lambda_1 \ge \lambda_2 \ge \lambda_3 > 0"

LATEX_PROJECTION = (
    r"\mathbf{S}_{\mathrm{proj}} = \mathbf{P}\,\mathbf{S}\,\mathbf{P}^{\mathsf T}, "
    r"\qquad \mu_1 = a_{\mathrm{proj}}^2 \ge \mu_2 = b_{\mathrm{proj}}^2"
)

LATEX_INTERLACING = (
    r"a^2 \;\ge\; a_{\mathrm{proj}}^2 \;\ge\; b^2 \;\ge\; b_{\mathrm{proj}}^2 \;\ge\; c^2"
)

LATEX_BOUND_A = r"a_{\mathrm{proj}} \le a"

LATEX_BOUND_B = r"b_{\mathrm{proj}} \ge c"

LATEX_MAIN = (
    r"q_{\mathrm{proj}} = \frac{b_{\mathrm{proj}}}{a_{\mathrm{proj}}} "
    r"\;\ge\; \frac{c}{a_{\mathrm{proj}}} \;\ge\; \frac{c}{a}"
)

LATEX_CONSEQUENCE = (
    r"q_{\mathrm{obs}} = q \quad \Longrightarrow \quad 0 < \frac{c}{a} \le q"
)

LATEX_WLOG = (
    r"\text{WLOG } a=1:\quad p = \frac{b}{a},\; q_{\mathrm{int}} = \frac{c}{a}, "
    r"\quad \mathbf{S} = \mathrm{diag}(1,\; p^2,\; q_{\mathrm{int}}^2)"
)

LATEX_ANALYTICAL = (
    r"\text{With } \mathbf{n} = (n_1, n_2, n_3),\; "
    r"T = 1 + p^2 + q^2 - (n_1^2 + p^2 n_2^2 + q^2 n_3^2),\; "
    r"D = p^2 q^2 n_1^2 + q^2 n_2^2 + p^2 n_3^2"
)

LATEX_ANALYTICAL_Q = (
    r"q_{\mathrm{proj}} = \sqrt{\frac{\mu_{\min}}{\mu_{\max}}}, \quad "
    r"\mu_\pm = \frac{T \pm \sqrt{T^2 - 4D}}{2}"
)
