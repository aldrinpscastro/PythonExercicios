nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    if media == 10:
        print('Aprovado com distinção.')
    else:
        print('Aprovado.')
else:
    print('Reprovado.')