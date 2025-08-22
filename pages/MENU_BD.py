import streamlit as st
import pandas as pd
import Herramientas as h  # Módulo de herramientas para links de las páginas
import Conexion as cnx # Módulo para la conexion de bases de datos de pruebas
import conexion2 as cn


def menu_BD():
    h.MenuPrincipal()
    st.set_page_config(page_title="Componetes", initial_sidebar_state="auto",page_icon="💬")
    st.markdown(h.page_bg_img, unsafe_allow_html=True)
    st.title("Bases de datos")
    
    Menu =[" ","eventos_cartelera","informacion_ux","chatbot_turismo","test"]
    
    Bdatos=st.selectbox("Selecciona una Base de datos:",options=Menu)


    if Bdatos == "informacion_ux":
        
        opciones2(Bdatos)

    elif Bdatos == "eventos_cartelera":
             
        opciones2(Bdatos)

    elif Bdatos == "chatbot_turismo":        
        
        opciones2(Bdatos)

    elif Bdatos == "test":        
        opciones2(Bdatos)

        
    
def opciones(tabla,campos,Bdatos):

    Menu_Sec = ["Leer","Crear" ,"Eliminar"]
    st.subheader("Formulario")
    opcion = st.selectbox("Selecciona una opción", options=Menu_Sec, index=0)

    if opcion == "Crear":
        crear(tabla, campos,Bdatos)
    elif opcion == "Leer":
        leer(Bdatos)     
    elif opcion == "Eliminar":
        eliminar(tabla)




