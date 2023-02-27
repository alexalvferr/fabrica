soma = 0
nota_acima = 0
nota_abaixo = 0
notas = []
cont = 0 
while True:
    nota = float(input('Digite a nota: '))

    if nota == -1:
        break
    
    else:
        notas.append(nota)
        cont += 1
        soma += nota
        media = soma / cont
       
        if nota < 7:
            nota_abaixo += 1

for c in range(len(notas)):
    if notas[c] >= media:
        nota_acima +=1

print(50 * '-')
print(f'A quantidades de notas digitadas foi: {cont}')

print(50 * '-')
print('Notas em Ordem Crescente:')       
for c in range(len(notas)):
    print(f'{notas[c]}')

print(50 * '-')

notas.reverse()
print('Notas em Ordem Decrescente:')
for c in range(len(notas)):
    print(f'{notas[c]}')

print(50 * '-') 
print(f'A soma das notas da {soma}')
print(f'A média das notas da {media:.2f}')
print(f'Notas acima da media: {nota_acima}')
print(f'Notas abaixo abaixo: {nota_abaixo}')
print(50 * '-')