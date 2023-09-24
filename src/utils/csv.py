import numpy as np

from src.utils.constants import MIN_YEAR_VOLUME, MAX_YEAR_VOLUME


def save_result(results: np.ndarray, time: float, mu: float, mutation: float, generations: int):
    for result in results:

        solution = ''
        for s in result[1]:
            solution += str(s) + ' '

        planning_horizon = ''
        for p in result[2]:
            planning_horizon += str(p) + ' '

        with open(f'dataset/results.csv', "a") as file:
            file.write(
                f'\n{result[0]};{solution};{planning_horizon};{time};{mu};{mutation};{generations}'
            )

        is_within_range = (result[2] >= MIN_YEAR_VOLUME) & (result[2] <= MAX_YEAR_VOLUME)
        if is_within_range:
            with open(f'dataset/feasible_results.csv', "a") as file:
                file.write(
                    f'\n{result[0]};{solution};{planning_horizon};{time};{mu};{mutation};{generations}'
                )
