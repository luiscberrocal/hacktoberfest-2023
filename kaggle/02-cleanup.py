# %% tags=["parameters"]
upstream = ['01-get']
product = None

# %%
import sys
import os
import pandas as pd
import seaborn as sns
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt


# %%
df = pd.read_csv(upstream['01-get']['csv_file'])

# %%
df.info()

# %%
df.isna().sum()
