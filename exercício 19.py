l1 = float(input("Digite o valor do primeiro lado do triângulo: "))
l2 = float(input("Digite o valor do segundo lado do triângulo: "))
l3 = float(input("Digite o valor do terceiro lado do triângulo: "))

if ((l1 + l2) > l3 or (l1 + l3) > l2 or (l2 + l3) > l1):
    print("É possível criar esse triângulo")

    if (l1 != l2) and (l1 != l3) and (l2 != l3):
        print("Esse triângulo é Escaleno")
    elif (l1 == l2) and (l1 != l3) and (l2 != l3):
        print("Esse triângulo é Isóceles")
    elif (l1 == l2) and (l1 == l2) and (l2 == l3):
        print("Esse triângulo é Equilátero")

elif (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1):
        print('Nao é possível criar esse triangulo')
