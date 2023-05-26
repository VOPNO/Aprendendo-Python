# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
país_a = int(input('Insira a população do País A: '))
crescimento_a = int(input('Insira a porcentagem de crescimento: '))
crescimento_a /= 100
país_b = int(input('Insira a população do País B: '))
crescimento_b = int(input('Insira a porcentagem de crescimento: '))
crescimento_b /= 100
anos = 0 
while país_a < país_b:
    país_a += país_a * crescimento_a
    país_b += país_b * crescimento_b
    anos += 1

print(f'Vai demorar {anos} anos para que a população do País A se iguale ou ultrapasse a população do País B. No final de {anos} anos a população do País A será de {país_a:.0f} habitantes e a do País B será {país_b:.0f} habitantes.')