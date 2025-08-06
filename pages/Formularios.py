import streamlit as st
import pandas as pd
import Herramientas as h  # Módulo de herramientas para links de las páginas


def BasesDatos():
    
    h.MenuPrincipal()
    st.set_page_config(page_title="Componetes", initial_sidebar_state="auto",page_icon="💬")
    
    st.title("Componetes")    
 
    
    # Aquí puedes agregar más opciones en la barra lateral si es necesario


    Menu = ["Base de datos", "Markdown"]
    
    

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
    Menu_Sec = ["Leer", "Modificar","Crear" , "Eliminar"]
    st.subheader(f"Formulario {entrada}")
    opcion = st.selectbox("Selecciona una opción", options=Menu_Sec, index=0)

    if opcion == "Crear":
        crear(entrada)
    elif opcion == "Modificar":
        modificar(entrada)
    elif opcion == "Leer":
        leer(entrada)
    elif opcion == "Eliminar":
        eliminar(entrada)


def crear(entrada):

    Opt_M =[" ","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    st.subheader("Crear un nuevo registro")
    col1, col2, col3, col4 = st.columns(4)
    if entrada == "Base de datos":
        
       
        with col1:
            st.subheader("**Tabla:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Titulo:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Recinto:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Dirección:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Mes:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Fechas:**")
            st.markdown("<br>", unsafe_allow_html=True)
                        
           

        with col2:
            st.selectbox("", options=[" ","Eventos", "Actividades", "Cursos", "Talleres"], index=0)  # Nombre de la tabla
            title_text = st.text_input(" ")
            building_name_text = st.text_input("   ")
            address_text = st.text_input("    ")
            month_text = st.selectbox("", options=Opt_M, index=0)       
            dates_text = st.text_input("      ", placeholder="YYYY/MM/DD ")
            

        with col3:
            st.subheader("**Hora:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Duración:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Categoría:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Costo:**") 
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**URL:**")
    
        with col4:
            hora_text = st.text_input("         ")
            duracion_text = st.text_input("                 ")
            category_text = st.text_input("          ")
            cost_text = st.text_input("              ")
            url = st.text_input("            ")


        st.subheader("**Descripción:**")
        description_text = st.text_area(" ", height=300, placeholder="Escribe aquí la descripción del evento o actividad...")
       # st.button(on_click="Guardar", label="Guardar registro", type="primary")

#########################################################
    if entrada == "Markdown":
        with col1:
            
            st.subheader("**Titulo:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Recinto:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Dirección:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Mes:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Fechas:**")
            st.markdown("<br>", unsafe_allow_html=True)  

        with col2:
            title = st.text_input(" ")
            building_name = st.text_input("   ")
            address = st.text_input("    ")
            month = st.selectbox("", options=Opt_M, index=0)       
            dates = st.text_input("      ", placeholder="YYYY/MM/DD ")
            

        with col3:
            st.subheader("**Hora:**")
            st.markdown("<br>", unsafe_allow_html=True)
            
            st.subheader("**Categoría:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Costo:**") 
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**URL:**")
    
        with col4:
            hour = st.text_input("         ")
            category = st.text_input("          ")
            cost = st.text_input("              ")
            url = st.text_input("            ")


        st.subheader("**Descripción:**")
        description = st.text_area(" ", height=300, placeholder="Escribe aquí la descripción del evento o actividad...")
       # st.button(on_click="Guardar", label="Guardar registro", type="primary")
        
def modificar(entrada):
    st.subheader("Modificar un registro existente")
    # Aquí puedes agregar el formulario para modificar un registro existente

def leer(entrdada):
    st.subheader("Leer registros")
    # Aquí puedes agregar el código para leer registros de la base de datos 

def eliminar(entrada):
    st.subheader("Eliminar un registro existente")
    # Aquí puedes agregar el formulario para eliminar un registro existente




BasesDatos()
