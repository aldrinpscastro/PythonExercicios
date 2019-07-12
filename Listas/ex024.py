from random import randint
resultado = [0] * 6
for i in range(0, 100):
    resultado[randint(0, 5)] += 1
print('Resultado:')
for i in range(0, 6):
    print(f'Valor {i + 1}: {resultado[i]}')