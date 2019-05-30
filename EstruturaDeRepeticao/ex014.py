contpar = 0
contimpar = 0
for i in range(1, 11):
    numero = int(input(f'Digite o {i}° número: '))
    if numero % 2 == 0:
        contpar += 1
    else:
        contimpar += 1
print(f'Você digitou {contpar} números pares  e {contimpar} números ímpares.')