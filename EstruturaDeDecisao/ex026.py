qlitro = float(input('digite quantos litros de combustível você quer: '))
print('\nDigite "A" para Álcool.')
print('Digite "G" para Gasolina.')
opcao = str(input('\nDigite sua opção: ')).upper()
if opcao in 'AG':
    if opcao == 'A':
        if qlitro <= 20:
            precototal = 1.9 * qlitro * (1 - 0.03)
        else:
            precototal = 1.9 * qlitro * (1 - 0.05)
        print(f'\nValor a ser pago: R$ {precototal:.2f}')
    else:
        if qlitro <= 20:
            precototal = 2.5 * qlitro * (1 - 0.04)
        else:
            precototal = 2.5 * qlitro * (1 - 0.06)
        print(f'\nValor a ser pago: R$ {precototal:.2f}')
else:
    print('Opção inválida.')
