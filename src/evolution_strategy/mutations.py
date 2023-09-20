import random
from numpy import ndarray


def shift1(individual: ndarray, dataset: ndarray) -> ndarray:
    shift_position = random.randint(0, 119)
    fields_filter = dataset[dataset[:, 0] == shift_position + 1]
    field = fields_filter[random.randint(0, fields_filter.shape[0] - 1)]
    individual[1][shift_position] = field[2]

    return individual


def shift_with_mutation_factor(
        individual: ndarray, dataset: ndarray, mutation_factor: float, shift_number: int
) -> ndarray:
    for i in range(0, shift_number):
        if round(random.uniform(0, 1), 2) <= mutation_factor:
            fields_filter = dataset[dataset[:, 0] == i + 1]
            field = fields_filter[random.randint(0, fields_filter.shape[0] - 1)]
            individual[1][i] = field[2]
    return individual


def shift_all(
        individual: ndarray, dataset: ndarray, mutation_factor: float
) -> ndarray:
    for i in range(0, 120):
        if round(random.uniform(0, 1), 2) <= mutation_factor:
            fields_filter = dataset[dataset[:, 0] == i + 1]
            field = fields_filter[random.randint(0, fields_filter.shape[0] - 1)]
            individual[1][i] = field[2]
    return individual


def mutation(individual: ndarray, dataset: ndarray, mutation_factor: float, shift_number: int) -> ndarray:
    match random.randint(1, 6):
        case 1:
            return shift1(individual, dataset)
        case 2:
            return shift_with_mutation_factor(individual, dataset, mutation_factor, shift_number)
        case 3:
            return shift_with_mutation_factor(individual, dataset, mutation_factor, 5)
        case 4:
            return shift_with_mutation_factor(individual, dataset, mutation_factor, 10)
        case 5:
            return shift_with_mutation_factor(individual, dataset, mutation_factor, 15)
        case 6:
            return shift_all(individual, dataset, mutation_factor)
        case _:
            return individual
