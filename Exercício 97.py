print(''''Qual o veículo quer avaliar, dentre os informados abaixo:'

1- Fusca
2- Gol
3- Uno
4- Vectra
5- Peugeout
''')

veiculos = ['Fusca', 'Gol', 'UNO', 'Vectra', 'Peugeout']
consumo_carros = []

print('\nComparativo de Consumo de Combustível\n')

for i in range(5):
    print(f'veículo {i + 1}\nNome: {veiculos[i]}')
    km_litro = float(input('Km por litro: '))
    consumo_carros.append(km_litro)

print('\nRelatório Final')

for i in range(5):
    print(f'{i+1} - {veiculos[i]:<15} - {consumo_carros[i]:>6.1f} - {round(1000 / consumo_carros[i]):>5.1f} litros - R$ {round(1000 / consumo_carros[i]) * 2.25:.2f}')

ind_menor_consumo = consumo_carros.index(max(consumo_carros))
print('O menor consumo é o do ', veiculos[ind_menor_consumo])