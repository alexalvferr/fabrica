lista_num = []
soma = 0

print('Digite 5 Números Inteiros: ')
for i in range(5):
  lista_num.append(int(input('Número ' + str(i+1) + ': ')))
  num = lista_num[i]
  soma = soma + num
  print(f' A soma com o número anterior é: {soma}')
  num = lista_num[i]
  print(f'O último número digitado foi: {num}')

