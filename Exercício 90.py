faixas_salarios = [
    [200,299],
    [300,399],
    [400,499],
    [500,599],
    [600,699], 
    [700,799],
    [800,899],
    [900,999]
    ]
quantidades = [0,0,0,0,0,0,0,0,0]

salarios = []
valor_vendas = True
while valor_vendas != 0:
    valor_vendas = float(input("\nDigite a valor das vendas: $ "))
    if valor_vendas == 0:
        break
    else:
        salario = (valor_vendas * 0.09) + 200
        print(f'R$ {salario:.2f}')
        if salario < 1000:
            for i in range(len(faixas_salarios)):
                if salario >= faixas_salarios[i][0] and salario < faixas_salarios[i][1]:
                    quantidades[i] += 1
        else:
            quantidades[8] += 1
print('\n' * 3)
for i in range(len(faixas_salarios)):
    print('Faixas de Salários:')
    print(f'Entre $ {faixas_salarios[i][0]:.2f} e R$ {faixas_salarios[i][1]:.2f}: {quantidades[i]}')
print(f'Salarios maiores que $1000: {quantidades[8]}')