import streamlit as st
import conexion2 as cn
from cryptography.hazmat.primitives import serialization


def log_in():
    st.set_page_config(page_title="Iniciar sesión", page_icon="🌎")
    st.title("Iniciar sesión")
    
    usuario = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    clave_privada = st.file_uploader("Sube tu clave privada SSH")
    clave_pass = st.text_input("Contraseña de la clave privada (si tiene)", type="password")
    boton_habilitado = bool(usuario and password and clave_privada)

    if st.button("Iniciar sesión", disabled=not boton_habilitado):
        with st.spinner("Verificando credenciales y claves..."):
            user = cn.validar_usuario(usuario, password)
            if user:
                public_key_pem = cn.obtener_llave_publica(usuario)
                private_key_bytes = clave_privada.read()
                password_bytes = clave_pass.encode() if clave_pass else None

                if validar_llaves(private_key_bytes, public_key_pem, password_bytes):
                    tunnel = cn.crear_tunel(private_key_bytes, clave_pass if clave_pass else None)
                    st.session_state["tunnel"] = tunnel
                    st.session_state["usuario"] = user[0]
                    st.session_state["rol"] = user[1]
                    st.success("¡Inicio de sesión exitoso!")
                    st.switch_page("pages/Pagina_Principal.py")
                    st.rerun()
                else:
                    st.error("Error en la validación. Verifica tu llave privada.")
            else:
                st.error("Usuario o contraseña incorrectos")

def log_out():
    
    if "tunnel" in st.session_state:
        st.session_state["tunnel"].stop()
        del st.session_state["tunnel"]

    for key in ["usuario", "rol"]:
        if key in st.session_state:
            del st.session_state[key]

    st.switch_page("inicio.py")

def obtener_rol_actual():
    if "rol" in st.session_state:
        return st.session_state["rol"]
    else:
        return None


def validar_llaves(privada_bytes, publica_bytes, password_bytes=None):
    private_key = serialization.load_ssh_private_key(privada_bytes, password=password_bytes)
    public_key = serialization.load_ssh_public_key(publica_bytes)
    mensaje = b"inicio de secion comprobado"
    firma = private_key.sign(mensaje)
    try:
        public_key.verify(firma, mensaje)
        return True
    except Exception:
        return False