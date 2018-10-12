from rows import rows
from betterDisplay import display, printdata
import random, math


def cap(input, lower, upper):
    if input in range(lower, upper):
        return input
    elif input >= upper:
        return upper
    elif input <= lower:
        return lower


def another(x, t):
    y = cap(math.floor(0.5 + random.random() * len(t)), 0, len(t) - 1)
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


def doms(data):
    n = 100   # samples = 100
    c = len(data.name)
    data.name.append(">dom")
    for r1, row1 in enumerate(data.rows):
        row1.append(0)
        for i in range(n):
            row2 = another(r1, data.rows)
            s = dom(data, row1, row2) and 1 / n or 0
            row1[c] += s

    return data


def mainDom(s):
    print(s)
    doms(rows(s))
