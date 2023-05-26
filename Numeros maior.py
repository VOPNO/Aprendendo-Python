# Faça um programa que leia 5 números e informe o maior número.
print('VERIFICADOR DE NÚMERO MAIOR')
print('-=' * 10)
n_maior = 0
for c in range(1, 5 + 1):
    n = int(input(f'Insira o {c}º número: '))
    if n > n_maior:
        n_maior = n 
print(f'O numero maior é {n_maior}')