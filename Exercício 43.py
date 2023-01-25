c1 = int(input('Digite a quantidade de moedas de R$ 0,01: '))
c5 = int(input('Digite a quantidade de moedas de R$ 0,05: '))
c10 = int(input('Digite a quantidade de moedas de R$ 0,10: '))
c25 = int(input('Digite a quantidade de moedas de R$ 0,25: '))
c50 = int(input('Digite a quantidade de moedas de R$ 0,50: '))
r1 = int(input('Digite a quantidade de moedas de R$ 1,00: '))

soma = ((c1 * 0.01) + (c5 * 0.05) + (c10 * 0.1) + (c25 * 0.25) + (c50 * 0.5) + r1)
print(f'O total economizado foi de R$ {soma}')
