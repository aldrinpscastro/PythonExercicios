totalalunos = 0
somaacertos = 0
maioracerto = 0
menoracerto = 10
gabarito = ''
validarrespostas = True
while len(gabarito) != 10 or validarrespostas is not True:
    gabarito = str(input('Professor! Digite o gabarito: ')).strip().upper()
    if len(gabarito) != 10 or not gabarito:
        print('Gabarito inválido! Tente novamente.')
    else:
        for i in range(0, 10, 1):
            if gabarito[i] not in 'ABCDE':
                validarrespostas = False
                print('Gabarito inválido! Tente novamente.')
                break
opcao = ''
while opcao not in 'N' or not opcao:
    opcao = ''
    respostas = ''
    resposta = ' '
    contaracertos = 0
    for i in range(1, 11, 1):
        resposta = ' '
        while resposta not in 'ABCDE' or not resposta:
            resposta = str(input(f'Digite a resposta da questão {i}: ')).strip().upper()
            if resposta not in 'ABCDE' or not resposta:
                print('Opção inválida! Tente novamente.')
        respostas += resposta
        if respostas[i-1] == gabarito[i-1]:
            contaracertos += 1
    somaacertos += contaracertos
    if contaracertos > maioracerto:
        maioracerto = contaracertos
    if contaracertos < menoracerto:
        menoracerto = contaracertos
    while opcao not in 'SN' or not opcao:
        opcao = str(input('Outro aluno vai utilizar o sistema? [S/N]')).strip().upper()
        if opcao not in 'SN' or not opcao:
            print('Opção  inválida! Tente novamente.')
    totalalunos += 1
mediaturma = somaacertos / totalalunos
print(f'\nMaior acerto: {maioracerto}.')
print(f'Menor acerto: {menoracerto}.')
print(f'Total de alunos que utilizaram o sistema: {totalalunos}.')
print(f'Média das notas da turma: {mediaturma}')