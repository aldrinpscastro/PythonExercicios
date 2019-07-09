print('"Qual é o melhor Sistema Operacional para uso em servidores?"\nAs possíveis respostas são:\n')
print('1 para Windows Server\n2 para UNix\n3 para Linux\n4 para Netware\n5 para Mac OS\n6 para Outros\n')
votos = [0, 0, 0, 0, 0, 0, 0]
opcoes = ['', 'Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outros']
vopcoes = ['0', '1', '2', '3', '4', '5', '6']
while True:
    voto = ''
    while voto not in vopcoes or not voto:
        voto = str(input('Qual é o seu voto? 0 para sair. '))
        if voto not in vopcoes or not voto:
            print('Opção inválida! Tente Novamente.'.upper())
    if voto in '0':
        break
    if voto == '1':
        votos[1] += 1
    if voto == '2':
        votos[2] += 1
    if voto == '3':
        votos[3] += 1
    if voto == '4':
        votos[4] += 1
    if voto == '5':
        votos[5] += 1
    if voto == '6':
        votos[6] += 1
print('\nSistema Operacional      Votos   %')
print('-------------------      -----   ---')
for i in range(1, len(votos)):
    print(f'{opcoes[i]:<24}', f'{votos[i]:^6}', f'{f" {votos[i] / sum(votos) * 100:.0f} %":^4}')
print('-------------------      -----   ---')
print(f'{"Total":<26}', sum(votos))
print(f'\nO Sistema Operacional mais votado foi o {opcoes[votos.index(max(votos))]}, com {max(votos)} voto(s),'
      f' correspondendo a {votos[votos.index(max(votos))] / sum(votos) * 100:.0f}% dos votos.')
