numero = int(input('Digite um número: '))
eprimo = True
for i in range(numero - 1, 1, -1):
        if numero % i == 0:
            eprimo = False
            break
if eprimo:
    print('O digitado é primo.')
else:
    print('O número digitado não é primo, pois o número digitado também é divisível por: ', end='')
    for i in range(numero - 1, 1, -1):
        if numero % i == 0:
            print(i, end=' | ')