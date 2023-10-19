from fastapi import FastAPI
import uvicorn

from class_info.lessons.opening_files import Helper

app = FastAPI()
data = Helper()
API_KEYS = ["pen4hr48snc", "79sfhsieuhsi", "0123456789"]


@app.get("/athletes")
async def get_all_athletes(api_key: str):
    if api_key in API_KEYS:
        res = []
        for athlete in data.data:
            res.append(athlete["name"])
        return res
    return {"msg": "You do not have permission to access this rss"}


@app.get("/athletes/{athlete}")
async def get_athlete(athlete: str, api_key: str):
    if api_key in API_KEYS:
        for student in data.data:
            if athlete in student["name"]:
                return student
        return {"msg": "Athlete not found"}
    return {"msg": "You do not have permission to access this rss"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True)
