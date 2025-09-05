import streamlit as st
from configparser import ConfigParser as cp
from sqlmodel import create_engine
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
    
        st.image(imagen, width=140)
        st.image(imagen2, width=200)
        st.write("")
        st.write("")
        st.page_link("Pagina_Principal.py",label=" Página Principal",icon="🤖")
        st.page_link("pages/Formularios.py",label=" Componentes",icon="📝")
        st.page_link("pages/Chatbot.py",label=" Gráficas",icon="📊")
        st.page_link("pages/MENU_BD.py",label= "TEST")

# Ejemplo de como aaceder  a las variables de la configuracion  de la conexion a la base de datos
# en este caso se usara para crear la conexion a la base de datos
#Server= st.secrets["BasesDatos"]["Host"] 
#DataBase= st.secrets["BasesDatos"]["nombre_bd"]
#User= st.secrets["BasesDatos"]["Usuario"]
#Password= st.secrets["BasesDatos"]["password"]
#Port= st.secrets["BasesDatos"]["puerto"]


##Estes es es fondo de pantalla de la pagina la imagen es de prueba se puede cambiar por cualquier otra imagen
##Esta dividida en 2 partes una para el fondo de la pagina y otra para el fondo de la barra lateral
##
##para cambiar la imagen solo hay que cambiar la url de la imagen en el string

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
background-color: #9c2c4a !important;
}

/* FIN BOTONES */


</style>
"""