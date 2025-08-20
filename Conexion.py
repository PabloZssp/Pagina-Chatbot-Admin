import psycopg2


def get_connection():
    return psycopg2.connect(
        'postgres://avnadmin:AVNS_BVDiq3SEleEgX51PwfA@pg-106b1540-pruebaconexionfront.c.aivencloud.com:18155/defaultdb?sslmode=require'
    )



def obtener_eventos():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_BVDiq3SEleEgX51PwfA@pg-106b1540-pruebaconexionfront.c.aivencloud.com:18155/defaultdb?sslmode=require')
    cur = conn.cursor()
    cur.execute("SELECT * FROM eventos ORDER BY id ASC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def obtener_Actividades():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_BVDiq3SEleEgX51PwfA@pg-106b1540-pruebaconexionfront.c.aivencloud.com:18155/defaultdb?sslmode=require')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Actividades ORDER BY id ASC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def obtenerCursos():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_BVDiq3SEleEgX51PwfA@pg-106b1540-pruebaconexionfront.c.aivencloud.com:18155/defaultdb?sslmode=require')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Cursos ORDER BY id ASC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def obtener_Talleres():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_BVDiq3SEleEgX51PwfA@pg-106b1540-pruebaconexionfront.c.aivencloud.com:18155/defaultdb?sslmode=require')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Talleres ORDER BY id ASC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def obtener_columnas(nombre_tabla):
    conn = get_connection()
    cur = conn.cursor()

    # Usar parámetros para evitar inyecciones SQL
    consulta = """
        SELECT COLUMN_NAME
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = %s;
    """
    cur.execute(consulta, (nombre_tabla,))
    columnas = [row[0] for row in cur.fetchall()]
    conn.close()

    # Crear diccionario con nombres como claves y valores iguales
    diccionario = {col: col for col in columnas}
    return diccionario



def obtener_tablas():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public'
        ORDER BY table_name;
    """)
    tablas = [row[0] for row in cur.fetchall()]
    conn.close()

    # Crear diccionario con nombres como claves y valores iguales (puedes personalizar)
    diccionario = {tabla: tabla for tabla in tablas}
    return diccionario



def editar_campo(t_seleccion):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT id FROM {t_seleccion} ORDER BY id")
    ids = [row[0] for row in cur.fetchall()]
    return ids

def obtener_registro_id(id_evento, t_Select):
    TABLAS_PERMITIDAS = ["cursos", "eventos", "actividades","talleres"]
    if t_Select not in TABLAS_PERMITIDAS:
        raise ValueError("Tabla no permitida")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"""
        SELECT Titulo, Recinto, Direccion, Mes, Fechas, Hora, Duracion, Descripcion, Categoria, Costo, URL
        FROM {t_Select} WHERE id = %s
    """, (id_evento,))
    evento = cur.fetchone()
    conn.close()
    return evento


def actualizar_registro(Tabla, id, titulo, recinto, direccion, mes, fechas, hora, duracion, descripcion, categoria, costo, url):
    conn = get_connection()
    cur = conn.cursor()
    
    query = f"""
        UPDATE {Tabla} SET
            Titulo = %s,
            Recinto = %s,
            Direccion = %s,
            Mes = %s,
            Fechas = %s,
            Hora = %s,
            Duracion = %s,
            Descripcion = %s,
            Categoria = %s,
            Costo = %s,
            URL = %s
        WHERE id = %s
    """
    
    valores = (titulo, recinto, direccion, mes, fechas, hora, duracion, descripcion, categoria, costo, url, id)
    cur.execute(query, valores)
    
    conn.commit()
    conn.close()



def Crear_registro(Tabla, title_text, building_name_text, address_text, month_text, dates_text,
                   hora_text, duracion_text, category_text, cost_text, url, description_text):
    conn = get_connection()
    cur = conn.cursor()
    
    query = f"""
        INSERT INTO {Tabla} (
            titulo, recinto, direccion, mes, fechas, hora, duracion, categoria, costo, url, descripcion
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    
    cur.execute(query, (
        title_text, building_name_text, address_text, month_text, dates_text,
        hora_text, duracion_text, category_text, cost_text, url, description_text
    ))
    
    conn.commit()
    cur.close()
    
def Crear_registro2(tabla, valores):
        try:
            # Conexión a la base de datos
            conn = get_connection()
            cursor = conn.cursor()

            # Extraer columnas y valores
            columnas = list(valores.keys())
            datos = list(valores.values())

            # Construir SQL dinámico
            columnas_sql = ", ".join(columnas)
            placeholders = ", ".join(["%s"] * len(columnas))

            query = f"INSERT INTO {tabla} ({columnas_sql}) VALUES ({placeholders})"

            # Ejecutar la consulta
            cursor.execute(query, datos)
            conn.commit()

            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(f"Error al insertar registro: {e}")
            return False
        

        
def eliminar_registro(tabla, id):
    try:
        conn = get_connection()
        cur = conn.cursor()
        query = f"DELETE FROM {tabla} WHERE id = %s"
        cur.execute(query, (id,))
        conn.commit()
        cur.close()
        conn.close()
        
    except Exception as e:
        print(f"Error al eliminar el registro: {e}")



#####################################################################
############### Creacion tablas de ejemplo ##########################
#####################################################################


def crear_tabla_Actividades():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Actividades (
            id SERIAL PRIMARY KEY,
            titulo TEXT,
            recinto TEXT,
            direccion TEXT,
            mes TEXT,
            fechas TEXT,
            hora TEXT,
            duracion TEXT,
            categoria TEXT,
            costo TEXT,
            url TEXT,
            descripcion TEXT
        )
    """)
    conn.commit()
    cur.close()


def crear_tabla_Cursos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Cursos (
            id SERIAL PRIMARY KEY,
            titulo TEXT,
            recinto TEXT,
            direccion TEXT,
            mes TEXT,
            fechas TEXT,
            hora TEXT,
            duracion TEXT,
            categoria TEXT,
            costo TEXT,
            url TEXT,
            descripcion TEXT
        )
    """)
    conn.commit()
    cur.close()




def crear_tabla_Talleres():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Talleres (
            id SERIAL PRIMARY KEY,
            titulo TEXT,
            recinto TEXT,
            direccion TEXT,
            mes TEXT,
            fechas TEXT,
            hora TEXT,
            duracion TEXT,
            categoria TEXT,
            costo TEXT,
            url TEXT,
            descripcion TEXT
        )
    """)
    conn.commit()
    cur.close()

def crear_tablaAdd():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Talleres (
            id SERIAL PRIMARY KEY,
            Nombre TEXT,
            Correo TEXT,
            Fecha de registro TEXT,
            Rol TEXT,
            Estado TEXT,
        )
    """)
    conn.commit()
    cur.close()
    

