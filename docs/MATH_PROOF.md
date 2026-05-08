# Mathematical Proof: Projected Axis Ratio as an Upper Bound

## Statement

For a triaxial ellipsoid with semi-axes $a \ge b \ge c > 0$, the projected axis ratio
$q_\text{proj} = b_\text{proj} / a_\text{proj}$ satisfies

$$q_\text{proj} \ge \frac{c}{a}$$

for **every** projection direction.

## Proof

### Setup

Represent the ellipsoid by a symmetric positive-definite **shape tensor** $\mathbf{S}$
with eigenvalues

$$\lambda_1 = a^2, \quad \lambda_2 = b^2, \quad \lambda_3 = c^2, \qquad \lambda_1 \ge \lambda_2 \ge \lambda_3 > 0.$$

When the ellipsoid is orthogonally projected onto an arbitrary plane, the image is an
ellipse described by a $2\times2$ projected shape tensor $\mathbf{S}_\text{proj}$ with
eigenvalues $\mu_1 = a_\text{proj}^2 \ge \mu_2 = b_\text{proj}^2$.

### Applying the Poincaré / Cauchy Interlacing Theorem

By the **Poincaré separation theorem** (also called the Cauchy interlacing theorem;
see Bellman 1997), the eigenvalues of any $2\times2$ principal submatrix of a
$3\times3$ symmetric matrix interlace with the eigenvalues of the full matrix.
Applied to our shape tensor this gives the **interlacing chain**:

$$a^2 \;\ge\; a_\text{proj}^2 \;\ge\; b^2 \;\ge\; b_\text{proj}^2 \;\ge\; c^2.$$

### Extracting the Two Bounds

Taking square roots (all quantities are positive):

1. From $a^2 \ge a_\text{proj}^2$:
   $$a_\text{proj} \le a \tag{1}$$
   Projection cannot enlarge the longest axis.

2. From $b_\text{proj}^2 \ge c^2$:
   $$b_\text{proj} \ge c \tag{2}$$
   Projection cannot shrink below the shortest intrinsic axis.

### Combining the Bounds

$$q_\text{proj} = \frac{b_\text{proj}}{a_\text{proj}}
  \;\overset{(2)}{\ge}\; \frac{c}{a_\text{proj}}
  \;\overset{(1)}{\ge}\; \frac{c}{a}. \qquad \blacksquare$$

## Geometric Interpretation

Projection onto a plane can only make an ellipsoid appear *rounder*, never *flatter*,
than it intrinsically is.

**Observational consequence:** measuring $q_\text{proj}$ rules out every intrinsic
shape with $c/a > q_\text{proj}$, because such shapes are geometrically prohibited.

## Reference

Bellman, R. (1997). *Introduction to Matrix Analysis* (2nd ed.). SIAM.
