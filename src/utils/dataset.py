import pandas as pd
import os
from numpy import ndarray


def open_dataset() -> ndarray:
    try:
        return pd.read_csv(
            f'{os.getcwd()}/dataset/forest_planning_data.csv'
        ).to_numpy()
    except Exception as e:
        raise e
