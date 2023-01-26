nome = str(input("Digite o seu nome: "))
idade = float(input("Digite a sua idade: "))
if idade >= 0 and idade <= 2:
    print(f"Seu nome é: {nome} e é um Bebê")
elif idade >= 3 and idade <= 10:
    print(f"Seu nome é: {nome} e é uma Criança")
elif idade >= 11 and idade <= 21:
    print(f"Seu nome é: {nome} e é um Jovem")
elif idade >= 22 and idade <= 64:
    print(f"Seu nome é: {nome} e é um Adulto")
elif idade >= 65 and idade <= 100:
    print(f"Seu nome é: {nome} e é uma Idoso")
elif idade >100:
    print(f"Seu nome é: {nome} e é Muito Velhinho")
else:
    print("Digite uma idade válida")
