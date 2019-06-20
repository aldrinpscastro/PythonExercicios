from statistics import mean
while True:
    Nome = input('Atleta: ')
    if not Nome:
        break
    saltos = []
    for i in range(1, 8, 1):
        salto = float(input(f'Qual foi a nota: '))
        saltos.append(salto)
    print(f'\nAtleta : {Nome}')
    print(f'Nota: {saltos[0]}')
    print(f'Nota: {saltos[1]} ')
    print(f'Nota: {saltos[2]}')
    print(f'Nota: {saltos[3]}')
    print(f'Nota: {saltos[4]}')
    print(f'Nota: {saltos[5]}')
    print(f'Nota: {saltos[6]}')
    print('Resultado final:')
    print(f'Atleta: {Nome}')
    print(f'Melhor Nota: {max(saltos)}')
    print(f'Pior Nota: {min(saltos)}')
    saltos.remove(max(saltos))
    saltos.remove(min(saltos))
    print(f'Média: {mean(saltos):.2f} m.\n')