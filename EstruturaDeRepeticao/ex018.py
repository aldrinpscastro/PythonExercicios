maior = 0
menor = 0
soma = 0
opcao = ' '
while opcao != 'N':
    opcao = ' '
    numero = int(input('Digite um número: '))
    if menor == 0:
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    soma += numero
    while opcao not in 'SN' or not opcao:
        opcao = str(input('Quer continuar: [S/N] ')).upper()
        if opcao not in 'SN' or not opcao:
            print('Opção inválida. Tente novamente.')
print(f'O maior número digitado foi {maior}. O menor número digitado foi {menor}. E a soma de todos os números é igual a {soma}.')