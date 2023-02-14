'''a = b = c = d = e = f = g = h = i = 0
lista = [a, b, c, d, e, f, g, h, i]
while True:
    vendas = float(input("Informe o valor das vendas brutas do vendedor: R$")) #800    -  9% = 72
    for x in range (9):
        if 200 + 100*x > 200 + vendas*0.09 <= 299 + 100*x:
            lista[x] += 1
        elif vendas >= 200 + 100*x:
            lista[x] += 1
    if vendas == 0:
        break
print(lista)'''

salarios = []
count_faixa_salario = [0] * 9

for salario in salarios:
    i = (salario // 100) - 2
    i_max = len(count_faixa_salario) - 1
    i = min(i, i_max)
    count_faixa_salario [i] += 1
print(count_faixa_salario)