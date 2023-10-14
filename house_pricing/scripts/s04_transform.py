# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
from src.db import get_dataframe, save_to_duckdb

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
upstream = ['s01_get']

# This is a placeholder, leave it as None
product = None
table_name = None
transformed_table_name = None

# %%
# your code here...
db_file = upstream['s01_get']['database']
df = get_dataframe(duckdb_file=db_file, table_name=table_name)

# %%
from sklearn.preprocessing import StandardScaler

features =  df.columns # ["col1", "col2", "col3", "col4"]
autoscaler = StandardScaler()
df[features] = autoscaler.fit_transform(df[features])


# %%
save_to_duckdb(df=df, table_name=transformed_table_name, db_path=upstream['s01_get']['database'])


# %%
import duckdb

conn = duckdb.connect(upstream['s01_get']['database'])
conn.sql('SHOW TABLES;')
conn.close()