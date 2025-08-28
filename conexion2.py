from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()

# Obtener las variables
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAMEU = os.getenv("DB_NAMEU")
DB_NAMEC = os.getenv("DB_NAMEC")
DB_NAMET = os.getenv("DB_NAMET")


DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAMEU}"
DATABASE_URL2 = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAMEC}"
DATABASE_URL3 = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAMET}"



engine = create_engine(DATABASE_URL)
engine2 = create_engine(DATABASE_URL2)
engine3 = create_engine(DATABASE_URL3)




#usuarios conexion 
DB_USER2 = os.getenv("DB_USER2")
DB_PASSWORD2 = os.getenv("DB_PASSWORD2")
DB_HOST2 = os.getenv("DB_HOST2")
DB_PORT2 = os.getenv("DB_PORT2")
DB_NAME2 = os.getenv("DB_NAME2")

DATABASE_URL4 = f"postgresql+psycopg2://{DB_USER2}:{DB_PASSWORD2}@{DB_HOST2}:{DB_PORT2}/{DB_NAME2}"

engine4 = create_engine(DATABASE_URL4)
    
def obtener_eventos(tabla):
    query = f"SELECT * FROM {tabla} ORDER BY id ASC"
    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
    return rows


def editar_campo(t_seleccion):
    query = text(f"SELECT id FROM {t_seleccion} ORDER BY id")
    with engine.connect() as conn:
        result = conn.execute(query)
        ids = [row[0] for row in result.fetchall()]
    return ids


def crear_registro(tabla, valores):
    if not tabla or not valores:
        raise ValueError("Tabla y valores no pueden estar vacíos.")

    columnas = list(valores.keys())
    columnas_sql = ", ".join(columnas)
    placeholders = ", ".join([f":{col}" for col in columnas])  # Usar :nombre para SQLAlchemy

    query = text(f"INSERT INTO {tabla} ({columnas_sql}) VALUES ({placeholders})")

    try:
        with engine.begin() as conn:
            conn.execute(query, valores)  # valores es un dict
    except Exception as e:
        print(f"Error al insertar registro: {e}")

        


def obtener_registro_id(id_evento, t_Select, campos):
    columnas = ", ".join(campos)  # convierte la lista en texto SQL válido

    query = text(f"""
        SELECT {columnas}
        FROM {t_Select} WHERE id = :id_evento
    """)

    with engine.connect() as conn:
        result = conn.execute(query, {"id_evento": id_evento})
        evento = result.fetchone()

    return evento

def actualizar_registro(tabla, id_registro, nuevos_valores):
    set_clause = ", ".join([f"{campo} = :{campo}" for campo in nuevos_valores])
    query = text(f"UPDATE {tabla} SET {set_clause} WHERE id = :id")

    nuevos_valores["id"] = id_registro

    with engine.connect() as conn:
        conn.execute(query, nuevos_valores)
        conn.commit()

def obtener_tablas():
    query = text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)
    with engine.connect() as conn:
        tablas = [row[0] for row in conn.execute(query)]
    return {tabla: tabla for tabla in tablas}

