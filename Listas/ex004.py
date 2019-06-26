letras = []
for i in range(0, 10):
    letra = input('Digite uma letra: ')
    letras.append(letra)
contar_consoantes = []
for i in letras:
    if i not in 'aeiou':
        contar_consoantes.append(i)
print(f'Foram lidas {len(contar_consoantes)} consoante(s).\nE as consoante(s) são: {contar_consoantes}')
