situaçao = ['1 - necessita de esfera', '2 - necessita de limpeza', '3 - necessita troca de cabo ou conector', '4 - quebrado ou unitilizado']
quantidade = [0] * 4
print('CÓDIGO DE ERRO')
print('=' * 14)
for i in situaçao:
    print(i)
idmouse = -1
contarmouses = 0
while True:
    idmouse = int(input('\nQual é o nº de identificação do mouse: '))
    if idmouse <= 0:
        break
    contarmouses += 1
    opcao = int(input('Qual é o tipo de defeito? '))
    quantidade[opcao - 1] += 1
print(f'Quantidaded de mouses: {contarmouses}')
print(f'{"Situação":<41}{"Quantidade":^12}{"Percentual":^10}')
for i in range(0, len(situaçao)):
    print(f'{situaçao[i]:<41}{quantidade[i]:^12}{f"{quantidade[i]/sum(quantidade) * 100} %":^10}')