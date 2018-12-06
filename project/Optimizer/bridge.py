
from __future__ import division

import logging
import sys

import pandas as pd

from ABEN.main import gen_setting_obj, abe_execute
from FeatureModel.Feature_tree import FeatureTree
from utils.kfold import KFoldSplit

"""
Connecting packages "ABE" and "FeatureModel"
"""

fm2S = {
    "Outlier"                            : 'outlier',
    "Prototype"                          : 'prototype',
    "Remove_Nothing"                     : 'rm_noting',
    "Information_Gain"                   : 'gain_rank',
    "Relief"                             : 'relief',
    "Principal_Components"               : 'principal_component',
    "Correlation-based_Feature_Selection": 'cfs',
    "Consistency-Based_Subset_Evaluation": 'consistency_subset',
    "Wrapper_Subset_Evaluation"          : 'wrapper_subset',
    "Feature_Weighted_ABE"               : 'genetic_weighting',
    # "Analogy-X": '',
    "Equal_Frequency"                    : 'equal_frequency',
    "Equal_Width"                        : 'equal_width',
    "Entropy"                            : 'entropy',
    # "PKID": '',
    "Remain_Same"                        : 'remain_same',
    "Weighted_Euclidean"                 : 'weighted_euclidean',
    "Unweighted_Euclidean"               : 'euclidean',
    "Max_Distance"                       : 'maximum_measure',
    "Triangular_Distribution"            : 'local_likelihood',
    "Minkowski"                          : 'minkowski',
    "Mean_of_Ranking"                    : 'feature_mean_dist',
    "Median"                             : 'median_adaptation',
    "Weighted_Mean"                      : 'weighted_mean',
    "Unweighted_Mean"                    : 'mean_adaptation',
    "Second_Learner"                     : 'second_learner_adaption',
    "Dynamic"                            : 'analogy_dynamic',
    "Set_K_as_1"                         : 'analogy_fix1',
    "Set_K_as_2"                         : 'analogy_fix2',
    "Set_K_as_3"                         : 'analogy_fix3',
    "Set_K_as_4"                         : 'analogy_fix4',
    "Set_K_as_5"                         : 'analogy_fix5'
}


def ft_dict_to_ABE_setting(d):
    S_str = list()
    for item in d.keys():
        if not d[item]: continue
        if item.name in fm2S:
            S_str.append(fm2S[item.name])
    # print(S_str)
    return gen_setting_obj(S_str)
