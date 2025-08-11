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
    cur.execute("SELECT * FROM eventos ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def Eliminar_eventos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM eventos WHERE id_evento = %s")
    rows = cur.fetchall()
    cur.close()
    return rows

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
    cur.execute("DELETE FROM eventos WHERE id_evento = %s")
    rows = cur.fetchall()
    cur.close()
    return rows