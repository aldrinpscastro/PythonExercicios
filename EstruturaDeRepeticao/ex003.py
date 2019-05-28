Nome = ''
idade = -1
salario = -1
sexo = ''
estadocivil = ''
while len(Nome) <= 3 or not Nome:
    Nome = str(input('Digite um nome: '))
    if len(Nome) > 3:
        break
    print('ERRO! Nome tem menos de três caracteres. Tente novamente.')
while idade < 0 or idade > 150 or not idade:
    idade = int(input('Digite uma idade: '))
    if idade >= 0 and idade <= 150:
        break
    print('ERRO! Tente novamene.')
while salario < 0 or not salario:
    salario = float(input('Digite um valor de salário: '))
    if salario > 0:
        break
    print('ERRO! Tente novamene.')
while sexo not in 'MF' or not sexo:
    sexo = str(input('Digite um sexo: [M/F]')).upper()
    if sexo in 'MF' and sexo:
        break
    print('ERRO! Sexo inválido.')
while estadocivil not in 'SCVD' or not estadocivil:
    estadocivil = str(input('Digite um estado civil: [S/C/V/D]')).upper()
    if sexo in 'SCVD' and estadocivil:
        break
    print('ERRO! Estado civil inválido.')