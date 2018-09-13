import math


class Sym:

    def __init__(self, Lists):
        self.counts = dict()
        self.mode = None
        self.most = 0
        self.n = 0
        self._ent = None
        for i in Lists:
            self.symInc(i)

    def symInc(self, x):
        if x == "?":
            return x
        self._ent = None
        self.n += 1
        old = self.counts.get(x)
        if old:
            new = old + 1
        else:
            new = 1
        self.counts[x] = new
        if new > self.most:
            self.most = new
            self.mode = x
        return x

    def symDec(self, x):
        self._ent = None
        if self.n > 0:
            self.n -= 1
            self.counts[x] -= 1
        return x

    def symEnt(self):
        if not self._ent:
            self._ent = 0
            for i, n in self.counts.items():
                p = n / self.n
                self._ent -= p * math.log(p, 2)
        return self._ent
