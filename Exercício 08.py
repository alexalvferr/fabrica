distancia = float(input("Qual a distância a pecorrer: "))
consumo = float(input("Qual o consumo do veículo: "))
valor_combustivel = 4.75
valor_estadia = 110.55  
valor_alimento = 85.35
gasto_combustivel = (distancia/consumo) * valor_combustivel
custo_total = valor_estadia + valor_alimento + gasto_combustivel
print("Qual a distância a percorrer: \n", distancia, "km")
print("Qual o consumo do veículo: \n", consumo, "km/l")
print(valor_combustivel)
print(valor_estadia)
print(valor_alimento)
print(f"A distância da viagem é de {distancia} km, com consumo de {consumo} km/l, gastando R$ {valor_combustivel} por litro de gasolina ")
print(f"Vou gastar R$ {gasto_combustivel:.2f} com gasolina")
print(f"O valor da diária do hotel é de R$ {valor_estadia}, a estimativa de gasto com alimentação é de R$ {valor_alimento}")
print(f"o custo total da viagem será de R$ {custo_total:.2f}")