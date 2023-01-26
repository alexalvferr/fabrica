soma = 0
quantidade = 0
while True:
    n = int(input("Digite um número inteiro: "))
    if n == -999:
        break
    soma = soma + n
    quantidade = quantidade + 1
print("Quantidade de números digitados:", quantidade)
print("Soma: ", soma)

