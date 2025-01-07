import sys

a = sys.stdin.readlines()

for i in range(1, len(a), 2):
	print(a[i], end="")

