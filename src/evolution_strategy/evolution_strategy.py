import multiprocessing
from multiprocessing import Pool

import pandas as pd

from src.evolution_strategy.individual import recalculate_vpl, create_individual_by_mutation
from src.evolution_strategy.population import sort_population, init_population


class EvolutionStrategy:

    def __init__(self, dataset: pd.DataFrame, mu: int, generations: int, mutation: float):
        self.dataset = dataset
        self.mu = mu
        self.generations = generations
        self.mutation = mutation

    def start(self) -> pd.DataFrame:
        population = sort_population(
            init_population(self.mu, self.dataset)
        )

        for i in range(self.generations):
            # make it parallel
            # new_population = []
            # for _, individual in population.iterrows():
            #     new_individual = shift10_with_mutation_factor(individual.copy(deep=True), self.dataset, self.mutation)
            #     recalculate_vpl(new_individual, self.dataset)
            #
            #     new_population.append(
            #         new_individual
            #     )

            with Pool(multiprocessing.cpu_count()) as pool:
                new_population = pool.starmap(create_individual_by_mutation,
                                              [(row, self.dataset, self.mutation) for _, row in population.iterrows()])

            population = pd.concat([population, pd.DataFrame(new_population)], ignore_index=True)
            population = (sort_population(population)).iloc[:self.mu]

            # print(f"Iteration: {i}\tVLP: {population['vpl'][0]}")

        return population.iloc[0]
