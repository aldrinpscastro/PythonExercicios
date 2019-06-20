ntermo = int(input('Até qual termo: '))
ii = 1
soma = 0
print('H = ', end='')
for i in range(1, ntermo + 1):
    soma += (ii / i)
    if i == 1:
        print(f'{i} + ', end='')
    elif i == ntermo:
        print(f'{ii}/{i}', end='')
    else:
        print(f'{ii}/{i} + ', end='')
print(f' = {soma}')