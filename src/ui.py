"""Shared Streamlit UI helpers."""

import streamlit as st

from src.i18n import t


def init_session_state():
    if "lang" not in st.session_state:
        st.session_state.lang = "en"
    if "ellipsoid_params" not in st.session_state:
        st.session_state.ellipsoid_params = {
            "q_obs": 0.5,
            "p": 0.7,
            "q": 0.3,
            "azim": 45.0,
            "elev": 30.0,
        }


def render_header():
    lang = st.session_state.lang
    col1, col2 = st.columns([4, 1])
    with col1:
        st.title(t("app_title", lang))
        st.caption(t("app_subtitle", lang))
    with col2:
        choice = st.selectbox(
            t("lang_label", lang),
            options=["en", "zh"],
            format_func=lambda x: t("lang_en", lang) if x == "en" else t("lang_zh", lang),
            key="lang_select",
            index=0 if lang == "en" else 1,
        )
        if choice != st.session_state.lang:
            st.session_state.lang = choice
            st.rerun()
