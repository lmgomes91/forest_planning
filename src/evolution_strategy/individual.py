import numpy as np
from numpy import ndarray
import random
from src.evolution_strategy.fo import calculate_vpl
from src.evolution_strategy.local_search import local_search
from src.evolution_strategy.mutations import mutation
from src.utils.constants import TOTAL_PRESCRIPTIONS


def generate_individual(_) -> list[int | ndarray[int] | ndarray]:
    solution = np.random.randint(1, TOTAL_PRESCRIPTIONS + 1, 120)
    vpl = 0
    planning_horizon = np.full(16, 0)

    return [vpl, solution, planning_horizon]


def create_descendant(individual: ndarray, dataset: ndarray, mutation_factor: float) -> ndarray:
    new_individual = mutation(individual, dataset, mutation_factor, random.randint(0, 119))
    calculate_vpl(new_individual, dataset)
    return local_search(new_individual, dataset)
