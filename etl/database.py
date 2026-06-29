from dotenv import load_dotenv
import os

from sqlalchemy import create_engine

# Cargar variables del archivo .env
load_dotenv()

# Datos de conexión
usuario = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = os.getenv("DB_PORT")
database = os.getenv("DB_NAME")

# Crear conexión
engine = create_engine(
    f"mysql+pymysql://{usuario}:{password}@{host}:{puerto}/{database}")

print("Conexión exitosa a MySQL")
