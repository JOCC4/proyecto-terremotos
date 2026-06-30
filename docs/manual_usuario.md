# Manual de Usuario — Dashboard de Terremotos

## Descripción

Este sistema permite visualizar, analizar y monitorear información sísmica mediante un dashboard interactivo desarrollado con Streamlit.

La solución integra:

* datos históricos desde archivos CSV,
* datos en tiempo real desde la API pública USGS,
* almacenamiento en MySQL,
* procesamiento ETL automatizado.

---

# Acceso al Dashboard

Ejecutar el sistema:

```bash
streamlit run dashboards/app.py
```

Luego abrir en navegador:

```text
http://localhost:8501
```

---

# Funcionalidades principales

## 1. Visualización de KPIs

El dashboard presenta indicadores ejecutivos:

* Total de eventos históricos
* Magnitud máxima histórica
* Magnitud promedio
* Profundidad promedio
* Cantidad de países
* Categoría sísmica más frecuente

---

## 2. Filtros interactivos

El usuario puede filtrar información por:

* Categoría de magnitud
* País

Los gráficos y métricas se actualizan automáticamente.

---

## 3. Visualizaciones analíticas

El sistema incluye:

### Vista ejecutiva

KPIs y métricas resumidas para apoyo a decisiones.

### Vista operativa

Gráficos de categorías sísmicas y análisis por país.

### Vista técnica

Relación entre profundidad y magnitud mediante scatter plot.

---

## 4. Integración API pública

El dashboard muestra evidencia de integración con la API pública USGS:

* cantidad de eventos obtenidos,
* magnitud máxima,
* muestra de datos consumidos.

---

# Tecnologías utilizadas

* Python
* Pandas
* Streamlit
* Plotly
* FastAPI
* MySQL
* Docker
* GitHub

---

# Consideraciones

* El sistema requiere conexión a MySQL.
* La API USGS requiere acceso a internet.
* Las variables de entorno deben estar configuradas en el archivo `.env`.

---

# Autor

Proyecto académico desarrollado para la asignatura:

SCY1101 — Programación para la Ciencia de Datos.
