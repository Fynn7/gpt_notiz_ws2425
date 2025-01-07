import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == b and b == c:
    print("Gleich")
elif a <= b and b <= c:
    print("Aufsteigend sortiert")
elif a >= b and b >= c:
    print("Absteigend sortiert")
else:
    print("Unsortiert")