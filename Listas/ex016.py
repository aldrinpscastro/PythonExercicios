salarios = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while True:
    vendasbrutas = float(input('Qual é o valor bruto das vendas? '))
    if vendasbrutas < 0:
        break
    total = vendasbrutas * 0.09 + 200
    indice = int(total // 100)
    salarios[indice] += 1
print('Quantidade de vendedores por salário:')
print('$200 - $299: ', salarios[2])
print('$300 - $399: ', salarios[3])
print('$400 - $499: ', salarios[4])
print('$500 - $599: ', salarios[5])
print('$600 - $699: ', salarios[6])
print('$600 - $799: ', salarios[7])
print('$900 - $899: ', salarios[8])
print('$900 - $999: ', salarios[9])
print('$1000 em diante: ', salarios[10])
