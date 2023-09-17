import pandas as pd
import numpy as np
from pandas import Series
import random
from src.evolution_strategy.mutations import mutation
from src.utils.constants import MIN_YEAR_VOLUME, MAX_YEAR_VOLUME, PENALTY


def generate_individual(dataset: pd.DataFrame) -> Series:
    solution = np.full(120, -1)
    vpl = 0
    planning_horizon = np.full(16, 0)

    for i in range(0, 120):
        prescription_line = dataset[(dataset['TAL'] == i + 1)].sample(n=1)

        vpl += prescription_line['VPL'].values[0]
        solution[prescription_line['TAL'].values[0] - 1] = prescription_line['PRE'].values[0]

        for j in range(1, 17):
            planning_horizon[j - 1] += prescription_line[str(j)].values[0]

    individual = Series(
        {
            'solution': solution,
            'vpl': vpl,
            'planning_horizon': planning_horizon
        }
    )
    penalize(individual)

    return individual


def penalize(individual: pd.Series):
    for year_plan in individual['planning_horizon']:
        if year_plan == 0:
            individual['vpl'] = 0
            break
        elif int(year_plan) < MIN_YEAR_VOLUME or int(year_plan) > MAX_YEAR_VOLUME:
            individual['vpl'] -= PENALTY


def recalculate_vpl(individual: pd.Series, dataset: pd.DataFrame):
    individual['vpl'] = 0
    for j in range(0, 16):
        individual['planning_horizon'][j] = 0

    for i in range(0, 120):
        condition1 = dataset['PRE'] == individual['solution'][i]
        condition2 = dataset['TAL'] == i + 1

        actual_slope = dataset[condition1 & condition2]

        individual['vpl'] += actual_slope['VPL'].values[0]
        for j in range(1, 17):
            individual['planning_horizon'][j - 1] += actual_slope[str(j)].values[0]

    penalize(individual)


def create_individual_by_mutation(individual: pd.Series, dataset: pd.DataFrame, mutation_factor: float) -> pd.Series:
    new_individual = mutation(individual.copy(deep=True), dataset, mutation_factor, random.randint(0, 119))
    recalculate_vpl(new_individual, dataset)
    return new_individual
