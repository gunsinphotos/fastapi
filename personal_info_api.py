from fastapi import FastAPI

app = FastAPI()

@app.get('/greet')
def greet(name:str, age:int):
    return {"message": f"Hello {name} you are {age} years old!"}