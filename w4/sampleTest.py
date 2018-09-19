from testEngine import O
from sample import Sample
import random


@O.k
def test_sample():
    random.seed(1)
    s = []
    for i in range(5, 11):
        s.append(Sample(2**i))
    for i in range(10000):
        y = random.random()
        for t in s:
            t.sampleInc(y)
    for t in s:
        print(t.max, t.nth(0.5))
        assert (0.5 - 0.2) < t.nth(0.5) < (0.5 + 0.2)  # or 0.33?
