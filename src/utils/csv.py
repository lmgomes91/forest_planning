import numpy as np

from src.utils.constants import MIN_YEAR_VOLUME, MAX_YEAR_VOLUME


def save_result(results: np.ndarray, time: float, mu: float, mutation: float, generations: int):
    for result in results:

        solution = ''
        for s in result[1]:
            solution += str(s) + ' '

        with open(f'dataset/results.csv', "a") as file:
            file.write(
                f'\n{result[0]};{solution};{time};{mu};{mutation};{generations}'
            )
