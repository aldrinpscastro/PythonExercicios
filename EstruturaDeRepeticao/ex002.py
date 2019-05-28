nomeusuario = ''
senha = ''
while nomeusuario == senha:
    nomeusuario = str(input('Digite seu nome de usuário: '))
    senha = str(input('Digite sua senha: '))
    if nomeusuario != senha:
        break
    print('ERRO! Usuário e senha iguais! Tente novamente.')
