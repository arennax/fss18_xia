
from __future__ import division

import numpy as np
import pandas as pd
import warnings
import pdb

from sklearn import linear_model

"""
Use last column as target

input
- pd.dataframe including closest rows
- row pandas.core.series.Series
- dists: see analogies second return

output is a float
"""


def default(df, row=None, dists=None):
    return median_adaptation(df)


def median_adaptation(df, row=None, dists=None):
    """
    return the median of y-value
    :param df:
    :return:
    """
    Y = df.iloc[:, -1]
    return np.median(Y)


def mean_adaptation(df, row=None, dists=None):
    """
    return the mean of y-value
    :param df:
    :return:
    """
    Y = df.iloc[:, -1]
    return np.mean(Y)


def second_learner_adaption(df, row, dists=None):
    """
    Using linear regression to make prediction
    :param df:
    :return:
    """
    warnings.filterwarnings(action="ignore", module="scipy",
                            message="^internal gelsd")  # https://github.com/scipy/scipy/issues/5998
    clf = linear_model.LinearRegression()
    clf.fit(df.iloc[:, :-1], df.iloc[:, -1])
    res = float(clf.predict([row.tolist()[:-1]])[0])
    return res


def weighted_mean(df, row, dists):
    """
    - Report a weighted mean wehre the nearer analogies are weighted higher than those further away
    - Reference: Mendes et al. A comparative study of cost estimation models for web hypermedia applications
    :param df:
    :return:
    """
    if df.shape[0] <= 2 or sum(dists) == 0:
        return mean_adaptation(df)

    Y = df.iloc[:, -1]
    # normalize
    dists = pd.Series(dists)
    dists = sum(dists) - dists
    dists = dists / sum(dists)

    # weighted sum
    res = sum(dists.tolist() * Y)
    return res
