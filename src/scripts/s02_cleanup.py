# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
import duckdb

from src.db import get_dataframe, save_to_duckdb
import re
import seaborn as sns
import matplotlib.pyplot as plt

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
upstream = ["s01_get"]

# This is a placeholder, leave it as None
product = None
table_name = None

# %%
# your code here...
db_file = upstream["s01_get"]["database"]
df = get_dataframe(duckdb_file=db_file, table_name=table_name)

# %%
df.shape

# %%
df.info()

# %%
renamed_mapping = {}
for c in df.columns:
    new_c_name = re.sub("[^0-9a-zA-Z_]+", "", c)
    renamed_mapping[c] = new_c_name.lower()

df = df.rename(columns=renamed_mapping)

df.info()

# %%
df.isna().sum()

# %%
df.hist(figsize=(12, 9))
plt.tight_layout()
plt.show()

# %%
plt.figure(figsize=(18, 8))
sns.heatmap(df.corr(), annot=True, cmap="YlGnBu")
plt.show()

# %%
save_to_duckdb(df=df, table_name=table_name, db_path=db_file)

# %%

conn = duckdb.connect(db_file)
conn.sql(f"DESCRIBE {table_name};")
