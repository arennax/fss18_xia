
from __future__ import division

import logging
import sys
import pdb

import pandas as pd
import numpy as np
from scipy.io import arff

from Optimizer.bridge import ft_dict_to_ABE_setting
from ABEN.main import abe_execute
from FeatureModel.Feature_tree import FeatureTree
from data.new_data import data_albrecht, data_china, data_desharnais, data_kemerer, data_maxwell, data_miyazaki
from utils.kfold import KFoldSplit, KFoldSplit_df


def random_config(ft, dataset):
    """
    Randomly generate an ABE hyperparameter.
    To reduce the error, use cross-validation (10 fold).

    :param ft:
    :param dataset:
    :return: average relative error [0,1]
    """

    while True:
        X = ft.top_down_random(None)

        if ft.check_fulfill_valid(X):
            break
        logging.debug('=== Invalid configuration. Regenerating...')
    settings = ft_dict_to_ABE_setting(X)
    # print(settings)

    # data0, meta0 = arff.loadarff(dataset)
    all_error = list()
    for train, test in KFoldSplit_df(dataset, folds=len(dataset)):
        trainData = pd.DataFrame(data=train)
        testData = pd.DataFrame(data=test)
        error = abe_execute(S=settings, train=trainData, test=testData)
        all_error.append(error)
    return np.mean(all_error)


if __name__ == '__main__':
    # logging.basicConfig(stream=sys.stdout,
    #                     format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    #                     level=logging.DEBUG)

    url = "./FeatureModel/tree_model.xml"
    ft = FeatureTree()
    ft.load_ft_from_url(url)

    pop = 10
    gen_list = list()

    # for _ in range(10):
    #     print(random_config(ft, "data/albrecht.arff"))

    for _ in range(pop):
        gen_list.append(random_config(ft, data_albrecht))

    # rd_mean = np.mean(gen_list)
    # rd_std = np.std(gen_list)
    # rd_min = np.min(gen_list)
    # rd_max = np.max(gen_list)
    # rd_median = np.median(gen_list)

    print(gen_list)
    # print("evals:", pop, "mean:", rd_mean, "std:", rd_std, "min:", rd_min, "max:", rd_max, "median:", rd_median)
