# Arquitectura del Sistema

## Flujo general del sistema

```text
             API Pública USGS
                     │
                     ▼
          ETL Python (Extract)
                     │
                     ▼
     Transformación y limpieza
                     │
                     ▼
              Base de datos
                  MySQL
                     │
                     ▼
            API REST FastAPI
                     │
                     ▼
        Dashboard Streamlit BI
                     │
                     ▼
          Contenedores Docker
```

---

## Descripción de componentes

### API pública USGS

Fuente de datos sísmicos en tiempo real utilizada para obtener eventos de terremotos mediante consumo REST.

### ETL Python

Proceso encargado de:

* extraer datos históricos y API,
* transformar variables,
* limpiar registros,
* categorizar magnitudes y profundidad.

### MySQL

Base de datos relacional donde se almacenan los terremotos procesados para análisis.

### FastAPI

API REST utilizada para exponer endpoints analíticos y consultas de terremotos.

### Streamlit

Dashboard interactivo para visualización analítica, filtros dinámicos y KPIs.

### Docker

Contenedorización completa del sistema para facilitar despliegue y portabilidad.
