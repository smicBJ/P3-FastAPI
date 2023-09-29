from fastapi import FastAPI
import uvicorn

app = FastAPI()


# First we make some fake data to be able to use as our "database calls"
users = [
    {"name": "Hudson", "grade": 11},
    {"name": "Jack", "grade": 10},
    {"name": "Adriaan", "grade": 11}
]


# Here we see that order matters. Going to this path will trigger this route first rather than the next because it
# comes first
@app.get("/users/me")
async def get_me():
    return {"name": "My Profile"}


# Parameters in our route definitions allow us to match multiple paths
@app.get("/users/{user_name}")
async def get_profile(user_name: str):
    for user in users:
        if user_name.lower() == user["name"].lower():
            return user
    return {"msg": "User not found"}


# Here we see another way to create dynamic routes using query parameters
@app.get("/documents")
async def get_document(name: str | None = None):
    if name:
        return {"msg": f"Document {name} successfully retrieved", "doc": name}
    return {"msg": "Name was not passed as a query"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
