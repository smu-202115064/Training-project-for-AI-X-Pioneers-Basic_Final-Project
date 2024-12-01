import glob
import os
import pathlib
import typing

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import requests


sns.set_palette('Set2')
sns.set_style('whitegrid')

plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["savefig.transparent"] = True
plt.rcParams["savefig.bbox"] = 'tight'

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent

T_TICKS = typing.Union[typing.List[str], typing.List[int], typing.List[float]]
T_LABELS = typing.List[str]


def get_json(url: str) -> dict:
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_files(glob_pattern: str) -> typing.List[str]:
    return glob.glob(str(BASE_DIR / glob_pattern))


def get_file(path: str) -> str:
    return str(BASE_DIR / path)


def get_dataframe(file: str) -> pd.DataFrame:
    match (ext := os.path.splitext(file)[1]):
        case ".csv":
            return pd.read_csv(file)
        case ".xlsx":
            return pd.read_excel(file)
    raise ValueError(f"Unsupported file type: {ext}")


def get_merged_dataframe(files: typing.List[str]) -> pd.DataFrame:
    return pd.concat(map(get_dataframe, files), ignore_index=True)


def formatter(x: typing.Union[int, float]) -> str:
    if x.is_integer():
        return f"{int(x):,d}"
    return f"{x:,.2f}"


def formatted_ticks_kwargs(ticks: typing.List[int]) -> typing.Dict[str, typing.Union[T_TICKS, T_LABELS]]:
    return {
        'ticks': ticks,
        'labels': [formatter(x) for x in ticks],
    }
