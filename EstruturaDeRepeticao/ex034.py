numero = int(input('Digite um número: '))
for i in range(numero - 1, 1, -1):
    if numero % i == 0:
        eprimo = False
        break
    else:
        eprimo = True
if eprimo:
    simnao = 'Sim'
else:
    simnao = 'Não'
print(f'É primo? {simnao}.')
