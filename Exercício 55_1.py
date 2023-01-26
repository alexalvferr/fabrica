num = int(input('Digite um número: '))
menor = num
maior = num

for i in range(1,5):
    num = int(input('Digite outro número: '))
    if num < menor:
        menor = num
    if num > maior:
        maior = num

print(f'O menor número digitado foi: {menor}')
print(f'O maior número digitado foi: {maior}')
