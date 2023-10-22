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
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from src.app.schema import House
from src.db import get_dataframe
from src.handlers import transformation_handler

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
    pickle.dump(rfr_model, f)

print(f'Model file: {model_file} exists: {model_file.exists()}')
# %%

with open(model_file, 'rb') as f:
    pickled_model = pickle.load(f)


# %%

house_data_test = {
    'median_income': 3.87,
    "median_age": 28.6,
    "tot_rooms": 5,
    "tot_bedrooms": 3,
    "population": 1425,
    "households": 500,
    "latitude": 35.6,
    "longitude": -119.56,
    "distance_to_coast": 40_509.3,
    "distance_to_la": 269_422,
    "distance_to_sandiego": 398_000,
    "distance_to_sanjose": 34_000.0,
    "distance_to_sanfrancisco": 346_000.0,
}
house = House(**house_data_test)

# %%
X_to_predict = pd.DataFrame.from_records([house.dict(exclude={'median_house_value'})])

X_to_predict.head()

# %%

X_to_predict_t, scaler = transformation_handler(X_to_predict)

X_to_predict_t.head()

# %%
# FIXME this is wrong need to scale first
y_pred_pickled = pickled_model.predict(X_to_predict)

print(y_pred_pickled)
