from fastapi import FastAPI

app = FastAPI()

@app.get('/to_fahrenheit')
def to_fahrenheit(celsius:float):
    fahrenheit = (celsius * (9/5)) + 32
    return {"Fahrenheit ": fahrenheit}

@app.get('/to_celsius')
def to_celsius(fahrenheit: float):
    celsius = (fahrenheit-32) * (5/9)
    return {'celsius': celsius}