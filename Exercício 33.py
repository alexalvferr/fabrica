n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
op  = input('Digite + para Soma, - para Subtração, * para Multiplicação e / para Divisão:  ')

soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2

if op == '+':
  resultado = soma

elif op == '-':
  resultado = sub

elif op == '*':
  resultado = mult

elif op == '/':
  resultado = div

else:
  print('Digite uma opção válida')

print(f'O resultado da operação escolhida é: {resultado:.2f}')

if resultado % 2 == 0:
  print('O Resultado é um Número Par')
else:
  print('O Resultado é um Número Ímpar')
    
if resultado >= 0:
  print('O Resultado é um Número Positivo')
else:
  print('O Resultado é um Número Negativo')
    
if type(resultado) == int:
  print('O Resultado é um Número Inteiro')
else:
  print('O Resultado é um Número Decimal')
  
