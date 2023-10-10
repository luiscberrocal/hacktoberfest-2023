# %% tags=["parameters"]
upstream = ['01-get']
product = None

# %%
import warnings

warnings.filterwarnings('ignore')

# %%
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
# renamed_mapping['targetprice_in_lacs'] = 'target_price_in_lacs'

df = df.rename(columns=renamed_mapping)

# %%
# Convert price to dolllars 1 lac == 1,397
df['price'] = df['targetprice_in_lacs'] * 1_397

# Convert square_ft to square meters
df['area_m2'] = df['square_ft'] * 0.092903

# %%
df = df.drop(columns=['square_ft', 'targetprice_in_lacs'])

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

df.to_csv(product['clean_csv'], index=False)

# %%
sns.scatterplot(data=df, x="price", y="area_m2")
plt.title(f'Price vs Area before cleaning outliers (count {df.shape[0]:,})')
plt.show()

# %%
# There seem to be outliers in price

# Z score
from scipy import stats
import numpy as np

df['z_score'] = np.abs(stats.zscore(df['price']))

# %%
''' Detection '''


def clean_with_iqr(data_frame: pd.DataFrame, column: str) -> pd.DataFrame:
    # IQR
    # Calculate the upper and lower limits
    Q1 = data_frame[column].quantile(0.25)
    Q3 = data_frame[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    # Create arrays of Boolean values indicating the outlier rows
    upper_array = np.where(data_frame[column] >= upper)[0]
    lower_array = np.where(data_frame[column] <= lower)[0]

    # Removing the outliers
    data_frame.drop(index=upper_array, inplace=True)
    data_frame.drop(index=lower_array, inplace=True)
    return data_frame

# %%
# outlier_index = df.loc[df['z_score'] > 3.0].index
# df = clean_with_iqr(data_frame=df, column='price')
# df = clean_with_iqr(data_frame=df, column='area_m2')
# df = df.drop(outlier_index)
print(df.shape)
out_area = df.loc[df['area_m2'] >= 10_000.00]
df = df.drop(index=out_area.index)

# %%
sns.scatterplot(data=df, x="price", y="area_m2")
plt.title(f'Price vs Area after cleaning outliers (count {df.shape[0]:,})')
plt.show()

# %%

df.describe()