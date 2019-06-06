print('* Panificadora Pão de Ontem - Tabela de preços\n')
print(' Nº de Pães | Valor da Conta ')
contador = 1
valordopao = 0.18
while contador <= 50:
    print(f'{f"Pão nº {contador}":^12}{"|":^2}{f"R$ {valordopao:.2f}":^14}')
    contador += 1
    valordopao += 0.18