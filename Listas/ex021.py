carros = ["Fusca", "Gol", "Uno", "Vectra", "Peugeout",]
KmporL = [7, 10, 12.5, 9, 14.5]
print('comparativo de consumo de combustível'.upper())
print('=' * 37, '\n')
for i in range(1, len(carros) + 1):
    print(f'Veículo {i}')
    print(f'Nome: {carros[i-1]}')
    print(f'Km por Litro: {KmporL[i-1]}\n')
print('relatório final'.upper())
print('=' * 15, '\n')
print(f'{"Nº":>3}{"Veículo":^10}{"Km por Litro":^16}{"Litro por 1000K":^15}{"Preço":^11}')
for i in range(1, len(carros) + 1):
    print(f'{i:^3}{carros[i-1]:^10}{KmporL[i-1]:^16.1f}{f"{1000/KmporL[i-1]:.1f} litros":^15}{f"R$ {1000/KmporL[i-1]*2.25:.2f}":^11}')
print(f'\nO menor consumo é do {carros[KmporL.index(max(KmporL))]}.')
