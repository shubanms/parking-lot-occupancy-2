import random

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from random import randint
from time import sleep


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def generate_random_data():
    data = {
        "left": [random.choice([0, 1]) for _ in range(22)],
        "middle": [random.choice([0, 1]) if x != -1 else -1 for x in [-1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, -1]],
        "right": [random.choice([0, 1]) for _ in range(22)]
    }
    return data


@app.get("/get_parking_lot_state/")
def get_parking_lot_state():
    sleep(randint(1, 3))
    return generate_random_data()
