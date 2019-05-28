quilomorango = int(input('Digite a quantidade em Kg de morango:'))
quilomaca = int(input('Digite a quantidade em Kg de maçã:'))
if quilomorango <= 5:
    precototalmorango = quilomorango * 2.5
else:
    precototalmorango = quilomorango * 2.2
if quilomaca <= 5:
    precototalmaca = quilomaca * 1.8
else:
    precototalmaca = quilomaca * 1.5
precototal = precototalmaca + precototalmorango
if quilomaca + quilomorango > 8 or precototal > 25:
    precototal *= (1 - 0.1)
print(f'\nValor a ser pago: R$ {precototal:.2f}')
