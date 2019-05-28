n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 and n1 > n3:
    print(n1)
    if n2 > n3:
        print(n2)
        print(n3)
    else:
        print(n3)
        print(n2)
if n2 > n1 and n2 > n3:
    print(n2)
    if n1 > n3:
        print(n1)
        print(n3)
    else:
        print(n3)
        print(n1)
if n3 > n1 and n3 > n2:
    print(n3)
    if n1 > n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)