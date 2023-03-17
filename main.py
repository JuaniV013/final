from fastapi import FastAPI

# Aquí importaríamos el módulo que nos permita acceder a los datos de la empresa

app = FastAPI()

# Película con mayor duración
@app.get("/max_duration/")
async def get_max_duration(release_year: int = None, ID: str = None, duration_type: str = None):
    cnx = mysql.connector.connect(user='root', password='12345678', host='127.0.0.1', database='proyecto_individual')
    cursor = cnx.cursor()

    query = "SELECT title, duration_int FROM tabla_union_prueba"
    filters = []

    if release_year is not None:
        filters.append("release_year = %s")
    if duration_type is not None:
        filters.append("duration_type = %s")
    if ID is not None:
        filters.append("ID LIKE %s")

    if len(filters) > 0:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY duration_int DESC LIMIT 1"

    filters

    cursor.execute(query, (release_year, duration_type, ID))
    result = cursor.fetchone()

    cursor.close()
    cnx.close()

    return {"title": result[0], "duration": result[1]}

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
