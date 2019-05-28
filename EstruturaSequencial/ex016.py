area = float(input('Área a ser pintada: '))
litrosparacompra = area / 3
quantlatastinta = round(litrosparacompra / 18)
precotinta = quantlatastinta * 80
print(f'{"Quantidade de latas de tinta para comprar:":<50}', f'{quantlatastinta} lata(s)')
print(f'{"Preço total:":<50}', f'R$ {precotinta:.2f}')

