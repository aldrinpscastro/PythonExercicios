frase = input('Digite uma frase: ')
qespacos = 0
qvogais = 0
for i in frase:
    if i == ' ':
        qespacos += 1
    if i in 'aeiou':
        qvogais += 1
print(f'Existem {qespacos} espaço(s) na frase.')
print(f'As vogais aparecem {qvogais} vez(es).')