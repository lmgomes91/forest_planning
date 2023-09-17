from typing import Tuple, Dict

import pandas as pd
import numpy as np
from numpy import ndarray


def generate_individual(dataset: pd.DataFrame) -> dict[str, ndarray | int]:
    solution = np.full(120, -1)
    vpl = 0
    planning_horizon = np.full(16, 0)

    for i in range(0, 120):
        prescription_line = dataset[(dataset['TAL'] == i + 1)].sample(n=1)

        vpl += prescription_line['VPL'].values[0]
        solution[prescription_line['TAL'].values[0] - 1] = prescription_line['PRE'].values[0]

        for j in range(1, 17):
            planning_horizon[j - 1] += prescription_line[str(j)].values[0]

    return {
        'solution': solution,
        'vpl': vpl,
        'planning_horizon': planning_horizon
    }


