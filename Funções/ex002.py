def imprimir(numero):
    for i in range(1, numero + 1):
        for ii in range(1, i + 1):
            print(ii, end=' ')
        if i != 0:
            print()
numero = int(input('Digite um número:'))
imprimir(numero)