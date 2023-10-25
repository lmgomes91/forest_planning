import random
from numpy import ndarray


def shift1(individual: ndarray) -> ndarray:
    shift_position = random.randint(0, 119)
    individual[1][shift_position] = random.randint(1, 81)

    return individual


def shift_with_mutation_factor(
        individual: ndarray, mutation_factor: float, shift_number: int
) -> ndarray:
    for i in range(0, shift_number):
        if round(random.uniform(0, 1), 2) <= mutation_factor:
            shift_position = random.randint(0, 119)
            individual[1][shift_position] = random.randint(1, 81)
    return individual


def shift_all(
        individual: ndarray, mutation_factor: float
) -> ndarray:
    for i in range(0, 120):
        if round(random.uniform(0, 1), 2) <= mutation_factor:
            individual[1][i] = random.randint(1, 81)
    return individual


def mutation(individual: ndarray, mutation_factor: float) -> ndarray:
    match random.randint(1, 9):
        case 1:
            return shift_with_mutation_factor(individual, mutation_factor, 1)
        case 2:
            return shift_with_mutation_factor(individual, mutation_factor, 2)
        case 3:
            return shift_with_mutation_factor(individual, mutation_factor, 3)
        case 4:
            return shift_with_mutation_factor(individual, mutation_factor, 4)
        case 5:
            return shift_with_mutation_factor(individual, mutation_factor, 5)
        case 6:
            return shift_with_mutation_factor(individual, mutation_factor, 6)
        case 7:
            return shift_with_mutation_factor(individual, mutation_factor, 7)
        case 8:
            return shift_with_mutation_factor(individual, mutation_factor, 8)
        case 9:
            return shift_with_mutation_factor(individual, mutation_factor, 9)
        case _:
            return individual
