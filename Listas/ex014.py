respostas = []
print('=== INTERRROGATÓRIO ===')
resposta = ' '
while resposta not in 'SN' or not resposta:
    resposta = input('\nTelefonou para à vítima? [S/N]: ').upper().strip()
    if resposta not in 'SN' or not resposta:
        print('Opção inválida! Tente novamente.')
respostas.append(resposta)
resposta = ' '
while resposta not in 'SN' or not resposta:
    resposta = input('Esteve no local do crime? [S/N]: ').upper().strip()
    if resposta not in 'SN' or not resposta:
        print('Opção inválida! Tente novamente.')
respostas.append(resposta)
resposta = ' '
while resposta not in 'SN' or not resposta:
    resposta = input('Mora perto da vítima? [S/N]: ').upper().strip()
    if resposta not in 'SN' or not resposta:
        print('Opção inválida! Tente novamente.')
respostas.append(resposta)
resposta = ' '
while resposta not in 'SN' or not resposta:
    resposta = input('Devia para à vítima? [S/N]: ').upper().strip()
    if resposta not in 'SN' or not resposta:
        print('Opção inválida! Tente novamente.')
respostas.append(resposta)
resposta = ' '
while resposta not in 'SN' or not resposta:
    resposta = input('Trabalhava com a vítima? [S/N]: ').upper().strip()
    if resposta not in 'SN' or not resposta:
        print('Opção inválida! Tente novamente.')
respostas.append(resposta)
if respostas.count('S') == 5:
    classificacao = '"Assassino"'
elif respostas.count('S') == 3 or respostas.count('S') == 4:
    classificacao = '"Cúmplice"'
elif respostas.count('S') == 2:
    classificacao = '"Suspeita"'
else:
    classificacao = '"Inocente"'
print(f'\nVocê é classificado como: {classificacao}')