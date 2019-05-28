numero = int(input('Digite um número menor que 1000: '))
if numero > 0 and numero < 1000:
    centena = numero // 100
    dezena = (numero - numero // 100 * 100) // 10
    unidade = (numero - numero // 100 * 100) % 10
    textoc = 'centena'
    textod = 'dezena'
    textou = 'unidade'
    if centena > 1:
        textoc += 's'
    if dezena > 1:
        textod += 's'
    if unidade > 1:
        textou += 's'
    if centena == 0 and dezena > 0 and unidade > 0:
        print(f'{dezena} {textod} e {unidade} {textou}.')
    elif centena == 0 and dezena == 0 and unidade > 0:
        print(f'{unidade} {textou}.')
    else:
        print(f'{centena} {textoc}, {dezena} {textod} e {unidade} {textou}.')

else:
    print('O número digitado é maior que 1000 ou menor que 1.')
