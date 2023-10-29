from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from routers import academic, athlete

app = FastAPI()

app.include_router(academic.router, prefix="/academics")
app.include_router(athlete.router, prefix="/athletes")

app.mount("/static", StaticFiles(directory="static"))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
