n = int(input("Digite um numero de 1 a 10: "))

print(f'A Tabuada de {n}')
print(12*'#')
for i in range(1, 11):
  print(f'{n} X {i} = {n * i}')
print(12*'#') 