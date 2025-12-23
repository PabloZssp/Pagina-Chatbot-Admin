import streamlit as st
from configparser import ConfigParser as cp
from sqlmodel import create_engine
import log as l
from PIL import Image


#esto crea 3 columnas, dejando el contenido centrado
def st_normal():
    _, col, _ = st.columns([1, 2, 1])
    return col

def st_modal():
    _, col, _ = st.columns([1,3,1])
    return col

imagen = Image.open("logos2025/LogoCDMX.png")
imagen2 = Image.open("logos2025/LogoADIP.png")

def MenuPrincipal():
    
    with st.sidebar:
        if st.session_state["rol"] == "administrador":
            st.image(imagen, width=140)
            st.image(imagen2, width=200)
            st.write("")
            st.write("")
            st.page_link("pages/Pagina_Principal.py",label=" Página Principal",icon="🏠")
            st.page_link("pages/Formularios.py",label=" Componentes",icon="📝")
            st.page_link("pages/Chatbot.py",label=" Gráficas",icon="📊")
            st.page_link("pages/MENU_BD.py",label= "TEST")

        elif st.session_state["rol"] in ["usuario", "usuarioUX", "usuarioCl", "usuarioTU"]:
            st.page_link("pages/Pagina_Principal.py",label="Pagina Principal",icon="🏠")
            st.page_link("pages/Formularios.py", label="Componentes", icon="📝")
            #st.page_link("pages/MENU_BD.py", label="TEST")
            #st.page_link("pages/Chatbot.py", label="Gráficas", icon="📊")
            #st.page_link("pages/log.py", label="login")
        else:
            st.page_link("pages/Pagina_Principal.py",label="Pagina Principal",icon="🏠")
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




page_bg_img = """

<style>
/* SELECT BOX SECTION */

/* Cambia el color de fondo de todos los selectbox en lightmode*/
.stSelectbox > div[data-baseweb="select"] > div{
background-color:#faf7f7 !important;
border-radius: 5px;
color: black;
}

/*color del dropdown del selectbox */
.st-cy, .st-dn{
background-color:#f5f2f2 !important;
}

/*color del texto dentro del dropdown*/
.st-b6, .st-dj{
color:#121112;
}

/*color del selectbox en modo oscuro*/
.st-b7, .st-b8, .st-b9, .st-ba, .st-dp, .st-do, .st-dn, .st-dm {
border-color: #bcbcbc;
}

/*color de bordes de selectbox active*/
.st-cv, .st-cu, .st-ct, .st-cs{
border-color: #bcbcbc;
}

/* Aplica estilo solo al label*/
.stSelectbox label p, .stTextInput label p, .stTextArea label p {
    color: #8b233f !important;
    font-size: 1rem;  
    font-weight: 500;   
}


/* clase para título de los selectbox*/
.hd-formulario {
    color: #8b233f;
    font-weight: 400;
}

/* FIN SELECT BOX SECTION */

/* INICIO MODALES */

/* clase para título de los modales*/
.hd-modal {
    color: #8b233f;
    font-weight: 400;
    font-size:20px;
}

/* FIN MODALES */

/* CONTENIDO CENTRAL EN EL BLOCK */

[data-testid="stVerticalBlock"]{
display: flex;
justify-content: center;
align-items: center;
flex-direction: column;
text-align:center;
padding-top:3px;
padding-bottom:3px;
}

[data-testid="stAppViewContainer"] {
    position: relative; 
    background-color: #f2f0f0;
    overflow: hidden;
}

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url("https://previews.123rf.com/images/sunspire/sunspire1610/sunspire161000053/63825371-abstract-geometric-black-and-white-hipster-fashion-polygon-background-pattern.jpg");
    background-size: contain;
    background-position: center;
    opacity: 0.03;
}

/* Solo los títulos del contenedor principal */
.stAppViewContainer h1,
.stAppViewContainer h2 {
color: #800020 !important;
display: flex;
flex-direction: column !important;
justify-content: center;
align-items:center;
font-family: 'Segoe UI', sans-serif !important;
font-weight: 600 !important;
}

.stAppViewContainer h3{
color: #3c3c3c !important;

}

[data-testid="stElementContainer"] {
text-align: center;
}

[data-testid="stHeader"] {
background-color: rgba(107, 27, 59);
color: white;
}


img {
border-radius: 0px !important;
}

#chat-bot-admin{
padding:3px;
}
/* FIN CONTENIDO CENTRAL EN EL BLOCK */


/* CONTENIDO SIDEBAR */

/* icono de la sidebar minimizada*/
[data-testid="stExpandSidebarButton"] span{
color:white;
}

[data-testid="stSidebar"] {
    
    background-color: rgba(203, 175, 133, 0.7);
    background-size: cover;
}

[data-testid="stSidebar"] * {
    color: rgba(107, 27, 59) !important;
}


/* FIN CONTENIDO SIDEBAR */


/* BOTONES */

button {
# padding: 0.5rem 1rem !important;
background-color: #8b233f !important;
color:white !important;
}

button p{
font-weight:700 !important;
color: white !important;
font-size: 1.1rem !important;
}

button:hover{
transform: scale(0.9) !important;
transition: all 500ms !important; 
}

[data-testid="stWidgetLabel"] {
color: #848889 !important;
}

[data-testid="stElementContainer"]{
text-align: center;

}

[data-testid="stHeader"] {
    background-color: rgba(188, 149, 92, 0.2);

}


[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #2e2e2e, #b34d66);
    //background-color: rgb( 114, 19, 34);
    background-size: cover;
    color: white !important;
background-color: #9c2c4a !important;
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