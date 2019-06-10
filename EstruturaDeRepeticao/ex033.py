opcao = ' '
maior = 0
menor = 0
soma = 0
contaloop = 0
while opcao != 'N':
    temperatura = float(input('Digite a temperatura registrada: '))
    if contaloop == 0:
        menor = temperatura
    if temperatura > maior:
        maior = temperatura
    if temperatura < menor:
        menor = temperatura
    soma += temperatura
    contaloop += 1
    opcao = ' '
    while opcao not in 'SN' or not opcao:
        opcao = str(input('Quer continuar? [S/N]')).upper()
        if opcao not in 'SN' or not opcao:
            print('Opção inválida! Tente novamente.')
media = soma / contaloop
print(f'A maior temperatura registrada foi {maior}º.')
print(f'A menor temperatura registrada foi {menor}º.')
print(f'A media das temperaturas registrada é {media:.2f}º.')
