
import streamlit as st
import pandas as pd
import Herramientas as h  # Módulo de herramientas para links de las páginas
import Conexion as cnx # Módulo para la conexion de bases de datos de pruebas
import conexion2 as cn # Módulo para la conexion de la base de datos principal 

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
            tabla = st.selectbox("", options=[" ","Eventos", "Actividades", "Cursos", "Talleres"], index=0)  # Nombre de la tabla
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
                cnx.Crear_registro(tabla,title_text,building_name_text,address_text,month_text,dates_text,hora_text,duracion_text,category_text,cost_text,url, description_text)
                st.success("Registro guardado exitosamente")
            except Exception as e:
                st.error(f" Error al guardar el registro: {e}")


        

            # Aquí puedes agregar el código para guardar el registro en la base de datos
           
#########################################################
####################Markdowns############################
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
        if st.button("Guardar "):
           st.success("Markdown Guardado")    
        




def selec_comp(Select):
    if Select == "eventos":
        eventos = cnx.obtener_eventos()

        if eventos:
            df_eventos = pd.DataFrame(eventos, columns=[
                "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
                "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
            ])
            st.subheader(" Registros guardados")
            st.dataframe(df_eventos)
            st.markdown(h.tabla_Format,unsafe_allow_html=True)
    
    elif Select == "actividades" :
        actividades =cnx.obtener_Actividades()

        if actividades:
            df_activ =pd.DataFrame(actividades,columns=[
                "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
                "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
            ])
            st.header("Registros Actividades Guardados")
            st.dataframe(df_activ)

    elif Select== "cursos":

        actividades =cnx.obtenerCursos()

        if actividades:
            df_activ =pd.DataFrame(actividades,columns=[
                "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
                "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
            ])
            st.header("Registros Actividades Guardados")
            st.dataframe(df_activ)

    elif Select == "talleres":
        actividades =cnx.obtener_Talleres()

        if actividades:
            df_activ =pd.DataFrame(actividades,columns=[
                "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
                "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
            ])
            st.header("Registros Actividades Guardados")
            st.dataframe(df_activ)


