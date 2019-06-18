numero = 0
entre0e25 = 0
entre26e50 = 0
entre51e75 = 0
entre76e100 = 0
while numero >= 0:
    numero = int(input('Digite um número: '))
    if numero >= 0 and numero <= 25:
        entre0e25 += 1
    if numero >= 26 and numero <=50:
        entre26e50 += 1
    if numero >= 51 and numero <= 75:
        entre51e75 += 1
    if numero >= 76 and numero <= 100:
        entre76e100 += 1
print(f'Quantidade de números digitados entre 0 e 25: {entre0e25}')
print(f'Quantidade de números digitados entre 26 e 50: {entre26e50}')
print(f'Quantidade de números digitados entre 51 e 75: {entre51e75}')
print(f'Quantidade de números digitados entre 76 e 100: {entre76e100}')