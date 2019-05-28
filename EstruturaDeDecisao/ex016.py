a = int(input('Digite o valor de "a" da equação do 2º grau: '))
if a == 0:
    print('Não é uma equação do 2º grau.')
    exit(0)
b = int(input('Digite o valor de "b" da equação do 2º grau: '))
c = int(input('Digite o valor de "c" da equação do 2º grau: '))
delta = b ** 2 - 4 * a * c
if delta < 0:
    print('A equação não possui raízes reais.')
    exit(0)
elif delta == 0:
    x = (- b + delta ** (1/2)) / (2 * a)
    print(f'A raíz é igual a {x}.')
else:
    x1 = (- b + delta ** (1/2)) / (2 * a)
    x2 = (- b - delta ** (1/2)) / (2 * a)
    print(f'A raíz 1 é igual a {x1}.')
    print(f'A raíz 2 é igual a {x2}.')