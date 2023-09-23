import numpy as np
from src.evolution_strategy.local_search import shift1_first_improvement


def ils(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    actual_vpl = individual[0]
    while True:
        individual = shift1_first_improvement(individual, dataset)

        if int(individual[0]) > actual_vpl:
            actual_vpl = individual[0]
        else:
            break
    return individual
