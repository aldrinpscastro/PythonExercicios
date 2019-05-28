peso = float(input('Qual é o peso do peixe em Kg: '))
excesso = int(peso - 50)
multa = 4 * excesso
if excesso < 1:
    multa = 0
print('Peso do peixe:', f'{peso:>10} Kg.')
print('Quilo excedente:', f'{excesso:>8} Kg.')
print('Multa:',f'{"R$ ":>17}' f'{multa:.2f}.')
