ValorDaDivida = float(input('Digite o valor da sua dívida: '))
QuantidadeDeParcelas = 1
Juros = 0
print('\nValor da Dívida  Valor dos Juros  Quantidade de Parcelas  Valor das Parcelas\n')
while QuantidadeDeParcelas <= 60:
    ValorDosJuros = ValorDaDivida * Juros
    ValorTotal = ValorDaDivida + ValorDosJuros
    ValorDasParcelas = (ValorDaDivida + ValorDosJuros) / QuantidadeDeParcelas
    print(f'{f"R$ {ValorTotal:.2f}":<16}', f'{f"R$ {ValorDosJuros:.2f}":<16}', f'{QuantidadeDeParcelas:<23}',f'{f"R$ {ValorDasParcelas:.2f}":<18}')
    if QuantidadeDeParcelas == 1:
        QuantidadeDeParcelas += 2
    else:
        QuantidadeDeParcelas += 3
    if QuantidadeDeParcelas == 3:
        Juros = 0.1
    else:
        Juros += 0.05