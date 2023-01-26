idades = []
alturas = []

for i in range(1, 6):
    print('%dº Pessoa' %i)
    idade = int(input('Digite a idade: '))
    altura = float(input('Digite a altura: '))
    idades.append(idade)
    alturas.append(altura)

print('Alturas na Ordem Lida')
print(alturas)
print('Idades na Ordem Lida')
print(idades)

print('Alturas na Ordem Inversa')
print(alturas[::-1])
print('Idades na Ordem Inversa')
print(idades[::-1])

