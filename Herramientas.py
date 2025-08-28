import streamlit as st
import log as l

def MenuPrincipal():
    
    with st.sidebar:
         if st.session_state["rol"] == "administrador":
            st.page_link("pages/Pagina_Principal.py",label="Pagina Principal",icon="🤖")
            st.page_link("pages/Formularios.py", label="Componentes", icon="📝")
            st.page_link("pages/Chatbot.py", label="Gráficas", icon="📊")
            st.page_link("pages/MENU_BD.py", label="TEST")

         elif st.session_state["rol"] in ["usuario", "usuarioUX", "usuarioCl", "usuarioTU"]:
            st.page_link("pages/Pagina_Principal.py",label="Pagina Principal",icon="🤖")
            st.page_link("pages/Formularios.py", label="Componentes", icon="📝")
            #st.page_link("pages/MENU_BD.py", label="TEST")
           #st.page_link("pages/Chatbot.py", label="Gráficas", icon="📊")
            #st.page_link("pages/log.py", label="login")
         else:
            st.page_link("pages/Pagina_Principal.py",label="Pagina Principal",icon="🤖")
         Ex_b = st.button("Salir")
         if Ex_b:
              l.log_out()


def verificar_sesion():
    if "usuario" not in st.session_state or st.session_state["usuario"] is None:
        st.error("Debes iniciar sesión para acceder a esta página.")
        if st.button("**Iniciar sesión**"):
            st.switch_page("inicio.py")

        st.stop()
        
    
def acceso_multiple(roles_permitidos):
    if "rol" not in st.session_state or st.session_state["rol"] not in roles_permitidos:
        st.warning(" No tienes permiso para acceder")
        st.stop()

##Estes es es fondo de pantalla de la pagina la imagen es de prueba se puede cambiar por cualquier otra imagen
##Esta dividida en 2 partes una para el fondo de la pagina y otra para el fondo de la barra lateral
##

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: rgba(159, 34, 65, 0.5);
    background-size: cover;
}



[data-testid="stHeader"] {
    background-color: rgba(188, 149, 92, 0.1);

}


[data-testid="stSidebar"] {
    background-color: rgba(44, 45, 50);
    background-size: cover;
}
</style>
"""

tabla_Format= """
<style>
table {
        width: 100%;
        border-collapse: collapse;
    }
    th {
        background-color: #000000;
        color: white;
        padding: 8px;
        border: 1px solid #444;
    }
    td {
        background-color: #111111;
        color: white;
        padding: 8px;
        border: 1px solid #444;
    }
    tr:nth-child(even) td {
        background-color: #222222;
    }
    a {
        color: #1E90FF;
    }

</style>
"""