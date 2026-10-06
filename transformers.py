from sklearn.base import BaseEstimator, TransformerMixin
 
 
class NegativeToNaN(BaseEstimator, TransformerMixin):
 
    def __init__(self, columns):
        self.columns = columns
 
    def fit(self, X, y=None):
        return self
 
    def transform(self, X):
        X = X.copy()
 
        X[self.columns] = X[self.columns].mask(
            X[self.columns] < 0
        )
 
        return X