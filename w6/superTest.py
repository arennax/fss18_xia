from testEngine import O
from super import mainSuper


@O.k
def testSuper1():
    mainSuper("./weatherLong.csv")


@O.k
def testSuper2():
    mainSuper("./auto.csv")



