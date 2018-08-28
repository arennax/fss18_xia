import re, traceback
import math, random
from collections import defaultdict, Counter
from functools import partial, reduce



class O:
    y = n = 0

    @staticmethod
    def report():
        print("\n# pass= %s fail= %s %%pass = %s%%" % (
            O.y, O.n, int(round(O.y * 100 / (O.y + O.n + 0.001)))))

    @staticmethod
    def k(f):
        try:
            print("\n-----| %s |-----------------------" % f.__name__)
            if f.__doc__:
                print("# " + re.sub(r'\n[ \t]*', "\n# ", f.__doc__))
            f()
            print("# pass")
            O.y += 1
        except:
            O.n += 1
            print(traceback.format_exc())
        return f


# Page 5
@O.k
def test_whitespace():
    two_plus_three = 2 + \
                     3
    assert two_plus_three == 5


# Page 6
@O.k
def test_modules():
    m = math.sqrt(4)
    assert m == 2


# Page 7
@O.k
def test_arithmetic():
    n = 5//2
    assert n == 2


# Page 8
def double(x):
    return x * 2

@O.k
def test_functions():
    p = double(10)
    assert p == 20


# Page 9
@O.k
def test_strings():
    tab_string = '\t'
    assert len(tab_string) == 1


# Page 10
@O.k
def test_exceptions():
    alpha = 1
    try:
        a = 0/0
    except ZeroDivisionError:
        alpha = 0
    assert alpha == 0


# Page 11
@O.k
def test_lists_1():
    x = [1, 2, 3]
    x.append(0)
    y = x[-1]
    assert y == 0


# Page 12
@O.k
def test_lists_2():
    x, y = [1, 2]
    assert x == 1 and y == 2


# Page 13
@O.k
def test_tuples():
    x, y = 1, 2
    x, y = y, x
    assert x == 2 and y == 1


# Page 14
@O.k
def test_dictionaries():
    grades = {"Joel": 80, "Tim": 95}
    tims_grade = grades["Tim"]
    assert tims_grade == 95


# Page 15
@O.k
def test_defaultdict():
    document = ["i", "have", "a", "dream"]
    word_counts = defaultdict(int)
    for word in document:
        word_counts[word] += 1
    assert word_counts["dream"] == 1


# Page 16
@O.k
def test_counter():
    document = ["apple", "banana", "lemmon", "apple"]
    m = Counter(document)
    assert m["apple"] == 2


# Page 17
@O.k
def test_sets():
    s = set()
    s.add(1)
    s.add(2)
    s.add(2)
    assert len(s) == 2


# Page 18
@O.k
def test_controlflow():
    a = 0
    for x in range(10):
        if x == 3:
            continue
        if x == 5:
            break
        a += x
    assert a == 7


# Page 19
@O.k
def test_truthiness_1():
    true_equals_false = True == False
    assert true_equals_false is False


# Page 20
@O.k
def test_truthiness_2():
    x = all([True, 1, {}])
    assert x is False


# Page 22
@O.k
def test_sorting():
    x = [4, 1, 2, 3]
    y = sorted(x)
    assert y[0] == 1


# Page 23
@O.k
def test_listcomprehensions():
    squares = [x * x for x in range(5)]
    sample = [0, 1, 4, 9, 16]
    assert squares == sample


# Page 24
@O.k
def test_generator():
    n, m = 1, 0
    while True:
        yield n
        m += n
        n += 1
        if n == 100:
            break
    assert m == 4950


# Page 25
@O.k
def test_randomness():
    random.seed(1)
    a = random.random()
    random.seed(1)
    b = random.random()
    assert a == b


# Page 26
@O.k
def test_regex():
    a = "patricia"
    b = re.sub("[0-9]", "a", "p3trici7")
    assert a == b


# Page 27

class Set:
    def __init__(self, values=None):
        self.dict = {}
        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        return "Set: " + str(self.dict.keys())

    def add(self, value):
        self.dict[value] = True

    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

@O.k
def test_oop():
    s = Set([1, 3, 5, 7, 9])
    s.remove(5)
    assert s.contains(5) is False


# Page 28
def exp(base, power):
    return base ** power

@O.k
def test_functionaltools_1():
    three_to_the = partial(exp, power=3)
    assert three_to_the(3) == 27


# Page 29
def multiply(x, y):
    return x * y

@O.k
def test_functionaltools_2():
    xs = [1, 2, 3, 4]
    x_product = reduce(multiply, xs)
    assert x_product == 24


# Page 30
@O.k
def test_enumerate():
    my_list = ['sun', 'moon', 'earth', 'mars']
    for c, value in enumerate(my_list, 1):
        print(c, value)
    assert c == 4 and value == 'mars'


# Page 31
def add(a, b):
    return a + b

@O.k
def test_zip():
    a = add(*[5, 10])
    assert a == 15


# Page 32
def add(a, b):
    return a + b

@O.k
def test_args_1():
    x = [1]
    y = [2]
    z = add(*x, *y)
    assert z == 3


# Page 33
def add(a, b):
    return a + b


def doubler_correct(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g


g = doubler_correct(add)

@O.k
def test_args_2():
    x = g(3, 5)
    assert x == 16


if __name__ == "__main__":
    O.report()
