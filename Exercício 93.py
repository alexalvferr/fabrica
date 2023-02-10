temp_meses = []
meses = ['Janeiro', 'Fevereiro', 'Março','Abril',
    'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
    'Outubro', 'Novembro', 'Dezembro']

for i in range(12):
    print(f'\nMês de: {meses[i]}')
    media = temp_meses.append(float(input('Digite a temperatura média em °C: ')))

media_anual = sum(temp_meses) / 12
print('\n' * 1)
print(f'Média Anual de Temperatura: {media_anual:.1f}°C')
print('\n' * 1)
for i in range(12):
    if temp_meses[i] > media_anual:
        print(f'Temperatura a cima da média no mês: {meses[i]} com Temperatura de: {temp_meses[i]}')
        