from src.utils.dataset import open_dataset
from src.evolution_strategy.evolution_strategy import EvolutionStrategy
import time


def main():
    dataset = open_dataset()

    es = EvolutionStrategy(dataset, 100)

    start_time = time.time()
    es.start()
    end_time = time.time()

    # Calculate the elapsed time in seconds
    elapsed_time_seconds = end_time - start_time

    # Convert the elapsed time to minutes
    elapsed_time_minutes = elapsed_time_seconds / 60

    print(f"The algorithm took {elapsed_time_minutes:.2f} minutes to run.")


if __name__ == '__main__':
    main()

