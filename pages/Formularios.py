
import streamlit as st
import pandas as pd
import Herramientas as h  # Módulo de herramientas para links de las páginas
import conexion2 as cn # Módulo para la conexion de la base de datos principal 
import log 
from normalizacion import normalizar_dataframe
h.verificar_sesion()
h.acceso_multiple(["administrador","usuarioUX" , "usuarioCl", "usuarioTU"])

def menu_BD():

    h.MenuPrincipal()
    st.set_page_config(page_title="Componetes", initial_sidebar_state="auto",page_icon="💬")
    st.markdown(h.page_bg_img, unsafe_allow_html=True)
    st.title("Bases de datos")
    
    
    rol = log.obtener_rol_actual()
    
    if rol == "administrador":
        Menu =[" ","eventos_cartelera","informacion_ux","chatbot_turismo","test","chatbot_fifa"]
    elif rol== "usuarioUX":
        Menu =[" ","informacion_ux",]
    elif rol== "usuarioCl":
        Menu =[" ","eventos_cartelera"]
    elif rol== "usuarioTU":
        Menu =[" ","chatbot_turismo"]
   
    Bdatos=st.selectbox("Selecciona una Base de datos:",options=Menu)

    if Bdatos == "informacion_ux":
        
        opciones2(Bdatos)

    elif Bdatos == "eventos_cartelera":
             
        opciones2(Bdatos)

    elif Bdatos == "chatbot_turismo":        
        if rol=="administrador":
            opcionesMT =[" ","categorias","preguntas_frecuentes","prompts_seguridad"]
        else:
            opcionesMT =[" ","categorias","preguntas_frecuentes"]
        squma =st.selectbox("Elige un esquema", options=opcionesMT)
        if squma != " ":
         opcionesT(Bdatos,squma)

    elif Bdatos == "test":        
        opciones2(Bdatos)
    elif Bdatos == "chatbot_fifa":        
        opciones2(Bdatos)
        
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
         tabla = cn.obtener_tablas4()
         slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
         campos =cn.obtener_campos4(slect_t)
         
    elif baseD=="informacion_ux":
        tabla = cn.obtener_tablas()
        slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
        campos =cn.obtener_campos(slect_t)
     
    elif baseD=="eventos_cartelera":
         tabla = cn.obtener_tablas2()
         slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
         campos =cn.obtener_campos2(slect_t)
    
    
    elif baseD=="chatbot_fifa":
         tabla = cn.obtener_tablas6()
         slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
         campos =cn.obtener_campos6(slect_t)     # obtiene los datos de la tabla
   
    else:
        st.text("seleciona una base de datos valida")
   


    col1, col2 = st.columns(2)    
    valores = {}

    indice = 0  
    
    for  campo in campos:
        if campo.lower() == "id"or campo.lower().startswith("id_"):

            continue
        with col1 if indice % 2 == 0 else col2:
            if "dates_otros" in campo.lower():
                valores[campo] = st.text_input(f"{campo}:")
            elif "codigo_postal" in campo.lower():
                valores[campo] = st.number_input(f"{campo}:", min_value=0, step=1)
            elif "dates" in campo.lower():
                valores[campo] =st.date_input(f"{campo}:")
            elif "month"  in campo.lower():
                valores[campo] = st.selectbox(f"{campo}:", options=Opt_M)
            elif "descripcion"  in campo.lower():
                valores[campo] =st.text_area(f"{campo}:",height=100,placeholder="Escribe aqui tu descrpcion:")
            elif "hora"  in campo.lower():
                valores[campo] = st.time_input(f"{campo}:")
            else:
                valores[campo] = st.text_input(f"{campo}:")
        indice +=1

    if st.button("Guardar registro", key="guardar_registro"):
        try:

            if baseD=="test":
                 cn.crear_registro4(slect_t,valores)
                 st.success("Registro guardado exitosamente")
            elif baseD=="informacion_ux":
                 cn.crear_registro(slect_t, valores)
                 st.success("Registro guardado exitosamente")     
            elif baseD=="eventos_cartelera":
                 cn.crear_registro2(slect_t, valores)
                 st.success("Registro guardado exitosamente")
            
            elif baseD=="chatbot_fifa":
                 cn.crear_registro6(slect_t,valores)
                 st.success("Registro guardado exitosamente")
            else:
                st.error("seleciona una base de datos valida")

        except Exception as e:
            st.error(f"Error al guardar el registro: {e}")
    archivo = st.file_uploader("Elige un archivo CSV o Excel", type=["csv", "xlsx"])
    df = None

    if archivo is not None:
        nombre = archivo.name

        if nombre.endswith(".csv"):
            df = pd.read_csv(archivo)
        elif nombre.endswith(".xlsx"):
            df = pd.read_excel(archivo)
        else:
            st.error("Formato no soportado.")
            df = None

        if df is not None:
            columnas_archivo = list(df.columns)
            columnas_tabla = [c for c in campos if not c.lower().startswith("id")]
            print(columnas_tabla)
            print(columnas_archivo)

            faltantes = set(columnas_tabla) - set(columnas_archivo)
            extras = set(columnas_archivo) - set(columnas_tabla)

            if faltantes or extras:
                st.warning(" Las columnas del archivo no coinciden con la tabla seleccionada.")
                if faltantes:
                    st.write(" Faltan en el archivo:", list(faltantes))
                if extras:
                    st.write(" Sobran en el archivo:", list(extras))
            else:
                st.success(" Las columnas coinciden. Puedes proceder con la carga.")
                st.write("Vista previa de los datos:")
                st.dataframe(df.head())

                
                if st.button("Cargar datos en la base"):
                    if df.empty:
                        st.warning("No hay registros para cargar.")
                    else:
                        
                        mensaje_info = st.empty()
                        mensaje_info.info("Normalizando datos...")
                        barra_normalizacion = st.progress(0)

                        def actualizar_barra_normalizacion(valor):
                            barra_normalizacion.progress(valor)

                        df, log_df = normalizar_dataframe(df, actualizar_barra_normalizacion)
                        barra_normalizacion.empty()
                        mensaje_info.success("Normalización completada")
                        #st.dataframe(log_df)

                        
                        mensaje_info.info("Cargando datos en la base de datos...")
                        barra_carga = st.progress(0)
                        total = len(df)
                        errores = []
                        cargados = 0

                        for i, fila in df.iterrows():
                            valores_fila = fila[columnas_tabla].to_dict()
                            ok = False
                            try:
                                if baseD == "test":
                                    ok = cn.crear_registro4(slect_t, valores_fila)
                                elif baseD == "informacion_ux":
                                    ok = cn.crear_registro(slect_t, valores_fila)
                                elif baseD == "eventos_cartelera":
                                    ok = cn.crear_registro2(slect_t, valores_fila)
                                elif baseD == "chatbot_turismo":
                                    ok = cn.crear_registro3(slect_t, valores_fila)
                                elif baseD == "chatbot_fifa":
                                    ok = cn.crear_registro6(slect_t, valores_fila)

                                if ok:
                                    cargados += 1
                                else:
                                    errores.append((i, "No se insertó el registro"))
                            except Exception as e:
                                errores.append((i, str(e)))


                            progreso = int((i + 1) / total * 100)
                            barra_carga.progress(min(progreso, 100))

                        barra_carga.empty()
                        mensaje_info.success("Carga finalizada")

                        if errores:
                            st.warning(f"Se cargaron {cargados} registros, pero {len(errores)} fallaron.")
                            for idx, err in errores:
                                st.write(f"Fila {idx}: {err}")
                        else:
                            st.success("Todos los registros han sido cargados exitosamente.")