@st.dialog("Modificar")
def modificar(T_select):
    
    
    Opt_M =[" ","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    st.write("Selecciona el campo a modificar")
    
    ids = cnx.editar_campo(T_select)
    id_seleccionado = st.selectbox("Selecciona un ID", ids)
    
    # Aquí podrías cargar los datos del registro seleccionado
    registro = cnx.obtener_registro_id(id_seleccionado, T_select)
    c1,c2 = st.columns([5,5])
    if registro:
         with c1:
          Titulo = st.text_input("Titulo", value=registro[0])
          Recinto= st.text_input("Recinto", value=registro[1])
          Direccion = st.text_input("Direccion", value =registro[2])
          Mes = st.selectbox("Mes", options=Opt_M, index=Opt_M.index(registro[3]))
          Fechas= st.text_input("Fechas",value=registro[4] )
         
         with c2:
          Hora= st.text_input("Hora",value=registro[5])
          Duracion = st.text_input("Duracion", value=registro[6])
          Categoria = st.text_input("Categoria", value=registro[8])
          Costo= st.text_input("Costo",value=registro[9])
          Url= st.text_input("URL",value=registro[10])
          
         Descripcion = st.text_area("Descripción", height=300 ,  value=registro[7])
         G_b =st.button("Guardar cambios")
        
    if G_b:
            cnx.actualizar_registro(T_select,id_seleccionado, Titulo, Recinto, Direccion, Mes, Fechas, Hora, Duracion, Descripcion, Categoria, Costo, Url)
            st.success("Registro actualizado correctamente")
    
###########################################################################
############################### FUNCION LEER ##############################
###########################################################################     
#@st.dialog("Leer")
def leer(entrada):

    if entrada == "Base de datos":
       tablas_abacus=cn.obtener_tablas()
       T_a=st.selectbox("tabalas disponibles:", options=list(tablas_abacus.values()))
       Campos_abacus=cn.obtener_campos(T_a)
       st.selectbox("Campos disponibles",options= list(Campos_abacus.values()))

       
       st.subheader("Leer registros")
       diccionario_tablas = cnx.obtener_tablas()
       tablas = st.selectbox("Selecciona una tabla", options=list(diccionario_tablas.values()))
       selec_comp(tablas)
       edit_b = st.button("Editar")
       if edit_b:
            try:
                 modificar(tablas)
            except Exception as e:
                st.error(f"Ocurrió un error al editar el evento: {e}")
    
    
    
    elif entrada == "Markdown":
        st.subheader("Leer registros")


##########################################################################
##########################################################################
    
@st.dialog("Eliminar",width="large")
def eliminar(entrada):
    st.subheader("Eliminar un registro existente")
   

    if entrada == "Base de datos":
        
        diccionario_tablas = cnx.obtener_tablas()
        tablas = st.selectbox("Selecciona una tabla", options=list(diccionario_tablas.values()))
        
        if tablas == "eventos":   
             eventos = cnx.obtener_eventos()

             if eventos:
                 df_eventos = pd.DataFrame(eventos, columns=[
                     "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
                       "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
                   ])
                 st.subheader(" Registros guardados")
                 st.dataframe(df_eventos, use_container_width=True)
             st.write("Selecciona el campo a Eliminar")
             c1,c2 = st.columns([5,5])
             ids = cnx.editar_campo(tablas)
             with c1:
              id_seleccionado = st.selectbox("Selecciona un ID", ids) 
              registro=cnx.obtener_registro_id(id_seleccionado, tablas)
             with c2:
                
                st.text(f"Título: {registro[0]}")
                st.text(f"Recinto: {registro[1]}")
                st.text(f"Dirección: {registro[2]}")

            
             B_El = st.button(" Eliminar registro")

             if B_El:
                cnx.eliminar_registro(tablas,id_seleccionado)
                st.success(f"Se elimino el registro {registro[0]} exitosamente")
             
                     
###############################################
        elif tablas == "actividades":
             eventos = cnx.obtener_Actividades()

             if eventos:
                 df_actividades = pd.DataFrame(eventos, columns=[
                     "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
                       "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
                   ])
                 st.subheader(" Registros guardados")
                 st.dataframe(df_actividades, use_container_width=True)
             st.write("Selecciona el campo a Eliminar")
             c1,c2 = st.columns([5,5])
             ids = cnx.editar_campo(tablas)
             with c1:
              id_seleccionado = st.selectbox("Selecciona un ID", ids) 
              registro=cnx.obtener_registro_id(id_seleccionado, tablas)
             with c2:
                
                st.text(f"Título: {registro[0]}")
                st.text(f"Recinto: {registro[1]}")
                st.text(f"Dirección: {registro[2]}")

            
             B_El = st.button(" Eliminar registro")

             if B_El:
                cnx.eliminar_registro(tablas,id_seleccionado)
                st.success(f"Se elimino el registro {registro[0]} exitosamente")
###############################################
        elif tablas == "cursos":
             eventos = cnx.obtenerCursos()

             if eventos:
                 df_cursos = pd.DataFrame(eventos, columns=[
                     "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
                       "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
                   ])
                 st.subheader(" Registros guardados")
                 st.dataframe(df_cursos, use_container_width=True)
             st.write("Selecciona el campo a Eliminar")
             c1,c2 = st.columns([5,5])
             ids = cnx.editar_campo(tablas)
             with c1:
              id_seleccionado = st.selectbox("Selecciona un ID", ids) 
              registro=cnx.obtener_registro_id(id_seleccionado, tablas)
             with c2:
                
                st.text(f"Título: {registro[0]}")
                st.text(f"Recinto: {registro[1]}")
                st.text(f"Dirección: {registro[2]}")

            
             B_El = st.button(" Eliminar registro")

             if B_El:
                cnx.eliminar_registro(tablas,id_seleccionado)
                st.success(f"Se elimino el registro {registro[0]} exitosamente")
################################################
        elif tablas == "talleres":
             eventos = cnx.obtener_Talleres()
             if eventos:
                 df_talleres = pd.DataFrame(eventos, columns=[
                     "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
                       "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
                   ])
                 st.subheader(" Registros guardados")
                 st.dataframe(df_talleres, use_container_width=True)
             st.write("Selecciona el campo a Eliminar")
             c1,c2 = st.columns([5,5])
             ids = cnx.editar_campo(tablas)
             with c1:
              id_seleccionado = st.selectbox("Selecciona un ID", ids) 
              registro=cnx.obtener_registro_id(id_seleccionado, tablas)
             with c2:
                
                st.text(f"Título: {registro[0]}")
                st.text(f"Recinto: {registro[1]}")
                st.text(f"Dirección: {registro[2]}")
                
            
             B_El = st.button(" Eliminar registro")

             if B_El:
                cnx.eliminar_registro(tablas,id_seleccionado)
                st.success(f"Se elimino el registro {registro[0]} exitosamente")
        

    if entrada == "Markdown":
       tablas= st.selectbox("Selecciona el Markdown", options= ["", "mRK1","Mrk2"], index = 0)


BasesDatos()


