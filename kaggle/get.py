import shutil
from pathlib import Path

from kaggle import settings
from kaggle.terminal_commands import run_commands


def configure_kaggle(envs_folder: Path):
    envs_file = envs_folder / 'kaggle.json'
    if not envs_file.exists():
        raise Exception('Kaggle configuration file not found')
    kaggle_folder = Path.home() / '.kaggle'
    kaggle_folder.mkdir(exist_ok=True)
    config_file = kaggle_folder / 'kaggle.json'
    if not config_file.exists():
        shutil.copy(envs_file, config_file)
        return True
    else:
        return False


def download_dataset(dataset_name: str, download_folder: Path) -> Path:
    command_list = ['kaggle', 'datasets', 'download', dataset_name, '-p', str(download_folder), '--unzip']
    results, errors = run_commands(command_list)
    for r in results:
        print(r)
    if len(errors):
        print('-' * 50)
        print('errors')
        for e in errors:
            print(e)


if __name__ == '__main__':
    #  kaggle datasets download joebeachcapital/house-prices
    configure_kaggle(settings.ENVS_FOLDER)
    dataset = 'joebeachcapital/house-prices-2001-2020'
    data_folder = Path(__file__).parent / 'data'
    data_folder.mkdir(exist_ok=True)

    file = download_dataset(dataset_name=dataset, download_folder=data_folder)
