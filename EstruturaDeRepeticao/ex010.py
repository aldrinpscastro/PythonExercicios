num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
for i in range(num1 + 1, num2):
    if i == num2 - 1:
        print(i, end='')
    else:
        print(i, end=', ')