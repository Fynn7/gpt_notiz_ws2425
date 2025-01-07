x = int(input("Bitte geben Sie eine Ganzzahl ein: "))

for e in range(1,x): # x=8, [1,2,3,4,5,6,7]
    if x % e == 0:
        print(e)