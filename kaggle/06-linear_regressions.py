# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

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
upstream = ['05-split']

# This is a placeholder, leave it as None
product = None

import matplotlib.pyplot as plt
# %%
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression

# %%
train_data = pd.read_csv(upstream['05-split']['train_data'])
test_data = pd.read_csv(upstream['05-split']['test_data'])

# %%
# Correlation on train data
plt.figure(figsize=(18, 8))
sns.heatmap(train_data.corr(), annot=True, cmap='YlGnBu')
plt.show()

# %%
# Columns to drop for a linear refression
columns_to_drop = ['bhk_or_rk_BHK', 'bhk_or_rk_RK', 'latitude', 'longitude']
train_data = train_data.drop(columns=columns_to_drop, axis=1)
test_data = test_data.drop(columns=columns_to_drop, axis=1)

# %%
# Correlation on train data
plt.figure(figsize=(18, 8))
sns.heatmap(train_data.corr(), annot=True, cmap='YlGnBu')
plt.show()
# %%
X_train = train_data.drop(['price'], axis=1)
y_train = train_data['price']

# %%
X_test = test_data.drop(['price'], axis=1)
y_test = test_data['price']
# %%

# %%
linear_reg = LinearRegression()

linear_reg.fit(X_train, y_train)

# %%
score = linear_reg.score(X_test, y_test)

print(score)
