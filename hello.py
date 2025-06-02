from fastapi import FastAPI 

app = FastAPI

@app.get("/")
def greet():
    return {'message':'Hello python programmer I am learning machine learning.'}