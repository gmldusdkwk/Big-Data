import pandas as pd


def pandas_index():
    df = pd.read_csv('data-netflix.csv', encoding='CP949')
    return df
