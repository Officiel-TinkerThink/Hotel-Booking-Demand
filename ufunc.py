import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class LogTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
    
    def fit(self, X, y=None):
        self.feature_names = X.columns if isinstance(X, pd.DataFrame) else [f'feature_{i}' for i in range(X.shape[1])]
        return self
    
    def transform(self, X):
        X_copy = X.copy()
        for column in self.columns:
            X_copy[column] = np.log(X_copy[column] + 1)
        return X_copy
    
    def get_feature_names_out(self, input_features=None):
        return self.feature_names
    
class ModeImputer(BaseEstimator, TransformerMixin):
    def __init__(self, column, missing_value="Undefined"):
        self.column = column
        self.missing_value = missing_value
    
    def fit(self, X, y=None):
        self.mode = X[self.column][X[self.column] != self.missing_value].mode()[0]
        self.feature_names = X.columns if isinstance(X, pd.DataFrame) else [f'feature_{i}' for i in range(X.shape[1])]
        return self
    
    def transform(self, X):
        X_copy = X.copy()
        X_copy[self.column] = X_copy[self.column].replace(self.missing_value, self.mode)
        return X_copy
    
    def get_feature_names_out(self, input_features=None):
        return self.feature_names