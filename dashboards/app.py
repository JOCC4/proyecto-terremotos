import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title="Dashboard Terremotos", layout="wide")

engine = create_engine("mysql+pymysql://root:@localhost:3306/terremotos_db")

df = pd.read_sql("SELECT * FROM terremotos", engine)

st.title("Dashboard de Análisis de Terremotos")

col1, col2, col3 = st.columns(3)

col1.metric("Total eventos", len(df))
col2.metric("Magnitud máxima", df["mag"].max())
col3.metric("Magnitud promedio", round(df["mag"].mean(), 2))

st.subheader("Terremotos por categoría de magnitud")
fig1 = px.histogram(df, x="categoria_magnitud", color="categoria_magnitud")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Magnitud promedio por país")
df_pais = df.groupby("country")["mag"].mean().reset_index(
).sort_values("mag", ascending=False).head(10)
fig2 = px.bar(df_pais, x="country", y="mag")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Relación entre profundidad y magnitud")
fig3 = px.scatter(
    df,
    x="depth",
    y="mag",
    color="categoria_profundidad",
    hover_data=["country", "place"]
)
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Datos")
st.dataframe(df.head(100))
