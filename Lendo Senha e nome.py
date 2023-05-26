#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
name = str(input('Digite seu nome de usuário: '))
senha = input('Digite sua senha: ')
if name == '' or senha == '':
    print('\033[31mERRO! Deve haver dados validos em todos os campos.\033[m')
    exit()
while senha == name:
    print('\033[31mERRO! A senha deve ser diferente do nome de usuário.\033[m')
    senha = input('Digite sua senha: ')
    if senha != name:
        print('\033[32mSenha registrada! \033[m')
        break
print(f'Usuário: {name}\nSenha: {senha}')
