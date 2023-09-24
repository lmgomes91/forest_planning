import multiprocessing

from src.utils.csv import save_result
from src.utils.dataset import open_dataset
from src.evolution_strategy.evolution_strategy import EvolutionStrategy
import time


def main():
    for i in range(0, 10):
        print(f'\n############# Processing {i} ##############')
        start_time = time.time()
        dataset = open_dataset()
        mu = multiprocessing.cpu_count() * 2
        generations = 700
        mutation = 0.40

        es = EvolutionStrategy(dataset, mu, generations, mutation)
        result = es.start()
        end_time = time.time()
        elapsed_time_minutes = (end_time - start_time) / 60

        print(f"The algorithm took {elapsed_time_minutes:.2f} minutes to run.")
        # print(f"VPL: {result[0]}")
        # print(f"\nSolution: {result[1]}")
        # print(f"\nPlanning Horizon: {result[2]}")

        save_result(result, elapsed_time_minutes, mu, mutation, generations)


if __name__ == '__main__':
    main()
