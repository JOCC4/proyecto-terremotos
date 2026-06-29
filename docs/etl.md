# Pipeline ETL

## Objetivo

El pipeline ETL permite extraer, transformar y cargar datos sísmicos para su posterior análisis en la API y el dashboard.

## Extract

Se utilizan dos fuentes principales:

1. **CSV histórico**
   - Archivo: `data/raw/dataset_terremotos_limpio.csv`
   - Contiene registros históricos de terremotos.

2. **API pública USGS**
   - Script: `etl/extract_api.py`
   - Permite obtener eventos sísmicos recientes desde una fuente externa.

## Transform

Durante la transformación se realizan los siguientes pasos:

- Validación de valores nulos.
- Validación de filas duplicadas.
- Revisión de tipos de datos.
- Creación de nuevas variables:
  - `categoria_magnitud`
  - `categoria_profundidad`

## Load

Los datos transformados se cargan en MySQL en la tabla:

```text
terremotos

## Evidencia

El pipeline genera:

- `data/processed/terremotos_transformados.csv`
- tabla `terremotos` en MySQL
- datos disponibles para FastAPI y Streamlit