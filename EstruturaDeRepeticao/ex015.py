termo = int(input('Digite até qual termo a série de fibonacci irá: '))
primeiro = 0
segundo = 1
print(primeiro, end=' ')
for i in range(1, termo):
    print(segundo, end=' ')
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
