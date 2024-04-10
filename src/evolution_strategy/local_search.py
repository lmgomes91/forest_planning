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


def shift_any_first_improvement(individual: np.ndarray, dataset: np.ndarray, fields_numbers: np.ndarray) -> np.ndarray:
    original_vpl = individual[0]
    has_improved = False
    for i in fields_numbers:
        vpl = original_vpl
        field = individual[1][i]

        for field in range(1, 82):
            individual[1][i] = field
            calculate_vpl(individual, dataset)

            if individual[0] > vpl:
                has_improved = True
                break

        if not has_improved:
            individual[0] = vpl
            individual[1][i] = field

    return individual


def shift1_best_improvement(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    best_vpl = individual[0]
    best_field = -1
    actual_vpl = individual[0]
    field_to_change = -1

    for i in range(0, 120):
        actual_field = individual[1][i]
        for j in range(1, 82):
            individual[1][i] = j
            calculate_vpl(individual, dataset)
            if individual[0] > best_vpl:
                best_vpl = individual[0]
                best_field = j
                field_to_change = i

            individual[1][i] = actual_field
            individual[0] = actual_vpl

    if best_field > 0:
        individual[0] = best_vpl
        individual[1][field_to_change] = best_field

    return individual


def local_search(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    match random.randint(1, 10):
        case 1:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=5))
        case 2:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=10))
        case 3:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=15))
        case 4:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=20))
        case 5:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=25))
        case 6:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=30))
        case 7:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=35))
        case 8:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=45))
        case 9:
            return shift_any_best_improvement(individual, dataset, np.random.randint(0, 120, size=50))
        case _:
            return individual
