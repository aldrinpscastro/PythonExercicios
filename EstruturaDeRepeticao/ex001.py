nota = -1
while nota < 0 or nota > 10 or not nota:
    nota = int(input('Digite uma nota entre 0 e 10: '))
    if nota >= 0 and nota <= 10:
        break
    print('Valor inválido.')