def selec_comp2(tabla,basedatos):
   
    if basedatos=="test":
        columnas = cn.obtener_campos4(tabla)
        registros= cn.obtener_eventos4(tabla)
    elif basedatos=="informacion_ux":
        columnas = cn.obtener_campos(tabla)         
        registros = cn.obtener_eventos(tabla)        
    elif basedatos=="eventos_cartelera":
        columnas = cn.obtener_campos2(tabla)         
        registros = cn.obtener_eventos2(tabla)        
    elif basedatos=="chatbot_turismo":
        columnas = cn.obtener_campos3(tabla)         
        registros = cn.obtener_eventos3(tabla) 
    elif basedatos=="chatbot_fifa":
        columnas = cn.obtener_campos6(tabla)
        registros= cn.obtener_eventos6(tabla)
    else:
        st.text("seleciona una base de datos valida")
     

    df_compn = pd.DataFrame(registros, columns=columnas)
    st.subheader("Registros")
    st.dataframe(df_compn)

def leer2(basedatos):
       st.subheader(f"Leer registros de: {basedatos} ")

       if basedatos=="test":
            diccionario_tablas = cn.obtener_tablas4()
       elif basedatos=="informacion_ux":
           diccionario_tablas= cn.obtener_tablas()
       elif basedatos=="eventos_cartelera":
           diccionario_tablas=cn.obtener_tablas2()
       elif basedatos=="chatbot_turismo":
           diccionario_tablas=cn.obtener_tablas3()
       elif basedatos=="chatbot_fifa":
           diccionario_tablas=cn.obtener_tablas6()
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
     campos =cn.obtener_campos4(t_elec)
     st.write("Selecciona el campo a modificar")
     ids = cn.editar_campo4_1(t_elec)
     id_seleccionado = st.selectbox("Selecciona un ID", ids)
     registro= cn.obtener_registro_id4(id_seleccionado,t_elec,campos)

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
    elif bdatos=="chatbot_fifa":
      campos =cn.obtener_campos6(t_elec)
      st.write("Selecciona el campo a modificar")
      ids = cn.editar_campo6(t_elec)
      id_seleccionado = st.selectbox("Selecciona un ID", ids)
      registro= cn.obtener_registro_id6(id_seleccionado,t_elec,campos)

    else:
        st.text("seleciona una base de datos valida")
    

    
    col1, col2 = st.columns(2)

    
    valores = {}

    valor_idx = 0

    for campo in campos:
        
        with col1 if valor_idx % 2 == 0 else col2:
            valor_actual = registro[valor_idx]

            if "dates_otros" in campo.lower():
                valores[campo] = st.text_input(f"{campo}:")
            elif "codigo_postal" in campo.lower():
                valores[campo] = st.number_input(f"{campo}:", min_value=0, step=1)
            elif "dates" in campo.lower():
                valores[campo] =st.date_input(f"{campo}:", value=None)
            elif "month" in campo.lower():
                valores[campo] = st.selectbox(f"{campo}:", options=Opt_M, index=Opt_M.index(valor_actual) if valor_actual in Opt_M else 0)
            elif "description" in campo.lower():
                valores[campo] = st.text_area(f"{campo}:", value=valor_actual, height=100, placeholder="Escribe aquí tu descripción:")
            elif "respuesta" in campo.lower():
                valores[campo]= st.text_input( f"{campo}:", value=valor_actual)
            elif "pregunta" in campo.lower():
                valores[campo]= st.text_input( f"{campo}:", value=valor_actual)
            else:
                valores[campo] = st.text_input(f"{campo}:", value=valor_actual)

        valor_idx += 1
    st.text(f"tabla: {t_elec}")    
    G_b= st.button("Guardar cambios")
    if G_b:

        if bdatos=="test":
         cn.actualizar_registro5(t_elec,id_seleccionado,valores)
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

        elif bdatos=="chatbot_fifa":
         cn.actualizar_registro6(t_elec,id_seleccionado,valores)
         st.success("Registro actualizado correctamente")

        else:
             st.text("seleciona una base de datos valida")

