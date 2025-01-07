import sys


def avg(l):
    return (sum(l)/len(l))


def get_min(l):
    _min = l[0]
    for e in l:
        if e < _min:
            _min = e
    return _min


def get_max(l):
    _max = l[0]
    for e in l:
        if e > _max:
            _max = e
    return _max


l = []
for line in sys.stdin:
    l.append(float(line))



print("Durchschnitt:", avg(l))
print("Minimum:", get_min(l))
print("Maximum:", get_max(l))
