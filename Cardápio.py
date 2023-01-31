cardapio = [['Cachorro Quente', 100, 11.2], ['Ovo Simples', 101, 8.3], ['Bauru com Ovo', 102, 11.5], ['Hambúrguer', 103, 16.2], ['Refrigeante', 201, 6.0], ['Suco', 202, 7.5], ['Água Mineral', 203, 4.7]]
cardapio.sort()

print("=" * 32)
print(" " * 12, "CARDÁPIO")
print("=" * 32)
for i, comida in enumerate(cardapio):
    print(f"{cardapio[i][1]} - {cardapio[i][0]} - R$ {cardapio[i][2]:.2f}")
    print("-" * 32)
print("=" * 32)

produtos = [cardapio[0][0], cardapio[1][0], cardapio[2][0], cardapio[3][0], cardapio[4][0], cardapio[5][0], cardapio[6][0]]
codigo = [cardapio[0][1], cardapio[1][1], cardapio[2][1], cardapio[3][1], cardapio[4][1], cardapio[5][1], cardapio[6][1]]
preco = [cardapio[0][2], cardapio[1][2], cardapio[2][2], cardapio[3][2], cardapio[4][2], cardapio[5][2], cardapio[6][2]]
qtdComprada = []
subTotal = []

for i, produto in enumerate(codigo):
    while True:
        try:
            qtdComprada.append(int(input(f'Quantidade de {codigo[i]}: ')))
            subTotal.append(preco[i] * qtdComprada[i])
            break
        except:
            print('ERRO! Digite um número inteiro')
total = sum(subTotal)

print("==" * 24)
print("**" * 6, "DETALHAMENTO DO PEDIDO", "**" * 6)
print("==" * 24)

for i, produto in enumerate(codigo):
    print(f'{codigo[i]}: {produtos[i]} : R$ {preco[i]:.2f} X {qtdComprada[i]} = R$ {subTotal[i]:.2f}')
    print("--" * 24)

print("==" * 24)
print("**" * 6, f'TOTAL A PAGAR: R$ {total:.2f}', "**" * 6)
print("==" * 24)