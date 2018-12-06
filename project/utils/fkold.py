
from __future__ import division

import random

import numpy
from scipy.io import arff
from sklearn.model_selection import KFold
from sklearn.utils import shuffle


def KFoldSplit(arff_file_name, folds=3):
    """
    Split the dataset in cross-validation

    :param arff_file_name:
    :param folds:
    :return:
    """
    data, meta = arff.loadarff(arff_file_name)
    random.shuffle(data)
    indices = range(len(data))
    kf = KFold(n_splits=folds)

    for train, test in kf.split(indices):
        trainData = data[train]
        testData = data[test]
        yield (meta, trainData, testData)


def KFoldSplit_df(df, folds=3):
    kf = KFold(n_splits=folds)

    df = shuffle(df)
    for train, test in kf.split(df.index):
        trainData = df.iloc[train]
        testData = df.iloc[test]
        yield trainData, testData
