import pandas as pd


class DataValidation:
    def __init__(self, data_set: pd.DataFrame):
        self.df = data_set
        self.null_cols: list = []

    def check_null_values(self) -> pd.DataFrame:
        for col in self.df.columns:
            null_bool = self.df[col].isna().any()
            if null_bool:
                self.impute_null_values(col)

        return self.df

    def impute_null_values(self, cols: pd.Series) -> None:
        if self.df[cols].dtype == 'object':
            self.df[cols].fillna(self.df[cols].mode()[0], inplace=True)
        else:
            self.df[cols].fillna(self.df[cols].median(), inplace=True)

    def outliers(self) -> pd.DataFrame:
        for col in self.df.columns:
            IQR = self.df[col].quantile(0.75) - self.df[col].quantile(0.25)
            lower_boundary = self.df[col].quantile(0.25) - (1.5 * IQR)
            upper_boundary = self.df[col].quantile(0.75) + (1.5 * IQR)

            self.df.loc[self.df[col] >= upper_boundary, col] = upper_boundary
            self.df.loc[self.df[col] <= lower_boundary, col] = lower_boundary

        return self.df
