# Arquitectura Técnica

## Descripción general

El sistema permite analizar eventos sísmicos mediante un flujo end-to-end de datos.

## Flujo de datos

CSV original → ETL Python → Dataset transformado → MySQL → API FastAPI → Dashboard Streamlit → Docker

## Componentes

### ETL
Lee el dataset, valida nulos y duplicados, crea nuevas variables y guarda los datos procesados.

### MySQL
Almacena la tabla `terremotos` con los datos transformados.

### API REST
Expone endpoints para consultar eventos, resumen general y terremotos más fuertes.

### Dashboard
Visualiza KPIs, magnitud por categoría, magnitud promedio por país y relación profundidad-magnitud.

### Docker
Permite ejecutar el dashboard en un contenedor reproducible usando `docker-compose`.

## Decisiones técnicas

- Se usó FastAPI por su documentación automática.
- Se usó Streamlit por rapidez para dashboards interactivos.
- Se usó MySQL como fuente SQL.
- Se usó Docker para reproducibilidad.
- Se usó Pytest para validar el pipeline.