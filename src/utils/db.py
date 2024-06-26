from uuid import UUID

import numpy as np
from pymongo import MongoClient
from decouple import config


def save_result_in_db(population: np.ndarray, mu: int, generations: int, mutation: float, time):
    client = MongoClient(config('CONN_STRING_MONGO'))
    db = client["ppgmcs"]
    collection = db["forest_planning_v2"]

    for individual in population:
        if int(individual[0]) > 0:
            collection.insert_one({
                "vpl": int(individual[0]),
                "solution": np.array2string(individual[1], separator=','),
                "mu": mu,
                "generations": generations,
                "mutation": mutation,
                "time": time,
            })

    client.close()
