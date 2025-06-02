from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def Hello():
    return {'Message':'Hello python Programmer from FastAPI'}

@app.get("/users/{user_id}")
def users(user_id:int):
    return {"user_id":user_id}