data = str(input('Digite uma data no formato dd/mm/aaaa: '))
if len(data) == 10 and data[2] == '/' and data[5] == '/' and data[:1].isdigit() and data[3:4].isdigit() and data[6:].isdigit():
    print('É um formato de data dd/mm/aaaa')
else:
    print('Não é um formato de data dd/mm/aaaa')