@st.dialog("Eliminar",width="large")    
def eliminar2(Bdatos):
    if Bdatos=="test":
       D_tab= cn.obtener_tablas5()

    elif Bdatos=="informacion_ux":
       D_tab= cn.obtener_tablas()


    elif Bdatos=="eventos_cartelera":
       D_tab= cn.obtener_tablas2()


    elif Bdatos=="chatbot_turismo":
       D_tab= cn.obtener_tablas3() 

    elif Bdatos=="chatbot_fifa":
       D_tab= cn.obtener_tablas6() 

    else:
        st.text("seleciona una base de datos valida")    
   
    t_selec = st.selectbox("Elige una tabla", options= list(D_tab.values()))
    selec_comp2(t_selec,Bdatos)

    c1,c2 = st.columns([5,5])

    if Bdatos=="test":
      ids = cn.editar_campo5(t_selec)
      campos= cn.obtener_campos5(t_selec)

    elif Bdatos=="informacion_ux":
      ids = cn.editar_campo(t_selec)
      campos= cn.obtener_campos(t_selec)


    elif Bdatos=="eventos_cartelera":
      ids = cn.editar_campo2(t_selec)
      campos= cn.obtener_campos2(t_selec)

    elif Bdatos=="chatbot_turismo":
      ids = cn.editar_campo3(t_selec)
      campos= cn.obtener_campos3(t_selec)

    elif Bdatos=="chatbot_fifa":
      ids = cn.editar_campo6(t_selec)
      campos= cn.obtener_campos6(t_selec)

    else:
        st.text("seleciona una base de datos valida")  

    with c1:
         id_seleccionado = st.selectbox("Selecciona un ID", ids) 
         
         if Bdatos=="test":
          registro=cn.obtener_registro_id5(id_seleccionado, t_selec,campos)
         elif Bdatos=="informacion_ux":
          registro=cn.obtener_registro_id(id_seleccionado, t_selec,campos)
         elif Bdatos=="eventos_cartelera":
          registro=cn.obtener_registro_id2(id_seleccionado, t_selec,campos)
         elif Bdatos=="chatbot_turismo":
           registro=cn.obtener_registro_id3(id_seleccionado, t_selec,campos)
         elif Bdatos=="chatbot_fifa":
           registro=cn.obtener_registro_id6(id_seleccionado, t_selec,campos)
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
         elif Bdatos=="chatbot_fifa":
          
          st.text(f"ID: {registro[0]}")
          st.text(f"pregunta: {registro[3]}")
          st.text(f"respuesta: {registro[4]}")

    b_El = st.button("Eliminar registro")
    if b_El:

         if Bdatos=="test":
          cn.eliminar_campo5(t_selec,id_seleccionado)
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
         
         elif Bdatos=="chatbot_fifa":
          cn.eliminar_campo6(t_selec,id_seleccionado)
          st.success("Registro eliminado exitosamente.")
        
         else:
             st.text("seleciona una base de datos valida")

