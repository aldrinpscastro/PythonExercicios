maisalto = 0
codmaisalto = 0
maisbaixo = 99
codmaisbaixo = 0
maisgordo = 0
codmaisgordo = 0
maismagro = 99
codmaismagro = 0
somaalturas = 0
somapesos = 0
contarcliente = 0
while True:
    codigo = str(input('Qual é o seu código? Digite 0 para encerrar.'))
    if codigo == 0:
        break
    altura = float(input('Qual é a sua altura? '))
    if altura > maisalto:
        maisalto = altura
        codmaisalto = codigo
    if altura < maisbaixo:
        maisbaixo = altura
        codmaisbaixo = codigo
    peso = float(input('Qual é o seu peso? '))
    if peso > maisgordo:
        maisgordo = peso
        codmaisgordo = codigo
    if peso < maismagro:
        maismagro = peso
        codmaismagro = codigo
    somaalturas += altura
    somapesos += peso
    contarcliente += 1
    print()
mediaaltura = somaalturas / contarcliente
mediapeso = somapesos / contarcliente
print(f'O cliente mais alto tem {maisalto}m. E seu código é {codmaisalto}.')
print(f'O cliente mais baixo tem {maisbaixo}m. E seu código é {codmaisbaixo}.')
print(f'O cliente mais gordo tem {maisgordo}Kg. E seu código é {codmaisgordo}.')
print(f'O cliente mais magro tem {maismagro}kg. E seu código é {codmaismagro}.')
print(f'A média de altura dos clientes é {mediaaltura:.2f}m.')
print(f'A média de peso dos clientes é {mediapeso:.2f}Kg.')
