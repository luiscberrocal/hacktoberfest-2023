# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---
import pickle
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

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
transformed_table_name = None

# %%
# your code here...

# %%

db_file = upstream['s01_get']['database']
df = get_dataframe(duckdb_file=db_file, table_name=transformed_table_name)

df.shape

# %%
X = df.drop(['median_house_value'], axis=1)
y = df['median_house_value']

# %%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# %%
rfr_model = RandomForestRegressor(n_estimators = 30)

rfr_model.fit(X_test, y_test)

# %%
y_pred_rfr = rfr_model.predict(X_test)

# %%
mse_rfr = mse(y_test,y_pred_rfr)
mae_rfr = mae(y_test,y_pred_rfr)
r2_rfr = r2_score(y_test,y_pred_rfr)

print(f'RMSE: {np.sqrt(mse_rfr):,.2f}')
print(f'MAE: {mae_rfr:,.2f}')
print(f'R2 : {r2_rfr:,.2f}')

# %%
model_file = Path(product['model_file'])
with open(model_file, 'wb') as f:
    pickle.dump(product['model_file'], f)

print(f'Model file: {model_file} exists: {model_file.exists()}')