def opcionesT(Bdatos, esquema):

    Menu_Sec = ["Leer","Crear" ,"Eliminar"]
    st.subheader("Formulario")
    opcion = st.selectbox("Selecciona una opción", options=Menu_Sec, index=0)

    if opcion == "Crear":
        crearT(esquema)
    elif opcion == "Leer":
        leerT(Bdatos,esquema)     
    elif opcion == "Eliminar":
        eliminarT(esquema)

@st.dialog("Crear", width="large")
def crearT(esquema):
    Opt_M = [" ", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"] 
        
    if esquema=="categorias":
         tabla = cn.obtener_tablas3()
         slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
         campos =cn.obtener_campos3(slect_t)     
    elif esquema=="preguntas_frecuentes":
         tabla = cn.obtener_tablas3_1(esquema)
         slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
         campos =cn.obtener_campos3_1(slect_t,esquema)     
    elif esquema=="prompts_seguridad":
         tabla = cn.obtener_tablas3_1(esquema)
         slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)
         campos =cn.obtener_campos3_1(slect_t,esquema)     


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
            elif "month"  in campo.lower():
                valores[campo] = st.selectbox(f"{campo}:", options=Opt_M)
            elif "descripcion"  in campo.lower():
                valores[campo] =st.text_area(f"{campo}:",height=100,placeholder="Escribe aqui tu descrpcion:")
            else:
                valores[campo] = st.text_input(f"{campo}:")
        indice +=1

    if st.button("Guardar registro", key="guardar_registro"):
        try:  
            if esquema=="categorias":
             cn.crear_registro3(slect_t, valores)
            elif esquema=="preguntas_frecuentes":
             cn.crear_registro3_1(slect_t, valores,esquema)
            elif esquema=="prompts_seguridad":
             cn.crear_registro3_1(slect_t, valores,esquema)
             st.success("Registro guardado exitosamente")
            
            else:
                st.error("selecciona una base de datos valida")

        except Exception as e:
            st.error(f"Error al guardar el registro: {e}")
    archivo = st.file_uploader("Elige un archivo CSV o Excel", type=["csv", "xlsx"])
    df = None

    if archivo is not None:
        nombre = archivo.name

        if nombre.endswith(".csv"):
            df = pd.read_csv(archivo)
        elif nombre.endswith(".xlsx"):
            df = pd.read_excel(archivo)
        else:
            st.error("Formato no soportado.")
            df = None

        if df is not None:
            columnas_archivo = list(df.columns)
            columnas_tabla = [c for c in campos if not c.lower().startswith("id")]
            print(columnas_tabla)
            print(columnas_archivo)

            faltantes = set(columnas_tabla) - set(columnas_archivo)
            extras = set(columnas_archivo) - set(columnas_tabla)

            if faltantes or extras:
                st.warning(" Las columnas del archivo no coinciden con la tabla seleccionada.")
                if faltantes:
                    st.write(" Faltan en el archivo:", list(faltantes))
                if extras:
                    st.write(" Sobran en el archivo:", list(extras))
            else:
                st.success(" Las columnas coinciden. Puedes proceder con la carga.")
                st.write("Vista previa de los datos:")
                st.dataframe(df.head())

            
            if st.button("Cargar datos en la base"):
                if esquema == "eventos_cartelera":
                    df, log_df = normalizar_dataframe(df)
                    st.info("Datos normalizados antes de cargar.")
                    #st.dataframe(log_df)

                progress_bar = st.progress(0)
                total = len(df)

                for i, fila in df.iterrows():
                    valores_fila = fila[columnas_tabla].to_dict()
                    if esquema == "categorias":
                        cn.crear_registro3(slect_t, valores_fila)
                    elif esquema == "informacion_ux":
                        cn.crear_registro3_1(slect_t, valores_fila, esquema)
                    elif esquema == "eventos_cartelera":
                        cn.crear_registro3_1(slect_t, valores_fila, esquema)

                    progress_bar.progress(int((i + 1) / total * 100))

                progress_bar.empty()

                st.success("Todos los registros fueron cargados correctamente.")


