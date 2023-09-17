import pandas as pd
import random

from pandas import Series


def shift1(individual: pd.Series, dataset: pd.DataFrame) -> Series:
    shift_position = random.randint(0, 119)
    new_slope = dataset[(dataset['TAL'] == shift_position + 1)].sample(n=1)
    individual['solution'][shift_position] = new_slope['PRE'].values[0]

    return individual


def shift_with_mutation_factor(
        individual: pd.Series, dataset: pd.DataFrame, mutation_factor: float, shift_number: int
) -> Series:
    for i in range(0, shift_number):
        if round(random.uniform(0, 1), 2) <= mutation_factor:
            shift_position = random.randint(0, 119)
            new_slope = dataset[(dataset['TAL'] == shift_position + 1)].sample(n=1)
            individual['solution'][shift_position] = new_slope['PRE'].values[0]
    return individual


def shift_all(
        individual: pd.Series, dataset: pd.DataFrame, mutation_factor: float
) -> Series:
    for i in range(0, 120):
        if round(random.uniform(0, 1), 2) <= mutation_factor:
            new_slope = dataset[(dataset['TAL'] == i + 1)].sample(n=1)
            individual['solution'][i] = new_slope['PRE'].values[0]
    return individual


def mutation(individual: pd.Series, dataset: pd.DataFrame, mutation_factor: float, shift_number: int) -> pd.Series:
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
