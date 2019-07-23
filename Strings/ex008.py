def reverso(texto):
    textoreverso = list(texto)
    textoreverso.reverse()
    textoreverso = ''.join(textoreverso)
    return textoreverso
def removeesppaco(texto):
    texto = str(texto).replace(' ', '')
    return texto
texto = removeesppaco(input('Digite uma frase: '))
textoreverso = reverso(removeesppaco(texto))
if texto == textoreverso:
    print('A frase que você digitou é um palíndromo.')
else:
    print('A frase que você digitou não é um palíndromo.')