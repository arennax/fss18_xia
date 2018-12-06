
from __future__ import division
import numpy as np
import pandas as pd
import hashlib
import ABEN.measures
import logging
import pdb

"""
input:
  dists - one pandas.core.series.Series. distances from test row to each train
  train - pandas.dataframe. INCLUDING Y value
  measures - one of function in ABE.measures
  
output:
- pandas.dataFrame. closest targets inside the train
- distances: a list

"""


def default(dists, train, measures=None):
    return analogy_fix1(dists, train)


def analogy_fix1(dists, train, measures=None):
    return _fixed(dists, train, 1)


def analogy_fix2(dists, train, measures=None):
    return _fixed(dists, train, 2)


def analogy_fix3(dists, train, measures=None):
    return _fixed(dists, train, 3)


def analogy_fix4(dists, train, measures=None):
    return _fixed(dists, train, 4)


def analogy_fix5(dists, train, measures=None):
    return _fixed(dists, train, 5)


cache = dict()


def analogy_dynamic(dists, train, measures=ABE.measures.default):
    # to avoid repeat computation, check for cache first
    tid = hashlib.sha256(train.values.tobytes()).hexdigest()
    if tid in cache:
        bestK = cache[tid]
    else:
        # tune the k
        # bestK = _tuneK(train, measures)
        # cache[tid] = bestK
        bestK = 6
    return _fixed(dists, train, bestK)


def _fixed(dists, train, k):
    info = [(d, r) for d, (i, r) in zip(dists.tolist(), train.iterrows())]
    info.sort(key=lambda i: i[0])
    cares = [i[1] for i in info[:k]]
    res = pd.DataFrame(cares)
    c_dists = [i[0] for i in info[:k]]

    return res, c_dists


def _tuneK(train, measures):

    logging.debug("Tuning K")
    # limit the data size of train as 50. otherwise randomly prune some
    if train.shape[0] > 50:
        train = train.sample(n=50)

    # measure the distance between them
    table = pd.DataFrame(data=np.full([train.shape[0], train.shape[0]], np.inf),
                         index=train.index, columns=train.index)

    for i in train.index:

        ds = measures(train.loc[i], train)
        for j in train.index:
            if i == j:
                continue
            table[i][j] = ds[j]
            table[j][i] = ds[j]

    def errork(k):
        errors = 0
        for r_index in train.index:
            predict = sum(sorted(table[r_index])[:k]) / k
            errors += abs(predict - train.loc[r_index].iloc[-1])
        return errors

    _current_min = float('inf')
    res = 1
    for k in range(1, train.shape[0]):
        e = errork(k)
        if e < _current_min:
            res = k
            _current_min = e
    return res
