area = float(input('Área a ser pintada: '))
litrosparacompra = area / 6 * 1.1
quantlatastinta = round(litrosparacompra / 18)
quantgaloes = round(litrosparacompra / 3.6)
precogaloes = quantgaloes * 25
precotintalata = quantlatastinta * 80
precotintagaloes = round((litrosparacompra - 3.6) / 18) * 80 + 1 * 25
print(f'{"Quantidade de latas de tinta para comprar:":<50}', f'{quantlatastinta} lata(s)')
print(f'{"Quantidade de latas de galões para comprar:":<50}', f'{quantgaloes} galão(s)')
print(f'{"Preço comprando apenas latas de 18 litros:":<50}', f'R$ {precotintalata:.2f}')
print(f'{"Preço comprando apenas galôes de 3.6 litros:":<50}', f'R$ {precogaloes:.2f}')
print(f'{"Preços comprando galões e latas com menor preço:":<50}', f'R$ {precotintagaloes:.2f}')

