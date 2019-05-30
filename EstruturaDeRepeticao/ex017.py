fatorial = int(input('Digite qual número para fazer o fatorial: '))
for i in range(fatorial, 0, -1):
    if i == 1:
        print(i, end=' = ')
    else:
        print(i,end=' x ')
    if i - 1 == 0:
        break
    else:
        fatorial *= i - 1
print(fatorial)
