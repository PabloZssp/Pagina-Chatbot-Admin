import psycopg2


def Conectar_BD():
    conn = psycopg2.connect('postgres://avnadmin:AVNS_BVDiq3SEleEgX51PwfA@pg-106b1540-pruebaconexionfront.c.aivencloud.com:18155/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


def get_connection():
    return psycopg2.connect(
        'postgres://avnadmin:AVNS_BVDiq3SEleEgX51PwfA@pg-106b1540-pruebaconexionfront.c.aivencloud.com:18155/defaultdb?sslmode=require'
    )

def get_version():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT VERSION()")
    version = cur.fetchone()[0]
    cur.close()
    return version

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

# eventos = cnx.obtener_eventos()

 #       if eventos:
  #          df_eventos = pd.DataFrame(eventos, columns=[
   #             "ID", "Título", "Recinto", "Dirección", "Mes", "Fechas",
    #            "Hora", "Duración", "Categoría", "Costo", "URL", "Descripción"
     #       ])
      #      st.subheader(" Registros guardados")
       #     st.dataframe(df_eventos, use_container_width=True)

def editar_campo():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM eventos ORDER BY id")
    ids = [row[0] for row in cur.fetchall()]
    return ids


def obtener_registro_id(id_evento):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Titulo, Recinto, Direccion, Mes, Fechas, Hora, Duracion, Descripcion, Categoria, Costo, URL
        FROM eventos WHERE id = %s
    """, (id_evento,))
    evento = cur.fetchone()
    conn.close()
    return evento

def actualizar_registro(id, titulo, recinto, direccion, mes, fechas, hora, duracion, descripcion, categoria, costo, url):
    conn = get_connection()
    cur = conn.cursor()
    
    query = """
        UPDATE eventos SET
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


