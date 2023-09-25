from fastapi import FastAPI
# -1: missing uvicorn import
# -1: need to import randint from the random library
# Extra note, standard library should be imported before external libraries
import random

app = FastAPI()


@app.get("/")
def home_route():
    # -1: Return a string, not a set with a string inside
    return {"Unit 3": "Quiz"}


@app.get("/about_me")
def about_me():
    return {"name": "Ethan"}


@app.get("/helper/random_number")
def random_number_helper():
    # -1: missing random_num variable
    return {"random 1:", random.random()}

    # -1: Due to the above return statement, all this code can never be reached and is irrelevant
    @app.get("/dictionary")
    def ret_dict():
        return {"random number": random_number_helper}

    print(random_number_helper)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
