salario = float(input('Qual é o seu salário? '))
if salario <= 280:
    aumento = 0.2
if salario > 280 <= 700:
    aumento = 0.15
if salario > 700 <= 1500:
    aumento = 0.1
if salario > 1500:
    aumento = 0.05
print(f'{"Salário antes do reajuste:":<40}', f'R$ {salario:.2f}')
print(f'{"Percentual de aumento aplicado:":<40}', f'{aumento * 100:.0f} %')
print(f'{"Valor do aumento:":<40}', f'R$ {salario * aumento:.2f}')
print(f'{"Novo salário, após aumento:":<40}', f'R$ {salario * (1 + aumento):.2f}')
