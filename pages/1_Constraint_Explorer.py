"""Constraint Explorer — how 2D observations constrain 3D shape."""

import streamlit as st

from src.i18n import t
from src.projection import is_allowed, min_projected_ratio, project_ellipsoid
from src.ui import init_session_state, render_header
from src.viz import (
    build_2d_projection_figure,
    build_3d_ellipsoid_figure,
    build_parameter_space_figure,
    build_qproj_heatmap,
)

st.set_page_config(page_title="Constraint Explorer", page_icon="📊", layout="wide")

init_session_state()
render_header()

lang = st.session_state.lang
st.header(t("page_constraint_title", lang))

st.success(t("constraint_one_liner", lang))
with st.expander(t("hint_update", lang), expanded=False):
    st.markdown(t("constraint_how_to", lang))

params = st.session_state.ellipsoid_params

with st.sidebar:
    st.subheader(t("sidebar_params", lang))
    with st.form("constraint_params"):
        q_obs = st.slider(t("param_q_obs", lang), 0.05, 1.0, params["q_obs"], 0.01)
        p = st.slider(t("param_p", lang), 0.05, 1.0, params["p"], 0.01)
        q_max = max(0.05, min(p, 1.0))
        q = st.slider(t("param_q", lang), 0.05, q_max, min(params["q"], q_max), 0.01)
        azim = st.slider(t("param_azim", lang), 0.0, 360.0, params["azim"], 1.0)
        elev = st.slider(t("param_elev", lang), -90.0, 90.0, params["elev"], 1.0)
        submitted = st.form_submit_button(t("btn_update", lang), type="primary")

    c1, c2, c3, c4 = st.columns(4)
    if c1.button(t("preset_sphere", lang)):
        st.session_state.ellipsoid_params = {
            "q_obs": q_obs,
            "p": 1.0,
            "q": 1.0,
            "azim": azim,
            "elev": elev,
        }
        st.rerun()
    if c2.button(t("preset_oblate", lang)):
        st.session_state.ellipsoid_params = {
            "q_obs": q_obs,
            "p": 1.0,
            "q": 0.3,
            "azim": azim,
            "elev": elev,
        }
        st.rerun()
    if c3.button(t("preset_prolate", lang)):
        st.session_state.ellipsoid_params = {
            "q_obs": q_obs,
            "p": 0.3,
            "q": 0.3,
            "azim": azim,
            "elev": elev,
        }
        st.rerun()
    if c4.button(t("preset_triaxial", lang)):
        st.session_state.ellipsoid_params = {
            "q_obs": q_obs,
            "p": 0.8,
            "q": 0.7,
            "azim": azim,
            "elev": elev,
        }
        st.rerun()

if submitted:
    st.session_state.ellipsoid_params = {
        "q_obs": q_obs,
        "p": p,
        "q": q,
        "azim": azim,
        "elev": elev,
    }

par = st.session_state.ellipsoid_params
q_obs = par["q_obs"]
p = par["p"]
q = par["q"]
azim = par["azim"]
elev = par["elev"]


@st.cache_data(show_spinner=False)
def cached_param_space(q_obs, p, q, allowed_l, forbidden_l):
    return build_parameter_space_figure(q_obs, p, q, allowed_l, forbidden_l)


@st.cache_data(show_spinner=False)
def cached_heatmap(p, q, q_obs):
    return build_qproj_heatmap(p, q, q_obs=q_obs)


@st.cache_data(show_spinner=False)
def cached_3d(p, q, azim, elev):
    return build_3d_ellipsoid_figure(p, q, azim, elev)


@st.cache_data(show_spinner=False)
def cached_2d(p, q, azim, elev):
    return build_2d_projection_figure(p, q, azim, elev)


left, right = st.columns([3, 2])

with left:
    st.markdown(f"{t('constraint_focus', lang)} {t('panel_param_space', lang)}")
    st.caption(t("constraint_panel_a", lang))
    fig_ps = cached_param_space(
        q_obs, p, q, t("allowed_label", lang), t("forbidden_label", lang)
    )
    st.plotly_chart(fig_ps, use_container_width=True)

    st.markdown(f"**{t('panel_heatmap', lang)}**")
    st.caption(t("constraint_panel_b", lang))
    fig_hm = cached_heatmap(p, q, q_obs)
    st.plotly_chart(fig_hm, use_container_width=True)

with right:
    st.markdown(f"**{t('panel_3d', lang)}**")
    st.caption(t("constraint_panel_c", lang))
    st.plotly_chart(cached_3d(p, q, azim, elev), use_container_width=True)

    st.markdown(f"**{t('panel_2d', lang)}**")
    st.caption(t("constraint_panel_d", lang))
    st.plotly_chart(cached_2d(p, q, azim, elev), use_container_width=True)

q_proj, _, _, _, _ = project_ellipsoid(p, q, azim, elev)
q_min = min_projected_ratio(p, q)
allowed = is_allowed(p, q, q_obs)

m1, m2, m3, m4, m5 = st.columns(5)
m1.metric(t("metric_c_over_a", lang), f"{q:.3f}")
m2.metric(t("metric_q_proj", lang), f"{q_proj:.3f}")
m3.metric(t("metric_q_min", lang), f"{q_min:.3f}")
m4.metric(t("metric_q_obs", lang), f"{q_obs:.3f}")
m5.metric(
    t("metric_status", lang),
    t("status_allowed", lang) if allowed else t("status_forbidden", lang),
)
