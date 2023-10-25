import numpy as np
from src.evolution_strategy.fo import calculate_vpl
import random


def shift_any_best_improvement(individual: np.ndarray, dataset: np.ndarray, fields_numbers: np.ndarray) -> np.ndarray:
    original_vpl = individual[0]

    for i in fields_numbers:
        best_vpl = original_vpl
        best_field = individual[1][i]

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


def change_2_best_improvement(individual: np.ndarray, dataset: np.ndarray, fields: np.ndarray) -> np.ndarray:
    best_vpl = individual[0]
    best_field_0 = individual[1][fields[0]]
    best_field_1 = individual[1][fields[1]]

    for i in range(1, 82):
        individual[1][fields[0]] = i
        for j in range(1, 82):
            individual[1][fields[1]] = j

            calculate_vpl(individual, dataset)
            if individual[0] > best_vpl:
                best_vpl = individual[0]
                best_field_0 = i
                best_field_1 = j

    individual[0] = best_vpl
    individual[1][fields[0]] = best_field_0
    individual[1][fields[1]] = best_field_1

    return individual


def local_search(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    match random.randint(1, 11):
        case 1:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=1))
        case 2:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=2))
        case 3:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=3))
        case 4:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=4))
        case 5:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=5))
        case 6:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=6))
        case 7:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=7))
        case 8:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=8))
        case 9:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=9))
        case 10:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=10))
        case 11:
            return change_2_best_improvement(individual, dataset, np.random.randint(0, 120, size=2))
        case _:
            return individual
