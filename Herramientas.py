import streamlit as st

def MenuPrincipal():
    
    with st.sidebar:
         st.page_link("Pagina_Principal.py",label="Pagina Principal",icon="🤖")
         st.page_link("pages/Bases_Datos.py",label="Formularios",icon="💬")
         st.page_link("pages/Chatbot.py",label="Graficas",icon="📊")



##Estes es es fondo de pantalla de la pagina la imagen es de prueba se puede cambiar por cualquier otra imagen
##Esta dividida en 2 partes una para el fondo de la pagina y otra para el fondo de la barra lateral
##
##para cambiar la imagen solo hay que cambiar la url de la imagen en el string
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://th.bing.com/th/id/R.7d7f4351c51dd1200bdea57735c8e25b?rik=Ct6%2bBPXenE4VQw&riu=http%3a%2f%2fgetwallpapers.com%2fwallpaper%2ffull%2fa%2f9%2f8%2f451587.jpg&ehk=5dyceC%2fQupl%2bHpSVz%2bmzhbjja%2fqhzC90tPKDisWow%2bk%3d&risl=&pid=ImgRaw&r=0");
    background-size: cover;
}



[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);

}


[data-testid="stSidebar"] {
    background-image: url("https://tse2.mm.bing.net/th/id/OIP.Ba2JQ6Cmz07WXLAliKvM-QHaEo?pid=ImgDet&w=474&h=296&rs=1&o=7&rm=3");
    background-size: cover;
}
</style>
"""