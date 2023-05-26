# Faça um programa que leia e valide as seguintes informações:Nome: maior que 3 caracteres;Idade: entre 0 e 150;Salário: maior que zero;Sexo: 'f' ou 'm';Estado Civil: 's', 'c', 'v', 'd';
import time 
name = str(input('Qual o seu nome? ')).capitalize()
year = int(input('Qual a sua idade? '))
salario = float(input('Qual é o seu salario? '))
sex = str(input('Qual o seu sexo? [M/F ]'))[0].upper().strip()
estate = str(input('Qual o seu estado civil? '))[0].upper().strip()
while True:
    print('---VERIFICANDO INFORMAÇÔES---')
    time.sleep(0.3)
    if len(name) < 3:
        print('\033[31mERRO! Nome curto demais. O nome deve conter mais de 3 caracteres.\033[m')
        name = str(input('Digite seu nome novamente: ')).capitalize()
    elif year >= 150:
        print('\033[31mERRO! Idade incorreta.\033[m')
        year = int(input('Digite sua idade novamente: '))
    elif salario <= 0:
        print('\033[31mERRO! Salario incorreto.\033[m')
        salario = float(input('Digite seu salario novamente: '))
    elif sex != 'M' and sex != 'F':
        print('\033[31mERRO! Sexo incorreto.\033[m')
        sex = str(input('Digite seu sexo novamente: '))[0].upper().strip()
    elif estate not in ['S', 'C', 'D', 'V']:
        print('\033[31mERRO! Estado civil digitado incorretamente.\033[m')
        estate = str(input('Digite seu estado civil novamente: '))[0].upper().strip()
    else:
        break
print(f'NOME: {name}\nIDADE: {year} anos\nSALARIO: R${salario:.2f}\nSEXO: {sex}\nESTADO CIVIL: {estate}')
    
