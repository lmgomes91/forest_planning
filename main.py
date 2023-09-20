import multiprocessing
from src.utils.dataset import open_dataset
from src.evolution_strategy.evolution_strategy import EvolutionStrategy
import time


def main():
    for i in range(0, 10):
        print(f'\n############# Processing {i} ##############')
        start_time = time.time()
        dataset = open_dataset()

        es = EvolutionStrategy(dataset, multiprocessing.cpu_count() * 3, 1000, 0.40)
        result = es.start()

        end_time = time.time()
        elapsed_time_minutes = (end_time - start_time) / 60
        print(f"The algorithm took {elapsed_time_minutes:.2f} minutes to run.")
        print(f"VPL: {result[0]}")
        # print(f"\nSolution: {result[1]}")
        # print(f"\nPlanning Horizon: {result[2]}")

        with open(f'output/result_{int(time.time()*1000)}', "w") as file:
            file.write(f"The algorithm took {elapsed_time_minutes:.2f} minutes to run.")
            file.write(f"\nVPL: {result[0]}")
            file.write(f"\nSolution: {result[1]}")
            file.write(f"\nPlanning Horizon: {result[2]}")


if __name__ == '__main__':
    main()
