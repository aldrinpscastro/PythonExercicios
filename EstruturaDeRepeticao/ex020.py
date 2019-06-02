opcao = ' '
while opcao != 'N':
    opcao = ' '
    fatorial = -1
    while fatorial < 0 or fatorial > 16:
        fatorial = int(input('Digite qual número para fazer o fatorial: '))
        if fatorial < 0 or fatorial > 16:
            print('Você deve digitar um número inteiro positivo e menor que 16.')
    for i in range(fatorial, 0, -1):
        if i == 1:
            print(i, end=' = ')
        else:
            print(i, end=' x ')
        if i - 1 == 0:
            break
        else:
            fatorial *= i - 1
    print(fatorial)
    while opcao not in 'SN' or not opcao:
        opcao = str(input('Quer continuar? [S/N] ')).upper()
        if opcao not in 'SN' or not opcao:
            print('Opção inválida. Tente novamente.')