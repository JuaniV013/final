from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Cargar los datos a un dataframe
df = pd.read_csv("data.csv")

# Definir la estructura del endpoint
@app.get("/max_duration")
async def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    # Filtrar los datos según los parámetros recibidos
    filtered_df = df.copy()
    if year is not None:
        filtered_df = filtered_df[filtered_df['release_year'] == year]
    if platform is not None:
        filtered_df = filtered_df[filtered_df['ID'].str.contains(platform)]
    if duration_type is not None:
        filtered_df = filtered_df[filtered_df['duration_type'] == duration_type]

    # Encontrar la película con la mayor duración
    max_duration = filtered_df['duration_int'].max()
    movie = filtered_df[filtered_df['duration_int'] == max_duration].iloc[0]

    # Devolver los resultados en el formato especificado
    return {
        "movie_title": movie['title'],
        "duration": movie['duration_int'],
        "year": movie['release_year'],
        "platform": movie['ID'],
        "duration_type": movie['duration_type']
    }

get_max_duration(2020,'a','min')
