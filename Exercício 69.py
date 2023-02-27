num = int(input('Quantos numeros: '))
ini = int(input('Numero 1: '))
count = 1
soma = ini
media = soma / num

while count < num:
    count += 1
    i = int(input('Numero %d: ' % count))
    soma += i

print(f'A soma dos números é: {soma}')
print(f'A média dos números é {media:.2f} ')


