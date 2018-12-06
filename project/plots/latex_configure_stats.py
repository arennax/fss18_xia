
import ast

import numpy as np
import pandas as pd


def most_comm(lst):
    return max(((item, lst.count(item)) for item in set(lst)), key=lambda a: a[1])[0]


def most_common(lst):
    return max(lst, key=lst.count)


def counting(data_id):
    data = pd.read_csv('Outputs/final_list.txt', sep=";", header=None)
    data.columns = ["Data_ID", "Method_ID", "MRE", "SA", "CONFIG", "NGEN"]
    new_data = data.query('Data_ID == ["' + str(data_id) +
                          '"] and Method_ID == ["' + str(4) +
                          '"]')
    new_data = new_data.loc[:, "CONFIG"]
    alist = []
    for i in new_data:
        i = ast.literal_eval(i)
        alist.append(i)

    alist = np.array(alist).T

    density = list()

    # handing subsets
    d = alist[0].tolist()
    n = len(d)
    density.append([(d.count(0) + d.count(2)) / n, d.count(1) / n])

    # handing weighing
    d = alist[1].tolist()
    n = len(d)
    density.append([d.count(i) / n for i in range(8)])

    # handing disct
    d = alist[2].tolist()
    n = len(d)
    density.append([d.count(0) / n,
                    d.count(1) / n,
                    (d.count(2) + d.count(3) + d.count(4)) / n,
                    ])

    # handing similarity
    d = alist[3].tolist()
    n = len(d)
    density.append([d.count(i) / n for i in range(6)])

    # handing adaption
    d = alist[4].tolist()
    n = len(d)
    density.append([d.count(i) / n for i in range(4)])

    # handing analogies
    d = alist[5].tolist()
    n = len(d)
    density.append([d.count(i) / n for i in range(6)])

    return density


def latex_plot(model_name, data_id):
    def print_one_box(den):
        den *= 100
        if den == 100:
            den = 99
        if den >= 50:
            return "\wbox{" + str(int(den)) + "}"
        elif den < 10:
            return "\dbox{0" + str(int(den)) + "}"
        else:
            return "\dbox{" + str(int(den)) + "}"

    density = counting(data_id)
    str1 = model_name + '&'
    for i, v in enumerate(density):
        # handing v here
        v = [float(i) / sum(v) for i in v]
        for j, vv in enumerate(v):
            str1 += print_one_box(vv)
        str1 += '&'
    str1 = str1[:-1]
    str1 += "\\\\"
    print(str1)


def latex_plot_all_density():
    model_names = ['albrecht', 'desharnais', 'finnish', 'kemerer', 'maxwell', 'miyazaki', 'china', 'isbsg10',
                   'kitchenham']
    for i, n in enumerate(model_names):
        latex_plot(n, i)


if __name__ == '__main__':
    latex_plot_all_density()
