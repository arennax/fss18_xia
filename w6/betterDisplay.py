import pandas as pd
from pandas import DataFrame

'''I just use this to make results look prettier'''

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def display(data):
    return DataFrame(data)


def printdata(x):
    return print(x.to_string(index=False))