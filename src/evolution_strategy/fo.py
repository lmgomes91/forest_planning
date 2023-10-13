from numpy import ndarray
import numpy as np
from src.utils.constants import MIN_YEAR_VOLUME, MAX_YEAR_VOLUME, PENALTY
from numba import jit


@jit
def penalize(individual: ndarray, planning_horizon: ndarray):
    for year_plan in planning_horizon:
        if year_plan < MIN_YEAR_VOLUME:
            individual[0] -= (MAX_YEAR_VOLUME - year_plan) * PENALTY
        elif year_plan > MAX_YEAR_VOLUME:
            individual[0] -= (year_plan - MAX_YEAR_VOLUME) * PENALTY


@jit
def calculate_vpl(individual: ndarray, dataset: ndarray, reset_values: bool = True):
    if reset_values:
        individual[0] = 0

    planning_horizon = np.full(16, 0)
    for i in range(0, 120):
        condition_1 = dataset[:, 0] == i + 1
        condition_2 = dataset[:, 2] == individual[1][i]

        data_row = (dataset[condition_1 & condition_2])[0]

        individual[0] += data_row[19]

        for j in range(0, 16):
            planning_horizon[j] += data_row[j + 3]

    penalize(individual, planning_horizon)
