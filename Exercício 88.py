print(38 * '#')
print('''\tnormal    - R$ 1,05 - 1
\texpresso  - R$ 1,52 - 2
\tcapuccino - R$ 2,17 - 3
\tmocaccino - R$ 2,36 - 4''')
print(38 * '#')
while True:
    cafe = int(input('Digite o númro do seu pedido: '))
    if cafe >= 1 and cafe <= 4:
        break
    else:
        print('Código inválido, por favor tente novamente!!\n')

match cafe:
    case 1:
        valor_cafe = 1.05

    case 2:
        valor_cafe = 1.52

    case 3:
        valor_cafe = 2.17

    case 4:
        valor_cafe = 2.36

while True:
    valor = float(input('Digite o valor você irá pagar R$ '))
    if valor >= valor_cafe:
        break
    else:
        print('\nValor digitado menor que valor do café selecionado')
        print('Digite um valor maior!!\n')


troco = valor - valor_cafe


num = valor - valor_cafe

real = num // 1.0
num = num - (real * 1.0)

m50 = num // 0.5
num = num - (m50 * 0.5)

m25 = num // 0.25
num = num - (m25 * 0.25)

m10 = num // 0.10
num = num - (m10 * 0.10)

m5 = num // 0.05
num = num - (m5 * 0.05)

m1 = num // 0.01

print(f'O valor do troco é de R$ {troco:.2f}')
print(f'Moedas de R$1 real = {real} ')
print(f'Moedas de R$0,50 centavos = {m50}')
print(f'Moedas de R$0,25 centavos = {m25}')
print(f'Moedas de R$0,10 centavos = {m10}')
print(f'Moedas de R$0,05 centavos = {m5}')
print(f'Moedas de R$0,01 centavos = {m1}')