alunomaisalto = 0
alunomaisbaixo = 9999
nalunomaisalto = 0
nalunomaisbaixo = 0
for i in range(1, 11, 1):
    naluno = int(input('Digite o número do aluno: '))
    altura = float(input('Digite a altura do aluno em centímetros: '))
    if altura > alunomaisalto:
        alunomaisalto = altura
        nalunomaisalto = naluno
    if altura < alunomaisbaixo:
        alunomaisbaixo = altura
        nalunomaisbaixo = naluno
print(f'O aluno mais tem {alunomaisalto}cm. E seu número é {nalunomaisalto}.')
print(f'O aluno mais baixo tem {alunomaisbaixo}cm. E seu número é {nalunomaisbaixo}.')