# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ['02-cleanup']
product = None

# %%
import warnings

warnings.filterwarnings('ignore')

# %%
import pandas as pd

# %%
df = pd.read_csv(upstream['02-cleanup']['clean_csv'])

df.head()
# %%
# Scaling
# df['bhk_no'] = np.log(df['bhk_no'] + 1)

# %%
df.to_csv(product['transformed_csv'], index=False)
