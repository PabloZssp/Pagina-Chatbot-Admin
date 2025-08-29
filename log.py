import streamlit as st
import json as j  # Asegúrate de importar json correctamente
import conexion2 as cn

def log_in():
    st.set_page_config(page_title="Iniciar sesión", page_icon="🌎")

    st.title("Iniciar sesión")

    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        user = cn.validar_usuario(usuario, password)
        if user:
            st.session_state["usuario"] = user[0]
            st.session_state["rol"] = user[1]
            st.success(f"Bienvenido {user[0]} ({user[1]})")
            st.switch_page("pages/Pagina_Principal.py")
            st.rerun()
        else:
            st.error("Usuario o contraseña incorrectos")


def log_out():
    
    for key in ["usuario", "rol"]:
        if key in st.session_state:
            del st.session_state[key]   
    st.switch_page("inicio.py")


def obtener_rol_actual():
    if "rol" in st.session_state:
        return st.session_state["rol"]
    else:
        return None



