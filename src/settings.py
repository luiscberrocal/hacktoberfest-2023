from pathlib import Path

ROOT_FOLDER = Path(__file__).parent.parent

APP_FOLDER = Path(__file__).parent

ENVS_FOLDER = ROOT_FOLDER / ".envs"

DATA_FOLDER = APP_FOLDER / "data"

PROJECT_DATA_FOLDER = DATA_FOLDER / "california-housing-prices-data-extra-features"
