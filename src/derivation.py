"""Render the mathematical derivation page."""

import streamlit as st

from src import theory_content as tc
from src.i18n import t


def render_derivation_page():
    lang = st.session_state.lang
    st.header(t("page_proof_title", lang))
    st.markdown(t("der_intro", lang))

    st.subheader(t("sec1_title", lang))
    st.markdown(t("sec1_body", lang))
    st.latex(tc.LATEX_SHAPE_TENSOR)
    st.latex(tc.LATEX_WLOG)
    st.info(t("sec1_wlog_note", lang))
    st.info(t("sec1_shape_defs", lang))

    st.subheader(t("sec2_title", lang))
    st.markdown(t("sec2_body", lang))
    st.latex(tc.LATEX_PROJECTION)

    st.subheader(t("sec3_title", lang))
    st.markdown(t("sec3_body", lang))
    st.latex(tc.LATEX_INTERLACING)

    st.subheader(t("sec4_title", lang))
    st.markdown(t("sec4_body", lang))
    st.latex(tc.LATEX_BOUND_A)
    st.latex(tc.LATEX_BOUND_B)

    st.subheader(t("sec5_title", lang))
    st.markdown(t("sec5_body", lang))
    st.latex(tc.LATEX_MAIN)

    st.subheader(t("sec6_title", lang))
    st.markdown(t("sec6_body", lang))
    st.latex(tc.LATEX_CONSEQUENCE)

    st.subheader(t("sec7_title", lang))
    st.markdown(t("sec7_body", lang))

    st.subheader(t("sec8_title", lang))
    st.markdown(t("sec8_body", lang))
    st.latex(tc.LATEX_ANALYTICAL)
    st.latex(tc.LATEX_ANALYTICAL_Q)
