import streamlit as st
import pandas as pd
import Herramientas as h  # Módulo de herramientas para links de las páginas


def BasesDatos():
    
    h.MenuPrincipal()
    st.set_page_config(page_title="Formularios", initial_sidebar_state="auto",page_icon="💬")
    
    st.title("Formularios")
    st.sidebar.header("MENU")
    
    # Aquí puedes agregar más opciones en la barra lateral si es necesario
    st.sidebar.button("Base de datos")
    st.sidebar.button("Markdown")

    Menu = ["","Base de datos", "Markdown"]
    
    

    eleccion=st.selectbox("Selecciona una opción",options=Menu, index=0)

    #A partir de aqui vamos a poner la mayoria de las opciones que tendra la pagina
    #como los botones para los formularios ya sea para los markdowns o para una base de datos
    #nueva dejo 2 opciones de donde colocar los botones y ya dependiendo de como nos guste mas
    #lo dejamos asi en la pagina para la version final

    if eleccion == "Base de datos":
         
        opciones(eleccion)  # Llama a la función opciones para mostrar las opciones de crear, modificar, leer y eliminar registros
       
    if eleccion == "Markdown":
        
        opciones(eleccion)

    
    st.markdown(h.page_bg_img, unsafe_allow_html=True)
    
# Esta la usaremos para modificar las opciones de los formularios
def opciones(entrada):
    Menu_Sec = ["","Crear", "Modificar", "Leer", "Eliminar"]
    st.subheader(f"Formulario {entrada}")
    opcion = st.selectbox("Selecciona una opción", options=Menu_Sec, index=0)

    if opcion == "Crear":
        crear()
    elif opcion == "Modificar":
        modificar()
    elif opcion == "Leer":
        leer()
    elif opcion == "Eliminar":
        eliminar()


def crear():
    st.subheader("Crear un nuevo registro")
    # Aquí puedes agregar el formulario para crear un nuevo registro
    
def modificar():
    st.subheader("Modificar un registro existente")
    # Aquí puedes agregar el formulario para modificar un registro existente

def leer():
    st.subheader("Leer registros")
    # Aquí puedes agregar el código para leer registros de la base de datos 

def eliminar():
    st.subheader("Eliminar un registro existente")
    # Aquí puedes agregar el formulario para eliminar un registro existente




BasesDatos()
