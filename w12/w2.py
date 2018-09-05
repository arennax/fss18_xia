DATA1 = """
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 = """
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""

import re, traceback


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


def lines(s):
    "Return contents, one line at a time."
    src_1 = s.splitlines()
    src_2 = []
    for i, lin in enumerate(src_1):
        for j, ch in enumerate(lin):
            if ch == '#':
                lin = lin[:j]
        src_2.append(lin)
    return src_2


def rows(src):
    """Kill bad characters. If line ends in ','
   then join to next. Skip blank lines."""
    row_1 = []
    skip_blank = ""
    for row in src:
        row = row.replace(' ', '')
        skip_blank += row
        if row[-1:] == ',' or row == "":
            continue
        row_1.append(skip_blank)
        skip_blank = ""
    return row_1


def cols(src):
    """ If a column name on row1 contains '?',
    then skip over that column."""
    col_del = []
    col_1 = [i.split(",") for i in src]
    for j, ch in enumerate(col_1[0]):
        if ch.startswith('?'):
            col_del.append(j)
    for row in col_1:
        for k in col_del:
            row.pop(k)
    return col_1


def prep(src):
    """ If a column name on row1 contains '$',
    coerce strings in that column to a float."""
    prep_flo = []
    for j, ch in enumerate(src[0]):
        if str(ch).startswith('$'):
            prep_flo.append(j)
    for row in src[1:]:
        for k in prep_flo:
            row[k] = float(row[k])
    return src


# ----- Test Case ----------------------------

def ok0(s):
    for row in prep(cols(rows(lines(s)))):
        print(row)

@O.k
def ok1(): ok0(DATA1)


@O.k
def ok2(): ok0(DATA2)
