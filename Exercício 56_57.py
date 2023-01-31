qtd_livros = int(input('Digite a Quantidade de Livros comprados: '))
ponto0 = 0
ponto1 = 5
ponto2 = 15
ponto3 = 30
ponto4 = 60

if qtd_livros == 1:
  print(f'Você ganhou {ponto1} pontos')
elif qtd_livros == 2:
  print(f'Você ganhou {ponto2} pontos')
elif qtd_livros == 3:
  print(f'Você ganhou {ponto3} pontos')
elif qtd_livros >= 2:
  print(f'Você ganhou {ponto4} pontos')
else:
  print(f'Você ganhou {ponto0} pontos')