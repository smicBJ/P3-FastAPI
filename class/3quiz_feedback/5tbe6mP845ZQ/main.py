from fastapi import FastAPI
import uvicorn
# -1: missing uvicorn import
# added missing import
from random import randint

# -1: need to import randint from the random library
# added missing import


# Extra note, standard library should be imported before external libraries

app = FastAPI()


@app.get("/")
def home_route():
    # -1: Return a string, not a set with a string inside
    # removed the original and change to return a string.
    # return {"Unit 3": "Quiz"}
    return "Unit 3 Quiz"


@app.get("/about_me")
def about_me():
    return {"name": "Ethan"}


@app.get("/helper/random_number")
def random_number_helper():
    # -1: missing random_num variable
    # added the missing variable
    # return {"random 1:", random.random()}
    random_num = randint(0, 100000000000)

    # -1: Due to the above return statement, all this code can never be reached and is irrelevant
    # removed the below codes.
    # @app.get("/dictionary")
    # def ret_dict():
    # return {"random number": random_number_helper}

    # print(random_number_helper)
    # change to return
    return {"number": f"{random_num}"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
