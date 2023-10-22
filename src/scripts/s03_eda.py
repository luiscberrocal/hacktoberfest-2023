# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
import matplotlib.pyplot as plt
import pandas as pd

from src.db import get_dataframe

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

# %%

# %%
db_file = upstream['s01_get']['database']
df = get_dataframe(duckdb_file=db_file, table_name=table_name)

# %%
df.hist(figsize=(12, 9))
plt.tight_layout()
plt.show()

# %%
df.plot(kind='box', subplots=True, layout=(4,4), figsize=(15,8))
plt.title('Box-plot of Features')
plt.show()

# %%
X = df.drop(['median_house_value'], axis=1)
y = df['median_house_value']

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
df.describe()
