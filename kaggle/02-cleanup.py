# %% tags=["parameters"]
upstream = ['01-get']
product = None

# %%
import warnings
warnings.filterwarnings('ignore')

# %%
import re
import pandas as pd

# %%
df = pd.read_csv(upstream['01-get']['csv_file'])

# %%
df.info()

# %%
df.isna().sum()

# %%
# Rename columns to snake case
renamed_mapping = {}
for c in df.columns:
    new_c_name = re.sub('[^0-9a-zA-Z_]+', '', c)
    renamed_mapping[c] = new_c_name.lower()  # .replace(' ', '_').replace('(', '').replace(')', '')
renamed_mapping['targetprice_in_lacs'] = 'target_price_in_lacs'

df = df.rename(columns=renamed_mapping)

df.info()
# %%
# Extracting cities from address
def get_city(value):
    parts = value.split(',')
    return parts[-1:][0]

# Too many cities, heatmap not working.
# df['city'] = df['address'].apply(get_city)

# df['city'].value_counts()

# %%
df = df.drop(columns=['address'])

# %%
df['posted_by'].value_counts()

# %%
df['bhk_or_rk'].value_counts()

# %%
# df = pd.get_dummies(df, columns=['posted_by', 'bhk_or_rk', 'city'])
df = pd.get_dummies(df, columns=['posted_by', 'bhk_or_rk'])

# %%
df.head()

# %%
df.info()

# %%
for c in df.columns:
    if df[c].dtype == bool:
        print(f'{c} {df[c].dtype}')
        df[c] = df[c].astype(int)

df.info()

# %%
# 1. hot shoe encoding
# 2. Drop encoded columns
# 3. Extract city
# 4.
# %%

df.to_csv(product['clean_csv'], index=False)
