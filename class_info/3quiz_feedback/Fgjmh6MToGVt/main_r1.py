from fastapi import FastAPI
# This import is irrelevant, lol
from fastapi.responses import RedirectResponse
# Standard Libraries should be imported before external ones
from random import randint
import uvicorn

app = FastAPI()


@app.get("/")
def home_route():
    return "Unit 3 Quiz"

@app.get("/about_me")
def about_me():
    return {"Name": "Sam"}

@app.get("/helper/random_number")
def random_number_helper():
    random_num = randint(0, 100)
    # -1: It should be the key of "number"
    return {"number": random_num}

@app.get("/funny")
def funny():
    return RedirectResponse(url="https://www.youtube.com/watch?v=znUS2KqPYCw")
    
if __name__ == "__main__":
    uvicorn.run("main:app", port=6969, log_level="info", reload=True)
