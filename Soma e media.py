#Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for c in range(1, 6):
    n = float(input(f'Insira o {c}º número: '))
    soma += n
media = soma / 5
print(f'A soma dos 5 número é {soma:.2f} e a media é {media:.2f}.')
    