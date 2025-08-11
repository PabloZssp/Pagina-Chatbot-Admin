import streamlit as st
import pandas as pd
import Herramientas as h  # Módulo de herramientas para links de las páginas
import sqlmodel as sql
import BD2   # Importa el módulo BD.py para acceder a las clases de eventos
import Conexion as cnx






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

def crear_tabla_eventos():
    conn = cnx.get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Eventos (
            id SERIAL PRIMARY KEY,
            titulo TEXT,
            recinto TEXT,
            direccion TEXT,
            mes TEXT,
            fechas TEXT,
            hora TEXT,
            duracion TEXT,
            categoria TEXT,
            costo TEXT,
            url TEXT,
            descripcion TEXT
        )
    """)
    conn.commit()
    cur.close()    


# Esta la usaremos para modificar las opciones de los formularios
def opciones(entrada):
    Menu_Sec = ["Leer","Crear" , "Eliminar"]
    st.subheader(f"Formulario {entrada}")
    opcion = st.selectbox("Selecciona una opción", options=Menu_Sec, index=0)

    if opcion == "Crear":
        crear(entrada)
    elif opcion == "Leer":
        leer(entrada)
        
    elif opcion == "Eliminar":
        eliminar(entrada)

@st.dialog("Crear",width="large")
def crear(entrada):

    Opt_M =[" ","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    crear_tabla_eventos()

    st.subheader("Crear un nuevo registro")
    col1, col2, col3, col4 = st.columns([2,3,2,3])
    if entrada == "Base de datos":
        st.dialog("inserte los campos")
        with col1:
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Tabla:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Titulo:**")
            st.markdown("<br>", unsafe_allow_html=True)
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
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Hora:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Duración:**")
            st.markdown("<br>", unsafe_allow_html=True)
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
        
        if st.button("Guardar registro"):
            try:
                conn = cnx.get_connection()
                cur = conn.cursor()
                cur.execute("""
                    INSERT INTO Eventos (
                        titulo, recinto, direccion, mes, fechas, hora, duracion, categoria, costo, url, descripcion
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (
                    title_text, building_name_text, address_text, month_text, dates_text,
                    hora_text, duracion_text, category_text, cost_text, url, description_text
                ))
                conn.commit()
                cur.close()
                st.success("Registro guardado exitosamente")
            except Exception as e:
                st.error(f" Error al guardar el registro: {e}")


        

            # Aquí puedes agregar el código para guardar el registro en la base de datos
           


#########################################################
    if entrada == "Markdown":
        with col1:
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Titulo:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Recinto:**")
            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("**Dirección:**")
            st.markdown("<br>", unsafe_allow_html=True)
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
            st.markdown("<br>", unsafe_allow_html=True) 
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