def selec_compT(tabla,esquema):

    if esquema=="categorias":
        columnas = cn.obtener_campos3(tabla)
        registros= cn.obtener_eventos3(tabla)
    elif esquema=="preguntas_frecuentes":
        columnas = cn.obtener_campos3_1(tabla,esquema)         
        registros = cn.obtener_eventos3_1(tabla,esquema)       
    elif esquema=="prompts_seguridad":
        columnas = cn.obtener_campos3_1(tabla,esquema)        
        registros = cn.obtener_eventos3_1(tabla,esquema)        
   
    else:
        st.text("seleciona una base de datos valida")
     
   
    df_compn = pd.DataFrame(registros, columns=columnas)
    st.subheader("Registros")
    st.dataframe(df_compn)


def leerT(basedatos, esquema):
       st.subheader(f"Leer registros de: {basedatos} ")

       if esquema=="categorias":
            diccionario_tablas = cn.obtener_tablas3()
       elif esquema=="preguntas_frecuentes":
           diccionario_tablas= cn.obtener_tablas3_1(esquema)
       elif esquema=="prompts_seguridad":
           diccionario_tablas=cn.obtener_tablas3_1(esquema)
       
       else:
           st.text("seleciona una base de datos valida")

       tablas = st.selectbox("Selecciona una tabla", options=list(diccionario_tablas.values()))
       selec_compT(tablas,esquema)
       edit_b = st.button("Editar")
       if edit_b:
            try:
                 modificarT(tablas,esquema)
            except Exception as e:
                st.error(f"Ocurrió un error al editar el evento: {e}")

