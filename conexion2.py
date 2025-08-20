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
DB_NAME = os.getenv("DB_NAME")

# Crear la URL de conexión
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
DATABASE_URL2 = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/chatbot_turismo"
# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)
engine2 = create_engine(DATABASE_URL2) 

def obtener_Datoss():
   
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM eventos ORDER BY id ASC"))
        return result.fetchall()
    
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

from sqlalchemy import text

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
###################################################################

def obtener_Datoss2():
   
    with engine2.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM eventos ORDER BY id ASC"))
        return result.fetchall()
    
def obtener_eventos2(tabla):
    query = f"SELECT * FROM {tabla} ORDER BY id ASC"
    with engine2.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
    return rows


from sqlalchemy import create_engine, text



def obtener_tablas2():
    query = text("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'categorias'
        ORDER BY table_name;
    """)
    with engine2.connect() as conn:
        result = conn.execute(query)
        tablas = [row[0] for row in result]
    
    # Devuelve un diccionario tipo {'tabla1': 'tabla1', 'tabla2': 'tabla2'}
    return {nombre: nombre for nombre in tablas}


def obtener_campos2(tabla):
    """Devuelve un diccionario {columna: columna} de la tabla indicada."""
    query = text("""
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = 'categorias'
        AND table_name = :tabla
        ORDER BY ordinal_position;
    """)
    with engine2.connect() as conn:
        columnas = [row[0] for row in conn.execute(query, {"tabla": tabla})]
    return {col: col for col in columnas}