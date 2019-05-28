print(f'{" PROMOÇÃO DE CARNES ":=^40}')
quantcarne = float(input('\nQuantos Kg você vai comprar: '))
print('\nDigite "1" para escolher file duplo. ')
print('Digite "2" para escolher alcatra. ')
print('Digite "3" para escolher picanha. \n')
opcao = ' '
while opcao not in '123' or not opcao:
    opcao = str(input('Escolha uma opção: '))
if opcao in '123':
    if opcao == '1':
        tipo = 'File Duplo'
        if quantcarne <= 5:
            precokg = 4.9
        else:
            precokg = 5.8
    if opcao == '2':
        tipo = 'Alcatra'
        if quantcarne <= 5:
            precokg = 5.9
        else:
            precokg = 6.8
    if opcao == '3':
        tipo = 'Picanha'
        if quantcarne <= 5:
            precokg = 6.9
        else:
            precokg = 7.8
precototal = quantcarne * precokg
print(f'\n{" OPÇÃO DE PAGAMENTO ":=^40}\n')
print('Digite "1" para cartão tabajara.')
print('Digite "2" para outros.\n')
opcaopag = ' '
while opcaopag not in '12' or not opcaopag:
    opcaopag = str(input('Digite sua opção: '))
    if opcaopag == '2':
        tipopag = 'Outros'
        desconto = 0
    else:
        tipopag = 'Cartão tabajara'
        desconto = round(precototal * 0.05, 2)
valorapagar = precototal - desconto
print(f'\n{" NOTA FISCAL ":=^40}\n')
print(f'{"Tipo de carne:":<25}{tipo:>15}')
print(f'{"Quantidade:":<25}{f"{quantcarne:.2f} Kg":>15}')
print(f'{"Tipo de pagamento:":<25}{tipopag:>15}')
print(f'{"Total da compra:":<25}{f"R$ {precototal:.2f}":>15}')
print(f'{"Valor do desconto:":<25}{f"R$ {desconto:.2f}":>15}')
print(f'{"Valor à pagar:":<25}{f"R$ {valorapagar:.2f}":>15}')