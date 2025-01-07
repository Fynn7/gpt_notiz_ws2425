n1 = input("Geben Sie den ersten Namen ein: ")
n2 = input("Geben Sie den zweiten Namen ein: ")
n3 = input("Geben Sie den dritten Namen ein: ")

if n1 < n2 and n1 < n3:
    print(n1)
    if n2 < n3:
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)
elif n2 < n1 and n2 < n3:
    print(n2)
    if n1 < n3:
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
elif n3 < n1 and n3 < n2:
    print(n3)
    if n2 < n1:
        print(n2)
        print(n1)
    else:
        print(n1)
        print(n2)
