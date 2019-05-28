nota1 = float(input('Digite a primeira nota bimestral: '))
nota2 = float(input('Digite a segunda nota bimestral: '))
nota3 = float(input('Digite a terceira nota bimestral: '))
nota4 = float(input('Digite a quarta nota bimestral: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
mediastr = ''
for i in str(media):
    if i == '.':
        i = ','
    mediastr += i
print(f'A média das notas é: {mediastr}.')
