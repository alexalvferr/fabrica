p = 10.0
m = 12.0
g = 15.0
pedido_p = int(input('Digite a quantidade de camisetas tamanho P: '))
pedido_m = int(input('Digite a quantidade de camisetas tamanho M: '))
pedido_g = int(input('Digite a quantidade de camisetas tamanho G: '))
pedido_final = (pedido_p * p) + (pedido_m * m) + (pedido_g + g)
print("==" * 24)
print("**" * 6, "DETALHAMENTO DO PEDIDO", "**" * 6)
print(f'O seu pedido é:\n {pedido_p} unidades de Camisetas P\n {pedido_m} unidades de Camisetas M\n {pedido_g} unidades de Camisetas G\n')
print(f'O Valor Total do seu Pedido é de R$ {pedido_final:.2f}')
print("==" * 24)
