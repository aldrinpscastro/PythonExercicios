def dataporextenso(data):
    data = str(data)
    mesporextenso = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
                     'Outubro', 'Novembro', 'Dezembro']
    dia = data[0:2]
    mes = int(data[3:5])
    ano = data[6:]
    if len(data) == 10:
        return f'{dia} de {mesporextenso[mes - 1]} de {ano}'
    else:
        return False
print(dataporextenso('01/01/1994'))