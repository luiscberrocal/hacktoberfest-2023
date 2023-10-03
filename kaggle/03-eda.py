# %% tags=["parameters"]
# declare a list tasks whose products you want to use as inputs
upstream = ['02-cleanup']
product = None

import matplotlib.pyplot as plt
# %%
import pandas as pd
import seaborn as sns

# log convert non gaussian columns?
# df['x'] = np.log(df['x'] +1)
# df.hist()

# %%
df = pd.read_csv(upstream['02-cleanup']['clean_csv'])

df.head()

# %%
df.corr()

# %%
plt.figure(figsize=(18, 8))
sns.heatmap(df.corr(), annot=True, cmap='YlGnBu')
plt.show()

# %%
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='targetprice_in_lacs', palette='flare')
plt.show()
# %%
df.hist(figsize=(12, 9))
plt.tight_layout()
plt.show()
