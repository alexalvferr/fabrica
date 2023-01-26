notas = []
media = 0
print ('Digite as 4 notas: ')
for i in range(4):
  notas.append(float(input('Nota ' + str(i+1) + ': ')))
  media += notas[i]
media = media/4
print (f'notas: {notas}')
print(f'media: {media:.2f}')