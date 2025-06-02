from fastapi import FastAPI

app = FastAPI()

@app.get('/add')
def add(a:float,b:float):
    return {'result':a+b}

@app.get('/subract')
def subract(a:float,b:float):
    return {'result':a-b}

@app.get('/multiply')
def multiply(a: float,b: float):
    return {'result': a*b}

@app.get('/divide')
def divide(a:float,b:float):
    if b==0:
        return {'error':'Division by Zero'}
    return {'Result':a/b}
