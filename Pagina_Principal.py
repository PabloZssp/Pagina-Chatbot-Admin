import streamlit as st
import Herramientas as h #modulo de herramientas para links de las paginas


st.set_page_config(page_title="Pagina principal", initial_sidebar_state="auto",page_icon="🤖")

st.header("CHATBOT ADMIN")


st.subheader("Bienvenido al Chatbot Admin, aqui podras administrar los datos de tu chatbot")


st.markdown(h.page_bg_img, unsafe_allow_html=True)

h.MenuPrincipal()

