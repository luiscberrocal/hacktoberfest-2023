import subprocess
from pathlib import Path

from kaggle.terminal_commands import run_commands


def download_dataset(dataset_name: str, download_folder: Path) -> Path:
    command_list = ['kaggle', 'datasets', 'download', dataset_name] #, '-p', str(download_folder)]
    # command_list = ['which', 'kaggle']
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
    dataset = 'joebeachcapital/house-prices'
    data_folder = Path(__file__).parent / 'data'
    data_folder.mkdir(exist_ok=True)

    file = download_dataset(dataset_name=dataset, download_folder=data_folder)
    # cmds = ['kaggle', 'datasets', 'download', dataset] #, '-p', str(download_folder)]
    # d = subprocess.call(cmds)
    # print(d)
