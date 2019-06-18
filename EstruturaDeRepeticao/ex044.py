print('=== Tabela para votação ===')
print('1 - José')
print('2 - João')
print('3 - Joana')
print('4 - Jassa')
print('5 - Voto nulo')
print('6 - Voto branco')
votosjose = 0
votosjoao = 0
votosjoana = 0
votosjassa = 0
votosnulos = 0
votosbranco = 0
votostotal = 0
voto = ' '
while voto not in '0':
    voto = ' '
    while voto not in '0123456' or not voto:
        voto = str(input('\nQual é o seu voto? '))
        if voto not in '0123456' or not voto:
            print('OPÇÃO INVÁLIDA!! Tente novamente.')
    if voto == '1':
        votosjose += 1
    if voto == '2':
        votosjoao += 1
    if voto == '3':
        votosjoana += 1
    if voto == '4':
        votosjassa += 1
    if voto == '5':
        votosnulos += 1
    if voto == '6':
        votosbranco += 1
    if voto != '0':
        votostotal += 1
print(f'\n* Total de votos para o candidato José: {votosjose}')
print(f'* Total de votos para o candidato João: {votosjoao}')
print(f'* Total de votos para a candidato Joana: {votosjoana}')
print(f'* Total de votos para o candidato Jassa: {votosjassa}')
print(f'* Total de votos nulos: {votosnulos}')
print(f'* Total de votos brancos: {votosbranco}')
print(f'* Percentagem de votos nulos sobre o total de votos: {votosnulos / votostotal * 100:.2f} %')
print(f'* Percentagem de votos brancos sobre o total de votos: {votosbranco / votostotal * 100:.2f} %')
