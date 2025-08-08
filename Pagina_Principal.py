######
# Pagina_Principal.py  
# El arcvhio Formularios.py se cabiara el nomebre a Formularios.py
# Por el momento lo dejaremos asi para cuestiones de una Version alfa
######
# Este archivo es la pagina principal del chatbot admin
# Este por el momento se utilizara para hacer un menu princial 
# Despues veremos de que manera implemetar mas cosas
import streamlit as st
import Herramientas as h #modulo de herramientas para links de las paginas

col_1,col_2=st.columns(2)
st.set_page_config(page_title="Pagina principal", initial_sidebar_state="auto",page_icon="🤖", layout="centered")

st.header("CHATBOT ADMIN")


st.subheader("Bienvenido al Chatbot Admin, aqui podras administrar los datos de tu chatbot")


col_1,col_2=st.columns(2)
with col_1:
    bt_A = st.button("Ir a Formularios")

with col_2:
    bt_b = st.button("Ir a Graficas" )

if bt_A:
    st.switch_page("pages/Formularios.py" )#boton para ir a la pagina de formularios
if bt_b:
    st.switch_page("pages/Chatbot.py" )#boton para ir a la pagina de graficas


st.markdown(h.page_bg_img, unsafe_allow_html=True)

h.MenuPrincipal()

