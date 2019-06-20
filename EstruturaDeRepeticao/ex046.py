from statistics import mean
while True:
    Nome = input('Atleta: ')
    if not Nome:
        break
    saltos = []
    for i in range(1, 6, 1):
        salto = float(input(f'Qual foi a distância do {i}º salto? '))
        saltos.append(salto)
    print(f'\nAtleta : {Nome}')
    print(f'Primeiro Salto: {saltos[0]} m.')
    print(f'Segundo Salto: {saltos[1]} m.')
    print(f'Terceiro Salto: {saltos[2]} m.')
    print(f'Quarto Salto: {saltos[3]} m.')
    print(f'Quinto Salto: {saltos[4]} m.')
    print(f'Melhor Salto: {max(saltos)} m.')
    print(f'Pior Salto: {min(saltos)} m.')
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))
    print(f'Média dos demais saltos: {mean(saltos):.2f} m.')
    print('Resultado final:')
    print(f'{Nome}: {mean(saltos):.2f} m.\n')