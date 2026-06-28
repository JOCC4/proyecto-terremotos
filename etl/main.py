from sqlalchemy import create_engine
import pandas as pd

# Leer dataset
df = pd.read_csv("data/raw/dataset_terremotos_limpio.csv")

# Mostrar primeras filas
print(df.head())

# Mostrar información general
print(df.info())


# Verificar valores nulos
print("\nValores nulos por columna:")
print(df.isnull().sum())

# Verificar duplicados
print("\nFilas duplicadas:")
print(df.duplicated().sum())

# Estadísticas generales
print("\nEstadísticas:")
print(df.describe())

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


df["categoria_magnitud"] = df["mag"].apply(clasificar_magnitud)

# Clasificación de profundidad


def clasificar_profundidad(depth):

    if depth < 70:
        return "Superficial"

    elif depth < 300:
        return "Intermedio"

    else:
        return "Profundo"


df["categoria_profundidad"] = df["depth"].apply(clasificar_profundidad)

# Mostrar nuevas columnas
print("\nNuevas columnas creadas:")
print(df[["mag", "categoria_magnitud",
        "depth", "categoria_profundidad"]].head())


# Guardar dataset transformado
df.to_csv(
    "data/processed/terremotos_transformados.csv",
    index=False
)

print("\nDataset transformado guardado correctamente.")


# Conexión MySQL
engine = create_engine(
    "mysql+pymysql://root:@localhost:3306/terremotos_db"
)

# Guardar tabla en MySQL
df.to_sql(
    "terremotos",
    con=engine,
    if_exists="replace",
    index=False
)

print("\nDatos cargados correctamente en MySQL.")
