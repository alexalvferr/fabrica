from Ex_classes01 import Retangulo
import math

ret = Retangulo(0,0)
print('Digite a Base e a Altura do Retângulo: ')
ret.base = float(input('Digite o valor da Base: '))
ret.alt = float(input('Digite o valor da Altura: '))

print("Area: {:.2f}".format(ret.area()))
print("Perímetro: {:.2f}".format(ret.parimetro()))
print("Diagonal: {:.2f}".format(ret.diagonal()))

