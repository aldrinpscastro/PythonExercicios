ntermo = int(input('Até qual termo: '))
ii = 1
soma = 0
print('S = ', end='')
for i in range(1, ntermo + 1):
    soma += (i / ii)
    if i == ntermo:
        print(f'{i}/{ii}', end='')
    else:
        print(f'{i}/{ii} + ', end='')
    ii += 2
print(f' = {soma}')