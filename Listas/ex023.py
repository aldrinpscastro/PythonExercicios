from statistics import mean
def bytesparamegabytes(numero):
    numero = f'{numero / 1024 / 1024:.2f}'
    numero = numero.replace('.', ',')
    numero = f'{numero} MB'
    return numero
espacosutilizados = []
nomes = []
numero = ''
nome = ''
with open('../relatorio.txt', 'w') as ff:
    ff.write(f'{"ACME Inc.":<20}{"Uso de espaço em disco pelos usuários"}\n')
    ff.write('-' * 57 + '\n\n')
    ff.write(f'{"Nr.":<5}{"Usuário":^9}{"Espaço Utilizado":^18}{"% do uso":^10} \n\n')
    with open('../usuarios.txt', 'r') as f:
        for i in f.read():
            if i.isnumeric() or i == '\n':
                if i == '\n':
                    espacosutilizados.append(int(numero))
                    numero = ''
                numero += i
            if i.isalpha() or i == '\n':
                if i == '\n':
                    i = ''
                    nomes.append(nome)
                    nome = ''
                nome += i
    for i in range(0, len(nomes)):
        ff.write(f'{i + 1:<5}{nomes[i]:^9}{bytesparamegabytes(espacosutilizados[i]):^18}'
              f'{f"{espacosutilizados[i]/sum(espacosutilizados) * 100:.2f} %":^10}\n')
    ff.write(f'\nEspaço total ocupado: {bytesparamegabytes(sum(espacosutilizados))}\n')
    ff.write(f'Espaço médio utilizado: {bytesparamegabytes(mean(espacosutilizados))}\n')