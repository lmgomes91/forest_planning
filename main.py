import os

from src.utils.dataset import open_dataset
from src.evolution_strategy.evolution_strategy import EvolutionStrategy
import time
import uuid

from src.utils.db import save_result_in_db


def main():

    for i in range(0, 100):
        try:
            print(f'\n############# Processing {i} ##############')
            start_time = time.time()
            dataset = open_dataset()
            mu = 30
            generations = 600
            mutation = 0.4
            max_workers = (os.cpu_count() * 2) - 1

            es = EvolutionStrategy(dataset, mu, generations, mutation, max_workers)
            results = es.start()
            end_time = time.time()
            elapsed_time_minutes = (end_time - start_time) / 60

            print(f"The algorithm took {elapsed_time_minutes:.2f} minutes to run.")
            print(f"VPL: {results[0][0]}")
            print(f"\nSolution: {results[0][1]}")

            save_result_in_db(results, mu, generations, mutation, elapsed_time_minutes)

        except Exception as e:
            raise e


if __name__ == '__main__':
    main()
