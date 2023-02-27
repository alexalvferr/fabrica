import time

salario = float(input('Digite o salário R$  '))
financiamento = float(input('Digite o valor do financiamento desejado R$ '))

salMin = salario * 5
print('ANALIZANDO O SEU PEDIDO...')
time.sleep(3)
print('ANALIZANDO O SEU PEDIDO...')
time.sleep(2)
print('ANALIZANDO O SEU PEDIDO...')
time.sleep(1)

if financiamento <= salMin:
    print('Parabéns!!!\nSeu Financiamento Foi Aprovado!!')

else:
    print('Que Pena!!!\nO seu Financiamento Não Foi Aprovado!!')

print('Obrigado por nos consultar!')