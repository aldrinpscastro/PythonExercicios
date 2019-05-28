nota1 = float(input('Digite a nota 1:'))
nota2 = float(input('Digite a nota 2: '))
media = (nota1 + nota2) / 2
if media >= 6 <= 10:
    mensagem = 'APROVADO'
    if media >= 9 and media <= 10:
        conceito = 'A'
    if media >=7.5 and media < 9:
        conceito = 'B'
    if media >= 6 and media < 7.5:
        conceito = 'C'
else:
    mensagem = 'REPROVADO'
    if media >= 4 and media < 6:
        conceito = 'D'
    if media < 4:
        conceito = 'E'
print(f'\n{"Nota 1:":<10}', f'{nota1:^8}')
print(f'{"Nota 2:":<10}', f'{nota2:^8}')
print(f'{"Média:":<10}', f'{media:^8}')
print(f'{"Conceito:":<10}', f'{conceito:^8}')
print(f'{"Situação:":<10}', f'{mensagem:^8}')

