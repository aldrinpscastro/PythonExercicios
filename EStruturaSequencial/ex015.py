ganhohora = float(input('Quanto você ganha por hora? '))
horames = int(input('Quantas horas você trabalha no mês? '))
salariobruto = ganhohora * horames
IR = salariobruto * 0.11
INSS = salariobruto * 0.08
Sindicato = salariobruto * 0.05
salarioliquido = salariobruto - IR - INSS - Sindicato
print(f'{"+ Salário Bruto:":<25}', f'R$ {salariobruto:.2f}')
print(f'{"- IR (11%):":<25}', f'R$ {IR:.2f}')
print(f'{"- INSS (8%):":<25}', f'R$ {INSS:.2f}')
print(f'{"- Sindicato (5%):":<25}', f'R$ {Sindicato:.2f}')
print(f'{"= Salário Líquido:":<25}', f'R$ {salarioliquido:.2f}')