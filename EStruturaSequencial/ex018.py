tamanho = float(input('Digite o tamanho do arquivo em MB: '))
link = float(input('Digite a velocidade do link em Mbps: ')) / 8
tempodownload = tamanho / link / 60
resto = int((tempodownload - int(tempodownload)) / (1 / 60))
if tempodownload < 1:
    print(f'O tempo de download será de aproximadamente {resto} segundo(s).')
else:
    print(f'O tempo de download será de aproximadamente {int(tempodownload)} minutos(s) e {resto} segundo(s).')
