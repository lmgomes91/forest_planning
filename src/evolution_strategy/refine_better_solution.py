from numpy import ndarray

from src.evolution_strategy.local_search import shift1_best_improvement


def refine_better_solution(individual: ndarray, dataset: ndarray) -> ndarray:
    vpl = individual[0]
    while True:
        individual = shift1_best_improvement(individual, dataset)
        if vpl >= individual[0]:
            break
        else:
            vpl = individual[0]
    return individual
