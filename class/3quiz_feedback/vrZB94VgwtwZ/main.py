from fastapi import FastAPI
import uvicorn
# note: Standard library imports should come before external ones
from random import randint

app = FastAPI()

@app.get("/")
def home_route():
    return "Unit 3 Quiz"

@app.get("/about_me")
def about_me():
    return {"name": "Hudson"}

@app.get("/helper/random_number")
def random_number_helper():
    random_num = randint(0, 10)
    # -1: The exercise required the value of random_num, not the string version of it
    return {"number": f"{random_num}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)