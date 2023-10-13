# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
from src.db import save_to_duckdb
from src.handlers import find_csv_file

table_name = ''
upstream = None

# %%

import pandas as pd

from src import settings

from src.kaggle import configure_kaggle, download_dataset

# %%


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
