from fastapi import FastAPI
import uvicorn
# Standard Libraries should be imported before external libraries
from random import randint

app = FastAPI()
# -1: this should be inside the response request
random_num = randint(1, 1000)


@app.get("/")
def home_route():
    return "Unit 3 quiz"

@app.get("/about_me")
def about_me():
    return {"name": "Nolan"}

@app.get("/helper/random_number")
def random_number_helper():
    return {"number": random_num}



if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)