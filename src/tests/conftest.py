from pathlib import Path

import pytest


@pytest.fixture
def db_file() -> Path:
    file = Path(__file__).parent.parent / 'etl' / 'data.duckdb'
    return file
