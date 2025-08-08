from typing import  Optional
from sqlmodel import Field, SQLModel,Column, create_engine, Session, select
from datetime import datetime
import pandas as pd
from configparser import ConfigParser
from sqlalchemy import BigInteger, Text
import streamlit as st

if not hasattr(SQLModel.metadata, "_tables_defined"):
        class EventoBase(SQLModel):
            titulo: Optional[str] = Field(default=None, max_length=255)
            recinto: Optional[str] = Field(default=None, max_length=255)
            direccion: Optional[str] = Field(default=None, max_length=255)
            mes: Optional[str] = Field(default=None, max_length=50)
            fechas: Optional[str] = Field(default=None, max_length=100)
            hora: Optional[str] = Field(default=None, max_length=50)
            duracion: Optional[str] = Field(default=None, max_length=50)
            categoria: Optional[str] = Field(default=None, max_length=100)
            costo: Optional[str] = Field(default=None, max_length=100)
            url: Optional[str] = Field(default=None, max_length=500)
            descripcion: Optional[str] = Field(default=None, sa_type=Text)

        class Evento(EventoBase, table=True):
            """
            SQLModel class for the 'eventos' table.
            """
            __tablename__ = "eventos"
            id: Optional[int] = Field(
                default=None,
            #  primary_key=True,
                sa_column=Column(BigInteger, primary_key=True) # Ensure BigInteger for 'id'
            )


        class Actividad(EventoBase, table=True):
            """
            SQLModel class for the 'actividades' table.
            """
            __tablename__ = "actividades"
            id: Optional[int] = Field(
                default=None,
                #primary_key=True,
                sa_column=Column(BigInteger, primary_key=True)
            )


        class Curso(EventoBase, table=True):
            """
            SQLModel class for the 'cursos' table.
            """
            __tablename__ = "cursos"
            id: Optional[int] = Field(
                default=None,
                #primary_key=True,
                sa_column=Column(BigInteger, primary_key=True)
            )


        class Taller(EventoBase, table=True):
            """
            SQLModel class for the 'talleres' table.
            """
            __tablename__ = "talleres"
            id: Optional[int] = Field(
                default=None,
            # primary_key=True,
                sa_column=Column(BigInteger, primary_key=True)
            )

@st.cache_resource
def get_engine():
    """
    Carga la configuración y crea el motor de la base de datos.
    """
    config = ConfigParser()
    try:
        # La ruta del config.ini es relativa al directorio raíz de la app Streamlit
        # Si este archivo 'db_models.py' está en el mismo directorio que tu app.py,
        # y config.ini está en .streamlit/config.ini, la ruta debería ser correcta.
        config.read('.streamlit/config.ini')
        usser = config["Postgres"]["Usuario"]
        password = config["Postgres"]["password"]
        server = config["Postgres"]["Host"]
        database = config["Postgres"]["nombre_bd"]
        port = config.getint("Postgres", "puerto")
        
        db_url = f'postgresql+psycopg2://{usser}:{password}@{server}:{port}/{database}'
        engine = create_engine(db_url, echo=False)
        return engine
    except Exception as e:
        st.error(f"Error al cargar la configuración o crear el engine de la base de datos: {e}")
        st.stop() # Detiene la ejecución de la app si la DB no se conecta
        return None

ENGINE = get_engine() # Asignamos el engine a una variable global para fácil acceso

def create_db_and_tables():
    """Crea todas las tablas definidas por los modelos SQLModel en la base de datos."""
    if ENGINE:
        try:
            SQLModel.metadata.create_all(ENGINE)
            st.success("Tablas de la base de datos creadas/aseguradas con éxito.")
        except Exception as e:
            st.error(f"Error al crear las tablas: {e}")
    else:
        st.warning("Motor de base de datos no disponible para crear tablas.")

def get_session():
    """
    Genera una sesión de la base de datos para usar con un bloque 'with'.
    """
    if ENGINE:
        with Session(ENGINE) as session:
            yield session
    else:
        st.error("No se pudo obtener una sesión; el motor de la base de datos no está inicializado.")
        # Podrías lanzar una excepción o manejarlo de otra forma.

def sqlmodel_to_dataframe(objs: list[SQLModel]) -> pd.DataFrame:
    """Convierte una lista de objetos SQLModel a un DataFrame de pandas."""
    if not objs:
        return pd.DataFrame()
    recordable = [i.model_dump() for i in objs]
    df = pd.DataFrame(recordable)
    return df

def fetch_eventos() -> pd.DataFrame:
    """Recupera todos los eventos de la base de datos."""
    with next(get_session()) as session:
        statement = select(Evento)
        eventos = session.exec(statement).all()
        return sqlmodel_to_dataframe(eventos)

def fetch_actividades() -> pd.DataFrame:
    """Recupera todas las actividades de la base de datos."""
    with next(get_session()) as session:
        statement = select(Actividad)
        actividades = session.exec(statement).all()
        return sqlmodel_to_dataframe(actividades)

def fetch_cursos() -> pd.DataFrame:
    """Recupera todos los cursos de la base de datos."""
    with next(get_session()) as session:
        statement = select(Curso)
        cursos = session.exec(statement).all()
        return sqlmodel_to_dataframe(cursos)

def fetch_talleres() -> pd.DataFrame:
    """Recupera todos los talleres de la base de datos."""
    with next(get_session()) as session:
        statement = select(Taller)
        talleres = session.exec(statement).all()
        return sqlmodel_to_dataframe(talleres)