import requests
import pandas as pd

# URL de la API pública USGS
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

# Consumir API
response = requests.get(url)

# Convertir respuesta a JSON
data = response.json()

# Lista para guardar terremotos
terremotos = []

# Recorrer eventos
for evento in data["features"]:

    propiedades = evento["properties"]
    coordenadas = evento["geometry"]["coordinates"]

    terremotos.append({
        "place": propiedades["place"],
        "mag": propiedades["mag"],
        "time": propiedades["time"],
        "longitude": coordenadas[0],
        "latitude": coordenadas[1],
        "depth": coordenadas[2]
    })

# Crear DataFrame
df_api = pd.DataFrame(terremotos)

# Mostrar primeras filas
print(df_api.head())

print("\nTotal terremotos API:", len(df_api))

# Guardar CSV de la API
df_api.to_csv(
    "data/raw/terremotos_api.csv",
    index=False
)

print("\nArchivo CSV API guardado correctamente.")
