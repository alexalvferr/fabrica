impar = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == -999:
        break
    elif n % 2 != 0:
        n = impar
        impar = impar + 1

print("Quantidade de números ímpares digitados:", impar)
