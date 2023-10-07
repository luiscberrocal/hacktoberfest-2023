from pathlib import Path

import duckdb


def test_read_db(db_file):
    assert db_file.exists()
    con = duckdb.connect(str(db_file))
    r = con.sql('SHOW ALL TABLES;')
    print(r)