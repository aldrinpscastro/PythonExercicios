valor = int(input('Digite quanto você quer sacar: '))
if valor >= 10 and valor <= 600:
    qn100 = valor // 100
    rn100 = valor % 100
    qn50 = rn100 // 50
    rn50 = rn100 % 50
    qn10 = (rn100 % 50) // 10
    rn10 = (rn100 % 50) % 10
    qn5 = ((rn100 % 50) % 10) // 5
    rn5 = ((rn100 % 50) % 10) % 5
    qn1 = ((rn100 % 50) % 10) % 5
    print('Você sacará:\n')
    if qn100 > 0:
        print(f'{qn100} nota(s) de 100.')
    if rn100 > 0:
        if qn50 > 0:
            print(f'{qn50} nota(s) de 50.')
    if rn50 > 0:
        if qn10 > 0:
            print(f'{qn10} nota(s) de 10.')
    if rn10 > 0:
        if qn5 > 0:
            print(f'{qn5} nota(s) de 5.')
    if rn5 > 0:
        if qn1 > 0:
            print(f'{qn1} nota(s) de 1.')
else:
    print('Você deve sacar valor entre 10 e 600 reais.')