def obtener_campos(tabla):
    """Devuelve un diccionario {columna: columna} de la tabla indicada."""
    query = text("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'public'
        AND table_name = :tabla
        ORDER BY ordinal_position;
    """)
    with engine.connect() as conn:
        columnas = [row[0] for row in conn.execute(query, {"tabla": tabla})]
    return {col: col for col in columnas}



def eliminar_campo(tabla, id):
    query = text(f"DELETE FROM {tabla} WHERE id = :id")
    with engine.connect() as conn:
        trans = conn.begin()
        try:
            conn.execute(query, {'id': id})
            trans.commit()
        except Exception as e:
            trans.rollback()
            print(f"Error al eliminar el registro: {e}")

###################################################################
def obtener_eventos2(tabla):
    query = f"SELECT * FROM {tabla} ORDER BY id ASC"
    with engine2.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
    return rows


def editar_campo2(t_seleccion):
    query = text(f"SELECT id FROM {t_seleccion} ORDER BY id")
    with engine2.connect() as conn:
        result = conn.execute(query)
        ids = [row[0] for row in result.fetchall()]
    return ids


def crear_registro2(tabla, valores):
    if not tabla or not valores:
        raise ValueError("Tabla y valores no pueden estar vacíos.")

    columnas = list(valores.keys())
    columnas_sql = ", ".join(columnas)
    placeholders = ", ".join([f":{col}" for col in columnas])  # Usar :nombre para SQLAlchemy

    query = text(f"INSERT INTO {tabla} ({columnas_sql}) VALUES ({placeholders})")

    try:
        with engine2.begin() as conn:
            conn.execute(query, valores)  # valores es un dict
    except Exception as e:
        print(f"Error al insertar registro: {e}")

def obtener_registro_id2(id_evento, t_Select, campos):
    columnas = ", ".join(campos)  # convierte la lista en texto SQL válido

    query = text(f"""
        SELECT {columnas}
        FROM {t_Select} WHERE id = :id_evento
    """)

    with engine2.connect() as conn:
        result = conn.execute(query, {"id_evento": id_evento})
        evento = result.fetchone()

    return evento

def actualizar_registro2(tabla, id_registro, nuevos_valores):
    set_clause = ", ".join([f"{campo} = :{campo}" for campo in nuevos_valores])
    query = text(f"UPDATE {tabla} SET {set_clause} WHERE id = :id")

    nuevos_valores["id"] = id_registro

    with engine2.connect() as conn:
        conn.execute(query, nuevos_valores)
        conn.commit()

def obtener_tablas2():
    query = text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)
    with engine2.connect() as conn:
        tablas = [row[0] for row in conn.execute(query)]
    return {tabla: tabla for tabla in tablas}

def obtener_campos2(tabla):
    """Devuelve un diccionario {columna: columna} de la tabla indicada."""
    query = text("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'public'
        AND table_name = :tabla
        ORDER BY ordinal_position;
    """)
    with engine2.connect() as conn:
        columnas = [row[0] for row in conn.execute(query, {"tabla": tabla})]
    return {col: col for col in columnas}



def eliminar_campo2(tabla, id):
    query = text(f"DELETE FROM {tabla} WHERE id = :id")
    with engine2.connect() as conn:
        trans = conn.begin()
        try:
            conn.execute(query, {'id': id})
            trans.commit()
        except Exception as e:
            trans.rollback()
            print(f"Error al eliminar el registro: {e}")

#################################################################


def obtener_eventos3(tabla):
    campos_id = {
        'Arte_publico_monumentos': 'id_monumento',
        'Bibliotecas_archivos':'id_biblioteca',
        'Barrios_colonias': 'id_barrios',
        'Centros_culturales': 'id_centro',
        'Edificios_historicos':'id_edificio',
        'Embajadas': 'id_embajada',
        'Estaciones_de_metro': 'id_estacion',
        'Galerias_de_arte':'id_galeria',
        'Gran_aforo': 'id_aforo',
        'Hoteles': 'id_hotel',
        'Iglecias_catedrales':'id_iglecia',
        'Ir_de_compras': 'id_plaza_comer',
        'Mercados': 'id_mercado',
        'Miradores':'id_mirador',
        'Museos': 'id_museo',
        'Parques_plazas_publicas': 'id_parque',
        'Restaurantes':'id_rest',
        'sitios_arqueologico': 'id_sitio',
        'cat_hotel_estrellas': 'id_estrella',
        'cat_restaurantes_estrellas':'id_estrella',
        
    }

    nombre_id = campos_id.get(tabla)
    if not nombre_id:
        raise ValueError(f"No se encontró campo ID para la tabla '{tabla}'")

    query = text(f'SELECT * FROM categorias."{tabla}" ORDER BY {nombre_id} ASC')

    with engine3.connect() as conn:
        result = conn.execute(query)
        rows = result.fetchall()

    return rows


