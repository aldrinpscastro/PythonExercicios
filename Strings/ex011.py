from random import randint
palavras = []
with open('../palavras.txt', 'r') as palavra:
    for i in palavra:
        i = i.replace('\n', '').upper()
        palavras.append(i)
palavraescolhida = palavras[randint(0, len(palavras) - 1)]
forca = [' _ '] * len(palavraescolhida)
erros = 0
completo = False
while erros < 6:
    letra = input('Digite um letra: ').upper()
    if letra not in palavraescolhida:
        erros += 1
        print(f'Você errou pela {erros}ª vez. Tente de novo!')
    else:
        indices = []
        for i in range(0, len(palavraescolhida)):
            try:
                indices.append(palavraescolhida.index(letra, i))
            except ValueError:
                continue
        indices = list(dict.fromkeys(indices))
        for i in indices:
            forca[i] = forca[i].replace('_', letra)
        print('A palavra é:',''.join(forca))
        if ' _ ' not in forca:
            print('Que bom! Você não foi enforcado. :)')
            break
if erros == 6:
    print('Que pena! Você foi enforcado. :(')