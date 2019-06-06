qturmas = int(input('Digite a quantidade de turmas: '))
qturmas1 = qturmas
somaalunos = 0
while qturmas != 0:
    nalunos = 41
    while nalunos > 40 or nalunos < 0:
        nalunos = int(input(f'Digite a quantidade de alunos da turma {qturmas}: '))
        if nalunos > 40 or nalunos < 0:
            print('ERRO! A quantidade de alunos por turma não pode ser maior que 40 ou ser negativo.')
        else:
            somaalunos += nalunos
    qturmas -= 1
mediaalunoturma = somaalunos / qturmas1
print(f'A média de alunos por turma é de {mediaalunoturma} alunos por turma.')