from sqlalchemy import create_engine

# Datos de conexión
usuario = "root"
password = ""
host = "localhost"
puerto = "3306"
database = "terremotos_db"

# Crear conexión
engine = create_engine(
    f"mysql+pymysql://{usuario}:{password}@{host}:{puerto}/{database}")

print("Conexión exitosa a MySQL")
