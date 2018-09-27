from testEngine import O
from dom import mainDom

@O.k
def test_1():
    mainDom("./weatherLong.csv", 'all')

@O.k
def test_2():
    mainDom("./auto.csv", 'short')