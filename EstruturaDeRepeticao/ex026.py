print(f'{" Eleição ":=^40}')
print(f'Digite "A" para votar no canditado 1.\nDigite "B" para votar no canditado 2.\nDigite "C" para votar no canditado 3.\n')
nteleitores = int(input('Qual é número total de leitores? '))
print()
qvcandi1 = 0
qvcandi2 = 0
qvcandi3 = 0
while nteleitores != 0:
    opcao = ' '
    while opcao not in 'ABC' or not opcao:
        opcao = str(input(f'Eleitor nº {nteleitores}. Em qual canditado você vai votar? ')).upper()
        if opcao not in 'ABC' or not opcao:
            print('Opção inválida. Tente novamente.')
        if opcao == 'A':
            qvcandi1 += 1
        if opcao == 'B':
            qvcandi2 += 1
        if opcao == 'C':
            qvcandi3 += 1
    nteleitores -= 1
print(f'\nO candidato 1 recebeu {qvcandi1} voto(s).\nO candidato 2 recebeu {qvcandi2} voto(s).\nO candidato 3 recebeu {qvcandi3} voto(s).')
