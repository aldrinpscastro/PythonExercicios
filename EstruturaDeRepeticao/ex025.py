opcao = ' '
somaidade = 0
qidades = 0
while opcao != 'N':
    opcao = ' '
    idade = int(input('Qual é a sua idade? '))
    somaidade += idade
    qidades += 1
    while opcao not in 'SN' or not opcao:
        opcao = str(input('Quer continuar? [S/N] ')).upper()
        if opcao not in 'SN' or not opcao:
            print('Opção inválida! Tente novamente.')
mediaidade = somaidade / qidades
if mediaidade >= 0 and mediaidade <= 25:
    turma = 'JOVEM'
if mediaidade >= 26 and mediaidade <= 60:
    turma = 'ADULTA'
if mediaidade > 60:
    turma = 'IDOSA'
print(f'A turma foi considerada como "{turma}".')