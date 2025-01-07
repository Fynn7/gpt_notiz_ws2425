from itertools import product

p = product([False, True], repeat=3)


for i in p:  # gebe alle möglichen Kombinationen/Kreuzprodukte aus
    print(i)

for a, b, c in p: # teste alle möglichen Kombinationen
    try:
        assert ((a and a) or (b and b)) == (a or b)
    except AssertionError:
        print("Ausdruck 1 falsch für a={}, b={}".format(a, b))
    try:
        assert ((a and b) or (a and c)) == (a and (b or c))
    except AssertionError:
        print("Ausdruck 2 falsch für a={}, b={}, c={}".format(a, b, c))
    try:
        assert (not (a < b) or (a == b)) == (a >= b)
    except AssertionError:
        print("Ausdruck 3 falsch für a={}, b={}".format(a, b))
    try:
        assert ((not (a < b) and not (a > b))) == (a == b)
    except AssertionError:
        print("Ausdruck 4 falsch für a={}, b={}".format(a, b))
    try:
        assert ((not (a and b) and (a or b)) or (
            (a and b) or not (a or b))) == True
    except AssertionError:
        print("Ausdruck 5 falsch für a={}, b={}".format(a, b))
