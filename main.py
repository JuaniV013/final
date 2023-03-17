from fastapi import FastAPI

# Aquí importaríamos el módulo que nos permita acceder a los datos de la empresa

app = FastAPI()

# Película con mayor duración
@app.get("/max_duration/")
async def get_max_duration(year: int = None, platform: str = None, duration_type: str = None):
    # Aquí iría la lógica para obtener la película con mayor duración,
    # teniendo en cuenta los filtros opcionales de año, plataforma y tipo de duración.
    return {"title": title, "duration": duration}

# Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/score_count/")
async def get_score_count(platform: str, scored: int, year: int):
    # Aquí iría la lógica para contar la cantidad de películas con un puntaje mayor a scored en determinado año
    # y para la plataforma especificada.
    return {"platform": platform, "score_count": score_count}

# Cantidad de películas por plataforma
@app.get("/count_platform/")
async def get_count_platform(platform: str):
    # Aquí iría la lógica para contar la cantidad de películas para una plataforma especificada.
    return {"platform": platform, "count": count}

# Actor que más se repite según plataforma y año
@app.get("/actor/")
async def get_actor(platform: str, year: int):
    # Aquí iría la lógica para determinar el actor que más se repite según plataforma y año.
    return {"platform": platform, "year": year, "actor": actor}
