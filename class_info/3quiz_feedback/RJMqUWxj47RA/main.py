from fastapi import FastAPI
import uvicorn
# Standard libraries should be imported before external ones
from random import randint

app = FastAPI()

@app.get("/")
def home_route():
    return "Unit 3 Quiz"

@app.get("/about_me")
def about_me():
    return {"name":"Richard Liu"}

@app.get("/helper/random_number")
def random_number_helper():
    random_num= randint(0,100)
    return {"number:":random_num}

if __name__ == "__main__":
    # -1" This is missing the reload functionality
    uvicorn.run("main:app")