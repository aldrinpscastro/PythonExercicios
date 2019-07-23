data = input('Data de Nascimento: ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho'
         , 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
dia = data[:2]
mes = int(data[3:5])
ano = data[6:]
print(f'Você nasceu em {dia} de {meses[mes - 1]} de {ano}.')