string1 = 'Olá'
string2 = 'Mundo'
print(f'String 1: {string1}')
print(f'String 2: {string2}')
print(f'tamanho de "{string1}": {len(string1)}')
print(f'tamanho de "{string2}": {len(string2)}')
if len(string1) == len(string2):
    tamanho = 'iguais'
else:
    tamanho = 'diferentes'
if string1 == string2:
    conteudo = 'igual'
else:
    conteudo = 'diferente'
print(f'As duas strings são de tamanhos {tamanho}.')
print(f'As duas strings possuem conteúdo {conteudo}.')