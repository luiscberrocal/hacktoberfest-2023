# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ['02-cleanup']
product = None

# %%
import warnings

warnings.filterwarnings('ignore')

# %%
import pandas as pd
from sklearn.model_selection import train_test_split

# %%
df = pd.read_csv(upstream['02-cleanup']['clean_csv'])

df.head()

# %%
X = df.drop(['price'], axis=1)
y = df['price']

# %%

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# %%
train_data = X_train.join(y_train)
test_data = X_test.join(y_test)

# %%
train_data.to_csv(product['train_data'], index=False)
test_data.to_csv(product['test_data'], index=False)
