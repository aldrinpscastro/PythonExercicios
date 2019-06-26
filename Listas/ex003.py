from statistics import mean
notas = []
for i in range(0, 4):
    nota = float(input('Digite a nota: '))
    notas.append(nota)
for i in notas:
    print(f'Nota: {i}')
print(f'Média: {mean(notas)}')
