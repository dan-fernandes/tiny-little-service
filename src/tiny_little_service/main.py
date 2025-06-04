import logging

import uvicorn
from fastapi import FastAPI

app = FastAPI()

LOGGER = logging.getLogger(__name__)


def start():
    LOGGER.info("Starting the service.")
    uvicorn.run(app, host="0.0.0.0")


@app.get("/iseven/{number}")
def read_root(number: int):
    print(__name__)
    LOGGER.info(f"Checking if {number} is even.")
    return {"answer": not bool(number % 2)}
