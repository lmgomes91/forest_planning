import pandas as pd
import multiprocessing
from src.evolution_strategy.individual import generate_individual


def init_population(num_individuals: int, dataset: pd.DataFrame) -> pd.DataFrame:
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_cores)
    population_list = pool.map(generate_individual, [dataset] * num_individuals)

    pool.close()
    pool.join()

    return pd.DataFrame(population_list)


def sort_population(population: pd.DataFrame) -> pd.DataFrame:
    return population.sort_values(by='vpl', ascending=False)
