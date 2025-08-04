import streamlit as st
import pandas as pd
import Herramientas as h  # 

def graficas():

    h.MenuPrincipal()
    st.set_page_config(page_title="Graficas", initial_sidebar_state="auto", page_icon="📊")
    st.title("Graficas")
    st.subheader("Pronto disponible.. :D")

graficas()
