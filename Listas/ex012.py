from statistics import mean
alturas = [1.65, 1.76, 1.8, 1.43, 1.76, 1.89]
idades = [15, 12, 14, 16, 13, 11]
contar = 0
for i in range(0, len(alturas)):
    if idades[i] > 13 and alturas[i] < round(mean(alturas), 3):
        print(idades[i], alturas[i])
        contar += 1
print(round(mean(alturas), 3))
print(contar)
