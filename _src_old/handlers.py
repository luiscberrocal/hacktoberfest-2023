from pathlib import Path


def find_csv_file(folder: Path, csv_name: str) -> Path:
    csvs = folder.glob('**/*.csv')
    for csv in csvs:
        if csv.name == csv_name:
            return csv
