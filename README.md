# Proyecto Terremotos

Proyecto end-to-end de análisis de datos sísmicos usando Python, MySQL, FastAPI, Streamlit, Docker y Git.

## Objetivo

Construir una solución de análisis de terremotos que permita extraer, transformar, cargar y visualizar información sísmica para apoyar decisiones técnicas, operativas y ejecutivas.

## Fuentes de datos

El proyecto integra tres fuentes de datos:

1. **CSV histórico local**  
   Archivo principal con registros históricos de terremotos.

2. **API pública USGS**  
   Fuente externa para obtener eventos sísmicos recientes.

3. **Base de datos MySQL**  
   Almacena los datos procesados por el pipeline ETL.

## Tecnologías

- Python
- Pandas
- MySQL
- SQLAlchemy
- FastAPI
- Streamlit
- Plotly
- Docker
- Docker Compose
- Git / GitHub
- Pytest
- Python-dotenv

## Estructura del proyecto

```text
api/            API REST con FastAPI
dashboards/     Dashboard interactivo Streamlit
data/           Datos raw y processed
etl/            Pipeline ETL
tests/          Pruebas automatizadas
docs/           Documentación técnica