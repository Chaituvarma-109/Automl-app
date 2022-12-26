import pandas as pd
import numpy as np


def columns_numerical_categorical(df: pd.DataFrame):
    numerical_cols = df.select_dtypes(include=[np.number])
    categorical_cols = df.select_dtypes(exclude=[np.number])

    return numerical_cols, categorical_cols
