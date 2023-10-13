import numpy as np
import multiprocessing
from numpy import ndarray
from src.evolution_strategy.fo import calculate_vpl
from src.evolution_strategy.individual import generate_individual
import concurrent.futures


def init_population(num_individuals: int) -> ndarray:
    num_cores = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(processes=num_cores)
    population_list = pool.map(generate_individual, range(num_individuals))

    pool.close()
    pool.join()

    return np.array(population_list, dtype=object)


def sort_population(population: ndarray) -> ndarray:
    sorted_indices = np.argsort(population[:, 0])[::-1]
    return population[sorted_indices]


def tournament_selection(population: ndarray, mu: int) -> ndarray:
    winners = []
    total_population = (2 * mu) - 1
    np.random.shuffle(population)
    for i in range(0, mu):
        if population[i][0] > population[total_population - i][0]:
            winners.append(population[i])
        else:
            winners.append(population[total_population - i])

    return np.array(winners, dtype=object)


def elitism_selection(population: ndarray) -> ndarray:
    return (sort_population(population))[:population.shape[0] // 2]


def calculate_vpl_population(population: ndarray, dataset: ndarray, reset_values: bool = True):
    with concurrent.futures.ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
        futures = [executor.submit(calculate_vpl, element, dataset, reset_values) for element in population]
        concurrent.futures.wait(futures)
