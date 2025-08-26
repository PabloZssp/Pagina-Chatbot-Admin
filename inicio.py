import streamlit as st
import Herramientas as h #modulo de herramientas para links de las paginas
import log

log.log_in()
st.markdown(h.page_bg_img, unsafe_allow_html=True)
