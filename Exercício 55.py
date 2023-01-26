quantidade = 0

while True:
    numero = int(input('Digita um número: '))
    if numero == -99:
        break
    quantidade = quantidade + 1
       
    if quantidade == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        

print(f'Você digitou {quantidade} números e o maior valor foi {maior} e o menor foi {menor}')

