import streamlit as st
import pandas as pd
import Herramientas as h  # Módulo de herramientas para links de las páginas
import conexion_N as cnN # Módulo para la conexion de la base de datos del chatbot fifa
import log 
from normalizacion import normalizar_dataframe


h.verificar_sesion()
h.acceso_multiple(["administrador","usuarioUX" , "usuarioCl", "usuarioTU"])

def menu_BD():
    h.MenuPrincipal()
    st.set_page_config(page_title="Componetes", initial_sidebar_state="auto",page_icon="💬")
    st.markdown(h.page_bg_img, unsafe_allow_html=True)
    
    st.title("Eventos Prioritarios")

    Menu_Sec = ["Leer","Crear"]
    
    opcion = st.selectbox("Selecciona una opción", options=Menu_Sec, index=0)

    if opcion == "Crear":
        crear2()
    elif opcion == "Leer":
        leer2()     
   
def leer2():
       st.subheader(f"Leer registros de: Eventos Prioritarios ")
       diccionario_tablas=cnN.obtener_tablas()
       

       tablas = st.selectbox("Selecciona una tabla", options=list(diccionario_tablas.values()))
       selec_comp2(tablas)
       edit_b = st.button("Editar")
       if edit_b:
            try:
                 modificar2(tablas)
            except Exception as e:
                st.error(f"Ocurrió un error al editar el evento: {e}")



def selec_comp2(tabla):
    
    columnas = cnN.obtener_campos(tabla)         
    registros = cnN.obtener_eventos(tabla)        

    df_compn = pd.DataFrame(registros, columns=columnas)
    st.subheader("Registros")
    st.dataframe(df_compn)

@st.dialog("Modificar registro",width="large")
def modificar2(t_elec):
    Opt_M = [" ", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    campos = cnN.obtener_campos(t_elec)
    st.write("Selecciona el campo a modificar")

    ids = cnN.editar_campo(t_elec)
    id_seleccionado = st.selectbox("Selecciona un ID", ids)
    registro = cnN.obtener_registro_id(id_seleccionado, t_elec, campos)

    # Definir el formulario
    with st.form("form_modificar_registro"):
        col1, col2 = st.columns(2)
        valores = {}
        valor_idx = 0

        for campo in campos:
            with col1 if valor_idx % 2 == 0 else col2:
                valor_actual = registro[valor_idx]

                if "dates_otros" in campo.lower():
                    valores[campo] = st.text_input(f"{campo}:", value=valor_actual)
                elif "codigo_postal" in campo.lower():
                    valores[campo] = st.number_input(f"{campo}:", min_value=0, step=1, value=int(valor_actual) if valor_actual else 0)
                elif "dates" in campo.lower():
                    valores[campo] = st.date_input(f"{campo}:", value=valor_actual)
                elif "month" in campo.lower():
                    valores[campo] = st.selectbox(f"{campo}:", options=Opt_M,
                                                  index=Opt_M.index(valor_actual) if valor_actual in Opt_M else 0)
                elif "description" in campo.lower():
                    valores[campo] = st.text_area(f"{campo}:", value=valor_actual, height=100,
                                                  placeholder="Escribe aquí tu descripción:")
                elif "hora" in campo.lower():
                    valores[campo] = st.time_input(f"{campo}:", value=valor_actual)
                else:
                    valores[campo] = st.text_input(f"{campo}:", value=valor_actual)

            valor_idx += 1

        st.text(f"Tabla: {t_elec}")

        # Botón dentro del formulario
        submitted = st.form_submit_button("Guardar cambios")

        if submitted:
            try:
                # Mandas todos los valores como dict
                cnN.actualizar_registro(t_elec, id_seleccionado, valores)
                st.success("Registro actualizado correctamente")
            except Exception as e:
                st.error(f"Error al actualizar el registro: {e}")
      
def crear2():
    Opt_M = [" ", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    tabla = cnN.obtener_tablas()
    slect_t = st.selectbox("Selecciona una tabla:", options=tabla, index=0)
    campos = cnN.obtener_campos(slect_t)

    # Definir el formulario
    with st.form("form_crear_registro"):
        col1, col2 = st.columns(2)
        valores = {}
        indice = 0  

        for campo in campos:
            if campo.lower() == "id" or campo.lower().startswith("id_"):
                continue

            with col1 if indice % 2 == 0 else col2:
                if "dates_otros" in campo.lower():
                    valores[campo] = st.text_input(f"{campo}:")
                elif "codigo_postal" in campo.lower():
                    valores[campo] = st.number_input(f"{campo}:", min_value=0, step=1)
                elif "dates" in campo.lower():
                    valores[campo] = st.date_input(f"{campo}:")
                elif "month" in campo.lower():
                    valores[campo] = st.selectbox(f"{campo}:", options=Opt_M)
                elif "description" in campo.lower():
                    valores[campo] = st.text_area(f"{campo}:", height=100, placeholder="Escribe aquí tu descripción:")
                elif "hora" in campo.lower():
                    valores[campo] = st.time_input(f"{campo}:")
                elif "prioridad" in campo.lower():
                    valores[campo] = st.selectbox(f"{campo}:", options=["alta", "media", "baja"])
                else:
                    valores[campo] = st.text_input(f"{campo}:")
            indice += 1

        # Botón dentro del formulario
        submitted = st.form_submit_button("Guardar registro")

        if submitted:
            try:
                cnN.crear_registro(slect_t,campos ,valores)
                st.success("Registro guardado exitosamente")
            except Exception as e:
                st.error(f"Error al guardar el registro: {e}")

          
        
menu_BD()