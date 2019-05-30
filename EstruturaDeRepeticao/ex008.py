soma = 0
for i in range (0, 5):
    numero = ''
    while not str(numero).isdigit():
        numero = str(input('Digite um número: '))
        if numero.isdigit():
            numero = int(numero)
            soma += numero
        else:
            print('Valor inválido. Tente novamente.')
media = soma / 5
print(f'A soma dos números digitados é {soma}. E a média é igual {media}.')