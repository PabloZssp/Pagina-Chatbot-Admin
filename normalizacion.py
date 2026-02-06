import pandas as pd
from datetime import datetime

category_map = {
    "Música y Conciertos": [
        "musica", "música", "musica en vivo", "música en vivo", "concierto", 
        "conciertos", "concierto clasico", "concierto de violin", 
        "presentacion musical", "presentación musical", "toquin", "toquín",
        "festival musical", "show musical", "recital", "evento de musica"
    ],
    "Museos y Exposiciones": [
        "museo", "museos", "expo", "exposición", "exposicion", "expocicion", 
        "exposision", "muestra", "muestra artistica", "museo ambulante", 
        "casa abierta", "noche de museos"
    ],
    "Artes Escénicas": [
        "teatro", "obra", "obra de teatro", "danza", "baile", "performance",
        "stand up", "monologo", "ópera", "opera"
    ],
    "Cine": [
        "cine", "pelicula", "películas", "proyección", "cine club", 
        "cine al aire libre", "cine de arte", "funcion"
    ],
    "Festivales y Ferias": [
        "festival", "feria", "festival de dia de muertos", "feria local",
        "feria nacional", "festibal", "fiesta", "feria del alebrije", "fest"
    ],
    "Deporte": [
        "partido", "match", "competencia", "juego deportivo", "torneo", 
        "carrera", "maraton", "juego de pelota"
    ],
    "Cursos y Talleres": [
        "curso", "taller", "capacitacion", "manualidades", "curso de acuarela", 
        "taller interactivo", "clase", "formacion"
    ],
    "Infantiles": [
        "niños", "kids", "infantil", "para niños", "familia"
    ],
    "Congresos y Convenciones": [
        "congreso", "convencion", "convención", "convension", "reunion", 
        "simposium", "coloquio", "encuentro"
    ],
    "Eventos Literarios": [
        "lectura", "presentación de libro", "recital literario", 
        "poesía", "poesia"
    ],
    "Recorridos": [
        "tour", "recorrido", "paseo", "visita guiada", "experiencia"
    ]
}

def limpiar_texto(texto):
    if pd.isna(texto): return ""
    texto = str(texto).strip()
    texto = " ".join(texto.split())
    texto = texto.replace("|", "")
    return texto

def limpiar_url(url):
    if pd.isna(url): return ""
    return str(url).strip()

def normalizar_categoria(cat):
    if pd.isna(cat): return ""
    cat_limpia = cat.lower().strip()
    for categoria_normal, palabras in category_map.items():
        for palabra in palabras:
            if palabra in cat_limpia:
                return categoria_normal
    return cat.title()



def normalizar_dataframe(df,actualizar_barra=None):
    log_cambios = []
    total = len(df)

    for i, row in df.iterrows():
        original_title = row.get("title", "")
        original_cat = row.get("category", "")
        original_url = row.get("url", "")
        id_evento = row.get("id", i)

        nuevo_title = limpiar_texto(original_title)
        nuevo_cat = normalizar_categoria(original_cat)
        
        nuevo_url = limpiar_url(original_url)

        if nuevo_title != original_title:
            log_cambios.append([id_evento, "title", original_title, nuevo_title])
        if nuevo_cat != original_cat:
            log_cambios.append([id_evento, "category", original_cat, nuevo_cat])
        if nuevo_url != original_url:
            log_cambios.append([id_evento, "url", original_url, nuevo_url])

        df.at[i, "title"] = nuevo_title
        df.at[i, "category"] = nuevo_cat
        df.at[i, "url"] = nuevo_url
        if actualizar_barra:
            actualizar_barra(int((i + 1) / total * 100))

    log_df = pd.DataFrame(log_cambios, columns=["id", "campo_modificado", "valor_anterior", "valor_nuevo"])
    return df, log_df
