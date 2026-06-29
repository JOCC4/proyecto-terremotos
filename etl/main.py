from sqlalchemy import create_engine
import pandas as pd
import logging

# =========================================
# CONFIGURACIÓN LOGS
# =========================================

logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Inicio del pipeline ETL")

try:

    # =========================================
    # EXTRACT
    # =========================================

    logging.info("Leyendo dataset CSV")

    df = pd.read_csv("data/raw/dataset_terremotos_limpio.csv")

    print(df.head())

    print(df.info())

    # =========================================
    # VALIDACIONES
    # =========================================

    logging.info("Validando datos")

    print("\nValores nulos por columna:")
    print(df.isnull().sum())

    print("\nFilas duplicadas:")
    print(df.duplicated().sum())

    print("\nEstadísticas:")
    print(df.describe())

    # =========================================
    # TRANSFORM
    # =========================================

    logging.info("Transformando variables")

    # Clasificación de magnitud

    def clasificar_magnitud(mag):

        if mag < 5:
            return "Moderado"

        elif mag < 6:
            return "Fuerte"

        elif mag < 7:
            return "Severo"

        else:
            return "Extremo"

    df["categoria_magnitud"] = df["mag"].apply(
        clasificar_magnitud
    )

    # Clasificación de profundidad

    def clasificar_profundidad(depth):

        if depth < 70:
            return "Superficial"

        elif depth < 300:
            return "Intermedio"

        else:
            return "Profundo"

    df["categoria_profundidad"] = df["depth"].apply(
        clasificar_profundidad
    )

    print("\nNuevas columnas creadas:")

    print(
        df[
            [
                "mag",
                "categoria_magnitud",
                "depth",
                "categoria_profundidad"
            ]
        ].head()
    )

    # =========================================
    # LOAD CSV
    # =========================================

    logging.info("Guardando CSV procesado")

    df.to_csv(
        "data/processed/terremotos_transformados.csv",
        index=False
    )

    print("\nDataset transformado guardado correctamente.")

    # =========================================
    # LOAD MYSQL
    # =========================================

    logging.info("Conectando a MySQL")

    engine = create_engine(
        "mysql+pymysql://root:@localhost:3306/terremotos_db"
    )

    logging.info("Cargando datos en MySQL")

    df.to_sql(
        "terremotos",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("\nDatos cargados correctamente en MySQL.")

    logging.info("Pipeline ETL finalizado correctamente")

except Exception as e:

    logging.error(f"Error en pipeline ETL: {e}")

    print(f"\nOcurrió un error: {e}")
