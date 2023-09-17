import pandas as pd
import numpy as np
from src.utils.constants import MAX_YEAR_VOLUME, MIN_YEAR_VOLUME
import random


def generate_individual(dataset: pd.DataFrame) -> pd.DataFrame:
    try:
        solution = np.full(120, -1)
        vpl = 0
        planning_horizon = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0,
            9: 0,
            10: 0,
            11: 0,
            12: 0,
            13: 0,
            14: 0,
            15: 0,
            16: 0
        }

        slope_used = np.array([])

        index = 1
        while index < 17:
            if slope_used.size == 120:
                break
            if MIN_YEAR_VOLUME <= planning_horizon[index] <= MAX_YEAR_VOLUME:
                index += 1
                continue

            dataset_filtered = dataset[
                (dataset[str(index)] > 0) &
                (~dataset['TAL'].isin(slope_used)) &
                (dataset['VPL'].values[0] > 0)
            ]

            if dataset_filtered.empty:
                index += 1
                continue

            prescription_line = dataset_filtered.sample(n=1)

            slope_used = np.append(slope_used, prescription_line['TAL'].values[0])
            vpl += prescription_line['VPL'].values[0]
            solution[prescription_line['TAL'].values[0] - 1] = prescription_line['PRE'].values[0]
            planning_horizon[index] += prescription_line[str(index)].values[0]

            index += 1
            if index == 17 and slope_used.size < 120:
                index = 1

        return pd.DataFrame([
            {
                'solution': solution,
                'vpl': vpl,
                'planning_horizon': pd.DataFrame([planning_horizon])
            }
        ])
    except Exception as e:
        raise e
