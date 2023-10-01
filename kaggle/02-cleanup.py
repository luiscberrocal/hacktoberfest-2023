# %% tags=["parameters"]
upstream = ['01-get']
product = None

import re

# %%
import pandas as pd

# %%
df = pd.read_csv(upstream['01-get']['csv_file'])

# %%
df.info()

# %%
df.isna().sum()

## %%
# Rename columns to snake case
renamed_mapping = {}
for c in df.columns:
    new_c_name = re.sub('[^0-9a-zA-Z_]+', '', c)
    renamed_mapping[c] = new_c_name.lower()  # .replace(' ', '_').replace('(', '').replace(')', '')
renamed_mapping['targetprice_in_lacs'] = 'target_price_in_lacs'

df = df.rename(columns=renamed_mapping)

df.info()

# %%
