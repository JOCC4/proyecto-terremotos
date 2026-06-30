# Guía de Despliegue — Proyecto Terremotos

# Descripción

Esta guía explica el proceso de instalación y ejecución del sistema de análisis de terremotos utilizando Python, MySQL, Docker, FastAPI y Streamlit.

---

# Requisitos

Instalar previamente:

* Python 3.12+
* MySQL Server
* Docker Desktop
* Git
* Visual Studio Code

---

# Clonar repositorio

```bash
git clone https://github.com/USUARIO/proyecto-terremotos.git
```

Entrar al proyecto:

```bash
cd proyecto-terremotos
```

---

# Crear entorno virtual

Windows:

```bash
python -m venv venv
```

Activar entorno:

```bash
venv\Scripts\activate
```

---

# Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Configuración de variables de entorno

Crear archivo `.env`:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=
DB_NAME=terremotos_db
```

---

# Crear base de datos MySQL

Ingresar a MySQL y ejecutar:

```sql
CREATE DATABASE terremotos_db;
```

---

# Ejecutar Pipeline ETL

```bash
python etl/main.py
```

El pipeline realiza:

1. Extract:

   * lectura CSV histórico
   * consumo API pública USGS

2. Transform:

   * limpieza
   * validación
   * categorización sísmica

3. Load:

   * carga de datos en MySQL

---

# Ejecutar API FastAPI

```bash
uvicorn api.main:app --reload
```

Acceder a documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

---

# Ejecutar Dashboard Streamlit

```bash
streamlit run dashboards/app.py
```

Abrir:

```text
http://localhost:8501
```

---

# Ejecución con Docker

Construir contenedores:

```bash
docker-compose up --build
```

El sistema iniciará:

* Dashboard Streamlit
* API FastAPI

---

# Ejecutar pruebas automatizadas

```bash
pytest
```

---

# Estructura principal del proyecto

```text
api/
dashboards/
data/
docs/
etl/
tests/
docker/
```

---

# Evidencias incluidas

El proyecto incluye:

* dashboard interactivo,
* API REST,
* Docker funcionando,
* pruebas automatizadas,
* documentación técnica,
* integración API pública,
* evidencia GitHub.

---

# Autor

Proyecto académico desarrollado para:

SCY1101 — Programación para la Ciencia de Datos.