@st.dialog("Modificar",width="large")
def modificarT(t_elec,squema):
    Opt_M =[" ","Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    if squema=="categorias":
        campos =cn.obtener_campos3(t_elec)
        st.write("Selecciona el campo a modificar")
        ids = cn.editar_campo3(t_elec)
        id_seleccionado = st.selectbox("Selecciona un ID", ids)
        registro= cn.obtener_registro_id3(id_seleccionado,t_elec,campos)

    elif squema=="preguntas_frecuentes":
        campos =cn.obtener_campos3_1(t_elec,squema)
        st.write("Selecciona el campo a modificar")
        ids = cn.editar_campo3_1(t_elec,squema)
        id_seleccionado = st.selectbox("Selecciona un ID", ids)
        registro= cn.obtener_registro_id3_1(id_seleccionado,t_elec,campos,squema)

    elif squema=="prompts_seguridad":
        campos =cn.obtener_campos3_1(t_elec,squema)
        st.write("Selecciona el campo a modificar")
        ids = cn.editar_campo3_1(t_elec,squema)
        id_seleccionado = st.selectbox("Selecciona un ID", ids)
        registro= cn.obtener_registro_id3_1(id_seleccionado,t_elec,campos,squema) 
        
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
            elif "month" in campo.lower():
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

        if squema=="categorias":
         cn.actualizar_registro3(t_elec,id_seleccionado,valores)
         st.success("Registro actualizado correctamente")


        elif squema=="preguntas_frecuentes":
         cn.actualizar_registro3_1(t_elec,id_seleccionado,valores,squema)
         st.success("Registro actualizado correctamente")
        
        
        elif squema=="prompts_seguridad":
         cn.actualizar_registro3_1(t_elec,id_seleccionado,valores,squema)
         st.success("Registro actualizado correctamente")
        
        else:
             st.text("selecciona un esquema valido")

    

@st.dialog("Eliminar",width="large")    
def eliminarT(esquema):
    if esquema=="categorias":
       D_tab= cn.obtener_tablas3()

    elif esquema=="preguntas_frecuentes":
       D_tab= cn.obtener_tablas3_1(esquema)


    elif esquema=="prompts_seguridad":
       D_tab= cn.obtener_tablas3_1(esquema)

    else:
        st.text("seleciona una base de datos valida")    
   
    t_selec = st.selectbox("Elige una tabla", options= list(D_tab.values()))
    selec_compT(t_selec,esquema)

    c1,c2 = st.columns([5,5])

    if esquema=="categorias":
      ids = cn.editar_campo3(t_selec)
      campos= cn.obtener_campos3(t_selec)

    elif esquema=="preguntas_frecuentes":
      ids = cn.editar_campo3_1(t_selec,esquema)
      campos= cn.obtener_campos3_1(t_selec,esquema)


    elif esquema=="prompts_seguridad":
      ids = cn.editar_campo3_1(t_selec,esquema)
      campos= cn.obtener_campos3_1(t_selec,esquema)

    else:
        st.text("seleciona un esquema de datos valido")

    with c1:
         id_seleccionado = st.selectbox("Selecciona un ID", ids) 
         
         if esquema=="categorias":
          registro=cn.obtener_registro_id3(id_seleccionado, t_selec,campos)
         elif esquema=="preguntas_frecuentes":
          registro=cn.obtener_registro_id3_1(id_seleccionado, t_selec,campos,esquema)
         elif esquema=="prompts_seguridad":
          registro=cn.obtener_registro_id3_1(id_seleccionado, t_selec,campos,esquema)

    with c2:

         if esquema=="categorias":
          st.text(f"ID: {registro[0]}")
          st.text(f"nombre: {registro[1]}")
          st.text(f"descripcion: {registro[2]}")

         elif esquema=="preguntas_frecuentes":

          st.text(f"id: {registro[0]}")
          st.text(f"Pregunta: {registro[3]}")
          st.text(f"Respuesta: {registro[4]}")

         elif esquema=="prompts_seguridad":

          st.text(f"id: {registro[0]}")
          st.text(f"contenido: {registro[1]}")
          
        
    b_El = st.button("Eliminar registro")
    if b_El:

         if esquema=="categorias":
          cn.eliminar_campo3(t_selec,id_seleccionado)
          st.success("Registro eliminado exitosamente.") 


         elif esquema=="preguntas_frecuentes":
          cn.eliminar_campo3_1(t_selec,id_seleccionado,esquema)
          st.success("Registro eliminado exitosamente.") 
          
        
         elif esquema=="prompts_seguridad":
          cn.eliminar_campo3_1(t_selec,id_seleccionado,esquema)
          st.success("Registro eliminado exitosamente.") 
        
         else:
             st.text("seleciona un esquema valido")

menu_BD()


