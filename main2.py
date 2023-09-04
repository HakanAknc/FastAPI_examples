from fastapi import FastAPI

app = FastAPI()

@app.get("/add/")
def add_numbers(x: int, y: int):
    result = x + y
    return {"result": result}

@app.get("/subtract/")
def subtract_numbers(x: int, y: int):
    result = x - y
    return {"result": result}

@app.get("/multiply/")
def multiply_numbers(x: int, y: int):
    result = x * y
    return {"result": result}

@app.get("/divide/")
def divide_numbers(x: int, y: int):
    if y == 0:
        return {"error": "Division by zero"}
    result = x / y
    return {"result": result}