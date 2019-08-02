telefone = input('Digite um número de telefone: ')
if len(telefone) == 7 or len(telefone) == 8 and telefone.isnumeric():
    if len(telefone) == 7:
        print(f'Telefone: {telefone}')
        print(f'Telefone possui {len(telefone)} Dígitos. Vou acrescentar o dígito 3 na frente.')
        telefone = list(telefone)
        telefone.insert(0, '3')
        telefoneformatado = telefone
        telefoneformatado.insert(4, '-')
        telefone = ''.join(telefone).replace('-', '')
        telefoneformatado = ''.join(telefoneformatado)
        print(f'Telefone corrigido sem formatação: {telefone}')
        print(f'Telefone corrigido com formatação: {telefoneformatado}')
    elif len(telefone) == 8:
        print(f'Telefone: {telefone}')
        print(f'Telefone possui {len(telefone)} Dígitos.')
        telefoneformatado = list(telefone)
        telefoneformatado.insert(4, '-')
        telefoneformatado = ''.join(telefoneformatado)
        print(f'Telefone sem formatação: {telefone}')
        print(f'Telefone corrigido com formatação: {telefoneformatado}')
elif len(telefone) == 8 and telefone[len(telefone) - 5] == '-' and telefone[:3].isnumeric() and telefone[4:].isnumeric():
    print(f'Telefone: {telefone}')
    print(f'Telefone possui {len(telefone) - 1} Dígitos. Vou acrescentar o dígito 3 na frente.')
    telefone = list(telefone)
    telefone.insert(0, '3')
    telefone = ''.join(telefone)
    telefonesemformatacao = telefone.replace('-', '')
    print(f'Telefone corrigido sem formatação: {telefonesemformatacao}')
    print(f'Telefone corrigido com formatação: {telefone}')
elif len(telefone) == 9 and telefone[len(telefone) - 5] == '-' and telefone[:4].isnumeric() and telefone[5:].isnumeric():
    print(f'Telefone: {telefone}')
    print(f'Telefone possui {len(telefone) - 1} Dígitos.')
    telefonesemformatacao = telefone.replace('-', '')
    print(f'Telefone corrigido sem formatação: {telefonesemformatacao}')
    print(f'Telefone com formatação: {telefone}')
else:
    print('Não é um número de telefone.')