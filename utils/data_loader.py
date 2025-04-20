# utils/data_loader.py

import pandas as pd

def load_and_preprocess(file_path: str):
    df = pd.read_csv(file_path, parse_dates=['Timestamp'])
    df.fillna(method='ffill', inplace=True)
    return df
