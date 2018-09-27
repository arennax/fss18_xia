from rows import rows
from betterDisplay import display, printdata
import random, math


def cap(x, lo, hi):
    return min(hi, max(lo, x))


def another(x, t):
    y = cap(math.floor(random.random() * len(t)), 0, len(t) - 1)
    if x == y:
        return another(x, t)
    if t[y]:
        return t[y]
    return another(x, t)


def dom(data, row1, row2):
    s1, s2 = 0, 0
    n = len(data.w)
    for c, w in data.w.items():
        a0 = row1[c]
        b0 = row2[c]
        a = data.nums[c].numNorm(a0)
        b = data.nums[c].numNorm(b0)
        s1 -= 10 ** (w * (a - b) / n)
        s2 -= 10 ** (w * (b - a) / n)
    return s1 / n < s2 / n


def doms(data, result_display):
    n = len(data.rows)
    c = len(data.name)
    new_header = data.name + ['>dom']
    for r1, row1 in enumerate(data.rows):
        row1.append(0)
        for i in range(n):
            row2 = another(r1, data.rows)
            s = dom(data, row1, row2) and 1 / n or 0
            row1[c] += s

    if result_display == 'short':
        sorted_data = display(data.rows)
        sorted_data.columns = new_header
        sorted_data = sorted_data.sort_values(by=['>dom'])
        print("First 10 lines:")
        df_first10 = sorted_data.head(10)
        printdata(df_first10)
        print("Last 10 lines:")
        df_last10 = sorted_data.tail(10)
        printdata(df_last10)
    else:
        df_all = display(data.rows)
        df_all.columns = new_header
        printdata(df_all)


def mainDom(s, result_display):
    print(s)
    doms(rows(s), result_display)


