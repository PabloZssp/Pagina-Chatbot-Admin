import streamlit as st
import pandas as pd
#import utilidades as util

st.set_page_config(page_title="pruebas str", initial_sidebar_state="collapsed")

def main():
     
     st.title("CHATBOT ADMIN")
     st.sidebar.header(" MENU PRINCIPAL")
     
     with st.sidebar:
            st.subheader("Opciones")
            st.button("Cargar datos")
            st.subheader("graficas")
            st.button("Gráfica de barras")
            st.button("Gráfica de líneas")
            st.button("Gráfica de dispersión")
            #Sst.page_link("Bases_Datos.py", label="Bases de Datos") 
     








 
    



if __name__ == "__main__":
    main()
