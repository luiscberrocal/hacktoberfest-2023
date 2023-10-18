from pathlib import Path

import duckdb
import pandas as pd


def save_to_duckdb(df: pd.DataFrame, table_name: str, db_path: str) -> None:
    """Save dataframe to duckdb"""
    conn = duckdb.connect(db_path)
    conn.register('df', df)
    conn.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
    conn.close()


def get_dataframe(duckdb_file: Path, table_name: str) -> pd.DataFrame:
    conn = duckdb.connect(str(duckdb_file))
    df = conn.query(f'SELECT * FROM {table_name};').to_df()
    conn.close()
    return df
