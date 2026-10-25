from fastapi import FastAPI

app = FastAPI()



@app.get("/add")
def add_numbers(x: int, y: int):
    total = x + y
    return {"sum": total}

