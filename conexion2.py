import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

db_url = os.getenv("DATABASE_URL")
print("URL de conexión:", db_url)
engine = create_engine(db_url, echo=True)

try:
    with engine.connect() as connection:
        result = connection.execute("SELECT 1")
        print("✅ Conexión exitosa:", result.scalar() == 1)
except Exception as e:
    print("❌ Error al conectar:", e)