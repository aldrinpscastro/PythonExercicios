alturas = []
idades = []
for i in range(1, 6):
    altura = float(input(f'Digite a altura da pessoa nº {i}: '))
    idade = int(input(f'Digite a idade da pessoa nº {i}: '))
    alturas.append(altura)
    idades.append(idade)
alturas.reverse()
idades.reverse()
print(alturas)
print(idades)