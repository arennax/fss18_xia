from sample import Sample


class Num:
    def __init__(self, Lists=[]):
        self.max = len(Lists)
        self.n = 0
        self.mu = 0
        self.m2 = 0
        self.sd = 0
        self.lo = 10 ** 32
        self.hi = -10 ** 32
        self.some = Sample(self.max)
        self.w = 1
        for i in Lists:
            self.numInc(i)

    def numInc(self, x):
        if x == "?":
            return x
        self.n += 1
        self.some.sampleInc(x)
        d = x - self.mu
        self.mu += d / self.n
        self.m2 += d * (x - self.mu)
        if x > self.hi:
            self.hi = x
        if x < self.lo:
            self.lo = x
        if self.n >= 2:
            self.sd = (self.m2 / (self.n - 1 + 10 ** -32)) ** 0.5
        return x

    def numDec(self, x):
        if x == "?":
            return x
        if self.n == 1:
            return x
        self.n -= 1
        d = x - self.mu
        self.mu = abs(self.mu - d / self.n)
        self.m2 = abs(self.m2 - d * (x - self.mu))
        if self.n >= 2:
            self.sd = (self.m2 / (self.n - 1 + 10 ** -32)) ** 0.5
        return x

    def numNorm(self, x):
        return (x - self.lo) / (self.hi - self.lo + (10 ** -32))

    def numXpect(i, j):
        n = i.n + j.n + 0.0001
        return i.n / n * i.sd + j.n / n * j.sd
