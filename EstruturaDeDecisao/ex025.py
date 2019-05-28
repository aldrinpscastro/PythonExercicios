contadordsim = 0
opcao = str(input('Telefonou para vítima? [S/N] ')).upper()
if opcao in 'SN':
    if opcao == 'S':
        contadordsim += 1
else:
        print('Opção inválida.')
        exit(1)
opcao = str(input('Esteve no local do crime? [S/N] ')).upper()
if opcao in 'SN':
    if opcao == 'S':
        contadordsim += 1
else:
        print('Opção inválida.')
        exit(1)
opcao = str(input('Mora perto da vítima? [S/N] ')).upper()
if opcao in 'SN':
    if opcao == 'S':
        contadordsim += 1
else:
        print('Opção inválida.')
        exit(1)
opcao = str(input('Devia para vítima? [S/N] ')).upper()
if opcao in 'SN':
    if opcao == 'S':
        contadordsim += 1
else:
        print('Opção inválida.')
        exit(1)
opcao = str(input('Já trabalhou para vítima? [S/N] ')).upper()
if opcao in 'SN':
    if opcao == 'S':
        contadordsim += 1
else:
        print('Opção inválida.')
        exit(1)
if contadordsim == 2:
    print('Você é considerado como "Suspeita".')
elif contadordsim >= 3 and contadordsim <= 4:
    print('Você é considerado como "Cúmplice".')
elif contadordsim == 5:
    print('Você é considerado como "Assassino".')
else:
    print('Você é considerado como "Inocente".')