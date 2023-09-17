import pandas as pd
import os


def open_dataset() -> pd.DataFrame:
    try:
        return pd.read_csv(
            f'{os.getcwd()}/dataset/forest_planning_data.csv'
        )
    except Exception as e:
        raise e
