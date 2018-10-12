from num import Num
from sym import Sym
import re


class Data:

    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.Class = None
        self.rows = []
        self.name = []
        self._use = []

        self.indeps = []

    def indep(self, c):
        return c not in self.w and self.Class != c

    def dep(self, c):
        return not self.indep(c)

    def header(self, cells):
        for c0, x in enumerate(cells):
            if '?' not in x:
                c = len(self._use)
                self._use.append(c0)
                self.name.append(x)
                if re.search('[<>$]', x):
                    self.nums[c] = Num([])
                else:
                    self.syms[c] = Sym([])
            if re.match('<', x):
                self.w[c] = -1
            elif re.match(">", x):
                self.w[c] = 1
            elif re.match('!', x):
                self.Class = c
            else:
                self.indeps.append(c)
        return self

    def row(self, cells):
        r = len(self.rows)
        self.rows.append([])
        for c, c0 in enumerate(self._use):
            x = cells[c0]
            if x != '?':
                if c in self.nums:
                    try:
                        x = int(x)
                    except ValueError:
                        x = float(x)
                    self.nums[c].numInc(x)
                else:
                    self.syms[c].symInc(x)
            self.rows[r].append(x)
        return self


def rows1(file):
    data = Data()
    first = True
    for line in file:
        line = re.sub(r'[\t\r\n ]', '', line)
        line = re.sub(r'#.*', '', line)
        cells = line.split(',')
        if len(cells) > 0:
            if first:
                data.header(cells)
            else:
                data.row(cells)
        first = False
    return data


def reader(file):
    with open(file) as temp:
        for line in temp:
            yield line


def rows(file):
    return rows1(reader(file))
