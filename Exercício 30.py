peso = float(input("Digite o peso dos peixes em Kg: "))
if peso <= 50:
  print('Peso dentro da Cota, Sem Multa')
elif peso > 50:
  exc = peso - 50
  valor_multa = exc * 4
  print(f'O peso excedeu em {exc:.3f}Kg e a Multa é de R$ {valor_multa:.2f}')
  