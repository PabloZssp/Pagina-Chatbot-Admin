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

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)


def obtener_Datoss():
    """Obtiene todos los eventos ordenados por ID usando SQLAlchemy."""
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM eventos ORDER BY id ASC"))
        return result.fetchall()
    

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
