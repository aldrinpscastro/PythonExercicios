def reverso(numero):
    numero = str(numero)
    numero = list(numero)
    numero.reverse()
    return ''.join(numero)
print(reverso(123456789))