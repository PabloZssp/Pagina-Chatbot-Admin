import streamlit as st



def MenuPrincipal():
    
    with st.sidebar:
         st.page_link("Pagina_Principal.py",label="Pagina Principal",icon="🤖")
         st.page_link("pages/Formularios.py",label="Componetes",icon="📝")
         st.page_link("pages/Chatbot.py",label="Graficas",icon="📊")



##Estes es es fondo de pantalla de la pagina la imagen es de prueba se puede cambiar por cualquier otra imagen
##Esta dividida en 2 partes una para el fondo de la pagina y otra para el fondo de la barra lateral
##
##para cambiar la imagen solo hay que cambiar la url de la imagen en el string
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: rgba(159, 34, 65, 0.5);
    background-size: cover;
}



[data-testid="stHeader"] {
    background-color: rgba(188, 149, 92, 0.2);

}


[data-testid="stSidebar"] {
    background-color: rgba(44, 45, 50);
    background-size: cover;
}
</style>
"""