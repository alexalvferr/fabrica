encontrado = 0
numeros = []
for c in range(3):
    numeros.append(int(input(f'Digite o número {c+1}: ')))
num = int(input('Número para verificar: '))
for c in range(len(numeros)):
    if num == numeros[c]:
        print(f'Encontrado na posição {c}')
    else:
        print('Não encontrado')
