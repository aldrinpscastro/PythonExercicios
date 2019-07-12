def somaImposto(taxaImposto, custo):
    taxaImposto /= 100
    taxaImposto *= custo
    custo += taxaImposto
    custo = f'R$ {custo:.2f}'
    custo = custo.replace('.',',')
    return custo
print(somaImposto(10, 1508))