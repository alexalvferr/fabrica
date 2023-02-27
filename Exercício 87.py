valor = 0
peso = float(input('Digite o peso da encomenda em Kg: '))

if   peso <= 0.5:
    valor = 1.1

elif peso > 0.5 and peso <= 2.0:
    valor = 2.20

elif peso > 2.0 and peso <= 10.0:
    valor = 3.70

elif peso > 10.0:
     valor = 5
     dif = (peso - 10.0)
     valorDif = dif * 3.8
     valor += valorDif
     
print(f'O valor pelo transporte da encomenda é R$ {valor:.2f}')