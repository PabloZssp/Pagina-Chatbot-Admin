import streamlit as st
import pandas as pd
import Herramientas as h  # Módulo de herramientas para links de las páginas


def BasesDatos():
    
    h.MenuPrincipal()
    st.set_page_config(page_title="Formularios", initial_sidebar_state="auto",page_icon="💬")
    
    st.title("Formularios")
    st.sidebar.header("MENU")
    
    # Aquí puedes agregar más opciones en la barra lateral si es necesario
    st.button("Markdown")
    st.button("Base de datos")
    st.sidebar.button("Base de datos")
    st.sidebar.button("Markdown")


    Menu = ["Base de datos", "Markdown"]
    eleccion=st.selectbox("Selecciona una opción",options=Menu)

    if eleccion == "Base de datos":
        subtitle = "Base de datos"
    elif eleccion == "Markdown":
        subtitle = "Markdown"


    #A partir de aqui vamos a poner la mayoria de las opciones que tendra la pagina
    #como los botones para los formularios ya sea para los markdowns o para una base de datos
    #nueva dejo 2 opciones de donde colocar los botones y ya dependiendo de como nos guste mas
    #lo dejamos asi en la pagina para la version final
    
    



    # Crear un DataFrame de ejemplo
    data = {
        'Dato a': [1, 2, 3, 4, 5],
        'Dato b': [5, 6, 7, 8, 9],
        'Dato c': [9, 10, 11, 12, 13]
    }
    df = pd.DataFrame(data)
    
    # Mostrar el DataFrame
    st.write("Aquí hay un DataFrame de ejemplo:")
    st.dataframe(df)
    st.markdown(h.page_bg_img, unsafe_allow_html=True)

BasesDatos()
