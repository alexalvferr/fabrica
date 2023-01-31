valor_compra = float(input('Digite o valor de compra do item R$: '))
if valor_compra < 50:
    valor_venda = valor_compra * 1.45
else:
    valor_venda = valor_compra * 1.30
lucro = valor_venda - valor_compra
print(f'O valor de venda do item é de R$ {valor_venda:.2f}, com lucro de R$ {lucro:.2f}')