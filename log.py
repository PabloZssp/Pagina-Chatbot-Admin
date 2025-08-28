import streamlit as st
import json as j  # Asegúrate de importar json correctamente

def log_in():
    st.set_page_config(page_title="Iniciar sesión", page_icon="🌎")

    
    if "usuario" in st.session_state:
        st.success(f"Bienvenido, {st.session_state['usuario']} ")

    with open("usuarios.json", "r") as f:
        usuarios = j.load(f)

    st.title("Iniciar sesión")

    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if usuario in usuarios and usuarios[usuario]["password"] == password:
            st.session_state["usuario"] = usuario
            st.session_state["rol"] = usuarios[usuario]["rol"]
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



