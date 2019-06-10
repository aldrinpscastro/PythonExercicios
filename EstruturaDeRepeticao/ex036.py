numero = int(input('Montar a tabuada de: '))
comeca = int(input('Que começa em: '))
termina = int(input('E termina em: '))
while termina < comeca:
    print('ERRO!. nº termina menor que o nº começa. Tente novamente.')
    termina = int(input('E termina em: '))
print(f'\nMontar tabuada de 5. Começando em {comeca} e terminando em {termina}:\n')
for i in range(comeca, termina + 1, 1):
    print(f'{numero} x {i} = {numero * i}')