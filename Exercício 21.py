sal_fixo = float(input('Digite o Salário Fixo R$: '))
vendas = float(input(('Digite o valor do Tota das Vendas do mês R$: ')))
comissao = vendas * 0.04
sal_total = sal_fixo + comissao
print(f'O seu Salário Fixo é de R$ {sal_fixo}\nSuas Vendas desse mês foram de R$ {vendas}\nSua Comissão foi de R$ {comissao:.2f}\nO Total do seu Salário é de R$ {sal_total:.2f}')