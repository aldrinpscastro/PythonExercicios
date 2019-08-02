Ips = []
with open('../entrada.txt', 'r') as IPS:
    for ip in IPS:
        Ip = []
        numero = ''
        for c in range(0, len(ip) + 1):
            if c == 0:
                ip += '.'
            if ip[c] == '.':
                Ip.append(int(numero))
                numero = ''
            elif ip[c] == '\n':
                Ip.append(int(numero))
                Ips.append(Ip)
                Ip = []
            else:
                numero += ip[c]
with open('../saida.txt', 'w') as saida:
    Ips_validos = []
    Ips_invalidos = []
    for ip in Ips:
        for i in ip:
            if i > 255 or i < 0:
                if ip not in Ips_invalidos:
                    Ips_invalidos.append(ip)
        for i in ip:
            if i < 255 and i >= 0 and ip not in Ips_invalidos:
                if ip not in Ips_validos:
                    Ips_validos.append(ip)

    saida.write('[Endereços válidos:]\n')
    for ip in Ips_validos:
        for i in range(0, len(ip)):
            if i == len(ip) - 1:
                saida.write(f'{ip[i]}\n')
            else:
                saida.write(f'{ip[i]}.')
    saida.write('\n')
    saida.write('[Endereços inválidos:]\n')
    for ip in Ips_invalidos:
        for i in range(0, len(ip)):
            if i == len(ip) - 1:
                saida.write(f'{ip[i]}\n')
            else:
                saida.write(f'{ip[i]}.')