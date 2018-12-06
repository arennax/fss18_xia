
from __future__ import division
import numpy as np
import warnings
import pdb

"""
three case subset selectors
input is a pd.dataframe
output format is same as input
"""


def default(train):
    return prototype(train)


def rm_noting(train):
    return train


def outlier(train):
    # for each row, if any feature of that row fall outside 3-sigma (normal dist),
    # then remove that row of data

    for r_i in range(train.shape[1] - 1):  # ignoring the last column, i.e. the y-value
        column = train.iloc[:, r_i]
        train = train[np.abs(column - column.mean()) <= 3 * column.std()]

    return train


def prototype(train):
    # prototype find, or generate a set of representative examples that replace the training cases
    # typically, prototype generation removes most of the training data
    # here, we use Change et al. "Finding prototypes for nearest neighbor classifiers", 1974

    # warnings.warn("Currently prototype subset selector is NOT available. Will apply outlier")
    return outlier(train)
