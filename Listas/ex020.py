salarios = []
abonos = []
print('Projeção de gastos com abono'.upper())
print('=' * 28, '\n')
while True:
    salario = float(input('Qual é o valor do seu salário bruto de dezembro? R$ '))
    if salario == 0:
        break
    salarios.append(salario)
    if salario * 0.2 < 100:
        abonos.append(100)
    else:
        abonos.append(salario * 0.2)
print(f'\n{"Salário":<11}- Abono')
for i in range(0 , len(salarios)):
    print(f'R$ {salarios[i]:<7} - R$ {abonos[i]:<10.2f}')
print(f'\nForam processados {len(salarios)} colaborador(es).')
print(f'Total gasto com abonos: R$ {sum(abonos):.2f}')
print(f'Valor mínimo pago a {abonos.count(100)} colaborador(es)')
print(f'Maior valor de abono pago: R$ {max(abonos):.2f}')
