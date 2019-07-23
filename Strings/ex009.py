from statistics import *
cpf = input('Digite seu CPF: ')
sdv1 = 0    # soma para verificar o 1º digito verificador.
sdv2 = 0    # soma para verificar o 2º digito verificador.
od = []     # Só os números do cpf
if len(cpf) == 14 and cpf[0:3].isdigit() and cpf[4:7].isdigit() and cpf[8:11].isdigit() and cpf[12:].isdigit() and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    cdv2 = 11   #Número de multiplcações para verificar o 2º dígito verificador.
    for i in cpf:
        if i.isdigit():
            od.append(int(i)) # Adiconando os números a lista od.
            if cdv2 == 1:
                break
            sdv2 += (int(i) * cdv2)
            cdv2 -= 1
    cdv1 = 10   #Número de multiplcações para verificar o 1º dígito verificador.
    for i in cpf:
        if i.isdigit():
            if cdv1 == 1:
                break
            sdv1 += (int(i) * cdv1)
            cdv1 -= 1
    rdsdv1 = sdv1 * 10 % 11     #Resto da divisão por 11 da multiplicação por 10 da soma para verificar o 1º digito verificador.
    rdsdv2 = sdv2 * 10 % 11     #Resto da divisão por 11 da multiplicação por 10 da soma para verificar o 2º digito verificador.
    if cpf[12] == str(rdsdv1) and cpf[13] == str(rdsdv2) and mean(od) != od[0]:
        print('É CPF válido.')
    else:
        print('Não é um CPF válido.')
else:
    print('Não é um CPF.')