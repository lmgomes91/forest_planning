import concurrent.futures
import multiprocessing
from multiprocessing import Pool
import numpy as np
from src.evolution_strategy.ils import ils
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
        num_cores = multiprocessing.cpu_count()

        for i in range(self.generations):
            with Pool(num_cores) as pool:
                new_population = pool.starmap(
                    create_individual_by_mutation,
                    [
                        (individual.copy(),
                         self.dataset, self.mutation) for individual in population
                    ]
                )
            calculate_vpl_population(new_population, self.dataset)
            population = np.vstack((population, new_population))
            population = (sort_population(population))[:population.shape[0]//2]

        print(f'Worst Vpl before ils: {population[num_cores-1][0]}')
        print(f'Best Vpl before ils: {population[0][0]}')

        with concurrent.futures.ProcessPoolExecutor(max_workers=num_cores) as executor:
            futures = [
                executor.submit(
                    ils,
                    individual,
                    self.dataset
                ) for individual in population[:num_cores]
            ]

            for p, future in enumerate(concurrent.futures.as_completed(futures)):
                population[p] = future.result()

        print(f'Worst Vpl after ils: {population[num_cores-1][0]}')
        print(f'Best Vpl after ils: {population[0][0]}')
        return population[0]
