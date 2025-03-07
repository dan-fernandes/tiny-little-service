import uvicorn
from fastapi import FastAPI

app = FastAPI()


def start():
    uvicorn.run(app)


@app.get("/iseven/{number}")
def read_root(number: int):
    return {"answer": not bool(number % 2)}
