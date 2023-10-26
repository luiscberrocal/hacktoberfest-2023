# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
from pathlib import Path
import pandas as pd

from src import settings
from src.db import save_to_duckdb
from src.handlers import find_csv_file
from src.kaggle import configure_kaggle, download_dataset

# Add description here
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %%
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = None

# This is a placeholder, leave it as None
product = None
table_name = None
kaggle_owner = None
kaggle_dataset_name = None
kaggle_csv = None


# %%
# your code here...
configure_kaggle(settings.ENVS_FOLDER)
data_folder = Path(product["csv_file"]).parent
data_folder.mkdir(exist_ok=True)
fldr = download_dataset(
    owner=kaggle_owner, dataset_name=kaggle_dataset_name, download_folder=data_folder
)
print(f"Data folder: {fldr}")
csv_file = find_csv_file(fldr, kaggle_csv)
df = pd.read_csv(csv_file)
df.to_csv(product["csv_file"], index=False)
save_to_duckdb(df=df, table_name=table_name, db_path=product["database"])

print(f"CSV: {csv_file}")

# %%
df.head()
