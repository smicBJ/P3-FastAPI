from random import randint
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/helper/random_number")
def random_number_helper():
    random_num = randint(0, 1000000000000000000000000000000)
    return {"number": random_num}


@app.get("/about")
def read_about():
    return {"name": "Jon"}


@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"id": user_id}


if __name__ == "__main__":
    # -1: Missing reload
    # uvicorn.run("main:app")
    uvicorn.run("main:app", reload=True)
