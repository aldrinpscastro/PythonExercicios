medias = []
for i in range(1, 11):
    media = 0
    for ii in range(0, 4):
        nota = float(input(f'Digita a nota do aluno {i}: '))
        media += nota
        if ii == 3:
            media /= 4
    medias.append(media)
contador = 0
for i in medias:
    if i >= 7:
        contador += 1
print(contador)