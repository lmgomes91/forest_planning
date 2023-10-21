from numpy import ndarray
import numpy as np
from src.utils.constants import MIN_YEAR_VOLUME, MAX_YEAR_VOLUME, PENALTY


def penalize(individual, planning_horizon):
    below_min = planning_horizon < MIN_YEAR_VOLUME
    above_max = planning_horizon > MAX_YEAR_VOLUME
    individual[0] -= np.sum((MAX_YEAR_VOLUME - planning_horizon) * PENALTY * below_min)
    individual[0] -= np.sum((planning_horizon - MAX_YEAR_VOLUME) * PENALTY * above_max)


def calculate_vpl(individual, dataset, reset_values=True):
    if reset_values:
        individual[0] = 0

    planning_horizon = np.zeros(16, dtype=int)

    for i in range(1, 121):
        condition_1 = dataset[:, 0] == i
        condition_2 = dataset[:, 2] == individual[1][i - 1]

        data_rows = dataset[condition_1 & condition_2]

        if data_rows.shape[0] > 0:
            data_row = data_rows[0]
            individual[0] += data_row[19]
            planning_horizon += data_row[3:19]

    penalize(individual, planning_horizon)