@st.dialog("Crear", width="large")
def crear(tabla, campos,baseD):
    Opt_M = [" ", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
   
    col1, col2 = st.columns(2)    
    valores = {}

    indice = 0  
    
    for  campo in campos:
        if campo.lower() == "id":
            continue
        with col1 if indice % 2 == 0 else col2:
            if "fecha" in campo.lower():
                valores[campo] = st.date_input(f"**{campo}:**")
            elif "dates" in campo.lower():
                valores[campo] =st.date_input(f"{campo}:")
            elif "mes" in campo.lower():
                valores[campo] = st.selectbox(f"{campo}:", options=Opt_M)
            elif "descripcion"  in campo.lower():
                valores[campo] =st.text_area(f"{campo}:",height=100,placeholder="Escribe aqui tu descrpcion:")
            else:
                valores[campo] = st.text_input(f"{campo}:")
        indice +=1

    if st.button("Guardar registro", key="guardar_registro"):
        try:
            cn.crear_registro(tabla, valores)
            st.success("Registro guardado exitosamente")
        except Exception as e:
            st.error(f"Error al guardar el registro: {e}")



def selec_comp(tabla):
    columnas = cn.obtener_campos(tabla)         # obtiene los nombres de las columnas
    registros = cn.obtener_eventos(tabla)        # obtiene los datos de la tabla
    df_compn = pd.DataFrame(registros, columns=columnas)
    st.subheader("Registros")
    st.dataframe(df_compn)


def leer(basedatos):
       st.subheader(f"Leer registros de: {basedatos} ")
       diccionario_tablas = cn.obtener_tablas()
       tablas = st.selectbox("Selecciona una tabla", options=list(diccionario_tablas.values()))
       selec_comp(tablas)
       edit_b = st.button("Editar")
       if edit_b:
            try:
                 modificar(tablas)
            except Exception as e:
                st.error(f"Ocurrió un error al editar el evento: {e}")

@st.dialog("Modificar",width="large")
def modificar(t_elec):
    Opt_M =[" ","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    campos =cn.obtener_campos(t_elec)

    st.write("Selecciona el campo a modificar")
    ids = cn.editar_campo(t_elec)
    id_seleccionado = st.selectbox("Selecciona un ID", ids)
    registro= cn.obtener_registro_id(id_seleccionado,t_elec,campos)
    
    col1, col2 = st.columns(2)

    
    valores = {}

    valor_idx = 0

    for campo in campos:
        

        with col1 if valor_idx % 2 == 0 else col2:
            valor_actual = registro[valor_idx]

            if "fecha" in campo.lower() or "dates" in campo.lower():
                valores[campo] = st.date_input(f"{campo}:", value=None)
            elif "mes" in campo.lower():
                valores[campo] = st.selectbox(f"{campo}:", options=Opt_M, index=Opt_M.index(valor_actual) if valor_actual in Opt_M else 0)
            elif "descripcion" in campo.lower():
                valores[campo] = st.text_area(f"{campo}:", value=valor_actual, height=100, placeholder="Escribe aquí tu descripción:")
            elif "respuesta" in campo.lower():
                valores[campo]= st.text_area( f"{campo}:", value=valor_actual, height=100)
            elif "pregunta" in campo.lower():
                valores[campo]= st.text_area( f"{campo}:", value=valor_actual, height=100)
            else:
                valores[campo] = st.text_input(f"{campo}:", value=valor_actual)

        valor_idx += 1
    G_b= st.button("Guardar cambios")
    if G_b:
        cn.actualizar_registro(t_elec,id_seleccionado,valores)
        st.success("Registro actualizado correctamente")



@st.dialog("Eliminar",width="large")    
def eliminar(entrada):
     st.subheader("Eliminar un registro existente")
     D_tab= cn.obtener_tablas()
     t_selec = st.selectbox("Elige una tabla", options= list(D_tab.values()))
     selec_comp(t_selec)
     c1,c2 = st.columns([5,5])
     ids = cn.editar_campo(t_selec)
     campos= cn.obtener_campos(t_selec)
     with c1:
         id_seleccionado = st.selectbox("Selecciona un ID", ids) 
         registro=cn.obtener_registro_id(id_seleccionado, t_selec,campos)
     with c2:
         st.text(f"tabla seleccionada:{t_selec}")
         st.text(f"id seleccionado:{id_seleccionado}")
         st.text(f"Titulo: {registro[1]}")
         st.text(f"Pregunta:{registro[3]}")
         st.text(f"Respuesta{registro[4]}")
     b_El = st.button("Eliminar registro")
     if b_El:
         cn.eliminar_campo(t_selec,id_seleccionado)
         st.success("Registro eliminado exitosamente.")


###################################################
##################TEST#############################
###################################################
def opciones2(Bdatos):

    Menu_Sec = ["Leer","Crear" ,"Eliminar"]
    st.subheader("Formulario")
    opcion = st.selectbox("Selecciona una opción", options=Menu_Sec, index=0)

    if opcion == "Crear":
        crear2(Bdatos)
    elif opcion == "Leer":
        leer2(Bdatos)     
    elif opcion == "Eliminar":
        eliminar2(Bdatos)

@st.dialog("Crear", width="large")
def crear2(baseD):
    Opt_M = [" ", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    if baseD=="test":
         tabla = cnx.obtener_tablas()
         slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
         campos =cnx.obtener_columnas(slect_t)
         
    elif baseD=="informacion_ux":
        tabla = cn.obtener_tablas()
        slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
        campos =cn.obtener_campos(slect_t)
     
    elif baseD=="eventos_cartelera":
         tabla = cn.obtener_tablas2()
         slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
         campos =cn.obtener_campos2(slect_t)
    
    elif baseD=="chatbot_turismo":
         tabla = cn.obtener_tablas3()
         slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
         campos =cn.obtener_campos3(slect_t)     # obtiene los datos de la tabla
    else:
        st.text("seleciona una base de datos valida")
   


    col1, col2 = st.columns(2)    
    valores = {}

    indice = 0  
    
    for  campo in campos:
        if campo.lower() == "id"or campo.lower().startswith("id_"):

            continue
        with col1 if indice % 2 == 0 else col2:
            if "fecha" in campo.lower():
                valores[campo] = st.date_input(f"**{campo}:**")
            elif "dates" in campo.lower():
                valores[campo] =st.date_input(f"{campo}:")
            elif "mes" in campo.lower():
                valores[campo] = st.selectbox(f"{campo}:", options=Opt_M)
            elif "descripcion"  in campo.lower():
                valores[campo] =st.text_area(f"{campo}:",height=100,placeholder="Escribe aqui tu descrpcion:")
            else:
                valores[campo] = st.text_input(f"{campo}:")
        indice +=1

    if st.button("Guardar registro", key="guardar_registro"):
        try:

            if baseD=="test":
                 cnx.Crear_registro2(slect_t,valores)
                 st.success("Registro guardado exitosamente")
            elif baseD=="informacion_ux":
                 cn.crear_registro(slect_t, valores)
                 st.success("Registro guardado exitosamente")     
            elif baseD=="eventos_cartelera":
                 cn.crear_registro(slect_t, valores)
                 st.success("Registro guardado exitosamente")
            elif baseD=="chatbot_turismo":
                 cn.crear_registro3(slect_t, valores)
                 st.success("Registro guardado exitosamente")
            else:
                st.error("seleciona una base de datos valida")

        except Exception as e:
            st.error(f"Error al guardar el registro: {e}")



def selec_comp2(tabla,basedatos):
   
    if basedatos=="test":
        columnas = cnx.obtener_columnas(tabla)
        registros= cnx.obtener_Actividades()
    elif basedatos=="informacion_ux":
        columnas = cn.obtener_campos(tabla)         # obtiene los nombres de las columnas
        registros = cn.obtener_eventos(tabla)        # obtiene los datos de la tabla
    elif basedatos=="eventos_cartelera":
        columnas = cn.obtener_campos2(tabla)         # obtiene los nombres de las columnas
        registros = cn.obtener_eventos2(tabla)        # obtiene los datos de la tabla
    elif basedatos=="chatbot_turismo":
        columnas = cn.obtener_campos3(tabla)         # obtiene los nombres de las columnas
        registros = cn.obtener_eventos3(tabla)        # obtiene los datos de la tabla
    else:
        st.text("seleciona una base de datos valida")
     

    df_compn = pd.DataFrame(registros, columns=columnas)
    st.subheader("Registros")
    st.dataframe(df_compn)


def leer2(basedatos):
       st.subheader(f"Leer registros de: {basedatos} ")

       if basedatos=="test":
            diccionario_tablas = cnx.obtener_tablas()
       elif basedatos=="informacion_ux":
           diccionario_tablas= cn.obtener_tablas()
       elif basedatos=="eventos_cartelera":
           diccionario_tablas=cn.obtener_tablas2()
       elif basedatos=="chatbot_turismo":
           diccionario_tablas=cn.obtener_tablas3()
       else:
           st.text("seleciona una base de datos valida")

       tablas = st.selectbox("Selecciona una tabla", options=list(diccionario_tablas.values()))
       selec_comp2(tablas,basedatos)
       edit_b = st.button("Editar")
       if edit_b:
            try:
                 modificar2(tablas,basedatos)
            except Exception as e:
                st.error(f"Ocurrió un error al editar el evento: {e}")

@st.dialog("Modificar",width="large")
def modificar2(t_elec,bdatos):
    Opt_M =[" ","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    if bdatos=="test":
     campos =cnx.obtener_columnas(t_elec)
     st.write("Selecciona el campo a modificar")
     ids = cnx.editar_campo(t_elec)
     id_seleccionado = st.selectbox("Selecciona un ID", ids)
     registro= cnx.obtener_registro_id(id_seleccionado,t_elec)

    elif bdatos=="informacion_ux":
      campos =cn.obtener_campos(t_elec)
      st.write("Selecciona el campo a modificar")
      ids = cn.editar_campo(t_elec)
      id_seleccionado = st.selectbox("Selecciona un ID", ids)
      registro= cn.obtener_registro_id(id_seleccionado,t_elec,campos)
   
    elif bdatos=="eventos_cartelera":
      campos =cn.obtener_campos2(t_elec)
      st.write("Selecciona el campo a modificar")
      ids = cn.editar_campo2(t_elec)
      id_seleccionado = st.selectbox("Selecciona un ID", ids)
      registro= cn.obtener_registro_id2(id_seleccionado,t_elec,campos)

    elif bdatos=="chatbot_turismo":
      campos =cn.obtener_campos3(t_elec)
      st.write("Selecciona el campo a modificar")
      ids = cn.editar_campo3(t_elec)
      id_seleccionado = st.selectbox("Selecciona un ID", ids)
      registro= cn.obtener_registro_id3(id_seleccionado,t_elec,campos)

    else:
        st.text("seleciona una base de datos valida")
    

    
    col1, col2 = st.columns(2)

    
    valores = {}

    valor_idx = 0

    for campo in campos:
        
        with col1 if valor_idx % 2 == 0 else col2:
            valor_actual = registro[valor_idx]

            if "fecha" in campo.lower() or "dates" in campo.lower():
                valores[campo] = st.date_input(f"{campo}:", value=None)
            elif "mes" in campo.lower():
                valores[campo] = st.selectbox(f"{campo}:", options=Opt_M, index=Opt_M.index(valor_actual) if valor_actual in Opt_M else 0)
            elif "descripcion" in campo.lower():
                valores[campo] = st.text_area(f"{campo}:", value=valor_actual, height=100, placeholder="Escribe aquí tu descripción:")
            elif "respuesta" in campo.lower():
                valores[campo]= st.text_area( f"{campo}:", value=valor_actual, height=100)
            elif "pregunta" in campo.lower():
                valores[campo]= st.text_area( f"{campo}:", value=valor_actual, height=100)
            else:
                valores[campo] = st.text_input(f"{campo}:", value=valor_actual)

        valor_idx += 1
    st.text(f"tabla: {t_elec}")    
    G_b= st.button("Guardar cambios")
    if G_b:

        if bdatos=="test":
         cn.actualizar_registro(t_elec,id_seleccionado,valores)
         st.success("Registro actualizado correctamente")


        elif bdatos=="informacion_ux":
         cn.actualizar_registro(t_elec,id_seleccionado,valores)
         st.success("Registro actualizado correctamente")
        
        
        elif bdatos=="eventos_cartelera":
         cn.actualizar_registro2(t_elec,id_seleccionado,valores)
         st.success("Registro actualizado correctamente")
        
        
        elif bdatos=="chatbot_turismo":
         cn.actualizar_registro3(t_elec,id_seleccionado,valores)
         st.success("Registro actualizado correctamente")
        
        else:
             st.text("seleciona una base de datos valida")

@st.dialog("Eliminar",width="large")    
def eliminar2(Bdatos):
    if Bdatos=="test":
       D_tab= cnx.obtener_tablas()

    elif Bdatos=="informacion_ux":
       D_tab= cn.obtener_tablas()


    elif Bdatos=="eventos_cartelera":
       D_tab= cn.obtener_tablas2()


    elif Bdatos=="chatbot_turismo":
       D_tab= cn.obtener_tablas3() 

    else:
        st.text("seleciona una base de datos valida")    
   
    t_selec = st.selectbox("Elige una tabla", options= list(D_tab.values()))
    selec_comp2(t_selec,Bdatos)

    c1,c2 = st.columns([5,5])

    if Bdatos=="test":
      ids = cnx.editar_campo(t_selec)
      campos= cnx.obtener_columnas(t_selec)

    elif Bdatos=="informacion_ux":
      ids = cn.editar_campo(t_selec)
      campos= cn.obtener_campos(t_selec)


    elif Bdatos=="eventos_cartelera":
      ids = cn.editar_campo2(t_selec)
      campos= cn.obtener_campos2(t_selec)

    elif Bdatos=="chatbot_turismo":
      ids = cn.editar_campo3(t_selec)
      campos= cn.obtener_campos3(t_selec)

    else:
        st.text("seleciona una base de datos valida")  

    with c1:
         id_seleccionado = st.selectbox("Selecciona un ID", ids) 
         
         if Bdatos=="test":
          registro=cnx.obtener_registro_id(id_seleccionado, t_selec)
         elif Bdatos=="informacion_ux":
          registro=cn.obtener_registro_id(id_seleccionado, t_selec,campos)
         elif Bdatos=="eventos_cartelera":
          registro=cn.obtener_registro_id2(id_seleccionado, t_selec,campos)
         elif Bdatos=="chatbot_turismo":
           registro=cn.obtener_registro_id3(id_seleccionado, t_selec,campos)
    with c2:
         
         if Bdatos=="test":
          st.text(f"Título: {registro[0]}")
          st.text(f"Recinto: {registro[1]}")
          st.text(f"Dirección: {registro[2]}")
        
         elif Bdatos=="informacion_ux":
          
          st.text(f"Titulo: {registro[1]}")
          st.text(f"Pregunta: {registro[3]}")
          st.text(f"Respuesta: {registro[4]}")
        
         elif Bdatos=="eventos_cartelera":
          
          st.text(f"Titulo: {registro[1]}")
          st.text(f"Recinto: {registro[2]}")
          
        
         elif Bdatos=="chatbot_turismo":
          
          st.text(f"ID: {registro[0]}")
          st.text(f"Nombre/categoria: {registro[1]}")
          
   
    b_El = st.button("Eliminar registro")
    if b_El:

         if Bdatos=="test":
          cnx.eliminar_registro(t_selec,id_seleccionado)
          st.success("Registro eliminado exitosamente.") 


         elif Bdatos=="informacion_ux":
          cn.eliminar_campo(t_selec,id_seleccionado)
          st.success("Registro eliminado exitosamente.") 
          
        
         elif Bdatos=="eventos_cartelera":
          cn.eliminar_campo2(t_selec,id_seleccionado)
          st.success("Registro eliminado exitosamente.") 
        
        
         elif Bdatos=="chatbot_turismo":
          cn.eliminar_campo3(t_selec,id_seleccionado)
          st.success("Registro eliminado exitosamente.") 
        
         else:
             st.text("seleciona una base de datos valida")
   
menu_BD()