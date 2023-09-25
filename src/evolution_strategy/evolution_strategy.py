import multiprocessing
from multiprocessing import Pool
import numpy as np

from src.evolution_strategy.individual import create_descendant
from src.evolution_strategy.population import sort_population, init_population, calculate_vpl_population, \
    elitism_selection, tournament_selection


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

        count_vpl = 1
        vpl = population[0][0]

        for i in range(self.generations):
            if count_vpl == 3 and self.mutation > 0.1:
                count_vpl = 0
                self.mutation = round(self.mutation - 0.03, 2)
                print(f'Mutation downgraded to {self.mutation}')

            with Pool(num_cores) as pool:
                new_population = pool.starmap(
                    create_descendant,
                    [
                        (individual.copy(),
                         self.dataset, self.mutation) for individual in population
                    ]
                )

            # population = tournament_selection(np.vstack((population, new_population)), self.mu)
            population = elitism_selection(np.vstack((population, new_population)))
            print(f'Iteration {i+1}\tVPL -> Best: {population[0][0]} worst: {population[-1][0]}')

            if vpl == population[0][0]:
                count_vpl += 1
            else:
                count_vpl = 1
                vpl = population[0][0]
        return population