def editar_campo3(t_seleccion):
    campos_id = {
        'Arte_publico_monumentos': 'id_monumento',
        'Bibliotecas_archivos':'id_biblioteca',
        'Barrios_colonias': 'id_barrios',
        'Centros_culturales': 'id_centro',
        'Edificios_historicos':'id_edificio',
        'Embajadas': 'id_embajada',
        'Estaciones_de_metro': 'id_estacion',
        'Galerias_de_arte':'id_galeria',
        'Gran_aforo': 'id_aforo',
        'Hoteles': 'id_hotel',
        'Iglecias_catedrales':'id_iglecia',
        'Ir_de_compras': 'id_plaza_comer',
        'Mercados': 'id_mercado',
        'Miradores':'id_mirador',
        'Museos': 'id_museo',
        'Parques_plazas_publicas': 'id_parque',
        'Restaurantes':'id_rest',
        'sitios_arqueologico': 'id_sitio',
        'cat_hotel_estrellas': 'id_estrella',
        'cat_restaurantes_estrellas':'id_estrella',
        
    }

    
    campo_id = campos_id.get(t_seleccion)
    if not campo_id:
        raise ValueError(f"No se encontró campo ID para la tabla '{t_seleccion}'")

    query = text(f'SELECT {campo_id} FROM categorias."{t_seleccion}" ORDER BY {campo_id}')
    with engine3.connect() as conn:
        result = conn.execute(query)
        ids = [row[0] for row in result.fetchall()]
    return ids


def crear_registro3(tabla, valores):
    if not tabla or not valores:
        raise ValueError("Tabla y valores no pueden estar vacíos.")

    
    tabla_sql = f'"{tabla}"' if not tabla.islower() else tabla

    columnas = list(valores.keys())

    
    columnas_sql = ", ".join([f'"{col}"' for col in columnas])
    placeholders = ", ".join([f":{col}" for col in columnas])

    query = text(f"""
        INSERT INTO categorias.{tabla_sql} ({columnas_sql})
        VALUES ({placeholders})
    """)

    try:
        with engine3.begin() as conn:
            conn.execute(query, valores)
    except Exception as e:
        print(f" Error al insertar registro en '{tabla}': {e}")


def obtener_registro_id3(id_evento, t_Select, campos):
    campos_id = {
        'Arte_publico_monumentos': 'id_monumento',
        'Bibliotecas_archivos': 'id_biblioteca',
        'Barrios_colonias': 'id_barrios',
        'Centros_culturales': 'id_centro',
        'Edificios_historicos': 'id_edificio',
        'Embajadas': 'id_embajada',
        'Estaciones_de_metro': 'id_estacion',
        'Galerias_de_arte': 'id_galeria',
        'Gran_aforo': 'id_aforo',
        'Hoteles': 'id_hotel',
        'Iglecias_catedrales': 'id_iglecia',
        'Ir_de_compras': 'id_plaza_comer',
        'Mercados': 'id_mercado',
        'Miradores': 'id_mirador',
        'Museos': 'id_museo',
        'Parques_plazas_publicas': 'id_parque',
        'Restaurantes': 'id_rest',
        'sitios_arqueologico': 'id_sitio',
        'cat_hotel_estrellas': 'id_estrella',
        'cat_restaurantes_estrellas': 'id_estrella',
    }

    columna_id = campos_id.get(t_Select)
    if not columna_id:
        raise ValueError(f"No se encontró columna ID para la tabla '{t_Select}'")

    
    columnas_sql = ", ".join([f'"{col}"' if not col.islower() else col for col in campos])

    query = text(f"""
        SELECT {columnas_sql}
        FROM categorias."{t_Select}"
        WHERE {columna_id} = :id_evento
    """)

    with engine3.connect() as conn:
        result = conn.execute(query, {"id_evento": id_evento})
        evento = result.fetchone()

    return evento



