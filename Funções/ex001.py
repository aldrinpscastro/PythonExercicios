def imprimir(numero):
    for i in range(1, numero + 1):
        print(f'{str(i)} ' * i)
numero = int(input('Digite um número: '))
imprimir(numero)