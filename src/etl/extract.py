# + tags=["parameters"]
# declare a list tasks whose products you want to use as inputs

upstream = None

from pathlib import Path

import json
from time import time

import duckdb
import pandas as pd
import requests


# +
def extract_data(url: str, max_page_count: int = 3, page_size: int = 2_000) -> pd.DataFrame:
    """Extract data from URL and return a dataframe"""
    d_df = None
    print('Started extractoion')
    for page in range(max_page_count):
        offset = page * page_size
        start = time()
        paged_url = f'{url}?$limit={page_size}&$offset={offset}'
        # print(f'Calling {paged_url}')
        response = requests.get(paged_url)
        elapsed = time() - start
        print(f'Url: {paged_url} time: {elapsed:,.2f} seconds')
        if response.status_code == 200:
            if d_df is None:
                d_df = pd.DataFrame(json.loads(response.content))
            else:
                # pos = len(d_df)
                # d_df.loc[pos] = json.loads(response.content)
                id_df = pd.DataFrame(json.loads(response.content))
                d_df = pd.concat([d_df, id_df])

        else:
            error_message = f'Error calling {paged_url}. Status code {response.status_code} error: {response.content}'
            raise Exception(error_message)
    return d_df


# +
# write a function that saves a dataframe to duckdb
def save_to_duckdb(df, table_name, db_path):
    """Save dataframe to duckdb"""
    conn = duckdb.connect(db_path)
    conn.register('df', df)
    conn.execute(f"CREATE TABLE {table_name} AS SELECT * FROM df")
    conn.close()

# +
if __name__ == "__main__":
    delete_if_exists = True
    data_folder = Path(__file__).parent / 'data'
    duckdb.default_connection.execute("SET GLOBAL pandas_analyze_sample=100000")

    # Extract data from URL
    # Source : https://data.cityofnewyork.us/Social-Services/311-Service-Requests-from-2010-to-Present/erm2-nwe9
    data_url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    df = extract_data(data_url)

    table_name = "nycitydata"

    # Saving intermediate Parquet
    parquet_file = data_folder / f'{table_name}.parquet'
    df.to_parquet()
    
    # Save to duckdb
    db_path =  data_folder / f"{table_name}.duckdb"
    if delete_if_exists and db_path.exists():
        db_path.unlink()

    save_to_duckdb(df, table_name, db_path.root)

