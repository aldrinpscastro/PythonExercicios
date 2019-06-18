print('Especificação  Código  Preço')
print(f'{"Cachoro Quente":<14}', f'{"100":<7}', f'{"R$ 1.20":<5}')
print(f'{"Bauru Simples":<14}', f'{"101":<7}', f'{"R$ 1.30":<5}')
print(f'{"Bauru Com Ovo":<14}', f'{"102":<7}', f'{"R$ 1.50":<5}')
print(f'{"Hambúrguer":<14}', f'{"103":<7}', f'{"R$ 1.20":<5}')
print(f'{"Cheeseburguer":<14}', f'{"104":<7}', f'{"R$ 1.30":<5}')
print(f'{"Refrigerante":<14}', f'{"105":<7}', f'{"R$ 1.00":<5}')
tabela = f'\n{"ITEM":^18}' + f'{" | ":^3}' + f'{"PREÇO X QUANTIDADE":^20}' + f'{" | ":^3}' + f'{"VALOR":^8}\n'
opcao = ''
total = 0
while opcao != 'S':
    opcao = ''
    coditem = input('\nDigite o código do item:')
    quantidade = int(input('Digite a quantidade: '))
    while opcao not in 'SN' or not opcao:
        opcao = input('O pedido deve ser encerrado? [S/N]').upper()
        if opcao not in 'SN' or not opcao:
            print('Opção Inválida! Tente novamente.')
    if coditem == '100':
        preco = 1.2
        item = 'Cachorro Quente'
    if coditem == '101':
        preco = 1.3
        item = 'Bauro Simples'
    if coditem == '102':
        preco = 1.5
        item = 'Bauru Com Ovo'
    if coditem == '103':
        preco = 1.2
        item = 'Hambúrguer'
    if coditem == '104':
        preco = 1.3
        item = 'Cheeseburguer'
    if coditem == '105':
        preco = 1.0
        item = 'Refrigerante'
    valor = preco * quantidade
    total += valor
    tabela += f'{item:^18}' + f'{" | ":^3}' + f'{f"R$ {preco:.2f} X {quantidade}":^20}' + f'{" | ":^3}' + f'{f"R$ {valor:.2f}":^8}\n'
tabela += '-' * 52 + '\n'
tabela += f'{"TOTAL":^18}' + f'{"":^3}' + f'{"":^20}' + f'{"":^3}' + f'{f"R$ {total:.2f}":^8}'
print(tabela)
