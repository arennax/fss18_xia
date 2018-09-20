from testEngine import O
from rows import rows

@O.k
def test():
    rows("weather.csv")
    rows("weatherLong.csv")
    rows("auto.csv")