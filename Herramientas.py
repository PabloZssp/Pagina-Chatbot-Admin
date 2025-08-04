import streamlit as st

def MenuPrincipal():
    
    with st.sidebar:
         st.page_link("Pagina_Principal.py",label="Pagina Principal",icon="🤖")
         st.page_link("pages/Bases_Datos.py",label="Formularios",icon="📊")
         st.page_link("pages/Chatbot.py",label="Graficas",icon="💬")


