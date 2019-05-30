num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
soma = 0
for i in range(num1, num2 + 1):
    soma += i
print(f'A soma entre os números {num1} e {num2} é {soma}.')