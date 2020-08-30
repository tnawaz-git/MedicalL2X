"""
Script for generate dataframe for the heart failure dataset

"""
from __future__ import print_function
import numpy as np
import pandas as pd


def generate_heart_data():
    """
    Reads the heart data.
    """
    df = pd.read_csv('./heart_dataset.csv', error_bad_lines=False)
    Y = df['DEATH_EVENT']    # response variable
    X = df.iloc[:, :-1]      # independent variables
    X = X.to_numpy()
    y = np.zeros((Y.size, Y.max() + 1))
    y[np.arange(Y.size), Y] = 1
    print(X.shape, y.shape)
    return X, y


def generate_data(n=100, datatype='', seed=0, val = False):
    """
    Generate data (X,y)
    Args:
        n(int): number of samples
        datatype(string): The type of data
        seed: random seed used
    Return:
        X(float): [n,d].
        y(float): n dimensional array.
    """

    np.random.seed(seed)

    datatypes = None

    if datatype == 'heart':
        X, y = generate_heart_data()

    return X, y, datatypes
