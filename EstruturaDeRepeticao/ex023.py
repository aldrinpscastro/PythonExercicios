numero = int(input('Digite um número: '))
contador = 2
ndivisoes = 0
print(f'Os números entre 1 e {numero} que são primos:\n')
print('|', end=' ')
while contador <= numero:
    eprimo = True
    for i in range(contador - 1, 1, -1):
        if contador % i == 0:
            eprimo = False
            break
        ndivisoes += 1
    if eprimo:
        print(contador, end=' | ')
    contador += 1
print(f'\n\nNúmeros de divisoes executadas: {ndivisoes}')