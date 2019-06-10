numero = int(input('Digite um número inteiro: '))
eprimo = False
print(f'\nEste são os números primos até {numero}:\n')
for i in range(1, numero + 1, 1):
    for ii in range(i - 1, 1, -1):
        if i % ii == 0:
            eprimo = False
            break
        else:
            eprimo = True
    if eprimo or i == 2:
        print(i, end=' | ')
print()
