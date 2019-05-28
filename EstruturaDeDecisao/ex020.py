nota1 = float(input('Digite a nota 1: '))
nota2 = float(input('Digite a nota 2: '))
nota3 = float(input('Digite a nota 3: '))
media = (nota1 + nota2 + nota3) / 3
if media == 10:
    print(f'{"SITUAÇÃO:":<10}', f'{"APROVADO COM DISTINÇÃO":^22}')
    print(f'{"MÉDIA:":<10}', f'{media:^22}')
elif media >= 7:
    print(f'{"SITUAÇÃO:":<10}', f'{"APROVADO":^22}')
    print(f'{"MÉDIA:":<10}', f'{media:^22.1f}')
else:
    print(f'{"SITUAÇÃO:":<10}', f'{"REPROVADO":^8}')
    print(f'{"MÉDIA:":<10}', f'{media:^22.1f}')