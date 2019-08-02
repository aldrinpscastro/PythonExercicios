from random import choice, shuffle
palavras = []
with open('../palavras.txt', 'r') as palavra:
    for i in palavra:
        palavras.append((i.replace('\n', '').upper()))
palavraescolhida = choice(palavras)
palavraembaralhada = list(palavraescolhida)
shuffle(palavraembaralhada)
palavraembaralhada = ''.join((palavraembaralhada))
print('JOGO DA PALAVRA EMBARALHADA\n')
print(f'A palavra embaralha é: "{palavraembaralhada}"')
erros = 0
qualeapalavra = ''
while erros < 6 or qualeapalavra == palavraescolhida:
    qualeapalavra = input('Qual é a palavra: ').upper()
    if qualeapalavra == palavraescolhida:
        break
    else:
        print(f'Você errou sua {erros + 1}ª tentativa.')
    erros += 1
if qualeapalavra == palavraescolhida:
    print(f'A palavra é: "{palavraescolhida}"')
    print('Você ganhou!')
else:
    print(f'A palavra é: "{palavraescolhida}"')
    print('Você perdeu!')
