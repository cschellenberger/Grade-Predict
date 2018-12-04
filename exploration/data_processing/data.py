import logging
import numpy as np
from sklearn.preprocessing import OneHotEncoder


class DummyEncoder:
    """Encode a DataFrame to binary categories

    Parameters
    ----------
    df : pandas DataFrame to encode

    Methods
    -------
    fit : for finding the categories to encode using
        sklearn.preprocessing.OneHotEncoder
    transform : for generating the binary representation of the
        encoded categories and dropping the first feature of the
        category
    fit_transform : for the execution of both the fit and transform
        methods

    Returns
    -------
    a numpy.ndarray of binary values for each encoded category
    """

    def __init__(self, drop_first=True):
        self.num_columns = 0
        self.encoders = []
        self.feature_names = []
        self.drop_first = drop_first

    def fit(self, df):
        for i in df.columns:
            ohe = OneHotEncoder(categories='auto')
            self.num_columns = + 1
            ohe.fit(df[i].values.reshape(-1, 1))
            self.encoders.append(ohe)
            self.feature_names.append(list(ohe.get_feature_names()))

    def transform(self, df):
        results = []
        for i, c in enumerate(df.columns):
            results.append(self.encoders[i]. \
                           transform(df[c].values.reshape(-1, 1)). \
                           toarray()[:, int(self.drop_first):])
        return np.hstack(results)

    def fit_transform(self, df):

        logging.info("Fitting and transforming the features of the DataFrame")

        self.fit(df)
        return self.transform(df)