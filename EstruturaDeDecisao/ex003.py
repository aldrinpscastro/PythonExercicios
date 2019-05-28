letra = str(input('Digite uma letra: ')).upper()
if letra in 'FM':
    if letra == 'F':
        print('Você digitou a letra F.')
    else:
        print('Você digitou a letra M.')
else:
    print('A letra digitada não é F ou M.')
