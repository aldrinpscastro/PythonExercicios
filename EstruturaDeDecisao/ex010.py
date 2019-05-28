print('Digite M para matutino.')
print('Digite V para vespertino')
print('Digite N para noturno.')
opcao = str(input('Em que turno você estuda? ')).upper()
if opcao in 'MVN':
    if opcao == 'M':
        print('Bom dia!')
    if opcao == 'V':
        print('Boa tarde!')
    if opcao == 'N':
        print('Boa noite!')
else:
    print('Valor inválido.')
