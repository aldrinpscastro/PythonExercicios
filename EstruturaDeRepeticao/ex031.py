from os import system, name
opcao = ' '
while opcao != 'N' or not opcao:
    print(f'{" LOJAS TABAJARA ":=^40}\n')
    totalcompra = 0
    contador = 1
    precoproduto = - 1
    while precoproduto != 0:
        precoproduto = float(input(f'Produto {contador}: R$ '))
        totalcompra += precoproduto
        contador +=1
    valordinheiro = float(input('\nQual é o valor em dinheiro que o cliente deu? R$ '))
    troco = valordinheiro - totalcompra
    print(f'\nTotal da compra:', f'{f"R$ {totalcompra:.2f}":>20}')
    print(f'Dinheiro:', f'{f"R$ {valordinheiro:.2f}":>28}')
    print(f'Troco:', f'{f"R$ {troco:.2f}":>31}\n')
    opcao = ' '
    while opcao not in 'SN' or not opcao:
        opcao = str(input('Ir para o próximo cliente? [S/N] ')).upper()
        if opcao not in 'SN' or not opcao:
            print('Opção inválida! Tente novamente.')
        else:
            if opcao == 'S':
                system('cls' if name == 'nt' else 'clear')