
from __future__ import division

import numpy as np
import pandas as pd

"""
Five discretization Methods
Discretization will also perform over last column, i.e. the y-value
Input:
- pd.dataframe
Output:
- pd.dataframe

"""


def default(df):
    return equal_width(df)


def do_nothing(df):
    return df

def equal_frequency(df, groupSize=10):
    """
    by default, groupsize=10. i.e. discrete all into 10 groups. each group, value should be median of original values
    :param df:
    :param groupSize:
    :return:
    """
    for c_i in range(df.shape[1] - 1):
        if df.iloc[:, c_i].unique().shape[0] < groupSize:
            continue
        maps = pd.qcut(df.iloc[:, c_i], groupSize, duplicates='drop')
        map_v = np.zeros([df.shape[0], 1])
        for r_i, m in enumerate(maps):
            x = m.left
            y = m.right
            map_v[r_i] = (y + x) / 2
        df.iloc[:, c_i] = map_v

    return df


def equal_width(df, groupSize=10):
    """
    by default, groupsize=10. i.e. discrete all into 10 groups. each group, value should be median of original values
    :param df:
    :param groupSize:
    :return:
    """
    for c_i in range(df.shape[1] - 1):
        if df.iloc[:, c_i].unique().shape[0] < groupSize:
            continue
        maps = pd.cut(df.iloc[:, c_i], groupSize)
        map_v = np.zeros([df.shape[0], 1])
        for r_i, m in enumerate(maps):
            x = m.left
            y = m.right
            map_v[r_i] = (y + x) / 2
        df.iloc[:, c_i] = map_v

    return df


def entropy(df):
    """
    referece: Fayyad et al. "Multi-Interval Discretization of Continuous-Valued Attributes for Classification Learning"
    :param df:
    :return:
    """
    def calc_ent(vect):
        """
        Calculate the differential entropy. reference https://www2.isye.gatech.edu/~yxie77/ece587/Lecture17.pdf
        :param vect: np.array like vector. e.g. pandas.core.series.Series
        :return:
        """
        integers = map(int, vect)

    # warnings.warn("Currently entropy based discretization is NOT available. Will apply equal width")
    return equal_width(df)


def pkid(df):
    return equal_width(df)
