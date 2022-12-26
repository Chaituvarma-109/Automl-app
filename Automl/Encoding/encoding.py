import numpy as np
import pandas as pd

from sklearn.preprocessing import OrdinalEncoder

from Automl.utils.util import columns_numerical_categorical


class Encoding:
    def __init__(self, data_set: pd.DataFrame):
        self.df = data_set

    def get_unique_values_cols(self, col: pd.Series) -> np.ndarray:
        return self.df[col].unique()

    def encoding(self, output: str):
        drop_df = self.df.drop([output], axis=1)
        y = self.df[output]
        # _, cat_cols = columns_numerical_categorical(drop_df)
        cat_cols = [i for i in drop_df.columns if drop_df[i].dtypes == 'O']
        drop_df = pd.get_dummies(drop_df, columns=cat_cols, drop_first=True)

        self.df = pd.concat([drop_df, y], ignore_index=True)

        return self.df
