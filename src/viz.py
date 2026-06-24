"""Plotly figures for ellipsoid projection visualization."""

import numpy as np
import plotly.graph_objects as go

from src.projection import (
    generate_ellipsoid_surface,
    project_ellipsoid,
    projected_axis_ratio,
    projected_axis_ratio_grid,
    view_direction,
)


def _add_contour_level(fig, azim, elev, q_grid, level, color, name):
    fig.add_trace(
        go.Contour(
            x=azim,
            y=elev,
            z=q_grid,
            contours=dict(
                type="constraint",
                operation="=",
                value=level,
                coloring="lines",
            ),
            showscale=False,
            line=dict(color=color, width=2),
            name=name,
        )
    )


def build_parameter_space_figure(q_obs, p_sel, q_sel, allowed_label, forbidden_label):
    """Triangle in (b/a, c/a) with allowed/forbidden split at c/a = q_obs."""
    ba_a = np.array([0.0, 1.0, 0.0, 0.0])
    ca_a = np.array([0.0, min(1.0, q_obs), q_obs, 0.0])
    ba_f = np.array([q_obs, 1.0, 1.0, q_obs])
    ca_f = np.array([q_obs, 1.0, q_obs, q_obs])

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=ba_a,
            y=ca_a,
            fill="toself",
            fillcolor="rgba(40,167,69,0.25)",
            line=dict(color="rgba(40,167,69,0.8)"),
            name=allowed_label,
            hoverinfo="skip",
        )
    )
    if q_obs < 1.0:
        fig.add_trace(
            go.Scatter(
                x=ba_f,
                y=ca_f,
                fill="toself",
                fillcolor="rgba(220,53,69,0.2)",
                line=dict(color="rgba(220,53,69,0.8)"),
                name=forbidden_label,
                hoverinfo="skip",
            )
        )
    fig.add_trace(
        go.Scatter(
            x=[0, 1, 0],
            y=[0, 1, 0],
            mode="lines",
            line=dict(color="gray", width=2, dash="dot"),
            name="c/a = b/a",
            hoverinfo="skip",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[0, 1],
            y=[q_obs, q_obs],
            mode="lines",
            line=dict(color="crimson", width=2, dash="dash"),
            name=f"q_obs = {q_obs:.3f}",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[p_sel],
            y=[q_sel],
            mode="markers",
            marker=dict(size=14, color="navy", symbol="circle", line=dict(width=2, color="white")),
            name=f"({p_sel:.2f}, {q_sel:.2f})",
        )
    )
    fig.update_layout(
        xaxis_title="b/a",
        yaxis_title="c/a",
        xaxis=dict(range=[0, 1.05], constrain="domain"),
        yaxis=dict(range=[0, 1.05], scaleanchor="x", scaleratio=1),
        height=420,
        margin=dict(l=50, r=20, t=30, b=50),
        legend=dict(orientation="h", yanchor="bottom", y=1.02),
    )
    return fig


def build_qproj_heatmap(p, q, n_azim=72, n_elev=37, q_obs=None):
    azim, elev, q_grid = projected_axis_ratio_grid(p, q, n_azim, n_elev)
    q_min = float(q_grid.min())
    fig = go.Figure(
        data=go.Heatmap(
            x=azim,
            y=elev,
            z=q_grid,
            colorscale="Viridis",
            colorbar=dict(title="q_proj"),
        )
    )
    _add_contour_level(fig, azim, elev, q_grid, q, "crimson", f"min c/a = {q:.3f}")
    if q_obs is not None:
        _add_contour_level(fig, azim, elev, q_grid, q_obs, "white", f"q_obs = {q_obs:.3f}")
    fig.update_layout(
        title=(
            f"q_proj(azimuth, elevation)  |  b/a={p:.2f}, c/a={q:.2f}  |  "
            f"min = {q_min:.3f}"
        ),
        xaxis_title="Azimuth (°)",
        yaxis_title="Elevation (°)",
        height=380,
        margin=dict(l=50, r=20, t=50, b=50),
    )
    return fig


