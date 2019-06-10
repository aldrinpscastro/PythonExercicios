maiornacidentes = 0
cmaiornacidentes = 0
menornacidentes = 99999999999
cmenornacidentes = 0
somaveiculos = 0
somaacidentecidade2000 = 0
contacidademenos2000 = 0
for i in range(1, 6, 1):
    print(f'Cidade brasileira com código {i}.')
    nveiculo = int(input('Número de veículos de passeio (em 1999); '))
    nacidente = int(input('Número de acidentes de transito com vítimas: '))
    if nacidente > maiornacidentes:
        maiornacidentes = nacidente
        cmaiornacidentes = i
    if nacidente < menornacidentes:
        menornacidentes = nacidente
        cmenornacidentes = i
    if nveiculo < 2000:
        somaacidentecidade2000 += nacidente
        contacidademenos2000 += 1
    somaveiculos += nveiculo
mediaveiculos = somaveiculos / 5
print(f'\nO maior número de acidentes é de {maiornacidentes}, que pertence a cidade brasileira com código {cmaiornacidentes}.')
print(f'O menor número de acidentes é de {menornacidentes}, que pertence a cidade brasileira com código {cmenornacidentes}.')
print(f'A soma dos veículos de todas as cidade é {somaveiculos}.')
print(f'A média de veículos nas cinco cidades juntas é {mediaveiculos}.')
if contacidademenos2000 != 0:
    mediaveiculos2000 = somaacidentecidade2000 / contacidademenos2000
    print(f'A média de acidentes em cidade com menos de 2000 veículos é {mediaveiculos2000}.')
