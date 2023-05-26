# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
n = int(input('Digite o número para saber sua tabuada: '))
for t in range(0, 10 + 1):
    print(f'{n} x {t} = {n * t}')