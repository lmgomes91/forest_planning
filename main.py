import multiprocessing

# from src.analysis.boxplot import boxplot_results
from src.utils.csv import save_result
from src.utils.dataset import open_dataset
from src.evolution_strategy.evolution_strategy import EvolutionStrategy
import time
import warnings

def main():
    
    warnings.filterwarnings("ignore")

    for i in range(0, 23):
        try:
            print(f'\n############# Processing {i} ##############')
            start_time = time.time()
            dataset = open_dataset()
            mu = multiprocessing.cpu_count() * 2
            generations = 800
            mutation = 0.8

            es = EvolutionStrategy(dataset, mu, generations, mutation)
            result = es.start()
            end_time = time.time()
            elapsed_time_minutes = (end_time - start_time) / 60

            print(f"The algorithm took {elapsed_time_minutes:.2f} minutes to run.")
            print(f"VPL: {result[0][0]}")
            print(f"\nSolution: {result[0][1]}")

            save_result(result[0], elapsed_time_minutes, mu, mutation, generations)
            # boxplot_results()

        except Exception as e:
            raise e


if __name__ == '__main__':
    main()
