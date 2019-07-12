def valorPagamento(valorPrestacoes, ndatraso=0):
    if ndatraso == 0:
        return valorPrestacoes
    else:
        valorPagamento = valorPrestacoes * (1 + (0.03 + (ndatraso * 0.001)))
        return f'R$ {valorPagamento:.2f}'.replace('.', ',')
valorp = -1
while valorp != 0:
    valorp = int(input('Digite o valor da prestação: '))
    ndatraso = int(input('Digite nº de dias atrasados: '))
    print(f'\nVocê vai pagar {valorPagamento(valorp, ndatraso)}.\n')