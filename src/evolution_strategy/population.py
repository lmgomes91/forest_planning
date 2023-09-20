import numpy as np
import multiprocessing
from numpy import ndarray
from src.evolution_strategy.individual import generate_individual, calculate_vpl
import concurrent.futures


def init_population(num_individuals: int) -> ndarray:
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_cores)
    population_list = pool.map(generate_individual, range(num_individuals))

    pool.close()
    pool.join()

    return np.array(population_list, dtype=object)


def sort_population(population: ndarray) -> ndarray:
    sorted_indices = np.argsort(population[:, 0])[::-1]
    return population[sorted_indices]


def calculate_vpl_population(population: ndarray, dataset: ndarray, reset_values: bool = True):
    with concurrent.futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        futures = [executor.submit(calculate_vpl, element, dataset, reset_values) for element in population]
        concurrent.futures.wait(futures)
