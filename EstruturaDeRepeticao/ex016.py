primeiro = 0
segundo = 1
print(primeiro, end=' ')
while segundo < 500:
    print(segundo, end=' ')
    terceiro = primeiro + segundo
    primeiro = segundo
    segundo = terceiro
