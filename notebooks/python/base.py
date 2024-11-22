import glob
import os
import pathlib
import typing

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


sns.set_palette('husl')
sns.set_style('whitegrid')

plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent.parent


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
