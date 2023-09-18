from src.utils.dataset import open_dataset
from src.evolution_strategy.evolution_strategy import EvolutionStrategy
import time


def main():
    for i in range(0, 10):
        print(f'Processing {i}...')
        start_time = time.time()
        dataset = open_dataset()

        es = EvolutionStrategy(dataset, 8, 1000, 0.45)
        result = es.start()

        end_time = time.time()
        elapsed_time_minutes = (end_time - start_time) / 60

        print(f"The algorithm took {elapsed_time_minutes:.2f} minutes to run.")
        print(f"\nVPL: {result['vpl']}")
        print(f"\nSolution: {result['solution']}")
        print(f"\nPlanning Horizon: {result['planning_horizon']}")

        with open(f'output/result_{int(time.time()*1000)}', "w") as file:
            file.write(f"The algorithm took {elapsed_time_minutes:.2f} minutes to run.")
            file.write(f"\nVPL: {result['vpl']}")
            file.write(f"\nSolution: {result['solution']}")
            file.write(f"\nPlanning Horizon: {result['planning_horizon']}")


if __name__ == '__main__':
    main()
