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


def download_dataset(owner: str, dataset_name: str, download_folder: Path) -> Path:
    dataset = f'{owner}/{dataset_name}'
    folder = download_folder / dataset_name
    folder.mkdir(exist_ok=True)

    command_list = ['kaggle', 'datasets', 'download', dataset, '-p', str(folder), '--unzip']
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
    ds_owner = 'fedesoriano'
    ds_name = 'california-housing-prices-data-extra-features'
    data_folder = Path(__file__).parent / 'data'
    data_folder.mkdir(exist_ok=True)

    file = download_dataset(owner=ds_owner, dataset_name=ds_name, download_folder=data_folder)
