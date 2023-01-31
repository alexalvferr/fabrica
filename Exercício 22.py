valor = float(input('Digite o valor do Produto R$: '))
desc = valor * 0.1
valor_final = valor - desc
print(f'Ovalor do produto é de R$ {valor}\nO desconto é de R$ {desc:.2f}\nO Valor Final do produto é R$ {valor_final:.2f}')