def actualizar_registro3(tabla, id_registro, nuevos_valores):
    campos_id = {
        'Arte_publico_monumentos': 'id_monumento',
        'Bibliotecas_archivos': 'id_biblioteca',
        'Barrios_colonias': 'id_barrios',
        'Centros_culturales': 'id_centro',
        'Edificios_historicos': 'id_edificio',
        'Embajadas': 'id_embajada',
        'Estaciones_de_metro': 'id_estacion',
        'Galerias_de_arte': 'id_galeria',
        'Gran_aforo': 'id_aforo',
        'Hoteles': 'id_hotel',
        'Iglecias_catedrales': 'id_iglecia',
        'Ir_de_compras': 'id_plaza_comer',
        'Mercados': 'id_mercado',
        'Miradores': 'id_mirador',
        'Museos': 'id_museo',
        'Parques_plazas_publicas': 'id_parque',
        'Restaurantes': 'id_rest',
        'sitios_arqueologico': 'id_sitio',
        'cat_hotel_estrellas': 'id_estrella',
        'cat_restaurantes_estrellas': 'id_estrella',
    }

    columna_id = campos_id.get(tabla)
    if not columna_id:
        raise ValueError(f"No se encontró columna ID para la tabla '{tabla}'")

    
    set_clause = ", ".join([f'"{campo}" = :{campo}' for campo in nuevos_valores])

    query = text(f"""
    UPDATE "categorias"."{tabla}"
    SET {set_clause}
    WHERE "{columna_id}" = :id_registro;
      """)


    nuevos_valores["id_registro"] = id_registro

    with engine3.connect() as conn:
        conn.execute(query, {"id_registro":id_registro},nuevos_valores)
        conn.commit()



def obtener_tablas3():
    query = text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'categorias'
        ORDER BY table_name;
    """)
    with engine3.connect() as conn:
        tablas = [row[0] for row in conn.execute(query)]
    return {tabla: tabla for tabla in tablas}



def obtener_campos3(tabla):
    query = text(f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'categorias'
        AND table_name = '{tabla}'
        ORDER BY ordinal_position;
    """)
    with engine3.connect() as conn:
        columnas = [row[0] for row in conn.execute(query)]
    return {col: col for col in columnas}




def eliminar_campo3(tabla, id):
    campos_id = {
        'Arte_publico_monumentos': 'id_monumento',
        'Bibliotecas_archivos': 'id_biblioteca',
        'Barrios_colonias': 'id_barrios',
        'Centros_culturales': 'id_centro',
        'Edificios_historicos': 'id_edificio',
        'Embajadas': 'id_embajada',
        'Estaciones_de_metro': 'id_estacion',
        'Galerias_de_arte': 'id_galeria',
        'Gran_aforo': 'id_aforo',
        'Hoteles': 'id_hotel',
        'Iglecias_catedrales': 'id_iglecia',
        'Ir_de_compras': 'id_plaza_comer',
        'Mercados': 'id_mercado',
        'Miradores': 'id_mirador',
        'Museos': 'id_museo',
        'Parques_plazas_publicas': 'id_parque',
        'Restaurantes': 'id_rest',
        'sitios_arqueologico': 'id_sitio',
        'cat_hotel_estrellas': 'id_estrella',
        'cat_restaurantes_estrellas': 'id_estrella',
    }

    columna_id = campos_id.get(tabla)
    if not columna_id:
        raise ValueError(f"No se encontró columna ID para la tabla '{tabla}'")

    query = text(f"""DELETE FROM "categorias"."{tabla}"
                  WHERE "{columna_id}" = :id""")
    with engine3.connect() as conn:
        trans = conn.begin()
        try:
            conn.execute(query, {'id': id})
            trans.commit()
        except Exception as e:
            trans.rollback()
            print(f"Error al eliminar el registro: {e}")

###########Conexion users###############

def obtener_tablas4():
    query = text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'herramientas'
        ORDER BY table_name;
    """)
    with engine4.connect() as conn:
        tablas = [row[0] for row in conn.execute(query)]
    return {tabla: tabla for tabla in tablas}

def obtener_eventos4(tabla):
    query = text(f"SELECT * FROM herramientas.{tabla} ORDER BY id ASC")
    with engine4.connect() as conn:
        result = conn.execute(query)  
        rows = result.fetchall()
    return rows

def obtener_campos4(tabla):
    query = text(f"""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'herramientas'
        AND table_name = '{tabla}'
        ORDER BY ordinal_position;
    """)
    with engine4.connect() as conn:
        columnas = [row[0] for row in conn.execute(query)]
    return {col: col for col in columnas}

def validar_usuario(usuario, password):
   
    query = text("""
        SELECT username, role
        FROM herramientas.usuarios
        WHERE username = :u AND password = :p
    """)
    with engine4.connect() as conn:
        result = conn.execute(query, {"u": usuario, "p": password}).fetchone()
        return result