"""LaTeX mathematical derivation."""

import streamlit as st

from src.derivation import render_derivation_page
from src.ui import init_session_state, render_header

st.set_page_config(page_title="Mathematical Proof", page_icon="📐", layout="wide")

init_session_state()
render_header()
render_derivation_page()
