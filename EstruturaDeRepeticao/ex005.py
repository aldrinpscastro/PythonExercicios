opcao = ' '
while opcao != 'N':
    popA = int(input('Digite a quantidade de habitantes do país A: '))
    txcreA = float(input('Digite a taxa de cresccimento do país A em %: ')) / 100 + 1
    popB = int(input('Digite a quantidade de habitantes do país B: '))
    txcreB = float(input('Digite a taxa de cresccimento do país B em %: ')) / 100 + 1
    if txcreB >= txcreA and popA <= popB:
        while txcreB >= txcreA:
            print('A taxa de crescimento do país B deve ser menor que a do país A.')
            txcreB = float(input('Digite a taxa de cresccimento do país B em %: ')) / 100 + 1
    else:
        while txcreB <= txcreA:
            print('A taxa de crescimento do país A deve ser menor que a do país B.')
            txcreA = float(input('Digite a taxa de cresccimento do país A em %: ')) / 100 + 1
    anospassados = 0
    while popA <= popB:
        popA *= txcreA
        popB *= txcreB
        anospassados += 1
    print(f'Serão necessários {anospassados} anos para que a população do país A ultrapasse a população do país B.')
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Gostaria de Repetir? [S/N]')).upper()[0]
        if opcao not in 'SN' or not opcao:
            print('Opcão inválida. Tente novamente.')

