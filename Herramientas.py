import streamlit as st
import log as l

def st_normal():
    _, col, _ = st.columns([1, 2, 1])
    return col

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
[data-testid="stMain"] {

}

[data-testid="stVerticalBlock"]{
display: flex;
justify-content: center;
align-items: center;
flex-direction: column;
text-align:center;
padding-top:15px;
padding-bottom:10px;
}



[data-testid="stAppViewContainer"] {
background-color: #F8F9FA;
background-size: cover;
}

/* Solo los títulos del contenedor principal */
.stAppViewContainer h1,
.stAppViewContainer h2 {
color: #800020 !important;
text-align: center !important;
font-family: 'Segoe UI', sans-serif !important;
font-weight: 600 !important;
}

.stAppViewContainer h3{
color: grey important;
}

button {
padding: 1rem 2rem !important;
background-color: #8b233f !important;
}

button p{
font-weight:700 !important;
color: white !important;
font-size: 1.3rem !important;
transform: scale(1) !important;
}

button:hover{
box-shadow: 3px 5px 3px rgba(0, 0, 0, 0.2) !important;
transform: scale(0.9) !important;
transition: box-shadow 0.3s ease-in-out !important;
transition: all 500ms !important; 
}

[data-testid="stWidgetLabel"] {
color: #848889 !important;
}

[data-testid="stElementContainer"]{
text-align: center;

}

[data-testid="stHeader"] {
    background-color: rgba(188, 149, 92, 0.1);

}


[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #8b233f, #b34d66);
    //background-color: rgb( 114, 19, 34);
    background-size: cover;
    color: white !important;
}

[data-testid="stSidebar"] * {
    color: white !important;
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
