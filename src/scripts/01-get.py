# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs

table_name = ''
upstream = None

# %%
from pathlib import Path

import duckdb
import pandas as pd

from src import settings

from src.kaggle import configure_kaggle, download_dataset

# %%
def save_to_duckdb(df: pd.DataFrame, table_name: str, db_path: str) -> None:
    """Save dataframe to duckdb"""
    conn = duckdb.connect(db_path)
    conn.register('df', df)
    conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
    conn.close()


# %%
def find_csv_file(folder: Path, csv_name: str) -> Path:
    csvs = folder.glob('**/*.csv')
    for csv in csvs:
        if csv.name == csv_name:
            return csv


# %%
configure_kaggle(settings.ENVS_FOLDER)
ds_owner = 'akash14'
ds_name = 'house-price-dataset'
data_folder = settings.DATA_FOLDER
data_folder.mkdir(exist_ok=True)
fldr = download_dataset(owner=ds_owner, dataset_name=ds_name, download_folder=data_folder)
print(f'Data folder: {fldr}')
csv_file = find_csv_file(fldr, 'Train.csv')
df = pd.read_csv(csv_file)
df.to_csv(product['csv_file'], index=False)
save_to_duckdb(df=df, table_name=table_name, db_path=product['database'])

print(f'CSV: {csv_file}')

# %%
df.head()
