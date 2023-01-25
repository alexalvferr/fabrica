preco = float(input('Digite o valor do produto R$: '))
pag_avista = preco * 0.9
cred = preco * 0.95
duas_x = preco
tres_x = preco * 1.1

print(f'O produto custa R$ {preco:.2f}\nPagamento A Vista ou PIX custa R$ {pag_avista:.2f}\nPagamento A Vista no Cartão de Crédito custa R$ {cred:.2f}'
      f'\nPagamento em 02 vezes custa R$ {duas_x:.2f}\nPagamento em 03 vezes custa R$ {tres_x:.2f}')
