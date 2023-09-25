from numpy import ndarray
from src.utils.constants import MIN_YEAR_VOLUME, MAX_YEAR_VOLUME, PENALTY


def penalize(individual: ndarray):
    for year_plan in individual[2]:
        if year_plan < MIN_YEAR_VOLUME or year_plan > MAX_YEAR_VOLUME:
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
