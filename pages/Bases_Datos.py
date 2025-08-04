import streamlit as st
import pandas as pd


def BasesDatos():
    st.set_page_config(page_title="Bases de Datos", initial_sidebar_state="collapsed")
    
    st.title("Bases de Datos")
    st.sidebar.header("Opciones")
    
    # Aquí puedes agregar más opciones en la barra lateral si es necesario
    st.sidebar.button("Cargar datos")
    
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



