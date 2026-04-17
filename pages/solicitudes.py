import streamlit as st
import pandas as pd
import Herramientas as h  
h.verificar_sesion()
h.acceso_multiple(["administrador"])

def graficas():

    h.MenuPrincipal()
    st.set_page_config(page_title="Solicitudes", initial_sidebar_state="auto", page_icon="📊")
    st.title("Solicitudes de funciones")
    st.subheader("Pronto disponible.. :D")
    st.markdown(h.page_bg_img,unsafe_allow_html=True)

graficas()
