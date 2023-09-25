# -1: Need to import the class from fastapi library
import FastAPI
import uvicorn
# Standard Libraries should be imported before external libraries
from random import randint

app=FastAPI()

@app.get("/")
def home_route():
    # -1: The response should be a string, not a set with a string
    return {"Unit 3 Quiz"}

@app.get("/about_me")
def about_me():
    me = {
        'name': 'Samuel W'
    }
    return me
# Put atleast one space between function definitions, two is required
@app.get('/helper/random_number')
def random_number_helper():
    random_num=randint(1, 6969)
    k = {
        'number':random_num
    }
    return k

# -4: Did not use Uvicorn, run the string, or have the reload option needed
