def desenhamoldura(coluna=10, linha=5):
    if coluna < 1 or coluna > 20 and linha < 1 or linha > 20:
        coluna = 10
        linha = 5
        print(f'Trocando para {coluna} coluna(s) e {linha} linha(s).')
    print('+' * coluna, ' ', '-' * coluna, ' ', '|' * coluna)
    for i in range(0, linha - 2):
        print('+' + ' ' * (coluna - 2) + '+', ' ', '-' + ' ' * (coluna - 2) + '-', ' ', '|' + ' ' * (coluna - 2) + '|')
    print('+' * coluna, ' ', '-' * coluna, ' ',  '|' * coluna)
linha = int(input('Digite a quantidade de linhas: '))
coluna = int(input('Digite a quantidade de colunas: '))
desenhamoldura(coluna, linha)