print('* Lojas Quase Dois - Tabela de preços\n')
print(' Nº de Produtos | Valor da Conta ')
contador = 1
valordaconta = 1.99
while contador <= 50:
    print(f'{f"Produto nº {contador}":^16}{"|":^2}{f"R$ {valordaconta:.2f}":^15}')
    contador += 1
    valordaconta += 1.99