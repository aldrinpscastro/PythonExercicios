def embaralhatexto(texto):
    from random import randint
    textoembaralhado = ''
    njaescolhido = []
    for i in range(0, len(texto)):
        numero = randint(0, len(texto) - 1)
        while numero in njaescolhido:
            numero = randint(0, len(texto) - 1)
        njaescolhido.append(numero)
        textoembaralhado += texto[numero]
    return textoembaralhado.upper()
print(embaralhatexto('Olá mundo'))