from re import match

n1 = float(input("Digite o Primeiro Número: "))
n2 = float(input("Digite o Segundo Número: "))

print('-' * 29)
print('--  Opções da Calculadora  --')
print('--          SOMA = +       --')
print('--      SUBTAÇÃO = -       --')
print('-- MULTIPLICAÇÃO = *       --')
print('--       DIVISÃO = /       --')
print('-' * 29)

op = input('Digite a operação desejada: ')

match(op):
    case '+':
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')

match(op):
    case '-':
        sub = n1 - n2
        print(f'{n1} - {n2} = {sub}')

match(op):
    case '*':
        mult = n1 + n2
        print(f'{n1} * {n2} = {mult}')

match(op):
    case '/':
        div = n1 / n2
        print(f'{n1} / {n2} = {div}')

