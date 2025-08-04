import streamlit as st
import pandas as pd
import Herramientas as h  # Módulo de herramientas para links de las páginas


def BasesDatos():
    
    h.MenuPrincipal()
    st.set_page_config(page_title="Bases de Datos", initial_sidebar_state="auto")
    
    st.title("Bases de Datos")
    st.sidebar.header("Opciones")
    
    # Aquí puedes agregar más opciones en la barra lateral si es necesario
    st.button("")
    st.sidebar.button("Guardar datos")
    st.sidebar.button("Actualizar datos")
    
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

if __name__ == "__main__":
    BasesDatos()
    st.sidebar.button("Salir")