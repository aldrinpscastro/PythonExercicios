numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)
soma = 0
for i in range(0, len(numeros)):
    if i < len(numeros) - 1:
        print(f'{numeros[i]}² + ', end='')
    else:
        print(f'{numeros[i]}² = ', end='')
    soma += numeros[i] ** 2
print(soma)