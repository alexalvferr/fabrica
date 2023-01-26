lista_num = []
lista_par = []
lista_impar = []
num = 0

print('Digite 20 Números Inteiros: ')
for i in range(20):
  lista_num.append(int(input('Número ' + str(i+1) + ': ')))
  num = lista_num[i]
  
  if num %2 == 0:
    lista_par.append(num)
  else:
    lista_impar.append(num)

print(f'Lista de Números: {lista_num}\n Lista Par: {lista_par}\n Lista Ímpar: {lista_impar}')
