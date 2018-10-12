import math
from rows import rows
from num import Num
from dom import doms
from betterDisplay import display, printdata


def super(data, goal=None, enough=None):
    sd_temp = {}
    splitter = None
    sd_min = None
    rows = data.rows
    if goal is None:
        goal = len(rows[0]) - 1
    if enough is None:
        enough = len(rows) ** 0.5

    def band(c, lo, hi):
        if lo == 0:
            return ".." + str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c]) + ".."
        else:
            return str(rows[lo][c]) + ".." + str(rows[hi][c])

    def argmin(c, lo, hi):
        cut = None
        xl = Num()
        xr = Num()
        yl = Num()
        yr = Num()
        for i in range(lo, hi + 1):
            xr.numInc(rows[i][c])
            yr.numInc(rows[i][goal])
        bestx = xr.sd
        besty = yr.sd
        mu = yr.mu
        n = yr.n
        if (hi - lo > 2 * enough):
            for i in range(lo, hi + 1):
                x = rows[i][c]
                y = rows[i][goal]
                xl.numInc(x)
                xr.numDec(x)
                yl.numInc(y)
                yr.numDec(y)
                if xl.n >= enough and xr.n >= enough:
                    tmpx = Num.numXpect(xl, xr) * 1.05
                    tmpy = Num.numXpect(yl, yr) * 1.05
                    if tmpx < bestx and tmpy < besty:
                        cut, bestx, besty = i, tmpx, tmpy
        return cut, mu, n, besty

    def cuts(c, lo, hi, pre):
        txt = pre + str(rows[lo][c]) + ".." + str(rows[hi][c])
        cut, mu, n, sd = argmin(c, lo, hi)
        if cut:
            print(txt)
            cuts(c, lo, cut, pre + "|.. ")
            cuts(c, cut + 1, hi, pre + "|.. ")
        else:
            s = band(c, lo, hi)
            sd_temp[c] = {}
            sd_temp[c][s] = (n, sd)
            print(txt + " ==> " + str(math.floor(100 * mu)))
            for r in range(lo, hi + 1):
                rows[r][c] = s

    def stop(c, t):
        for i in range(len(t) - 1, -1, -1):
            if t[i][c] != "?": return i
        return 0

    def split_value(src):
        total = 0
        result = 0
        for _, (n, sd) in src.items():
            total += n
        for _, (n, sd) in src.items():
            result += n / (total + 10 ** -32) * sd
        return result


    for c in data.indeps:
        if c in data.nums:
            rows = sorted(rows, key=lambda x: str(x[c]))
            most = stop(c, rows)
            print("\n-- " + data.name[c] + ": " + str(most) + "----------\n")
            cuts(c, 0, most, "|.. ")

    output = display(rows)
    new_header = [data.name]
    output.columns = new_header
    printdata(output)

    for c in data.indeps:
        if c in data.nums:
            sd_true = split_value(sd_temp[c])
            if sd_min is None or sd_true < sd_min:
                sd_min = sd_true
                splitter = data.name[c]
    print("Split Point: " + splitter + "\n")


def mainSuper(s):
    print(s)
    super(doms(rows(s)))



