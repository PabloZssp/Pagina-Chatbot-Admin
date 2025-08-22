import streamlit as st
from configparser import ConfigParser as cp
from sqlmodel import create_engine


def st_normal():
    _, col, _ = st.columns([1, 2, 1])
    return col

def MenuPrincipal():
    
    with st.sidebar:
         st.page_link("Pagina_Principal.py",label="Pagina Principal",icon="🤖")
         st.page_link("pages/Formularios.py",label="Componetes",icon="📝")
         st.page_link("pages/Chatbot.py",label="Graficas",icon="📊")
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
[data-testid="stAppViewContainer"] {
    background-color: #F8F9FA;
    background-size: cover;
}

[data-testid="stMainBlockContainer"]{
padding: 3rem 1rem 3rem;

}

[data-testid="stElementContainer"]{
text-align: center;

}

[data-testid="stHeader"] {
    background-color: #8b233f;

}


[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #8b233f, #b34d66);
    //background-color: rgb( 114, 19, 34);
    background-size: cover;
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
