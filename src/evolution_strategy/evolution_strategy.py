import multiprocessing
from multiprocessing import Pool
import numpy as np
from src.evolution_strategy.individual import create_individual_by_mutation
from src.evolution_strategy.population import sort_population, init_population, calculate_vpl_population


class EvolutionStrategy:

    def __init__(self, dataset: np.ndarray, mu: int, generations: int, mutation: float):
        self.dataset = dataset
        self.mu = mu
        self.generations = generations
        self.mutation = mutation

    def start(self) -> np.ndarray:
        population = init_population(self.mu)
        calculate_vpl_population(population, self.dataset, False)
        population = sort_population(population)

        for i in range(self.generations):
            with Pool(multiprocessing.cpu_count()) as pool:
                new_population = pool.starmap(
                    create_individual_by_mutation,
                    [
                        (np.copy(individual, order='K'),
                         self.dataset, self.mutation) for individual in population
                    ]
                )
            calculate_vpl_population(new_population, self.dataset)
            population = np.vstack((population, new_population))
            population = (sort_population(population))[:population.shape[0]//2]
        return population[-1]
