fatorial = int(input('Digite o número do qual deseja calcular o fatorial: '))
resulfatorial = fatorial
print(f'{fatorial}! =', f'{fatorial} ', end='')
for i in range(fatorial, 1, -1):
    print(f'x {i - 1}', end=' ')
    resulfatorial *= (i - 1)
print(f'= {resulfatorial}')
