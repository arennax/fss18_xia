from testEngine import O
from num import Num

@O.k
def test_num():
    n = Num([4,10,15,38,54,57,62,83,100,100,174,190,215,225,
       233,250,260,270,299,300,306,333,350,375,443,475,
       525,583,780,1000])

    print(n.mu, n.sd)
    assert round(n.mu, 1) == 270.3
    assert round(n.sd, 3) == 231.946
