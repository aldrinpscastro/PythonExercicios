from datetime import date
salario = float(input('Digite o salário inicial: '))
ano = 1995
aumento = 0.015
while ano <= date.today().year:
    if ano == 1996:
        salario *= (1 + aumento)
    if ano > 1996:
        aumento *= 2
        salario *= (1 + aumento)
    if ano == 1995:
        print(f'Em {ano} ganha R$ {salario:.2f}.')
    else:
        print(f'Com o aumento, em {ano} ganha R$ {salario:.2f}.')
    ano += 1
