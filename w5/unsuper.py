from rows import rows
from num import Num
from betterDisplay import display, printdata


def unsuper(data):
    rows = data.rows
    enough = len(rows) ** 0.5  # super.enough = 0.5

    def band(c, lo, hi):
        if lo == 0:
            return ".." + str(rows[hi][c])
        elif hi == most:
            return str(rows[lo][c]) + ".."
        else:
            return str(rows[lo][c]) + ".." + str(rows[hi][c])

    def argmin(c, lo, hi):
        cut = None
        if (hi - lo > 2 * enough):
            l, r = Num(), Num()
            for i in range(lo, hi + 1): r.numInc(rows[i][c])
            best = r.sd
            for i in range(lo, hi + 1):
                x = rows[i][c]
                l.numInc(x)
                r.numDec(x)
                if l.n >= enough and r.n >= enough:
                    tmp = Num.numXpect(l, r) * 1.05  # super.margin = 1.05
                    if tmp < best:
                        cut, best = i, tmp
        return cut


    def cuts(c, lo, hi, pre):
        txt = pre + str(rows[lo][c]) + ".. " + str(rows[hi][c])
        cut = argmin(c, lo, hi)
        if cut:
            print(txt)
            cuts(c, lo, cut, pre + "|.. ")
            cuts(c, cut + 1, hi, pre + "|.. ")
        else:
            b = band(c, lo, hi)
            print(txt + " (" + b + ")")
            for r in range(lo, hi + 1):
                rows[r][c] = b


    def stop(c, t):
        for i in range(len(t) - 1, -1, -1):
            if t[i][c] != "?": return i
        return 0

    for c in data.indeps:
        if c in data.nums:
            rows = sorted(rows, key=lambda x: str(x[c]))
            most = stop(c, rows)
            # fyi("\n-- "..data.name[c]..most.."----------")
            print("\n---------- ", data.name[c], most, "----------")
            cuts(c, 0, most, "|.. ")
    output = display(rows)
    new_header = [i.replace('$', '') for i in data.name]
    output.columns = new_header
    printdata(output)


def mainUnsuper(s):
    print(s)
    unsuper(rows(s))
