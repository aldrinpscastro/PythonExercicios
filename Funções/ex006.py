def converterHora(hora, minuto):
    if minuto < 10:
        minuto = '0' + str(minuto)
    if hora > 11 and hora != 24:
        if hora == 12:
            hora = hora
        else:
            hora -= 12
            if hora < 10:
                hora = '0' + str(hora)
        return f'{hora}:{minuto} P.M.'

    else:
        if hora == 0:
            hora = 12
        elif hora == 24:
            hora -= 12
        else:
            hora = hora
        if hora < 10:
            hora = '0' + str(hora)
        return f'{hora}:{minuto} A.M.'
opcao = 'S'
while opcao == 'S':
    hora = int(input('Informe o valor da hora: '))
    minuto = int(input('Informe o valor do minuto: '))
    print(converterHora(hora, minuto))
    opcao = input('Quer continuar? [S/N]').upper()