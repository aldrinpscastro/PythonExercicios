nota = float(input('Digite uma nota: '))
soma = nota
qnotas = 1
opcao = ' '
while opcao not in 'SN' or not opcao:
    opcao = str(input('Quer continuar? [S/N] ')).upper()
    if opcao not in 'SN' or not opcao:
        print('Opção inválida. Tente Novamente.')
while opcao != 'N':
    nota = float(input('Digite outra nota: '))
    soma += nota
    qnotas += 1
    opcao = ' '
    while opcao not in 'SN' or not opcao:
        opcao = str(input('Quer continuar? [S/N] ')).upper()
        if opcao not in 'SN' or not opcao:
            print('Opção inválida. Tente Novamente.')
media = soma / qnotas
print(f'A média aritmética da(s) {qnotas} nota(s) digitadas é {media:.2f}.')