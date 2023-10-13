from numpy import ndarray

from src.evolution_strategy.local_search import local_search


def refine_better_solution(individual: ndarray, dataset: ndarray) -> ndarray:
    vpl = individual[0]
    while True:
        individual = local_search(individual, dataset)
        if vpl >= individual[0]:
            break
        else:
            vpl = individual[0]
    return individual
