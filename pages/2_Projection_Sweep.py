"""Projection sweep — q_proj vs viewing angle."""

import streamlit as st

from src.i18n import t
from src.ui import init_session_state, render_header
from src.viz import build_1d_sweep_figure, build_qproj_histogram, build_sweep_heatmap_full

st.set_page_config(page_title="Projection Sweep", page_icon="🔭", layout="wide")

init_session_state()
render_header()

lang = st.session_state.lang
st.header(t("page_sweep_title", lang))

st.success(t("sweep_one_liner", lang))
with st.expander(t("hint_update", lang), expanded=False):
    st.markdown(t("sweep_how_to", lang))

params = st.session_state.ellipsoid_params

with st.sidebar:
    st.subheader(t("sidebar_params", lang))
    with st.form("sweep_params"):
        q_obs = st.slider(t("param_q_obs", lang), 0.05, 1.0, params["q_obs"], 0.01)
        p = st.slider(t("param_p", lang), 0.05, 1.0, params["p"], 0.01)
        q_max = max(0.05, min(p, 1.0))
        q = st.slider(t("param_q", lang), 0.05, q_max, min(params["q"], q_max), 0.01)
        submitted = st.form_submit_button(t("btn_update", lang), type="primary")

if submitted:
    st.session_state.ellipsoid_params = {**params, "q_obs": q_obs, "p": p, "q": q}

par = st.session_state.ellipsoid_params
q_obs, p, q = par["q_obs"], par["p"], par["q"]


@st.cache_data(show_spinner=False)
def cached_heatmap(p, q):
    return build_sweep_heatmap_full(p, q, 90, 45)


@st.cache_data(show_spinner=False)
def cached_hist(p, q, q_obs):
    return build_qproj_histogram(p, q, q_obs)


@st.cache_data(show_spinner=False)
def cached_1d(p, q):
    return build_1d_sweep_figure(p, q, (0, 45, 90, 135))


st.markdown(f"**{t('panel_heatmap', lang)}**")
st.caption(t("sweep_panel_heatmap", lang))
st.plotly_chart(cached_heatmap(p, q), use_container_width=True)

with st.expander(t("expander_hist", lang), expanded=True):
    st.caption(t("sweep_panel_hist", lang))
    st.plotly_chart(cached_hist(p, q, q_obs), use_container_width=True)

with st.expander(t("expander_sweep_1d", lang), expanded=True):
    st.caption(t("sweep_panel_1d", lang))
    st.plotly_chart(cached_1d(p, q), use_container_width=True)

m1, m2 = st.columns(2)
m1.metric(t("metric_c_over_a", lang), f"{q:.3f}")
m2.metric("b/a", f"{p:.3f}")
