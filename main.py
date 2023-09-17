from src.utils.dataset import open_dataset
from src.evolution_strategy.evolution_strategy import EvolutionStrategy
import time


def main():
    print('Processing...')
    start_time = time.time()
    dataset = open_dataset()

    es = EvolutionStrategy(dataset, 25, 1000, 0.3)
    result = es.start()

    end_time = time.time()
    elapsed_time_minutes = (end_time - start_time) / 60

    print(f"The algorithm took {elapsed_time_minutes:.2f} minutes to run.")
    print(f"\nVPL: {result['vpl']}")
    print(f"\nSolution: {result['solution']}")
    print(f"\nPlanning Horizon: {result['planning_horizon']}")


if __name__ == '__main__':
    main()
