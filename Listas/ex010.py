pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
outros = [21, 43, 65, 87, 109, 1211, 1413, 1615, 1817, 2019]
paresmaisimpares = []
for i in range(0, 10):
    paresmaisimpares.append(impares[i])
    paresmaisimpares.append(pares[i])
    paresmaisimpares.append(outros[i])
print(paresmaisimpares)
