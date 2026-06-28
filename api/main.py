from fastapi import FastAPI
from sqlalchemy import create_engine, text
import pandas as pd

app = FastAPI(title="API de Terremotos")

engine = create_engine(
    "mysql+pymysql://root:@localhost:3306/terremotos_db"
)


@app.get("/")
def inicio():
    return {"mensaje": "API de terremotos funcionando"}


@app.get("/terremotos")
def obtener_terremotos():
    query = "SELECT * FROM terremotos LIMIT 100"
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")


@app.get("/terremotos/top")
def terremotos_mas_fuertes():
    query = """
    SELECT country, place, mag, depth, categoria_magnitud, categoria_profundidad
    FROM terremotos
    ORDER BY mag DESC
    LIMIT 10
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")


@app.get("/terremotos/resumen")
def resumen():
    query = """
    SELECT 
        COUNT(*) AS total_eventos,
        ROUND(AVG(mag), 2) AS magnitud_promedio,
        ROUND(MAX(mag), 2) AS magnitud_maxima,
        ROUND(AVG(depth), 2) AS profundidad_promedio
    FROM terremotos
    """
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")[0]
