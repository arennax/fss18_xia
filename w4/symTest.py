from testEngine import O
from sym import Sym


@O.k
def test_sym():
    s = Sym(['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y',
             'n', 'n', 'n', 'n', 'n'])
    print(s.symEnt())
    assert round(s.symEnt(), 4) == 0.9403
