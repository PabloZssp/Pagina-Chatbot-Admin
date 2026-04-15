import requests
from sshtunnel import SSHTunnelForwarder
import psycopg2
from dotenv import load_dotenv
import os
import logging

# Configuración inicial
logging.getLogger("paramiko.transport").setLevel(logging.CRITICAL)
logging.getLogger("paramiko").setLevel(logging.CRITICAL)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger("DB-SSH")

load_dotenv()

# Credenciales SSH
SSH_HOST = os.getenv('SSH_SERVER')
SSH_PORT = int(os.getenv('SSH_PORT'))
SSH_USER = os.getenv('SSH_USER')
SSH_PASSWORD = os.getenv('SSH_PASSWORD')

# Credenciales de la base de datos
DB_HOST = os.getenv('BD_HOST')
DB_PORT = int(os.getenv('BD_PORT'))
DB_NAME = os.getenv('BD_NAME')
DB_USER = os.getenv('BD_USER')
DB_PASSWORD = os.getenv('BD_PASSWORD')


def connect_db():
    """Establece conexión a PostgreSQL a través de túnel SSH y devuelve el cursor y la conexión."""
    try:
        logger.info("Estableciendo túnel SSH...")
        tunnel = SSHTunnelForwarder(
            (SSH_HOST, SSH_PORT),
            ssh_username=SSH_USER,
            ssh_password=SSH_PASSWORD,
            remote_bind_address=(DB_HOST, DB_PORT)
        )
        tunnel.start()
        logger.info(f"Túnel SSH activo en puerto local: {tunnel.local_bind_port}")

        conn = psycopg2.connect(
            host='127.0.0.1',
            port=tunnel.local_bind_port,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        logger.info("Conexión exitosa a la base de datos.")
        return conn, tunnel

    except Exception as e:
        logger.error("Error al conectar:", e)
        return None, None


def close_db(conn, tunnel):
    """Cierra la conexión y el túnel SSH."""
    try:
        if conn:
            conn.close()
            logger.info("Conexión cerrada correctamente.")
        if tunnel and tunnel.is_active:
            tunnel.stop()
            logger.info("Túnel SSH cerrado correctamente.")
    except Exception as e:
        logger.error("Error al cerrar conexión:", e)



def obtener_tablas():
    """Obtiene todas las tablas del esquema 'public' usando la conexión SSH."""
    conn, tunnel = connect_db()
    tablas = {}

    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)
            tablas = {row[0]: row[0] for row in cur.fetchall()}
            logger.info(f"Se encontraron {len(tablas)} tablas.")
        except Exception as e:
            logger.error("Error al obtener tablas:", e)
        finally:
            cur.close()
            close_db(conn, tunnel)

    return tablas

def obtener_campos(tabla):
    """Devuelve un diccionario {columna: columna} de la tabla indicada."""
    conn, tunnel = connect_db()
    columnas = {}

    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'public'
                AND table_name = %s
                ORDER BY ordinal_position;
            """, (tabla,))
            columnas = {row[0]: row[0] for row in cur.fetchall()}
            logger.info(f"Se encontraron {len(columnas)} columnas en la tabla {tabla}.")
        except Exception as e:
            logger.error("Error al obtener columnas:", e)
        finally:
            cur.close()
            close_db(conn, tunnel)

    return columnas

def obtener_eventos(tabla):
    """Devuelve todas las filas de la tabla indicada, ordenadas por id ASC."""
    conn, tunnel = connect_db()
    rows = []

    if conn:
        try:
            cur = conn.cursor()
            query = f"SELECT * FROM {tabla} ORDER BY id ASC"
            cur.execute(query)
            rows = cur.fetchall()
            logger.info(f"Se obtuvieron {len(rows)} registros de la tabla {tabla}.")
        except Exception as e:
            logger.error(f"Error al obtener eventos: {e}")

        finally:
            cur.close()
            close_db(conn, tunnel)

    return rows
def editar_campo(tabla):
    """Devuelve una lista de IDs disponibles en la tabla indicada."""
    conn, tunnel = connect_db()
    ids = []

    if conn:
        try:
            cur = conn.cursor()
            query = f"SELECT id FROM {tabla} ORDER BY id ASC"
            cur.execute(query)
            ids = [row[0] for row in cur.fetchall()]
            logger.info(f"Se encontraron {len(ids)} IDs en la tabla {tabla}.")
        except Exception as e:
            logger.error("Error al obtener IDs:", e)
        finally:
            cur.close()
            close_db(conn, tunnel)

    return ids
def obtener_registro_id(id_seleccionado, tabla, campos):
    """Devuelve el registro completo para el ID seleccionado en la tabla indicada."""
    conn, tunnel = connect_db()
    registro = None

    if conn:
        try:
            cur = conn.cursor()
            query = f"SELECT {', '.join(campos)} FROM {tabla} WHERE id = %s"
            cur.execute(query, (id_seleccionado,))
            registro = cur.fetchone()
            logger.info(f"Registro obtenido para ID {id_seleccionado} en la tabla {tabla}.")
        except Exception as e:
            logger.error("Error al obtener registro por ID:", e)
        finally:
            cur.close()
            close_db(conn, tunnel)

    return registro


def actualizar_registro(tabla, id_seleccionado, valores):
    """Actualiza todos los campos de un registro en la tabla indicada."""
    conn, tunnel = connect_db()
    success = False

    if conn:
        try:
            cur = conn.cursor()
            columnas = [c for c in valores.keys() if not (c.lower() == "id" or c.lower().startswith("id_"))] 
            set_clause = ", ".join([f"{col} = %s" for col in columnas])
            query = f"UPDATE {tabla} SET {set_clause} WHERE id = %s"

            
            params = [valores[c] for c in columnas] + [id_seleccionado]

            cur.execute(query, tuple(params))
            conn.commit()
            success = True
            logger.info(f"Registro {id_seleccionado} actualizado en {tabla} con valores {valores}.")
        except Exception as e:
            logger.error(f"Error al actualizar registro: {e}")
        finally:
            cur.close()
            close_db(conn, tunnel)

    return success

def crear_registro(tabla, campos, valores):
    """Crea un nuevo registro en la tabla indicada con los campos y valores proporcionados."""
    conn, tunnel = connect_db()
    success = False

    if conn:
        try:
            cur = conn.cursor()

            columnas = [c for c in campos if not (c.lower() == "id" or c.lower().startswith("id_"))]

            placeholders = ", ".join(["%s"] * len(columnas))

            query = f"INSERT INTO {tabla} ({', '.join(columnas)}) VALUES ({placeholders})"

            valores_finales = [valores[c] for c in columnas]

            cur.execute(query, tuple(valores_finales))
            conn.commit()
            success = True
            logger.info(f"Nuevo registro creado en la tabla {tabla} con valores {valores_finales}.")
        except Exception as e:
            logger.error(f"Error al crear registro: {e}")
        finally:
            cur.close()
            close_db(conn, tunnel)

    return success



