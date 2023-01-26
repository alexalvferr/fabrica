lata = 0.35
gar = 0.6
pet = 2.0
l1 = int(input('Digite a quantidade latas do pedido: '))
g1 = int(input('Digite a quantidade garrafas do pedido: '))
p1 = int(input('Digite a quantidade pets do pedido: '))
qtd_total = (lata * l1) + (gar * g1) + (pet * p1)
print(f'O total de refrigerante pedido foi de {qtd_total:.2f} litros')
