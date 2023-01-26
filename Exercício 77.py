lista_caract = []
consoantes = 0
vogais = 0

print('Digite 10 caracteres: ')

for i in range(10):
  lista_caract.append((input('Caracter  ' + str(i+1) + ': ')))
  caract = lista_caract[i]
  if caract not in ('a' , 'b' , 'c' , 'd' , 'e'):
    consoantes += 1
  elif caract in ('a' , 'b' , 'c' , 'd' , 'e'):
    vogais += 1
  

print(lista_caract)
print(f'Foram digitados:\n {consoantes} consoantes e {vogais} vogais')
