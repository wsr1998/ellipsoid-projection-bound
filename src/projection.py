"""Exact ellipsoid projection via the shape tensor (Poincaré interlacing)."""

import numpy as np


def view_direction(azim_deg, elev_deg):
    """Unit viewing direction n (line of sight) from azimuth and elevation in degrees."""
    az = np.radians(azim_deg)
    el = np.radians(elev_deg)
    return np.array([np.cos(el) * np.cos(az), np.cos(el) * np.sin(az), np.sin(el)])


def projection_basis(n):
    """Orthonormal basis (e1, e2) spanning the projection plane perpendicular to n."""
    n = np.asarray(n, dtype=float)
    n = n / np.linalg.norm(n)
    if abs(n[2]) < 0.999:
        up = np.array([0.0, 0.0, 1.0])
    else:
        up = np.array([1.0, 0.0, 0.0])
    e1 = np.cross(up, n)
    e1 = e1 / np.linalg.norm(e1)
    e2 = np.cross(n, e1)
    return e1, e2


def shape_matrix(p, q):
    """Shape tensor S = diag(1, p^2, q^2) with a=1 (WLOG)."""
    return np.diag([1.0, float(p) ** 2, float(q) ** 2])


def _view_components(azim_deg, elev_deg):
    """Direction cosines for viewing direction (scalar or broadcast arrays)."""
    az = np.radians(azim_deg)
    el = np.radians(elev_deg)
    n1 = np.cos(el) * np.cos(az)
    n2 = np.cos(el) * np.sin(az)
    n3 = np.sin(el)
    return n1, n2, n3


def projected_axis_ratio_from_n(p, q, n1, n2, n3):
    """
    Analytical q_proj from shape tensor S = diag(1, p^2, q^2) and view direction n.

    Eigenvalues of the projected 2×2 tensor satisfy a quadratic; q_proj = sqrt(μ_min/μ_max).
    """
    p2, q2 = float(p) ** 2, float(q) ** 2
    T = 1.0 + p2 + q2 - (n1**2 + p2 * n2**2 + q2 * n3**2)
    D = p2 * q2 * n1**2 + q2 * n2**2 + p2 * n3**2
    disc = np.sqrt(np.maximum(T**2 - 4.0 * D, 0.0))
    mu_max = (T + disc) / 2.0
    mu_min = (T - disc) / 2.0
    with np.errstate(invalid="ignore", divide="ignore"):
        ratio = np.sqrt(mu_min / mu_max)
    return ratio


def projected_axis_ratio(p, q, azim_deg, elev_deg):
    """Projected axis ratio q_proj = b_proj / a_proj for one viewing direction."""
    n1, n2, n3 = _view_components(azim_deg, elev_deg)
    return float(projected_axis_ratio_from_n(p, q, n1, n2, n3))


def project_ellipsoid(p, q, azim_deg, elev_deg, n_ellipse=100):
    """
    Orthogonal projection of the ellipsoid onto the plane perpendicular to the view.

    Returns
    -------
    axis_ratio, major_axis, minor_axis, proj_points (N×2), view_n (3,)
    """
    p, q = float(p), float(q)
    n = view_direction(azim_deg, elev_deg)
    e1, e2 = projection_basis(n)
    P = np.vstack([e1, e2])
    S = shape_matrix(p, q)
    S_proj = P @ S @ P.T
    evals, evecs = np.linalg.eigh(S_proj)
    order = evals.argsort()[::-1]
    evals = evals[order]
    evecs = evecs[:, order]
    major = np.sqrt(evals[0])
    minor = np.sqrt(evals[1])
    ratio = minor / major if major > 0 else 0.0

    t = np.linspace(0, 2 * np.pi, n_ellipse)
    ellipse_std = np.vstack([major * np.cos(t), minor * np.sin(t)])
    proj_points = (evecs @ ellipse_std).T
    return ratio, major, minor, proj_points, n


def projected_ellipse_points(p, q, azim_deg, elev_deg, n=100):
    """Parametric 2D points on the projected ellipse boundary."""
    _, _, _, pts, _ = project_ellipsoid(p, q, azim_deg, elev_deg, n_ellipse=n)
    return pts


def projected_axis_ratio_grid(p, q, n_azim=72, n_elev=37):
    """
    q_proj over a grid of viewing directions (vectorized).

    Returns azim_deg (n_azim,), elev_deg (n_elev,), q_grid (n_elev, n_azim).
    """
    azim = np.linspace(0.0, 360.0, n_azim, endpoint=False)
    elev = np.linspace(-90.0, 90.0, n_elev)
    AZ, EL = np.meshgrid(azim, elev)
    n1, n2, n3 = _view_components(AZ, EL)
    q_grid = projected_axis_ratio_from_n(p, q, n1, n2, n3)
    return azim, elev, q_grid


def min_projected_ratio(p, q):
    """Theoretical minimum of q_proj over all viewing directions (= c/a = q)."""
    return float(q)


def generate_ellipsoid_surface(p, q, n=50):
    """Surface mesh with a=1, semi-axes (1, p, q)."""
    u = np.linspace(0, 2 * np.pi, n)
    v = np.linspace(0, np.pi, n)
    x = np.outer(np.cos(u), np.sin(v))
    y = p * np.outer(np.sin(u), np.sin(v))
    z = q * np.outer(np.ones_like(u), np.cos(v))
    return x, y, z


def is_allowed(p, q, q_obs):
    """True if intrinsic c/a = q is compatible with observed q_obs (q <= q_obs)."""
    return q <= q_obs + 1e-12
