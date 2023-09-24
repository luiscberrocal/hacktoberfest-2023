from pathlib import Path


def test_read_db(db_file:Path):
    assert db_file.exists()