def selec_comp(Select):
    if Select == "Eventos":
        eventos = cnx.obtener_eventos()

        if eventos:
            df_eventos = pd.DataFrame(eventos, columns=[
                "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
                "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
            ])
            st.subheader(" Registros guardados")
            st.dataframe(df_eventos)
            st.markdown(h.tabla_Format,unsafe_allow_html=True)



    if Select == "Actividades" :
        actividades = {
            "Título": ["Yoga al aire libre", "Caminata ecológica"],
            "Recinto": ["Parque México", "Bosque de Chapultepec"],
            "Dirección": ["Av. México s/n", "Av. Chapultepec 200"],
            "Mes": ["Agosto", "Agosto"],
            "Fechas": ["15 Ago", "22 Ago"],
            "Hora": ["08:00", "09:00"],
            "Duración": ["1 hora", "2 horas"],
            "Categorías": ["Salud", "Medio ambiente"],
            "Costo": ["Gratis", "Gratis"],
            "URL": ["https://ejemplo.com/yoga", "https://ejemplo.com/caminata"]
        }
        df_actividades = pd.DataFrame(actividades)
        # Mostrar tabla
        st.table(df_actividades)
        st.markdown(h.tabla_Format,unsafe_allow_html=True)
    if Select== "Cursos":

        cursos = {
        "Título": ["Curso de Fotografía", "Curso de Programación"],
            "Recinto": ["Casa de Cultura", "Centro Digital"],
            "Dirección": ["Calle Arte 22", "Av. Tecnología 101"],
            "Mes": ["Septiembre", "Octubre"],
            "Fechas": ["1-15 Sep", "5-30 Oct"],
            "Hora": ["17:00", "18:00"],
            "Duración": ["2 semanas", "1 mes"],
            "Categorías": ["Arte", "Tecnología"],
            "Costo": ["$500", "$800"],
            "URL": ["https://ejemplo.com/foto", "https://ejemplo.com/programacion"]
        }

        df_cursos = pd.DataFrame(cursos)
        # Mostrar tabla
        st.table(df_cursos)
        st.markdown(h.tabla_Format,unsafe_allow_html=True)
    if Select == "Talleres":
        talleres = {
            "Título": ["Taller de Cerámica", "Taller de Escritura Creativa"],
            "Recinto": ["Centro Artesanal", "Biblioteca Central"],
            "Dirección": ["Av. Creativa 88", "Calle Letras 33"],
            "Mes": ["Octubre", "Noviembre"],
            "Fechas": ["3-7 Oct", "10-14 Nov"],
            "Hora": ["15:00", "16:00"],
            "Duración": ["5 días", "5 días"],
            "Categorías": ["Manualidades", "Literatura"],
            "Costo": ["$300", "Entrada libre"],
            "URL": ["https://ejemplo.com/ceramica", "https://ejemplo.com/escritura"]
        }

        df_talleres = pd.DataFrame(talleres)
        # Mostrar tabla
        st.table(df_talleres)
        st.markdown(h.tabla_Format,unsafe_allow_html=True)

    
        
#@st.dialog("Leer")
def leer(entrdada):
    st.subheader("Leer registros")
    Menu_tabla = ["Eventos", "Actividades", "Cursos", "Talleres"]
    elec = st.selectbox(" Componente a ver: " ,options=Menu_tabla, index=0 )
    selec_comp(elec)
    edit_b = st.button("Editar")
    if edit_b:
        try:
         cnx.editar_campo(elec)
        except Exception as e:
            st.error(f"Ocurrió un error al eliminar el evento: {e}")


    
@st.dialog("Eliminar",width="large")
def eliminar(entrada):
    st.subheader("Eliminar un registro existente")
     
    Menu_Elim = [" ","Campo 1", "Campo 2", "Campo 3"]
    Menu_tabla = [" ","Eventos", "Actividades", "Cursos", "Talleres"]

    if entrada == "Base de datos":

        opcion_elim = st.selectbox("Selecciona Tabla", options=Menu_tabla, index=0)
        
        if opcion_elim == "Eventos":   
             opcion_elim_campo= st.selectbox("Selecciona Campo", options=Menu_Elim, index=0)
             Elim_BE = st.button("Eliminar registro", type="primary",key="Eliminar Eventos")
             if Elim_BE:
              st.success(f"Registro eliminado de la tabla {opcion_elim} en el campo {opcion_elim_campo}")        

        elif opcion_elim == "Actividades":
             opcion_elim_campo= st.selectbox("Selecciona Campo", options=Menu_Elim, index=0)       
             Elim_BA = st.button("Eliminar registro", type="primary", key= "Eliminar actividades")
             if Elim_BA:
                st.success(f"Registro eliminado de la tabla {opcion_elim} en el campo {opcion_elim_campo}")

        elif opcion_elim == "Cursos":
             opcion_elim_campo= st.selectbox("Selecciona Campo", options=Menu_Elim, index=0)                    
             Elim_BC = st.button("Eliminar registro", type="primary", key = "Eliminar Cursos")
             if Elim_BC:
                st.success(f"Registro eliminado de la tabla {opcion_elim} en el campo {opcion_elim_campo}")

        elif opcion_elim == "Talleres":
            opcion_elim_campo= st.selectbox("Selecciona Campo", options=Menu_Elim, index=0)
                    
            Elim_BT = st.button("Eliminar registro", type="primary", key = "Eliminar Talleres")

            if Elim_BT:
                st.success(f"Registro eliminado de la tabla {opcion_elim} en el campo {opcion_elim_campo}")


        

    if entrada == "Markdown":
        opcion_elim= st.selectbox("Selecciona el Markdown", options= Menu_Elim, index = 0)


BasesDatos()
