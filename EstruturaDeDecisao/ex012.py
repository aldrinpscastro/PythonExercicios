valorhora = float(input('Qual é o valor da sua hora? '))
qhorames = int(input('Qual a quantidade de horas trabalhadas no mês? '))
salariobruto = valorhora * qhorames
if salariobruto <= 900:
    IR = 0
if salariobruto > 900 <= 1500:
    IR = 0.05
if salariobruto > 1500 <= 2500:
    IR = 0.1
if salariobruto > 2500:
    IR = 0.2
INSS = 0.1
FGTS = 0.11
SINDICATO = 0.03
descontoIR = salariobruto * IR
descontoINSS = salariobruto * INSS
recolhimentoFGTS = salariobruto * FGTS
descontoSINDICATO = salariobruto * SINDICATO
totaldescontos = descontoIR + descontoINSS + descontoSINDICATO
salarioliquido = salariobruto - totaldescontos
print(f"\n{f'Salário Bruto: ({valorhora} * {qhorames})':<40}: R$ {salariobruto:.2f}")
print(f"{f'(-) IR ({int(IR * 100)}%)':<40}: R$ {descontoIR:.2f}")
print(f"{f'(-) INSS ({int(INSS * 100)}%)':<40}: R$ {descontoINSS:.2f}")
print(f"{f'FGTS ({int(FGTS * 100)}%)':<40}: R$ {recolhimentoFGTS:.2f}")
print(f"{f'(-)Sindicato ({int(SINDICATO * 100)}%)':<40}: R$ {descontoSINDICATO:.2f}")
print(f"{f'Total de descontos':<40}: R$ {totaldescontos:.2f}")
print(f"{f'Salário Líquido':<40}: R$ {salarioliquido:.2f}")




