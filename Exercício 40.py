sal = 1200.0
c1 = 200.0
c2 = 120.0

total_contas = (c1 * 1.02) + (c2 * 1.02)
sal_liq = sal - total_contas

print(f'Foi descontado do salário do João o valor de R$ {total_contas:.2f}, restando para ele o total de R$ {sal_liq:.2f}')

