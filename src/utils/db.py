import numpy as np
from pymongo import MongoClient
from decouple import config


def save_result_in_db(individual: np.ndarray, mu: int, generations: int, mutation: float, time, date: int):
    client = MongoClient(config('CONN_STRING_MONGO'))
    db = client["ppgmcs"]
    collection = db["forest_planning"]

    collection.insert_one({
        "vpl": int(individual[0]),
        "solution": np.array2string(individual[1], separator=','),
        "mu": mu,
        "generations": generations,
        "mutation": mutation,
        "time": time,
        "date": date
    })

    client.close()
