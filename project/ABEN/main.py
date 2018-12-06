
from __future__ import division

import logging
import pdb
import pandas as pd
import sys
import ABEN.adaptation
import ABEN.analogies
import ABEN.discretization
import ABEN.measures
import ABEN.normalize
import ABEN.subSelector
import ABEN.weighting
# from Optimizer.feature_link import sa_calc
from utils.bunch import ABE_configures
from utils.kfold import KFoldSplit_df
from data.new_data import data_albrecht, data_desharnais, data_finnish, data_kemerer, data_maxwell, data_miyazaki, \
    data_china, data_isbsg10, data_kitchenham

def abe_execute(S, data):
    """
    executing the ABE method
    :param S:
    :param data:
    :param test:
    :return:
    """
    # for convenience, use negative index for test
    logging.debug("Sub selection -- " + S.subSelector.__name__)
    data = S.subSelector(data)
    logging.debug("Normalization")
    data = ABEN.normalize.normalize(data)
    logging.debug("Discretization -- " + S.discretization.__name__)
    if S.weighting in [ABEN.weighting.gain_rank, ABEN.weighting.relief]:
        data = S.discretization(data)

    logging.debug("Feature weighting -- " + S.weighting.__name__)
    data = S.weighting(data)

    logging.debug("Predicting " + S.analogies.__name__ + " " + S.adaptation.__name__)
    Y_predict, Y_actual = list(), list()
    for index, test in data.iterrows():
        train = data.drop(index)
        dists = S.measures(test, train)
        closest, c_dists = S.analogies(dists, train, measures=S.measures)
        Y_predict.append(S.adaptation(closest, test, c_dists))
        Y_actual.append(test[-1])

    return Y_predict, Y_actual


def gen_setting_obj(S_str):
    S = ABE_configures()

    # three case subset selectors
    S.subSelector = ABEN.subSelector.default
    for subSelector in dir(ABEN.subSelector):
        if subSelector in S_str:
            S.subSelector = getattr(ABEN.subSelector, subSelector)

    # six similarity measures
    S.measures = ABEN.measures.weighted_euclidean
    for measures in dir(ABEN.measures):
        if measures in S_str:
            S.measures = getattr(ABEN.measures, measures)

    # six ways to select analogies
    S.analogies = ABEN.analogies.default
    for analogies in dir(ABEN.analogies):
        if analogies in S_str:
            S.analogies = getattr(ABEN.analogies, analogies)

    # eight feature weighting methods
    S.weighting = ABEN.weighting.default
    for weighting in dir(ABEN.weighting):
        if weighting in S_str:
            S.weighting = getattr(ABEN.weighting, weighting)

    # five discretization methods
    S.discretization = ABEN.discretization.default
    for discretization in dir(ABEN.discretization):
        if discretization in S_str:
            S.discretization = getattr(ABEN.discretization, discretization)

    # four adaptation methods
    S.adaptation = ABEN.adaptation.mean_adaptation
    for adaptation in dir(ABEN.adaptation):
        if adaptation in S_str:
            S.adaptation = getattr(ABEN.adaptation, adaptation)

    return S

if __name__ == '__main__':
    """
    ABE algorithm Demonstration
    """
    logging.basicConfig(stream=sys.stdout,
                        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
                        level=logging.DEBUG)

    settings = gen_setting_obj(
        ['outlier', 'maximum_measure', 'analogy_dynamic', 'relief'])

    for  train, test in KFoldSplit_df(data_isbsg10(), folds=3):
        trainData = pd.DataFrame(data=train)
        Y_predict, Y_actual = abe_execute(S=settings, data=trainData)
        import pdb
        pdb.set_trace()
        # print(sa_calc(Y_predict, Y_actual))
