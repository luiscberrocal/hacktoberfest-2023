# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
import pandas as pd
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
df.shape

# %%
X = df.drop(['median_house_value'], axis=1)
y = df['median_house_value']

# %%
from sklearn.preprocessing import StandardScaler

features = X.columns  # ["col1", "col2", "col3", "col4"]
autoscaler = StandardScaler()
X[features] = autoscaler.fit_transform(X[features])

# %%
# --Variance Inflation Factor
from statsmodels.stats.outliers_influence import variance_inflation_factor

vif_df = pd.DataFrame()
vif_x = X.copy()
vif_df["feature"] = vif_x.columns
vif_df["VIF"] = [variance_inflation_factor(vif_x.values, i)
                 for i in range(len(vif_x.columns))]

vif_df.head(10)

# %%
X = X.join(y)
# %%
X.shape

# %%
X.describe()

# %%
save_to_duckdb(df=X, table_name=transformed_table_name, db_path=upstream['s01_get']['database'])


# %%
import duckdb

conn = duckdb.connect(upstream['s01_get']['database'])
conn.sql('SHOW TABLES;')

# %%

conn.close()