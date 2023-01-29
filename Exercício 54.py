num = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == 0:
        break
    elif n == 50:
        n = num
        num = num + 1

print(f"O número 50 foi digitado {num} vezes")
