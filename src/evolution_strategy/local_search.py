import numpy as np
from src.evolution_strategy.fo import calculate_vpl
import random


def shift1_random_field_first_improvement(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    shift_position = random.randint(0, 119)
    fields_filter: np.ndarray = dataset[dataset[:, 0] == shift_position + 1]
    np.random.shuffle(fields_filter)

    actual_vpl = individual[0]
    old_field = individual[1][shift_position]

    for field in fields_filter:
        individual[1][shift_position] = field[2]
        calculate_vpl(individual, dataset)
        if individual[0] > actual_vpl:
            return individual

    individual[1][shift_position] = old_field
    individual[0] = actual_vpl

    return individual


def shift1_random_field_best_improvement(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    shift_position = random.randint(0, 119)
    fields_filter: np.ndarray = dataset[dataset[:, 0] == shift_position + 1]

    actual_vpl = individual[0]
    actual_field = individual[1][shift_position]
    for field in fields_filter:
        individual[1][shift_position] = field[2]
        calculate_vpl(individual, dataset)
        if individual[0] > actual_vpl:
            actual_vpl = individual[0]
            actual_field = individual[1][shift_position]
        else:
            individual[0] = actual_vpl
            individual[1][shift_position] = actual_field
    return individual


def shift_all_best_improvement(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    for i in range(0, 120):
        actual_vpl = individual[0]
        actual_field = individual[1][i]

        fields_filter: np.ndarray = dataset[dataset[:, 0] == i + 1]

        for field in fields_filter:
            individual[1][i] = field[2]
            calculate_vpl(individual, dataset)
            if individual[0] > actual_vpl:
                actual_vpl = individual[0]
                actual_field = individual[1][i]
            else:
                individual[0] = actual_vpl
                individual[1][i] = actual_field

    return individual


def shift_any_best_improvement(individual: np.ndarray, dataset: np.ndarray, fields_numbers: np.ndarray) -> np.ndarray:
    for i in fields_numbers:
        actual_vpl = individual[0]
        actual_field = individual[1][i]

        fields_filter: np.ndarray = dataset[dataset[:, 0] == i + 1]

        for field in fields_filter:
            individual[1][i] = field[2]
            calculate_vpl(individual, dataset)
            if individual[0] > actual_vpl:
                actual_vpl = individual[0]
                actual_field = individual[1][i]
            else:
                individual[0] = actual_vpl
                individual[1][i] = actual_field
    return individual


def local_search(individual: np.ndarray, dataset: np.ndarray) -> np.ndarray:
    match random.randint(0, 5):
        case 0:
            return shift1_random_field_first_improvement(individual, dataset)
        case 1:
            return shift1_random_field_best_improvement(individual, dataset)
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
