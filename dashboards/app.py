import os

import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title="Dashboard Terremotos", layout="wide")

# =========================
# CONFIGURACIÓN BD
# =========================

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "terremotos_db")

engine = create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# =========================
# CARGA DE DATOS
# =========================

df = pd.read_sql("SELECT * FROM terremotos", engine)

df_api = None

if os.path.exists("data/raw/terremotos_api.csv"):
    df_api = pd.read_csv("data/raw/terremotos_api.csv")

# =========================
# TÍTULO
# =========================

st.title("Dashboard de Análisis de Terremotos")

st.markdown("""
Este sistema integra datos históricos de terremotos,
datos en tiempo real desde la API pública USGS
y visualización analítica mediante Streamlit.
""")

# =========================
# ESTADO DE FUENTES
# =========================

st.subheader("Estado de fuentes de datos")

col_fuente1, col_fuente2, col_fuente3 = st.columns(3)

col_fuente1.success("CSV histórico cargado")
col_fuente2.success("Base de datos MySQL conectada")
col_fuente3.success("API pública USGS integrada")

st.info(f"Base de datos conectada: {DB_NAME}")

st.subheader("Pipeline ETL")

st.markdown("""
1. **Extract** → extracción de datos históricos CSV y datos en tiempo real desde API USGS.  
2. **Transform** → limpieza, categorización y normalización de variables sísmicas.  
3. **Load** → carga de datos procesados en MySQL para análisis y visualización.  
""")

# =========================
# FILTROS
# =========================

st.sidebar.title("Filtros")

categorias = st.sidebar.multiselect(
    "Categoría de magnitud",
    options=df["categoria_magnitud"].unique(),
    default=df["categoria_magnitud"].unique()
)

paises = st.sidebar.multiselect(
    "País",
    options=sorted(df["country"].unique()),
    default=sorted(df["country"].unique())
)

df_filtrado = df[
    (df["categoria_magnitud"].isin(categorias)) &
    (df["country"].isin(paises))
]

# =========================
# VISTA EJECUTIVA
# =========================

st.subheader("Vista ejecutiva")

col1, col2, col3 = st.columns(3)

col1.metric("Total eventos históricos", len(df_filtrado))
col2.metric("Magnitud máxima histórica", df_filtrado["mag"].max())
col3.metric("Magnitud promedio histórica", round(df_filtrado["mag"].mean(), 2))

st.divider()

col4, col5, col6 = st.columns(3)

col4.metric("Profundidad promedio", round(df_filtrado["depth"].mean(), 2))
col5.metric("Cantidad de países", df_filtrado["country"].nunique())
col6.metric("Categoría más frecuente",
            df_filtrado["categoria_magnitud"].mode()[0])

# =========================
# VISTA OPERATIVA
# =========================

st.subheader("Vista operativa: terremotos por categoría de magnitud")

fig1 = px.histogram(
    df_filtrado,
    x="categoria_magnitud",
    color="categoria_magnitud"
)

st.plotly_chart(fig1, use_container_width=True)

st.subheader("Vista operativa: magnitud promedio por país")

df_pais = (
    df_filtrado
    .groupby("country")["mag"]
    .mean()
    .reset_index()
    .sort_values("mag", ascending=False)
    .head(10)
)

fig2 = px.bar(
    df_pais,
    x="country",
    y="mag",
    color="mag"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# VISTA TÉCNICA
# =========================

st.subheader("Vista técnica: relación entre profundidad y magnitud")

fig3 = px.scatter(
    df_filtrado,
    x="depth",
    y="mag",
    color="categoria_profundidad",
    hover_data=["country", "place"]
)

st.plotly_chart(fig3, use_container_width=True)

# =========================
# API USGS
# =========================

st.subheader("Evidencia de integración con API pública USGS")

st.markdown("Fuente oficial: https://earthquake.usgs.gov/")

if df_api is not None:

    col_api1, col_api2 = st.columns(2)

    col_api1.metric("Eventos obtenidos desde API", len(df_api))
    col_api2.metric("Magnitud máxima API", round(df_api["mag"].max(), 2))

    st.write("Muestra de datos consumidos desde la API:")

    st.dataframe(df_api.head(10))

else:
    st.warning("No se encontró el archivo data/raw/terremotos_api.csv")

# =========================
# DATOS HISTÓRICOS
# =========================

st.subheader("Datos históricos filtrados desde MySQL")

st.dataframe(df_filtrado.head(100))
