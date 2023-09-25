from fastapi import FastAPI
import uvicorn
# Standard Libraries should be imported before external libraries
from random import randint
# You should place spaces between imports, variables, and methods
app = FastAPI()
# -1: The name of the response function is incorrect
@app.get("/")
def read_home_route():
    return "Unit 3 Quiz"
# -1: The name of the response function is incorrect
@app.get("/about_me")
def read_about_me():
    return {"name":"Jack Zheng"}
# -1: The name of the response function is incorrect
@app.get("/helper/random_number")
def read_random_number_helper():
    random_num=randint(1,3)
    return {"number":random_num}
if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)