def build_3d_ellipsoid_figure(p, q, azim_deg, elev_deg):
    x, y, z = generate_ellipsoid_surface(p, q, n=40)
    n = view_direction(azim_deg, elev_deg)
    lim = max(1.0, p, q) * 1.2
    traces = [
        go.Surface(
            x=x,
            y=y,
            z=z,
            colorscale="Blues",
            opacity=0.75,
            showscale=False,
            name="ellipsoid",
        ),
        go.Scatter3d(
            x=[0, lim], y=[0, 0], z=[0, 0],
            mode="lines",
            line=dict(color="red", width=4),
            name="x",
        ),
        go.Scatter3d(
            x=[0, 0], y=[0, p * lim], z=[0, 0],
            mode="lines",
            line=dict(color="green", width=4),
            name="y",
        ),
        go.Scatter3d(
            x=[0, 0], y=[0, 0], z=[0, q * lim],
            mode="lines",
            line=dict(color="blue", width=4),
            name="z",
        ),
        go.Scatter3d(
            x=[0, lim * n[0]],
            y=[0, lim * n[1]],
            z=[0, lim * n[2]],
            mode="lines+markers",
            line=dict(color="crimson", width=6),
            marker=dict(size=4, color="crimson"),
            name="view",
        ),
    ]
    fig = go.Figure(data=traces)
    fig.update_layout(
        title=f"3D ellipsoid (a=1, b/a={p:.2f}, c/a={q:.2f})",
        scene=dict(
            xaxis_title="x",
            yaxis_title="y",
            zaxis_title="z",
            aspectmode="data",
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.2)),
        ),
        height=420,
        margin=dict(l=0, r=0, t=50, b=0),
    )
    return fig


def build_2d_projection_figure(p, q, azim_deg, elev_deg):
    ratio, major, minor, pts, _ = project_ellipsoid(p, q, azim_deg, elev_deg)
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=pts[:, 0],
            y=pts[:, 1],
            mode="lines",
            line=dict(color="steelblue", width=2),
            name="projection",
        )
    )
    lim = max(major, minor) * 1.2
    fig.add_hline(y=0, line=dict(color="lightgray", width=1))
    fig.add_vline(x=0, line=dict(color="lightgray", width=1))
    fig.add_annotation(
        x=0.02,
        y=0.98,
        xref="paper",
        yref="paper",
        showarrow=False,
        text=f"c/a lower bound = {q:.3f}",
        font=dict(color="crimson"),
        bgcolor="rgba(255,255,255,0.8)",
    )
    fig.update_layout(
        title=(
            f"Projection  |  q_proj = {ratio:.3f}  |  "
            f"a_proj = {major:.3f}, b_proj = {minor:.3f}"
        ),
        xaxis=dict(range=[-lim, lim], scaleanchor="y", scaleratio=1),
        yaxis=dict(range=[-lim, lim]),
        height=380,
        margin=dict(l=40, r=20, t=60, b=40),
    )
    return fig


def build_1d_sweep_figure(p, q, phi_values=(0, 45, 90)):
    elev = np.linspace(-90, 90, 181)
    fig = go.Figure()
    for phi in phi_values:
        vals = [projected_axis_ratio(p, q, phi, el) for el in elev]
        fig.add_trace(go.Scatter(x=elev, y=vals, mode="lines", name=f"azim = {phi}°"))
    fig.add_hline(
        y=q,
        line=dict(color="crimson", width=2, dash="dash"),
        annotation_text=f"c/a = {q:.3f}",
    )
    fig.update_layout(
        title=f"q_proj vs elevation (b/a={p:.2f}, c/a={q:.2f})",
        xaxis_title="Elevation (°)",
        yaxis_title="q_proj",
        height=400,
        legend=dict(yanchor="top", y=0.99),
    )
    return fig


def build_qproj_histogram(p, q, q_obs=None, n_azim=60, n_elev=31):
    _, _, q_grid = projected_axis_ratio_grid(p, q, n_azim, n_elev)
    flat = q_grid.ravel()
    fig = go.Figure(data=[go.Histogram(x=flat, nbinsx=40, marker_color="steelblue")])
    fig.add_vline(
        x=q,
        line=dict(color="crimson", width=2, dash="dash"),
        annotation_text=f"min = c/a = {q:.3f}",
    )
    if q_obs is not None:
        fig.add_vline(
            x=q_obs,
            line=dict(color="darkgreen", width=2, dash="dot"),
            annotation_text=f"q_obs = {q_obs:.3f}",
        )
    fig.update_layout(
        title="Distribution of q_proj over viewing grid",
        xaxis_title="q_proj",
        yaxis_title="count",
        height=360,
    )
    return fig


def build_sweep_heatmap_full(p, q, n_azim=90, n_elev=45):
    return build_qproj_heatmap(p, q, n_azim, n_elev, q_obs=None)
