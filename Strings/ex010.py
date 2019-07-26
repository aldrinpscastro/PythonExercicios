zeroaquinze = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
             'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze']
vinteanoventa = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

numero = -1
while numero < 0 or numero > 99:
    numero = int(input('Digite um número de um a noventa e nove: '))
if numero >= 0 and numero <= 15:
    print(f'O número {numero} escrito por extenso é escrito como: {zeroaquinze[numero].upper()}')
elif numero >= 16 and numero <= 19:
    if numero == 18:
        print(f'O número {numero} escrito por extenso é escrito como: {zeroaquinze[numero - int(str(numero)[1])].upper()}{zeroaquinze[int(str(numero)[1])].upper()}')
    else:
        print(f'O número {numero} escrito por extenso é escrito como: {zeroaquinze[numero-int(str(numero)[1])].upper()}E{zeroaquinze[int(str(numero)[1])].upper()}')
elif numero % 10 == 0:
    print(f'O número {numero} escrito por extenso é escrito como: {vinteanoventa[int(str(numero)[0]) - 2].upper()}')
else:
    print(f'O número {numero} escrito por extenso é escrito como: {vinteanoventa[int(str(numero)[0]) - 2].upper()} E {zeroaquinze[int(str(numero)[1])].upper()}')
