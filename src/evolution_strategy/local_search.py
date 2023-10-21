import numpy as np
from src.evolution_strategy.fo import calculate_vpl
import random


def shift_any_best_improvement(individual: np.ndarray, dataset: np.ndarray, fields_numbers: np.ndarray) -> np.ndarray:
    original_vpl = individual[0]
    original_fields = individual[1].copy()  # Make a copy to keep track of original fields

    for i in fields_numbers:
        best_vpl = original_vpl
        best_field = original_fields[i]

        for field in range(1, 82):
            individual[1][i] = field
            calculate_vpl(individual, dataset)

            if individual[0] > best_vpl:
                best_vpl = individual[0]
                best_field = individual[1][i]

        # Update the individual with the best improvement
        individual[0] = best_vpl
        individual[1][i] = best_field

    return individual


def local_search(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    match random.randint(1, 5):
        case 1:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=1))
        case 2:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=5))
        case 3:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=7))
        case 4:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=3))
        case 5:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=9))
        case _:
            return individual
