from statistics import mean
while True:
    atleta = input('Nome do atleta? ')
    if not atleta:
        break
    saltos = []
    for i in range(1, 6):
        salto = float(input(f'Qual é a distância do {i}º salto? '))
        saltos.append(salto)
    print('Atleta: ', atleta)
    print()
    print('Primeiro salto: ', saltos[0], ' m')
    print('Segundo salto: ', saltos[1], ' m')
    print('Terceiro salto: ', saltos[2], ' m')
    print('Quarto salto: ', saltos[3], ' m')
    print('Quinto salto: ', saltos[4], ' m')
    print('Resultado final:')
    print('Atleta: ', atleta)
    print('Saltos: ', end='')
    for i in range(0, len(saltos)):
        if i == len(saltos) - 1:
            print(saltos[i])
        else:
            print(f'{saltos[i]} - ', end='')
    print('Média: ', mean(saltos), ' m')
