import numpy as np
from src.evolution_strategy.individual import calculate_vpl


def shift1_first_improvement(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    clone = individual.copy()

    for i in range(0, 120):
        data_field = dataset[dataset[:, 0] == i + 1]
        for field in data_field:
            clone[1][i] = field[2]
            calculate_vpl(clone, dataset)
            if clone[0] > individual[0]:
                return clone

    return individual


