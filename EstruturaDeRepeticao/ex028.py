qcds = ' '
while not qcds.isdigit() or not qcds:
    qcds = str(input('Digite a quantidade de CDs da coleção: '))
    if not qcds.isdigit() or not qcds:
        print('Dados inválidos! Tente novamente.')
    else:
        qcds = int(qcds)
        qcdspmedia = qcds
        break
soma = 0
while qcds != 0:
    preco = ' '
    while not preco.isdigit() or not preco:
        preco = str(input(f'Digite o preço do CD nº {qcds}: '))
        if not preco.isdigit() or not preco:
            try:
                preco = float(preco)
                soma += preco
                break
            except ValueError:
                print('Dados inválidos! Tente novamente.')
        else:
            preco = int(preco)
            soma += preco
            break
    qcds -= 1
media = soma / qcdspmedia
print(f'\nValor insvestido na coleçao:{f" R$ {soma:.2f}":>15}')
print(f'Valor médio investido por CD:{f"R$ {media:.2f}":>14}')