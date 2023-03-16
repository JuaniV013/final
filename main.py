from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/max_duration")
async def get_max_duration(year: Optional[int] = None,
                           platform: Optional[str] = None,
                           duration_type: Optional[str] = None):
    # Aquí iría la lógica para procesar los datos y devolver la película con mayor duración
    return {"max_duration_movie": max_duration_movie}

