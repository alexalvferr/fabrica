c1 = 0 
c2 = 0 
c3 = 0
c4 = 0
vb = 0
vn = 0 
voto = 0

while True:

  voto = int(input("Digite a opção desejada de 1 a 6: "))
  if voto <= 0 and voto >= 7:
    break

  elif voto == 1: 
    c1 = c1 + 1
  elif voto == 2: 
    c2 = c2 + 1
  elif voto == 3: 
    c3 = c3 + 1
  elif voto == 4: 
    c4 = c4 + 1
  elif voto == 5: 
    vb = vb + 1
  elif voto == 6: 
    vn = vn + 1


print(f'O Candidato c1 teve {c1} votos')  
print(f'O Candidato c2 teve {c2} votos')
print(f'O Candidato c3 teve {c3} votos')
print(f'O Candidato c4 teve {c4} votos')
print(f'{vb} votos em branco')
print(f'{vn} votos nulos')