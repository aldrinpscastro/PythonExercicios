numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print('\nDigite 1 para adição.')
print('Digite 2 para subtração.')
print('Digite 3 para multiplicação.')
print('Digite 4 para divisão.\n')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    soma = numero1 + numero2
    print(f'O resultado é igual a {soma}.')
    if soma % 2 == 0:
        print('a.  É par')
    else:
        print('a. É ímpar.')
    if soma > 0:
        print('b. É positivo.')
    else:
        print('b. É negativo')
    if soma - int(soma) == 0:
        print('c. É inteiro')
    else:
        print('c. É Decimal.')
if opcao == 2:
    subtracao = numero1 - numero2
    print(f'O resultado é igual a {subtracao}.')
    if subtracao % 2 == 0:
        print('a.  É par')
    else:
        print('a. É ímpar.')
    if subtracao > 0:
        print('b. É positivo.')
    else:
        print('b. É negativo')
    if subtracao - int(subtracao) == 0:
        print('c. É inteiro')
    else:
        print('c. É Decimal.')
if opcao == 3:
    multiplicacao = numero1 * numero2
    print(f'O resultado é igual a {multiplicacao}.')
    if multiplicacao % 2 == 0:
        print('a.  É par')
    else:
        print('a. É ímpar.')
    if multiplicacao > 0:
        print('b. É positivo.')
    else:
        print('b. É negativo')
    if multiplicacao - int(multiplicacao) == 0:
        print('c. É inteiro')
    else:
        print('c. É Decimal.')
if opcao == 4:
    divisao = numero1 / numero2
    print(f'O resultado é igual a {divisao}.')
    if divisao % 2 == 0:
        print('a.  É par')
    else:
        print('a. É ímpar.')
    if divisao > 0:
        print('b. É positivo.')
    else:
        print('b. É negativo')
    if divisao - int(divisao) == 0:
        print('c. É inteiro')
    else:
        print('c. É Decimal.')
