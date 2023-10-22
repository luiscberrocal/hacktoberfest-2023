from pathlib import Path
from typing import Tuple

import pandas as pd
from sklearn.preprocessing import StandardScaler


def find_csv_file(folder: Path, csv_name: str) -> Path:
    csvs = folder.glob('**/*.csv')
    for csv in csvs:
        if csv.name == csv_name:
            return csv


def transformation_handler(x_df: pd.DataFrame) -> Tuple[pd.DataFrame, StandardScaler]:
    features = x_df.columns
    autoscaler = StandardScaler()
    x_df[features] = autoscaler.fit_transform(x_df[features])
    return x_df, autoscaler

