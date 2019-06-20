numero = str(input('Digite um número inteiro: '))
numeroinvertido = ''
for i in range(len(numero) - 1, -1, -1):
    numeroinvertido += numero[i]
int(numeroinvertido)
print(numeroinvertido)
