from multiprocessing import Pool
import numpy as np
from src.evolution_strategy.individual import create_descendant
from src.evolution_strategy.population import sort_population, init_population, calculate_vpl_population, \
    tournament_selection
from src.evolution_strategy.refine_better_solution import refine_better_solution


class EvolutionStrategy:

    def __init__(self, dataset: np.ndarray, mu: int, generations: int, mutation: float, max_workers: int):
        self.dataset = dataset
        self.mu = mu
        self.generations = generations
        self.mutation = mutation
        self.max_workers = max_workers

    def start(self) -> np.ndarray:
        population = init_population(self.mu, self.max_workers)
        calculate_vpl_population(population, self.dataset, self.max_workers, False)
        population = sort_population(population)
        count_vpl = 1
        vpl = population[0][0]

        for i in range(self.generations):
            if count_vpl == 3 and self.mutation > 0.05:
                count_vpl = 0
                self.mutation = round(self.mutation - 0.03, 2)
                print(f'Mutation downgraded to {self.mutation}')

            with Pool(self.max_workers) as pool:
                new_population = pool.starmap(
                    create_descendant,
                    [
                        (individual.copy(),
                         self.dataset, self.mutation) for individual in population
                    ]
                )

            population = tournament_selection(np.vstack((population, new_population)), self.mu)
            population = sort_population(population)

            print(f'Iteration {i+1}\tVPL -> Best: {population[0][0]} worst: {population[-1][0]}')

            if vpl == population[0][0]:
                count_vpl += 1
            else:
                count_vpl = 1
                vpl = population[0][0]

            if count_vpl == 60:
                break

        print("Refining better solution...")
        population[0] = refine_better_solution(population[0], self.dataset)
        return population
