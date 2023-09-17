from src.evolution_strategy.individual import generate_individual
import pandas as pd
import multiprocessing


class EvolutionStrategy:

    def __init__(self, dataset: pd.DataFrame, mu: int, generations: int):
        self.dataset = dataset
        self.mu = mu
        self.generations = generations

    def init_population(self, num_individuals: int) -> pd.DataFrame:
        num_cores = multiprocessing.cpu_count()
        pool = multiprocessing.Pool(processes=num_cores)
        population_list = pool.map(generate_individual, [self.dataset] * num_individuals)

        pool.close()
        pool.join()

        return pd.DataFrame(population_list)

    def sort_population(self, population: pd.DataFrame) -> pd.DataFrame: # noqa
        return population.sort_values(by='vpl', ascending=False)

    def start(self) -> pd.DataFrame:
        population = self.sort_population(
            self.init_population(self.mu)
        )

        for i in range(self.generations):
            # make it parallel
            for _, individual in population.iterrows():
                individual.copy(True)
                # mapply mutation to generate new individual
                # add it to a new population
                # evaluate de population
                # join populations
                # evaluate them
                # cut with better

            pass
        return population.head(1)
