
import streamlit as st
import Herramientas as h #modulo de herramientas para links de las paginas

h.verificar_sesion()
st.set_page_config(page_title="Pagina principal", initial_sidebar_state="auto",page_icon="🤖", layout="centered")

st.title("Panel de administración de datos de Xoli")
st.markdown("  \n ")
st.subheader("Bienvenido al panel de administración")
with st.container():
 st.markdown(
        """
        <div style="padding-top:4rem; font-size:18px;">
        """,
        unsafe_allow_html=True
    )

col_1, col_2, = st.columns([1,1])  # tamaños relativos

with col_1:
    bt_A = st.button("Ir a tablas")

with col_2:
    bt_B = st.button("Ir a Solicitud")

if bt_A:
    st.switch_page("pages/Menu_nuevo.py" )#boton para ir a la pagina de formularios
if bt_B:
    st.switch_page("pages/solicitudes.py" )#boton para ir a la pagina de solicitudes


st.markdown(h.page_bg_img, unsafe_allow_html=True)

h.MenuPrincipal()

