pao = 1.0
broa = 3.5

vendas_pao = int(input('Digite a quantidade de pães vendidos: '))
vendas_broa = int(input('Digite a quantidade de broas vendidas: '))
total_pao = (pao * vendas_pao)
total_broa = (broa * vendas_broa)
venda_bruta = total_pao + total_broa
poupanca = venda_bruta * 0.1
venda_liquida = venda_bruta - poupanca

print(f'Foram vendidos {vendas_pao} o que rendeu R$ {total_pao:.2f}')
print(f'Foram vendidas {vendas_broa} o que rendeu R$ {total_broa:.2f}')
print(f'A venda bruta foi de R$ {venda_bruta:.2f},\n o valor depositado na poupança foi de R$ {poupanca:.2f},\n e o valor da venda liquida foi de R$ {venda_liquida:.2f}')
