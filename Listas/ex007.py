numeros = [1, 2, 3, 4, 5]
print(sum(numeros))
multiplicacao = 1
mostrar = ''
for i in numeros:
    multiplicacao *= i
    mostrar += f'{i} '
print(multiplicacao)
print(mostrar)
