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
    
    Menu =["eventos_cartelera","informacion_ux","chatbot_turismo","test"]
    
    eleccion=st.selectbox("Selecciona una Base de datos:",options=Menu)


    if eleccion == "informacion_ux":
        tabla = cn.obtener_tablas()
        

        slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)

        campos =cn.obtener_campos(slect_t)

        st.selectbox("Campos disponibles",options=campos,index=0)
        
        opciones(tabla,campos)

        
        
    elif eleccion == "eventos_cartelera":
        tabla = cn.obtener_tablas2()
        

        slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)

        campos =cn.obtener_campos2(slect_t)

        st.selectbox("Campos disponibles",options=campos,index=0)
        
        opciones(tabla,campos)
    elif eleccion == "chatbot_turismo":
        "menu chatbotturismo"
    elif eleccion == "test":
        tabla = cnx.obtener_tablas()
        

        slect_t=st.selectbox("Selecciona una tabla:",options=tabla,index=0)

        campos =cnx.obtener_columnas(slect_t)

        st.selectbox("Campos disponibles",options=campos,index=0)
        
        opciones(tabla,campos)

        
    
def opciones(tabla,campos):

    Menu_Sec = ["Leer","Crear" , "Eliminar"]
    st.subheader("Formulario")
    opcion = st.selectbox("Selecciona una opción", options=Menu_Sec, index=0)

    if opcion == "Crear":
        crear(tabla, campos)
    elif opcion == "Leer":
        leer()     
    elif opcion == "Eliminar":
        eliminar(tabla)



@st.dialog("Crear", width="large")
def crear(entrada, campos):
    Opt_M = [" ", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    tabla = st.selectbox("Tabla:", options=entrada, index=0)

   
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


def leer():
       st.subheader("Leer registros")
       diccionario_tablas = cn.obtener_tablas()
       tablas = st.selectbox("Selecciona una tabla", options=list(diccionario_tablas.values()))
       selec_comp(tablas)
       edit_b = st.button("Editar")
       if edit_b:
            try:
                 modificar(tablas)
            except Exception as e:
                st.error(f"Ocurrió un error al editar el evento: {e}")
    
def eliminar(entrada):
    "eliminar"


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

    
menu_BD()