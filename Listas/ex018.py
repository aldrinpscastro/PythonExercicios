def percentual(nvotos, totalvotos):
    percentual = round(nvotos / totalvotos, 3) * 100
    percentual = str(percentual)
    percentual = percentual.replace('.', ',')
    return percentual
votos = []
print('Enquete: Qual foi o melhor jogador? ')
print('Informe o valor entre 1 e 23 ou 0 para sair!')
while True:
    nmjogador = int(input('Número do jogador (0=fim): '))
    if nmjogador == 0:
        break
    if nmjogador >= 1 and nmjogador <= 23:
        votos.append(nmjogador)
    else:
        print('Voto inválido! Será desconsiderado.'.upper())
print('Resultado da votação:')
print(f'Foram computados {len(votos)} voto(s).')
print(f'{"Jogador":^7}{"Votos":^7}{"%":^7}')
melhorjogador = [0, 0, '0']
for i in range(1, 24):
    if votos.count(i):
        print(f'{i:^7}{votos.count(i):^7}{f"{percentual(votos.count(i), len(votos))} %":^7}')
        if votos.count(i) > melhorjogador[1]:
            melhorjogador[0] = i
            melhorjogador[1] = votos.count(i)
            melhorjogador[2] = percentual(votos.count(i), len(votos))
print(f'O melhor jogador foi o número {melhorjogador[0]} com {melhorjogador[1]}'
      f' votos, correspondendo a {melhorjogador[2]}% do total de votos.')
