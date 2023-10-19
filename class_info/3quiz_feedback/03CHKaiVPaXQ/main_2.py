from fastapi import FastAPI
# Standard Libraries should be imported before external libraries
# -1: the direction said to import randint from the random library
import random
import uvicorn
# Put spaces between your imports and variables and function definitions
app = FastAPI()
app_str = str(app)
@app.get('/')
async def home_route():
    # -1: Should return a string, not a tuple with a string inside
    return ('unit3quiz')

# -1: The response function should be called the "about_route"
@app.get('/about_me')
async def home_route():
    return {'name':'Joe Yang'}

# -1: The response function should be called the "random_number_helper"
@app.get('/helper/random_number')
async def home_route():
    # -1: The variable name should be "random_num" and not "joe"
    joe = random.randint(1,69)
    return {'urage':joe}

if __name__ == "__main__":
    # -1: The app string is incorrect, although I acknowledge it works, that wasn't the directions
    uvicorn.run(app_str, host="0.0.0.0", port=8000, reload=True)
