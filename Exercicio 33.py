numero = int(input('Digite o Valor a ser sacado entre R$ 10,00 e R$ 600,00]: '))

cem = int(numero / 100)
numero = numero - (cem * 100)

cinquenta = int(numero / 50)
numero = numero - (cinquenta * 50)

dez = int(numero / 10)
numero = numero - (dez * 10)

cinco = int(numero / 5)
numero = numero - (cinco * 5)

um = numero

print('Notas R$100,00 = ', cem)
print('Notas R$ 50,00 = ', cinquenta)
print('Notas R$ 10,00 = ', dez)
print('Notas R$  5,00 = ', cinco)
print('Notas R$  1,00 = ', um)

