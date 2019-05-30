maior = 0
for i in range (0, 5):
    numero = ''
    while not str(numero).isdigit():
        numero = str(input('Digite um número: '))
        if numero.isdigit():
            numero = int(numero)
            if numero > maior:
                maior = numero

        else:
            print('Valor inválido. Tente novamente.')
print(maior)