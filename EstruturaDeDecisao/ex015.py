lado1 = int(input('Digite o lado 1: '))
lado2 = int(input('Digite o lado 2: '))
lado3 = int(input('Digite o lado 3: '))
if lado1 + lado2 > lado3 or lado2 + lado3 > lado1 or lado3 + lado1 > lado2:
    print('Os valores podem formar um triângulo')
    if lado1 == lado2 and lado2 == lado3:
        print('E o triângulo formado é um equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('E o triângulo formado é um isóceles.')
    else:
        print('E o triângulo formado é um escaleno.')
else:
    print('Os valores não podem formar um triângulo.')
