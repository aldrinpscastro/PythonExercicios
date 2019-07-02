from statistics import mean
temperaturas = []
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho'
         , 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')
for i in range(0, 12):
    temperaturas.append(float(input(f'Digite a média de temperatura do mês de {meses[i]}: ')))
print('\nMeses com temperatura acima da média anual:\n')
for i in range(0, 12):
    if temperaturas[i] > mean(temperaturas):
        print(f'{temperaturas[i]}º - {meses[i]}')
