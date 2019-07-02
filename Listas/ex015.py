from statistics import mean
lista = []
while True:
    nota = float(input('Digite a nota: '))
    if nota >= 0:
        lista.append(nota)
    else:
        break
print(f'Quantidade de valores lidos; {len(lista)}')
print('Valores lidos;', end='')
for i in lista:
    print(f' {i}', end=' ')
print()
lista.reverse()
print('Valores lidos reverso;', end='')
contador = 0
for i in lista:
    if contador == 0:
        print(f' {i}')
    else:
        print(f'{"":^23}{i}')
    contador += 1
print(f'Soma dos valores; {sum(lista)}')
print(f'Média dos valores; {mean(lista)}')
print('Valores acima da média;', end='')
contador = 0
for i in lista:
    if i > mean(lista):
        if contador == 0:
            print(f' {i}')
        else:
            print(f'{"":^24}{i}')
        contador += 1
print('Valores abaixo de sete;', end='')
contador = 0
for i in lista:
    if i < 7:
        if contador == 0:
            print(f' {i}')
        else:
            print(f'{"":^24}{i}')
        contador += 1

print('Tchau!')