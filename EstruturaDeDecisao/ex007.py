n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)
if not n1 > n2 and not n1 > n3:
    print(n1)
elif not n2 > n1 and not n2 > n3:
    print(n2)
else:
    print(n3)
