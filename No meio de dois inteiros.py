# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
n1 = int(input('Insira o 1º número: '))
n2 = int(input('Insira o 2º número: '))
soma = 0
for c in range(n1, n2 + 1):
    soma += c
    print(c, end=',')
print(f'\nA soma dos números exibidos é {soma}')