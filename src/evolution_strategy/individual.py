import numpy as np
from numpy import ndarray
import random
from src.evolution_strategy.mutations import mutation
from src.utils.constants import MIN_YEAR_VOLUME, MAX_YEAR_VOLUME, PENALTY, TOTAL_PRESCRIPTIONS


def generate_individual(_) -> list[int | ndarray[int] | ndarray]:
    solution = np.random.randint(1, TOTAL_PRESCRIPTIONS + 1, 120)
    vpl = 0
    planning_horizon = np.full(16, 0)

    return [vpl, solution, planning_horizon]


def penalize(individual: ndarray):
    for year_plan in individual[2]:
        if int(year_plan) < MIN_YEAR_VOLUME or int(year_plan) > MAX_YEAR_VOLUME:
            individual[0] -= PENALTY


def calculate_vpl(individual: ndarray, dataset: ndarray, reset_values: bool = True):
    if reset_values:
        individual[0] = 0
        for j in range(0, 16):
            individual[2][j] = 0

    for i in range(0, 120):
        condition_1 = dataset[:, 0] == i + 1
        condition_2 = dataset[:, 2] == individual[1][i]

        data_row = (dataset[condition_1 & condition_2])[0]

        individual[0] += data_row[19]

        for j in range(0, 16):
            individual[2][j] += data_row[j + 3]

    penalize(individual)


def create_individual_by_mutation(individual: ndarray, dataset: ndarray, mutation_factor: float) -> ndarray:
    new_individual = mutation(individual, dataset, mutation_factor, random.randint(0, 119))
    calculate_vpl(new_individual, dataset)
    return new_individual
