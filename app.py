"""Streamlit entry point — home / welcome page.

See docs/MATH_PROOF.md for the full mathematical proof.
"""

import streamlit as st

from src.i18n import t
from src.theory_content import LATEX_INTERLACING, LATEX_MAIN
from src.ui import init_session_state, render_header

st.set_page_config(
    page_title="Ellipsoid Projection Bound",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

init_session_state()
render_header()

lang = st.session_state.lang
st.markdown(f"### {t('home_welcome', lang)}")
st.markdown(t("home_body", lang))

st.latex(LATEX_INTERLACING)
st.latex(LATEX_MAIN)
